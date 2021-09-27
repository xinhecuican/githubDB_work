# QUESTION: commit 和 pull request 是否涉及 commit_id
# ALMOST_DONE: activity 表

import datetime
from bs4 import BeautifulSoup
from datetime import date, timedelta
from common import getHTML, get_repo_id, get_user_id, trans_date_format, save_sth


def get_activity(user_name):
    url = 'https://github.com/' + user_name
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    nowy = str(datetime.date.today().year)
    userid = get_user_id(user_name)

    # ----- commit type = 1 -----
    commit_part = soup.find_all('div', class_='Progress mt-1 tooltipped tooltipped-n color-bg-primary')
    for i in range(len(commit_part)):
        commit_repo = commit_part[i].get('aria-label').split(' ')[-2]  # tonybaloney/hathi
        get_type_1(user_name, commit_repo.partition('/')[0], commit_repo.partition('/')[2], userid)

    # ----- create type = 0 -----
    create_part_names = soup.find_all('a', attrs={'data-hovercard-type': 'repository', 'class': 'mr-2'})
    create_part_dates = soup.find_all('time', class_='col-2 text-right f6 color-text-tertiary pt-1')
    if len(create_part_names) != len(create_part_dates):
        print('create part error!')

    for i in range(len(create_part_names)):
        name = create_part_names[i].text
        # example: tonybaloney/opentelemetry-python-contrib
        repo_id = get_repo_id(user_name, name.partition('/')[2])
        date2 = create_part_dates[i].text.strip() + ', ' + nowy
        save_sth(['0', userid, '', repo_id, trans_date_format(date2, 0)], 'activity', 0)
        print(['0', userid, repo_id, trans_date_format(date2, 0)])

    # ----- pull request type = 2  -----
    pull_part = soup.find_all('details', attrs={'class': 'Details-element details-reset my-1'})
    for i in range(len(pull_part)):
        repo_name = pull_part[i].find('span', class_='css-truncate css-truncate-target').text
        # example: tonybaloney/opentelemetry-python-contrib
        repo_id = get_repo_id(user_name, repo_name.partition('/')[2])
        each_repo_pull = pull_part[i].find_all('li', class_='py-1 ml-0 d-flex')
        for j in range(len(each_repo_pull)):
            each_time = each_repo_pull[j].find('time').text.strip() + ', ' + nowy
            save_sth(['2', userid, '', repo_id, trans_date_format(each_time, 0)], 'activity', 0)
            print(['2', userid, repo_id, trans_date_format(each_time, 0)])

    # ----- following type = 3 ----- TODO: 暂未找到例子
# ----------------------------------------------------------------------------------------------------
def get_type_1(user_name, owner_name, repo_name, userid): # 对于commit 顺便保存了
    res_dates = []
    today = date.today()
    last_day_last_month = date(today.year, today.month, 1) - timedelta(1)
    url = 'https://github.com/' + owner_name + '/' + repo_name + '/commits?author=' + user_name + '&since=' + str(
        last_day_last_month) + '&until=' + str(today)

    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    repo_id = get_repo_id(owner_name, repo_name)

    dates1 = soup.find('div', class_='TimelineItem TimelineItem--condensed pt-0 pb-2')
    date1 = dates1.find('h2', class_='f5 text-normal').text[11:]
    commit_id1 = dates1.find('a', class_='text-mono f6 btn btn-outline BtnGroup-item').text.replace('\n', '').strip()

    res_dates.append(date1)
    save_sth(['1', userid, repo_id, commit_id1, trans_date_format(date1, 0)], 'activity', 0)
    print(['1', userid, commit_id1, repo_id, trans_date_format(date1, 0)])

    dates2 = soup.find_all('div', class_='TimelineItem TimelineItem--condensed pt-2 pb-2')
    for i in range(len(dates2)):
        date2 = dates2[i].find('h2', class_='f5 text-normal').text[11:]
        commit_id2 = dates2[i].find('a', class_='text-mono f6 btn btn-outline BtnGroup-item').text.replace('\n', '').strip()
        res_dates.append(date2)
        save_sth(['1', userid, commit_id2, repo_id, trans_date_format(date2, 0)], 'activity', 0)
        print(['1', userid, commit_id2, repo_id, trans_date_format(date2, 0)])


# get_activity('tonybaloney')
