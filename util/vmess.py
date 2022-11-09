import base64
import json


def parse(vmess):
    return json.loads(base64.b64decode(vmess.split('//')[1]).decode('utf-8'))
