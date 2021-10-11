import requests
from retrying import retry
import time
import json
import csv
import os
import re

import urllib3.exceptions

@retry(wait_fixed=2000)
def getHTML(url, getType = 0):
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
    if getType == 0:
        return r.text
    else:
        return r.content



def get_user_id(user_name):
    url = 'https://api.github.com/users/' + user_name
    html = getHTML(url)
    js = json.loads(html)
    user_id = js['id']
    return user_id

def get_repo_id(user_name, repo_name):
    url = 'https://api.github.com/repos/' + user_name + '/' + repo_name
    html = getHTML(url)
    js = json.loads(html)
    repo_id = js['id']
    return repo_id

def trans_date_format(date, type): # yy-mm-dd
    month = {
        'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
    }
    if type == 0: # Sep 7, 2021 --- 2021-09-07
        date_l = date.split(' ')
        yy = date_l[2]
        mm = month[date_l[0]]
        dd = date_l[1].replace(',', '').zfill(2)
        res_data = yy + '-' + mm + '-' + dd
        return res_data
    elif type == 1: # 2021-02-21T02:53:55Z
        res_data = date.partition('T')[0]
        return res_data

def save_sth(lists, fname, types): # 0是单行 1是多行
    path = r'D:\\21-22-1\\Database_Practice2\\' + fname + '.csv'
    with open(path, 'a+', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        if types == 0:
            writer.writerow(lists)
        elif types == 1:
            writer.writerows(lists)
        else:
            print('error when saving')

def save_file(path, fbyte, fname): # fname是x/x/x的形式
    if not os.path.exists(path):
        os.makedirs(path)


    temp = fname.split('/')
    ends = temp[-1]
    outp = ''

    if ends.startswith('.'):  # gitnone/ [.asd.md]
        if ends.count('.') >= 2:
            for each in range(len(temp) - 1):
                outp = outp + temp[each] + '&'
            outp = outp + ends
        else:
            for each in range(len(temp) - 1):
                outp = outp + temp[each] + '&'
            outp = outp + ends + '.txt'
    else:
        if ends.count('.') >= 1:
            for each in range(len(temp) - 1):
                outp = outp + temp[each] + '&'
            outp = outp + ends
        else:
            for each in range(len(temp) - 1):
                outp = outp + temp[each] + '&'
            outp = outp + ends + '.txt'

    path = path + outp

    try:
        with open(path, 'ab+') as f:
            f.write(fbyte)
    except FileNotFoundError as e:
        print(e.filename)
        pass

#  eigen/.hgtags