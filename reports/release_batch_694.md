# Batch 694 release - Nakao-Nash research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 694 covers PDF page 337, rows 23-45, from Errol M Nakao through John S
Nash. Fresh visual inspection confirmed all 23 printed rows, including Edward J
Napieralski's service identifier displaced into the rank/serial boundary. The
immutable extraction remains unchanged.

Ann Nash has the cohort's verified employer finding. Three visually reviewed
issues of Cornell Alumni News identify E. Ann Nash as a Vogue staff member and
former editorial assistant, and connect Ann Nash Bottorff's year at Vogue to
her return to China in 1945 as an OSS employee. Vogue is therefore published
at high confidence as both her best-supported immediate pre-OSS affiliation
and last named civilian employer. The temporal basis remains
`strongly_date_bounded`, not `explicit_immediate`.

Gust Nanos is a high-confidence identity match to T/5 Gus Nanos in the OSS
Greek Operational Group VII roster. The roster corroborates identity and
service only; it does not establish a pre-OSS employer. Official Army data
supports high-confidence identity matches for Errol M Nakao, Joe H Nakata,
Peter T Namkoong, Edward J Napieralski, John B Napoles, Ralph R Napolitano,
Dino Nardi, Joseph J Nardi, Warren L Nardin, Boleslaus V Narewski, and John S
Nash. Those decisions accept identity only and do not convert Army coded
occupations into employers.

George K Nakashima, A Napombejara, Chok Naranong, Charles P Nash, Herman T
Nash, and John Nash remain unresolved where the reviewed evidence did not
bridge the index person to a namesake. The cohort records 22
`no_reliable_result_after_protocol` outcomes and one
`verified_employer_found` outcome. Identity statuses are 13 `high_confidence`
and ten `unresolved`. The oil-company category remains **nine people across 11
historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,007 (37.6248%) |
| People with confirmed/high employer evidence | 316 (1.3200%) |
| People with confirmed/high affiliation evidence | 698 (2.9157%) |
| Archival-review dispositions assessed | 7,464 (31.1792%) |
| Not started | 14,927 |
| Possible duplicate groups | 519 |
| Conflicts | 259 |
| Attempts or plans | 16,211 |
| Claims by confidence | confirmed 1,340; high 2,598; medium 1,459; low 196; conflicting 232 |
| Citation records / unique source documents | 5,438 / 2,680 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 159; `conflicting_sources` 216;
`documented_prewar_employer_found` 151; `in_progress` 1,904;
`needs_identity_review` 442; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 686; `not_started` 14,927;
`occupation_only_found` 1,036; `requires_archival_review` 3,783; and
`verified_employer_found` 278.

The public projection contains **2,373** published affiliations, **800**
organizations, **4,221** public sources, and **5,622** published claims.
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
- Astro diagnostics: **328 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,776 pages**.
- Browser release suite: **84 / 84 passed** across desktop, phone, and tablet
  (15 Batch 694, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,776 HTML files** checked; every internal link resolved and
  50,535 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 103,164,422 bytes** verified; manifest SHA-256
  `69b6b4f6ebd512c7d55002174dd2cedbf807fcabf1c11c796998c4478f3f079b`.
- Private-identifier audit: **24,848 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,848 files /
  303,333,567 bytes**, SHA-256
  `73b8d7dcba88f3c4e1907db4eea12d79dfbebe54af0d898604e0ea4ae9128d41`.

## Released and verified live

Batch 694 was fast-forwarded to `main` as commit
[`46876dc3ef944700767e4fb5f4213739b3347c57`](https://github.com/therealjameswilson/before-oss/commit/46876dc3ef944700767e4fb5f4213739b3347c57).
The GitHub Pages build and deployment
[`37098743085`](https://github.com/therealjameswilson/before-oss/actions/runs/37098743085)
and independent test workflow
[`37098743092`](https://github.com/therealjameswilson/before-oss/actions/runs/37098743092)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 103,164,422 bytes matched, as did eight core
routes, all 29 source-register pages, and the 23 Batch 694 profile routes. The
live site reports 23,978 source rows, 23,939 person entities, 9,007 researched
people, 698 verified affiliations, 316 verified employers, and 14,927
not-started people. The
[oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/)
continues to show nine people across 11 historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-694 --page 337 --first-row 23 --last-row 45
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch694.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page337-nakao-nash-review_batch-694_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, street address, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
