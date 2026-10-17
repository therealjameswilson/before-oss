# Batch 861 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 420, rows 24-46: 23 separately preserved and reviewed
  source rows, from Francis D Severance through Andrew W Shaffer.
- 23 saved terminal outcomes: one `verified_employer_found`, one
  `occupation_only_found` and 21 `requires_archival_review`.
- Ten high-confidence, two probable, seven ambiguous and four unresolved
  identities.
- Seven sources, four organizations, four affiliations, 17 published or
  qualified claims, 23 person updates, 23 research attempts and 31
  claim-source links.
- Kurt Schaffenberger's Jack Binder Studio employment separated from his
  immediate pre-OSS U.S. Army art assignment.
- Marjorie Severyns Ravenholt's University of Washington and Fletcher School
  attendance modeled as student affiliations rather than employment.
- Felizia Seyd's prewar authorship visibly qualified at medium confidence;
  her publisher is not treated as an employer.
- Daniel Shacter's postwar Library of Congress mission assignment retained as
  identity context and not converted into pre-OSS employment.
- Eight official Army identity bridges; coded Army fields remain private and
  do not become employer claims.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero; all 23 people have non-planned research attempts.
- Evidence-bundle validation: seven sources, four organizations, four
  affiliations, 17 claims, 23 person updates, 23 attempts and 31 claim-source
  links.
- Public projection: 23,978 source rows, 23,937 people, 2,861 affiliations,
  1,069 organizations, 5,285 sources and 7,733 published or qualified claims.
- Research-attempt coverage: 12,772/23,937 people (53.3567%).
- Verified-employer coverage: 422/23,937 people (1.7630%).
- Verified-affiliation coverage: 929/23,937 people (3.8810%).
- Archival-review coverage: 11,239/23,937 people (46.9524%).
- Remaining `not_started`: 11,160 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 495 files checked with zero errors, warnings or hints; 25,050 pages
  built.
- Bounded Playwright release suite: 87/87 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,050 HTML files, zero broken internal links; 51,404
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,122 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,338,637 bytes, SHA-256
  `fc6f9af1cd318a363f67b4db75f92afb4d1ce1fb171097543f866db59a95229b`.
- Deterministic production build: two 25,122-file builds matched at SHA-256
  `2b49e3b2a169da6a4f8bd487641556f20b27e2712acb901a6135e004bbc407ab`.

## Publication state

Published from content commit
`5199680264b561bf031aafa3c24f026c00170545`. GitHub Pages run
`39035599959` and Test run `39035599964` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(116,338,637 bytes), eight core routes, 36 source-register pages and all 23
direct profile routes referenced by the evidence bundle at
`https://therealjameswilson.github.io/before-oss/`. The live manifest SHA-256
is `fc6f9af1cd318a363f67b4db75f92afb4d1ce1fb171097543f866db59a95229b`,
matching the reviewed release. Live statistics report generation time
`2026-10-17T12:20:00Z`, 12,772 research-attempted people, 422 verified-
employer profiles, 929 verified-affiliation profiles and 11,239 people with
archival-review assessment.
