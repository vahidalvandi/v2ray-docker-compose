#!/usr/bin/python3

import base64
import yaml
import json
from pathlib import Path

path = Path(__file__).parent

v2ray_config_file = open(str(path.joinpath('v2ray/config/config.json')), 'r', encoding='utf-8')
v2ray_config = json.load(v2ray_config_file)
with open('docker-compose.yml', 'r') as f:
    dockerCompose = yaml.safe_load(f)

uuid = v2ray_config['inbounds'][0]['settings']['clients'][0]['id']
domain = dockerCompose["services"]["v2ray"]["environment"][1].split('=')[1];

j = json.dumps({
    "v": "2", "ps": domain, "add": domain, "port": "443", "id": uuid, "aid": "0", "net": "ws", "type": "none",
    "host": domain, "path": "/", "tls": "tls"
})

print("vmess://" + base64.b64encode(j.encode('ascii')).decode('ascii'))
