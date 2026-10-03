# Batch 698 release - Nelligan-Nelson research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 698 covers PDF page 339, rows 23-45, from James G Nelligan through
Isadore Nelson. Fresh visual inspection confirmed all 23 printed rows. The
immutable extraction remains unchanged.

Official Army bulk evidence supports high-confidence identity-only decisions
for James G Nelligan, Andrew E Nelson, Clifford R Nelson, Franklin Nelson,
Gilmer H Nelson, Herman Nelson, Ingolv Nelson, and Isadore Nelson. Exact names
and nonshared protected identifiers agree. No coded Army occupation is
converted into an employer, and Herman Nelson's anomalous coded entry date is
not used for wartime chronology.

A 9 May 1945 OSS Operational Group special order supplies a high-confidence
identity match and wartime OSS assignment for Harold G Nelson. The indexed
name, Technician Third Grade rank, and protected identifier agree, and the
order assigns him to Company B, Special Reconnaissance Battalion. An article
in *Veritas*, the U.S. Army Special Operations history journal, independently
names Sgt Ingolv Nelson on the OSS Maritime Unit P-101 crew. These sources
document wartime OSS context; neither identifies the immediate pre-OSS
affiliation or a civilian employer, and the site does not present either as
such.

Charles H Nelson and Charles W Nelson remain visible conflicts. Their printed
protected identifiers reach official Army bulk names that materially disagree
with the indexed names. Neither row is merged and no occupation or employer
data are transferred.

The current Library of Congress API produced 58 discovery candidates. Official
OCR page context for every candidate was reviewed with full-name queries,
per-request pacing, bounded retries, and in-memory-only response handling. All
58 were rejected as unrelated namesakes, different initials or ranks, postwar
items, or OCR collisions. The CIA adapter failed closed at the site's robots
policy without sending a search request; targeted official-domain discovery
searches returned no candidate.

The cohort records two `completed`, two `conflicting_sources`, and 19
`no_reliable_result_after_protocol` outcomes. Identity statuses are nine
`high_confidence`, two `conflicting`, and 12 `unresolved`. The evidence
bundle adds four sources, no organizations or affiliations, 11 identity
claims, 23 claim-source links, 23 person updates, and 23 consolidated research
attempts. Eight Army identity candidates are accepted, two Army candidates are
recorded as conflicts, and 58 LoC source candidates are rejected.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,098 (38.0049%) |
| People with confirmed/high employer evidence | 317 (1.3242%) |
| People with confirmed/high affiliation evidence | 703 (2.9366%) |
| Archival-review dispositions assessed | 7,555 (31.5594%) |
| Not started | 14,836 |
| Possible duplicate groups | 520 |
| Conflicts | 266 |
| Attempts or plans | 16,372 |
| Claims by confidence | confirmed 1,343; high 2,642; medium 1,465; low 196; conflicting 239 |
| Citation records / unique source documents | 5,470 / 2,706 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 166; `conflicting_sources` 223;
`documented_prewar_employer_found` 152; `in_progress` 1,904;
`needs_identity_review` 442; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 760; `not_started` 14,836;
`occupation_only_found` 1,037; `requires_archival_review` 3,783; and
`verified_employer_found` 279.

The public projection contains **2,383** published affiliations, **803**
organizations, **4,253** public sources, and **5,682** published claims.
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
- Astro diagnostics: **332 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,779 pages**.
- Browser release suite: **81 / 81 passed** across desktop, phone, and tablet
  (12 Batch 698, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,779 HTML files** checked; every internal link resolved and
  50,558 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 103,527,646 bytes** verified; manifest SHA-256
  `dcf5c478ea7bb79be94f1fd585b32b5bfc18d7f92688e10bbfc46b8272d54be6`.
- Private-identifier audit: **24,851 artifacts**, 12,926 normalized identifiers,
  120 formatted variants, and 1,159 candidate substrings checked with **0
  unexpected boundary matches** and **0 false positives**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,851 files /
  303,907,259 bytes**, SHA-256
  `3b646e93c0cd54298affbda688b4d13c5084ba0d738b4d38cbc24ee637a2da2a`.

## Released and verified live

Batch 698 was fast-forwarded to `main` as commit
[`8570e981989d5516b1432fa5fa4def85ed21b3ef`](https://github.com/therealjameswilson/before-oss/commit/8570e981989d5516b1432fa5fa4def85ed21b3ef).
The GitHub Pages build and deployment
[`37108581808`](https://github.com/therealjameswilson/before-oss/actions/runs/37108581808)
and independent test workflow
[`37108581759`](https://github.com/therealjameswilson/before-oss/actions/runs/37108581759)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 103,527,646 bytes matched, as did eight core
routes, all 29 source-register pages, and the 23 Batch 698 profile routes. The
live site reports 23,978 source rows, 23,939 person entities, 9,098 researched
people, 703 verified affiliations, 317 verified employers, and 14,836
not-started people. The
[oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/)
continues to show nine people across 11 historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-698 --page 339 --first-row 23 --last-row 45
python3 -m oss_research research --source cia --batch batch-698 --max-queries 23
python3 -m oss_research research --source loc --batch batch-698 --max-queries 23
python3 scripts/inspect_loc_candidates.py --batch batch-698 --max-candidates 58 --delay 3.2
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch698.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page339-nelligan-nelson-review_batch-698_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 339, row 46. No API key, raw API
response, full service number, copyrighted page image, unrelated Army coded
occupation, street address, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
