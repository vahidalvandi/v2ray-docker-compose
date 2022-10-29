#!/usr/bin/python3
import base64
import json
from urllib.request import urlopen

file = open('config/config.json', 'r')
config = json.load(file)

ip = urlopen("http://ifconfig.io/ip").read().decode().rstrip()

for inbound in config['inbounds']:
    if inbound['protocol'] == 'socks':
        port = str(inbound['port'])
        print("SOCKS Proxy: ")
        print("\tHost: 127.0.0.1, Port: {}".format(port))
    if inbound['protocol'] == 'http':
        port = str(inbound['port'])
        print("HTTP Proxy: ")
        print("\tHost: 127.0.0.1, Port: {}".format(port))
    if inbound['protocol'] == 'shadowsocks':
        port = str(inbound['port'])
        method = inbound['settings']['method']
        password = inbound['settings']['password']
        security = base64.b64encode((method + ":" + password).encode('ascii')).decode('ascii')

        print("Shadowsocks Proxy: ")
        print("\tss://{}@{}:{}#{}:{}".format(security, ip, port, ip, port))
    if inbound['protocol'] == 'vmess':
        port = str(inbound['port'])
        uuid = inbound['settings']['clients'][0]['id']
        security = inbound['settings']['clients'][0]['security']
        ps = "{}:{}".format(ip, port)

        c = {"add": ip, "aid": "0", "host": "", "id": uuid, "net": "tcp", "path": "", "port": port, "ps": ps,
             "tls": "none", "type": "none", "v": "2"}
        j = json.dumps(c)

        print("VMESS Proxy: ")
        print("\tvmess://" + base64.b64encode(j.encode('ascii')).decode('ascii'))
