import base64
import datetime

import requests
from bs4 import BeautifulSoup

url = "aHR0cHM6Ly9mcmVlZnEuY29tL2ZyZWUtc3NyLw=="
schemes_allow = ['vmess', 'ss', 'socks', 'ssr', 'trojan']


def get_request():
    ecode_url = base64.b64decode(url).decode('utf-8')
    yes_time = datetime.datetime.now()
    current_year = yes_time.strftime('%Y')
    current_month = yes_time.strftime('%m')
    current_day = yes_time.strftime('%d')
    request = requests.get(ecode_url + current_year + '/' + current_month + '/' + current_day + '/ssr.html')
    if request.status_code == 404:
        ecode_url = base64.b64decode(url).decode('utf-8')
        yes_time = datetime.datetime.now() - datetime.timedelta(days=1)
        current_year = yes_time.strftime('%Y')
        current_month = yes_time.strftime('%m')
        current_day = yes_time.strftime('%d')
        return requests.get(ecode_url + current_year + '/' + current_month + '/' + current_day + '/ssr.html')
    else:
        return request


def get():
    links = set()
    request = get_request()
    html = BeautifulSoup(request.text, "html.parser")
    a_links = html.find_all('a')
    for link in a_links:
        href = link.get('href')
        if 'https://www.freefq.com/d/file/free-ssr/' in href:
            href_request = requests.get(href)
            href_request.encoding = 'gb2312'
            href_html = BeautifulSoup(href_request.text, "html.parser")
            ps = href_html.find_all('p')
            for p in ps:
                if '://' in p.text:
                    agreements = p.text.split('\n')
                    for a in agreements:
                        segmentation_array = a.split('://')
                        if segmentation_array.__len__() <= 0:
                            continue
                        if segmentation_array[0] in schemes_allow:
                            links.add(a)

    return links
