import requests
import json
import re
from bs4 import BeautifulSoup


def getHTML(url):
    headers =  {
        'User-Agent': 'Mozilla/5.0',
        'Authorization': 'token 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',
        'Content-Type': 'application/json',
        'method': 'GET',
        'Accept': 'application/json'
    }
    if 'api' in url:
        r = requests.get(url, timeout=30, headers=headers)
    else:
        r = requests.get(url, timeout=30)
    try:
        if r.status_code == 200:
            return r.text
    except:
        print('conn failed')
        return None


# 处理 user_info, user_description, followers表
def get_user_info(user_name):
    url1 = 'https://api.github.com/users/' + user_name
    url2 = 'https://github.com/' + user_name
    html1 = getHTML(url1)
    html2 = getHTML(url2)
    js_res = json.loads(html1)
    soup = BeautifulSoup(html2, 'html.parser')

    # 我们只爬user
    if js_res['type'] == 'User':
        # start user_info---------------------------------------------------------------
        id = js_res['id']
        password = ''
        email = js_res['email']
        follower_num = js_res['followers']
        following_num = js_res['following']
        star_num = soup.find_all('span', class_='text-bold color-text-primary')[2].text
        repo_num = soup.find_all('span', class_='Counter')[0].text
        proj_num = soup.find_all('span', class_='Counter')[1].text
        package_num = 0

        single_user_info = [id, user_name, password, email, follower_num, following_num, star_num, proj_num, repo_num, package_num]
        print(single_user_info)
        # end user_info---------------------------------------------------------------

        # start user_description---------------------------------------------------------------
        nick_name = js_res['name']
        try:
            status = str(soup.find('div', class_='user-status-message-wrapper f6 color-text-primary no-wrap').find('div')).replace('<div>', '').replace('</div>', '')
        except:
            status = None
        try:
            company = js_res['company'].replace(r'\n', '').replace(r'\r', '')
        except:
            company = None
        try:
            location = js_res['location']
        except:
            location = None
        try:
            comments = soup.find('div', class_='p-note user-profile-bio mb-3 js-user-profile-bio f4').get('data-bio-text')
        except:
            comments = None
        try:
            link = soup.find('a', rel='nofollow me').get('href')
        except:
            link = None
        avatar_url = soup.find('a', itemprop='image').get('href')

        single_user_description = [id, user_name, nick_name, status, company, location, comments, link, avatar_url]
        print(single_user_description)
        # end user_description---------------------------------------------------------------

        # start follwers TODO: 修改成最新格式---------------------------------------------------------------
        # 对于每个人只爬30个follower, 目前采用[被follow，follow者]格式
        followers_url = js_res['followers_url']
        followers_html = getHTML(followers_url)
        f_res = json.loads(followers_html)
        followers_list = []
        for i in range(len(f_res)):
            followers_list.append([id, f_res[i]['id']])
        print(followers_list)
        # end followers---------------------------------------------------------------

        # start repository---------------------------------------------------------------
        get_repo_info(user_name, id)
        # end repository---------------------------------------------------------------
    else:
        pass


# 处理 repository, repository_info, licenses
def get_repo_info(user_name, user_id):
    url1 = 'https://api.github.com/users/' + user_name + '/repos'
    html1 = getHTML(url1)
    js_res = json.loads(html1)

    for i in range(len(js_res)): # 对于每个repo 以下针对的全都是一个项目
        # start repository---------------------------------------------------------------
        id = js_res[i]['id'] # FIXME: 目前存疑
        fname = js_res[i]['full_name']
        name = js_res[i]['name']
        create_date = js_res[i]['created_at']
        visibility = True
        default_branch = js_res[i]['default_branch']
        watch_num = js_res[i]['watchers_count']
        star_num = js_res[i]['stargazers_count']
        fork_num = js_res[i]['forks_count'] # 该值爬了别人fork你的，不是总fork
        # 这里只爬30个contributor 大于30也写30
        con_url = js_res[i]['contributors_url']
        con_html = getHTML(con_url)
        con_js = json.loads(con_html)
        contributor_num = len(con_js)

        single_repository = [id, user_id, fname, create_date, visibility, default_branch, contributor_num, watch_num, star_num, fork_num]
        print(single_repository)
        # end repository---------------------------------------------------------------

        # start repository_info---------------------------------------------------------------
        # id = id FIXME: 存疑
        description = js_res[i]['description']
        # website TODO: 是啥
        # licenses_id TODO: 是啥
        temp_url = 'https://github.com/' + user_name + '/' + name
        temp_html = getHTML(temp_url)
        tags = get_tags(temp_html)
        code_type = get_code_type(temp_html)
        contributors = []
        for i in range(len(con_js)):
            contributors.append(con_js[i]['login'])
        # end repository_info---------------------------------------------------------------

        # start licenses---------------------------------------------------------------
        licenses_name_d = js_res[i]['license']
        if licenses_name_d != None:
            licenses_name = licenses_name_d['name']
            print(licenses_name)
        else:
            licenses_name = None

        licenses_content_url_d = js_res[i]['license']
        try:
            licenses_content_url = licenses_content_url_d['url']
            licenses_content = get_licenses_content(licenses_content_url)
        except:
            licenses_content = None
        # end licenses---------------------------------------------------------------

        # start issue---------------------------------------------------------------
        get_issue(user_name, name, id)
        # end issue---------------------------------------------------------------


def get_issue(user_name, name, repo_id): # 处理issue
    url = 'https://github.com/' + user_name + '/' + name + '/issues'
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    issue_nums = soup.find_all('div', class_='Box-row Box-row--focus-gray p-0 mt-0 js-navigation-item js-issue-row')
    for i in range(len(issue_nums)):
        issue_num = issue_nums[i].get('id').partition('_')[2]
        url = 'https://api.github.com/repos/' + user_name + '/' + name + '/issues/' + issue_num
        html = getHTML(url)
        issue_js = json.loads(html)
        creator_id = issue_js['user']['id']
        labels = []
        label_d = issue_js['labels']
        for j in range(len(label_d)):
            labels.append(label_d[j]['name'])
        status = 'open'
        create_date = issue_js['created_at']
        comments_sum = issue_js['comments']
        question = issue_js['body']

# ---------------------------------------------------------------------------------------------------------------------
def get_tags(temp_html):
    res = []
    tag_bs4 = BeautifulSoup(temp_html, 'html.parser')
    tag = tag_bs4.find_all('a', attrs={'data-ga-click': 'Topic, repository page'})
    for i in range(len(tag)):
        temp = tag[i].get('data-octo-dimensions').partition(':')[2]
        res.append(temp)
    if res != []:
        print(res)
    return res

def get_code_type(temp_html):
    dict = {}
    types = re.findall(r'aria-label="\w* \d+.\d*?"', str(temp_html))
    for i in range(len(types)):
        par = types[i].partition('="')[2][:-1].partition(" ")
        dict[par[0]] = par[2]
    if dict != {}:
        print(dict)
    return dict

def get_licenses_content(l_url):
    html = getHTML(l_url)
    res = ''
    js_l = json.loads(html)
    res = js_l['body']
    return res
# ---------------------------------------------------------------------------------------------------------------------



# get_user_info('bollnh')
# get_user_info('antsmartian')
get_user_info('mysqlboy')