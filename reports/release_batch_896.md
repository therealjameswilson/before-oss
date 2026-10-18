# Batch 896 release audit

Date: 2026-10-18 America/New_York

## Release contents

- NARA index page 438, rows 1-23: Herbert K Sokoloff through Francis F Sommer.
- 23 terminal research outcomes and 23 manual research-attempt records.
- Four accepted official Army identity bridges; protected identifiers remain
  private and the historical occupation codes are not converted into employers.
- The Harvy T Solee/Harvey T Selee and Robert M/N Somers identity conflicts
  remain visible without merging or transferring disputed occupations.
- Alexis Sommaripa is confirmed as OSS civilian personnel. His immediate Office
  of War Information assignment, last civilian employer DuPont, Army
  Quartermaster Board advisory work and Harvard student status remain distinct.
- McCord Sollenberger's visually checked law-school listing is published as
  student status, not employment.
- A postwar Donald M Soliday namesake is retained only as a rejected lead.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 146 tests and 84 parameterized subtests pass.
- Astro: 527 files checked with zero errors, warnings or hints; 25,095 static
  pages built.
- Browser release suite: 93/93 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,095 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,167 artifacts; zero unexpected matches.
- Public manifest: 67 assets, 119,489,581 bytes, SHA-256
  `67f7f39332aa05890af4d3e0aad2945a3769d8b543f7b0eb1eddb8e3a5545b4e`.
- Two consecutive public trees: 70 files, 121,836,731 bytes, SHA-256
  `fc20604d69a1bce43f605c5276f2006f2ba3b563fa6359a6d6d159beb3bdf30d`.
- Two consecutive output trees: 25,167 files, 329,855,390 bytes, SHA-256
  `77cb4300a103c9e1779ce717e32b8e826578bddca7168a93e773d3137fb92763`.
- Production dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,565/23,936 people (56.6720%).
- Verified affiliation: 973/23,936 people (4.0650%).
- Verified employer: 437/23,936 people (1.8257%).
- Archival disposition assessed: 12,036/23,936 people (50.2841%).
- Not started: 10,366 people; in progress: 1,889 people.
- Public projection: 23,936 profiles, 3,014 affiliations, 1,114
  organizations, 5,519 sources and 8,214 claims.

## Publication verification

Publication is pending the immutable content commit, clean GitHub Actions Test
run, successful GitHub Pages deployment and unauthenticated deployed-release
verification. Local validation alone does not establish publication.
