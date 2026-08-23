# Contributing

Thanks for helping improve this Shodan OSINT reference.

## Contribution principles

Contributions should be accurate, reproducible, and focused on defensive or authorized use.

### Before submitting a filter

- Confirm the filter in the official Shodan documentation or API.
- Include the expected value format.
- Prefer examples scoped to owned or explicitly authorized assets.
- Distinguish official filters from free-text banner searches.
- Avoid claims that a query proves exploitation or compromise by itself.

## Recommended format

```markdown
### Filter name

**Purpose:** What the filter narrows.

**Syntax:**

```text
filter:value
```

**Authorized example:**

```text
org:"Example Organization" filter:value
```

**Notes:** Limitations, plan requirements, or interpretation guidance.
```

## Sources

Prefer primary sources:

- https://developer.shodan.io/api
- https://help.shodan.io/the-basics/search-query-fundamentals
- https://trends.shodan.io/search/filters
- https://datapedia.shodan.io/

## Commit style

Suggested prefixes:

- `docs:` documentation changes
- `fix:` corrections
- `feat:` new reference material
- `chore:` maintenance

## Pull requests

Keep pull requests focused. Explain what changed, why it changed, and how the syntax was validated.
