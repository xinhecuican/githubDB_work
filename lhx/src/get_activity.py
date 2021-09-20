import datetime
import requests
import json
import csv
import re
from bs4 import BeautifulSoup
from datetime import date, timedelta
from common import getHTML, get_repo_id, get_user_id

# type =0为创建仓库 =1为commit =2 pull request =3 following
table_activity = '''
create table Activity(
    id int primary key auto_increment,
    type tinyint,
    user_id int,
    owner_repository_id int,
    activity_date date
);'''
def get_activity(user_name):
    url = 'https://github.com/' + user_name
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    nowy = str(datetime.date.today().year)

    userid = get_user_id(user_name)
    # ----------
    commit_part = soup.find_all('div', class_='Progress mt-1 tooltipped tooltipped-n color-bg-primary')
    for i in range(len(commit_part)):
        act_type = 1
        # user_id =
        commit_repo = commit_part[i].get('aria-label').split(' ')[-2] #tonybaloney/hathi
        commit_dates = get_date(user_name, commit_repo.partition('/')[0], commit_repo.partition('/')[2], userid)
        owner_repo_id = get_repo_id(commit_repo.partition('/')[0], commit_repo.partition('/')[2])
    # ----------
    create_part_names = soup.find_all('a', attrs={'data-hovercard-type': 'repository', 'class': 'mr-2'})
    create_part_dates = soup.find_all('time', class_='col-2 text-right f6 color-text-tertiary pt-1')
    if len(create_part_names) != len(create_part_dates):
        print('create part error!')

    for i in range(len(create_part_names)):
        act_type = 2
        name = create_part_names[i].text # tonybaloney/opentelemetry-python-contrib
        repo_id = get_repo_id(user_name, name.partition('/')[2])
        date = create_part_dates[i].text.strip() + ', ' + nowy
        print(['0', userid, repo_id, date])
    # ----------
    pull_part = soup.find_all('details', attrs={'class': 'Details-element details-reset my-1'})
    for i in range(len(pull_part)):
        repo_name = pull_part[i].find('span', class_='css-truncate css-truncate-target').text # tonybaloney/opentelemetry-python-contrib
        repo_id = get_repo_id(user_name, repo_name.partition('/')[2])
        each_repo_pull = pull_part[i].find_all('li', class_='py-1 ml-0 d-flex')
        for j in range(len(each_repo_pull)):
            each_time = each_repo_pull[j].find('time').text.strip() + ', ' + nowy
            print(['2', userid, repo_id, each_time])

# ----------------------------------------------------------------------------------------------------
def get_date(user_name, owner_name, repo_name, userid):
    res_dates = []
    today = date.today()
    last_day_last_month = date(today.year, today.month, 1) - timedelta(1)
    url = 'https://github.com/' + owner_name + '/' + repo_name + '/commits?author=' + user_name + '&since=' + str(last_day_last_month) + '&until=' + str(today)

    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    repo_id = get_repo_id(owner_name, repo_name)

    dates1 = soup.find('div', class_='TimelineItem TimelineItem--condensed pt-0 pb-2')
    date1 = dates1.find('h2', class_='f5 text-normal').text[11:]
    res_dates.append(date1)
    print(['1', userid, repo_id, date1])

    dates2 = soup.find_all('div', class_='TimelineItem TimelineItem--condensed pt-2 pb-2')
    for i in range(len(dates2)):
        date2 = dates2[i].find('h2', class_='f5 text-normal').text[11:]
        res_dates.append(date2)
        print(['1', userid, repo_id, date2])

    return res_dates

get_activity('tonybaloney')
