#!/bin/sh

REAL_IP=$(curl -s -m 5 ifconfig.io)
printf "BRIDGE-IP (Leave empty to use '%s'): " "$REAL_IP"
read -r BRIDGE_IP
BRIDGE_IP=${BRIDGE_IP:-$REAL_IP}

printf "BRIDGE-PORT (Leave empty to use '%s'): " "1310"
read -r BRIDGE_PORT
BRIDGE_PORT=${BRIDGE_PORT:-1310}

printf "BRIDGE-UUID: "
read -r BRIDGE_UUID

JSON="{\"add\": \"$BRIDGE_IP\", \"aid\": \"0\", \"host\": \"\", \"id\": \"$BRIDGE_UUID\", \"net\": \"tcp\", \"path\": \
\"\", \"port\": \"$BRIDGE_PORT\", \"ps\": \"$BRIDGE_IP/tcp\", \"tls\": \"\", \"type\": \"none\", \"v\": \"2\"}"

printf "\n%s:\n%s%s\n" "VMESS Link" "vmess://" "$(echo "$JSON" | base64)"
