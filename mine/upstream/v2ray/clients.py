#!/usr/bin/python3

import base64
import json
from pathlib import Path

# VMESS
vmessTag = 'my-vmess'
ssTag = 'my-shadowsocks'
domain = '<DOMAIN.IR>'
bridgeIP = '<BRIDGE-IP>'
bridgePort = '<BRIDGE-PORT>'

path = Path(__file__).parent

config_file = open(str(path.joinpath('config/config.json')), 'r', encoding='utf-8')
config = json.load(config_file)

uuid = config['inbounds'][1]['settings']['clients'][0]['id']
password = config['inbounds'][0]['settings']['password']

vmessJson = json.dumps({
    "v": "2", "ps": vmessTag, "add": domain, "port": "443", "id": uuid, "aid": "0", "net": "ws", "type": "none",
    "host": domain, "path": "/v", "tls": "tls"
})

print("vmess://" + base64.b64encode(vmessJson.encode('ascii')).decode('ascii'))
print()

auth = base64.b64encode(("chacha20-ietf-poly1305:" + password).encode('ascii')).decode('ascii')
print("ss://" + auth + "@" + bridgeIP + ":" + bridgePort + "/?#" + ssTag)
print()
