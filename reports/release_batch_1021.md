# Batch 1021 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 511, rows 1-46: Ernest H. Wohlleben through Joseph
  Wolverton. All 46 printed rows remain separately recoverable as 46 cautious
  person entities.
- Every cohort person has a saved terminal outcome: 42
  `requires_archival_review`, two `completed`, one `verified_employer_found`
  and one `documented_prewar_employer_found`.
- Charles Wolf Jr.'s Harvard relationship is published as student status, not
  employment. His immediate pre-OSS pathway is the U.S. Army and his profile
  does not claim a civilian employer.
- Milton Wolff's U.S. Army service immediately before OSS-linked intelligence
  work is published as a military assignment, not a civilian employer.
- Robert Lee Wolff's 1937-1942 Harvard teaching fellowship is strongly
  date-bounded as both his immediate affiliation and last civilian employer.
- Peter N. Wolkonsky's Army intelligence assignment is his immediate military
  pathway. Library of Congress Photoduplication Service remains a qualified,
  medium-confidence probable last civilian employer because exact employment
  and leave dates are unavailable.
- Roger K. Wolbarst is a high-confidence identity match based on the rare name,
  rank and India context. Dartmouth Class of 1943 is student status, not an
  employer, and the exact OSS transition still requires archival review.
- Dorothy E. Wolgamott, Anthony A. Wollner and Dmitri Wolkonsky leads were not
  transferred without person-specific identity bridges. Common Wolf, Wolfe
  and Wolff namesakes remain unresolved.
- Bounded CIA and Library of Congress adapter errors remain access failures,
  not negative results. No authenticated NARA Catalog API request was used.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,887/23,935 people (70.5536%).
- Verified affiliation: 1,192/23,935 people (4.9802%).
- Verified employer: 547/23,935 people (2.2854%).
- Archival disposition assessed: 15,368/23,935 people (64.2072%).
- Not started: 7,043 people; in progress: 1,879 people.
- Research outcomes include 1,918 `occupation_only_found`, 9,420
  `requires_archival_review`, 459 `verified_employer_found`, 294
  `documented_prewar_employer_found`, 604 `needs_identity_review` and 475
  `conflicting_sources` people.
- Claim confidence: 1,974 confirmed; 5,505 high; 2,875 medium; 261 low; 463
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,341 affiliations, 1,371 organizations,
  6,739 sources and 10,813 published, qualified or conflict claims.
- Citations: 8,032 across 4,497 unique source documents.

## Local publication verification

- Evidence-bundle SHA-256:
  `3aede4eb643436817f2c685933918686e8dce6ce8e07d82885d028ec2252bb72`.
- The evidence bundle validates without exposing secrets, full identifiers or
  raw bulk records.
- Python: all 163 tests and 87 subtests passed.
- SQLite foreign-key, integrity and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 138,749,397 bytes, SHA-256
  `1be826a94589bf0168153fc32d8fa351276e2ab721615f38891e15ac3babc28d`.
- Clean Astro check: 652 files with zero errors, warnings or hints.
- Clean static build: 25,359 pages.
- Bounded browser release suite: 96/96 checks passed across desktop, phone and
  tablet: 27 Batch 1021 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,359 HTML files checked; all links resolve. The checker
  inventoried 52,409 unique external URLs separately.
- Public-identifier audit: 25,431 public artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,601 candidate substrings and found zero aggregate, manifest-size or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,431 artifacts and 432,408,550
  bytes at output-tree SHA-256
  `f063249e95ef652f619a5119d34f51c11d8cbd22b9e518c7d3d4f3374742cb92`.
- The production dependency audit found zero vulnerabilities.

The initial Test run `41835493069` exposed a checkout-portability defect in a
new browser test: it referenced a private, generated local file that is absent
from a clean checkout. The test was changed to validate the public schema
without that local dependency, and the full 96-check release suite passed
again locally before the correction was pushed.

Content commit `7057dc1bd4847a43afe0b798d3ec0bf843649147` passed the full
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/41836202147)
and the
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/41836202185).
The unauthenticated deployed-release verifier matched all 67 canonical assets
and 138,749,397 bytes to the committed manifest at SHA-256
`1be826a94589bf0168153fc32d8fa351276e2ab721615f38891e15ac3babc28d`.
It also returned successful main content for all eight core routes, all 45
source-register pages and all 46 Batch 1021 direct profile URLs.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
