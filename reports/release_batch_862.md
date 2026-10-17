# Batch 862 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 421, rows 1-23: 23 separately preserved and reviewed
  source rows, from Eugene Shaffer through John A Shannon.
- 23 saved terminal `requires_archival_review` outcomes.
- Two confirmed, five high-confidence, two probable and 14 unresolved
  identities.
- Six sources, two organizations, two affiliations, 11 published or qualified
  claims, 23 person updates, 23 research attempts and 20 claim-source links.
- John M. Shaheen's prewar political publicity role modeled as a professional
  affiliation, without recasting his postwar oil career as pre-OSS work.
- Lawrence B. Shallcross's official OSS Mission to France evidence used for
  identity only.
- Muddassir A. Shamsee's postwar United Nations record retained as qualified
  identity context, not a pre-OSS affiliation.
- Jack T. Shannon's probable Army-to-OSS pathway visibly qualified at medium
  confidence.
- Five official Army identity bridges; coded Army fields remain private and
  do not become employer claims.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero; all 23 people have non-planned research attempts.
- Evidence-bundle validation: six sources, two organizations, two
  affiliations, 11 claims, 23 person updates, 23 attempts and 20 claim-source
  links.
- Public projection: 23,978 source rows, 23,937 people, 2,863 affiliations,
  1,070 organizations, 5,291 sources and 7,744 published or qualified claims.
- Research-attempt coverage: 12,795/23,937 people (53.4528%).
- Verified-employer coverage: 422/23,937 people (1.7630%).
- Verified-affiliation coverage: 930/23,937 people (3.8852%).
- Archival-review coverage: 11,262/23,937 people (47.0485%).
- Remaining `not_started`: 11,137 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 496 files checked with zero errors, warnings or hints; 25,051 pages
  built.
- Bounded Playwright release suite: 87/87 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,051 HTML files, zero broken internal links; 51,407
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,123 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,402,851 bytes, SHA-256
  `2198dfb8729d7f05ebb21ae38da809d413512dec95bcd39e5df8691bb657eaf9`.
- Deterministic production build: two 25,123-file builds matched at SHA-256
  `ecb5d33b2b899e3ae90107eaf590c01a84344f7060abd7f97809c9d5fed0b3ee`.

## Publication state

Local release gates passed. Publication and unauthenticated live verification
are pending.
