#!/bin/sh

LINK=https://raw.githubusercontent.com/miladrahimi/v2ray-docker-compose/master
NAME=v2ray-bridge-server

mkdir -p $NAME/config && cd $NAME || exit
curl -s "$LINK/$NAME/docker-compose.yml" --output docker-compose.yml
curl -s "$LINK/$NAME/config/config.json" --output config/config.json
curl -s "$LINK/assets/clients.txt" --output clients.txt

printf "%s" "Enter UPSTREAM-IP: "
read -r UPSTREAM_IP

printf "%s" "Enter UPSTREAM-UUID: "
read -r UPSTREAM_UUID

printf "%s" "Enter BRIDGE-UUID (Leave empty to generate a random one): "
read -r BRIDGE_UUID
if [ -z "$BRIDGE_UUID" ]; then BRIDGE_UUID=$(cat /proc/sys/kernel/random/uuid); fi

printf "%s" "Enter SHADOWSOCKS-PASSWORD (Leave empty to generate a random one): "
read -r SHADOWSOCKS_PASSWORD
if [ -z "$SHADOWSOCKS_PASSWORD" ]; then SHADOWSOCKS_PASSWORD=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c8); fi

sed -ie "s/<UPSTREAM-IP>/$UPSTREAM_IP/g" config/config.json
sed -ie "s/<UPSTREAM-UUID>/$UPSTREAM_UUID/g" config/config.json
sed -ie "s/<BRIDGE-UUID>/$BRIDGE_UUID/g" config/config.json
sed -ie "s/<SHADOWSOCKS-PASSWORD>/$SHADOWSOCKS_PASSWORD/g" config/config.json

echo "The Docker-compose and configuration files are ready."

BRIDGE_IP=$(curl ifconfig.io)
OUTLINE="ss://$(printf '%s' aes-128-gcm:"$SHADOWSOCKS_PASSWORD" | base64)@$BRIDGE_IP:1210"

sed -ie "s/<BRIDGE-IP>/$BRIDGE_IP/g" clients.txt
sed -ie "s/<BRIDGE-UUID>/$BRIDGE_UUID/g" clients.txt
sed -ie "s/<SHADOWSOCKS-PASSWORD>/$SHADOWSOCKS_PASSWORD/g" clients.txt
sed -ie "s/<OUTLINE>/$OUTLINE/g" clients.txt
