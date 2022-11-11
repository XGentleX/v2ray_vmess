import base64

import requests
from bs4 import BeautifulSoup


def get():
    result = requests.get(
        base64.b64decode("aHR0cHM6Ly94dHJvamFuLnByby9mcmVlLXNzci1zaGFkb3dzb2Nrc3I=").decode('utf-8')).text
    parse_html = BeautifulSoup(result, "html.parser")
    return parse_html.body.find('pre', attrs={}).text
