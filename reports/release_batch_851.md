# Batch 851 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 415, rows 24-46: 23 separately preserved and reviewed
  source rows, from Ann M Schuetz through Bernard G Schulz.
- 23 terminal research outcomes: one `completed`, two
  `verified_employer_found` and 20 `requires_archival_review`.
- One confirmed identity, eight high-confidence identities and 14 unresolved
  identities.
- Four reviewed sources, one organization, one affiliation, eight claims and
  21 new manual staged-protocol attempts; the two Schulberg profiles retain
  their already reviewed employer outcomes.
- A confirmed, directly documented prewar Signal Intelligence Service
  assignment for Robert E Schukraft. It remains separate from the unknown
  immediate OSS predecessor and unknown last civilian employer.
- Six accepted Army identity decisions and one rejected conflicting candidate;
  protected identifiers and coded occupations remain private.
- The two Curtis C Schultz rows and the Audrey B Schultz/Schulz spelling
  variants remain separate, visibly grouped records.
- Chronologically incompatible namesakes remain rejected leads rather than
  published affiliations.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero.
- Evidence-bundle validation: four sources, one organization, one affiliation,
  eight claims, 21 person updates and 21 attempts.
- Idempotency: evidence and review-decision replays produced no duplicate
  accepted records.
- Public projection: 23,978 source rows, 23,937 people, 2,826 affiliations,
  1,048 organizations, 5,202 sources and 7,584 published claims.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 subtests passed.
- Astro: 485 files checked with zero errors, warnings or hints; 25,028 pages
  built.
- Bounded Playwright release suite: 87/87 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,028 HTML files, zero broken internal links; 51,331
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,100 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 115,374,097 bytes, SHA-256
  `fb812ebe3c22189305708ae7a1b3479acbb55530753893d21b1ded1d448947c9`.
- Deterministic production build: two 25,100-file builds matched at SHA-256
  `11ce470a3aa7047704b7d3d0e470e6f96f810fe3a750ed6a6964c2306369e719`.

## Publication state

Published from content commit
`3ff1adda5fc02e77b45353b6b6a71cab06f1e670`. GitHub Pages run
`38923261446` and test run `38923261487` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(115,374,097 bytes), eight core routes, 35 source-register pages and the 21
Batch 851 profiles updated by the evidence bundle at
`https://therealjameswilson.github.io/before-oss/`. Separate live checks
confirmed HTTP 200 responses and the correct names for the two Schulberg
profiles whose reviewed evidence predated this batch, completing verification
of all 23 Batch 851 profile routes. The live manifest SHA-256 is
`fb812ebe3c22189305708ae7a1b3479acbb55530753893d21b1ded1d448947c9`,
matching the reviewed release. Live statistics report generation time
`2026-10-16T18:54:00Z`, 12,545 research-attempted people, 412 verified
employer profiles, 909 verified-affiliation profiles and 11,010 people with
archival-review assessment.
