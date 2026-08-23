# Network and Service Queries

These examples are intended for owned or explicitly authorized infrastructure.

## Scope by network

```text
net:"203.0.113.0/24"
```

## Scope by ASN

```text
asn:"AS64500"
```

## Scope by organization

```text
org:"Example Organization"
```

Organization strings can be inconsistent. Corroborate results with known netblocks, ASN data, DNS, or internal inventories.

## Port discovery inside scope

```text
net:"203.0.113.0/24" port:443
net:"203.0.113.0/24" port:22
```

## Product discovery inside scope

```text
net:"203.0.113.0/24" product:"nginx"
net:"203.0.113.0/24" product:"OpenSSH"
```

## Operating-system metadata

```text
net:"203.0.113.0/24" os:"Linux"
```

OS identification is metadata and may be incomplete or inaccurate.

## Hostname pivots

```text
hostname:"example.com"
```

Combine with a known scope when possible:

```text
net:"203.0.113.0/24" hostname:"example.com"
```

## Geographic filters

```text
country:US
city:"San Diego"
state:"California"
```

Geolocation is approximate and should not be treated as authoritative physical location.

## Useful combinations

```text
net:"203.0.113.0/24" port:443 has_ssl:true
net:"203.0.113.0/24" product:"nginx" port:443
asn:"AS64500" country:US
```

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
