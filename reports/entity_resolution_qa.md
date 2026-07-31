# Entity-resolution QA

Generated: 2026-07-31T19:23:57+00:00

- Source rows: **23,978**.
- Cautious person entities: **23,941**.
- Source rows linked: **23,978**.
- Narrow automatic same-name/same-service-number groups: **37**.
- Possible duplicate groups: **211**.
- Same-service-number/different-name groups: **165**.
- Entities requiring manual review: **23,719**.

## Checks

- PASS - `all_source_rows_linked`
- PASS - `no_name_only_automatic_merges`
- PASS - `all_duplicate_groups_require_review`

Exact normalized names alone never trigger an automatic merge. Identical printed service numbers attached to different names remain separate review candidates.
