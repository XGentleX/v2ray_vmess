import base64

from modules import cfmem

vmess_array = set(())


def get_vmess():
    for c in cfmem.get_ssr():
        vmess_array.add(c)


if __name__ == '__main__':
    get_vmess()
    encode = base64.b64encode('\r\n'.join(vmess_array).encode("utf-8")).decode('utf-8')
    v = open('v', 'w', encoding='UTF-8')
    v.write(encode)
