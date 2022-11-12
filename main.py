import base64

from modules import a, b, c

vmess_array = set(())


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
    encode = base64.b64encode('\r\n'.join(vmess_array).encode("utf-8")).decode('utf-8')
    v = open('v', 'w', encoding='UTF-8')
    v.write(encode)
