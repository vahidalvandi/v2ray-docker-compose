# V2Ray Docker Compose

This repository introduces two V2Ray-based solutions to bypass censorship in highly restricted networks
without direct access to an upstream server (a server with access to free Internet).

## Documentation

### Solutions

#### Using Bridge Server

This solution needs these two servers:

* Upstream Server: A server that has access to the free Internet.
* Bridge Server: A server that is available to clients and has access to the upstream server.

```
(Client) <-> [ Bridge Server ] <-> [ Upstream Server ] <-> (Internet)
```

#### Using CDN Service

This solution needs only one server (upstream server) and a domain/subdomain.

* Upstream Server: A server that has free access to the Internet.
* CDN Service: A Content delivery network like [Cloudflare](//cloudflare.com) or [ArvanCloud](//arvancloud.ir).

```
(Client) <-> [ CDN Service ] <-> [ Upstream Server ] <-> (Internet)
```

### Setup Using Bridge Server

#### Upstream Server

1. Install Docker and Docker-compose.
1. Copy the `v2ray-upstream-server` directory into the upstream server.
1. Run ```cat /proc/sys/kernel/random/uuid``` command to generate a UUID.
1. Replace `<UPSTREAM-UUID>` in the `config/config.json` file with the generated UUID.
1. Run `docker-compose up -d`.

#### Bridge Server

1. Install Docker and Docker-compose.
1. Copy the `v2ray-bridge-server` directory into the bridge server.
1. Replace the following variables in the `config/config.json` file with appropriate values.
    * `<SHADOWSOCKS-PASSWORD>`: A password for Shadowsocks users like `FR33DoM`.
    * `<BRIDGE-UUID>`: A new UUID for bridge server (Run ```cat /proc/sys/kernel/random/uuid```).
    * `<UPSTREAM-IP>`: The upstream server IP address like `13.13.13.13`.
    * `<UPSTREAM-UUID>`: The generated UUID for the upstream server.
1. Run `docker-compose up -d`. 
1. (Optional) You can run `./v2ray-bridge-server/clients.py` to generate client configurations and links.

### Setup Using CDN Service

1. Create an `A` record in the CDN pointing to your server IP address with the proxy option off.
1. Install Docker and Docker-compose.
1. Copy the `v2ray-cdn-ready` directory into the upstream server.
1. Run ```cat /proc/sys/kernel/random/uuid``` command to generate a UUID.
1. Replace `<UPSTREAM-UUID>` in the `v2ray/config/config.json` file with the generated UUID.
1. Replace `<EXAMPLE.COM>` in the `caddy/Caddyfile` file with your domain/subdoamin.
1. Run `docker-compose up -d`.
1. Visit your domain/subdomain in your web browser, and wait for it to load the default HTML file.
1. Turn the proxy option on in the CDN for the record.
1. Run `./vmess.py` to generate VMESS url for your client application.

### Client Applications

#### VMESS Protocol

The VMESS proxy protocol is the primary protocol that V2Ray (V2Fly) servers provide.
We recommend these client applications:
* [V2RayX for macOS](https://github.com/Cenmrev/V2RayX/releases)
* [v2ray-core for Linux](https://github.com/v2ray/v2ray-core)
* [Qv2ray for Windows](https://qv2ray.net)
* [ShadowLink for iOS](https://apps.apple.com/us/app/shadowlink-shadowsocks-vpn/id1439686518)
* [v2rayNG for Android](https://github.com/2dust/v2rayNG)

#### Shadowsocks Protocol

Shadowsocks is a popular proxy protocol with a variety of client applications.
We recommend these client applications:
* [Outline](https://getoutline.org/get-started/#step-3)
* [Shadowsocks for macOS](https://github.com/shadowsocks/ShadowsocksX-NG/releases)
* [Shadowsocks for Linux](https://github.com/shadowsocks/shadowsocks-libev)
* [Shadowsocks for Windows](https://github.com/shadowsocks/shadowsocks-windows/releases)
* [Shadowsocks for Android](https://github.com/shadowsocks/shadowsocks-android/releases)
* [ShadowLink for iOS](https://apps.apple.com/us/app/shadowlink-shadowsocks-vpn/id1439686518)

#### HTTP/HTTPS & SOCKS Protocols

Moved here: [HTTP_SOCKS.md](HTTP_SOCKS.md)

### Tips

* Some hostings might ban your proxy traffic. Use an appropriate hosting.
* Some Internet providers might ban your proxy traffic. Changin AlterID could be helpful.
  See [#57](https://github.com/miladrahimi/v2ray-docker-compose/issues/57).

### Docker images

* GitHub:
  * Image: ```ghcr.io/getimages/v2fly-core:v4.45.2```
  * URL: https://github.com/orgs/getimages/packages/container/package/v2fly-core
  * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`
* Docker Hub:
  * Image: ```v2fly/v2fly-core:v4.45.2```
  * URL: https://hub.docker.com/r/v2fly/v2fly-core/tags
  * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`

## More

* [Docker Compose files to run an Outline bridge server](https://github.com/miladrahimi/outline-bridge-server)
* [V2Ray Config Examples](https://github.com/xesina/v2ray-config-examples)
* [Setup V2Ray servers using Ansible](https://github.com/ohmydevops/v2ray-ansible)
* [Read more about V2Fly](https://www.v2fly.org)
* [Read more about V2Fly configurations](https://guide.v2fly.org)
