# Batch 873 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 426, rows 24-46: 23 separately preserved source rows,
  from Leon E Shurman through James P Sicuranza, linked to 23 active people.
- 23 terminal research outcomes: one `verified_employer_found`, one
  `documented_prewar_employer_found`, five `needs_identity_review` and 16
  `requires_archival_review`.
- One confirmed, seven high-confidence, one probable, two ambiguous, one
  conflicting and 11 unresolved identities.
- Five new sources, one organization, one affiliation, 12 claims, 21 person
  updates, 21 research attempts and 24 embedded claim-source links.
- Confirmed Paul Siapicas identity from an official OSS Greek operational-group
  roster, without treating wartime service as pre-OSS employer evidence.
- A visibly qualified medium-confidence 1938 newspaper role for Doosik Shynn,
  kept separate from the unanswered immediate and last-civilian-employer
  questions.
- Explicit Emily-Emil Shwetzer and same-name Richard C Sickler conflicts,
  preserving competing evidence without forced identity assignments.
- Explicit possible-duplicate treatment for James P Sicuranza and the earlier
  James Securanza row without merging their entities or transferring evidence.

## Data gates

- SQLite integrity check: `ok`; foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts.
- Evidence-bundle validation: five sources, one organization, one affiliation,
  12 claims, 21 person updates, 21 attempts and 24 embedded claim-source links.
- Public projection: 23,978 source rows, 23,937 active people, 2,895
  affiliations, 1,089 organizations, 5,364 sources and 7,876 published or
  qualified claims.
- Research-attempt coverage: 13,042/23,937 people (54.4847%).
- Verified-employer coverage: 431/23,937 people (1.8006%).
- Verified-affiliation coverage: 948/23,937 people (3.9604%).
- Archival-review coverage: 11,509/23,937 people (48.0804%).
- Remaining `not_started`: 10,890 people; remaining `in_progress`: 1,893.
- Possible duplicate groups: 582; conflicts: 451 people.
- Claim confidence totals: 1,620 confirmed, 4,152 high, 1,728 medium, 206
  low, 380 conflicting and two unresolved.
- Citations: 6,599; unique source documents: 3,572.
- Public redaction checks: passed during public-data generation and in the
  post-build identifier audit.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 507 files checked with zero errors, warnings or hints; 25,070 pages
  built.
- Bounded Playwright release suite: 90/90 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,070 HTML files, zero broken internal links; 51,465
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,142 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 117,264,357 bytes, SHA-256
  `bf9dbf0228a62ce4c514d47d7d26c391566dacdcad70c1c663d1da988997accd`.
- Deterministic production build: two 25,142-file builds matched at SHA-256
  `af868a3ac4bd5853fa5ec36411b168d344495dbc34ce884ae1cf38a7b5687d46`.

## Publication state

Batch 873 has passed every local release gate and is ready to publish to the
existing site at <https://therealjameswilson.github.io/before-oss/>. The
immutable content commit, GitHub Actions test and Pages results, and
unauthenticated live verification will be added after deployment.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the previously
exposed key is rotated and supplied through a local environment or repository
secret. No credential was used, logged or committed in this release.
