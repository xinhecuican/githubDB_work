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
from get_commit import get_commit


# name_done = []
# q = queue.Queue(maxsize=0)



def getHTML(url, t):
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
    if t == 0:
        return r.text
    else:
        return r.content


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


# a = 'eigen/.hgtags'
# aa = '.gitnone/.asd.md'
# aaa = 'asd/asd.md'
# c = 'asd.md'
# b = c.split('/')
# print(b)


fname = 'asdasdasd/.ni/.hello'
temp = fname.split('/')
ends = temp[-1]
outp = ''
if ends.startswith('.'):  # gitnone/ [.asd.md]
    if ends.count('.') >= 2:
        for each in range(len(temp) - 1):
            outp = outp + temp[each] + '&'
        outp = outp + ends
        print(outp)

    else:
        for each in range(len(temp) - 1):
            outp = outp + temp[each] + '&'
        outp = outp + ends + '.txt'
        print(outp)
else:
    if ends.count('.') >= 1:
        for each in range(len(temp) - 1):
            outp = outp + temp[each] + '&'
        outp = outp + ends
        print(outp)
    else:
        for each in range(len(temp) - 1):
            outp = outp + temp[each] + '&'
        outp = outp + ends + '.txt'
        print(outp)