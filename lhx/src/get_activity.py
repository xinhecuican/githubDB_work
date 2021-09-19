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

    repo_part = soup.find('ul', class_='list-style-none mt-1')
    #

