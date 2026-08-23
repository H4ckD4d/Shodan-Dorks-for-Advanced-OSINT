# Exposure Risk Prioritization

> **Project owner:** h4ckd4d

## Purpose

This model helps analysts prioritize validated Internet-exposure findings. It is not a vulnerability scanner, exploitability score, or compromise indicator.

## Inputs

The framework considers eight dimensions:

1. Internet exposure
2. Service sensitivity
3. Authentication expectations
4. Software lifecycle / age
5. Vulnerability metadata
6. Asset criticality
7. Ownership confidence
8. Telemetry freshness

## Suggested scoring model

Each dimension receives 0–5 points. Weighted scores can then be normalized to 0–100.

| Dimension | Example question |
| --- | --- |
| Exposure | Is the service directly reachable from the Internet? |
| Sensitivity | Is this an administrative, database, identity, or control-plane service? |
| Authentication | Is strong authentication expected and enforced? |
| Lifecycle | Is the observed software supported and current? |
| Vulnerability context | Does trusted metadata indicate relevant known vulnerabilities? |
| Criticality | How important is the asset to business operations? |
| Ownership confidence | How certain are we that the asset belongs to the organization? |
| Freshness | How recent is the telemetry? |

## Suggested interpretation

```text
0–20   Informational
21–40  Low
41–60  Medium
61–80  High
81–100 Critical Review
```

## Guardrails

- A public service is not automatically vulnerable.
- Vulnerability metadata is not proof of exploitability.
- A version string may be incomplete or misleading.
- Low-confidence attribution should reduce escalation confidence.
- Old telemetry should reduce confidence or trigger revalidation.
- Business criticality should come from authoritative internal context.

## Finding state model

```text
Observation
   ↓
Candidate
   ↓
Attributed
   ↓
Validated Exposure
   ↓
Prioritized Finding
   ↓
Remediation
   ↓
Verified Closure
```

## Analyst note

Risk scoring should support judgment, not replace it. The score exists to make prioritization transparent and repeatable.

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
