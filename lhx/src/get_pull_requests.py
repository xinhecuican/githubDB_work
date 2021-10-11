import requests
import json
import csv
import re
from bs4 import BeautifulSoup
from common import getHTML, save_sth, get_user_id

# TODO: CLOSE 部分
# pull_request
def get_open_pulls(user_name, repo_name, repo_id):
    url = 'https://github.com/' + user_name + '/' + repo_name + '/pulls' # 网页
    html = getHTML(url)
    try:
        soup = BeautifulSoup(html, 'html.parser')
    except TypeError:
        print('仓库', repo_name, '没有open pull')
        return

    all_question = soup.find_all('div', class_='flex-auto min-width-0 p-2 pr-3 pr-md-2')
    # each问题
    for each in range(len(all_question)):
        q_id = all_question[each].find('span', class_='opened-by').text.split()[0][1:]
        each_url_api = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/pulls/' + q_id
        each_html = getHTML(each_url_api)
        each_js = json.loads(each_html)

        base_branch = each_js['base']['ref']
        from_branch = each_js['head']['ref']
        is_open = True
        merge_status = each_js['merged']
        suc_status = all_question[each].find('a', class_='color-text-success tooltipped tooltipped-e')
        if suc_status is not []:
            check_status = True
        else:
            check_status = False

        pull_id = each_js['id']
        try:
            link_pull_request_id = each_js['user']['id']
        except:
            link_pull_request_id = ''
        try:
            labelss = each_js['labels']
            labels = []
            for j in range(len(labelss)):
                labels.append(labelss[j]['name'])
        except:
            labels = []
        # milestone = each_js['milestone']


        related_commit = []
        related_commit_url = each_js['commits_url']
        related_commit_html = getHTML(related_commit_url)
        related_commit_js = json.loads(related_commit_html)
        for j in range(len(related_commit_js)):
            related_commit.append(related_commit_js[j]['sha'][:7])

        # 保存部分
        single_pull_request = [repo_id, q_id, base_branch, from_branch, related_commit, is_open, merge_status, check_status]
        save_sth(single_pull_request, 'pull_request', 0)
        print('[pull_request]: ', single_pull_request)

        single_pull_info = [pull_id, q_id, labels, '', '', link_pull_request_id]
        save_sth(single_pull_info, 'pull_request_info', 0)
        print('[pull_request_info]: ', single_pull_info)

        # 每个问题下的每个动作--普通评论
        each_comm_url_api = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/issues/' + q_id + '/comments'
        each_comm_html_api = getHTML(each_comm_url_api)
        each_comm_js = json.loads(each_comm_html_api)
        for i in range(len(each_comm_js)):
            user_id = each_comm_js[i]['user']['id']
            # comment_id = each_comm_js[i]['id']
            comment = each_comm_js[i]['body']
            action = 0

            single_pull_act_0 = [q_id, user_id, comment, action]
            save_sth(single_pull_act_0, 'pull_request_action', 0)
            print('[pull_request_action]: ', single_pull_act_0)

        # 每个问题下的每个动作--commit
        each_comi_url_api = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/issues/' + q_id + '/commits'
        each_comi_html_api = getHTML(each_comi_url_api)
        try:
            each_comi_js = json.loads(each_comi_html_api)
            for i in range(len(each_comi_html_api)):
                user_id = get_user_id(each_comi_js[i]['committer']['name'])
                comment = each_comi_js[i]['message']
                action = 1

                single_pull_act_1 = [q_id, user_id, comment, action]
                save_sth(single_pull_act_1, 'pull_request_action', 0)
                print('[pull_request_action]: ', single_pull_act_1)
        except:
            pass

        # 每个问题下的每个动作--review
        each_revw_url_api = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/pulls/' + q_id + '/comments'
        each_revw_html_api = getHTML(each_revw_url_api)
        each_revw_js = json.loads(each_revw_html_api)
        for i in range(len(each_revw_js)):
            user_id = each_revw_js[i]['user']['id']
            comment = each_revw_js[i]['body']
            action = 2

            single_pull_act_2 = [q_id, user_id, comment, action]
            save_sth(single_pull_act_2, 'pull_request_action', 0)
            print('[pull_request_action]: ', single_pull_act_2)


'''

def get_pull_request_info_label(user_name, repo_name): # 返回list类型 label
    url = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/labels'
    html = getHTML(url)
    js = json.loads(html)
    res_label = []
    for i in range(len(js)):
        res_label.append(js[i]['name'])
    return res_label
'''

# get_open_pulls('dependabot', 'dependabot-core', '93163073')