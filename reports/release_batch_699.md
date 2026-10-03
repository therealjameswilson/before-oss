# Batch 699 release - Nelson-Nenadovich research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 699 covers PDF page 339, row 46, through page 340, row 22, from James A
Nelson through Lubitsa Nenadovich. Fresh visual inspection confirmed all 23
printed rows. The immutable extraction remains unchanged.

Official Army bulk evidence supports high-confidence identity-only decisions
for John T Nelson, Orval D Nelson, Oscar K Nelson Jr., Raymond A Nelson, Vern W
Nelson, and Peter N Nemeth. Exact names and nonshared protected identifiers
agree. No coded Army occupation is converted into an employer.

Leonard A Nelson and John A Nemecz remain visible conflicts. Their printed
protected identifiers reach official Army bulk names that materially disagree
with the indexed names. Neither row is merged and no occupation or employer
data are transferred.

The current Library of Congress API produced 35 discovery candidates across
eight people. Official OCR page context for every candidate was reviewed with
full-name queries, per-request pacing, bounded retries, and in-memory-only
response handling. All 35 were rejected as unrelated namesakes, different
initials or names, postwar items, or OCR collisions. The CIA adapter failed
closed at the site's robots policy without sending a search request; targeted
official and institutional searches returned no defensible pre-OSS employer.
Later-life records for Lubitsa Nenadovich and Walter C Nemetz were not assigned
without a reliable indexed-identity or wartime bridge.

The cohort records two `conflicting_sources` and 21
`no_reliable_result_after_protocol` outcomes. Identity statuses are six
`high_confidence`, two `conflicting`, and 15 `unresolved`. The evidence bundle
adds two sources, no organizations or affiliations, eight identity claims, 16
claim-source links, 23 person updates, and 23 consolidated research attempts.
Six Army identity candidates are accepted, two Army candidates are recorded as
conflicts, and 35 LoC source candidates are rejected.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,121 (38.1010%) |
| People with confirmed/high employer evidence | 317 (1.3242%) |
| People with confirmed/high affiliation evidence | 703 (2.9366%) |
| Archival-review dispositions assessed | 7,578 (31.6555%) |
| Not started | 14,813 |
| Possible duplicate groups | 520 |
| Conflicts | 268 |
| Attempts or plans | 16,428 |
| Claims by confidence | confirmed 1,343; high 2,648; medium 1,465; low 196; conflicting 241 |
| Citation records / unique source documents | 5,472 / 2,707 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 166; `conflicting_sources` 225;
`documented_prewar_employer_found` 152; `in_progress` 1,904;
`needs_identity_review` 442; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 781; `not_started` 14,813;
`occupation_only_found` 1,037; `requires_archival_review` 3,783; and
`verified_employer_found` 279.

The public projection contains **2,383** published affiliations, **803**
organizations, **4,255** public sources, and **5,690** published claims.
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
- Astro diagnostics: **333 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,779 pages**.
- Browser release suite: **84 / 84 passed** across desktop, phone, and tablet
  (15 Batch 699, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,779 HTML files** checked; every internal link resolved and
  50,558 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 103,564,274 bytes** verified; manifest SHA-256
  `630d6be204a0a22b1cba5425b67588dcf7959ebbef7ba087f4c73dffa4e98721`.
- Private-identifier audit: **24,851 artifacts**, 12,926 normalized identifiers,
  120 formatted variants, and 1,159 candidate substrings checked with **0
  unexpected boundary matches** and **0 false positives**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,851 files /
  303,967,683 bytes**, SHA-256
  `dba018231ad2e7f01816bd088595026898b204778b18482512cad86351979fa5`.

## Released and verified live

Batch 699 was fast-forwarded to `main` as commit
[`2e47baa7f9d0f6e7880844ed8e94aa92ee222a09`](https://github.com/therealjameswilson/before-oss/commit/2e47baa7f9d0f6e7880844ed8e94aa92ee222a09).
The GitHub Pages build and deployment
[`37112081847`](https://github.com/therealjameswilson/before-oss/actions/runs/37112081847)
and independent test workflow
[`37112081845`](https://github.com/therealjameswilson/before-oss/actions/runs/37112081845)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 103,564,274 bytes matched, as did eight core
routes, all 29 source-register pages, and the 23 Batch 699 profile routes. The
live site reports 23,978 source rows, 23,939 person entities, 9,121 researched
people, 703 verified affiliations, 317 verified employers, and 14,813
not-started people. The
[oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/)
continues to show nine people across 11 historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-699 --page 339 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-699 --page 340 --first-row 1 --last-row 22
python3 -m oss_research research --source cia --batch batch-699 --max-queries 23
python3 -m oss_research research --source loc --batch batch-699 --max-queries 23
python3 scripts/inspect_loc_candidates.py --batch batch-699 --max-candidates 35 --delay 3.2
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch699.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages339-340-nelson-nenadovich-review_batch-699_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 340, row 23. No API key, raw API
response, full service number, copyrighted page image, unrelated Army coded
occupation, street address, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
