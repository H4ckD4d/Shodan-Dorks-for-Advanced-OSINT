# IoT and ICS Defensive Exposure Review

> **Project owner:** h4ckd4d  
> Use only for devices and networks you own, administer, or are explicitly authorized to assess.

IoT and industrial-control environments require extra caution. This page deliberately avoids presenting undocumented field names as official Shodan filters and avoids instructions for interacting with exposed control systems.

## Start from an ownership boundary

Use documented filters such as:

```text
org:"Example Organization"
net:"203.0.113.0/24"
asn:"AS64500"
```

Then narrow using documented metadata:

```text
org:"Example Organization" port:443
org:"Example Organization" product:"Example Product"
org:"Example Organization" version:"1.0"
org:"Example Organization" cpe:"cpe:/a:example:product"
```

## Banner-text searches

Vendor or protocol names can sometimes appear as free text in indexed banners. A free-text search is **not** the same thing as an official filter.

Conceptual pattern:

```text
"Vendor or Protocol Name" org:"Example Organization"
```

When using banner text, document it as a search term rather than inventing syntax such as `ics.vendor:` or `modbus.function:` unless Shodan officially documents that field as a current filter.

## Safe defensive workflow

1. Define the exact owned CIDRs, ASNs, sites, and devices in scope.
2. Search from that ownership boundary rather than globally targeting a technology.
3. Compare Shodan observations with the organization's OT/IoT asset inventory.
4. Treat unexpected exposure as a configuration-review lead.
5. Validate internally through the device-management or network-management plane.
6. Coordinate changes with the relevant operational and safety owners.

## OT/ICS caution

Do not probe, authenticate to, change, reboot, or send protocol commands to an Internet-visible control system solely because Shodan indexed it. Industrial systems can have safety, reliability, and availability constraints that differ significantly from conventional IT.

## Former undocumented filters

Earlier versions of this project listed names such as:

- `ics.vendor`
- `ics.product`
- `ics.version`
- `modbus.function`
- `bacnet.device`
- `iot`
- `manufacturer`
- `firmware`

They are not treated here as official current Shodan search filters unless independently verified against the current official filter list.

Reference reviewed: **August 23, 2026**.

---

**Original creator and project owner: h4ckd4d**
