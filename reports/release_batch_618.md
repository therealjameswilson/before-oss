# Batch 618 release status — pages 251–260 and David Krech

Date: 2026-09-21 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 251–260 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match; no correction was
needed. The complete-page visual-review ledger now covers **219/522** pages and
**10,040/23,978** rows, leaving **13,938** rows.

Thirteen possible-duplicate, spelling-variant, or identifier-conflict groups
covering 26 people were reviewed without merging them. Public group labels are
non-identifying hashes. One distinct reviewed merge resolves the adjacent
David Krech and Isadore Krechevsky rows to a single high-confidence person
entity while preserving both immutable source rows and both indexed names.

Krech now has two separately modeled earlier prewar employers: Swarthmore
College in 1937 and the University of Colorado in 1938–1939. Neither is
presented as the immediate pre-OSS affiliation or last civilian employer,
because the institutional chronology reports later unnamed nonacademic jobs
and imprecisely identified pre-Army survey work. A bounded Library of Congress
pass completed 46 page-251 searches and recorded 22 discovery candidates; none
is accepted as an identity or employer claim by this batch.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,239 (30.2394%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,118 (25.5566%) |
| Not started | 16,700 |
| Possible duplicate groups | 435 |
| Conflicts | 133 |
| Attempts or plans | 12,296 |
| Claims by confidence | confirmed 1,311; high 1,898; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,045 / 2,372 |

The public projection contains 2,224 affiliations, 708 organizations, 3,842
sources, and 4,711 claims. The oil-company category remains a supported,
incomplete evidence set of seven people across nine companies. Full-index
historical research remains unfinished.

## Local verification

The clean tracked-only release candidate passed:

- `validate-ingest`: all checks true; 23,978 rows on 522 pages, zero foreign-key
  errors, and SQLite `quick_check` `ok`;
- Python unit tests: **126/126**;
- deterministic structural profile audit: **200** sampled profiles and all seven
  checks true;
- Astro validation/build: **0 errors, 0 warnings, 0 hints** and **24,681** HTML
  pages (**24,753** total artifacts);
- bounded Playwright release suite: **84/84** tests, including **30**
  accessibility tests with no serious or critical axe violations;
- internal-link audit: all links resolved across 24,681 HTML files; **50,236**
  unique external URLs inventoried for separate live checking;
- public-identifier audit: **12,926** normalized private identifiers and **120**
  formatted variants checked across 24,753 artifacts, with zero unexpected
  boundary matches or aggregate/manifest false positives; and
- local release-manifest verification: **67 assets**, **97,982,649 bytes**,
  manifest SHA-256
  `4978362fdd3cab50c7f3b5c386948795a85562e7255f90b11653bd40e564174a`.

Two independent clean production builds produced the same 24,753-file,
294,116,447-byte tree SHA-256:
`27d7e4704d6fbacaa03d6dee0196b64b4c3b4db717bbd85a05c0172ef5965891`.

## Deployment

Research pull request
[#337](https://github.com/therealjameswilson/before-oss/pull/337)
passed its required test job and merged as commit
`49f1c627557bdc017ffb1e2ddace81fcfca013b5`. The post-merge
[Test run 35594512963](https://github.com/therealjameswilson/before-oss/actions/runs/35594512963)
and
[Pages run 35594512974](https://github.com/therealjameswilson/before-oss/actions/runs/35594512974)
both completed successfully.

Unauthenticated verification against the deployed site and the exact merged
commit matched all **67** manifest assets and **97,982,649** bytes at manifest
SHA-256
`4978362fdd3cab50c7f3b5c386948795a85562e7255f90b11653bd40e564174a`.
It also verified all eight core routes, all 26 source-register pages, the
canonical David Krech profile, and all 26 profiles represented in the reviewed
duplicate/variant evidence bundle.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages251-260_2026-09-21.json
python3 -m oss_research import-review-decisions research/entity_review_decisions_2026-09-21_batch618.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages251-260-duplicate-review_batch-618_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-david-krech-isadore-krechevsky_batch-618_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The exact page-batch assignment commands are recorded in
`research/batch-618-progress.md`. No authenticated NARA request was made. No
API key, raw API response, full service number, or private reviewer note is
committed or published.
