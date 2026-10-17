# Batch 860 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 420, rows 1-23: 23 separately preserved and reviewed
  source rows, from Walter Sereda through Paul D Sevcik.
- 23 saved terminal outcomes: one `verified_employer_found`, two
  `documented_prewar_employer_found` and 20 `requires_archival_review`.
- Eleven high-confidence, one probable and eleven unresolved identities.
- 13 sources, six organizations, six affiliations, 19 published claims, 23
  person updates, 23 research attempts and 39 claim-source links.
- Beurt R. SerVaas's Shortridge High School teaching published as both explicit
  immediate pre-OSS employment and his last civilian employer.
- Boris Sergievsky's Sikorsky Aircraft and Helicopter Corporation of America
  positions published as documented prewar work, without inventing an
  immediate predecessor.
- André Sérot's French military-intelligence and Air Force security assignments
  modeled as Allied military service, not civilian employment.
- Renzo Sereno's University of Chicago research work visibly qualified as a
  medium-confidence probable identity.
- Eight official Army identity bridges; coded Army fields remain private and
  do not become employer claims.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero; all 23 people have non-planned research attempts.
- Evidence-bundle validation: 13 sources, six organizations, six
  affiliations, 19 claims, 23 person updates, 23 attempts and 39 claim-source
  links.
- Public projection: 23,978 source rows, 23,937 people, 2,857 affiliations,
  1,068 organizations, 5,278 sources and 7,716 published claims.
- Research-attempt coverage: 12,749/23,937 people (53.2606%).
- Verified-employer coverage: 421/23,937 people (1.7588%).
- Verified-affiliation coverage: 927/23,937 people (3.8727%).
- Archival-review coverage: 11,216/23,937 people (46.8563%).
- Remaining `not_started`: 11,183 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 494 files checked with zero errors, warnings or hints; 25,049 pages
  built.
- Bounded Playwright release suite: 87/87 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,049 HTML files, zero broken internal links; 51,399
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,121 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,241,856 bytes, SHA-256
  `02cfe97ad88d326979996746b65ee051a3f8d3f251a27eab5b3da358dace1127`.
- Deterministic production build: two 25,121-file builds matched at SHA-256
  `f76328427f5bc93da4c4369d388c36e20657f69687a3ae984f436914945ca4d9`.

## Publication state

Published from content commit
`09d374bf48ea8d0ccdad914bd13e9b0799e93ee5`. GitHub Pages run
`38961424058` and Test run `38961424069` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(116,241,856 bytes), eight core routes, 36 source-register pages and all 23
direct profile routes referenced by the evidence bundle at
`https://therealjameswilson.github.io/before-oss/`. The live manifest SHA-256
is `02cfe97ad88d326979996746b65ee051a3f8d3f251a27eab5b3da358dace1127`,
matching the reviewed release. Live statistics report generation time
`2026-10-16T20:28:00Z`, 12,749 research-attempted people, 421
verified-employer profiles, 927 verified-affiliation profiles and 11,216
people with archival-review assessment.
