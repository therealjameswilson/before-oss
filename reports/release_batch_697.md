# Batch 697 release - Neff-Nellhaus research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 697 closes PDF page 338 at row 46 and continues through page 339,
rows 1-22, from Jacqueline H Neff through Gerhardt Nellhaus. Fresh visual
inspection confirmed all 23 printed rows. The immutable extraction remains
unchanged.

Stanley Nehmer is a high-confidence identity match with a documented prewar
student affiliation at City College of New York. The university is recorded
as a school attended, not as an employer or a proven immediate predecessor to
OSS. Postwar State and Commerce Department roles are excluded from the
pre-OSS answer.

Julian M Neimczylc is published as a probable match to Julian Martin Niemczyk,
not as a settled identity. A Library of Congress-hosted oral history sequences
University of Oklahoma attendance, National Guard induction, artillery
service and battery command, an OSS recruitment interview, and a War
Department transfer to OSS. The site therefore publishes the United States
Army as a qualified immediate pre-OSS military assignment and the university
separately as earlier student status. Neither is called a civilian employer.

Gerhardt Nellhaus is a high-confidence match to Gerhard Nellhaus in 99th Bomb
Group Historical Society records. His German radio-message intercept work
with the 348th Squadron, 99th Bomb Group, is published as a wartime Army Air
Forces assignment. The reviewed sources do not establish its sequence
relative to OSS service, so it remains earlier wartime context with
`temporal_relation_uncertain`, not an immediate pre-OSS claim.

Eldon N Nehring and Lester C Neimann remain visible conflicts rather than
forced merges. The other nine people remain unresolved after the minimum
staged protocol and receive explicit archival-review guidance. No Army coded
occupation is converted into an employer claim.

The cohort records three `completed`, two `conflicting_sources`, and 18
`no_reliable_result_after_protocol` outcomes. Identity statuses are 11
`high_confidence`, one `probable`, two `conflicting`, and nine `unresolved`.
The evidence bundle adds ten sources, four organizations (two reused), four
affiliations, 18 claims, 39 claim-source links, 23 person updates, and 23
consolidated research attempts. Ten official identity candidates are accepted
and three candidate rows are recorded as conflicts.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,075 (37.9089%) |
| People with confirmed/high employer evidence | 317 (1.3242%) |
| People with confirmed/high affiliation evidence | 703 (2.9366%) |
| Archival-review dispositions assessed | 7,532 (31.4633%) |
| Not started | 14,859 |
| Possible duplicate groups | 520 |
| Conflicts | 264 |
| Attempts or plans | 16,279 |
| Claims by confidence | confirmed 1,343; high 2,633; medium 1,465; low 196; conflicting 237 |
| Citation records / unique source documents | 5,466 / 2,703 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 164; `conflicting_sources` 221;
`documented_prewar_employer_found` 152; `in_progress` 1,904;
`needs_identity_review` 442; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 741; `not_started` 14,859;
`occupation_only_found` 1,037; `requires_archival_review` 3,783; and
`verified_employer_found` 279.

The public projection contains **2,383** published affiliations, **803**
organizations, **4,249** public sources, and **5,671** published claims.
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
- Astro diagnostics: **0 errors, 0 warnings, 0 hints**.
- Production build: **24,779 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 697, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,779 HTML files** checked; every internal link resolved and
  50,557 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 103,472,820 bytes** verified; manifest SHA-256
  `ba7d79f23181cbed029d9fc813ea29e31bcbe860e07447442922bfe0a5de5dd9`.
- Private-identifier audit: **0 unexpected boundary matches** and **0 false
  positives**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,851 files /
  303,819,126 bytes**, SHA-256
  `30e2318659f9f693c4e8df738a19a1a7fceea07ae4c53a05a142391a0a8f77c1`.

## Released and verified live

Batch 697 was fast-forwarded to `main` as commit
[`f8dd93117716c64311b8a3b86fb3b0c65243628a`](https://github.com/therealjameswilson/before-oss/commit/f8dd93117716c64311b8a3b86fb3b0c65243628a).
The GitHub Pages build and deployment
[`37105635130`](https://github.com/therealjameswilson/before-oss/actions/runs/37105635130)
and independent test workflow
[`37105635102`](https://github.com/therealjameswilson/before-oss/actions/runs/37105635102)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 103,472,820 bytes matched, as did eight core
routes, all 29 source-register pages, and the 23 Batch 697 profile routes. The
live site reports 23,978 source rows, 23,939 person entities, 9,075 researched
people, 703 verified affiliations, 317 verified employers, and 14,859
not-started people.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-697-boundary --page 338 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-697 --page 339 --first-row 1 --last-row 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch697.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages338-339-neff-nellhaus-review_batch-697_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 339, row 23. No API key, raw API
response, full service number, copyrighted page image, unrelated Army coded
occupation, street address, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
