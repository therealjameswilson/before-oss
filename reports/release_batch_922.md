# Batch 922 release audit

Date: 2026-10-26 America/New_York

## Release contents

- NARA index page 451, rows 24-46: Robert G. Storey through Eli Strahinic.
- 23 immutable source rows, 23 separate person entities, 23 terminal research
  outcomes and 23 saved staged-protocol research attempt records.
- Four accepted official Army identity bridges and one rejected conflicting-
  initial candidate; no protected identifier appears in public data.
- Robert Gerald Storey's qualified last civilian status is private Dallas legal
  practice, supported by a visually checked May 1941 official court listing.
  No 1941 firm or explicit immediate-pre-OSS transition is claimed.
- Hans Storhaug's December 1940 Norwegian Independent Company 1 service is an
  Allied military assignment, not a civilian employer.
- Four qualified historical Army occupation or status categories name no
  employer or institution. John L. Stoyka's independently documented OSS Cat
  Team identity remains separate from his pre-Army teacher/instructor category.
- Cecil C. Stovall's index C versus Army O middle-initial conflict remains
  visible and no Army field was transferred.
- The next boundary, Carl A. Strahle on page 452 row 1, was confirmed from the
  canonical source record.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 553 files checked with zero errors, warnings or hints; 25,140 static
  pages built.
- Batch browser suite: 24/24 checks pass on desktop, phone and tablet.
- Browser release suite: 93/93 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,140 HTML files checked; all links resolve. The checker
  separately inventories 51,715 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,212 production artifacts; 1,405 candidate substrings
  inspected and zero unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 122,817,400 bytes, SHA-256
  `061273032ffd29a0dcf45045081c9765861823c1be9c3666f44247694c08ad39`.
- Consecutive public trees: 70 files, 125,164,553 bytes, SHA-256
  `a1e0f4edf8489ea6df009ea7cb925e6e23150e4ea4009e9cf38391cb4657d37e`.
- Consecutive output trees: 25,212 files, 335,210,084 bytes, SHA-256
  `08187f771fd4ebc0740bad539953d4d8f651dd78854e270c9cea8969388ea05d`.
- Production dependency audit: zero vulnerabilities. Five findings remain
  confined to the build/test toolchain; no Node dependency ships with the
  static site.
- The CI-equivalent site validation ran from a `/private/tmp` copy containing
  the release's site, data, evidence and test inputs because the cloud-synced
  checkout's Astro diagnostic process did not return. Dependencies were
  installed from the local npm cache. This affected neither project files nor
  CI inputs.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,155/23,936 people (59.1369%).
- Verified affiliation: 1,006/23,936 people (4.2029%).
- Verified employer: 452/23,936 people (1.8884%).
- Archival disposition assessed: 12,628/23,936 people (52.7574%).
- Not started: 9,776 people; in progress: 1,886 people.
- Possible-duplicate groups: 619; conflicts: 487.
- Claim confidence: 1,646 confirmed; 4,603 high; 2,008 medium; 242 low;
  410 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,239 affiliations, 1,157 organizations,
  5,757 sources and 8,663 claims.
- Evidence ledger: 7,027 citations across 3,854 unique source documents.

## Publication verification

Batch 922 is public from immutable content commit
`e70dadec0477f693f3dbc071824c8f6bddb8df4c`. GitHub Actions Test run
[`40301838824`](https://github.com/therealjameswilson/before-oss/actions/runs/40301838824)
and Pages deployment run
[`40301838826`](https://github.com/therealjameswilson/before-oss/actions/runs/40301838826)
both completed successfully. The unauthenticated deployed-release verifier
matched all 67 public assets (122,817,400 bytes) to manifest SHA-256
`061273032ffd29a0dcf45045081c9765861823c1be9c3666f44247694c08ad39`,
verified eight core routes, 39 source-register pages and all 23 directly
affected profiles at <https://therealjameswilson.github.io/before-oss/>.

The first post-deployment verification encountered one transient GitHub Pages
503 while fetching a profile. The exact same immutable-commit verification was
repeated after the edge cache settled and then passed in full; no release file
or verifier input was changed. The workflows emitted non-blocking annotations
about GitHub's Node.js 20 action-runtime transition and the pending
`ubuntu-latest` runner migration. Neither annotation altered the successful
build, test, redaction audit or deployment.
