#!/usr/bin/python3

import uuid
import json
import secrets
from pathlib import Path

# LOAD CONFIG FILE

path = Path(__file__).parent
file = open(str(path.joinpath('v2ray.json')), 'r', encoding='utf-8')
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

# INPUT: VMESS-UUID

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
    if inbound['protocol'] == 'shadowsocks':
        defaultPassword = inbound['settings']['password']
        if defaultPassword == '<SHADOWSOCKS-PASSWORD>':
            message = "Relay Shadowsocks Password:\n"
        else:
            message = f"Relay Shadowsocks Password: (Leave empty to use `{defaultPassword}`)\n"

        relayPassword = input(message)
        if relayPassword == "":
            if defaultPassword == '<SHADOWSOCKS-PASSWORD>':
                relayPassword = secrets.token_urlsafe(16)
            else:
                relayPassword = defaultPassword

        config['inbounds'][i]['settings']['password'] = relayPassword

# SAVE CONFIG FILE

content = json.dumps(config, indent=2)
open(str(path.joinpath('v2ray.json')), 'w', encoding='utf-8').write(content)

# PRINT OUT RESULT

print('Done!')
