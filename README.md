# Shodan Dorks for Advanced OSINT

[![Documentation Quality](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/docs-quality.yml/badge.svg)](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/docs-quality.yml)
[![Shodan Filter Validation](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/filter-validation.yml/badge.svg)](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/filter-validation.yml)
[![Framework Validation](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/framework-validation.yml/badge.svg)](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/framework-validation.yml)
[![Intelligence Engineering](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/intelligence-engineering.yml/badge.svg)](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/intelligence-engineering.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Framework](https://img.shields.io/badge/framework-Internet%20Exposure%20Intelligence-blue.svg)](docs/architecture.md)

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

**Shodan Dorks for Advanced OSINT** is a defensive **Internet Exposure Intelligence**, **External Attack Surface Management (EASM)**, **OSINT**, and **Cyber Threat Intelligence (CTI)** framework for authorized environments.

The project has evolved beyond a list of search queries. It now provides a structured intelligence pipeline for transforming public Internet telemetry and approved inventory data into defensible, normalized, analyst-reviewed security intelligence.

> **Authorized use only:** Use this project only for systems you own, administer, or are explicitly authorized to assess. Public visibility does not grant permission to access, authenticate to, modify, exploit, disrupt, or test a third-party system.

## Protect. Detect. Defend.

Project h4ckd4d combines technical cybersecurity engineering with a broader public-interest mission: using technology, OSINT, threat intelligence, and responsible digital-investigation methods to help protect people — especially children and families — from digital threats.

The child-protection and public-awareness pillar is represented by **[rifleman.us](https://www.rifleman.us/)**. Its strongest themes — prevention, online-safety awareness, responsible OSINT, preservation of digital evidence, family support, and threat visibility — are reflected in this repository without changing the framework's technical EASM/OSINT/CTI focus.

Project h4ckd4d and rifleman.us are independent initiatives. They do not represent, speak for, or imply affiliation with government, police, military, intelligence, or law-enforcement agencies.

- [`docs/child-protection-mission.md`](docs/child-protection-mission.md) — child-protection mission and operating principles.
- [`docs/visual-identity.md`](docs/visual-identity.md) — visual system derived from the project's protection + intelligence identity.
- [`BRANDING.md`](BRANDING.md) — canonical brand and signature standard.

## Intelligence lifecycle

```text
Authorized Scope
      ↓
Discover Observations
      ↓
Attribute Ownership
      ↓
Normalize Assets
      ↓
Build Relationships
      ↓
Enrich Context
      ↓
Compare Baseline
      ↓
Classify Exposure
      ↓
Prioritize Review
      ↓
Validate Internally
      ↓
Generate Findings
      ↓
Report / Track Drift
```

The core analytical rule is:

> **Observation ≠ Finding ≠ Vulnerability ≠ Exploitability ≠ Compromise**

Each transition requires evidence.

## v2 Intelligence Engineering

The v2 data layer introduces vendor-neutral normalized objects for Internet exposure analysis:

- **Asset** — IP, CIDR, ASN, domain, hostname, certificate, service, or cloud resource.
- **Finding** — analyst-reviewed exposure condition with evidence, confidence, status, and severity.
- **Baseline** — approved expected assets and services used for drift comparison.
- **Relationship graph** — evidence-backed links among organizations, domains, certificates, IPs, networks, and services.

Schemas:

- [`schemas/asset.schema.json`](schemas/asset.schema.json)
- [`schemas/finding.schema.json`](schemas/finding.schema.json)
- [`schemas/baseline.schema.json`](schemas/baseline.schema.json)
- [`schemas/scope.schema.json`](schemas/scope.schema.json)

Methodology:

- [`docs/data-model.md`](docs/data-model.md)
- [`intelligence/relationship-graph.md`](intelligence/relationship-graph.md)
- [`intelligence/confidence-engine.md`](intelligence/confidence-engine.md)
- [`intelligence/risk-prioritization.md`](intelligence/risk-prioritization.md)

## h4ckd4d-osint CLI

The unified CLI operates offline and does not contact Shodan or external targets.

Validate an authorized scope:

```bash
python scripts/h4ckd4d_osint.py scope examples/authorized-scope.json
```

Generate scope-bound query templates:

```bash
python scripts/h4ckd4d_osint.py queries examples/authorized-scope.json
```

Compare an expected baseline with normalized observations:

```bash
python scripts/h4ckd4d_osint.py baseline \
  examples/expected-baseline.json \
  examples/observed-assets.json \
  --output comparison.json
```

Generate an analyst-readable Markdown report:

```bash
python scripts/h4ckd4d_osint.py report comparison.json --output report.md
```

Full guide: [`docs/cli-v2.md`](docs/cli-v2.md).

## What this project provides

- Curated and validated Shodan filter reference.
- Defensive query collections.
- Scope-aware offline query generation.
- External attack-surface analyst playbooks.
- Asset-attribution methodology.
- Ownership-confidence model.
- Normalized asset and finding schemas.
- Expected-versus-observed baseline comparison.
- Relationship-graph methodology.
- Exposure taxonomy and risk-prioritization guidance.
- Markdown reporting pipeline.
- Machine-readable scope, catalog, baseline, asset, and finding structures.
- CI validation for documentation, Shodan filters, framework integrity, schemas, fixtures, and the v2 intelligence pipeline.

## Professional analyst workflow

### 1. Define authorization and scope

Establish domains, CIDRs, ASNs, organizations, constraints, and an authorization reference.

### 2. Discover observations

Use approved public telemetry and internal inventories to identify candidate Internet-facing assets and services.

### 3. Attribute ownership

Correlate candidates with authoritative DNS, owned CIDRs/ASNs, internal inventory, cloud control planes, certificate relationships, and other independent evidence.

### 4. Normalize

Represent observations through the vendor-neutral asset model so different data sources can be compared consistently.

### 5. Build relationships

Model domain → IP → service → certificate → ASN relationships and assign confidence to evidence-backed edges.

### 6. Compare baseline

Identify expected assets, missing expected assets, unexpected services, and unknown potentially related assets.

### 7. Prioritize

Use business criticality, service sensitivity, exposure context, telemetry freshness, ownership confidence, and analyst validation status.

### 8. Validate internally

Confirm observations using administrative systems and control planes the organization is authorized to operate.

### 9. Report

Create findings only after sufficient validation, preserving evidence, confidence, timestamps, and analyst rationale.

## Repository map

### Framework and methodology

- [`ROADMAP.md`](ROADMAP.md) — development roadmap.
- [`docs/architecture.md`](docs/architecture.md) — architecture and trust boundaries.
- [`docs/data-model.md`](docs/data-model.md) — normalized intelligence data model.
- [`docs/asset-attribution.md`](docs/asset-attribution.md) — ownership evidence and attribution.
- [`docs/query-standard.md`](docs/query-standard.md) — professional query-documentation standard.
- [`docs/osint-methodology.md`](docs/osint-methodology.md) — defensive OSINT methodology.
- [`docs/cli-v2.md`](docs/cli-v2.md) — unified offline CLI guide.
- [`docs/child-protection-mission.md`](docs/child-protection-mission.md) — child-protection and public-awareness mission.
- [`docs/visual-identity.md`](docs/visual-identity.md) — visual identity and graphic-language specification.
- [`intelligence/confidence-engine.md`](intelligence/confidence-engine.md) — evidence-confidence model.
- [`intelligence/relationship-graph.md`](intelligence/relationship-graph.md) — asset relationship graph.
- [`intelligence/risk-prioritization.md`](intelligence/risk-prioritization.md) — exposure prioritization.

### Analyst playbooks

- [`playbooks/external-attack-surface-baseline.md`](playbooks/external-attack-surface-baseline.md)
- [`playbooks/shadow-it-review.md`](playbooks/shadow-it-review.md)
- [`playbooks/certificate-pivoting.md`](playbooks/certificate-pivoting.md)

### Shodan reference

- [`CHEATSHEET.md`](CHEATSHEET.md)
- [`docs/getting-started.md`](docs/getting-started.md)
- [`docs/filters-reference.md`](docs/filters-reference.md)
- [`docs/cli-api.md`](docs/cli-api.md)
- [`dorks/network.md`](dorks/network.md)
- [`dorks/web.md`](dorks/web.md)
- [`dorks/ssl-tls.md`](dorks/ssl-tls.md)
- [`dorks/dns-hostnames.md`](dorks/dns-hostnames.md)
- [`dorks/ssh.md`](dorks/ssh.md)
- [`dorks/cloud.md`](dorks/cloud.md)
- [`dorks/databases.md`](dorks/databases.md)
- [`dorks/iot-ics.md`](dorks/iot-ics.md)

### Structured data and tooling

- [`catalog/index.json`](catalog/index.json)
- [`catalog/exposure-categories.json`](catalog/exposure-categories.json)
- [`config/official-filters.txt`](config/official-filters.txt)
- [`scripts/validate_filters.py`](scripts/validate_filters.py)
- [`scripts/validate_framework.py`](scripts/validate_framework.py)
- [`scripts/scope_query_builder.py`](scripts/scope_query_builder.py)
- [`scripts/baseline_compare.py`](scripts/baseline_compare.py)
- [`scripts/generate_report.py`](scripts/generate_report.py)
- [`scripts/h4ckd4d_osint.py`](scripts/h4ckd4d_osint.py)

### Documentation-safe fixtures

- [`examples/authorized-scope.json`](examples/authorized-scope.json)
- [`examples/expected-baseline.json`](examples/expected-baseline.json)
- [`examples/observed-assets.json`](examples/observed-assets.json)
- [`examples/example-finding.json`](examples/example-finding.json)

All example infrastructure uses documentation-safe values and is intended for local testing and learning.

## Ownership confidence

| Confidence | Interpretation |
| --- | --- |
| 90–100 | Confirmed ownership |
| 70–89 | Probable ownership |
| 40–69 | Possible relationship requiring validation |
| 1–39 | Weak / unverified relationship |
| 0 | No supporting evidence or excluded |

**Relationship is not ownership. Ownership is not authorization.**

## Query documentation standard

Every professional query should explain:

1. Objective.
2. Query syntax.
3. Filters used.
4. Expected result.
5. What the query does **not** prove.
6. Validation steps.
7. False-positive considerations.
8. Related analytical pivots.

This makes the repository analyst training material rather than a command dump.

## Validation policy

Before adding a Shodan filter:

1. Confirm it in the official Shodan reference or API.
2. Verify the expected value format.
3. Distinguish official filters from free-text banner searches.
4. Use documentation-safe or explicitly authorized examples.
5. Document important limitations.
6. Run `python scripts/validate_filters.py`.

## Project owner profile

**Chris Cruz | h4ckd4d** is the original creator, project owner, and primary maintainer.

Technical focus documented by this project includes cybersecurity, cyber intelligence, OSINT, Red Team methodologies, attack-surface analysis, network and systems infrastructure, defensive architecture, automation, OT/IT integration, and security frameworks such as NIST CSF, CIS Controls, ISO/IEC 27001, MITRE ATT&CK, and OWASP-oriented practices.

See [`AUTHOR.md`](AUTHOR.md) for the expanded profile.

## Official Shodan references

- [Shodan Search Query Fundamentals](https://help.shodan.io/the-basics/search-query-fundamentals)
- [Shodan Developer API](https://developer.shodan.io/api)
- [Shodan filter reference](https://trends.shodan.io/search/filters)
- [Shodan Datapedia](https://datapedia.shodan.io/)

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions should preserve defensive scope, evidence standards, data-model consistency, and project attribution.

## Security and responsible use

See [`SECURITY.md`](SECURITY.md).

## License and credits

Released under the MIT License. See [`LICENSE`](LICENSE) and [`CREDITS.md`](CREDITS.md).

---

**Shodan Dorks for Advanced OSINT**  
**Internet Exposure Intelligence · EASM · OSINT · CTI · Defensive Security**  
Created and maintained by **h4ckd4d**.

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
