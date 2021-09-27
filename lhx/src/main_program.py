import threading
import json
from version2 import get_user_info, get_issue, get_branches
from get_activity import get_activity
from get_tags import get_repo_tags
from get_pull_requests import get_open_pulls
from common import getHTML


# from common import get_user_id

def get_all(user_name):
    # user_id = get_user_id(user_name)

    # user_info
    # followers
    # user_description
    # repository
    # repository_info
    # licenses
    # threading.Thread(target=get_user_info, args=(user_name,)).start()

    # activity
    # threading.Thread(target=get_activity, args=(user_name,)).start()

    # tags
    # tag_files
    a_repos = get_user_all_repos(user_name)
    for i in range(len(a_repos)):
        # threading.Thread(target=get_repo_tags, args=(user_name, a_repos[i][0], )).start()
        # threading.Thread(target=get_issue, args=(user_name, a_repos[i][0], a_repos[i][1],)).start()
        # get_issue(user_name, a_repos[i][0], a_repos[i][1])
        get_open_pulls(user_name, a_repos[i][0], a_repos[i][1])
        # get_branches(user_name, a_repos[i][0], a_repos[i][1])


def get_user_all_repos(user_name):
    res_repo = []
    url = 'https://api.github.com/users/' + user_name + '/repos'
    html = getHTML(url)
    js = json.loads(html)
    for i in range(len(js)):
        res_repo.append([js[i]['name'], js[i]['id']])
    print(len(res_repo))
    return res_repo


if __name__ == '__main__':
    get_all('bollnh')
