import requests
import json
import csv
import re
from bs4 import BeautifulSoup
# from lhx.src.version2 import getHTML

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

# pull_request
def get_open_pulls(user_name, repo_name):
    url = 'https://github.com/' + user_name + '/' + repo_name + '/pulls' # 网页
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    all_question = soup.find_all('div', class_='flex-auto min-width-0 p-2 pr-3 pr-md-2')
    # each问题
    for each in range(len(all_question)):
        q_id = all_question[each].find('span', class_='opened-by').text.split()[0][1:]
        each_url_api = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/pulls/' + q_id # api
        print(each_url_api)
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

        assignees = each_js['assignees'] # TODO
        labels = each_js['labels']
        milestone = each_js['milestone']

        print([q_id, base_branch, from_branch, is_open, merge_status, check_status])

        # 每个问题下的每个动作--普通评论
        each_comm_url_api = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/issues/' + q_id + '/comments'
        each_comm_html_api = getHTML(each_comm_url_api)
        each_comm_js = json.loads(each_comm_html_api)
        for i in range(len(each_comm_js)):
            user_id = each_comm_js[i]['user']['id']
            # comment_id = each_comm_js[i]['id']
            comment = each_comm_js[i]['body']
            action = 0

        # 每个问题下的每个动作--commit
        each_comi_url_api = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/issues/' + q_id + '/commits'
        each_comi_html_api = getHTML(each_comi_url_api)
        each_comi_js = json.loads(each_comi_html_api)
        for i in range(len(each_comi_html_api)):
            user_id = each_comi_js[i]['committer']['name'] # TODO: 名字->id
            comment = each_comi_js[i]['message']
            action = 1

        # 每个问题下的每个动作--review
        each_revw_url_api = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/pulls/' + q_id + '/comments'
        each_revw_html_api = getHTML(each_revw_url_api)
        each_revw_js = json.loads(each_revw_html_api)
        for i in range(len(each_revw_js)):
            user_id = each_revw_js[i]['user']['id']
            comment = each_revw_js[i]['body']
            action = 2


# get_open_pulls('log4cplus', 'log4cplus')