# DNS and Hostname Discovery

> **Project owner:** H4ckD4d  
> Use only for owned or explicitly authorized infrastructure.

Shodan is not a full passive-DNS platform, but hostname metadata can be useful when reviewing an authorized external asset inventory.

## Exact hostname

```text
hostname:"example.com"
```

## Hostname plus organization

```text
hostname:"example.com" org:"Example Organization"
```

## Hostname plus service

```text
hostname:"example.com" port:443
```

## Organization assets with hostname metadata

```text
org:"Example Organization" hostname:"example.com"
```

## TLS pivot for an owned domain

Certificate metadata can complement hostname results:

```text
ssl.cert.subject.cn:"example.com" org:"Example Organization"
```

Do not assume every certificate or hostname match is currently owned by the same organization. Historical hosting, shared infrastructure, CDNs, acquisitions, and stale telemetry can create false associations.

## Review checklist

- confirm the domain is in scope;
- compare results with authoritative DNS and cloud inventories;
- note shared hosting/CDN infrastructure;
- record timestamps;
- verify ownership before remediation.

---

**Original creator and project owner: H4ckD4d**
