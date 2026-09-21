# Batch 619 release status — pages 261–270 and variant review

Date: 2026-09-21 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 261–270 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match; no correction was
needed. Because five pages overlapped required middle-page or warning-page QA,
the complete-page visual-review ledger advances by five pages and 230 rows to
**224/522 pages** and **10,270/23,978 rows**, leaving **13,708** rows.

Fifteen possible-duplicate, spelling-variant, or identifier-conflict groups
covering 45 people were reviewed without an unsupported merge. The two Reynold
W Larson rows remain linked to one high-confidence entity while preserving
both source rows and boxes. Same-identifier/different-name collisions are
explicit conflicts with critical archival priority; plausible spelling,
middle-initial, and name-order variants remain ambiguous and separate. Public
group labels are non-identifying hashes.

A bounded Library of Congress pass completed 46 page-261 searches. Its two
discovery candidates were rejected after contextual review for conflicting or
missing identifiers and the absence of an OSS or employment bridge. No
employer claim was added, and no authenticated NARA request was made.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,285 (30.4315%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,162 (25.7404%) |
| Not started | 16,654 |
| Possible duplicate groups | 450 |
| Conflicts | 141 |
| Attempts or plans | 12,342 |
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
- bounded Playwright release suite: **81/81** tests, including **30**
  accessibility tests with no serious or critical axe violations;
- internal-link audit: all links resolved across 24,681 HTML files; **50,236**
  unique external URLs inventoried for separate live checking;
- public-identifier audit: **12,926** normalized private identifiers and **120**
  formatted variants checked across 24,753 artifacts, with zero unexpected
  boundary matches or aggregate/manifest false positives; and
- local release-manifest verification: **67 assets**, **98,003,514 bytes**,
  manifest SHA-256
  `4ef376c64439bef98ce651dffc2c4810d26ca4aa1356cb65d3433ce3e3cd7ec3`.

Two independent clean production builds produced the same 24,753-file,
294,155,584-byte tree SHA-256:
`1f836e027bda9dc6144bf421d2fb75be0f3cf109b98a44e0551dd52e61735d58`.

## Deployment

Pending push, required CI, merge, Pages deployment, and unauthenticated live
manifest and route verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages261-270_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch619.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages261-270-duplicate-review_batch-619_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The exact page-batch assignment commands are recorded in
`research/batch-619-progress.md`. No API key, raw API response, full service
number, or private reviewer note is committed or published.
