# Project Roadmap

> **Project owner:** h4ckd4d

## Vision

Transform **Shodan Dorks for Advanced OSINT** into a professional defensive framework for **Internet Exposure Intelligence**, **External Attack Surface Management (EASM)**, **OSINT**, and **Cyber Threat Intelligence (CTI)** workflows.

The project is intentionally defensive. It focuses on discovery, attribution, normalization, enrichment, classification, prioritization, validation, reporting, and drift tracking for assets that are owned, administered, or explicitly authorized for assessment.

## Operating model

```text
Authorized Scope
  ↓
Discover
  ↓
Attribute
  ↓
Normalize
  ↓
Build Relationships
  ↓
Enrich
  ↓
Compare Baseline
  ↓
Classify Exposure
  ↓
Prioritize
  ↓
Validate
  ↓
Report
  ↓
Track Drift
```

## Phase 1 — Professional foundation — complete

- Structured query collections.
- Official-filter validation.
- Documentation quality CI.
- Defensive-use policy.
- Project governance and ownership attribution.
- Machine-readable catalog.

## Phase 2 — Exposure intelligence framework — complete

- Asset-attribution methodology.
- Ownership-confidence model.
- Exposure taxonomy.
- Analyst playbooks.
- Risk-prioritization model.
- Authorized-scope schema.
- Framework validation CI.

## Phase 3 — Intelligence engineering v2 — active / substantially implemented

- Normalized asset schema.
- Normalized finding schema.
- Expected-exposure baseline schema.
- Expected-versus-observed comparison engine.
- Relationship-graph methodology.
- Evidence-confidence engine.
- Markdown report generation.
- Unified offline `h4ckd4d-osint` CLI.
- JSON fixtures and end-to-end CI validation.

## Phase 4 — Multi-source normalization adapters — planned

Planned defensive adapters and correlation patterns:

- Shodan export/API normalization.
- DNS observations.
- Certificate Transparency.
- RDAP / WHOIS.
- Censys or equivalent approved Internet telemetry.
- Internal CMDB / cloud inventory.

Adapters should normalize approved telemetry into the vendor-neutral asset model. Collection and target interaction remain separate from the core analysis engine.

## Phase 5 — Temporal and graph intelligence — planned

- First-seen / last-seen history.
- Baseline snapshots.
- Exposure drift timelines.
- Certificate clustering.
- Infrastructure relationship graph exports.
- Confidence change tracking.
- Shadow-IT trend detection.

## Phase 6 — Reporting and interoperability — planned

- JSON and Markdown report profiles.
- SARIF-compatible defensive findings where appropriate.
- CSV analyst exports.
- Evidence bundles.
- Ticketing/SIEM integration patterns.
- Dashboard-ready summary datasets.

## Phase 7 — Platform maturity — planned

- Python package structure.
- Stable CLI command contract.
- Unit/integration test suite.
- Versioned schemas.
- Release automation.
- Signed releases and provenance metadata.
- Optional local web interface for authorized datasets.

## Core analytical rule

> Observation ≠ Finding ≠ Vulnerability ≠ Exploitability ≠ Compromise

Every stage requires its own evidence and validation.

## Project ownership

**Shodan Dorks for Advanced OSINT** was created by and remains under the project ownership and primary maintenance of **h4ckd4d**.
