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

url = 'https://api.github.com/repos/tonybaloney/wily/commits/e72b7d95228bbe5538a072dc5d1186daa318bb03'
# IssueLabel hx_IssueLabel d-inline-block v-align-middle
html = getHTML(url)
soup = BeautifulSoup(html, 'html.parser')
# a = soup.find('a', class_='pl-3 pr-3 py-3 p-md-0 mt-n3 mb-n3 mr-n3 m-md-0 Link--primary no-underline no-wrap').find('strong').text
p = json.loads(html)
pj = json.dumps(p, indent=4, separators=(',', ':'))
print(pj)

