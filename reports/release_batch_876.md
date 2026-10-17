# Batch 876 release report

Date: 2026-10-17

## Release contents

- NARA index PDF page 428, rows 1-23: 23 separately preserved source rows,
  from Oliver M Silsby through Uumo A Simila, linked to 23 active people.
- 23 terminal research outcomes: one `conflicting_sources` and 22
  `requires_archival_review`.
- One confirmed, 11 high-confidence, one conflicting and ten unresolved
  identities.
- Five sources, one reused organization, one affiliation, 14 claims, 23
  person updates, 23 staged research attempts and 29 claim-source links.
- A confirmed Oliver M Silsby Army-to-OSS pathway supported by National Park
  Service and Washington Post evidence, explicitly separated from his still
  unresolved last civilian employer.
- Eleven high-confidence official Army identity matches without converting
  Army-coded data into unsupported employers or OSS roles.
- An explicit Mario J Silvestri versus `SELLERS JIM` Army-record conflict.
- Rejected Albert Simard and Uumo Simila leads retained for auditability but
  excluded from published affiliations.

## Data gates

- SQLite integrity check: `ok`; foreign-key check: zero rows.
- Batch `not_started` and `in_progress`: zero; all 23 people have non-planned
  research attempts.
- Repeat evidence and Army-decision imports: idempotent.
- Public projection: 23,978 source rows, 23,937 active people, 2,898
  affiliations, 1,089 organizations, 5,380 sources and 7,913 published or
  qualified claims.
- Research-attempt coverage: 13,111/23,937 people (54.7729%).
- Verified-employer coverage: 431/23,937 people (1.8006%).
- Verified-affiliation coverage: 950/23,937 people (3.9688%).
- Archival-review coverage: 11,578/23,937 people (48.3686%).
- Remaining `not_started`: 10,821 people; remaining `in_progress`: 1,893.
- Possible duplicate groups: 583; conflicts: 455 people.
- Claim confidence totals: 1,622 confirmed, 4,179 high, 1,733 medium, 206 low,
  383 conflicting and two unresolved.
- Citations: 6,618; unique source documents: 3,588.
- Public redaction checks: passed during public-data generation.

## Software and publication gates

- Python: 145 tests and 81 parameterized subtests passed.
- Astro production renderer: 25,070 pages built.
- Bounded Playwright release suite: 87/87 passed across Batch 876, core routes,
  the oil-company category, analytics and accessibility at desktop, phone and
  tablet viewports.
- Stratified profile audit: 200/200 profiles passed all integrity checks.
- Internal link check: 25,070 HTML files, zero broken internal links; 51,472
  external URLs inventoried for separate live review.
- Identifier audit: 12,926 normalized private identifiers, 120 formatted
  variants and 25,142 artifacts checked; zero unexpected boundary matches.
- Public manifest: 67 assets, 117,460,018 bytes, SHA-256
  `484ef20bd60671a5209db30c75e1caf65e3cd46bd7531f13a17209cb8212c0ef`.
- Deterministic production render: two 25,142-file builds matched at SHA-256
  `2d1e40507debe0ee3875f8a0544f20d8ae74cacc9c2836a0c0b357baa49b14f5`.
- Local Astro diagnostics stalled without an error on the current macOS/Node
  runtime. GitHub's clean Linux test workflow independently completed the full
  test and release gate successfully in 3m36s (run `39077612048`).

## Publication state

Batch 876 is published at <https://therealjameswilson.github.io/before-oss/>.
Content commit `7b1001988eb2e9751409ec53f135f2c8253b29aa` passed the GitHub
Actions test workflow (run `39077612048`) and GitHub Pages deployment (run
`39077612032`). An unauthenticated immutable verification matched all 67 assets
and 117,460,018 bytes to the committed manifest, then checked all eight core
routes, all 36 source-register pages and all 23 Batch 876 person profiles.

## Current blocker

Authenticated NARA Catalog API research remains disabled until the previously
exposed key is rotated and supplied through a local environment or repository
secret. No credential was used, logged or committed in this batch.
