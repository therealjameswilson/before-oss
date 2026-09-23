# Batch 649 release status - pages 45-54 and Mellen-Mencoboni research

Research date: 2026-09-23 America/New_York. This report records the reviewed
research, extraction, and local release-verification state. Production
deployment evidence is added after the reviewed release merges.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 45-54 were compared
against the extraction at 180 dpi. Pages 46, 50, and 53 were already covered;
the other **322** rows received their first complete visual comparison. Every
row matches. Complete-page visual review now covers **475/522 pages** and
**21,816/23,978 rows**: **21,784** match the extraction, **32** retain reviewed
corrections, and **2,162** remain unaudited. All PDF pages remain represented,
every parser warning is resolved, and SQLite integrity and foreign-key checks
pass.

The page-315/316 `Constance L. Mellen` through `Daniel J. Mencoboni` queue
contains **22 source rows and 22 cautious people**. Every person received four
staged source-specific plans and a saved reviewed outcome. Ten exact official
Army identity bridges were accepted; August O. Melnar and Oleg Melnikoff II
remain probable variants, and Joseph V. Menanga remains conflicting with the
`Menengas` form attached to the same protected identifier.

The principal employment finding is **Amos W. Melton**. The Fort Worth
Star-Telegram is modeled as his last documented civilian employer before
wartime service, while the United States Army Air Forces is modeled separately
as his immediate documented military assignment before his 1944 OSS posting.
A November 6, 1945 Office of Price Administration directory entry for Dolores
J. Mencke was checked in the official GovInfo scan and retained as a rejected
post-OSS lead, not a pre-OSS affiliation.

The cohort ends with 18 `in_progress`, two `needs_identity_review`, one
`conflicting_sources`, and one `verified_employer_found` status. Identity
statuses are 11 `high_confidence`, eight `unresolved`, two `probable`, and one
`conflicting`. The evidence bundle adds 16 claims: 13 high, two medium, and one
conflicting. The oil-company category remains limited to the supported set of
**seven people across nine historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 21,816 / 23,978 rows; 475 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,032 (33.5519%) |
| People with confirmed/high employer evidence | 285 (1.1905%) |
| People with confirmed/high affiliation evidence | 637 (2.6609%) |
| Archival-review dispositions assessed | 6,490 (27.1106%) |
| Not started | 15,902 |
| Possible duplicate groups | 492 |
| Conflicts | 180 |
| Attempts or plans | 13,564 |
| Claims by confidence | confirmed 1,311; high 2,033; medium 1,394; low 187; conflicting 155 |
| Citation records / unique source documents | 5,120 / 2,424 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 139;
`documented_prewar_employer_found` 119; `in_progress` 1,864;
`needs_identity_review` 418; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,902;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 262.

The public projection contains **2,243** published affiliations, **720**
organizations, **3,912** public sources, and **4,889** published claims.
Full-index historical research remains unfinished.

## Local verification

The exact tracked-only release candidate passes:

- **133/133** Python unit tests;
- Astro diagnostics across **280** source files with zero errors, warnings, or
  hints;
- **84/84** bounded Playwright checks: 15 Batch 649, 33 core route and
  interaction, six analysis, and 30 accessibility checks across desktop,
  phone, and tablet;
- internal-link validation across **24,694** generated HTML files;
- public-identifier redaction across **24,766** production artifacts, with
  zero aggregate, manifest-size, or unexpected-boundary matches; and
- local manifest verification of **67** projected assets totaling
  **99,139,369 bytes**, manifest SHA-256
  `257ecd79b728666f6ba2efaad08c2bd70d19780048fc06410343b32beaa7b069`.

Two complete tracked-only site builds produced the same **24,766-file,
295,976,336-byte** tree with SHA-256
`f9a75fc389b076fcec4ffce8990961b16377c7648fbcbf249d93c424e068c168`.
User-owned Finder-style ` 2` files and local SQLite sidecars were excluded
from the isolated build and remain untouched.

## Deployment

Research [PR #399](https://github.com/therealjameswilson/before-oss/pull/399)
passed its required test and merged as commit
`c79a1903ea25f2789bbeb7ade4da74a75edd3a31`. The post-merge
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35837383882)
and [GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35837383794)
both completed successfully. The test workflow emitted only GitHub-hosted
runner migration notices about Node.js 20 actions and a future
`ubuntu-latest` image change; no project check failed.

Commit-specific live verification at
[Before OSS](https://therealjameswilson.github.io/before-oss/) reproduced the
expected **67 assets**, **99,139,369 bytes**, and manifest SHA-256
`257ecd79b728666f6ba2efaad08c2bd70d19780048fc06410343b32beaa7b069`.
It also verified all **eight** core routes, **27** source-register pages, and
the **22** direct profiles represented in the Batch 649 evidence bundle. The
[oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/)
remains live with its evidence-scoped seven-person set.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages45-54_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch649.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-23_batch649.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page315-316-mellen-mencoboni-review_batch-649_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published. No authenticated NARA Catalog
request was made.
