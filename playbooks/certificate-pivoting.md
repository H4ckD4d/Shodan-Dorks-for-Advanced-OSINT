# Certificate Pivoting Playbook

> **Project owner:** h4ckd4d

## Objective

Use TLS certificate metadata as supporting evidence for defensive asset discovery and relationship analysis within an authorized scope.

## Why certificates matter

Certificates can connect hostnames, services, and infrastructure through subject names, SANs, issuers, and fingerprints. They are useful correlation evidence but should not be treated as proof of current ownership by themselves.

## Shodan-oriented pivots

Examples for documentation-safe domains:

```text
ssl.cert.subject.cn:"example.com"
ssl.cert.issuer.cn:"Example CA"
has_ssl:true hostname:"example.com"
```

When a known certificate fingerprint exists in an authorized inventory, it can be used to identify matching observations:

```text
ssl.cert.fingerprint:"FINGERPRINT"
```

## Workflow

1. Start from a domain or certificate already confirmed in scope.
2. Review certificate subject and SAN relationships.
3. Compare candidate hostnames with authoritative DNS.
4. Compare candidate IPs with owned CIDRs, ASNs, and cloud inventory.
5. Check certificate validity dates and observation timestamps.
6. Assign ownership confidence.
7. Add validated relationships to the asset graph or baseline.

## Interpretation risks

- expired certificates;
- certificate reuse;
- shared hosting;
- managed certificate services;
- CDN certificates;
- wildcard certificates;
- historical infrastructure;
- certificate transparency entries that no longer represent active services.

## Analyst rule

Certificate correlation is a **relationship signal**, not automatic ownership proof.

---

**Shodan Dorks for Advanced OSINT — created and maintained by h4ckd4d.**

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
