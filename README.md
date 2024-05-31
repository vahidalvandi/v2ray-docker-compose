# V2Ray Docker Compose

This repository contains V2Ray-based solutions for bypassing firewalls in restricted networks where direct access to upstream servers (servers with free internet access) is unavailable.

## Table of contents

  * [Server Solutions](#server-solutions)
    * [V2Ray Upsream and Relay Servers](#v2ray-upsream-and-relay-servers)
    * [V2Ray Behind a CDN Service](#v2ray-behind-a-cdn-service)
    * [V2Ray as Relay for Outline](#v2ray-as-relay-for-outline)
  * [Client Applications](#client-applications)
    * [Shadowsocks Protocol](#shadowsocks-protocol)
    * [VMess Protocol](#vmess-protocol)
    * [HTTP and SOCKS Protocols](#http-and-socks-protocols)
  * [More](#more)

## Server Solutions

### V2Ray Upsream and Relay Servers

The "V2Ray Upsream and Relay Servers" solution offers **high stability and speed** (depends on the network speeds of the relay and upstream servers).

The solution uses V2Ray on the upstream server, using the VMess protocol (over Websockets) for communication with the relay server.
The relay server provides **Shadowsocks** protocol for users, in addition to Socks5 and HTTP protocols for the relay server's own use.

You will need two types of servers:
* **Upstream Server**: A server with access to the free internet, likely located in a foreign data center.
* **Relay Server**: A server that can connect to the upstream server and is accessible to users, likely located in the same region as the users.

The flow of V2Ray Upsream and Relay Servers:

```
Users <-(Shadowsocks)-> Relay Server <-(VMess)-> Upstream Server <-> Internet
```

**Step 1: Setup Upstream Server**

1. Install Docker and Docker-compose ([Official Documanetation](https://docs.docker.com/engine/install/#supported-platforms)).
1. Run `git clone https://github.com/miladrahimi/v2ray-docker-compose.git` to download this repository.
1. Run `./utils/bbr.sh` to setup BBR in order to speed up server network.
1. Run `cd v2ray-upstream-server` to change the directory.
1. Run `cat /proc/sys/kernel/random/uuid` to generate a UUID.
1. Replace `<UPSTREAM-UUID>` in `v2ray.json` with the generated UUID.
1. Run `docker-compose up -d`.

**Step 2: Setup Relay Server**

1. Install Docker and Docker-compose ([Official Documanetation](https://docs.docker.com/engine/install/#supported-platforms)).
1. Run `git clone https://github.com/miladrahimi/v2ray-docker-compose.git` to download this repository.
1. Run `./utils/bbr.sh` to setup BBR in order to speed up server network.
1. Run `cd v2ray-relay-server` to change the directory.
1. Replace the following variables in `v2ray.json` with appropriate values.
    * `<SHADOWSOCKS-PASSWORD>`: A password for Shadowsocks users like `FR33DoM`.
    * `<UPSTREAM-IP>`: The upstream server IP address (like `13.13.13.13`).
    * `<UPSTREAM-UUID>`: The upstream server UUID from the previous step.
1. Run `docker-compose up -d`.
1. Run `./clients.py` to generate client configurations and links.

### V2Ray Behind CDN

The "V2Ray Behind CDN" solution is recommended only if you don't have relay server to implement other solutions.

This solution provides **VMess over Websockets + TLS + CDN** ([Read more](https://guide.v2fly.org/en_US/advanced/wss_and_web.html)) for users.

In this solution, you need upstream server and a domain added to a CDN service.
* **Upstream Server**: A server with access to the free internet, likely located in a foreign data center.
* **CDN Service**: A Content Delivery Network service like [Cloudflare](//cloudflare.com) and [ArvanCloud](//arvancloud.ir).

The flow of V2Ray Behind CDN:

```
Users <-(VMess)-> CDN <-> Upstream Server <-> Internet
```

Follow these steps to set up V2Ray, Caddy (Web server) and CDN:

1. On the CDN panel, create an `A` record pointing to the server IP with the proxy option turned off.
1. Install Docker and Docker-compose ([Official Documanetation](https://docs.docker.com/engine/install/#supported-platforms)).
1. Run `git clone https://github.com/miladrahimi/v2ray-docker-compose.git` to download this repository.
1. Run `./utils/bbr.sh` to setup BBR in order to speed up server network.
1. Run `cd v2ray-caddy-cdn` to change the directory.
1. Run `cat /proc/sys/kernel/random/uuid` to generate a UUID.
1. Replace `<UPSTREAM-UUID>` in `v2ray.json` with the generated UUID.
1. Replace `<EXAMPLE.COM>` in `caddy/Caddyfile` with your domain/subdomain.
1. Run `docker-compose up -d`.
1. Visit your domain/subdomain in your web browser.
   Wait until the [homepage](https://github.com/miladrahimi/v2ray-docker-compose/blob/master/v2ray-caddy-cdn/caddy/web/index.html) is loaded.
1. On the CDN panel, turn the proxy option on for the record created in the first step.
1. Run `./vmess.py` to generate client configuration (link).

**Notes**
- If you prefer using NGINX as your web server, please refer to [V2RAY_NGINX_CDN](docs/V2RAY_NGINX_CDN.md).
- Some CDN services do not provide unlimited traffic with their free plans.
  Please check [CDN Free Plans](https://github.com/miladrahimi/v2ray-docker-compose/discussions/89).
- You can skip step 10 and keep the proxy off, but this could lead to quicker server blocking.

### V2Ray as Relay for Outline

This **highly recommended** solution is stable and easy to set up.
Using the Outline Manager app, you can setup servers, create and manage users and track their traffic.
It supports **Shadowsocks** protocol and offers the user-friendly Outline client application.

Read more: [Outline Bridge Server](https://github.com/miladrahimi/outline-bridge-server)

## Client Applications

### Shadowsocks Protocol

This is the list of recommended applications to use the Shadowsocks protocol:

* [Outline](https://getoutline.org/get-started/#step-3) for all platforms
* [ShadowsocksX-NG](https://github.com/shadowsocks/ShadowsocksX-NG/releases) for macOS
* [shadowsocks-libev](https://github.com/shadowsocks/shadowsocks-libev) for Linux
* [shadowsocks-windows](https://github.com/shadowsocks/shadowsocks-windows/releases)
* [shadowsocks-android](https://github.com/shadowsocks/shadowsocks-android/releases)
* [ShadowLink](https://apps.apple.com/us/app/shadowlink-shadowsocks-vpn/id1439686518) for iOS

### VMess Protocol

This is the list of recommended applications to use the VMess protocol:

* [Nekoray](https://github.com/MatsuriDayo/nekoray/releases) for macOS, Windows, and Linux
* [FoXray](https://foxray.org/#download) for macOS, iOS, and Android
* [V2Box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690) for macOS and iOS
* [V2Box](https://play.google.com/store/apps/details?id=dev.hexasoftware.v2box) for Android
* [ShadowLink](https://apps.apple.com/us/app/shadowlink-shadowsocks-vpn/id1439686518) for iOS
* [v2rayNG](https://github.com/2dust/v2rayNG) for Android
* [v2rayN](https://github.com/2dust/v2rayN/releases) for Windows

### HTTP and SOCKS Protocols

Moved here: [HTTP_SOCKS](docs/HTTP_SOCKS.md)

## More

* [Outline Bridge Server](https://github.com/miladrahimi/outline-bridge-server)
* [V2Ray Config Examples](https://github.com/xesina/v2ray-config-examples)
* [NekoRay Installer (for Linux)](https://github.com/ohmydevops/nekoray-installer)
* [V2Ray Ansible](https://github.com/ohmydevops/v2ray-ansible)
* [V2Fly (V2Ray)](https://www.v2fly.org)
* [V2Fly (V2Ray) configurations](https://guide.v2fly.org)
