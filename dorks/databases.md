# Database Service Inventory

> **Project owner:** H4ckD4d  
> Use only for systems you own, administer, or are explicitly authorized to assess.

This page is for identifying database services that appear in an authorized external asset inventory. Discovery does not authorize connection, authentication attempts, or data access.

## Product-based inventory

Use Shodan's documented `product` filter when the indexed service exposes recognizable product metadata:

```text
org:"Example Organization" product:"PostgreSQL"
org:"Example Organization" product:"MySQL"
org:"Example Organization" product:"MongoDB"
org:"Example Organization" product:"Redis"
```

Product names depend on Shodan's banner normalization and may not match every deployment.

## Network-scoped inventory

```text
net:"203.0.113.0/24" product:"PostgreSQL"
net:"203.0.113.0/24" product:"MySQL"
```

## Port-assisted review

Ports can help classify an approved inventory, but a port number does not prove which service is running:

```text
org:"Example Organization" port:5432
org:"Example Organization" port:3306
org:"Example Organization" port:27017
org:"Example Organization" port:6379
```

Validate every result against the organization's current CMDB, cloud inventory, firewall rules, and service configuration.

## Defensive review questions

- Is the database expected to be Internet-facing?
- Is the asset still active and owned by the organization?
- Does the observed product/version match configuration management?
- Is exposure restricted by network policy and authentication controls?
- Is the Shodan observation current enough to act on?

## Interpretation rules

- Never treat a port match alone as confirmation of a database.
- Never attempt to log in to validate a third-party result.
- Vulnerability metadata is a lead for internal validation, not proof of exploitability.
- Prefer remediation through infrastructure configuration rather than interacting with the exposed service from the Internet.

---

**Original creator and project owner: H4ckD4d**
