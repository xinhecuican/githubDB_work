import requests
import json
import csv

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
            r.encoding = r.apparent_encoding
            return r.text
    except:
        print('conn failed')
        return None

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
        d = date.partition('T')[0]
        return d

def save_sth(lists, fname, types): # 0是单行 1是多行
    path = r'D:\\21-22-1\\Database_Practice1\\' + fname + '.csv'
    with open(path, 'a+', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        if types == 0:
            writer.writerow(lists)
        elif types == 1:
            writer.writerows(lists)
        else:
            print('error when saving')