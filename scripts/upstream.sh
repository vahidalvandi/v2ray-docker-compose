#!/bin/sh

LINK=https://raw.githubusercontent.com/miladrahimi/v2ray-docker-compose/master
NAME=v2ray-upstream-server

mkdir -p $NAME && cd $NAME || exit
curl -s "$LINK/$NAME/docker-compose.yml" --output docker-compose.yml

mkdir -p config
curl -s "$LINK/$NAME/config/config.json" --output config/config.json

printf "%s" "Enter UPSTREAM-UUID (Leave empty to generate a random one): "
read -r UPSTREAM_UUID
if [ -z "$UPSTREAM_UUID" ]; then UPSTREAM_UUID=$(cat /proc/sys/kernel/random/uuid); fi

sed -ie "s/<UPSTREAM-UUID>/$UPSTREAM_UUID/g" config/config.json

echo "The Docker-compose and configuration files are ready."

UPSTREAM_IP=$(curl ifconfig.io)

echo "UPSTREAM-IP: $UPSTREAM_IP"
echo "UPSTREAM-UUID: $UPSTREAM_UUID"
