# Batch 637 release status - pages 441-450 and McFaddin-McGhee research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 441-450 were compared
against SQLite at 180 dpi. Every page matches the current extraction. Because
pages 442, 444, and 447 were already in the random audit, the durable visual
ledger rises by seven pages and 322 rows to **373/522 pages** and
**17,124/23,978 rows**: **17,092** match the extraction, **32** retain reviewed
corrections, and **6,854** remain.

The page-308 `Lawerence B. McFaddin` through `William M. McGhee` queue contains
23 source rows and 23 people. The Library of Congress pass saved a live result
for every person and returned 11 discovery candidates across six people. Every
official item context was inspected; all were rejected as conflicting-name or
unbridged common-name results.

Ten official Army bulk crosswalks received high-confidence identity decisions
from nonshared protected identifiers and exact or explicitly preserved name
variants. William C. McGaragle remains ambiguous because his protected
identifier is also printed for William C. McAragle on page 303; the Army entry
supports the McGaragle spelling, but no merge is made pending comparison of
Boxes 496 and 505. The McCaughy/McGaughy cluster also remains separate and
ambiguous. Full identifiers stay private; Army grades and occupation codes are
not employer evidence.

The final queue state is 20 `in_progress` and three `needs_identity_review`.
All 24 candidates have decisions: ten accepted, three probable, and 11
rejected. This is research-attempt progress, not completion of the minimum
research protocol. No new employer or affiliation claim was made.

The oil-company category remains prominently available in the site navigation,
home page, and personnel directory. It lists the current evidence-scoped set of
**seven people** across **nine historically named companies** and excludes
mere text matches and unsupported candidates.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 17,124 / 23,978 rows; 373 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,763 (32.4283%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,313 (26.3712%) |
| Not started | 16,167 |
| Possible duplicate groups | 488 |
| Conflicts | 164 |
| Attempts or plans | 12,890 |
| Claims by confidence | confirmed 1,311; high 1,936; medium 1,375; low 187; conflicting 139 |
| Citation records / unique source documents | 5,066 / 2,385 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 125;
`documented_prewar_employer_found` 118; `in_progress` 1,639;
`needs_identity_review` 399; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,167;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,859
sources, and 4,757 claims. Full-index historical research remains unfinished.

## Local verification

The isolated tracked-only candidate passes all local release gates:

- **132/132** Python unit tests;
- **84/84** browser checks across desktop, phone, and tablet: 15 Batch 637,
  33 core-route, six analysis, and 30 accessibility/axe checks;
- Astro check with zero errors, warnings, or hints across **268** source files;
- **24,681** static HTML pages and **24,753** total artifacts;
- every internal link resolved, with **50,238** unique external URLs
  inventoried for the separate live check;
- all **67** manifest-listed assets matched, totaling **98,362,523** bytes at
  manifest SHA-256
  `3c2ce3c66855b56003e64cfed3ded21547ff4e675f6adcbdd860bb94648ac454`;
- the public-identifier audit compared **12,926** normalized identifiers and
  **120** formatted variants with zero unexpected full-number boundary matches;
- two clean builds reproduced production-tree SHA-256
  `e9cbde5128c3a921acb31355166f4e9a2f2d080c32ef87f741fe65d742f5328e`.

Unrelated user-owned duplicate files remain preserved and excluded.

## Deployment

Pending commit, pull request, CI, merge, Pages deployment, and exact-ref public
verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages441-450_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch637.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch637.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page308-mcfaddin-mcghee-review_batch-637_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
