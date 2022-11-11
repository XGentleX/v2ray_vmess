import base64
from xml.dom.minidom import parseString

import requests as requests
from bs4 import BeautifulSoup

ok_code = [200, 201, 202, 203, 204, 205, 206]
url = "aHR0cHM6Ly93d3cuY2ZtZW0uY29tL2ZlZWRzL3Bvc3RzL2RlZmF1bHQ/YWx0PXJzcw=="


def get_last():
    resout = requests.get(base64.b64decode(url).decode('utf-8'))
    return resout.text


def parse_result():
    dom = parseString(get_last())
    items = dom.documentElement.getElementsByTagName('item')
    return items[0].getElementsByTagName('link')[0].childNodes[0].nodeValue


def get():
    link = parse_result()
    html = requests.get(link).text
    parse_html = BeautifulSoup(html, "html.parser")
    vmess = parse_html.body.find('pre', attrs={}).text
    vmess_list = vmess.split('vmess://')
    ssr_result = set()
    for v in vmess_list:
        if len(v) != 0:
            ssr_result.add('vmess://' + v)
    return ssr_result
