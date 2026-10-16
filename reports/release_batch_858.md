# Batch 858 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 419, rows 1-23: 23 separately preserved and reviewed
  source rows, from Albert B Seitz through Helen M Selvig.
- 23 saved terminal outcomes: one `completed`, one `conflicting_sources` and
  21 `requires_archival_review`.
- Eleven high-confidence, ten unresolved, one ambiguous and one conflicting
  identity.
- Eight sources, two reused organizations, two affiliations, 13 published
  claims, 23 person updates, 23 research attempts and 27 claim-source links.
- Marguerite Seitzer's qualified State Department-to-OSS chronology modeled as
  government assignment rather than civilian employment.
- Official OSS identity evidence for Joseph P. Seliquini and George C. Selvig,
  without inventing pre-OSS employers or predecessor units.
- Helen Selvig's University of Minnesota attendance modeled as student status,
  not employment.
- Eight official Army identity bridges; coded Army fields remain private and
  do not become employer claims.
- George/Conrad Selvig and Harvey Selee/Harvy Solee review issues remain
  separate and publicly visible through opaque labels.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero; all 23 people have non-planned research attempts.
- Evidence-bundle validation: eight sources, two organizations, two
  affiliations, 13 claims, 23 person updates, 23 attempts and 27 claim-source
  links.
- Public projection: 23,978 source rows, 23,937 people, 2,848 affiliations,
  1,062 organizations, 5,259 sources and 7,682 published claims.
- Research-attempt coverage: 12,703/23,937 people (53.0685%).
- Verified-employer coverage: 418/23,937 people (1.7463%).
- Verified-affiliation coverage: 921/23,937 people (3.8476%).
- Archival-review coverage: 11,170/23,937 people (46.6642%).
- Remaining `not_started`: 11,229 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests passed.
- Astro: 492 files checked with zero errors, warnings or hints; 25,043 pages
  built.
- Bounded Playwright release suite: 90/90 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,043 HTML files, zero broken internal links; 51,382
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,115 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,012,998 bytes, SHA-256
  `0d3f90dc101ef769f19745e1e9182cda3c5cd0edfa9b75365d97a22a2b031309`.
- Deterministic production build: two 25,115-file builds matched at SHA-256
  `179aaba5410208d7f179693e410a7773af01b3dfa06ad22987fc26ea19776a6c`.

## Publication state

Published from content commit
`4037fe2e4d211c17b0b738dbcd7f8cf093a9f8b4`. GitHub Pages run
`38953214685` and Test run `38953214654` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(116,012,998 bytes), eight core routes, 36 source-register pages and all 23
direct profile routes referenced by the evidence bundle at
`https://therealjameswilson.github.io/before-oss/`. The live manifest SHA-256
is `0d3f90dc101ef769f19745e1e9182cda3c5cd0edfa9b75365d97a22a2b031309`,
matching the reviewed release. Live statistics report generation time
`2026-10-16T20:05:00Z`, 12,703 research-attempted people, 418
verified-employer profiles, 921 verified-affiliation profiles and 11,170
people with archival-review assessment.
