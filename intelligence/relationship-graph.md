# Asset Relationship Graph

> **Project owner:** Chris Cruz | h4ckd4d

Internet exposure analysis becomes more reliable when assets are modeled as relationships instead of isolated search results.

## Graph concept

```text
Organization
   ├── owns ── ASN
   │             └── announces ── CIDR
   │                                └── contains ── IP
   │                                               └── exposes ── Service
   ├── owns ── Domain
   │             ├── resolves_to ── IP
   │             └── uses ── Certificate
   └── operates ── Cloud Resource
                    └── publishes ── IP / Hostname
```

## Supported relationship types

The normalized asset schema currently supports:

- `resolves_to`
- `belongs_to`
- `served_by`
- `certifies`
- `hosts`
- `observed_on`
- `related_to`

Each relationship may carry a confidence value from 0 to 100.

## Why graph thinking matters

A single hostname match can be misleading. A relationship becomes stronger when independent evidence converges.

Example:

```text
hostname → resolves_to → IP
certificate → certifies → hostname
IP → belongs_to → approved CIDR
CIDR → belongs_to → approved ASN
```

When several independent relationships support the same attribution, ownership confidence can increase.

## Defensive pivoting

Pivots should remain anchored to an authorized scope. The graph is used to answer questions such as:

- Which approved domains resolve to unexpected public IPs?
- Which certificates are shared across approved services?
- Which Internet-facing services are associated with a confirmed asset?
- Which observations have only weak relationships to the organization?
- Which assets disappeared or appeared between two baselines?

## Relationship confidence

Suggested guidance:

- **95–100:** authoritative internal inventory or control-plane evidence.
- **80–94:** strong authoritative DNS, owned CIDR, or validated certificate relationship.
- **60–79:** multiple consistent external signals.
- **40–59:** plausible but incomplete relationship.
- **1–39:** weak pivot requiring analyst review.

## Guardrail

Relationship discovery does not authorize interaction with an asset. Graph edges represent evidence and context, not permission.

---

**Internet Exposure Intelligence Framework by h4ckd4d.**

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
