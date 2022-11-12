import base64

from modules import a, b, c

vmess_array = set(())
schemes_allow = ['vmess', 'ss', 'socks', 'ssr', 'trojan']


# noinspection PyBroadException
def get():
    try:
        for link in a.get():
            vmess_array.add(link)
    except Exception as e:
        print()
    try:
        for link in b.get():
            vmess_array.add(link)
    except Exception as e:
        print()
    try:
        for link in c.get():
            vmess_array.add(link)
    except Exception as e:
        print()


if __name__ == '__main__':
    get()
    link_array = set()
    for link in vmess_array:
        segmentation_array = link.split('://')
        if segmentation_array.__len__() <= 0:
            continue
        if segmentation_array[0] in schemes_allow:
            link_array.add(link)
    encode = base64.b64encode('\r\n'.join(link_array).encode("utf-8")).decode('utf-8')
    v = open('v', 'w', encoding='UTF-8')
    v.write(encode)
