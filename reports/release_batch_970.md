# Batch 970 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 475, rows 24-46: Joseph E Turcotte through Mildred M
  Turner. Olive J Turner at page 476, row 1 is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: 9 occupation-only outcomes and 14 archival-review outcomes.
- Eleven Army identity bridges were accepted. Nine publish only qualified
  occupation or student categories; two provide identity evidence without a
  usable pre-OSS occupation.
- Campbell Turner's probable connection to Turner's Diplomatic School is
  qualified, excluded from default analytics and left for Box 789 confirmation.
- The Turlano/Iurlano spelling discrepancy remains visible. The Leonard
  Turkowski roster lead and an incompatible Marden Turner namesake were not
  admitted as final evidence.
- This batch establishes no new named employer and makes no authenticated NARA
  Catalog API request.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `1bc6bc13d3036e33da53da9cd3153122e998db3f3fafd776d390cf8bb3d64c29`.
- Durable import: 6 sources, 1 reused organization input, 10 affiliations, 22
  claims, 65 claim-source links, 23 person updates and 23 research attempts;
  repeated imports are idempotent.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 601 files checked with zero errors, warnings or hints; 25,237 static
  pages built.
- Batch browser matrix: 24/24 checks pass across desktop, phone and tablet.
- Browser release suite: 93/93 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,237 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,309 output artifacts; 1,418 candidate substrings and zero
  unexpected boundary, aggregate or manifest-size matches.
- Dependency audit: zero vulnerabilities.
- Public manifest: 67 assets, 129,858,075 bytes, SHA-256
  `06bb20ef155a3338304a9e904445f0367c36120a18a346d18c07af95b7a1be38`.
- Public tree: 70 files, 132,205,234 bytes, SHA-256
  `5877da6e7eee688813342d9d315a7febc18a41911bed8a324ee3a696bab37f6e`.
- Output tree: 25,309 files, 417,614,147 bytes, SHA-256
  `a50f1139835122bf0d31bd664e72d9eaffb340b60b3df364451e0521b017b013`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,246/23,936 people (63.6949%).
- Verified affiliation: 1,094/23,936 people (4.5705%).
- Verified employer: 488/23,936 people (2.0388%).
- Archival disposition assessed: 13,722/23,936 people (57.3279%).
- Not started: 8,685 people; in progress: 1,883 people.
- Claim confidence: 1,706 confirmed; 5,091 high; 2,414 medium; 255 low;
  434 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,744 affiliations, 1,251 organizations,
  6,245 sources and 9,641 claims.
- Evidence ledger: 7,531 citations across 4,180 unique source documents.

## Replay disclosure

- Batch 970 evidence and review decisions replay idempotently.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented in
  durable replay inputs. The current integrity-checked database remains
  authoritative for the public projection.

## Publication verification

- Immutable content commit:
  `3e0bb36b12da7a2e92921411c754bd2b0b849e3f`.
- GitHub Actions Test run `41009050588` and Pages run `41009050610` completed
  successfully.
- The unauthenticated deployed-release verifier matched the 67-asset,
  129,858,075-byte public manifest at SHA-256
  `06bb20ef155a3338304a9e904445f0367c36120a18a346d18c07af95b7a1be38`,
  all eight core routes, all 42 source-register pages and all 23 Batch 970
  profile routes to the content commit.
- Public site: <https://therealjameswilson.github.io/before-oss/>.
