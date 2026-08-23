# Shodan Dorks for Advanced OSINT

[![Documentation Quality](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/docs-quality.yml/badge.svg)](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/docs-quality.yml)
[![Shodan Filter Validation](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/filter-validation.yml/badge.svg)](https://github.com/h4ckd4d/Shodan-Dorks-for-Advanced-OSINT/actions/workflows/filter-validation.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Framework](https://img.shields.io/badge/framework-Internet%20Exposure%20Intelligence-blue.svg)](docs/architecture.md)

> **Original creator, project owner, and primary maintainer: h4ckd4d**

**Shodan Dorks for Advanced OSINT** is evolving into a defensive **Internet Exposure Intelligence**, **External Attack Surface Management (EASM)**, **OSINT**, and **Cyber Threat Intelligence (CTI)** framework for authorized environments.

The project is not designed as a collection of exploitation recipes. Its purpose is to help analysts move from raw public Internet telemetry to defensible security intelligence through explicit scope, attribution, enrichment, classification, prioritization, validation, and reporting.

> **Authorized use only:** Use this project only for systems you own, administer, or are explicitly authorized to assess. Public visibility does not grant permission to access, authenticate to, modify, exploit, disrupt, or test a third-party system.

## Framework model

```text
Authorized Scope
      ↓
Discover
      ↓
Attribute
      ↓
Enrich
      ↓
Classify
      ↓
Analyze Exposure
      ↓
Prioritize Risk
      ↓
Validate
      ↓
Report / Baseline
```

The core analytical rule is:

> **Observation ≠ Finding ≠ Vulnerability ≠ Exploitability ≠ Compromise**

Each transition requires evidence.

## What this project provides

- Curated Shodan filter and query reference.
- Defensive query collections.
- External attack-surface analyst playbooks.
- Asset-attribution and ownership-confidence methodology.
- Exposure taxonomy and risk-prioritization guidance.
- Machine-readable scope and catalog structures.
- Offline validation tooling.
- Scope-aware query generation.
- Documentation and CI standards for reproducible research.

## Quick start

Shodan filters use the form:

```text
filter:value
```

Examples using documentation-safe values:

```text
org:"Example Organization"
net:"203.0.113.0/24"
asn:"AS64500"
hostname:"example.com"
org:"Example Organization" port:443 has_ssl:true
```

A query is only the beginning. Every result should be interpreted in context and validated against ownership, freshness, service identity, and authoritative inventory.

## Scope-aware query builder

The project includes an offline query-template generator that requires explicit authorization in the local scope file.

Example scope:

```json
{
  "organization": "Example Organization",
  "authorization": {
    "confirmed": true,
    "reference": "INTERNAL-AUTH-REFERENCE"
  },
  "scope": {
    "domains": ["example.com"],
    "cidrs": ["203.0.113.0/24"],
    "asns": ["AS64500"],
    "organizations": ["Example Organization"]
  }
}
```

Generate reviewable query templates:

```bash
python scripts/scope_query_builder.py examples/authorized-scope.json
```

The script does **not** contact Shodan and does **not** execute searches.

## Professional analyst workflow

### 1. Define authorization and scope

Establish domains, CIDRs, ASNs, organizations, and constraints that are explicitly approved.

### 2. Discover observations

Use public telemetry to identify candidate Internet-facing assets and services.

### 3. Attribute ownership

Correlate candidates with authoritative DNS, internal inventory, cloud resources, RDAP/WHOIS, certificates, and known infrastructure relationships.

### 4. Classify exposure

Group services by function such as web, remote administration, databases, identity, network/security appliances, cloud, DevOps, monitoring, messaging, or IoT/OT.

### 5. Prioritize

Use business criticality, service sensitivity, exposure context, telemetry freshness, and ownership confidence to prioritize analyst review.

### 6. Validate internally

Confirm findings using systems and administrative control planes that the organization is authorized to operate.

### 7. Report and baseline

Record evidence, confidence, remediation ownership, and expected-vs-observed state.

## Repository map

### Framework and methodology

- [`ROADMAP.md`](ROADMAP.md) — long-term development plan.
- [`docs/architecture.md`](docs/architecture.md) — Internet Exposure Intelligence architecture.
- [`docs/asset-attribution.md`](docs/asset-attribution.md) — ownership evidence and confidence model.
- [`docs/query-standard.md`](docs/query-standard.md) — professional query documentation standard.
- [`docs/osint-methodology.md`](docs/osint-methodology.md) — defensive OSINT methodology.
- [`intelligence/risk-prioritization.md`](intelligence/risk-prioritization.md) — exposure risk-prioritization model.

### Analyst playbooks

- [`playbooks/external-attack-surface-baseline.md`](playbooks/external-attack-surface-baseline.md) — establish and maintain an external baseline.
- [`playbooks/shadow-it-review.md`](playbooks/shadow-it-review.md) — investigate candidate undocumented assets.
- [`playbooks/certificate-pivoting.md`](playbooks/certificate-pivoting.md) — use certificate metadata as relationship evidence.

### Shodan reference

- [`CHEATSHEET.md`](CHEATSHEET.md) — compact reference.
- [`docs/getting-started.md`](docs/getting-started.md) — search fundamentals.
- [`docs/filters-reference.md`](docs/filters-reference.md) — curated official-filter reference.
- [`docs/cli-api.md`](docs/cli-api.md) — defensive CLI/API patterns.
- [`dorks/network.md`](dorks/network.md) — network and service discovery.
- [`dorks/web.md`](dorks/web.md) — web and HTTP metadata.
- [`dorks/ssl-tls.md`](dorks/ssl-tls.md) — TLS/certificate searches.
- [`dorks/dns-hostnames.md`](dorks/dns-hostnames.md) — hostname/domain pivots.
- [`dorks/ssh.md`](dorks/ssh.md) — SSH inventory.
- [`dorks/cloud.md`](dorks/cloud.md) — cloud asset review.
- [`dorks/databases.md`](dorks/databases.md) — database-service inventory.
- [`dorks/iot-ics.md`](dorks/iot-ics.md) — conservative IoT/ICS exposure review.

### Structured data and tooling

- [`schemas/scope.schema.json`](schemas/scope.schema.json) — authorized-scope schema.
- [`catalog/index.json`](catalog/index.json) — project content catalog.
- [`catalog/exposure-categories.json`](catalog/exposure-categories.json) — exposure taxonomy.
- [`config/official-filters.txt`](config/official-filters.txt) — curated Shodan filter allowlist.
- [`scripts/validate_filters.py`](scripts/validate_filters.py) — offline filter validation.
- [`scripts/scope_query_builder.py`](scripts/scope_query_builder.py) — scope-aware query-template generator.
- [`examples/authorized-scope.json`](examples/authorized-scope.json) — documentation-only scope example.

## Ownership confidence

| Confidence | Interpretation |
| --- | --- |
| High | Supported by authoritative inventory, owned CIDR/ASN, cloud inventory, or authoritative DNS |
| Medium | Strong supporting relationship requiring confirmation |
| Low | Candidate based on weak public relationship evidence |
| Rejected | Confirmed unrelated or outside scope |

**Relationship is not ownership. Ownership is not authorization.**

## Exposure categories

The framework organizes review around security context rather than ports alone:

- Web Infrastructure
- Remote Administration
- Database Services
- Identity and Authentication
- Network and Security Appliances
- Cloud Infrastructure
- Development and DevOps Infrastructure
- Monitoring and Management
- Messaging and Mail Infrastructure
- IoT and OT/ICS

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

This makes the repository useful as analyst training material, not just a command list.

## Validation policy

Before adding a Shodan filter:

1. Confirm it in the official Shodan reference or API.
2. Verify the expected value format.
3. Distinguish official filters from free-text banner searches.
4. Use documentation-safe or explicitly authorized examples.
5. Document important limitations.
6. Run `python scripts/validate_filters.py`.

## Project owner profile

**h4ckd4d** is the original creator, project owner, and primary maintainer.

Technical focus documented by this project includes cybersecurity, cyber intelligence, OSINT, Red Team methodologies, attack-surface analysis, network and systems infrastructure, defensive architecture, automation, OT/IT integration, and security frameworks such as NIST CSF, CIS Controls, ISO/IEC 27001, MITRE ATT&CK, and OWASP-oriented practices.

See [`AUTHOR.md`](AUTHOR.md) for the expanded profile.

## Official Shodan references

- [Shodan Search Query Fundamentals](https://help.shodan.io/the-basics/search-query-fundamentals)
- [Shodan Developer API](https://developer.shodan.io/api)
- [Shodan filter reference](https://trends.shodan.io/search/filters)
- [Shodan Datapedia](https://datapedia.shodan.io/)

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions should preserve defensive scope, evidence standards, and project attribution.

## Security and responsible use

See [`SECURITY.md`](SECURITY.md).

## License and credits

Released under the MIT License. See [`LICENSE`](LICENSE) and [`CREDITS.md`](CREDITS.md).

---

**Shodan Dorks for Advanced OSINT**  
**Internet Exposure Intelligence · EASM · OSINT · CTI · Defensive Security**  
Created and maintained by **h4ckd4d**.
