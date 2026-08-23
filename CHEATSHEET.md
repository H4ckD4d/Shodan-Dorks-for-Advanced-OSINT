# Shodan Defensive OSINT Cheatsheet

> **Project owner:** h4ckd4d  
> Part of **Shodan Dorks for Advanced OSINT**, created and maintained by **h4ckd4d**.

Use only for assets you own, administer, or are explicitly authorized to assess.

## Core syntax

```text
filter:value
```

Quote values containing spaces:

```text
org:"Example Organization"
```

Combine filters:

```text
org:"Example Organization" port:443 has_ssl:true
```

## Network and ownership

```text
ip:203.0.113.10
net:"203.0.113.0/24"
asn:"AS64500"
org:"Example Organization"
hostname:"example.com"
country:US
port:443
```

## Service identification

```text
product:"nginx"
version:"1.24.0"
os:"Linux"
cpe:"cpe:/a:example:product"
```

## HTTP

```text
http.title:"Example Portal"
http.status:200
http.component:"nginx"
http.waf:"Cloudflare"
has_screenshot:true
```

## TLS / certificates

```text
has_ssl:true
ssl.version:"TLSv1.3"
ssl.cert.subject.cn:"example.com"
ssl.cert.issuer.cn:"Example CA"
ssl.cert.fingerprint:"FINGERPRINT"
ssl.jarm:"JARM_HASH"
ssl.ja3s:"JA3S_HASH"
```

## SSH

```text
port:22
ssh.fingerprint:"FINGERPRINT"
```

## Exposure metadata

```text
has_vuln:true
vuln:"CVE-YYYY-NNNN"
tag:"example-tag"
```

Treat vulnerability metadata as a lead to validate, not proof that exploitation is possible.

## Defensive workflow

1. Establish a written scope: domains, ASNs, CIDRs, and organizations you are authorized to review.
2. Start broad with `org`, `asn`, or `net`.
3. Narrow by `port`, `product`, `hostname`, or HTTP/TLS metadata.
4. Record result timestamp and Shodan `last_update`/banner dates where available.
5. Validate ownership and freshness before acting on a finding.
6. Remediate through normal administrative channels; do not interact with third-party systems.

## Current-reference note

Shodan's authoritative filter list can change. Validate filters using the official API endpoint:

`/shodan/host/search/filters`

Reference reviewed: **August 23, 2026**.

---

**Original creator and project owner: h4ckd4d**

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
