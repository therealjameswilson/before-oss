# Batch 1020 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 510, rows 1-46: Hedwig Wirowski through Chester G. Wohlert.
  All 46 printed rows remain separately recoverable as 46 cautious person
  entities.
- Every cohort person has a saved terminal outcome: 33
  `requires_archival_review`, nine `occupation_only_found`, three
  `verified_employer_found` and one `completed`.
- Identity disposition is 11 confirmed, five high-confidence and 30 unresolved
  cohort people.
- Twelve protected-identifier Army candidates received explicit acceptance
  review. Nine support qualified historical occupation categories only. Two
  official codes are undefined in the inspected code table, and one Army
  entry postdates OSS dissolution; those three identities receive no
  occupation claim. No accepted record is converted into a named employer,
  workplace or exact OSS-transfer date.
- Direct May 1944 OSS evidence confirms Peter S. Wludyka's Army-to-OSS Cairo
  recruitment pathway. The Army is a military assignment, not a civilian
  employer, and the absent recruitment date remains absent.
- Scholarly and official military sources support a high-confidence James R.
  Withrow Jr. identity and explicit recruitment from William J. Donovan's New
  York law firm. The law firm is both his immediate affiliation and last
  documented civilian employer; the reviewed source does not supply an exact
  departure date, so none is published.
- Official and institutional archival sources support Otto Wittman Jr.'s Air
  Transport Command pathway, last civilian employment at Portland Art Museum,
  and earlier Hyde Collection, Skidmore College and Rockhill Nelson Gallery
  work as distinct affiliations.
- Frank G. Wisner's existing verified claims remain unchanged.
- The indexed Ernest J. Wisynski and Ernest J. Wixynski rows remain distinct
  and visibly grouped for comparison of Boxes 847 and 849.
- The famous academic Carl F. Wittke candidate was rejected without a bridge
  to this OSS index row; no academic career was transferred.
- Bounded CIA and Library of Congress adapter checks failed closed with
  separately recorded access errors. The failures are not treated as negative
  results. No authenticated NARA Catalog API request was used.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,842/23,935 people (70.3656%).
- Verified affiliation: 1,187/23,935 people (4.9593%).
- Verified employer: 546/23,935 people (2.2812%).
- Archival disposition assessed: 15,323/23,935 people (64.0192%).
- Not started: 7,088 people; in progress: 1,879 people.
- Research outcomes include 1,918 `occupation_only_found`, 9,379
  `requires_archival_review`, 458 `verified_employer_found`, 293
  `documented_prewar_employer_found`, 604 `needs_identity_review` and 475
  `conflicting_sources` people.
- Claim confidence: 1,972 confirmed; 5,496 high; 2,875 medium; 261 low; 463
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,335 affiliations, 1,371 organizations,
  6,732 sources and 10,802 published, qualified or conflict claims.
- Citations: 8,024 across 4,490 unique source documents.

## Local publication verification

- Evidence-bundle SHA-256:
  `dd98edfa38d206ba4944926c89c372c5305c130e6cf39b44c636464c9837c35a`.
- Army review-decision SHA-256:
  `7b548b6d9c88f38b6a521490ff18b4c10a64d14c0bbf6a394581ba48ffaed82a`.
- Evidence-bundle and Army decision files validate without exposing secrets,
  full identifiers or raw bulk records.
- Python: all 158 tests and 87 subtests passed.
- SQLite foreign-key, integrity and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 138,624,105 bytes, SHA-256
  `84be7651e38782d3290fa451f2876aaeeec0772cff3fc9b8aa3b6702dcffd92f`.
- Clean Astro check: 651 files with zero errors, warnings or hints.
- Clean static build: 25,359 pages.
- Bounded browser release suite: 93/93 checks passed across desktop, phone and
  tablet: 24 Batch 1020 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,359 HTML files checked; all links resolve. The checker
  inventoried 52,403 unique external URLs separately.
- Public-identifier audit: 25,424 public artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,586 candidate substrings and found zero aggregate, manifest-size or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,431 artifacts and 432,212,402
  bytes at output-tree SHA-256
  `6815750af1230a2ae46dcd0077f5a6a8809280ebb2a6daaea2ccbda4f41d2ccd`.
- The production dependency audit found zero vulnerabilities.

CI, GitHub Pages deployment and unauthenticated live verification remain
pending. The currently public site remains the earlier verified release until
those gates pass.

Public site URL: <https://therealjameswilson.github.io/before-oss/>.
