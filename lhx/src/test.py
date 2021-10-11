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


def getHTML(url, t=0):
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

url = 'https://github.com/abbazs'
html = getHTML(url)
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# try:
#     s = soup.find('svg', class_='octicon octicon-project UnderlineNav-octicon hide-sm').parent.text.replace('\n', '').replace(' ', '')[8:]
# except:
#     s = 0
a = soup.find_all('span', class_='Counter')
print(a)

