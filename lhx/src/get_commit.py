import re
import time
import json
from bs4 import BeautifulSoup
from common import getHTML, get_repo_id, save_sth, trans_date_format, save_file, get_user_id


def get_commit(user_name, repo_name, branch_name, have_had_commit, nick_login):
    print('已进入', repo_name, '的', branch_name, '分支')
    url = 'https://github.com/' + user_name + '/' + repo_name + '/commits/' + branch_name
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    repo_id = get_repo_id(user_name, repo_name)

    all_commits = soup.find('div', class_='js-navigation-container js-active-navigation-container mt-3')
    each_date_commit = all_commits.find_all('li',
                                            class_='Box-row Box-row--focus-gray mt-0 d-flex js-commits-list-item '
                                                   'js-navigation-item js-details-container Details js-socket-channel '
                                                   'js-updatable-content')

    # NEW 10.2 添加所有页面
    next_link = soup.find('a', attrs={'rel': 'nofollow', 'class': 'btn btn-outline BtnGroup-item'})
    while next_link is not None:
        next_page_url = next_link.get('href')
        next_page_html = getHTML(next_page_url)
        next_page_soup = BeautifulSoup(next_page_html, 'html.parser')
        next_page_commits = next_page_soup.find('div', class_='js-navigation-container js-active-navigation-container mt-3').find_all('li',
                                            class_='Box-row Box-row--focus-gray mt-0 d-flex js-commits-list-item '
                                                   'js-navigation-item js-details-container Details js-socket-channel '
                                                   'js-updatable-content')
        each_date_commit = each_date_commit + next_page_commits  # 两个list拼接
        next_link = next_page_soup.find_all('a', attrs={'rel': 'nofollow', 'class': 'btn btn-outline BtnGroup-item'})
        temp_nl = None
        for i in range(len(next_link)):
            if next_link[i].text == 'Older':
                temp_nl = next_link[i]
        next_link = temp_nl
    # NEW END 此时each_date_commit包含所有commit


    # https://github.com/xinhecuican/githubDB_work/commits/master?before=62423802a3e629f2c738dca9201b1540b6dda8f1+35&branch=master
    # 对于每次提交的详细信息 / 单个commit
    for i in range(len(each_date_commit)-1, -1, -1):
        commit_sha = each_date_commit[i].get('data-url').split('/')[4]
        # NEW 10.2 避免重复
        if commit_sha in have_had_commit:
            print('sha', commit_sha, '已存在')
            continue
        have_had_commit.append(commit_sha)
        # NEW END
        comi_url_api = 'https://api.github.com/repos/' + user_name + '/' + repo_name + '/commits/' + commit_sha
        comi_html_api = getHTML(comi_url_api)
        comi_js = json.loads(comi_html_api)

        parents = comi_js['parents']
        try:
            parent_commit = parents[0]['sha'][:7]
        except:
            parent_commit = ''
        '''
        try:
            author_user_id = comi_js['author']['id']
        except TypeError as e:
            print(repo_name, '的提交', commit_sha, '没有author的id')
            author_user_id = ''
          
        try:
            commit_user_id = comi_js['committer']['id']
            i2 = nick_login[comi_js['commit']['committer']['name']]
        except TypeError as e:
            print(repo_name, '的提交', commit_sha, '没有commiter的id')
            commit_user_id = ''
        '''
        if comi_js['author'] is None:
            try:
                a2 = nick_login[comi_js['commit']['author']['name']]
                author_user_id = get_user_id(a2)
            except:
                author_user_id = ''
        else:
             author_user_id = comi_js['author']['id']
        print('author_user_id:', author_user_id)
        if comi_js['committer'] is None:
            try:
                i2 = nick_login[comi_js['commit']['committer']['name']]
                commit_user_id = get_user_id(i2)
            except:
                commit_user_id = ''
        else:
            commit_user_id = comi_js['committer']['id']
        print('commit_user_id:', commit_user_id)


        commit_date = comi_js['commit']['committer']['date']
        message = comi_js['commit']['message']

        add_line_num = comi_js['stats']['additions']
        del_line_num = comi_js['stats']['deletions']
        change_files = comi_js['files']
        change_file_num = len(change_files)
        change_file_names = []  # 一个提交的所有改变文件


        all_adddel_lines = get_all_adddel_lines(user_name, repo_name, commit_sha)
        all_add_lines = all_adddel_lines[0]
        all_del_lines = all_adddel_lines[1]
        all_add_lines_index = 0
        all_del_lines_index = 0

        single_commit = [commit_sha, parent_commit, repo_id, author_user_id, commit_user_id, trans_date_format(commit_date, 1), message]
        save_sth(single_commit, 'commits', 0)
        print('[commits]: ', single_commit)

        # NEW: 9.28 添加一个commit的所有comment
        try:
            comi_comm_url_api = comi_url_api + '/comments'
            commit_comment = get_commit_comment(comi_comm_url_api) # 给commit_files表使用
        except:
            commit_comment = [] # 可能根本没有评论


        # NEW: 10.3 改变 commit_file_info 表
        single_commit_file_info = [commit_sha[:7], '', add_line_num, del_line_num, change_file_num]
        save_sth(single_commit_file_info, 'commit_file_info', 0)
        print('[commit_file_info]: ', single_commit_file_info)
        # NEW END

        # NEW: 10.3 获取 file_line
        url = 'https://github.com/' + user_name + '/' + repo_name + '/commit/' + commit_sha
        html = getHTML(url)
        soup = BeautifulSoup(html, 'html.parser')
        file_line_dic = {}
        file_line_re = re.compile(r'file js-file js-details-container js-targetable-element Details.*')
        all_files = soup.find_all('div', class_=file_line_re)
        for i in range(len(all_files)):
            f_name = all_files[i].find('a', class_='Link--primary').text
            try: # add的最后一行
                ad = all_files[i].find_all('td', class_='blob-num blob-num-addition js-linkable-line-number')
                addl = int(ad[-1].get('data-line-number'))
            except:
                addl = 0
            try: # 非add的最后一行
                nad = all_files[i].find_all('td', class_='blob-num blob-num-context js-linkable-line-number')
                nadl = int(nad[-1].get('data-line-number'))
            except:
                nadl = 0
            one_file_line = max(addl, nadl)
            file_line_dic[f_name] = one_file_line
        # NEW END

        for each in range(change_file_num):  # 一个提交的每个改变文件

            file_path = change_files[each]['filename']
            file_name = file_path.rpartition('/')[2]

            change_file_names.append(file_name)

            file_type = change_files[each]['filename'].rpartition('.')[2]
            if file_type == 'jpg' or file_type == 'png' or file_type == 'svg' or file_type == 'zip' or file_type == 'pdf':
                continue

            if file_type == '':
                file_type = file_name  # 比如Makefile
            file_id = change_files[each]['sha'][:7]

            act_map = {'added': '0', 'modified': '1', 'removed': '2', 'renamed': '3'}
            file_action = change_files[each]['status']
            file_action_num = act_map[file_action]
            # 若 status = removed 则 有行数量，但无具体行数值
            # 即file_additions != 0, 但all_add_lines中为空


            file_add_lines = []
            file_del_lines = []
            file_additions = change_files[each]['additions']  # 行数量
            file_deletions = change_files[each]['deletions']
            file_changes_line_num = change_files[each]['changes']  # 等于上面两个相加
            '''
            for i in range(int(file_additions)):
                if file_action == 'modified' or file_action == 'renamed' or file_action == 'added':
                    try:
                        file_add_lines.append(all_add_lines[all_add_lines_index])
                    except:
                        pass

                all_add_lines_index += 1
            for i in range(int(file_deletions)):
                if file_action == 'modified' or file_action == 'renamed' or file_action == 'added':
                    try:
                        file_del_lines.append(all_del_lines[all_del_lines_index])
                    except:
                        pass  # 理由同上
                all_del_lines_index += 1
            '''


            # commit_file_info表
            '''
            commit_directory_address = ''
            single_commit_file_info = [file_id, commit_directory_address, file_type, file_additions, file_deletions,
                                       file_changes_line_num]
            save_sth(single_commit_file_info, 'commit_file_info', 0)
            print('[commit_file_info]: ', single_commit_file_info)
            '''

            # NEW 10.2 added文件的爬取
            if file_action == 'added':
                path = r'D:\\21-22-1\\Database_Practice2\\files\\' + user_name + r'\\' + repo_name + r'\\' + commit_sha[:7]
                real_link = 'https://raw.githubusercontent.com/' + user_name + '/' + repo_name + '/' + commit_sha + '/' + file_path
                r_html = getHTML(real_link)
                save_file(path, r_html, file_path)
            # NEW END

            try:
                file_line = file_line_dic[file_name]
            except:
                file_line = 0
            single_commit_files = [commit_sha[:7], commit_comment, file_name, file_type, file_action_num, file_line, file_additions, file_deletions, file_path]

            save_sth(single_commit_files, 'commit_files', 0)
            print('[commit_files]: ', single_commit_files)
            time.sleep(0.5)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_all_adddel_lines(user_name, repo_name, sha):
    url = 'https://github.com/' + user_name + '/' + repo_name + '/commit/' + sha
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    add_lines = []
    del_lines = []
    all_add_lines = soup.find_all('td', class_='blob-num blob-num-addition js-linkable-line-number')
    all_del_lines = soup.find_all('td', class_='blob-num blob-num-deletion js-linkable-line-number')
    for i in range(len(all_add_lines)):
        add_lines.append(all_add_lines[i].get('data-line-number'))  # 增加行
    for i in range(len(all_del_lines)):
        del_lines.append(all_del_lines[i].get('data-line-number'))  # 删除行
    # print([add_lines, del_lines])
    return [add_lines, del_lines]

def get_commit_comment(url): # 传入的是api url
    html = getHTML(url)
    js = json.loads(html)
    res_comment = []
    for i in range(len(js)):
        commid_id = js[i]['commit_id'][:7]
        quota_id = js[i]['id']
        comment_date = trans_date_format(js[i]['created_at'], 1)
        comment_content = js[i]['body']
        res_comment.append(comment_content)

        each_comment = [commid_id, quota_id, comment_date, comment_content]
        save_sth(each_comment, 'commit_comment', 0)
        print('[commit_comment]: ', each_comment)
    return res_comment


# get_commit_comment('https://api.github.com/repos/xinhecuican/githubDB_work/commits/1d497a92a7a84a8a16cda830d0aa3319da74994e/comments')
# get_all_adddel_lines('tonybaloney', 'wily' , 'e1bcd8dcc1823da3c1d9e4670e68550ac8ac5f77')
# a = []
# get_commit('NavaneethDhruvsoft', 'bw-xero-devdocs', 'gh-pages', a)