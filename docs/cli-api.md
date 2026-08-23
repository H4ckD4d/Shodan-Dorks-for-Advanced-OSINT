# Shodan CLI and API for Defensive Inventory

> **Project owner:** h4ckd4d  
> Part of **Shodan Dorks for Advanced OSINT**, created and maintained by **h4ckd4d**.

This page shows conservative patterns for querying Shodan about infrastructure you own, administer, or are explicitly authorized to assess.

## CLI

Initialize the official Shodan CLI with your own API key according to Shodan's documentation, then use scoped queries such as:

```bash
shodan count 'org:"Example Organization"'
shodan search 'net:"203.0.113.0/24" port:443'
shodan search 'org:"Example Organization" has_ssl:true'
```

Prefer `count` while developing a query because it can help estimate result volume before retrieving records.

## Python API

```python
from shodan import Shodan

api = Shodan("YOUR_API_KEY")
query = 'net:"203.0.113.0/24" port:443'

result = api.count(query)
print(result["total"])
```

For an authorized asset inventory:

```python
from shodan import Shodan

api = Shodan("YOUR_API_KEY")
query = 'org:"Example Organization" port:443'

for service in api.search_cursor(query):
    print(service.get("ip_str"), service.get("port"), service.get("product"))
```

Do not hard-code production API keys into source repositories. Use environment variables or an appropriate secrets manager.

## Validate search syntax programmatically

Shodan exposes a tokenization endpoint that can show which filters a query contains:

`/shodan/host/search/tokens`

The authoritative current search-filter list is available through:

`/shodan/host/search/filters`

These endpoints are useful when maintaining this repository because they reduce reliance on undocumented filter names.

## API-credit awareness

Shodan account capabilities and query-credit rules can change. Consult the official API documentation before automating large searches. Keep queries scoped and avoid unnecessary collection.

## Data handling

When exporting results for defensive review:

- store only what is necessary;
- protect API keys and collected asset data;
- retain timestamps because Shodan telemetry can become stale;
- avoid publishing sensitive details about systems you do not own;
- validate apparent findings against your authoritative inventory.

## Official references

- https://developer.shodan.io/api
- https://developer.shodan.io/api/clients

Reference reviewed: **August 23, 2026**.

---

**Original creator and project owner: h4ckd4d**
