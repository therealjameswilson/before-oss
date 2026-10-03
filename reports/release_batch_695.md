# Batch 695 release - Nash-Nawrocki research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 695 covers PDF page 337, row 46, and page 338, rows 1-22, from Warren
E Nash through Walter T Nawrocki. Fresh visual inspection confirmed all 23
printed rows. The immutable extraction remains unchanged.

Robert R Nathan is a confirmed identity match. His exact name and nonshared
protected identifier agree between the OSS index and official Army data, and
his edited Truman Library oral history provides a direct chronology. The site
records the U.S. Army as his immediate pre-OSS military assignment and the War
Production Board Planning Committee separately as his last civilian
pre-service government affiliation.

Leonard H Nason is a high-confidence identity match. A contemporary TIME
article identifies him as Mutual Broadcasting System's military analyst in
1940, independently supported by Norwich University material. Mutual is
published only as documented prewar employment because the reviewed sources do
not establish that it immediately preceded OSS service.

Malia G Natirbov remains a probable identity match and receives no employer
claim. Charles J Naura is a high-confidence match to Charles J Nuara, with both
spellings preserved. Frank Navellou and James K Naughan remain explicit
identity conflicts because their printed protected identifiers do not support
a safe resolution. Official Army evidence supports eight additional
high-confidence identity-only decisions without converting coded occupations
into employers. John F Navarro retains his earlier occupation-only outcome.

The cohort records one `verified_employer_found`, one
`documented_prewar_employer_found`, one `occupation_only_found`, two
`conflicting_sources`, and 18 `no_reliable_result_after_protocol` outcomes.
Identity statuses are one `confirmed`, 11 `high_confidence`, one `probable`,
two `conflicting`, and eight `unresolved`. The oil-company category remains
**nine people across 11 historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,029 (37.7167%) |
| People with confirmed/high employer evidence | 317 (1.3242%) |
| People with confirmed/high affiliation evidence | 700 (2.9241%) |
| Archival-review dispositions assessed | 7,486 (31.2711%) |
| Not started | 14,905 |
| Possible duplicate groups | 520 |
| Conflicts | 261 |
| Attempts or plans | 16,233 |
| Claims by confidence | confirmed 1,343; high 2,609; medium 1,460; low 196; conflicting 234 |
| Citation records / unique source documents | 5,445 / 2,686 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 159; `conflicting_sources` 218;
`documented_prewar_employer_found` 152; `in_progress` 1,904;
`needs_identity_review` 442; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 704; `not_started` 14,905;
`occupation_only_found` 1,036; `requires_archival_review` 3,783; and
`verified_employer_found` 279.

The public projection contains **2,376** published affiliations, **800**
organizations, **4,228** public sources, and **5,639** published claims.
Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all parser-warning rows visually
  resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing.
- Astro diagnostics: **329 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,776 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 695, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,776 HTML files** checked; every internal link resolved and
  50,540 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 103,261,337 bytes** verified; manifest SHA-256
  `4f67d03e2a44c019c8469d103bd44f0bc3e0e41f059f0f771af4b43eb11da5fa`.
- Private-identifier audit: **24,848 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,848 files /
  303,484,340 bytes**, SHA-256
  `d2b74443ee730ec219c8e9b89734ee1cd28b5c30af9121c019aa7bfccb7be334`.

## Released and verified live

Batch 695 was fast-forwarded to `main` as commit
[`b3df47d226355bf511f3cf775807a11816fe696b`](https://github.com/therealjameswilson/before-oss/commit/b3df47d226355bf511f3cf775807a11816fe696b).
The GitHub Pages build and deployment
[`37100987081`](https://github.com/therealjameswilson/before-oss/actions/runs/37100987081)
and independent test workflow
[`37100987068`](https://github.com/therealjameswilson/before-oss/actions/runs/37100987068)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 103,261,337 bytes matched, as did eight core
routes, all 29 source-register pages, and the 23 Batch 695 profile routes. The
live site reports 23,978 source rows, 23,939 person entities, 9,029 researched
people, 700 verified affiliations, 317 verified employers, and 14,905
not-started people. The
[oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/)
continues to show nine people across 11 historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-695-boundary --page 337 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-695 --page 338 --first-row 1 --last-row 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch695.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages337-338-nash-nawrocki-review_batch-695_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 338, row 23. No API key, raw API
response, full service number, copyrighted page image, unrelated Army coded
occupation, street address, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
