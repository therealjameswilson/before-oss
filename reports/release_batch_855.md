# Batch 855 release report

Date: 2026-10-16

## Release contents

- NARA index PDF page 417, rows 24-46: 23 separately preserved and reviewed
  source rows, from Dagmar S Scott through Robert F Scott.
- 23 terminal `requires_archival_review` outcomes with saved staged-protocol
  attempts.
- Three high-confidence, six ambiguous and 14 unresolved identities.
- Two sources, no organizations or affiliations, three published identity
  claims, 23 person updates, 23 research attempts and six claim-source links.
- Three official Army identity bridges based on nonshared protected identifiers;
  coded Army fields are not published as employers or affiliations.
- Three Edward F Scott rows and two Marianne Scott rows remain separate and
  visibly flagged as possible duplicates.
- Franklin D Scott's Northwestern lead and the Lillie, Richard P and Robert F
  Scott namesakes remain rejected or unresolved; no employer was invented.
- Printed index spelling and notes remain recoverable, including `Dharles R
  Scott` and `British Ci`.

## Data gates

- SQLite integrity check: `ok`.
- SQLite foreign-key check: zero rows.
- Batch `not_started`: zero; all 23 people have non-planned research attempts.
- Evidence-bundle validation: two sources, no organizations or affiliations,
  three claims, 23 person updates, 23 attempts and six claim-source links.
- Public projection: 23,978 source rows, 23,937 people, 2,834 affiliations,
  1,055 organizations, 5,234 sources and 7,631 published claims.
- Research-attempt coverage: 12,635/23,937 people (52.7844%).
- Verified-employer coverage: 414/23,937 people (1.7295%).
- Verified-affiliation coverage: 912/23,937 people (3.8100%).
- Archival-review coverage: 11,101/23,937 people (46.3759%).
- Remaining `not_started`: 11,297 people.
- Public redaction checks: passed.

## Software and publication gates

- Python: 145 tests and 81 subtests passed.
- Astro: 489 files checked with zero errors, warnings or hints; 25,035 pages
  built.
- Bounded Playwright release suite: 81/81 passed across desktop, phone and
  tablet.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,035 HTML files, zero broken internal links; 51,359
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,107 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 115,681,276 bytes, SHA-256
  `063483284b40af23676cbc5e8bba6cecf69a82906c244fc7807ccaf42090b739`.
- Deterministic production build: two 25,107-file builds matched at SHA-256
  `23743b6c483d6eccb47490b3189c923964210aa7f0128b309795383054417e04`.

## Publication state

The reviewed content is ready to publish. The commit SHA, GitHub Pages and Test
run identifiers, and unauthenticated live-verifier result will be added after
deployment completes.
