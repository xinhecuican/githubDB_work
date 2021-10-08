import threading
import json
import time
import math
from version2 import get_user_info, get_issue, get_branches
from get_activity import get_activity
from get_pull_requests import get_open_pulls
from common import getHTML


# from common import get_user_id

def get_all(user_name):
    nick_login = {}
    get_user_info(user_name, nick_login)
    print('[nick_login]: ', nick_login)
    # 包括 user_info followers description repository repository_info tags tag_files
    get_activity(user_name)
    # 包括 activity
    a_repos = get_user_all_repos(user_name)
    for i in range(len(a_repos)):
        get_issue(user_name, a_repos[i][0], a_repos[i][1])
        # 包括 issue issue_comment labels
        get_open_pulls(user_name, a_repos[i][0], a_repos[i][1])
        # 包括 pull_request pull_request_info pull_request_action
        try:
            get_branches(user_name, a_repos[i][0], a_repos[i][1], a_repos[i][2], nick_login)
        except UnboundLocalError as e:
            print('仓库', a_repos[i][0], '里没东西呀')
        # 包括 branches commits commit_file_info commit_files commit_comment


def get_user_all_repos(user_name):
    res_repo = []
    url = 'https://api.github.com/users/' + user_name + '/repos'
    html = getHTML(url)
    js = json.loads(html)
    for i in range(len(js)):
        if not js[i]['fork']:
            res_repo.append([js[i]['name'], js[i]['id'], js[i]['default_branch']])  # 暂时不爬fork的，防止数据量太夸张跑一半挂了
        else:
            print('仓库', js[i]['name'], '是fork别人的')
    # print(len(res_repo))
    print(res_repo)
    return res_repo


if __name__ == '__main__':
    user_names = ['sydneyhen', 'ExpectozJJ', 'wangru25', 'ChenDdon', 'Jiahuic', 'dululu', 'L-Focus', 'nickzyang', 'ataola', 'yangshihao-arron', 'Bowinthecloud', 'weteghter', 'LGSKOKO']
    done = []

    with open('D:\\21-22-1\\Database_Practice\\done.txt', 'r') as f:
        for line in f:
            done.append(line.replace('\n', ''))

    for i in range(len(user_names)):
        if user_names[i] not in done:
            stime = time.time()
            get_all(user_names[i])
            etime = time.time()

            atime = etime - stime
            minn = math.trunc(atime / 60)
            secc = math.trunc(atime % 60)
            print('用户', user_names[i], '共用时', minn, '分', secc, '秒')

            with open('D:\\21-22-1\\Database_Practice\\done.txt', 'a+') as f:
                f.write('\n'+user_names[i])
        else:
            print('用户', user_names[i], '爬过了')
