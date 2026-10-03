# Batch 696 release - Naylor-Neff research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 696 covers PDF page 338, rows 23-45, from Glenn R Naylor through
Charles R Neff. Fresh visual inspection confirmed all 23 printed rows. The
immutable extraction remains unchanged.

Robert D Neasse is a high-confidence identity match. His exact name and
nonshared protected identifier agree between the OSS index and official Army
data, while an Arizona Republic obituary supplies a dated Army-to-OSS
chronology. The site records the United States Army as his immediate pre-OSS
military assignment and Ohio Wesleyan University separately as student status;
the university is not presented as an employer.

Charles F Neave is a high-confidence match to the officer listed in the 1916
Field Artillery Journal directory. His Battery B assignment is published only
as earlier documented military service, not as an immediate pre-OSS post or a
Yale employment or education claim. Harry M Neben is a high-confidence match
to the Illinois amateur radio operator W9QB. His amateur-radio work is an
occupation-only finding; postwar employers are excluded and no pre-OSS
employer is invented.

Paul Nebenzahl, Dean B Needham, Glenn R Naylor, Herman E Naylor Jr., and Joseph
Nechunskas receive high-confidence identity-only decisions. Martin E Nedell
remains a qualified probable match. Adam M Neely remains an explicit identity
conflict because the printed protected identifier reaches an Army record with
a materially different surname and grade. No Army coded occupation is
converted into an employer claim.

The cohort records two `completed`, one `occupation_only_found`, one
`conflicting_sources`, and 19 `no_reliable_result_after_protocol` outcomes.
Identity statuses are eight `high_confidence`, one `probable`, one
`conflicting`, and 13 `unresolved`. The oil-company category remains **nine
people across 11 historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,052 (37.8128%) |
| People with confirmed/high employer evidence | 317 (1.3242%) |
| People with confirmed/high affiliation evidence | 702 (2.9325%) |
| Archival-review dispositions assessed | 7,509 (31.3672%) |
| Not started | 14,882 |
| Possible duplicate groups | 520 |
| Conflicts | 262 |
| Attempts or plans | 16,256 |
| Claims by confidence | confirmed 1,343; high 2,621; medium 1,461; low 196; conflicting 235 |
| Citation records / unique source documents | 5,456 / 2,695 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 161; `conflicting_sources` 219;
`documented_prewar_employer_found` 152; `in_progress` 1,904;
`needs_identity_review` 442; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 723; `not_started` 14,882;
`occupation_only_found` 1,037; `requires_archival_review` 3,783; and
`verified_employer_found` 279.

The public projection contains **2,379** published affiliations, **801**
organizations, **4,239** public sources, and **5,653** published claims.
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
- Astro diagnostics: **330 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,777 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 696, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,777 HTML files** checked; every internal link resolved and
  50,548 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 103,358,165 bytes** verified; manifest SHA-256
  `ba4a94d0a79a430cb988e089570ef9ca0f575ec63f9a23885b773a1245671a8a`.
- Private-identifier audit: **24,849 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,849 files /
  303,635,183 bytes**, SHA-256
  `e2b223ff37ba4ae185188f0269ded1acc60d90819efcbf1e40a65e5c9032aeed`.

## Released and verified live

Batch 696 was fast-forwarded to `main` as commit
[`7a555b3e5bf829b4fe7e87a67a46096b7034a462`](https://github.com/therealjameswilson/before-oss/commit/7a555b3e5bf829b4fe7e87a67a46096b7034a462).
The GitHub Pages build and deployment
[`37103428577`](https://github.com/therealjameswilson/before-oss/actions/runs/37103428577)
and independent test workflow
[`37103428580`](https://github.com/therealjameswilson/before-oss/actions/runs/37103428580)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 103,358,165 bytes matched, as did eight core
routes, all 29 source-register pages, and the 23 Batch 696 profile routes. The
live site reports 23,978 source rows, 23,939 person entities, 9,052 researched
people, 702 verified affiliations, 317 verified employers, and 14,882
not-started people. The
[oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/)
continues to show nine people across 11 historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-696 --page 338 --first-row 23 --last-row 45
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch696.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page338-naylor-neff-review_batch-696_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 338, row 46. No API key, raw API
response, full service number, copyrighted page image, unrelated Army coded
occupation, street address, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
