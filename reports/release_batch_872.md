# Batch 872 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 426, rows 1-23: 23 separately preserved source rows,
  from Myron Shpur through Marshall J Shumate, linked to 23 active people.
- 23 terminal research outcomes: two `verified_employer_found`, one
  `documented_prewar_employer_found`, one `needs_identity_review` and 19
  `requires_archival_review`.
- Two confirmed, five high-confidence, one ambiguous and 15 unresolved
  identities.
- Seven sources, three organizations, three affiliations, 11 claims, 23 person
  updates, 23 research attempts and 25 claim-source links.
- Confirmed last civilian pre-service employment for Myron Shpur at the United
  States War Department, with intervening Army service kept distinct from the
  immediate-pre-OSS question.
- Confirmed self-employment for artist Frederick C Shrady before June 1943 Army
  enlistment and a later brief OSS assignment, without inventing an employer.
- A high-confidence Shuling-Suhling identity bridge based on official Army
  history, and a visibly qualified medium-confidence documented-prewar company
  presidency rather than an immediate-pre-OSS claim.
- Explicit possible-duplicate treatment for the Kenneth D Shuckers and Kenneth
  D Schuckers jackets without merging their entities or transferring employer
  evidence.

## Data gates

- SQLite integrity check: `ok`; foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts.
- Evidence-bundle validation: seven sources, three organizations, three
  affiliations, 11 claims, 23 person updates, 23 attempts and 25 embedded
  claim-source links.
- Public projection: 23,978 source rows, 23,937 active people, 2,894
  affiliations, 1,088 organizations, 5,359 sources and 7,864 published or
  qualified claims.
- Research-attempt coverage: 13,021/23,937 people (54.3970%).
- Verified-employer coverage: 431/23,937 people (1.8006%).
- Verified-affiliation coverage: 948/23,937 people (3.9604%).
- Archival-review coverage: 11,488/23,937 people (47.9926%).
- Remaining `not_started`: 10,911 people; remaining `in_progress`: 1,893.
- Possible duplicate groups: 581; conflicts: 450 people.
- Claim confidence totals: 1,619 confirmed, 4,146 high, 1,726 medium, 206
  low, 377 conflicting and two unresolved.
- Citations: 6,594; unique source documents: 3,569.
- Public redaction checks: passed during public-data generation and in the
  post-build identifier audit.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 506 files checked with zero errors, warnings or hints; 25,069 pages
  built.
- Bounded Playwright release suite: 90/90 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,069 HTML files, zero broken internal links; 51,463
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,141 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 117,201,448 bytes, SHA-256
  `71d95da3e8641020da9792e5fe6fe011cfc4fe18eec524e00f8b662cdcdc56e4`.
- Deterministic production build: two 25,141-file builds matched at SHA-256
  `a7bbd321e9e6c294b505e75b5692ecdd4efabffa17fabe2b9bb232d3030237db`.

## Publication state

Batch 872 is published at
<https://therealjameswilson.github.io/before-oss/> from immutable content
commit `758852752651ad9b9aec8c08d2d31b3f22ba2604`. GitHub Actions test run
`39059916300` completed successfully in 4 minutes 12 seconds, and Pages
deployment run `39059916318` completed successfully. The immutable live
verifier checked 67 assets totaling 117,201,448 bytes, manifest SHA-256
`71d95da3e8641020da9792e5fe6fe011cfc4fe18eec524e00f8b662cdcdc56e4`,
eight core routes, 36 source-register pages and all 23 direct profiles in the
Batch 872 evidence bundle.

The GitHub Actions annotations were non-failing platform notices: GitHub is
forcing selected actions from Node.js 20 to Node.js 24, and `ubuntu-latest` is
scheduled to migrate to Ubuntu 26. Neither annotation affected this release.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the previously
exposed key is rotated and supplied through a local environment or repository
secret. No credential was used, logged or committed in this release.
