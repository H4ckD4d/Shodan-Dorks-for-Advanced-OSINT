# h4ckd4d-osint CLI

> **Project owner:** Chris Cruz | h4ckd4d

The v2 CLI is an offline orchestration layer for the Internet Exposure Intelligence framework. It does not run Shodan searches and does not contact external targets.

## Commands

### Validate scope

```bash
python scripts/h4ckd4d_osint.py scope examples/authorized-scope.json
```

The command checks that the local scope file explicitly confirms authorization and summarizes the defined domains, CIDRs, and ASNs.

### Generate scoped query templates

```bash
python scripts/h4ckd4d_osint.py queries examples/authorized-scope.json
```

The generated Shodan query templates remain anchored to the authorized scope. Analysts review and execute approved queries separately through their normal tooling.

### Compare baseline

```bash
python scripts/h4ckd4d_osint.py baseline \
  examples/expected-baseline.json \
  examples/observed-assets.json \
  --output comparison.json
```

The comparison classifies:

- expected assets observed;
- expected assets not observed;
- unexpected or potentially related assets;
- unexpected services on expected assets.

### Generate report

```bash
python scripts/h4ckd4d_osint.py report comparison.json --output report.md
```

The report generator produces a concise Markdown summary suitable for analyst review and ticketing workflows.

## Data flow

```text
authorized-scope.json
        │
        ├── scope validation
        └── query templates

expected-baseline.json + observed-assets.json
        │
        └── baseline comparison
                 │
                 └── comparison.json
                          │
                          └── report.md
```

## Current design philosophy

The CLI intentionally separates **data collection** from **analysis**. This keeps the repository vendor-neutral and prevents the framework from treating access to a data source as permission to interact with an Internet system.

Future adapters may normalize approved telemetry into `asset.schema.json` without changing the core comparison and reporting pipeline.

## Output interpretation

The baseline engine is deterministic. It does not claim that an unexpected asset is malicious or vulnerable. An unexpected observation becomes an analyst lead requiring ownership, freshness, and configuration validation.

---

**h4ckd4d-osint — Internet Exposure Intelligence tooling by h4ckd4d.**

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
