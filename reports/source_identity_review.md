# Source document identity audit

Read-only census, 2026-09-04 UTC, after Batch 400 import.

The legacy `unique_source_documents` statistic groups
`COALESCE(archival_identifier, stable_url)`. It is a reproducible count of
citation document keys, not yet a certified count of unique historical items.
Some citations use different archive locators for one PDF; some collection
URLs legitimately support distinct identified archival documents. Conversely,
the same document may have different URLs. Blindly grouping only by URL would
also erase important distinctions.

- Citation records: **3,711**.
- Distinct non-null source URLs: **1,258**.
- Legacy document keys: **1,734**.
- URLs attached to multiple legacy document keys: **60**.

Reproduce the last figure:

```sql
SELECT COUNT(*) FROM (
  SELECT stable_url FROM sources WHERE stable_url IS NOT NULL
  GROUP BY stable_url
  HAVING COUNT(DISTINCT COALESCE(archival_identifier, stable_url)) > 1
);
```

Next action: introduce reviewed, stable document identities independently of
citation records, keeping page/box/folder locators on the citation. Start with
the repeatedly cited NARA personnel PDF and Army technical documents; then
review the remaining clusters. Preserve every citation and all links during
the process. Do not infer that equal URLs or equal titles identify the same
archival item. No research, employer, or personnel count is advanced by this
audit, and no historical claim was changed.
