import json
import csv
import re
from bs4 import BeautifulSoup
from common import getHTML, save_sth, trans_date_format
from get_tags import get_tags
from get_commit import get_commit


def get_user_info(user_name):
    url1 = 'https://api.github.com/users/' + user_name
    url2 = 'https://github.com/' + user_name
    html1 = getHTML(url1)
    html2 = getHTML(url2)
    js_res = json.loads(html1)
    soup = BeautifulSoup(html2, 'html.parser')

    # 我们只爬user
    if js_res['type'] == 'User':
        # start user_info
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
        save_sth(single_user_info, 'user_info', 0)

        # start user_description
        nick_name = js_res['name']
        try:
            status = str(soup.find('div', class_='user-status-message-wrapper f6 color-text-primary no-wrap').find('div')).replace('<div>', '').replace('</div>', '')
        except:
            status = ''
        try:
            company = js_res['company'].replace(r'\n', '').replace(r'\r', '')
        except:
            company = ''
        try:
            location = js_res['location']
        except:
            location = ''
        try:
            comments = js_res['bio']
        except:
            comments = ''
        try:
            link = js_res['blog']
        except:
            link = ''
        avatar_url = soup.find('a', itemprop='image').get('href')

        single_user_description = [id, user_name, nick_name, status, company, location, comments, link, avatar_url]
        print(single_user_description)
        save_sth(single_user_description, 'user_description', 0)

        # start follwers
        followers_url = js_res['followers_url']
        followers_html = getHTML(followers_url)
        f_res = json.loads(followers_html)
        followers_list = []
        for i in range(len(f_res)):
            followers_list.append([f_res[i]['id'], id])
        print(followers_list)
        save_sth(followers_list, 'followers', 1)
        # TODO: 爬大于30个

        # start repository
        get_repo_info(user_name, id)
    else:
        pass


def get_repo_info(user_name, user_id):
    url1 = 'https://api.github.com/users/' + user_name + '/repos'
    html1 = getHTML(url1)
    js_res = json.loads(html1)

    for i in range(len(js_res)): # 对于每个repo 以下每个 i 是一个repo
        # start repository
        id = js_res[i]['id']
        fname = js_res[i]['full_name']
        name = js_res[i]['name']
        create_date = js_res[i]['created_at']
        visibility = True
        default_branch = js_res[i]['default_branch']
        watch_num = js_res[i]['watchers_count']
        star_num = js_res[i]['stargazers_count']
        fork_num = js_res[i]['forks_count'] # 该值爬了别人fork你的，不是总fork
        con_url = js_res[i]['contributors_url']
        con_html = getHTML(con_url)
        try:
            con_js = json.loads(con_html)
        except:
            con_js = []
        contributor_num = len(con_js) # TODO: 直接爬页面，大于30个

        single_repository = [id, user_id, fname, trans_date_format(create_date, 1), visibility, default_branch, contributor_num, watch_num, star_num, fork_num]
        save_sth(single_repository, 'repository', 0)
        print('[repository]: ', single_repository)

        # start repository_info
        description = js_res[i]['description']
        temp_url = 'https://github.com/' + user_name + '/' + name
        temp_html = getHTML(temp_url)
        tags = get_this_tags(temp_html)
        code_type = get_code_type(temp_html)
        contributors = []
        for i in range(len(con_js)):
            contributors.append(con_js[i]['login'])

        licenses_url = 'https://github.com/' + user_name + '/' + name + '/blob/' + default_branch + '/LICENSE'
        lic_url = getHTML(licenses_url)
        try:
            lic_bs = BeautifulSoup(lic_url, 'html.parser')
            licenses_id = lic_bs.find('a', class_='https://github.com/tonybaloney/wily/blob/master/LICENSE').text
        except:
            licenses_id = ''

        # NEW
        temp_soup = BeautifulSoup(temp_html, 'html.parser')
        hreff = '/' + user_name + '/' + name + '/releases'
        try:
            release_num = temp_soup.find('a', href=hreff).find('span').get('title')
        except:
            release_num = 0


        single_repository_info = [id, description, '', licenses_id, tags, code_type, contributors, release_num]
        save_sth(single_repository_info, 'repository_info', 0)
        print('[repo_info]: ', single_repository_info)

        # start issue
        # get_issue(user_name, name, id)

        # start branch
        # get_branches(user_name, name, id, default_branch)


