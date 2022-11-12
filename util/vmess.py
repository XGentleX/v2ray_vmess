import base64
import json


# noinspection PyBroadException
def parse(link):
    try:
        return json.loads(base64.b64decode(link.split('//')[1]).decode('utf-8'))
    except Exception as e:
        return {}
