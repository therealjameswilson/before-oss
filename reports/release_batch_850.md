# Batch 850 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 415, rows 1-23: 23 separately preserved and reviewed
  source rows, from Joseph Schreiber through Gloria M Schuette.
- 23 terminal research outcomes: one `completed` and 22
  `requires_archival_review`.
- One confirmed identity, six high-confidence identities, one probable identity
  and 15 unresolved identities.
- Four reviewed sources, three organizations, three affiliations, 11 claims
  and 23 manual staged-protocol attempts.
- A confirmed Army Officer Candidate School-to-OSS pathway for George A
  Schriever and qualified University of Missouri and University of Chicago
  student affiliations. No civilian employer was invented from military or
  educational evidence.
- Six accepted Army identity decisions; protected identifiers and coded
  occupations remain private.
- The three Samuel A Schreiner rows remain separate, and the Kenneth D
  Schuckers/Shuckers identifier conflict remains qualified and unmerged.
- The unfamiliar `1ST ST` abbreviation for Richard E Schrunk remains
  unexpanded.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero.
- Evidence-bundle validation: four sources, three organizations, three
  affiliations, 11 claims, 23 updates and 23 attempts.
- Idempotency: evidence and review-decision replays produced no duplicate
  accepted records.
- Public projection: 23,978 source rows, 23,937 people, 2,825 affiliations,
  1,047 organizations, 5,198 sources and 7,576 published claims.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 subtests passed.
- Astro: 484 files checked with zero errors, warnings or hints; 25,027 pages
  built.
- Bounded Playwright release suite: 90/90 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,027 HTML files, zero broken internal links; 51,328
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,099 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 115,321,575 bytes, SHA-256
  `6159c373b25af53c8b6a24276f472734982da1db5899f0eac1c91d3eb2e4d8f3`.
- Deterministic production build: two 25,099-file builds matched at SHA-256
  `e3bf8f47ec26238fb5d9881107a996c0c3ca416445c5800d56867f31360a3a72`.

## Publication state

Published from content commit
`5f13d5f60f1ff7f93f572d692bdfac08d9517e10`. GitHub Pages run
`38918903925` and test run `38918903993` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(115,321,575 bytes), eight core routes, 35 source-register pages and all 23
Batch 850 person profiles at
`https://therealjameswilson.github.io/before-oss/`. The live manifest SHA-256
is `6159c373b25af53c8b6a24276f472734982da1db5899f0eac1c91d3eb2e4d8f3`,
matching the reviewed release. Live statistics report generation time
`2026-10-16T18:54:00Z`, 12,524 research-attempted people, 412 verified
employer profiles, 908 verified-affiliation profiles and 10,989 people with
archival-review assessment.
