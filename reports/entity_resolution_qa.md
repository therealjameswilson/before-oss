# Entity-resolution QA

Generated: 2026-10-15T15:13:17+00:00

- Source rows: **23,978**.
- Cautious person entities: **23,938**.
- Superseded person entities retained for audit: **3** of **23,941** stored rows.
- Source rows linked: **23,978**.
- Narrow automatic same-name/same-service-number groups: **18**.
- Possible duplicate groups: **552**.
- Same-service-number/different-name groups: **163**.
- Entities requiring manual review: **22,571**.

## Checks

- PASS - `all_source_rows_linked`
- PASS - `no_name_only_automatic_merges`
- PASS - `all_duplicate_groups_require_review`

Exact normalized names alone never trigger an automatic merge. Identical printed service numbers attached to different names remain separate review candidates.
