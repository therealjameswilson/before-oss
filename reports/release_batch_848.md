# Batch 848 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 414, rows 1-23: 23 separately preserved and reviewed
  source rows, from Louis Schneider through LA Vonne L. Schofield.
- 23 terminal research outcomes: 22 `requires_archival_review` and one
  `verified_employer_found`.
- 13 high-confidence identities and ten unresolved identities.
- 12 reviewed sources, eight organizations, eight affiliations, 22 claims and
  23 manual staged-protocol attempts.
- One newly verified employer pathway: John R. Schoemer Jr. and Townley &
  Updike. Thomas Schocken's professional affiliations, Eddie Schodt's student
  affiliations, Solomon Schneyer's qualified student link and Richard
  Schoenberger's military pathway remain separately modeled.
- Ten accepted Army identity decisions; protected identifiers and coded
  occupations remain private.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero.
- Evidence-bundle validation: 12 sources, eight organizations, eight
  affiliations, 22 claims, 23 updates and 23 attempts.
- Idempotency: evidence replay preserved 22 distinct claims, eight distinct
  affiliations and 23 distinct attempts; review replay skipped ten duplicate
  decisions.
- Public projection: 23,978 source rows, 23,937 people, 2,819 affiliations,
  1,043 organizations, 5,183 sources and 7,549 published claims.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 subtests passed.
- Astro: 482 files checked with zero errors, warnings or hints; 25,023 pages
  built.
- Bounded Playwright release suite: 90/90 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,023 HTML files, zero broken internal links; 51,315
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,095 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 115,144,480 bytes, SHA-256
  `30ddf134d4bf90a747e295c76511fdd9653e8abd145b422356b542eae9c68116`.
- Deterministic production build: two 25,095-file builds matched at SHA-256
  `70c0f950060b1077bc0ef36f8729b3baceb17dfd8a3986072ea1809875f9bff3`.

## Publication state

Local release candidate verified. GitHub Pages publication and immutable
unauthenticated verification are pending.
