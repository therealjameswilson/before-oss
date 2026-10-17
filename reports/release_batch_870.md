# Batch 870 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 425, rows 1-23: 23 separately preserved source rows,
  from Naotada Shimomura through Clifton B Shoemaker, linked to 23 active
  people.
- 23 terminal research outcomes: one `documented_prewar_employer_found`, one
  `occupation_only_found`, two `conflicting_sources` and 19
  `requires_archival_review`.
- One confirmed, five high-confidence, two probable, two conflicting and 13
  unresolved identities.
- Eight sources, four organizations, four affiliations, 13 claims, 23 person
  updates, 23 research attempts and 24 claim-source links.
- Direct OSS evidence for Ezra Shine, qualified identity evidence for Maurice
  Shire, and separate student-status evidence for Clayton L Shirey.
- Qualified employment chronology for Julius Shiskin without inventing an
  immediate pre-OSS relationship.
- Three protected-identifier Army candidates accepted for identity only; two
  incompatible candidates remain visible as conflicts.

## Data gates

- SQLite integrity check: `ok`; foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts.
- Evidence-bundle validation: eight sources, four organizations, four
  affiliations, 13 claims, 23 person updates, 23 attempts and 24 embedded
  claim-source links.
- Public projection: 23,978 source rows, 23,937 people, 2,886 affiliations,
  1,083 organizations, 5,342 sources and 7,838 published or qualified claims.
- Research-attempt coverage: 12,975/23,937 people (54.2048%).
- Verified-employer coverage: 428/23,937 people (1.7880%).
- Verified-affiliation coverage: 941/23,937 people (3.9312%).
- Archival-review coverage: 11,442/23,937 people (47.8005%).
- Remaining `not_started`: 10,957 people.
- Public redaction checks: passed during public-data generation.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 504 files checked with zero errors, warnings or hints; 25,064 pages
  built.
- Bounded Playwright release suite: 90/90 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,064 HTML files, zero broken internal links; 51,449
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,136 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 117,019,452 bytes, SHA-256
  `e4ab5fb64dcf850280e6e1c1cb1966a33938b0613799a9fa57b89763211e703f`.
- Deterministic production build: two 25,136-file builds matched at SHA-256
  `ee2c376bf290be403d25c86e16b3a08603132a6daa8c2ff8f7d670b4456d418a`.

## Publication state

Batch 870 has passed all local release gates and is awaiting publication to the
existing GitHub Pages site. The immutable content commit, GitHub Actions runs
and live verification will be recorded after deployment.
