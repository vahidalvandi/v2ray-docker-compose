#!/bin/sh

LINK=https://raw.githubusercontent.com/miladrahimi/v2ray-docker-compose/master
NAME=v2ray-bridge-server

mkdir -p $NAME/config && cd $NAME || exit
curl -s "$LINK/$NAME/docker-compose.yml" --output docker-compose.yml
curl -s "$LINK/$NAME/config/config.json" --output config/config.json
curl -s "$LINK/assets/clients.txt" --output clients.txt

printf "Enter UPSTREAM-IP: "
read -r UPSTREAM_IP

printf "Enter UPSTREAM-UUID: "
read -r UPSTREAM_UUID

printf "Enter BRIDGE-UUID (Leave empty to generate a random one): "
read -r BRIDGE_UUID
if [ -z "$BRIDGE_UUID" ]; then BRIDGE_UUID=$(cat /proc/sys/kernel/random/uuid); fi

printf "Enter SHADOWSOCKS-PASSWORD (Leave empty to generate a random one): "
read -r SHADOWSOCKS_PASSWORD
if [ -z "$SHADOWSOCKS_PASSWORD" ]; then SHADOWSOCKS_PASSWORD=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c8); fi

sed -ie "s/<UPSTREAM-IP>/$UPSTREAM_IP/g" config/config.json
sed -ie "s/<UPSTREAM-UUID>/$UPSTREAM_UUID/g" config/config.json
sed -ie "s/<BRIDGE-UUID>/$BRIDGE_UUID/g" config/config.json
sed -ie "s/<SHADOWSOCKS-PASSWORD>/$SHADOWSOCKS_PASSWORD/g" config/config.json

BRIDGE_IP=$(curl -s ifconfig.io)
OUTLINE="ss:\/\/$(printf '%s' aes-128-gcm:"$SHADOWSOCKS_PASSWORD" | base64)@$BRIDGE_IP:1210"

sed -ie "s/<BRIDGE-IP>/$BRIDGE_IP/g" clients.txt
sed -ie "s/<BRIDGE-UUID>/$BRIDGE_UUID/g" clients.txt
sed -ie "s/<SHADOWSOCKS-PASSWORD>/$SHADOWSOCKS_PASSWORD/g" clients.txt
sed -ie "s/<OUTLINE>/$OUTLINE/g" clients.txt

printf "\nThe Docker-compose and configuration files are ready.\n\n"
