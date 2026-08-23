# External Attack Surface Baseline Playbook

> **Project owner:** h4ckd4d

## Objective

Build a repeatable baseline of authorized Internet-facing assets and identify inventory drift, unexpected services, and candidate shadow IT without interacting with third-party systems.

## Inputs

- approved domains;
- approved CIDRs;
- approved ASNs;
- organization names used in public infrastructure;
- authoritative cloud inventory;
- CMDB or asset register;
- known external services and expected ports.

## Workflow

### 1. Define scope

Document the exact boundaries before querying public telemetry.

### 2. Establish known assets

Create the authoritative starting set from internal sources.

### 3. Discover candidates

Use ownership-scoped Shodan queries such as:

```text
org:"Example Organization"
net:"203.0.113.0/24"
asn:"AS64500"
hostname:"example.com"
```

### 4. Classify observed services

Group observations into categories such as:

- web infrastructure;
- remote administration;
- databases;
- network/security appliances;
- cloud services;
- messaging;
- monitoring;
- IoT/OT.

### 5. Attribute ownership

For each candidate, collect evidence from authoritative DNS, certificates, RDAP, cloud inventory, and internal records.

### 6. Compare expected vs. observed

Classify each asset/service as:

- Known + Expected
- Known + Unexpected Service
- Unknown + Potentially Related
- Historical / Stale
- Third Party / Shared Infrastructure

### 7. Review risk context

Prioritize conditions such as unexpected administrative interfaces, externally visible database services, deprecated services, or high-value assets with inconsistent controls.

### 8. Validate internally

Validate unexpected exposure through the organization's own administrative control plane. Do not test a third-party endpoint solely because it appears in public telemetry.

### 9. Record evidence

Capture:

- query used;
- source;
- observation timestamp;
- ownership-confidence level;
- analyst conclusion;
- remediation owner;
- validation status.

### 10. Maintain the baseline

Repeat periodically and track changes over time.

## Analyst interpretation

A Shodan result is an **observation**. It becomes a **finding** only after ownership, freshness, service identity, and security relevance are validated.

## Deliverable

The baseline should produce a concise inventory of:

- expected assets;
- unexpected exposures;
- unverified candidate assets;
- stale/historical telemetry;
- third-party infrastructure;
- remediation actions.

---

**Shodan Dorks for Advanced OSINT — created and maintained by h4ckd4d.**
