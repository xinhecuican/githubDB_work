import requests
import json
import csv
import re
from bs4 import BeautifulSoup
from common import getHTML


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
        package_num = 0 # TODO: 没见过0+的

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
            # comments = soup.find('div', class_='p-note user-profile-bio mb-3 js-user-profile-bio f4').get('data-bio-text')
            comments = js_res['bio']
        except:
            comments = None
        try:
            # link = soup.find('a', rel='nofollow me').get('href')
            link = js_res['blog']
        except:
            link = None
        avatar_url = soup.find('a', itemprop='image').get('href')

        single_user_description = [id, user_name, nick_name, status, company, location, comments, link, avatar_url]
        print(single_user_description)
        # end user_description---------------------------------------------------------------

        # start follwers TODO: 目前每人爬30个
        followers_url = js_res['followers_url']
        followers_html = getHTML(followers_url)
        f_res = json.loads(followers_html)
        followers_list = []
        for i in range(len(f_res)):
            followers_list.append([f_res[i]['id'], id])
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
        print('[repository]: ', single_repository)
        # end repository---------------------------------------------------------------

        # start repository_info---------------------------------------------------------------
        # id = id
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
        print('[contriburtors]: ', contributors)
        # end repository_info---------------------------------------------------------------

        # start licenses---------------------------------------------------------------
        licenses_name_d = js_res[i]['license']
        if licenses_name_d != None:
            licenses_name = licenses_name_d['name']
            print('[licenses_name]: ', licenses_name)
        else:
            licenses_name = None

        licenses_content_url_d = js_res[i]['license']
        try:
            licenses_content_url = licenses_content_url_d['url']
            licenses_content = get_licenses_content(licenses_content_url)
        except:
            licenses_content = None

        # 获得id
        licenses_url = 'https://github.com/' + user_name + '/' + name + '/blob/' + default_branch + '/LICENSE'
        print(licenses_url)
        lic_url = getHTML(licenses_url)
        try:
            lic_bs = BeautifulSoup(lic_url, 'html.parser')
            licenses_id = lic_bs.find('a', class_='https://github.com/tonybaloney/wily/blob/master/LICENSE').text
            print(['[licenses]: ', id, description, licenses_id, tags, code_type, contributors])
        except:
            print('no licenses')
        # end licenses---------------------------------------------------------------

        # start issue---------------------------------------------------------------
        get_issue(user_name, name, id)
        # end issue---------------------------------------------------------------

        # start branch-----------------------------------------------------------
        get_branches(user_name, name)
        # end branch-------------------------------------------------------------


def get_issue(user_name, name, repo_id): # 处理issue issue_comment labels
    url = 'https://github.com/' + user_name + '/' + name + '/issues'
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    # start issue 1--------------------------------------------------------------
    # 目前是open部分
    issue_ids = soup.find_all('div', class_='Box-row Box-row--focus-gray p-0 mt-0 js-navigation-item js-issue-row')
    for i in range(len(issue_ids)):
        issue_id = issue_ids[i].get('id').partition('_')[2]
        url = 'https://api.github.com/repos/' + user_name + '/' + name + '/issues/' + issue_id
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
        question = issue_js['title']
        single_issue = [issue_id, creator_id, labels, status, create_date, comments_sum, question]
        print('[issue]: ', single_issue)
        # end issue 1------------------------------------------------------------

        # 接下来获取单个issue下所有相关信息
        # start issue_comment---------------------------------------------------
        # 0类型
        # user_id = creator_id
        creator_name = issue_js['user']['login']
        action0 = '0'
        # create_date = create_date
        create_content = issue_js['body']

        # 1类型
        comment_api_url = 'https://api.github.com/repos/' + user_name + '/' + name + '/issues/' + issue_id + '/comments'
        comment_html = getHTML(comment_api_url)
        comment_js = json.loads(comment_html)

        for i in range(len(comment_js)): # 此处是评论类comment
            quota_id = comment_js[i]['id']
            commentator_id = comment_js[i]['user']['id']
            commentator_name = comment_js[i]['user']['login']
            action1 = '1'
            comment_date = comment_js[i]['created_at']
            comment_content = comment_js[i]['body']
        comment_url = comment_js['html_url'] # FIXME: ERROR

        # 2类型
        # label_creator = user_name
        get_label_comment(comment_url)
        # end issue_comment------------------------------------------------------

        # start labels----------------------------------------------------------
        label_js = issue_js['labels']
        for i in range(len(label_js)):
            label_url = label_js[i]['url']
            label_name = label_js[i]['name']
            label_color = label_js[i]['color']
            single_label = [label_url, label_name, label_color]
            print('[label]: ', single_label)
        # end labels------------------------------------------------------------


def get_branches(user_name, repo_name):
    url = 'https://github.com/' + user_name + '/' + repo_name + '/branches'
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    all_b = soup.find_all('branch-filter-item') # 需要get('branch')
    for i in range(len(all_b)): # 对于每个分支
        each_url = 'https://github.com/' + user_name + '/' + repo_name + '/tree/' + all_b[i].get('branch')
        each_html = getHTML(each_url)
        each_soup = BeautifulSoup(each_html, 'html.parser')
        commit_num = each_soup.find('a', class_='pl-3 pr-3 py-3 p-md-0 mt-n3 mb-n3 mr-n3 m-md-0 Link--primary no-underline no-wrap').find('strong').text
        single_branch = [all_b[i].get('branch'), commit_num]
        print('[branch]: ', single_branch)
# -------------------------------------------------------------------------------------------------------------------
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

def get_label_comment(url):
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    label_infos = soup.find_all('div', class_='TimelineItem-body')
    for i in range(len(label_infos)): # 以每次添加为单位
        if label_infos[i].find('a', class_='IssueLabel hx_IssueLabel d-inline-block v-align-middle') is not None:
            each_labels = []
            each_content = []
            temp = label_infos[i].find_all('a', class_='IssueLabel hx_IssueLabel d-inline-block v-align-middle')
            for j in range(len(temp)): # 此处获取一次添加的所有标签
                each_labels.append(temp[j].text) # 标签名
                try:
                    each_content.append(temp[j].get('title')) # 标签内容
                except:
                    each_labels.append('')
            time = label_infos[i].find('a', class_='Link--secondary').text
            single_label_comment = [each_labels, each_content, time]
            print('[label_comment]: ', single_label_comment)
# ---------------------------------------------------------------------------------------------------------------------
def save_sth(list, fname):
    path = r'D:\\21-22-1\\Database_Practice1\\' + fname + '.csv'
    with open(path, 'a+') as f:
        writer = csv.writer(f)
        writer.writerows(list)
# ---------------------------------------------------------------------------------------------------------------------


get_user_info('bollnh')
# get_user_info('antsmartian')
# get_user_info('tonybaloney')