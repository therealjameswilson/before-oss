# Batch 881 release audit

Date: 2026-10-17 America/New_York

## Release contents

- NARA index page 430, rows 24-46: Anne Sirotenko through H Skgolsvik.
- 23 saved terminal research outcomes, including nine high-confidence identity
  resolutions, 13 unresolved identities retained for archival review and one
  explicit identity conflict.
- Three new public affiliations, nine new public sources and 13 new public
  claims.
- Claim-level support for Youri Skarzynski's French Army-to-OSS pathway, Hans
  Skabo's prewar Indiana National Guard service and Alfred Skerpan's Harvard
  student status.
- Six accepted and two conflicting Army review decisions, with protected
  identifiers excluded from public assets.
- Explicit preservation of the H Skgolsvik/Hakon A Skjolsvik shared-identifier
  conflict without merging the two index people or accepting an unrelated
  Army name.

## Reproducible release checks

- SQLite integrity: `ok`; foreign-key violations: zero.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 145 tests and 81 parameterized subtests pass.
- Astro: 512 files checked with zero errors, warnings or hints; 25,074 static
  pages built.
- Browser release suite: 90/90 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,074 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,146 artifacts; zero unexpected matches.
- Public manifest: 67 assets, 117,860,306 bytes, SHA-256
  `4724d5fdb8f2a75bf23b60beccd588ac4e393106d94fbf384fd17528d6e8ccde`.
- Two consecutive output trees: 25,146 files, 327,246,775 bytes, SHA-256
  `c96e480bc392bdaae989c2f2ea36df2987dcffeac83ac4273ad8f66540abd401`.
- Dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,225/23,937 people (55.2492%).
- Verified affiliation: 959/23,937 people (4.0064%).
- Verified employer: 433/23,937 people (1.8089%).
- Archival disposition assessed: 11,692/23,937 people (48.8449%).
- Not started: 10,707 people; in progress: 1,893 people.
- Public projection: 23,937 profiles, 2,910 affiliations, 1,092
  organizations, 5,413 sources and 7,982 claims.

## Publication verification

Pending content commit, clean Linux Test workflow, GitHub Pages deployment and
unauthenticated live-release verification.
