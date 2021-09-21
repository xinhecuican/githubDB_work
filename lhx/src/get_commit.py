import requests
import json
import csv
import re
from bs4 import BeautifulSoup
from common import getHTML


# 我们目前只爬一页，之后的再说
def get_commit(user_name, repo_name, branch_name, repo_id):
    url = 'https://github.com/' + user_name + '/' + repo_name + '/commits/' + branch_name
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    all_commits = soup.find('div', class_='js-navigation-container js-active-navigation-container mt-3')
    each_date_commit = all_commits.find_all('li', class_='Box-row Box-row--focus-gray mt-0 d-flex js-commits-list-item js-navigation-item js-details-container Details js-socket-channel js-updatable-content')

    # 对于每次提交的详细信息
    for i in range(len(each_date_commit)):
        commit_sha = each_date_commit[i].get('data-url').split('/')[4]
        short_id = commit_sha[:7]
        comi_url_api = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/commits/' + commit_sha
        comi_html_api = getHTML(comi_url_api)
        comi_js = json.loads(comi_html_api)

        parents = comi_js['parents']
        parent_commit = parents[0]['sha'][:7]

        author_user_id = comi_js['author']['id']
        commit_user_id = comi_js['committer']['id']
        commit_date = comi_js['commit']['committer']['date']
        message = comi_js['commit']['message']
        # TODO: contributors

        add_line_num = comi_js['stats']['additions']
        del_line_num = comi_js['stats']['deletions']
        change_files = comi_js['files']
        change_file_num = len(change_files)
        for each in range(change_file_num):

            file_path = change_files[each]['filename']
            file_name = file_path.rpartition('/')[2]
            file_type = change_files[each]['filename'].partition('.')[2]
            if file_type == '':
                file_type = file_name # 比如Makefile
            file_id = change_files[each]['sha'][:7]
            file_action = change_files[each]['status']
            # file_path =
            print([file_path, file_name, file_type, file_id, file_action])



get_commit('tonybaloney', 'wily', 'master')