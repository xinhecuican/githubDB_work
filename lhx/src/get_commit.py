import time
import requests
import json
import csv
import re
from bs4 import BeautifulSoup
from common import getHTML, get_repo_id, save_sth


# 我们目前只爬一页，之后的再说
def get_commit(user_name, repo_name, branch_name):
    url = 'https://github.com/' + user_name + '/' + repo_name + '/commits/' + branch_name
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    repo_id = get_repo_id(user_name, repo_name)

    all_commits = soup.find('div', class_='js-navigation-container js-active-navigation-container mt-3')
    each_date_commit = all_commits.find_all('li', class_='Box-row Box-row--focus-gray mt-0 d-flex js-commits-list-item js-navigation-item js-details-container Details js-socket-channel js-updatable-content')

    # 对于每次提交的详细信息
    for i in range(len(each_date_commit)):
        commit_sha = each_date_commit[i].get('data-url').split('/')[4]
        short_id = commit_sha[:7]
        comi_url_api = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/commits/' + commit_sha
        # print(comi_url_api)
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
        change_file_names = [] # 一个提交的所有改变文件
        each_temp = []

        # new
        all_adddel_lines = get_all_adddel_lines(user_name, repo_name, commit_sha)
        all_add_lines = all_adddel_lines[0]
        all_del_lines = all_adddel_lines[1]
        all_add_lines_index = 0
        all_del_lines_index = 0
        # print(len(all_add_lines), len(all_del_lines))

        contributors = [] # TODO
        single_commit = [commit_sha, parent_commit, repo_id, author_user_id, commit_user_id, commit_date, message, contributors]
        save_sth(single_commit, 'commits', 0)
        print('[commits]: ', single_commit)
        # end new

        for each in range(change_file_num): # 一个提交的每个改变文件

            file_path = change_files[each]['filename']
            file_name = file_path.rpartition('/')[2]

            change_file_names.append(file_name)

            file_type = change_files[each]['filename'].rpartition('.')[2]
            if file_type == '':
                file_type = file_name # 比如Makefile
            file_id = change_files[each]['sha'][:7]

            act_map = {'added': '0', 'modified': '1', 'removed': '2', 'renamed': '3'}
            file_action = change_files[each]['status']
            file_action_num = act_map[file_action]
            # 若 status = removed 则 有行数量，但无具体行数值
            # 即file_additions != 0, 但all_add_lines中为空


            # new
            file_add_lines = []
            file_del_lines = []
            file_additions = change_files[each]['additions'] # 行数量
            file_deletions = change_files[each]['deletions']
            for i in range(int(file_additions)):
                if file_action == 'modified' or file_action == 'renamed' or file_action == 'added':
                    try:
                        file_add_lines.append(all_add_lines[all_add_lines_index])
                    except:
                        pass # 由于爬取的页面长度有限，对于长度夸张的commit没法全爬出来，上百个lines的话只能爬一部分
                             # 或许吧
                all_add_lines_index += 1
            for i in range(int(file_deletions)):
                if  file_action == 'modified' or file_action == 'renamed' or file_action == 'added':
                    try:
                        file_del_lines.append(all_del_lines[all_del_lines_index])
                    except:
                        pass # 理由同上
                all_del_lines_index += 1
            # end new

            # print('[add]: ', file_add_lines, ' [add_lines]:', all_add_lines_index)
            # print('[del]: ', file_del_lines, ' [del_lines]:', all_del_lines_index)

            each_temp.append([file_path, file_name, file_type, file_id, file_action])
            # print([commit_sha,parent_commit, repo_id, file_path, file_name, file_type, file_id, file_action])
            print('-----------------------------------------------------------')
            time.sleep(1)

def get_all_adddel_lines(user_name, repo_name, sha):
    url = 'https://github.com/' + user_name + '/' + repo_name + '/commit/' + sha
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    add_lines = []
    del_lines = []
    all_add_lines = soup.find_all('td', class_='blob-num blob-num-addition js-linkable-line-number')
    all_del_lines = soup.find_all('td', class_='blob-num blob-num-deletion js-linkable-line-number')
    for i in range(len(all_add_lines)):
        add_lines.append(all_add_lines[i].get('data-line-number')) # 增加行
    for i in range(len(all_del_lines)):
        del_lines.append(all_del_lines[i].get('data-line-number')) # 删除行
    # print([add_lines, del_lines])
    return [add_lines, del_lines]

# get_commit('tonybaloney', 'wily', 'master')
# get_all_adddel_lines('tonybaloney', 'wily' , 'e1bcd8dcc1823da3c1d9e4670e68550ac8ac5f77')