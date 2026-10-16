# Batch 849 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 414, rows 24-46: 23 separately preserved and reviewed
  source rows, from Norman B. Schofield through Dale F. Schreckengost.
- 23 terminal research outcomes: 20 `requires_archival_review`, two
  `verified_employer_found` and one `documented_prewar_employer_found`.
- One confirmed identity, 11 high-confidence identities, one probable identity
  and ten unresolved identities.
- 11 reviewed sources, three organizations, three affiliations, 16 claims and
  23 manual staged-protocol attempts.
- Newly documented pathways for Herman F. Scholtz and International Engineering
  Company, Frank Schoonmaker and Frank Schoonmaker Selections, and Anton B.
  Schrader and the Dutch wartime food-supply bureau. Each claim keeps immediate
  affiliation, last civilian employer and intervening chronology distinct.
- Six accepted and one rejected Army identity decisions; protected identifiers
  and coded occupations remain private.
- Two possible-duplicate pairs remain four separate public person entities.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero.
- Evidence-bundle validation: 11 sources, three organizations, three
  affiliations, 16 claims, 23 updates and 23 attempts.
- Idempotency: evidence and review-decision replays produced no duplicate
  accepted records.
- Public projection: 23,978 source rows, 23,937 people, 2,822 affiliations,
  1,046 organizations, 5,194 sources and 7,565 published claims.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests passed.
- Astro: 483 files checked with zero errors, warnings or hints; 25,026 pages
  built.
- Bounded Playwright release suite: 93/93 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,026 HTML files, zero broken internal links; 51,325
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,098 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 115,253,995 bytes, SHA-256
  `c550b130ba12cdbb21807567341557c4014ed218a46edc0868de6e0280441853`.
- Deterministic production build: two 25,098-file builds matched at SHA-256
  `a81ac6ada36ae698de38141a3bd88f3b5ba8771221cc11b6240f4ff9c0f77729`.

## Publication state

Publication is pending the Batch 849 content commit, GitHub Pages deployment,
test workflow and immutable unauthenticated verification. The previously
verified Batch 848 release remains public until those gates complete.
