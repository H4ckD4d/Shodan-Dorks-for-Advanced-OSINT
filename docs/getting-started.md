# Getting Started with Shodan Search

## 1. Understand what Shodan searches

Shodan stores service banners and metadata collected from Internet-facing systems. A normal search term is matched against banner data, while a search filter targets a specific indexed property.

Example free-text search:

```text
nginx
```

Example filtered search:

```text
product:"nginx"
```

Those queries are not equivalent. Prefer filters when you know which indexed property you want to constrain.

## 2. Filter syntax

Filters use:

```text
filter:value
```

There is no space between the filter name, colon, and value.

Quote values that contain spaces:

```text
city:"San Diego"
org:"Example Organization"
```

Combine filters by placing them in the same query:

```text
org:"Example Organization" country:US port:443
```

## 3. Start with an authorization boundary

A defensive workflow should begin with identifiers for assets you own or are authorized to assess, such as:

- Organization name
- Known CIDR ranges
- ASN
- Approved hostnames or domains

Examples use documentation-only reserved IP space where possible:

```text
net:"203.0.113.0/24"
```

## 4. Reduce noise progressively

Start broad inside your authorized boundary, then add filters:

```text
org:"Example Organization"
```

```text
org:"Example Organization" port:443
```

```text
org:"Example Organization" port:443 has_ssl:true
```

```text
org:"Example Organization" port:443 has_ssl:true http.status:200
```

This makes the reasoning behind each narrowing step easy to audit.

## 5. Validate query syntax

Shodan exposes a tokenization endpoint that can show which filters a query uses:

```text
GET /shodan/host/search/tokens
```

The API also provides:

```text
GET /shodan/host/search/filters
```

for the current supported search-filter list.

## 6. CLI quoting

When a query itself contains quotes, wrap the entire query for your shell:

```bash
shodan search 'city:"San Diego" port:443'
```

## 7. Interpret results carefully

A Shodan result is an observation from Shodan's collection infrastructure. It may be stale, incomplete, proxied, or changed since collection.

Do not treat a product string, vulnerability label, screenshot, or banner as proof that a system is currently exploitable. Validate ownership and current state through authorized defensive processes.

## References

- https://help.shodan.io/the-basics/search-query-fundamentals
- https://developer.shodan.io/api
- https://trends.shodan.io/search/filters
