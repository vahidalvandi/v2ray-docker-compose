# V2Ray Docker Compose

This repository contains V2Ray-based solutions for bypassing firewalls in restricted networks where direct access to upstream servers (servers with free internet access) is unavailable.

## Table of contents

  * [Server Solutions](#server-solutions)
    * [V2Ray Upsream and Relay Servers](#v2ray-upsream-and-relay-servers)
    * [V2Ray Behind CDN](#v2ray-behind-cdn)
    * [V2Ray as Relay for Outline](#v2ray-as-relay-for-outline)
  * [Client Applications](#client-applications)
    * [Shadowsocks Protocol](#shadowsocks-protocol)
    * [VMess Protocol](#vmess-protocol)
    * [HTTP and SOCKS Protocols](#http-and-socks-protocols)
  * [Links](#links)

## Server Solutions

### V2Ray Upsream and Relay Servers

The "V2Ray Upsream and Relay Servers" solution offers **high stability and speed** (depends on the network speeds of the relay and upstream servers).

The solution uses V2Ray on the upstream server, using the Shadowsocks protocol for communication with the relay server.
The relay server provides **Shadowsocks** protocol for users, in addition to Socks5 and HTTP protocols for the relay server's own use.

The Shadowsocks protocol is used because it operates on layer 4, making it very fast.
Additionally, there are many user-friendly client applications that support this protocol.

You will need two types of servers:
* **Upstream Server**: A server with access to the free internet, likely located in a foreign data center.
* **Relay Server**: A server that can connect to the upstream server and is accessible to users, likely located in the same region as the users.

The flow of V2Ray Upsream and Relay Servers:

```
Users <-> Relay Server <-> Upstream Server <-> Internet
```

**Step 1: Setup Upstream Server**

1. Install Docker and Docker-compose ([Official Documanetation](https://docs.docker.com/engine/install/#supported-platforms)).
1. Run `git clone https://github.com/miladrahimi/v2ray-docker-compose.git` to download this repository.
1. Run `cd v2ray-docker-compose/v2ray-upstream-server` to change the directory.
1. Replace `<UPSTREAM-PASSWORD>` in `v2ray.json` with a Shadowsocks password like `FR33DoM`.
1. Run `docker compose up -d`.
1. (Optional) Run `./../utils/bbr.sh` to setup BBR and speed up the server network.

**Step 2: Setup Relay Server**

1. Install Docker and Docker-compose ([Official Documanetation](https://docs.docker.com/engine/install/#supported-platforms)).
1. Run `git clone https://github.com/miladrahimi/v2ray-docker-compose.git` to download this repository.
1. Run `cd v2ray-docker-compose/v2ray-relay-server` to change the directory.
1. Replace the following variables in `v2ray.json` with appropriate values.
    * `<RELAY-PASSWORD>`: A password for Shadowsocks users like `FR33DoM`.
    * `<UPSTREAM-IP>`: The upstream server IP address (like `13.13.13.13`).
    * `<UPSTREAM-PASSWORD>`: The Shadowsocks password from the upstream server in the previous step.
1. Run `docker compose up -d`.
1. Run `./clients.py` to generate client configurations and links.
1. (Optional) Run `./../utils/bbr.sh` to setup BBR and speed up the server network.

### V2Ray Behind CDN

The "V2Ray Behind CDN" solution is recommended only if you don't have relay server to implement other solutions.

This solution provides **VMess** protocol over **Websockets + TLS + CDN** ([Read more](https://guide.v2fly.org/en_US/advanced/wss_and_web.html)) for users.

In this solution, you need an upstream server and a domain integrated with a CDN service:
* **Upstream Server**: A server with access to the free internet, likely located in a foreign data center.
* **CDN Service**: A Content Delivery Network service like [Cloudflare](//cloudflare.com) and [ArvanCloud](//arvancloud.ir).

The flow of V2Ray Behind CDN:

```
Users <-> CDN <-> Upstream Server <-> Internet
```

Follow these steps to set up V2Ray, Caddy (Web server) and CDN:

1. In the CDN panel, create an `A` record for the server IP with the proxy disabled.
1. Install Docker and Docker-compose ([Official Documanetation](https://docs.docker.com/engine/install/#supported-platforms)).
1. Run `git clone https://github.com/miladrahimi/v2ray-docker-compose.git` to download this repository.
1. Run `cd v2ray-docker-compose/v2ray-caddy-cdn` to change the directory.
1. Run `cat /proc/sys/kernel/random/uuid` to generate a UUID.
1. Replace `<UPSTREAM-UUID>` in `v2ray.json` with the generated UUID.
1. Replace `<EXAMPLE.COM>` in `caddy/Caddyfile` with your domain/subdomain.
1. Run `docker compose up -d`.
1. Visit your domain/subdomain in your web browser.
   Wait until the [homepage](https://github.com/miladrahimi/v2ray-docker-compose/blob/master/v2ray-caddy-cdn/caddy/web/index.html) is loaded.
1. In the CDN panel, enable the proxy option for the record created during the first step.
1. Run `./vmess.py` to generate client configuration link.
1. (Optional) Run `./../utils/bbr.sh` to setup BBR and speed up the server network.

create dns free in https://freedns.afraid.org/subdomain/

**Notes**

- If you prefer using NGINX as your web server, please refer to [V2Ray Behind CDN and NGINX](docs/V2RAY_NGINX_CDN.md).
- Some CDN services do not provide unlimited traffic with their free plans.
  Please check [CDN Free Plans](https://github.com/miladrahimi/v2ray-docker-compose/discussions/89).
- You can skip step 10 and keep the proxy off, but this could lead to quicker server blocking.

### V2Ray as Relay for Outline

The "V2Ray as Relay for Outline" solution is stable, fast, easy to set up, and **highly recommended**.

It allows you to use Outline proxy tools to support the **Shadowsocks** protocol and provides the user-friendly Outline Client application for users,
along with the Outline Manager app for setting up servers, creating and managing users, and tracking their traffic.

Read more in the [Outline Bridge Server](https://github.com/miladrahimi/outline-bridge-server) repository.

## Client Applications

### Shadowsocks Protocol

This is the list of recommended applications for Shadowsocks protocol:

* [Outline](https://getoutline.org/get-started/#step-3) for all platforms
* [ShadowsocksX-NG](https://github.com/shadowsocks/ShadowsocksX-NG/releases) for macOS
* [shadowsocks-libev](https://github.com/shadowsocks/shadowsocks-libev) for Linux
* [shadowsocks-windows](https://github.com/shadowsocks/shadowsocks-windows/releases)
* [shadowsocks-android](https://github.com/shadowsocks/shadowsocks-android/releases)
* [ShadowLink](https://apps.apple.com/us/app/shadowlink-shadowsocks-vpn/id1439686518) for iOS

### VMess Protocol

This is the list of recommended applications for VMess protocol:

* [Nekoray](https://github.com/MatsuriDayo/nekoray/releases) for macOS, Windows, and Linux
* [FoXray](https://foxray.org/#download) for macOS, iOS, and Android
* [V2Box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690) for macOS and iOS
* [V2Box](https://play.google.com/store/apps/details?id=dev.hexasoftware.v2box) for Android
* [ShadowLink](https://apps.apple.com/us/app/shadowlink-shadowsocks-vpn/id1439686518) for iOS
* [v2rayNG](https://github.com/2dust/v2rayNG) for Android
* [v2rayN](https://github.com/2dust/v2rayN/releases) for Windows

### HTTP and SOCKS Protocols

Moved to [HTTP & SOCKS Protocols](docs/HTTP_SOCKS.md).

## Links

* [Outline Bridge Server](https://github.com/miladrahimi/outline-bridge-server)
* [V2Ray Config Examples](https://github.com/xesina/v2ray-config-examples)
* [NekoRay Installer (for Linux)](https://github.com/ohmydevops/nekoray-installer)
* [V2Ray Ansible](https://github.com/ohmydevops/v2ray-ansible)
* [V2Fly (V2Ray)](https://www.v2fly.org)
* [V2Fly (V2Ray) configurations](https://guide.v2fly.org)
