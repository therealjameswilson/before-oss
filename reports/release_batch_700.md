# Batch 700 release - Nesbitt-Neumann research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 700 covers PDF page 340, rows 23-45, from Frank B Nesbitt through
Sigmund Neumann. Fresh visual inspection confirmed all 23 printed rows. The
immutable extraction remains unchanged.

Gerhardt Neumann is confirmed as Gerhard Neumann through the exact protected
identifier, indexed Master Sergeant rank, official Army evidence, the
Smithsonian catalog, a congressional report, and institutional aerospace
sources. The public profile distinguishes his immediate U.S. Army Air Corps
assignment, earlier American Volunteer Group service, and earlier aircraft-
maintenance work with the Chinese Nationalist Air Force. The last relationship
is explicitly not labeled an employer.

Frank B Nesbitt, Rudolph W Ness, Thomas E Nettles, Arthur J Neu Jr., and
Stanley P Neugebauer receive high-confidence identity-only decisions from exact
names and nonshared protected identifiers in official Army evidence. No coded
Army occupation is converted into an employer.

Harold E Ness and John E Nesline Jr. remain visible conflicts because official
Army evidence linked by the printed identifiers materially disagrees with the
indexed names. The two Robert G Neumann rows remain separate, ambiguous
entities in a documented possible-duplicate group. A plausible Beloit College
biography for Paul H Nesbitt remains a lead only; no affiliation is published
without a sufficiently specific bridge to the index record.

The Library of Congress API produced seven discovery candidates. Official OCR
context for each was inspected, and all seven were rejected as unrelated
namesakes or contexts that did not establish identity or pre-OSS work. The CIA
adapter failed closed at the site's robots policy without sending a request.
Exact-name, occupation, obituary, institutional, and archival searches were
completed for the cohort. Existing verified-employer outcomes for Franz L
Neumann and Sigmund Neumann are preserved.

The cohort records one `completed`, two `conflicting_sources`, three
`needs_identity_review`, 15 `no_reliable_result_after_protocol`, and two
pre-existing `verified_employer_found` outcomes. Identity statuses are one
`confirmed`, seven `high_confidence`, two `conflicting`, one `probable`, two
`ambiguous`, and ten `unresolved`. The evidence bundle adds seven sources,
three organizations, three affiliations, 13 claims, 29 claim-source links, 21
person updates, and 21 consolidated research attempts. Six Army identity
candidates are accepted, three conflicts are preserved, and seven LoC
candidates are rejected.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,142 (38.1887%) |
| People with confirmed/high employer evidence | 317 (1.3242%) |
| People with confirmed/high affiliation evidence | 704 (2.9408%) |
| Archival-review dispositions assessed | 7,599 (31.7432%) |
| Not started | 14,792 |
| Possible duplicate groups | 521 |
| Conflicts | 270 |
| Attempts or plans | 16,473 |
| Claims by confidence | confirmed 1,344; high 2,655; medium 1,466; low 196; conflicting 243; unresolved 2 |
| Citation records / unique source documents | 5,479 / 2,713 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 167; `conflicting_sources` 227;
`documented_prewar_employer_found` 152; `in_progress` 1,904;
`needs_identity_review` 445; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 796; `not_started` 14,792;
`occupation_only_found` 1,037; `requires_archival_review` 3,783; and
`verified_employer_found` 279.

The public projection contains **2,386** published affiliations, **806**
organizations, **4,262** public sources, and **5,701** published claims.
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
- Astro diagnostics: **334 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,782 pages**.
- Browser release suite: **84 / 84 passed** across desktop, phone, and tablet
  (15 Batch 700, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,782 HTML files** checked; every internal link resolved and
  50,566 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 103,650,247 bytes** verified; manifest SHA-256
  `44712a77bdd67871fb719079a33e37861a46cb4ce41ad6a5c857d60a4f4f3fb5`.
- Private-identifier audit: **24,854 artifacts**, 12,926 normalized identifiers,
  120 formatted variants, and 1,159 candidate substrings checked with **0
  unexpected boundary matches** and **0 false positives**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,854 files /
  304,109,862 bytes**, SHA-256
  `ba6cdfb9a371af62481813c3feef280e521fe1d723da441b3009bcaef45a0511`.

## Released and verified live

Batch 700 was fast-forwarded to `main` as commit
[`dc79489f37904f01e49ff2adae22f44482bc0fe8`](https://github.com/therealjameswilson/before-oss/commit/dc79489f37904f01e49ff2adae22f44482bc0fe8).
The GitHub Pages build and deployment
[`37114793686`](https://github.com/therealjameswilson/before-oss/actions/runs/37114793686)
and independent test workflow
[`37114793701`](https://github.com/therealjameswilson/before-oss/actions/runs/37114793701)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 103,650,247 bytes matched, as did eight core
routes, all 29 source-register pages, and all 23 Batch 700 profile routes. The
live site reports 23,978 source rows, 23,939 person entities, 9,142 researched
people, 704 verified affiliations, 317 verified employers, and 14,792
not-started people. Gerhardt Neumann's direct profile and the preserved
conflict, ambiguity, and unresolved profiles render from their public URLs.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-700 --page 340 --first-row 23 --last-row 45
python3 -m oss_research research --source cia --batch batch-700 --max-queries 23
python3 -m oss_research research --source loc --batch batch-700 --max-queries 23
python3 scripts/inspect_loc_candidates.py --batch batch-700 --max-candidates 7 --delay 3.2
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch700.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page340-nesbitt-neumann-review_batch-700_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 340, row 46. No API key, raw API
response, full service number, copyrighted page image, unrelated Army coded
occupation, street address, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
