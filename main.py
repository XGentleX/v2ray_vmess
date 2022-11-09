import base64

from modules import cfmem, xtrojan

vmess_array = set(())


# noinspection PyBroadException
def get():
    try:
        for c in cfmem.get():
            vmess_array.add(c)
    except Exception as e:
        print()
    try:
        for c in xtrojan.get():
            vmess_array.add(c)
    except Exception as e:
        print()


if __name__ == '__main__':
    get()
    encode = base64.b64encode('\r\n'.join(vmess_array).encode("utf-8")).decode('utf-8')
    v = open('v', 'w', encoding='UTF-8')
    v.write(encode)
