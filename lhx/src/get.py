import _thread
import queue
import time
import requests
import re
import csv
import threading
from bs4 import BeautifulSoup
from queue import Queue

name_done = []
q = queue.Queue(maxsize=0)

def getHTML(url):
    r = requests.get(url, timeout=30)
    try:
        if r.status_code == 200:
            return r.text
    except:
        print('conn failed')
        return None

def get_user_id(user_name):
    url = 'https://github.com/' + user_name
    html = getHTML(url)
    try:
        user_id = re.search(r'profile_user_id&quot;:\d{4,9}', str(html)).group(0)[22:]
        return user_id
    except:
        pass

# --------------------------------------------------------------------------------------

def get_user_info(user_name):
    url = 'https://github.com/' + user_name
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    time.sleep(1)
    user_id = get_user_id(user_name)
    nick = soup.find('span', class_='p-name vcard-fullname d-block overflow-hidden')
    nick_name = str(nick.text[2:]).strip()
    if nick_name == '':
        nick_name = 'no nick name'

    Counters_data = soup.find_all('span', class_='text-bold color-text-primary')
    followers = Counters_data[0].text
    following = Counters_data[1].text
    star_num = Counters_data[2].text

    proj_data = soup.find_all('span', class_='Counter')
    repositories_num = proj_data[0].text
    project_num = proj_data[1].text

    name_done.append(user_name)
    info = [user_id, nick_name, followers, following, star_num, repositories_num, project_num]
    # print(info)

    with open(r'D:\\21-22-1\\Database_Practice\\user_info.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(info)

    print('已爬取', user_name, '的用户信息, star', star_num, '个')

# --------------------------------------------------------------------------------------

def get_followers(user_name):
    fid = get_user_id(user_name)
    temp = []
    for i in range(1, 2):
        try:
            url = 'https://github.com/' + user_name + '?page=' + str(i) + '&tab=followers'
            html = getHTML(url)
            soup = BeautifulSoup(html, 'html.parser')

            followers_name = soup.find_all('span', class_='Link--secondary pl-1')
            followers_name_2 = soup.find_all('span', class_='Link--secondary')
            followers_name = set(followers_name).union(set(followers_name_2))
            followers_name = list(followers_name)
            print('用户', user_name, '在第', i, '页有', len(followers_name), '个follower')
            if len(followers_name) == 0:
                break
            for j in range(len(followers_name)):
                if followers_name[j].text not in name_done:
                    q.put(followers_name[j].text)
                    d = get_user_id(followers_name[j].text)
                    temp.append((d, fid))
        except:
            pass

    with open(r'D:\\21-22-1\\Database_Practice\\followers.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerows(temp)

# --------------------------------------------------------------------------------------

def get_contributor(user_name, repo_name, repo_id):
    temp = []
    url = 'https://github.com/' + user_name + '/' + repo_name
    print('url是:', url)
    html = getHTML(url)
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    c = soup.find_all('a', attrs={'data-octo-click': 'hovercard-link-click'})
    for i in range(len(c)):
        temp.append((repo_id, get_user_id(c[i].get('href').rpartition('/')[2])))

    temp = list(set(temp))
    with open(r'D:\\21-22-1\\Database_Practice\\contributor.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerows(temp)

    print('已获取项目', repo_name, '的贡献者, 收录其中', len(temp), '人')
# --------------------------------------------------------------------------------------

def get_user_repositories(user_name):
    url = 'https://github.com/' + user_name + '?tab=repositories'
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    try:
        data1 = soup.find_all('a', itemprop='name codeRepository')
        for i in range(len(data1)):
            r_url = str(data1[i].text).strip()
            get_repositories_info(r_url, user_name)
    except:
        pass


def get_repositories_info(r_url, user_name):
    url = 'https://github.com/' + user_name + '/' + r_url
    # print(url)
    html = getHTML(url)
    shtml = str(html)
    soup = BeautifulSoup(html, 'html.parser')
    # print(shtml)
    repository_id = re.search(r'repository_id" content="\d{6,11}', shtml).group(0)[24:]
    default_branch = re.search(r'data-menu-button>\w*</span>', shtml).group(0).partition('>')[2].partition('<')[0]
    try:
        contributor_num = re.search(r'Contributors <span title="\d*', shtml).group(0).rpartition(r'"')[2]
    except:
        contributor_num = 0
    # watch_num = re.search(r'\d* users are watching this repository', shtml)
    try:
        star_num = re.search(r'\d* users starred this repository', shtml).group(0).partition(' ')[0]
    except:
        star_num = 0
    try:
        fork_num = re.search(r'\d* users forked this repository', shtml).group(0).partition(' ')[0]
    except:
        fork_num = 0
    # print(star_num.group(0))
    owner_id = get_user_id(user_name)

    info = [repository_id, user_name, default_branch, contributor_num, star_num, fork_num]

    with open(r'D:\\21-22-1\\Database_Practice\\repository.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(info)

    print('已获取项目', r_url, '的基本信息, con_num是', contributor_num, 'star', star_num, ' fork', fork_num)

    # print(contributor_num)
    if contributor_num != 0:
        print('计算')
        get_contributor(user_name, r_url, repository_id)
    get_all_branch(url + '/branches', repository_id, user_name, default_branch)



def get_all_branch(url, repository_id, user_name, defalut_branch):
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    all_b = soup.find_all('branch-filter-item')
    for i in range(len(all_b)):
        t = url.partition('/branches')
        get_branch(t[0], all_b[i].get('branch'), repository_id, user_name, defalut_branch)


def get_branch(turl, name, repository_id, user_name, default_branch):
    # print(name)
    url = turl + '/tree/' + name
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    branch_name = name
    owner_repo = repository_id

    u2 = turl + '/commits/' + name
    h2 = getHTML(u2)
    soup2 = BeautifulSoup(h2, 'html.parser')
    last_commit = soup2.find_all('a', class_='text-mono f6 btn btn-outline BtnGroup-item')[0].text.strip()


    branch_par = default_branch
    owner_repo = repository_id
    commit_num = soup.find_all('strong')[3]

    info = [branch_name, branch_par, owner_repo, last_commit, commit_num.text]

    with open(r'D:\\21-22-1\\Database_Practice\\branches.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(info)

    print('已获取分支', name, '的基本信息')


    get_commit(turl, last_commit, repository_id, user_name, name)

def get_commit(turl, commit_id, repository_id, user_name, name):
    commit_user = get_user_id(user_name)
    url = turl + '/commits/' + name
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    commit_date = soup.find_all('h2', class_='f5 text-normal')[0].text[11:]
    comment = soup.find_all('a', class_='Link--primary text-bold js-navigation-open markdown-title')[0].text[:-2]

    commit_user = soup.find_all('a', class_='commit-author user-mention')[0].text

    info = [commit_id, repository_id, commit_user, commit_date, comment]
    with open(r'D:\\21-22-1\\Database_Practice\\commit.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(info)

    print('已获取提交', commit_id, '的基本信息')
# --------------------------------------------------------------------------------------

# 获取个人信息 关注者信息 仓库信息 单个仓库信息 贡献者 分支 提交
if __name__ == '__main__':
    q.put('sparshg')
    while True:
        temp_name = q.get()
        # print(q.qsize())
        # a = threading.Thread(target=get_user_info, args=(temp_name,))
        # b = threading.Thread(target=get_followers, args=(temp_name,))
        # c = threading.Thread(target=get_user_repositories, args=(temp_name,))
        get_user_info(temp_name)
        get_followers(temp_name)
        get_user_repositories(temp_name)
        # a.start()
        # b.start()
        # c.start()
        # print(q.qsize())
        print('用户', temp_name, '已完成')