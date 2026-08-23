# Evidence Confidence Engine

> **Project owner:** h4ckd4d

The confidence engine provides a repeatable way to estimate how strongly available evidence supports asset attribution. It is not a vulnerability score and does not indicate exploitability.

## Purpose

Internet exposure datasets frequently contain shared hosting, reassigned addresses, stale DNS, CDN infrastructure, and historical certificates. Confidence scoring helps analysts separate confirmed assets from weakly related observations.

## Evidence classes

| Evidence | Suggested weight |
| --- | ---: |
| Confirmed internal inventory / cloud control plane | 100 |
| Owned CIDR or ASN confirmed by authoritative records | 95 |
| Authoritative DNS resolution controlled by the organization | 90 |
| Valid certificate relationship for an approved domain | 80 |
| Multiple consistent external sources | 70 |
| Historical DNS or certificate relationship | 50 |
| Organization/banner metadata only | 35 |
| Keyword coincidence only | 15 |

Weights are guidance, not universal truth. Organizations should adapt them to their environment.

## Combining evidence

Do not simply add every signal until the score reaches 100. Correlated evidence may represent the same underlying fact.

Recommended approach:

1. Choose the strongest independent evidence source as the base confidence.
2. Add small increments for additional independent corroboration.
3. Apply penalties for contradictory evidence, stale telemetry, shared hosting, or reassignment risk.
4. Cap the final result between 0 and 100.

Example:

```text
Owned CIDR evidence                 95
Consistent authoritative DNS       +3
Telemetry older than 90 days       -10
---------------------------------------
Final attribution confidence       88
```

## Interpretation

| Score | Status |
| --- | --- |
| 90–100 | confirmed |
| 70–89 | probable |
| 40–69 | possible |
| 1–39 | unverified |
| 0 | excluded / no supporting evidence |

## Required analyst notes

Any automated or manual confidence score should preserve:

- evidence sources;
- observation dates;
- contradictions;
- stale-data considerations;
- analyst rationale.

## Guardrail

Confidence represents belief that an asset belongs to scope. It does not authorize access, prove vulnerability, or imply compromise.

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
