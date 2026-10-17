# Batch 875 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 427, rows 24-46: 23 separately preserved source rows,
  from Stanley V Sienkiewicz through Gerard I Sillman, linked to 23 active
  people.
- 23 terminal research outcomes: one `conflicting_sources` and 22
  `requires_archival_review`.
- Six high-confidence, one confirmed, one probable, one conflicting, one
  ambiguous and 13 unresolved identities.
- Seven sources, one reused organization, one affiliation, 11 claims, 24
  person updates and 23 research attempts.
- A documented prewar Vassar College student relationship for Sarah J
  Sillcocks, explicitly separated from employment and from the still-unresolved
  immediate pre-OSS question.
- Two qualified French official finding-aid references for probable Roger
  Siffredi, without inventing a pre-OSS employer, unit or service sequence.
- An explicit Joseph V Sika Army-record name conflict, preserving uncertainty
  despite agreement in a protected identifier.
- An explicit ambiguous profile for the visually verified `Signal | Section`
  source row instead of silently deleting it or inventing a person.
- Separate Sidianoff and Silianoff profiles connected only through a
  possible-duplicate group pending physical-jacket comparison.

## Data gates

- SQLite integrity check: `ok`; foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts.
- Repeat evidence and Army-decision imports: idempotent.
- Evidence-bundle validation: seven sources, one organization, one
  affiliation, 11 claims, 24 person updates and 23 attempts.
- Public projection: 23,978 source rows, 23,937 active people, 2,897
  affiliations, 1,089 organizations, 5,376 sources and 7,899 published or
  qualified claims.
- Research-attempt coverage: 13,088/23,937 people (54.6769%).
- Verified-employer coverage: 431/23,937 people (1.8006%).
- Verified-affiliation coverage: 949/23,937 people (3.9646%).
- Archival-review coverage: 11,555/23,937 people (48.2725%).
- Remaining `not_started`: 10,844 people; remaining `in_progress`: 1,893.
- Possible duplicate groups: 583; conflicts: 454 people.
- Claim confidence totals: 1,621 confirmed, 4,167 high, 1,733 medium, 206
  low, 382 conflicting and two unresolved.
- Citations: 6,613; unique source documents: 3,584.
- Public redaction checks: passed during public-data generation.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 509 files checked with zero errors, warnings or hints; 25,070 pages
  built.
- Bounded Playwright release suite: 90/90 passed across Batch 875, core routes,
  the oil-company category, analytics and accessibility at desktop, phone and
  tablet viewports.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,070 HTML files, zero broken internal links; 51,471
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,142 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 117,391,651 bytes, SHA-256
  `e37b3b8b6f9ee95382e9cabd35071a7cd8d5c9b00c6df35fb29240c8c146f39a`.
- Deterministic production build: two 25,142-file builds matched at SHA-256
  `23f182bcd8bec12bf8a26366df8fa54cacb00d2035b6966f08011d1a18360801`.

## Publication state

Batch 875 has passed every local release gate. Publication remains pending
until the content commit is pushed to `main`, the GitHub Actions test and Pages
deployment runs succeed, and the unauthenticated immutable live verifier
matches the committed manifest and all 23 direct profiles.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the previously
exposed key is rotated and supplied through a local environment or repository
secret. No credential was used, logged or committed in this batch.
