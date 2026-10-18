# Batch 893 release audit

Date: 2026-10-18 America/New_York

## Release contents

- NARA index page 436, rows 24-46: William M Smith through Richard D Smyser.
- 23 terminal research outcomes and 23 new research-attempt records.
- Ten high-confidence identities, including seven accepted Army identity
  bridges; two materially conflicting Army candidates are rejected.
- William Arthur Smith's three documented earlier prewar work relationships are
  qualified because the evidence does not establish the immediate predecessor.
- Richard D Smyser's Penn State student affiliation and Edward Charles
  Smith-Ross's Royal Air Force assignment remain distinct from civilian
  employment.
- Andre Smolianinoff and Jane Smith-Hutton receive identity or OSS-context
  evidence only, without invented employer claims.
- The two Carl A Smollar source rows remain separate and visible in one possible-
  duplicate group; Army evidence is not transferred between them.

## Reproducible release checks

- SQLite integrity: ok; foreign-key violations: zero.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 146 tests and 84 parameterized subtests pass.
- Astro: 524 files checked with zero errors, warnings or hints; 25,091 static
  pages built.
- Browser release suite: 93/93 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,091 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,163 artifacts; zero unexpected matches.
- Public manifest: 67 assets, 119,086,141 bytes, SHA-256
  3a6622e202f39856a8c2d11aee30633e078585610a1afbcac36b37d0d3da21d0.
- Two consecutive public trees: 70 files, 121,433,292 bytes, SHA-256
  1afa54dc2b35923ab85c0951c3e22f9049a59f93a3d023e667d99e14a521c548.
- Two consecutive output trees: 25,163 files, 329,227,491 bytes, SHA-256
  bd35d0186f001709506be8cefdd7e69829b0b6130cafbc24e71b5a17393fd769.
- Production dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,497/23,937 people (56.3855%).
- Verified affiliation: 966/23,937 people (4.0356%).
- Verified employer: 435/23,937 people (1.8173%).
- Archival disposition assessed: 11,967/23,937 people (49.9937%).
- Not started: 10,435 people; in progress: 1,890 people.
- Public projection: 23,937 profiles, 2,988 affiliations, 1,109
  organizations, 5,492 sources and 8,167 claims.

## Publication verification

- Content commit:
  a35a53ba5822a6a07eb0ccb8d8f7b4ba1a0cf8cd.
- Clean Linux Test workflow: passed in run 39118699117:
  https://github.com/therealjameswilson/before-oss/actions/runs/39118699117
- GitHub Pages build and deploy: passed in run 39118699122:
  https://github.com/therealjameswilson/before-oss/actions/runs/39118699122
- Unauthenticated verification: all 67 manifest assets, eight core routes, 37
  source-register pages and all 23 directly affected profiles matched the
  immutable content commit at
  https://therealjameswilson.github.io/before-oss/.

GitHub emitted non-failing maintenance annotations that its Node 20-based
actions are currently being forced onto Node 24 and that ubuntu-latest is
scheduled to migrate to Ubuntu 26. Neither annotation changed the successful
release result.
