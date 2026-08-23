# Shadow IT Review Playbook

> **Project owner:** h4ckd4d

## Objective

Identify candidate Internet-facing assets that may support the organization but are missing from the authoritative inventory.

## Safe analytical scope

This playbook is for defensive reconciliation of owned or explicitly authorized environments. Public telemetry is used only to identify candidates for internal validation.

## Workflow

1. Export known domains, CIDRs, ASNs, cloud resources, and approved SaaS relationships.
2. Query Shodan from those ownership anchors.
3. Identify assets that are absent from the CMDB or external-service register.
4. Correlate candidates with DNS, certificates, RDAP, and cloud inventory.
5. Assign ownership confidence.
6. Validate candidates through internal administrators or service owners.
7. Classify confirmed assets as approved, undocumented, deprecated, or third-party.
8. Record the inventory correction or remediation action.

## Candidate signals

Useful defensive signals include:

- hostname relationships;
- certificate subject/SAN relationships;
- consistent organization metadata;
- owned CIDR observations;
- owned ASN observations;
- historical DNS relationships;
- known business-unit naming patterns.

## False-positive risks

- SaaS infrastructure;
- CDN edges;
- MSP infrastructure;
- cloud reassignment;
- abandoned DNS records;
- old certificates;
- acquisitions and divestitures.

## Analyst output

A candidate should end in one of these states:

```text
Confirmed Internal Asset
Confirmed Third Party
Approved SaaS / Provider
Historical / Decommissioned
Unresolved Candidate
Rejected False Positive
```

## Important rule

Do not validate a candidate by authenticating to or probing an unknown system. Validate ownership through authoritative records and internal control planes.

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
