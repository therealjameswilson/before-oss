# Batch 961 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 471, rows 3-25: Fulton B Torry through Campbell Townsend.
  James B Townsend at page 471 row 26 is the next cohort boundary.
- All 23 researched source rows remain separate people and every person in the
  cohort has a saved terminal research outcome.
- John E Toulmin has a documented 1939 First National Bank of Boston employer,
  qualified as his last documented civilian employer rather than an explicit
  recruited-from affiliation. Ivan Tors and Bernardo Hugh Tovar retain
  distinct student, occupational and military pathways.
- Direct OSS records confirm Samuel J Toscano, Alvin Toso and Bernard A
  Towell without inventing earlier employers. Six unresolved people retain
  Box 782-783 archival-review outcomes.
- Elsie S Townlsey keeps the index spelling; Henri S Tosy remains probable;
  two undefined Army occupation codes remain uninterpreted. No authenticated
  NARA Catalog API request was used.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `ea1cacfbfc1b6fb0932c205906a34d191891e64f03adf8272144e0e5cd72079f`.
- The durable import records 10 review decisions, 14 affiliations, 30 claims,
  23 person updates, 23 research attempts, 15 sources, 5 organizations and 67
  claim-source links; repeated imports are idempotent. SQLite integrity is ok
  and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 592 files checked with zero errors, warnings or hints; 25,221 static
  pages built.
- Batch browser suite: 30/30 checks pass on desktop, phone and tablet.
- Browser release suite: 99/99 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,221 HTML files checked; all links resolve. The checker
  separately inventories 51,986 unique external URLs for bounded live checks.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,293 public artifacts; 1,420 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 128,530,706 bytes, SHA-256
  `e2fe2c969911243c740b8dbee2439ca3423e05548a5577123660d888b78a80c5`.
- Public tree: 70 files, 130,877,865 bytes, SHA-256
  `36264cb3c1b93d518c47e7266e11539097eb3eeae74c7dc646006855395b268b`.
- Two consecutive output trees: 25,293 files and 415,420,907 bytes each, with
  identical SHA-256
  `aaf035fe01fc11e10ccc8b9ff4ad6687fb3fb6c56013ab208077cb501b853e9a`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,041/23,936 people (62.8384%).
- Verified affiliation: 1,081/23,936 people (4.5162%).
- Verified employer: 485/23,936 people (2.0262%).
- Archival disposition assessed: 13,517/23,936 people (56.4714%).
- Not started: 8,890 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,259.
- Possible-duplicate groups: 660; conflicts: 516.
- Claim confidence: 1,690 confirmed; 5,001 high; 2,320 medium; 254 low;
  430 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,644 affiliations, 1,236 organizations,
  6,147 sources and 9,437 claims.
- Evidence ledger: 7,431 citations across 4,120 unique source documents.

## Replay disclosure

- Batch 961 evidence and review decisions replay idempotently in a clean
  disposable database.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented
  in durable replay inputs. The integrity-checked current research database
  remains authoritative for the public projection.
- This release does not claim that the older global replay gap has been
  repaired.

## Publication verification

Publication identifiers and the unauthenticated deployed-release audit will
be added after the immutable content commit is deployed.
