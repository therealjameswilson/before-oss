# Batch 854 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 417, rows 1-23: 23 separately preserved and reviewed
  source rows, from Anna F Schwiebert through Clarence E Scott.
- 23 terminal research outcomes: one `documented_prewar_employer_found`, one
  `occupation_only_found` and 21 `requires_archival_review`.
- Two confirmed, seven high-confidence, one probable, five ambiguous and eight
  unresolved identities.
- Seven sources, one organization, two affiliations, 12 claims, 23 person
  updates, 23 manual staged-protocol attempts and 24 claim-source links.
- Carleton F Scofield's 1935 University of Buffalo employment is published as
  documented prewar work, not as an immediate affiliation or last civilian
  employer.
- Arthur Sclater's direct official OSS awards evidence confirms his British
  identity and SFHQ commands without inventing a pre-service employer.
- Alfred/Alfredo Sciarrotta remains a qualified probable identity with an
  explicit immediate engineering occupation but no named Naples employer.
- Seven accepted Army identity bridges retain spelling and grade differences;
  protected identifiers and coded occupations remain private.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero; all 23 people have non-planned research attempts.
- Evidence-bundle validation: seven sources, one organization, two
  affiliations, 12 claims, 23 person updates, 23 attempts and 24 claim-source
  links.
- Public projection: 23,978 source rows, 23,937 people, 2,834 affiliations,
  1,055 organizations, 5,232 sources and 7,628 published claims.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 subtests passed.
- Astro: 488 files checked with zero errors, warnings or hints; 25,035 pages
  built.
- Bounded Playwright release suite: 81/81 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,035 HTML files, zero broken internal links; 51,359
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,107 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 115,658,990 bytes, SHA-256
  `4f15e4604eb3ac222c185dca51b6e36708b303ee4ff845c507b21c5169576aa6`.
- Deterministic production build: two 25,107-file builds matched at SHA-256
  `36b219880944338f576a4c351744b86c1dbe305d5f91209f02954dc535efd314`.

## Publication state

Published from content commit
`6d719307e06e977ad61537aa7eb0e47dfe3adad2`. GitHub Pages run
`38937082104` and test run `38937081582` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(115,658,990 bytes), eight core routes, 35 source-register pages and all 23
Batch 854 direct profile routes at
`https://therealjameswilson.github.io/before-oss/`. The live manifest SHA-256
is `4f15e4604eb3ac222c185dca51b6e36708b303ee4ff845c507b21c5169576aa6`,
matching the reviewed release. Live statistics report generation time
`2026-10-16T19:42:00Z`, 12,613 research-attempted people, 414
verified-employer profiles, 912 verified-affiliation profiles and 11,078 people
with archival-review assessment.
