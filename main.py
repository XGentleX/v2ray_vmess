import base64

from modules import a, b, c
from util import vmess

vmess_array = set(())
schemes_allow = ['vmess', 'ss', 'socks', 'ssr', 'trojan']


# noinspection PyBroadException
def get():
    try:
        for r in a.get():
            vmess_array.add(r)
    except Exception:
        print()
    try:
        for r in b.get():
            vmess_array.add(r)
    except Exception:
        print()
    try:
        for r in c.get():
            vmess_array.add(r)
    except Exception:
        print()


if __name__ == '__main__':
    get()
    link_array = set()
    for link in vmess_array:
        segmentation_array = link.split('://')
        if segmentation_array.__len__() <= 0:
            continue
        if not (segmentation_array[0] in schemes_allow):
            continue
        config = vmess.parse(link)
        add = config.get('add')
        port = config.get('port')
        if (not add) or (not port):
            continue
        link_array.add(link)
    encode = base64.b64encode('\r\n'.join(link_array).encode("utf-8")).decode('utf-8')
    v = open('v', 'w', encoding='UTF-8')
    v.write(encode)
