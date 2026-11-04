# Batch 1022 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 512, rows 1-46: William H. Wolverton Jr. through William D.
  Wood. All 46 printed rows remain separately recoverable as 46 cautious
  person entities.
- Every cohort person has a saved terminal outcome: 35
  `requires_archival_review`, nine `occupation_only_found`, and two
  `conflicting_sources`.
- Nine protected-identifier Army candidates were accepted: six exact-name
  confirmations and three high-confidence spelling or transcription variants.
  Their broad historical occupation categories remain qualified and unnamed.
- Pak Hoy Wong and Richard H. Wood are modeled as students at Army entry, not
  employees of unnamed schools.
- Shen T. Wong and Shew T. Wong remain separate. The identifier/name conflict
  is visible on both profiles; neither receives the Army occupation pending
  joint review of Box 850.
- Incompatible Army candidates for Thomas F. Wombacher and Andrew M. Wood were
  rejected. Famous, common-name, relative, genealogy, and postwar-only leads
  were not transferred without person-specific OSS identity evidence.
- No authenticated NARA Catalog API request was used.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,933/23,935 people (70.7458%).
- Verified affiliation: 1,192/23,935 people (4.9802%).
- Verified employer: 547/23,935 people (2.2854%).
- Archival disposition assessed: 15,414/23,935 people (64.3994%).
- Not started: 6,997 people; in progress: 1,879 people.
- Research outcomes include 1,927 `occupation_only_found`, 9,455
  `requires_archival_review`, 459 `verified_employer_found`, 294
  `documented_prewar_employer_found`, 604 `needs_identity_review`, and 477
  `conflicting_sources` people.
- Claim confidence: 1,980 confirmed; 5,508 high; 2,884 medium; 261 low; 465
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,350 affiliations, 1,371 organizations,
  6,740 sources, and 10,833 published, qualified, or conflict claims.
- Citations: 8,033 across 4,497 unique source documents.

## Local publication verification

- Evidence-bundle SHA-256:
  `3c73d7a023fbf3e9d95c94b9fa9186ac75cbe14c7f1a9eb6a10ef81529fe793b`.
- The evidence bundle validates without exposing secrets, full identifiers, or
  raw bulk records.
- Python: all 167 tests and 87 subtests passed.
- SQLite foreign-key, integrity, and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 138,893,882 bytes, SHA-256
  `429c76320fb70fdba1dbd5b44f00842db011e78e6818c485a83105796650cab8`.
- Clean Astro check: 653 files with zero errors, warnings, or hints.
- Clean static build: 25,359 pages.
- Bounded browser release suite: 81/81 checks passed across desktop, phone, and
  tablet: 12 Batch 1022 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,359 HTML files checked; all links resolve. The checker
  inventoried 52,409 unique external URLs separately.
- Public-identifier audit: 25,431 public artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,602 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,431 artifacts and 432,654,126
  bytes at output-tree SHA-256
  `baa3f856395d56384946199ebe3aa627256d1ccfc383e02185ed6ef42a9d251b`.
- The production dependency audit found zero vulnerabilities.

GitHub workflow and live deployment verification will be appended after the
content commit is published.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
