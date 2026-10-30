# Batch 963 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 472, rows 3-25: Harry Trainosky through William W Treat.
  Oliver E Trechter at page 472 row 26 is the next cohort boundary.
- All 23 researched source rows remain separate people and every person in the
  cohort has a saved terminal research outcome.
- Six exact Army identity bridges publish only qualified dated occupation or
  student categories. No employer, workplace or school is inferred from those
  codes.
- Owen E Treanor has a direct wartime OSS identity and commissioned Army
  classification without an invented pre-OSS affiliation.
- Lillian Trangott and Lillian Traugott remain separate ambiguous profiles.
  Plausible but unbridged Travaglini, Treacy and Treat namesakes remain
  rejected as final evidence.
- No authenticated NARA Catalog API request was used. The evidence-defined
  oil-company category remains unchanged at 14 people linked to 15 historically
  named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `d3484ae396f22e2e365b6a9e3c88aa428299dfab614c5dcd6e5aa78648baa4c5`.
- The durable import records 6 review decisions, 6 affiliations, 13 claims, 23
  person updates, 23 research attempts, 5 sources and 32 claim-source links;
  repeated imports are idempotent. SQLite integrity is ok and foreign-key
  violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 594 files checked with zero errors, warnings or hints; 25,224 static
  pages built.
- Batch browser suite: 24/24 checks pass on desktop, phone and tablet.
- Browser release suite: 93/93 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,224 HTML files checked; all links resolve. The checker
  separately inventories 51,992 unique external URLs for bounded live checks.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,296 public artifacts; 1,423 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 128,709,867 bytes, SHA-256
  `8a3f74416c4714df4ffe4b06bc601f0b652c603c0bc931a6a86e3b96c51cda57`.
- Public tree: 70 files, 131,057,032 bytes, SHA-256
  `3c06aa9b3739705830ed9d869e8f974f5d89217f1c319aba233f44a0a3b38ed3`.
- Two consecutive output trees: 25,296 files and 415,721,904 bytes each, with
  identical SHA-256
  `675cf645ebf62a0e1610b81a1719aeca946f86fd2bb75eee9a81f08f034fd22d`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,087/23,936 people (63.0306%).
- Verified affiliation: 1,084/23,936 people (4.5287%).
- Verified employer: 486/23,936 people (2.0304%).
- Archival disposition assessed: 13,563/23,936 people (56.6636%).
- Not started: 8,844 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,305.
- Possible-duplicate groups: 663; conflicts: 517.
- Claim confidence: 1,692 confirmed; 5,015 high; 2,328 medium; 254 low;
  431 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,655 affiliations, 1,238 organizations,
  6,164 sources and 9,462 claims.
- Evidence ledger: 7,448 citations across 4,128 unique source documents.

## Replay disclosure

- Batch 963 evidence and review decisions replay idempotently in a disposable
  database.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented
  in durable replay inputs. The integrity-checked current research database
  remains authoritative for the public projection.
- This release does not claim that the older global replay gap has been
  repaired.

## Publication verification

- Immutable content commit:
  [`d8f015e28dec84b188ed0bded2d8e12b48625dcf`](https://github.com/therealjameswilson/before-oss/commit/d8f015e28dec84b188ed0bded2d8e12b48625dcf).
- GitHub Test run
  [40988140782](https://github.com/therealjameswilson/before-oss/actions/runs/40988140782)
  passed, including the Python tests, checked-in public-manifest check, bounded
  browser release suite and public-identifier redaction audit.
- GitHub Pages run
  [40988140774](https://github.com/therealjameswilson/before-oss/actions/runs/40988140774)
  passed and deployed the immutable content commit.
- The unauthenticated deployed-release verifier compared 67 public assets
  totaling 128,709,867 bytes to that commit's manifest; the deployed manifest
  SHA-256 was
  `8a3f74416c4714df4ffe4b06bc601f0b652c603c0bc931a6a86e3b96c51cda57`.
- Eight core routes, 42 source-register pages and all 23 direct Batch 963
  profile routes returned successfully from
  <https://therealjameswilson.github.io/before-oss/>.
- GitHub emitted advisory runner notices about the Node.js 20 action-runtime
  transition and the `ubuntu-latest` migration; neither caused a test or
  deployment failure.
