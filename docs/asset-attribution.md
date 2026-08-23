# Asset Attribution and Ownership Confidence

> **Project owner:** Chris Cruz | h4ckd4d

## Purpose

Asset attribution answers one of the most important questions in external attack-surface analysis:

> Does this Internet-visible asset actually belong to, represent, or support the organization in scope?

Incorrect attribution creates false positives and can lead analysts outside authorized boundaries.

## Evidence sources

### Strong evidence

- internal CMDB or authoritative asset inventory;
- cloud-account resource inventory;
- organizational CIDR ownership;
- organizational ASN ownership;
- authoritative DNS controlled by the organization.

### Supporting evidence

- certificate subject/SAN relationship;
- stable hostname relationship;
- consistent organization metadata;
- long-lived DNS relationship;
- documented third-party hosting relationship.

### Weak evidence

- reverse DNS alone;
- banner keyword alone;
- public cloud ASN alone;
- search-engine indexing alone;
- shared certificate or shared hosting without tenant evidence.

## Ownership-confidence score

| Level | Meaning | Typical evidence |
| --- | --- | --- |
| High | Strong evidence that the asset is in scope | CMDB, owned CIDR, cloud inventory, authoritative DNS |
| Medium | Likely relationship requiring confirmation | certificate/SAN, stable hostname, consistent metadata |
| Low | Candidate only | banner keyword, shared host, reverse DNS |
| Rejected | Evidence indicates unrelated third party | mismatched ownership or confirmed shared infrastructure |

## Recommended analyst record

```json
{
  "asset": "203.0.113.10",
  "asset_type": "ip",
  "ownership_confidence": "high",
  "evidence": [
    "owned-cidr",
    "authoritative-dns",
    "internal-inventory"
  ],
  "analyst_status": "validated"
}
```

## Attribution workflow

1. Start from an authorized scope boundary.
2. Collect public observations.
3. Check internal ownership records.
4. Compare DNS and certificate relationships.
5. Review ASN/RDAP context.
6. Account for CDN, SaaS, MSP, and cloud-provider infrastructure.
7. Assign confidence.
8. Escalate only after ownership is reasonably established.

## Common false-positive patterns

- public cloud IP reassignment;
- CDN edge addresses;
- SaaS platforms using customer domains;
- expired DNS records;
- old certificates;
- acquired/divested companies;
- historical hosting providers;
- shared reverse DNS;
- third-party security gateways.

## Rule

**Relationship is not ownership. Ownership is not authorization.**

Both must be established independently.

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
