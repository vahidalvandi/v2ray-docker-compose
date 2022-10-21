# V2Ray Docker Compose

This repository contains sample Docker Compose files to run V2Ray upstream and bridge servers.

## Documentation

### Terminology

* Upstream Server: A server that has free access to the Internet.
* Bridge Server: A server that is available to clients and has access to the upstream server.
* Client: A user-side application with access to the bridge server.

```
(Client) <-> [ Bridge Server ] <-> [ Upstream Server ] <-> (Internet)
```

### Setup

#### Upstream Server

1. Install Docker and Docker-compose.
1. Copy the `v2ray-upstream-server` directory into the upstream server.
1. Run ```cat /proc/sys/kernel/random/uuid``` command to generate a UUID.
1. Replace `<UPSTREAM-UUID>` in the `config.json` file with the generated UUID.
1. Run `docker-compose up -d`.

#### Bridge Server

1. Install Docker and Docker-compose.
1. Copy the `v2ray-bridge-server` directory into the bridge server.
1. Replace the following variables in the `config.json` file with appropriate values.
    * `<SHADOWSOCKS-PASSWORD>`: A password for Shadowsocks users like `FR33DoM`.
    * `<BRIDGE-UUID>`: A new UUID for bridge server (Run ```cat /proc/sys/kernel/random/uuid```).
    * `<UPSTREAM-IP>`: The upstream server IP address like `13.13.13.13`.
    * `<UPSTREAM-UUID>`: The generated UUID for the upstream server.
1. Run `docker-compose up -d`. 

#### Clients

The bridge server exposes these proxy protocols:
* Shadowsocks
* VMESS
* HTTP
* SOCKS

##### Shadowsocks Protocol

Shadowsocks is a popular proxy protocol.
You can find many client apps to use the Shadowsocks proxy on your devices.
These are recommended client apps:
* [Qv2ray](https://qv2ray.net) (macOS, Linux and Windows)
* [Shadowsocks for macOS](https://github.com/shadowsocks/ShadowsocksX-NG/releases)
* [Shadowsocks for Linux](https://github.com/shadowsocks/shadowsocks-libev)
* [Shadowsocks for Windows](https://github.com/shadowsocks/shadowsocks-windows/releases)
* [Shadowsocks for Android](https://github.com/shadowsocks/shadowsocks-android/releases)
* [ShadowLink for iOS](https://apps.apple.com/us/app/shadowlink-shadowsocks-vpn/id1439686518)
* [Outline](https://getoutline.org/get-started/#step-3) (Supports Shadowsocks links)

###### Client configuration

```
IP Address: <BRIDGE-IP>
Port: 1210
Encryption/Method/Algorithm: aes-128-gcm
Password: <SHADOWSOCKS-PASSWORD>
```

You can run the following command to generate the Shadowsocks link.

```shell
echo "ss://$(echo -n METHOD:PASSWORD | base64)@IP:PORT"

# Example
echo "ss://$(echo -n aes-128-gcm:FR33DoM | base64)@13.13.13.13:1210"
# ss://YWVzLTEyOC1nY206RlIzM0RvTQ==@13.13.13.13:1210
```

##### VMESS Protocol

The VMESS proxy protocol is the recommended one.
It's the primary protocol that V2Ray provides.
These are recommended client apps:
* [Qv2ray](https://qv2ray.net) (macOS, Linux and Windows)
* [V2RayX for macOS](https://github.com/Cenmrev/V2RayX/releases)
* [v2ray-core for Linux](https://github.com/v2ray/v2ray-core)
* [v2rayN for Windows](https://github.com/2dust/v2rayN/releases)
* [ShadowLink for iOS](https://apps.apple.com/us/app/shadowlink-shadowsocks-vpn/id1439686518)
* [v2rayNG for Android](https://github.com/2dust/v2rayNG)

Client configuration:
```
IP Address: <BRIDGE-IP>
Port: 1310
ID/UUID/UserID: <BRIDGE-UUID>
Alter ID: 0
Level: 0
Security/Method/Encryption: aes-128-gcm
Network: TCP
```

##### HTTP & SOCKS Protocols

Moved here: [HTTP_SOCKS_PROTOCOLS.md](HTTP_SOCKS_PROTOCOLS.md)

### Docker images

We cannot pull docker images from Docker Hub here in Iran.
Therefore I've pushed the official V2Ray Docker image into the GitHub image registry.
If you prefer pulling the image from the Docker Hub, update the `docker-compose.yml` files.

```yaml
services:
  v2ray:
    image: ghcr.io/getimages/v2ray:latest
    # ...
```

* GitHub:
  * Image: ```ghcr.io/getimages/v2fly-core:v4.45.2```
  * URL: https://github.com/orgs/getimages/packages/container/package/v2fly-core
  * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`
* Docker Hub:
  * Image: ```v2fly/v2fly-core:v4.45.2```
  * URL: https://hub.docker.com/r/v2fly/v2fly-core/tags
  * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`
  
## Read more

* Read more about V2Ray: https://www.v2fly.org
* Read about V2Ray configurations: https://guide.v2fly.org

## P.S.

This repository is kind of forked from [v2ray-config-examples](https://github.com/xesina/v2ray-config-examples).
Thanks to [@xesina](https://github.com/xesina) and other contributors.
