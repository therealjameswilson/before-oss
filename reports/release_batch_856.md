# Batch 856 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 418, rows 1-23: 23 separately preserved and reviewed
  source rows, from Robert Scott through Helen Seeman.
- 23 saved terminal outcomes: two `verified_employer_found`, one
  `conflicting_sources` and 20 `requires_archival_review`.
- Two confirmed, nine high-confidence, two ambiguous, one conflicting and nine
  unresolved identities.
- Seven sources, five organizations, five affiliations, 16 published claims,
  24 person updates, 23 research attempts and 30 claim-source links.
- Winston M Scott's immediate FBI government assignment and separate
  University of Alabama last civilian employment.
- Jay Seeley's documented prewar Anatolia College teaching, separated from
  the unresolved immediate and last-civilian questions.
- Dorothea C Seelye's Bryn Mawr and Theodora Sedgwick's Radcliffe student
  affiliations, neither misclassified as employment.
- Seven official Army identity bridges based on nonshared protected
  identifiers; coded Army fields are not published as employers or
  affiliations.
- Jay Seeley/Jay S Seely and James Securanza/James P Sicuranza remain separate
  in opaque possible-duplicate groups. No protected identifier is embedded in
  public or durable group labels.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero; all 23 people have non-planned research attempts.
- Evidence-bundle validation: seven sources, five organizations, five
  affiliations, 16 claims, 24 person updates, 23 attempts and 30 claim-source
  links.
- Public projection: 23,978 source rows, 23,937 people, 2,839 affiliations,
  1,057 organizations, 5,241 sources and 7,647 published claims.
- Research-attempt coverage: 12,657/23,937 people (52.8763%).
- Verified-employer coverage: 416/23,937 people (1.7379%).
- Verified-affiliation coverage: 916/23,937 people (3.8267%).
- Archival-review coverage: 11,124/23,937 people (46.4720%).
- Remaining `not_started`: 11,275 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests passed.
- Astro: 489 files checked with zero errors, warnings or hints; 25,037 pages
  built.
- Bounded Playwright release suite: 84/84 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,037 HTML files, zero broken internal links; 51,366
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,109 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 115,786,491 bytes, SHA-256
  `4acbcef01fe19cf8a36866c212a160c265b9bce6be83d2a5b955adc3855e4524`.
- Deterministic production build: two 25,109-file builds matched at SHA-256
  `2349552601ceb52d845e7b38d80b2a971de60ca1aabf7b9b434cf31b31e17176`.

## Publication state

The reviewed content is locally complete. GitHub Pages publication and
unauthenticated immutable verification are pending.
