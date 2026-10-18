# Batch 892 release audit

Date: 2026-10-18 America/New_York

## Release contents

- NARA index page 436, rows 1-23: Susan Smith through William W Smith.
- 23 terminal research outcomes and 23 new research-attempt records.
- Seven high-confidence Army identity bridges and seven medium-confidence,
  qualified occupation or student-status findings.
- One official OSS order independently corroborates Warren J Smith's identity
  and wartime assignment without being mislabeled as pre-OSS employment.
- One materially conflicting Army candidate for Warren D Smith is rejected.
- No new finding is mislabeled as an immediate affiliation, last civilian
  employer, named school or precise OSS-transfer sequence.
- The three Thomas R Smith source rows remain separate and visible in one
  possible-duplicate group; evidence is not transferred among rows.

## Reproducible release checks

- SQLite integrity: ok; foreign-key violations: zero.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 146 tests and 84 parameterized subtests pass.
- Astro: 523 files checked with zero errors, warnings or hints; 25,086 static
  pages built.
- Browser release suite: 93/93 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,086 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,158 artifacts; zero unexpected matches.
- Public manifest: 67 assets, 118,927,505 bytes, SHA-256
  6572aea17382d89bf728b39fb6ca355dbe1b1ecabee383db7a395f0375f886dd.
- Two consecutive public trees: 70 files, 121,274,656 bytes, SHA-256
  0e2929143e7c2c5dfbf7c88be9bdb19252066412831d3ed41dace456e36980ca.
- Two consecutive output trees: 25,158 files, 328,964,767 bytes, SHA-256
  c18617de102ac8d5ebc537f646d8c3eb453f0be70e3d533173599558ef38530b.
- Production dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,474/23,937 people (56.2894%).
- Verified affiliation: 964/23,937 people (4.0272%).
- Verified employer: 435/23,937 people (1.8173%).
- Archival disposition assessed: 11,944/23,937 people (49.8976%).
- Not started: 10,458 people; in progress: 1,890 people.
- Public projection: 23,937 profiles, 2,978 affiliations, 1,104
  organizations, 5,481 sources and 8,147 claims.

## Publication verification

- Content commit:
  c9e3ec08c8f9ba2a391ff3f1b7e836cd9605a85e.
- Clean Linux Test workflow: passed in run 39115957124:
  https://github.com/therealjameswilson/before-oss/actions/runs/39115957124
- GitHub Pages build and deploy: passed in run 39115957138:
  https://github.com/therealjameswilson/before-oss/actions/runs/39115957138
- Unauthenticated verification: all 67 manifest assets, eight core routes, 37
  source-register pages and all 23 directly affected profiles matched the
  immutable content commit at
  https://therealjameswilson.github.io/before-oss/.

GitHub emitted non-failing maintenance annotations that its Node 20-based
actions are currently being forced onto Node 24 and that ubuntu-latest is
scheduled to migrate to Ubuntu 26. Neither annotation changed the successful
release result.
