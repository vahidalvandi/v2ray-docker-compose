#!/usr/bin/python3

import base64
import json
from pathlib import Path
from urllib.request import urlopen

path = Path(__file__).parent
file = open(str(path.joinpath('v2ray.json')), 'r', encoding='utf-8')
config = json.load(file)

ip = urlopen("https://ipv4.icanhazip.com/").read().decode().rstrip()

for inbound in config['inbounds']:
    if inbound['protocol'] == 'socks':
        print("SOCKS: 127.0.0.1:{}".format(str(inbound['port'])))
    if inbound['protocol'] == 'http':
        print("HTTP: 127.0.0.1:{}".format(str(inbound['port'])))
    if inbound['protocol'] == 'shadowsocks':
        port = str(inbound['port'])
        method = inbound['settings']['method']
        password = inbound['settings']['password']
        security = base64.b64encode((method + ":" + password).encode('ascii')).decode('ascii')
        print("Shadowsocks: " + "ss://{}@{}:{}".format(security, ip, port))
