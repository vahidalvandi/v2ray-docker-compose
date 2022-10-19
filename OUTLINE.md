# Outline

[Outline](https://getoutline.org) is a cross-platform proxy client created by Google.
It supports the Shadowsocks protocol and provides a VPN-like proxy to send all your network traffic through the proxy.

## Download

Outline dowload links are available at the link below.

[https://getoutline.org/get-started/#step-3](https://getoutline.org/get-started/#step-3)

## Configuration

Outline imports proxy configurations using Shadowsocks links (`ss://...`).
You can run the following command to generate Shadowsocks links from your proxy configurations.

```shell
echo "ss://$(echo -n METHOD:PASSWORD | base64)@IP:PORT"

# Example
echo "ss://$(echo -n aes-128-gcm:FR33DoM | base64)@13.13.13.13:1210"
# ss://YWVzLTEyOC1nY206RlIzM0RvTQ==@13.13.13.13:1210
```
