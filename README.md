# Shodan Dorks for Advanced OSINT

> **Project owner and maintainer:** **H4ckD4d**  
> Original project by **H4ckD4d**. Please preserve project attribution when redistributing or adapting this repository.

A curated, defensive reference for Shodan search syntax, filters, and OSINT workflows focused on authorized asset discovery, exposure auditing, service identification, and Internet-facing attack-surface awareness.

> **Scope:** Use this repository only on systems you own, administer, or are explicitly authorized to assess. Shodan indexes public Internet telemetry; public visibility does not imply permission to access or test a system.

## Why this project exists

Shodan queries are most useful when they are precise, reproducible, and grounded in documented filters. This repository separates:

- **Official Shodan filters** — fields accepted by the Shodan search engine.
- **Banner search terms** — free-text terms searched in collected service banners.
- **Defensive workflows** — practical ways to inventory and review authorized Internet-facing assets.

## Quick start

Shodan filters use the form:

```text
filter:value
```

Examples:

```text
org:"Example Organization"
net:"203.0.113.0/24"
port:443 country:US
product:"nginx" org:"Example Organization"
http.title:"Example Portal" org:"Example Organization"
has_ssl:true org:"Example Organization"
```

Combine filters to reduce noise:

```text
org:"Example Organization" port:443 has_ssl:true
```

For CLI searches containing quotes, wrap the full query in an additional pair of shell quotes:

```bash
shodan search 'org:"Example Organization" port:443'
```

## Repository map

### Documentation

- [`docs/getting-started.md`](docs/getting-started.md) — search fundamentals and safe workflow.
- [`docs/filters-reference.md`](docs/filters-reference.md) — curated official filter reference.
- [`docs/osint-methodology.md`](docs/osint-methodology.md) — repeatable defensive OSINT methodology.
- [`docs/cli-api.md`](docs/cli-api.md) — CLI/API usage for authorized inventory and validation.
- [`CHEATSHEET.md`](CHEATSHEET.md) — compact quick-reference sheet.

### Query collections

- [`dorks/network.md`](dorks/network.md) — network, ASN, geography, service, and product filters.
- [`dorks/web.md`](dorks/web.md) — HTTP metadata and web-technology discovery.
- [`dorks/ssl-tls.md`](dorks/ssl-tls.md) — certificate and TLS-focused searches.
- [`dorks/dns-hostnames.md`](dorks/dns-hostnames.md) — hostname and domain-oriented pivots.
- [`dorks/ssh.md`](dorks/ssh.md) — SSH inventory and fingerprint review.
- [`dorks/cloud.md`](dorks/cloud.md) — cloud-hosted asset inventory patterns.
- [`dorks/databases.md`](dorks/databases.md) — defensive database-service inventory.
- [`dorks/iot-ics.md`](dorks/iot-ics.md) — conservative IoT/ICS exposure review using documented filters and banner text.

### Defensive examples

- [`examples/asset-discovery.md`](examples/asset-discovery.md) — authorized asset-discovery workflow.

## Core filter families

| Category | Useful filters |
| --- | --- |
| Network | `ip`, `net`, `asn`, `port`, `hostname` |
| Ownership / location | `org`, `isp`, `country`, `city`, `region`, `state` |
| Service | `product`, `version`, `os`, `cpe` |
| HTTP | `http.title`, `http.status`, `http.component`, `http.component_category`, `http.waf` |
| TLS / SSL | `has_ssl`, `ssl`, `ssl.version`, `ssl.cert.subject.cn`, `ssl.cert.issuer.cn`, `ssl.cert.fingerprint`, `ssl.jarm`, `ssl.ja3s` |
| Screenshots | `has_screenshot`, `screenshot.label` |
| SSH | `ssh.fingerprint` |
| Exposure metadata | `tag`, `vuln`, `has_vuln` |

The authoritative filter set can change. Shodan exposes the current list programmatically through `/shodan/host/search/filters`.

## Important distinction: filters vs. banner text

A string that appears in a Shodan banner is not automatically a valid search filter. Vendor, protocol, product, or industrial metadata may be searchable as banner text or represented through another documented field. This project does not label undocumented field names as official filters.

## Validation policy

Before adding a new filter to this repository:

1. Confirm it in the official Shodan filter reference or API.
2. Verify the expected value format.
3. Prefer examples scoped to owned or explicitly authorized assets.
4. Document plan/API limitations when known.
5. Add the validation date to significant reference updates.

**Reference validation:** August 23, 2026.

## Official references

- Shodan Help Center — Search Query Fundamentals: https://help.shodan.io/the-basics/search-query-fundamentals
- Shodan Developer API: https://developer.shodan.io/api
- Shodan filter reference: https://trends.shodan.io/search/filters
- Shodan Datapedia: https://datapedia.shodan.io/

## Ownership and credits

**H4ckD4d** is the original creator, project owner, and primary maintainer of **Shodan Dorks for Advanced OSINT**.

See [`CREDITS.md`](CREDITS.md) for project attribution and contributor-credit conventions.

## Contributing

Corrections and additions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting changes.

## Security and responsible use

See [`SECURITY.md`](SECURITY.md).

## License

Released under the MIT License. See [`LICENSE`](LICENSE). The license preserves the copyright notice while permitting reuse under its terms.

---

**Shodan Dorks for Advanced OSINT** — created and maintained by **H4ckD4d**.  
Cybersecurity · OSINT · Threat Intelligence · Defensive Security
