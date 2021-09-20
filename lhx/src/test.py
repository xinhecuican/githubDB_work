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

url = 'https://github.com/tonybaloney'
# IssueLabel hx_IssueLabel d-inline-block v-align-middle
html = getHTML(url)
soup = BeautifulSoup(html, 'html.parser')
activity_part = soup.find_all('div', class_='Progress mt-1 tooltipped tooltipped-n color-bg-primary')

# all_question = soup.find_all('div', class_='flex-auto min-width-0 p-2 pr-3 pr-md-2')
#
# q_ids = all_question[0].find('span', class_='opened-by').text.split()[0][1:]

# a = soup.find('a', class_='pl-3 pr-3 py-3 p-md-0 mt-n3 mb-n3 mr-n3 m-md-0 Link--primary no-underline no-wrap').find('strong').text
# p = json.loads(html)
# pj = json.dumps(p, indent=4, separators=(',', ':'))
print(date.today().year)
