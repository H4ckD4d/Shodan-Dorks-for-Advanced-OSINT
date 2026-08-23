# Intelligence Engineering Data Model

> **Project owner:** h4ckd4d

The v2 framework treats public Internet telemetry as structured evidence rather than as a final security conclusion.

## Core objects

### Asset

An asset is an entity that may belong to the authorized organization or environment under review.

Examples include:

- IP address
- CIDR range
- ASN
- domain
- hostname
- certificate
- Internet-facing service
- cloud resource

Normalized representation: [`schemas/asset.schema.json`](../schemas/asset.schema.json).

### Finding

A finding represents an analyst-reviewed condition associated with an asset. A finding begins as an observation or candidate and becomes validated only after ownership, freshness, and context are reviewed.

Normalized representation: [`schemas/finding.schema.json`](../schemas/finding.schema.json).

### Baseline

A baseline describes expected assets and expected Internet-facing services. It is used to compare approved architecture with observed telemetry.

Normalized representation: [`schemas/baseline.schema.json`](../schemas/baseline.schema.json).

## Analytical separation

The framework enforces the following distinction:

> Observation ≠ Finding ≠ Vulnerability ≠ Exploitability ≠ Compromise

An indexed service is an observation. It does not automatically prove that the service is unexpected, vulnerable, exploitable, or compromised.

## Evidence model

Evidence should answer at least four questions:

1. **What was observed?**
2. **When was it observed?**
3. **Why is it believed to belong to the authorized scope?**
4. **How strongly does the evidence support the conclusion?**

Recommended evidence sources include authoritative DNS, internal inventory, cloud control planes, certificate relationships, ASN/RDAP data, and approved external telemetry sources.

## Ownership confidence

Suggested interpretation:

| Confidence | Interpretation |
| --- | --- |
| 90–100 | Confirmed ownership |
| 70–89 | Probable ownership |
| 40–69 | Possible relationship requiring validation |
| 1–39 | Weak evidence |
| 0 | No ownership evidence |

Confidence should be based on evidence quality, not on analyst intuition alone.

## Temporal model

Every observation should preserve timestamps where possible. This enables:

- stale-data detection;
- exposure trend analysis;
- first-seen / last-seen tracking;
- baseline drift detection;
- remediation verification.

## Expected vs. observed

The framework classifies relationships between the approved baseline and external observations into practical states:

- **Expected asset / expected service**
- **Expected asset / unexpected service**
- **Unknown but potentially related asset**
- **Historical or stale observation**
- **Third-party or excluded infrastructure**

This comparison is central to External Attack Surface Management.

## Interoperability

JSON schemas are intentionally vendor-neutral. Shodan is one telemetry source, not the data model itself. Future adapters can normalize data from certificate transparency, DNS, RDAP, cloud inventories, internal CMDBs, and other approved sources into the same asset/finding model.

---

**Shodan Dorks for Advanced OSINT — Internet Exposure Intelligence Framework by h4ckd4d.**

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
