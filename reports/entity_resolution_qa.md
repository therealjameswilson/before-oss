# Entity-resolution QA

Generated: 2026-09-23T05:18:50+00:00

- Source rows: **23,978**.
- Cautious person entities: **23,939**.
- Superseded person entities retained for audit: **2** of **23,941** stored rows.
- Source rows linked: **23,978**.
- Narrow automatic same-name/same-service-number groups: **27**.
- Possible duplicate groups: **492**.
- Same-service-number/different-name groups: **164**.
- Entities requiring manual review: **23,078**.

## Checks

- PASS - `all_source_rows_linked`
- PASS - `no_name_only_automatic_merges`
- PASS - `all_duplicate_groups_require_review`

Exact normalized names alone never trigger an automatic merge. Identical printed service numbers attached to different names remain separate review candidates.
