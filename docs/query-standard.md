# Professional Query Documentation Standard

> **Project owner:** h4ckd4d

Every query added to this repository should be documented as an analytical unit rather than as a raw command.

## Required fields

### Objective

Explain what the analyst is trying to learn.

### Query

Provide the Shodan query using documented filters and documentation-safe example values.

### Filters used

List each official filter and explain its role.

### Expected result

Describe what type of observation the query is likely to return.

### What the query does not prove

State the analytical limitations explicitly.

### Validation steps

Explain how to validate ownership, freshness, service identity, and security relevance through authorized sources.

### False-positive considerations

Document likely causes of incorrect attribution or stale observations.

### Related pivots

Link to related filters, playbooks, or evidence sources.

## Example

### Objective

Identify HTTPS services associated with an authorized organization.

### Query

```text
org:"Example Organization" port:443
```

### Filters used

- `org` — narrows results by Shodan organization metadata.
- `port` — limits observations to TCP port 443.

### Expected result

Internet-facing services indexed on TCP/443 and associated with the organization in Shodan metadata.

### What the query does not prove

It does not prove that:

- every result is currently owned by the organization;
- the service is an HTTPS application;
- the service is vulnerable;
- the organization has authorized interaction with every returned endpoint.

### Validation steps

1. Confirm IP/CIDR ownership.
2. Check authoritative DNS.
3. Review certificate metadata.
4. Compare against CMDB/cloud inventory.
5. Check Shodan observation freshness.

### False-positive considerations

- shared hosting;
- CDN infrastructure;
- cloud-IP reassignment;
- stale organization metadata.

## Analytical principle

A professional query should help an analyst answer a question and understand the evidentiary limits of the answer.

---

**Original creator and project owner: h4ckd4d**

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
