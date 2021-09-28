import _thread
import queue
import time
import requests
import re
import csv
import threading
from datetime import date, timedelta
from bs4 import BeautifulSoup
from queue import Queue
import json


# name_done = []
# q = queue.Queue(maxsize=0)


def getHTML(url):
    headers = {
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


def get_label_comment(url):
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')

    label_infos = soup.find_all('div', class_='TimelineItem-body')
    print('已进入: ', len(label_infos))
    for i in range(len(label_infos)):  # 以每次添加为单位
        if label_infos[i].find('a', class_='IssueLabel hx_IssueLabel d-inline-block v-align-middle') is not None:
            each_labels = []
            each_content = []
            temp = label_infos[i].find_all('a', class_='IssueLabel hx_IssueLabel d-inline-block v-align-middle')
            for j in range(len(temp)):  # 此处获取一次添加的所有标签
                each_labels.append(temp[j].text.replace('\n', '').strip())  # 标签名
                try:
                    each_content.append(temp[j].get('title'))  # 标签内容
                except:
                    each_labels.append('')
            time = label_infos[i].find('a', class_='Link--secondary').text
            single_label_comment = [each_labels, each_content, time]
            print('[label_comment]: ', single_label_comment)

url = 'https://github.com/tonybaloney/BotBuilder-Samples/commit/2cd3caf4fb85276863a9467925b5b3a222544931'
url1 = 'https://api.github.com/repos/xinhecuican/githubDB_work/commits/1d497a92a7a84a8a16cda830d0aa3319da74994e'
html = getHTML(url)
soup = BeautifulSoup(html, 'html.parser')

# jss = json.loads(html)
# js = json.dumps(jss, sort_keys=True, indent=4, separators=(',', ':'))
print(html)
