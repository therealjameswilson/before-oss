# Entity-resolution QA

Generated: 2026-09-11T10:14:44+00:00

- Source rows: **23,978**.
- Cautious person entities: **23,940**.
- Superseded person entities retained for audit: **1** of **23,941** stored rows.
- Source rows linked: **23,978**.
- Narrow automatic same-name/same-service-number groups: **35**.
- Possible duplicate groups: **237**.
- Same-service-number/different-name groups: **164**.
- Entities requiring manual review: **23,303**.

## Checks

- PASS - `all_source_rows_linked`
- PASS - `no_name_only_automatic_merges`
- PASS - `all_duplicate_groups_require_review`

Exact normalized names alone never trigger an automatic merge. Identical printed service numbers attached to different names remain separate review candidates.
