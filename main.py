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


def delay():
    try:
        for s in vmess_array:
            config = json.loads(base64.b64decode(s.split('//')[1]).decode('utf-8'))
            response = ping(config['add'])
            if response is not None:
                delay_ = int(response * 1000)
                print(config['ps'], " 延迟", delay_)
    except Exception as e:
        print()


if __name__ == '__main__':
    get_vmess()
    encode = base64.b64encode('\r\n'.join(vmess_array).encode("utf-8")).decode('utf-8')
    v = open('v', 'w', encoding='UTF-8')
    v.write(encode)
    delay()
