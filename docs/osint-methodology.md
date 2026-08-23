# Defensive OSINT Methodology with Shodan

This methodology is designed for assets you own, administer, or are explicitly authorized to assess.

## 1. Define the scope

Document the approved boundary before searching:

- Organization names used in Internet registration data
- ASNs
- CIDR ranges
- Domains and hostnames
- Known cloud or hosting providers
- Expected service ports

Do not assume that a matching organization string proves ownership. Treat it as a lead until corroborated.

## 2. Establish authoritative pivots

Start from strong identifiers where available:

```text
net:"203.0.113.0/24"
asn:"AS64500"
hostname:"example.com"
```

Organization-name searches are useful but can be noisy:

```text
org:"Example Organization"
```

## 3. Build an inventory

Review exposed services within scope:

```text
net:"203.0.113.0/24" port:443
net:"203.0.113.0/24" product:"nginx"
net:"203.0.113.0/24" has_ssl:true
```

Record at minimum:

- Observed IP
- Port
- Transport
- Product/version metadata
- Hostname
- TLS certificate subject/issuer where relevant
- Shodan observation timestamp
- Internal asset owner, if known

## 4. Pivot through web metadata

Use HTTP metadata to group similar services:

```text
net:"203.0.113.0/24" http.status:200
net:"203.0.113.0/24" http.title:"Example Portal"
```

Component metadata can help distinguish expected and unexpected technology:

```text
net:"203.0.113.0/24" http.component:"nginx"
```

## 5. Pivot through TLS metadata

Certificates often provide useful ownership and infrastructure context:

```text
net:"203.0.113.0/24" has_ssl:true
net:"203.0.113.0/24" ssl.cert.subject.cn:"example.com"
```

Certificate metadata is evidence, not proof of current ownership. Certificates can be reused, stale, or shared.

## 6. Review exposure metadata

Within an authorized scope, Shodan metadata can help prioritize review:

```text
net:"203.0.113.0/24" has_vuln:true
```

A vulnerability label does not prove that exploitation is currently possible. Confirm findings through your authorized vulnerability-management process and current vendor/security advisories.

## 7. Reconcile with internal inventory

Compare observed Internet-facing services against:

- CMDB or asset inventory
- DNS records
- Cloud inventories
- Firewall/NAT documentation
- Certificate inventories
- Approved service catalog

Classify each result as expected, unknown, stale, third-party, or requiring remediation.

## 8. Track time

Shodan observations represent collected telemetry and may not reflect the present state. Always record the observation timestamp and re-check relevant assets using authorized internal methods.

## 9. Report responsibly

A useful defensive report separates:

- Observation
- Evidence
- Confidence
- Ownership status
- Business context
- Recommended next action

Avoid wording that implies compromise when only exposure metadata has been observed.
