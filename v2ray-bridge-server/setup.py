#!/usr/bin/python3

import uuid
import re
import json
import base64
import secrets
from pathlib import Path
from urllib.request import urlopen

# LOAD CONFIG FILE

path = Path(__file__).parent
file = open(str(path.joinpath('config/config.json')), 'r', encoding='utf-8')
config = json.load(file)

# INPUT: UPSTREAM-IP

defaultUpstreamIP = config['outbounds'][0]['settings']['vnext'][0]['address']
if defaultUpstreamIP == '<UPSTREAM-IP>':
    message = "Upstream IP:\n"
else:
    message = f"Upstream IP: (Leave empty to use `{defaultUpstreamIP}`)\n"

upstreamIP = input(message)
if upstreamIP != '':
    config['outbounds'][0]['settings']['vnext'][0]['address'] = upstreamIP

# INPUT: UPSTREAM-UUID

defaultUpstreamUUID = config['outbounds'][0]['settings']['vnext'][0]['users'][0]['id']
if defaultUpstreamUUID == '<UPSTREAM-UUID>':
    message = "Upstream UUID:\n"
else:
    message = f"Upstream UUID: (Leave empty to use `{defaultUpstreamUUID}`)\n"

upstreamUUID = input(message)
if upstreamUUID != '':
    config['outbounds'][0]['settings']['vnext'][0]['users'][0]['id'] = upstreamUUID

# CONFIGURE INBOUNDS

for i, inbound in enumerate(config['inbounds']):
    if inbound['protocol'] == 'vmess':
        defaultUUID = inbound['settings']['clients'][0]['id']
        if defaultUUID == '<BRIDGE-UUID>':
            message = "Bridge UUID:\n"
        else:
            message = f"Bridge UUID: (Leave empty to use `{defaultUUID}`)\n"

        bridgeUUID = input(message)
        if bridgeUUID == "":
            if defaultUUID == '<BRIDGE-UUID>':
                bridgeUUID = str(uuid.uuid4())
            else:
                bridgeUUID = defaultUUID

        config['inbounds'][i]['settings']['clients'][0]['id'] = bridgeUUID

    if inbound['protocol'] == 'shadowsocks':
        defaultPassword = inbound['settings']['password']
        if defaultPassword == '<SHADOWSOCKS-PASSWORD>':
            message = "Shadowsocks Password:\n"
        else:
            message = f"Shadowsocks Password: (Leave empty to use `{defaultPassword}`)\n"

        bridgePassword = input(message)
        if bridgePassword == "":
            if defaultPassword == '<SHADOWSOCKS-PASSWORD>':
                bridgePassword = secrets.token_urlsafe(16)
            else:
                bridgePassword = defaultPassword

        config['inbounds'][i]['settings']['password'] = bridgePassword

# SAVE CONFIG FILE

content = json.dumps(config, indent=2)
open(str(path.joinpath('config/config.json')), 'w', encoding='utf-8').write(content)

# GENERATE CLIENT CONFIGS & LINKS

html = open(str(path.joinpath('web/index.html')), 'r', encoding="utf-8").read()

ip = urlopen("http://ifconfig.io/ip").read().decode().rstrip()

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
        link = "ss://{}@{}:{}#{}:{}".format(security, ip, port, ip, port)
        print("\nShadowsocks:\n" + link)
        html = re.sub(r'(ss://[^<]+)', link, html)
    if inbound['protocol'] == 'vmess':
        port = str(inbound['port'])
        uuid = inbound['settings']['clients'][0]['id']
        security = inbound['settings']['clients'][0]['security']
        ps = "{}:{}".format(ip, port)
        c = {"add": ip, "aid": "0", "host": "", "id": uuid, "net": "tcp", "path": "", "port": port, "ps": ps,
             "tls": "none", "type": "none", "v": "2"}
        j = json.dumps(c)
        link = "vmess://" + base64.b64encode(j.encode('ascii')).decode('ascii')
        print("\nVMESS:\n" + link)
        html = re.sub(r'(vmess://[^<]+)', link, html)

open(str(path.joinpath('web/index.html')), 'w', encoding='utf-8').write(html)

# PRINT OUT RESULT

print('\nDone!')
