# Batch 859 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 419, rows 24-46: 23 separately preserved and reviewed
  source rows, from William W Selvig through Anthony Serao.
- 23 saved terminal outcomes: one `completed`, one
  `verified_employer_found` and 21 `requires_archival_review`.
- Two confirmed, ten high-confidence and eleven unresolved identities.
- Six sources, three organizations, three affiliations, 15 published claims,
  23 person updates, 23 research attempts and 29 claim-source links.
- Mario V. Semolich's Palmer House work published as his last civilian
  employment before Army and OSS service, without claiming it immediately
  preceded OSS.
- Amos E. Sentman's Regular Army service published as his explicit immediate
  military pathway into OSS.
- Peter H. Selz's Columbia University attendance modeled as student status,
  not employment.
- Official wartime context for Amato A. Semenza and Hercules J. Sembrakis,
  without inventing employers or predecessor assignments.
- Nine official Army identity bridges; coded Army fields remain private and
  do not become employer claims.
- John W. Senter's unfamiliar printed `CAMDR` abbreviation remains verbatim
  and unforced.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero; all 23 people have non-planned research attempts.
- Evidence-bundle validation: six sources, three organizations, three
  affiliations, 15 claims, 23 person updates, 23 attempts and 29 claim-source
  links.
- Public projection: 23,978 source rows, 23,937 people, 2,851 affiliations,
  1,063 organizations, 5,265 sources and 7,697 published claims.
- Research-attempt coverage: 12,726/23,937 people (53.1646%).
- Verified-employer coverage: 419/23,937 people (1.7504%).
- Verified-affiliation coverage: 924/23,937 people (3.8601%).
- Archival-review coverage: 11,193/23,937 people (46.7602%).
- Remaining `not_started`: 11,206 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 493 files checked with zero errors, warnings or hints; 25,044 pages
  built.
- Bounded Playwright release suite: 90/90 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,044 HTML files, zero broken internal links; 51,385
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,116 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,101,952 bytes, SHA-256
  `04090186539b9ddc96c78f482a547b9d78dedd79742acfde07100678281441ed`.
- Deterministic production build: two 25,116-file builds matched at SHA-256
  `61170f147ee41a5947391a11e180b02a6534122ab9d313d667f7f06fc69c7607`.

## Publication state

Published from content commit
`3121f21718a2ac4f66dc0d497dd2223428c548c9`. GitHub Pages run
`38958006844` and Test run `38958006858` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(116,101,952 bytes), eight core routes, 36 source-register pages and all 23
direct profile routes referenced by the evidence bundle at
`https://therealjameswilson.github.io/before-oss/`. The live manifest SHA-256
is `04090186539b9ddc96c78f482a547b9d78dedd79742acfde07100678281441ed`,
matching the reviewed release. Live statistics report generation time
`2026-10-16T20:05:00Z`, 12,726 research-attempted people, 419
verified-employer profiles, 924 verified-affiliation profiles and 11,193
people with archival-review assessment.
