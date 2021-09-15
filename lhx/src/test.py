import _thread
import queue
import time
import requests
import re
import csv
import threading
from bs4 import BeautifulSoup
from queue import Queue
import json
# name_done = []
# q = queue.Queue(maxsize=0)


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

url = 'https://github.com/tonybaloney/wily/issues'
html = getHTML(url)
soup = BeautifulSoup(html, 'html.parser')
a = soup.find_all('div', class_='Box-row Box-row--focus-gray p-0 mt-0 js-navigation-item js-issue-row')
for i in range(len(a)):
    print(a[i].get('id').partition('_')[2])

# print(len(a))
# print(html)


