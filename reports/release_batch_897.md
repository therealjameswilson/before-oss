# Batch 897 release audit

Date: 2026-10-18 America/New_York

## Release contents

- NARA index page 438, rows 24-46: Henry Sonagere through Dario Soria.
- 23 terminal research outcomes and 23 manual research-attempt records.
- Five accepted official Army identity bridges; protected identifiers remain
  private and the historical occupation codes are not converted into employers.
- The Edgar/Brown and Daniel A Sorensen/Robert W Sorenson identity conflicts
  remain visible without merging or transferring disputed occupations.
- Henry Sonagere's 82nd Airborne pathway, Gunnar Sønsteby's Norwegian
  employment and resistance chronology, Karl G Sorg's Dartmouth student status
  and Dario Soria's qualified commercial and broadcasting history remain
  distinct and confidence-aware.
- The next boundary, Gene Sorisi on page 439 row 1, was visually confirmed.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 146 tests and 84 parameterized subtests pass.
- Astro: 528 files checked with zero errors, warnings or hints; 25,101 static
  pages built.
- Browser release suite: 96/96 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,101 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,173 artifacts; zero unexpected matches.
- Public manifest: 67 assets, 119,682,986 bytes, SHA-256
  `491a35104138b56e8452f146b23162b16093cff3113875d5d0f9a0987243c1e4`.
- Two consecutive public trees: 70 files, 122,030,133 bytes, SHA-256
  `076a0ba928ab8b79180009bdcb2f890e7b3c6d748b32e5b16aae6d0a880143fa`.
- Two consecutive output trees: 25,173 files, 330,175,095 bytes, SHA-256
  `eabbd18672e13ee896e81f3db87d75400207a9dc3e0da971f8f1c0f91702f53f`.
- Production dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,588/23,936 people (56.7680%).
- Verified affiliation: 976/23,936 people (4.0775%).
- Verified employer: 438/23,936 people (1.8299%).
- Archival disposition assessed: 12,059/23,936 people (50.3802%).
- Not started: 10,343 people; in progress: 1,889 people.
- Public projection: 23,936 profiles, 3,031 affiliations, 1,120
  organizations, 5,530 sources and 8,242 claims.

## Publication verification

Content commit, GitHub Actions Test, Pages deployment and unauthenticated live
verification are pending. Local validation does not by itself establish a
public release.
