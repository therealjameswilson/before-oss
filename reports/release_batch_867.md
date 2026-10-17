# Batch 867 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 423, rows 24-46: 23 separately preserved source rows,
  from John M Shepard through Harold S Sheridan, linked to 23 active people.
- 23 saved terminal research outcomes: one `verified_employer_found`, one
  `conflicting_sources` and 21 `requires_archival_review`.
- Twelve high-confidence, two ambiguous, one conflicting and eight unresolved
  identities.
- Seven sources, two organizations, two affiliations, 17 claims, 22 person
  updates, 22 manual research attempts and 33 claim-source links.
- Immediate and last civilian government employment at the Library of Congress
  documented for Jesse Hauk Shera; earlier employment at the Scripps Foundation
  for Research in Population Problems remains separately classified.
- Ten protected-identifier Army candidates accepted for identity only; no
  coded Army field was converted into an employer or OSS rank.
- Louis W. Sherack's protected-identifier conflict preserved without
  transferring a different person's Army data or an unbridged namesake's
  occupation.
- Two low-confidence namesake leads retained for review but withheld from
  public claims, sources and default analytics.

## Data gates

- SQLite integrity check: `ok`; foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts, totaling 28 attempts across manual and bounded adapter
  checks.
- Evidence-bundle validation: seven sources, two organizations, two
  affiliations, 17 claims, 22 person updates, 22 attempts and 33 embedded
  claim-source links.
- Public projection: 23,978 source rows, 23,937 people, 2,873 affiliations,
  1,076 organizations, 5,320 sources and 7,795 published or qualified claims.
- Research-attempt coverage: 12,907/23,937 people (53.9207%).
- Verified-employer coverage: 426/23,937 people (1.7797%).
- Verified-affiliation coverage: 938/23,937 people (3.9186%).
- Archival-review coverage: 11,374/23,937 people (47.5164%).
- Remaining `not_started`: 11,025 people.
- Public redaction checks: passed during public-data generation.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 501 files checked with zero errors, warnings or hints; 25,057 pages
  built.
- Bounded Playwright release suite: 87/87 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,057 HTML files, zero broken internal links; 51,431
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,129 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,746,847 bytes, SHA-256
  `4ab4f074fc6e8e850cc55a5818629916f97592d436e65908fdedf47dc4ced83f`.
- Deterministic production build: two 25,129-file builds matched at SHA-256
  `95dabb23c8b2b7d3a970d499da5fbc0010a618d5cc5762f4e07442102d522602`.

## Publication state

Batch 867 has passed local release gates but has not yet been published. The
current public site remains Batch 866 at
<https://therealjameswilson.github.io/before-oss/>.
