# CI Validation Notes

This short maintenance note documents the scope of the CI-only follow-up after the 2026 repository revamp.

## Changes

- Markdown lint rules were aligned with the repository's established documentation style.
- Shodan filter validation now scans Markdown code examples and inline-code snippets rather than prose.
- The validator still compares discovered `filter:value` tokens against `config/official-filters.txt` and does not execute Shodan queries or contact external targets.

## Owner

Project owner and primary maintainer: **h4ckd4d**.
