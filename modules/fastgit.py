from base64 import b64decode

import requests as requests

url = 'https://raw.fastgit.org/freefq/free/master/v2'


def get_ssr():
    context = requests.get(url).text
    return b64decode(context).decode('utf-8').splitlines()
