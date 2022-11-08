import base64
import json
import time

import requests
from ping3 import ping

from modules import cfmem, fastgit

vmess_array = set(())


def get_vmess():
    for c in cfmem.get_ssr():
        vmess_array.add(c)
    for f in fastgit.get_ssr():
        vmess_array.add(f)


# def test():
#     s = 'vmess://eyJhZGQiOiIyNS43MmltZy54eXoiLCJwcyI6IvCfh7rwn4e4X1VTX+e+juWbvS0+8J+HsPCfh7dfS1Jf6Z+p5Zu9Iiwic2N5IjoiYXV0byIsInByb3h5VHlwZSI6InZtZXNzIiwidHlwZSI6Im5vbmUiLCJzbmkiOiIiLCJwYXRoIjoiLyIsInBvcnQiOjQ0MywidiI6MiwiaG9zdCI6IiIsInRscyI6InRscyIsImlkIjoiODFkOTNmNjItMTVhMi00OTk0LWFkYjktMGI1ZDkwNmFhYzdlIiwibmV0Ijoid3MiLCJhaWQiOjAsIm9yaWdpbk5hbWUiOiJSZWxheV/wn4e68J+HuFVTLfCfh7Pwn4exTkxfMTA5NSJ9'
#     config = json.loads(base64.b64decode(s.split('//')[1]).decode('utf-8'))
#     print(config)
#     response = ping(config['add'])
#     if response is not None:
#         delay = int(response * 1000)
#         print(delay, "延迟")


def delay(address):
    s = 'vmess://eyJhZGQiOiIyNS43MmltZy54eXoiLCJwcyI6IvCfh7rwn4e4X1VTX+e+juWbvS0+8J+HsPCfh7dfS1Jf6Z+p5Zu9Iiwic2N5IjoiYXV0byIsInByb3h5VHlwZSI6InZtZXNzIiwidHlwZSI6Im5vbmUiLCJzbmkiOiIiLCJwYXRoIjoiLyIsInBvcnQiOjQ0MywidiI6MiwiaG9zdCI6IiIsInRscyI6InRscyIsImlkIjoiODFkOTNmNjItMTVhMi00OTk0LWFkYjktMGI1ZDkwNmFhYzdlIiwibmV0Ijoid3MiLCJhaWQiOjAsIm9yaWdpbk5hbWUiOiJSZWxheV/wn4e68J+HuFVTLfCfh7Pwn4exTkxfMTA5NSJ9'
    config = json.loads(base64.b64decode(s.split('//')[1]).decode('utf-8'))
    print(config)
    response = ping(config['add'])
    if response is not None:
        delay = int(response * 1000)
        print(delay, "延迟")


if __name__ == '__main__':
    get_vmess()
    encode = base64.b64encode(vmess_array.__str__().encode("utf-8")).decode('utf-8')
    v = open('v', 'w', encoding='UTF-8')
    v.write(encode)
