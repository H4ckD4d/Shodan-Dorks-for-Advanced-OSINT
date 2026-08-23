# Shodan Filter Reference

Validated against official Shodan documentation on **August 23, 2026**.

> The main Shodan search engine may support filters beyond those shown by Shodan Trends. For authoritative runtime discovery, use the Shodan API endpoint `/shodan/host/search/filters`.

## General filters

| Filter | Purpose | Example |
| --- | --- | --- |
| `all` | Match across indexed search data | `all:"Example"` |
| `asn` | Autonomous System Number | `asn:"AS64500"` |
| `city` | City | `city:"San Diego"` |
| `country` | Two-letter country code | `country:US` |
| `cpe` | Common Platform Enumeration | `cpe:"cpe:/a:example:product"` |
| `has_ipv6` | Assets with IPv6 metadata | `has_ipv6:true` |
| `hash` | Banner hash | `hash:123456789` |
| `hostname` | Hostname | `hostname:"example.com"` |
| `ip` | Specific IP address | `ip:"203.0.113.10"` |
| `isp` | Internet service provider | `isp:"Example ISP"` |
| `net` | CIDR network range | `net:"203.0.113.0/24"` |
| `org` | Organization | `org:"Example Organization"` |
| `os` | Operating system metadata | `os:"Linux"` |
| `port` | Service port | `port:443` |
| `product` | Identified product | `product:"nginx"` |
| `region` | Geographic region | `region:"California"` |
| `state` | Geographic state | `state:"California"` |
| `tag` | Shodan-assigned tag | `tag:cloud` |
| `version` | Product version | `version:"1.0"` |
| `title` | Legacy title field; prefer `http.title` for HTTP | `title:"Example"` |
| `has_ssl` | Services with SSL/TLS data | `has_ssl:true` |
| `has_screenshot` | Services with screenshots | `has_screenshot:true` |
| `vuln` | Vulnerability identifier metadata | `vuln:"CVE-YYYY-NNNN"` |
| `has_vuln` | Services with vulnerability metadata | `has_vuln:true` |

## HTTP filters

| Filter | Purpose |
| --- | --- |
| `http.component` | Detected web technology/component |
| `http.component_category` | Component category |
| `http.favicon.hash` | Favicon hash |
| `http.html_hash` | HTML-body hash |
| `http.robots_hash` | `robots.txt` hash |
| `http.securitytxt` | Security.txt-related data |
| `http.status` | HTTP status code |
| `http.title` | HTTP page title |
| `http.waf` | Detected web application firewall |

Examples:

```text
org:"Example Organization" http.status:200
org:"Example Organization" http.title:"Example Portal"
org:"Example Organization" http.component:"nginx"
```

## Screenshot filters

| Filter | Purpose |
| --- | --- |
| `screenshot.label` | Shodan screenshot classification label |

Example:

```text
org:"Example Organization" has_screenshot:true
```

## SSL/TLS filters

| Filter | Purpose |
| --- | --- |
| `ssl` | Search SSL/TLS metadata |
| `ssl.alpn` | ALPN protocol |
| `ssl.version` | TLS/SSL protocol version |
| `ssl.cert.fingerprint` | Certificate fingerprint |
| `ssl.cert.issuer.cn` | Certificate issuer common name |
| `ssl.cert.subject.cn` | Certificate subject common name |
| `ssl.cert.serial` | Certificate serial number |
| `ssl.jarm` | JARM fingerprint |
| `ssl.ja3s` | JA3S server fingerprint |

Examples:

```text
org:"Example Organization" has_ssl:true
org:"Example Organization" ssl.cert.subject.cn:"example.com"
org:"Example Organization" ssl.cert.issuer.cn:"Let's Encrypt"
```

## SSH filters

| Filter | Purpose |
| --- | --- |
| `ssh.fingerprint` | SSH host-key fingerprint |

Example:

```text
org:"Example Organization" ssh.fingerprint:"SHA256:..."
```

## Filters removed from the old README

The previous README presented several names as official filters without sufficient documentation. They are deliberately **not** listed as official filters here unless validated through current Shodan documentation/API.

Examples include:

```text
ics.vendor
ics.product
ics.version
modbus.function
bacnet.device
iot
manufacturer
firmware
is_public
is_upnp
tags
```

Some underlying concepts may still appear in banners, tags, Datapedia properties, protocol-specific metadata, or other Shodan products. That does not make these exact strings valid search filters.

## Programmatic validation

Shodan provides an API method for listing currently supported search filters:

```text
GET /shodan/host/search/filters
```

It also provides a query-tokenization endpoint:

```text
GET /shodan/host/search/tokens
```

Use these when maintaining this repository.

## Primary references

- https://developer.shodan.io/api
- https://trends.shodan.io/search/filters
- https://help.shodan.io/the-basics/search-query-fundamentals
- https://datapedia.shodan.io/
