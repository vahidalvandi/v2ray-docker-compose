#!/usr/bin/python3

import uuid
import json
from pathlib import Path

path = Path(__file__).parent.joinpath('config/config.json')
file = open(str(path), 'r', encoding='utf-8')
config = json.load(file)

defaultUUID = config['inbounds'][0]['settings']['clients'][0]['id']
if defaultUUID == "<UPSTREAM-UUID>":
    message = "Upstream UUID: (Leave empty to generate a random one)\n"
else:
    message = f"Upstream UUID: (Leave empty to use `{defaultUUID}`)\n"

upstreamUUID = input(message)
if upstreamUUID == "":
    if defaultUUID == "<UPSTREAM-UUID>":
        upstreamUUID = str(uuid.uuid4())
    else:
        upstreamUUID = defaultUUID

config['inbounds'][0]['settings']['clients'][0]['id'] = upstreamUUID
content = json.dumps(config, indent=2)
open(str(path), 'w', encoding='utf-8').write(content)

print('Upstream UUID:')
print(upstreamUUID)
print('\nDone!')
