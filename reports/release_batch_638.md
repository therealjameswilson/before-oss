# Batch 638 release status - pages 451-460 and McGill-McGovern research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 451-460 were compared
against SQLite at 180 dpi. Every page matches the current extraction. Because
pages 453, 455, and 456 were already in the random audit, the durable visual
ledger rises by seven pages and 322 rows to **380/522 pages** and
**17,446/23,978 rows**: **17,414** match the extraction, **32** retain reviewed
corrections, and **6,532** remain.

The page-309 `Barry McGill` through `William M. McGovern` queue contains 23
source rows and 23 people. The Library of Congress pass saved a live result for
every person and returned 11 discovery candidates across seven people. Every
official item context was inspected; all were rejected as conflicting-initial,
postwar, spousal, or unbridged common/famous-name results.

Eight official Army bulk crosswalks received high-confidence identity
decisions from nonshared protected identifiers and exact or explicitly
preserved name variants. Leon A. McGinnis remains conflicting because the
official Army entry prints middle initial D. The two David K. McGinnis index
rows remain separate and ambiguous because their grades, boxes, and lack of a
common identifier do not support a merge. Full identifiers stay private; Army
grades and occupation codes are not employer evidence.

The final queue state is 20 `in_progress`, two `needs_identity_review`, and one
`conflicting_sources`. All 20 candidates have decisions: eight accepted, one
conflicting, and 11 rejected. This is research-attempt progress, not completion
of the minimum research protocol. No new employer or affiliation claim was
made.

The oil-company category remains prominently available in the site navigation,
home page, and personnel directory. It lists the current evidence-scoped set of
**seven people** across **nine historically named companies** and excludes
mere text matches and unsupported candidates.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 17,446 / 23,978 rows; 380 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,786 (32.5243%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,322 (26.4088%) |
| Not started | 16,146 |
| Possible duplicate groups | 488 |
| Conflicts | 165 |
| Attempts or plans | 12,925 |
| Claims by confidence | confirmed 1,311; high 1,944; medium 1,375; low 187; conflicting 140 |
| Citation records / unique source documents | 5,068 / 2,386 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 126;
`documented_prewar_employer_found` 118; `in_progress` 1,659;
`needs_identity_review` 399; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,146;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,861
sources, and 4,766 claims. Full-index historical research remains unfinished.

## Local verification

Local verification has not yet been run for this candidate. Exact test, build,
link, privacy, determinism, manifest, and deployment results will replace this
paragraph before the release is reported complete.

## Deployment

Not yet deployed. The exact release commit, workflow runs, and read-only public
verification will be recorded here after deployment.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages451-460_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch638.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch638.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page309-mcgill-mcgovern-review_batch-638_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
