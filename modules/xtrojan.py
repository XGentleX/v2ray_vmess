import requests
from bs4 import BeautifulSoup


def get():
    result = requests.get('https://xtrojan.pro/free-ssr-shadowsocksr').text
    parse_html = BeautifulSoup(result, "html.parser")
    return parse_html.body.find('pre', attrs={}).text
