# Authorized Asset Discovery Example

This example demonstrates a defensive workflow for an organization reviewing its own Internet-facing footprint.

## Scenario

Assume the organization has explicitly confirmed ownership of the documentation-only network below:

```text
203.0.113.0/24
```

The goal is to compare Shodan observations against the organization's internal inventory.

## Step 1 — Establish the scope

```text
net:"203.0.113.0/24"
```

Export or record the observed IPs, ports, products, hostnames, timestamps, and TLS metadata relevant to your inventory process.

## Step 2 — Review HTTPS exposure

```text
net:"203.0.113.0/24" port:443
```

Then narrow to services where Shodan collected TLS metadata:

```text
net:"203.0.113.0/24" port:443 has_ssl:true
```

## Step 3 — Review HTTP metadata

```text
net:"203.0.113.0/24" http.status:200
```

If your organization maintains a known portal title:

```text
net:"203.0.113.0/24" http.title:"Example Portal"
```

## Step 4 — Review certificate metadata

```text
net:"203.0.113.0/24" ssl.cert.subject.cn:"example.com"
```

Compare observed certificates with the organization's certificate inventory.

## Step 5 — Review service products

```text
net:"203.0.113.0/24" product:"nginx"
```

Repeat for products you expect to operate. Unexpected product metadata should be treated as a review lead, not immediate proof of an unauthorized service.

## Step 6 — Prioritize exposure review

Within the authorized scope:

```text
net:"203.0.113.0/24" has_vuln:true
```

Treat Shodan vulnerability metadata as prioritization data only. Confirm current software state and applicability through authorized internal vulnerability-management processes.

## Step 7 — Reconcile observations

Create a table such as:

| IP | Port | Observed service | Internal owner | Expected? | Observation date | Next action |
| --- | --- | --- | --- | --- | --- | --- |
| 203.0.113.10 | 443 | HTTPS | Web Team | Yes | YYYY-MM-DD | Verify certificate inventory |
| 203.0.113.20 | 22 | SSH | Unknown | Review | YYYY-MM-DD | Resolve asset ownership |

## Step 8 — Classify findings

Useful classifications include:

- Expected and documented
- Expected but configuration review required
- Unknown asset/service
- Third-party/shared infrastructure
- Stale Shodan observation
- Remediation required

## Key principle

Shodan is a source of external telemetry, not a substitute for authoritative internal inventory or current authenticated assessment. Use it to find discrepancies and prioritize defensive review.
