# HTTP and Web Queries

Use these examples only within an owned or explicitly authorized scope.

## HTTP status

```text
net:"203.0.113.0/24" http.status:200
```

## HTTP title

```text
net:"203.0.113.0/24" http.title:"Example Portal"
```

## Web components

```text
net:"203.0.113.0/24" http.component:"nginx"
```

Component-category searches can help group technology classes:

```text
net:"203.0.113.0/24" http.component_category:"web-framework"
```

Exact category values depend on Shodan's detected metadata.

## WAF metadata

```text
net:"203.0.113.0/24" http.waf:"Example WAF"
```

Treat WAF detection as an observation rather than proof of enforcement coverage.

## Favicon pivots

When you already know the favicon hash for an application you own, it can help locate related deployments:

```text
net:"203.0.113.0/24" http.favicon.hash:123456789
```

Hash matching can produce shared-product matches. Corroborate ownership before drawing conclusions.

## HTML and robots hashes

```text
net:"203.0.113.0/24" http.html_hash:123456789
net:"203.0.113.0/24" http.robots_hash:123456789
```

These are useful for grouping similar services inside an authorized inventory.

## Screenshots

```text
net:"203.0.113.0/24" has_screenshot:true
```

Screenshots may be historical. Do not assume the observed interface is still live.

## Combined examples

```text
net:"203.0.113.0/24" port:443 http.status:200
net:"203.0.113.0/24" has_ssl:true http.title:"Example Portal"
net:"203.0.113.0/24" has_screenshot:true http.status:200
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
