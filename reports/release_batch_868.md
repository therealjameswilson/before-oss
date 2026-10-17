# Batch 868 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 424, rows 1-23: 23 separately preserved source rows,
  from Thomas J Sheridan through Byron P Sherry, linked to 23 active people.
- 23 saved terminal research outcomes: one `verified_employer_found`, two
  `documented_prewar_employer_found` and 20 `requires_archival_review`.
- Six high-confidence, two probable and 15 unresolved identities.
- Eight sources, five organizations, five affiliations, 15 claims, 23 person
  updates, 23 manual research attempts and 27 claim-source links.
- Immediate and last civilian employment at A.G. Becker documented for Irving
  H. Sherman; Florence Janson Sherriff's three teaching affiliations and Victor
  F. Sheronas's Moscow government assignment remain separately classified as
  documented prewar rather than immediate.
- Five protected-identifier Army candidates accepted for identity only; no
  coded Army field was converted into an employer or OSS rank.
- One low-confidence namesake lead retained for review but withheld from public
  claims, sources and default analytics.

## Data gates

- SQLite integrity check: `ok`; foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts, totaling 25 attempts across manual and bounded adapter
  checks.
- Evidence-bundle validation: eight sources, five organizations, five
  affiliations, 15 claims, 23 person updates, 23 attempts and 27 embedded
  claim-source links.
- Public projection: 23,978 source rows, 23,937 people, 2,878 affiliations,
  1,080 organizations, 5,327 sources and 7,809 published or qualified claims.
- Research-attempt coverage: 12,930/23,937 people (54.0168%).
- Verified-employer coverage: 427/23,937 people (1.7838%).
- Verified-affiliation coverage: 939/23,937 people (3.9228%).
- Archival-review coverage: 11,397/23,937 people (47.6125%).
- Remaining `not_started`: 11,002 people.
- Public redaction checks: passed during public-data generation.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 502 files checked with zero errors, warnings or hints; 25,061 pages
  built.
- Bounded Playwright release suite: 90/90 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,061 HTML files, zero broken internal links; 51,439
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,133 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,842,725 bytes, SHA-256
  `841b27a5d04449170bfbcb23e45c5472fd97bf3cb61f54710e700391875ffee3`.
- Deterministic production build: two 25,133-file builds matched at SHA-256
  `08fc3bd1303f1558a9cd66d1b7373a25eb26fc2b94563b16baecca92bdc462b9`.

## Publication state

Batch 868 is a locally validated release candidate. Publication and immutable
live verification are still pending.
