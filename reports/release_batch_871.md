# Batch 871 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 425, rows 24-46: 23 separately preserved source rows,
  from David L Shoemaker through Evelyn N Showers, linked to 23 active people.
- 23 terminal research outcomes: two `verified_employer_found`, one
  `documented_prewar_employer_found`, one `occupation_only_found`, two
  `needs_identity_review` and 17 `requires_archival_review`.
- Two confirmed, eight high-confidence, one ambiguous and 12 unresolved
  identities.
- Ten sources, five organizations, five affiliations, 15 claims, 24 person
  updates, 23 research attempts and 30 claim-source links.
- Direct wartime OSS Personnel Board evidence for Herbert B Sholar row 27,
  while the adjacent same-name row 28 remains separate and unresolved because
  its protected identifier differs.
- Confirmed OSS reference linkage and qualified prewar employment chronology
  for Max Shoop; the intervening Red Cross relationship prevents an
  immediate-pre-OSS label.
- Qualified documented-prewar RCA employment for Henry Shore, student-status
  evidence for Susan King Sholar and Edwin L Sholine, and seven accepted Army
  identity candidates that do not import Army-coded occupations as employers.
- Explicit possible-duplicate treatment for Frank Shoonmaker and the earlier
  Frank Schoonmaker without crossing biography or employer evidence between
  the two records.

## Data gates

- SQLite integrity check: `ok`; foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts.
- Evidence-bundle validation: ten sources, five organizations, five
  affiliations, 15 claims, 24 person updates, 23 attempts and 30 embedded
  claim-source links.
- Public projection: 23,978 source rows, 23,937 active people, 2,891
  affiliations, 1,087 organizations, 5,352 sources and 7,853 published or
  qualified claims.
- Research-attempt coverage: 12,998/23,937 people (54.3009%).
- Verified-employer coverage: 430/23,937 people (1.7964%).
- Verified-affiliation coverage: 946/23,937 people (3.9520%).
- Archival-review coverage: 11,465/23,937 people (47.8966%).
- Remaining `not_started`: 10,934 people.
- Possible duplicate groups: 581; conflicts: 450 people.
- Claim confidence totals: 1,617 confirmed, 4,139 high, 1,725 medium, 206
  low, 376 conflicting and two unresolved.
- Citations: 6,587; unique source documents: 3,563.
- Public redaction checks: passed during public-data generation and in the
  post-build identifier audit.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 505 files checked with zero errors, warnings or hints; 25,068 pages
  built.
- Bounded Playwright release suite: 93/93 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,068 HTML files, zero broken internal links; 51,458
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,140 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 117,120,430 bytes, SHA-256
  `e99bda3c40e3519512654a3d0b3a0818e003f50b493e5a1c6df56581a8dad65a`.
- Deterministic production build: two 25,140-file builds matched at SHA-256
  `3a7f0440e69916ffc7c3ced4f90c643a6d6117e4dd4c909ad7f282075c9e30ff`.

## Publication state

Batch 871 is published at
<https://therealjameswilson.github.io/before-oss/> from immutable content
commit `e2573dc89cde1e8ff1c96ef74eeda1731e6f68c4`. GitHub Actions test run
`39057639843` completed successfully in 5 minutes 5 seconds, and Pages
deployment run `39057639912` completed successfully. The immutable live
verifier checked 67 assets totaling 117,120,430 bytes, manifest SHA-256
`e99bda3c40e3519512654a3d0b3a0818e003f50b493e5a1c6df56581a8dad65a`,
eight core routes, 36 source-register pages and 24 direct profiles represented
in the Batch 871 evidence bundle.

The GitHub Actions annotations were non-failing platform notices: GitHub is
forcing selected actions from Node.js 20 to Node.js 24, and `ubuntu-latest` is
scheduled to migrate to Ubuntu 26. Neither annotation affected this release.
