# Batch 863 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 421, rows 24-46: 23 separately preserved and reviewed
  source rows, from Eli Shapiro through Lee M Sharrar.
- 23 saved terminal outcomes: 22 `requires_archival_review` and one
  `documented_prewar_employer_found`.
- One confirmed, seven high-confidence, one ambiguous and 14 unresolved
  identities.
- Seven sources, three organizations, three affiliations, ten published
  claims, 23 person updates, 23 research attempts and 22 claim-source links.
- Karl J. Shapiro's Enoch Pratt Library School attendance modeled as student
  status rather than employment or an immediate pre-OSS affiliation.
- Lee M. Sharrar's Humble Oil & Refining Company legal work modeled as his
  latest identifiable civilian employer before service, without inventing a
  direct Humble-to-Army or Humble-to-OSS transition; earlier Rice Institute
  teaching remains a separate documented-prewar role.
- Lee M. Sharrar added to the evidence-qualified oil-company category.
- John B. Sharp, Samuel L. Sharp and Doris Sharrai/Sharrar possible duplicates
  remain visible and separate pending archival comparison.
- Six official Army identity bridges accepted and one incompatible candidate
  rejected; coded Army fields remain private and do not become employer claims.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero; all 23 people have non-planned research attempts.
- Evidence-bundle validation: seven sources, three organizations, three
  affiliations, ten claims, 23 person updates, 23 attempts and 22 embedded
  claim-source links.
- Public projection: 23,978 source rows, 23,937 people, 2,866 affiliations,
  1,072 organizations, 5,298 sources and 7,754 published or qualified claims.
- Research-attempt coverage: 12,817/23,937 people (53.5447%).
- Verified-employer coverage: 423/23,937 people (1.7671%).
- Verified-affiliation coverage: 932/23,937 people (3.8936%).
- Archival-review coverage: 11,284/23,937 people (47.1404%).
- Remaining `not_started`: 11,115 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro: 497 files checked with zero errors, warnings or hints; 25,053 pages
  built.
- Bounded Playwright release suite: 87/87 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,053 HTML files, zero broken internal links; 51,414
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,125 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 116,488,321 bytes, SHA-256
  `c5eb292a751bc4f3ad87e0e7c0a9bcd45cc8b79c2738a854d22ab3f762d8bdca`.
- Deterministic production build: two 25,125-file builds matched at SHA-256
  `d79441e41246bc4c8e1d1d9a7740d2b69e4cdc0196599d06da5cfe913df43f3a`.

## Publication state

Local release gates passed. Publication and unauthenticated live verification
are pending.
