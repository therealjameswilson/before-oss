# Batch 972 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 476, rows 24-46: George B Tweed through John Tyson. Robert M
  Tyson at page 477, row 1 is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: one verified employer, four occupation-only outcomes, one
  conflicting-source outcome and 17 archival-review outcomes.
- Institutional rosters support Otto Twingley's immediate 99th Infantry
  military pathway and a qualified, temporally uncertain 86th Infantry
  assignment for probable John B Tweedy.
- Princeton and Miami obituaries support Hutchinson, Rivinus & Co. as John
  Tyson's immediate and last civilian employer and the Pennsylvania Railroad
  as an earlier employer; an Army institutional history independently
  corroborates his OSS identity.
- Four exact Army identity bridges publish only qualified occupation or student
  categories. Marvin E Tyree's two post-OSS rows support identity only. John E
  Tyczkowski's name conflict remains visible and receives no occupation.
- Fourteen unresolved identities retain archival-review routes.
- No authenticated NARA Catalog API request was used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `b79cbe1cee478051ee9f0477673442107725cb81121411927f9deeea04d932aa`.
- Durable import: 10 sources, 4 organization inputs, 8 affiliations, 19 claims,
  50 claim-source links, 23 person updates and 23 research attempts; repeated
  imports are idempotent.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests and 84 subtests pass.
- Astro: 603 files checked with zero errors, warnings or hints; 25,241 static
  pages built.
- Batch browser matrix: 30/30 checks pass across desktop, phone and tablet.
- Browser release suite: 99/99 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,241 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,313 output artifacts; 1,420 candidate substrings and zero
  unexpected boundary, aggregate or manifest-size matches.
- Dependency audit: zero vulnerabilities.
- Public manifest: 67 assets, 130,131,796 bytes, SHA-256
  `04bc0c5532115971d745853a0682a9a73077b799828b89e00505b53d9997b21c`.
- Public tree: 70 files, 132,478,960 bytes, SHA-256
  `e7e2bd1ab4b4bb9ccc9cf9a01e87e07dd6910f6aef97d41bef8b07feb54ef5c4`.
- Output tree: 25,313 files, 418,070,510 bytes, SHA-256
  `547b74b4f4be989c1e92936026e3d87e176cc9d181354e29dea0e155288c03c5`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,292/23,936 people (63.8870%).
- Verified affiliation: 1,097/23,936 people (4.5831%).
- Verified employer: 490/23,936 people (2.0471%).
- Archival disposition assessed: 13,768/23,936 people (57.5201%).
- Not started: 8,639 people; in progress: 1,883 people.
- Claim confidence: 1,706 confirmed; 5,114 high; 2,426 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,759 affiliations, 1,255 organizations,
  6,263 sources and 9,678 claims.
- Evidence ledger: 7,549 citations across 4,189 unique source documents.

## Replay disclosure

- Batch 972 evidence and review decisions replay idempotently.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented in
  durable replay inputs. The current integrity-checked database remains
  authoritative for the public projection.

## Publication verification

Published from immutable content commit
`5b9c9ccb50bdb78ad8fd2eda324d07e0909ba976`. GitHub Actions Test run
`41017086287` and Pages run `41017086290` succeeded. The unauthenticated
deployed-release verifier matched:

- 67 public assets totaling 130,131,796 bytes;
- manifest SHA-256
  `04bc0c5532115971d745853a0682a9a73077b799828b89e00505b53d9997b21c`;
- eight core routes;
- 42 source-register pages; and
- all 23 Batch 972 direct profile routes.

Verified public URL: <https://therealjameswilson.github.io/before-oss/>.
