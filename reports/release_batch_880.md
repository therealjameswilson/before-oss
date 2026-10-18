# Batch 880 release audit

Date: 2026-10-17 America/New_York

## Release contents

- NARA index page 430, rows 1-23: William A Sincek through Angelo Sirico.
- 23 saved terminal research outcomes, including 13 high-confidence identity
  resolutions and ten unresolved identities retained for archival review.
- Three new public affiliations, five new public sources and 17 new public
  claims.
- Claim-level source support for Charles Siragusa's federal government pathway
  and Curt Siodmak's qualified pre-OSS professional affiliation.
- Ten reviewed Army identity decisions, with protected identifiers excluded
  from public assets.
- Dependency lockfile security updates with zero vulnerabilities after the
  update.

## Reproducible release checks

- SQLite integrity: `ok`; foreign-key violations: zero.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 145 tests and 81 parameterized subtests pass.
- Astro: 511 files checked with zero errors, warnings or hints; 25,073 static
  pages built.
- Browser release suite: 90/90 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,073 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,145 artifacts; zero unexpected matches.
- Public manifest: 67 assets, 117,774,034 bytes, SHA-256
  `ec59662b6707f2060f07351ec493affd19f5e7d6dca3c446a106abcd5d2ffa86`.
- Two consecutive post-update output trees: 25,145 files, 327,109,218 bytes,
  SHA-256
  `b6f79b32be10dce973377a4dcea892651ebb50252e9db3296613851b516201f0`.
- Dependency audit: zero vulnerabilities after non-breaking updates.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,202/23,937 people (55.1531%).
- Verified affiliation: 956/23,937 people (3.9938%).
- Verified employer: 433/23,937 people (1.8089%).
- Archival disposition assessed: 11,669/23,937 people (48.7488%).
- Not started: 10,730 people; in progress: 1,893 people.
- Public projection: 23,937 profiles, 2,907 affiliations, 1,091
  organizations, 5,404 sources and 7,969 claims.

## Publication verification

Pending the content commit, clean Linux Test workflow, Pages deployment and
unauthenticated verification of the live GitHub Pages release.
