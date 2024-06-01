# V2Ray Behind CDN and NGINX

This solution is similar to [V2Ray Behind CDN](https://github.com/miladrahimi/v2ray-docker-compose/blob/master/README.md#v2ray-behind-cdn),
which uses Caddy as the web server and is easier to set up.

Follow these steps to set up V2Ray, NGINX (Web server) and CDN:

1. In the CDN panel, create an `A` record for the server IP with the proxy disabled.
1. Install Docker and Docker-compose ([Official Documanetation](https://docs.docker.com/engine/install/#supported-platforms)).
1. Run `git clone https://github.com/miladrahimi/v2ray-docker-compose.git` to download this repository.
1. Run `cd v2ray-docker-compose/v2ray-nginx-cdn` to change the directory.
1. Run `cat /proc/sys/kernel/random/uuid` to generate a UUID.
1. Replace `<UPSTREAM-UUID>` in `v2ray.json` with the generated UUID.
1. Replace `YOUR.DOMAIN.COM` in `docker-compose.yml` with your domain/subdoamin.
1. Replace `YOUR@EMAIL.COM` in `docker-compose.yml` with your email (for Let’s Encrypt).
1. Run `docker-compose up -d`.
1. Visit your domain/subdomain in your web browser.
1. In the CDN panel, enable the proxy option for the record created during the first step.
1. Run `./vmess.py` to generate client configuration (link).
1. (Optional) Run `./../utils/bbr.sh` to setup BBR and speed up the server network.
