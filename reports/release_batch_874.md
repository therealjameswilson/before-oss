# Batch 874 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 427, rows 1-23: 23 separately preserved source rows,
  from David K Sidbury through Casimir A Sienkiewicz, linked to 23 active
  people.
- 23 terminal research outcomes: two `conflicting_sources`, one
  `occupation_only_found` and 20 `requires_archival_review`.
- Seven high-confidence, two probable, one conflicting and 13 unresolved
  identities.
- Seven sources, one reused organization, one affiliation, 12 claims, 23
  person updates and 23 research attempts.
- A qualified prewar Columbia University student affiliation and earlier
  occupation evidence for Morris Siegel, without relabeling the university as
  an employer or inventing an employer for the occupations.
- Explicit Sideris-Sideropoulos conflict and possible-duplicate treatment,
  preserving the two profiles and preventing evidence transfer.
- Qualified Rosemary Sidley identity context without claiming that a FOIA
  request log disclosed a personnel file or established an employer.
- Hall Siddall and Casimir Sienkiewicz career leads retained for private review
  rather than published without an independent OSS-personnel identity bridge.
- Correction of Batch 873's reported next-row boundary: page 426 ends at row
  46; Batch 874 correctly resumes at page 427, row 1.

## Data gates

- SQLite integrity check: `ok`; foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts.
- Repeat evidence and Army-decision imports: idempotent.
- Evidence-bundle validation: seven sources, one organization, one
  affiliation, 12 claims, 23 person updates and 23 attempts.
- Public projection: 23,978 source rows, 23,937 active people, 2,896
  affiliations, 1,089 organizations, 5,369 sources and 7,888 published or
  qualified claims.
- Research-attempt coverage: 13,065/23,937 people (54.5808%).
- Verified-employer coverage: 431/23,937 people (1.8006%).
- Verified-affiliation coverage: 948/23,937 people (3.9604%).
- Archival-review coverage: 11,532/23,937 people (48.1765%).
- Remaining `not_started`: 10,867 people; remaining `in_progress`: 1,893.
- Possible duplicate groups: 582; conflicts: 453 people.
- Claim confidence totals: 1,620 confirmed, 4,159 high, 1,732 medium, 206
  low, 381 conflicting and two unresolved.
- Citations: 6,606; unique source documents: 3,578.
- Public redaction checks: passed during public-data generation.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 508 files checked with zero errors, warnings or hints; 25,070 pages
  built.
- Bounded Playwright release suite: 87/87 passed across Batch 874, core routes,
  the oil-company category, analytics and accessibility at desktop, phone and
  tablet viewports.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,070 HTML files, zero broken internal links; 51,468
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,142 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 117,323,615 bytes, SHA-256
  `ccc188058d34ce536c304e13f8bec12871df78323c9ee4fe3ca3e5a19e8b32ed`.
- Deterministic production build: two 25,142-file builds matched at SHA-256
  `bf49eb59f5b9102247ccf3d08d7c7c13c4d9bb25d3b59fe5e2ae8829540137e1`.
- GitHub Actions and live-site gates remain in progress.

## Publication state

Batch 874 is not yet published. The public site remains Batch 873 at
<https://therealjameswilson.github.io/before-oss/>. An immutable content commit,
successful GitHub Actions test and Pages deployment, and unauthenticated live
verification are required before this report can call the batch published.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the previously
exposed key is rotated and supplied through a local environment or repository
secret. No credential was used, logged or committed in this batch.