def get_issue(user_name, name, repo_id):
    url = 'https://github.com/' + user_name + '/' + name + '/issues'
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    # start issue
    # TODO: 目前只有open部分 差close部分
    issue_ids = soup.find_all('div', class_='Box-row Box-row--focus-gray p-0 mt-0 js-navigation-item js-issue-row')
    for i in range(len(issue_ids)): # 一个repo下的每一个issue
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

        single_issue = [repo_id, creator_id, labels, status, trans_date_format(create_date, 1), comments_sum, question]
        save_sth(single_issue, 'issue', 0)
        print('[issue]: ', single_issue)

        # 接下来获取单个issue下 comment
        # start issue_comment
        # ----- 新建 -----
        creator_name = issue_js['user']['login']
        action0 = '0'
        create_content = issue_js['body']

        single_issue_comm_0 = [issue_id, 0, creator_id, creator_name, action0, create_date, create_content]
        save_sth(single_issue_comm_0, 'issue_comment', 0)
        print('[issue_comment]: ', single_issue_comm_0)

        # ----- 评论 -----
        comment_api_url = 'https://api.github.com/repos/' + user_name + '/' + name + '/issues/' + issue_id + '/comments'
        comment_html = getHTML(comment_api_url)
        comment_js = json.loads(comment_html)

        for i in range(len(comment_js)):
            quota_id = comment_js[i]['id']
            commentator_id = comment_js[i]['user']['id']
            commentator_name = comment_js[i]['user']['login']
            action1 = '1'
            comment_date = comment_js[i]['created_at']
            comment_content = comment_js[i]['body']

            single_issue_comm_1 = [issue_id, quota_id, commentator_id, commentator_name, action1, comment_date, comment_content]
            save_sth(single_issue_comm_1, 'issue_comment', 0)
            print('[issue_comment]: ', single_issue_comm_1)

        # ----- 增加label -----
        try:
            get_label_comment(url, repo_id)
        except:
            print('获取label型comment失败！！！！！！！！')

        # ----- 关闭 -----
        # TODO: issue_comment 关闭类型


        # start labels
        label_js = issue_js['labels']
        for i in range(len(label_js)):
            label_url = label_js[i]['url']
            label_name = label_js[i]['name']
            label_color = label_js[i]['color']

            single_label = [repo_id, label_url, label_name, label_color]
            save_sth(single_label, 'labels', 0)
            print('[label]: ', single_label)


def get_branches(user_name, repo_name, repo_id, default_branch):
    url = 'https://github.com/' + user_name + '/' + repo_name + '/branches'
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    all_b = soup.find_all('branch-filter-item') # 需要get('branch')
    for i in range(len(all_b)): # 对于每个分支
        each_url = 'https://github.com/' + user_name + '/' + repo_name + '/tree/' + all_b[i].get('branch')
        each_html = getHTML(each_url)
        each_soup = BeautifulSoup(each_html, 'html.parser')
        commit_num = each_soup.find('a', class_='pl-3 pr-3 py-3 p-md-0 mt-n3 mb-n3 mr-n3 m-md-0 Link--primary no-underline no-wrap').find('strong').text
        last_commit = each_soup.find('a', class_='d-none js-permalink-shortcut').get('href').rpartition('/')[2][:7]

        single_branch = [all_b[i].get('branch'), repo_id, last_commit, commit_num]
        save_sth(single_branch, 'branches', 0)
        print('[branch]: ', single_branch)

        get_commit(user_name, repo_name, all_b[i].get('branch'))

    get_tags(user_name, repo_name, repo_id, default_branch, last_commit)

# -------------------------------------------------------------------------------------------------------------------
def get_this_tags(temp_html):
    res = []
    tag_bs4 = BeautifulSoup(temp_html, 'html.parser')
    tag = tag_bs4.find_all('a', attrs={'data-ga-click': 'Topic, repository page'})
    for i in range(len(tag)):
        temp = tag[i].get('data-octo-dimensions').partition(':')[2]
        res.append(temp)
    # if res != []:
        # print(res)
    return res

def get_code_type(temp_html):
    dict = {}
    types = re.findall(r'aria-label="\w* \d+.\d*?"', str(temp_html))
    for i in range(len(types)):
        par = types[i].partition('="')[2][:-1].partition(" ")
        dict[par[0]] = par[2]
    # if dict != {}:
        # print(dict)
    return dict

def get_licenses_content(l_url):
    html = getHTML(l_url)
    res = ''
    js_l = json.loads(html)
    res = js_l['body']
    return res

def get_label_comment(url, repo_id):
    html = getHTML(url)
    js = json.loads(html)

    url1 = url + '/timeline'
    html1 = getHTML(url1)
    js1 = json.loads(html1)

    labels_name = []
    labels_description = []
    labels_date = []
    labels_info = []
    # 分成两部分 一部分从 timeline 中获取创建时间
    # 另一部分从  中获取labels描述

    # 第一部分
    all_labels = js['labels']
    for i in range(len(all_labels)):
        labels_name.append(all_labels[i]['name'])
        labels_description.append(all_labels[i]['description'])
    # 第二部分
    for i in range(len(js1)):
        if js1[i]['event'] == 'labeled':
            labels_date.append(js1[i]['created_at'])

    # 将一二部分合起来
    for i in range(len(labels_name)):
        each = [repo_id, labels_name[i], labels_description[i], trans_date_format(labels_date[i], 1)]
        labels_info.append(each)
        print('[each_label]: ', each)
'''
    label_infos = soup.find_all('div', class_='TimelineItem-body')
    print('已进入: ', len(label_infos))
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
            single_label_comment = [repo_id, each_labels, each_content, time]
            print('[label_comment]: ', single_label_comment)
            '''
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# get_user_info('liuyib')
# get_user_info('xinhecuican')
# get_user_info('antsmartian')
# get_user_info('tonybaloney')