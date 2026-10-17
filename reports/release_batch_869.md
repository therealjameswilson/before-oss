# Batch 869 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 424, rows 24-46: 23 separately preserved source rows,
  from John Sherry through William L Shimko, linked to 23 active people.
- 23 terminal research outcomes: two `verified_employer_found`, one
  `documented_prewar_employer_found` and 20 `requires_archival_review`.
- One confirmed, 11 high-confidence, one probable and ten unresolved
  identities.
- Seven new sources, four organizations, four affiliations, 16 claims, 22
  person updates, 22 manual research attempts and 34 claim-source links.
- Last civilian employment with the Japanese American Evacuation and
  Resettlement Study documented for Tamotsu Shibutani, with student status kept
  separate; Frederick N. Shilzony's two 1942 affiliations remain classified as
  documented prewar rather than immediate.
- Haldor G. Shields confirmed through direct official OSS evidence while his
  employer remains unresolved and assigned to archival review.
- Ten protected-identifier Army candidates accepted for identity only; no
  coded Army field was converted into an employer or OSS rank.
- Edward A. Shils's prior reviewed outcome preserved without duplication.

## Data gates

- SQLite integrity check: `ok`; foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts, totaling 25 attempts across the preserved and new work.
- Evidence-bundle validation: seven sources, four organizations, four
  affiliations, 16 claims, 22 person updates, 22 attempts and 34 embedded
  claim-source links.
- Public projection: 23,978 source rows, 23,937 people, 2,882 affiliations,
  1,082 organizations, 5,334 sources and 7,825 published or qualified claims.
- Research-attempt coverage: 12,952/23,937 people (54.1087%).
- Verified-employer coverage: 428/23,937 people (1.7880%).
- Verified-affiliation coverage: 940/23,937 people (3.9270%).
- Archival-review coverage: 11,419/23,937 people (47.7044%).
- Remaining `not_started`: 10,980 people.
- Public redaction checks: passed during public-data generation.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 503 files checked with zero errors, warnings or hints; 25,063 pages
  built.
- Bounded Playwright release suite: 90/90 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,063 HTML files, zero broken internal links; 51,445
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,135 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,942,304 bytes, SHA-256
  `87e9ff47717ac829c484f81b355b7e76f067af7eaaff5bd03e996e919e4b5a62`.
- Deterministic production build: two 25,135-file builds matched at SHA-256
  `2ef16a14068b7183c0b12097b995a38c3a597b2396efa2e84e5ad726e73a222f`.

## Publication state

Batch 869 has passed every local gate and is ready for publication. GitHub
Actions run identifiers and immutable live verification will be recorded here
after deployment.
