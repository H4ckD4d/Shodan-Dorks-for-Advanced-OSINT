# SSH Defensive Inventory

> **Project owner:** H4ckD4d  
> Use only for owned or explicitly authorized infrastructure.

This collection is intended for identifying SSH exposure in an organization's approved external inventory.

## SSH by organization

```text
org:"Example Organization" port:22
```

## SSH by authorized network

```text
net:"203.0.113.0/24" port:22
```

## SSH fingerprint pivot

```text
ssh.fingerprint:"FINGERPRINT"
```

Combine the fingerprint with an ownership boundary where possible:

```text
ssh.fingerprint:"FINGERPRINT" org:"Example Organization"
```

## Product/version review

```text
org:"Example Organization" port:22 product:"OpenSSH"
```

Version metadata can be incomplete or stale. Treat it as inventory evidence to verify against configuration management rather than as proof of vulnerability.

## Defensive questions

- Is SSH intentionally Internet-facing?
- Does each exposed endpoint belong to the approved inventory?
- Are fingerprints expected and documented?
- Are legacy endpoints still visible in Shodan telemetry?
- Do Shodan results match current firewall and cloud-security-group policy?

Never attempt authentication or interaction with a third-party SSH service based solely on Shodan results.

---

**Original creator and project owner: H4ckD4d**
