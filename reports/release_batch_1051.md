# Batch 1051 release audit

Research and release date: 2026-11-11 America/New_York.

## Release contents

- NARA index page 306, rows 1-46: Howard P. McCormick through William C.
  McCutcheon. All 46 printed rows remain separately recoverable as 46 cautious
  person entities, and every entity has a saved terminal research outcome.
- The cohort contains 39 `requires_archival_review`, five
  `occupation_only_found`, one `verified_employer_found`, and one
  `conflicting_sources` outcome.
- Five accepted, nonshared, wartime-dated Army identity links support broad
  occupation or student categories only: general industry clerk, semiskilled
  structural or ornamental metal worker, student, semiskilled welder or flame
  cutter, and machinist. They identify no named employer, institution, or
  workplace and do not establish an Army-to-OSS sequence.
- Frank Ross McCoy's 1939-1945 Foreign Policy Association presidency is
  published as a temporally qualified professional affiliation, not silently
  converted into employment or an immediate predecessor.
- Thomas Frederick McCoy's Army-to-OSS pathway is modeled as an immediate
  military assignment; no civilian employer is inferred.
- The two Joseph F. McCrindle rows remain separate. The lieutenant is
  confirmed as Joseph Feder McCrindle through specific OSS and rank evidence,
  with Harvard recorded only as a student relationship. The corporal row has
  a distinct private identifier and receives only the official Army student
  category.
- The University of California memorial explicitly supports George McAfee
  McCune's Occidental College history-staff employment and 1942 leave for OSS.
  Occidental is therefore both his immediate pre-OSS affiliation and last
  civilian employer.
- Similar-name, misspelled, shared-identifier, and conflicting-identifier
  cases remain separate and visibly reviewable. No private identifier, raw
  Army record, authenticated NARA API payload, or full copyrighted source
  entered public data. No authenticated NARA Catalog API request was made.

## Evidence and import

- Reviewed evidence bundle: nine sources, five organizations, ten
  affiliations, 21 claims, 47 claim-source links, 46 person updates, and 46
  research attempts.
- Evidence and person-state imports were tested twice against a disposable
  database and remained idempotent on re-import.
- Evidence-bundle SHA-256:
  `fc9e551e8e258167d969a37ee32077f5161a32f32d4b4f82a88fec8ee86688e1`.
- The transient pre-import backup had SHA-256
  `b78c3ed574e0b2082f0d9d0c5e3a28a89d1b378f28677a1a485b7e2587c77ac3`.
  Immediately after import, the durable database had SHA-256
  `4828792064b01569924c62d0f8c54d78afc38f65ddf2ab36dddeb8e10731d91d`;
  after subsequent audited export and profile-audit pipeline runs, the current
  release database has SHA-256
  `dbb4baad82087d7ff69103c84c8a97b7232e6f9e9bf077f5fa9c656e315a5913`.
- SQLite integrity is `ok`, foreign-key violations are zero, all 46 page-306
  people have terminal outcomes, and uncited public claims are zero.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,922/23,935 people (74.8778%).
- Verified affiliation: 1,253/23,935 people (5.2350%).
- Verified employer: 573/23,935 people (2.3940%).
- Archival disposition assessed: 16,646/23,935 people (69.5467%).
- Not started: 6,013 people; in progress: 1,608 people.
- Research outcomes include 2,289 `occupation_only_found`, 10,221
  `requires_archival_review`, 485 `verified_employer_found`, 308
  `documented_prewar_employer_found`, 645 `needs_identity_review`, 53
  `needs_temporal_review`, and 497 `conflicting_sources` people.
- Claim confidence: 2,050 confirmed; 5,677 high; 3,298 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,842 affiliations, 1,432 organizations,
  7,025 sources, and 11,501 published, qualified, or conflict claims.
- Citations: 8,320 across 4,686 unique source documents.
- Possible duplicate groups: 710. Total conflict flags: 580.
- Private derived exports contain 4,869 affiliations, 1,446 organizations,
  32,861 research attempts, 20,522 unresolved rows, 23,492 NARA pull-list
  rows, and 7,364 Army review-queue rows.

## Local publication verification

- Targeted Batch 1051 and evidence tests: 23/23 passed. Independent unittest
  discovery passed all 154 tests.
- SQLite integrity is `ok`, foreign-key violations are zero, and uncited
  published, publish-qualified, or conflict claims are zero.
- Astro application check: 24 files with zero errors, warnings, or hints;
  strict TypeScript validation also covered the Playwright configuration and
  all test files.
- Static build: 25,422 pages. The resilient public-asset copy verified 70
  files totaling 146,862,112 bytes.
- Bounded browser release suite: 87/87 checks passed across desktop, phone,
  and tablet: 18 Batch 1051 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious or critical axe
  violations.
- Internal links: 25,422 HTML files checked; all links resolve. The checker
  inventoried 52,604 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 144,514,952 bytes,
  SHA-256
  `13898293adc1480ec5cf883550685d8b96fc7eb2db71ecdfbe6575703cf481e0`.
- Public-identifier audit: 25,494 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,583 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,494 artifacts totaling
  441,993,090 bytes at output-tree SHA-256
  `a0f07bcbd90e4becd76983df1827b82747b2a2c950faa483090ce9bf137473aa`.
- The deterministic 200-profile stratified audit passed all defined gates.
- The production dependency audit found zero vulnerabilities.

## Deployment status

Publication, GitHub Actions, Pages deployment, and unauthenticated live
verification are pending. This section must be updated with immutable commit
and workflow identifiers before the release is called deployed.

Public base URL: <https://therealjameswilson.github.io/before-oss/>.

Full-index historical research remains unfinished.
