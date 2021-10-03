import threading
import json
import time
from version2 import get_user_info, get_issue, get_branches
from get_activity import get_activity
from get_pull_requests import get_open_pulls
from common import getHTML


# from common import get_user_id

def get_all(user_name):
    get_user_info(user_name)
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
            get_branches(user_name, a_repos[i][0], a_repos[i][1], a_repos[i][2])
        except UnboundLocalError as e:
            print('仓库里没东西呀')
        # 包括 branches commits commit_file_info commit_files commit_comment


def get_user_all_repos(user_name):
    res_repo = []
    url = 'https://api.github.com/users/' + user_name + '/repos'
    html = getHTML(url)
    js = json.loads(html)
    for i in range(len(js)):
        res_repo.append([js[i]['name'], js[i]['id'], js[i]['default_branch']])
    # print(len(res_repo))
    return res_repo


if __name__ == '__main__':
    stime = time.time()
    user_name = 'NavaneethDhruvsoft'
    get_all(user_name)
    etime = time.time()

    atime = etime - stime
    minn = atime % 60
    secc = atime / 60
    print('用户', user_name, '共用时', minn, '分', secc, '秒')
