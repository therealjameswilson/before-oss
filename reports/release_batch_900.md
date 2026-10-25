# Batch 900 release audit

Date: 2026-10-25 America/New_York

## Release contents

- NARA index page 440, rows 1-23: Mildred S Spanum through John P Spence.
- 23 terminal research outcomes and 23 manual research-attempt records.
- Five accepted official Army identity bridges; their historical occupation
  or student categories remain qualified and name no employer or workplace.
- Two cross-row protected-identifier conflicts remain visible without merging
  people or transferring disputed evidence.
- Ephraim Speiser's University of Pennsylvania employment is published at high
  confidence while immediate chronology remains qualified and undated.
- The John P Spence combat-swimmer candidate remains private and withheld
  pending additional identity evidence.
- The next boundary, Marion J Spence on page 440 row 24, and the following
  same-identifier Deforest Spencer rows were visually confirmed.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 146 tests and 84 parameterized subtests pass.
- Astro: 531 files checked with zero errors, warnings or hints; 25,109 static
  pages built.
- Browser release suite: 90/90 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,109 HTML files checked; all links resolve. The checker
  separately inventories 51,596 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across the 70-file public tree and 25,181-file output tree; zero
  unexpected matches.
- Public manifest: 67 assets, 120,078,854 bytes, SHA-256
  `01e73e3be8c1a5da16aab808ccd4c5437217bbfc52ca2b5890c5e1e46112cd4e`.
- Two consecutive public trees: 70 files, 122,426,012 bytes, SHA-256
  `2356acfd36a1188035974270b8b30c03c03a5c55851d32390587ad18c6e1b93e`.
- Two consecutive output trees: 25,181 files, 330,819,394 bytes, SHA-256
  `470aece3eec796c09260d3a36dc0a388e36db5807deeda67388b89bacbe269a0`.
- Production dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,657/23,936 people (57.0563%).
- Verified affiliation: 979/23,936 people (4.0901%).
- Verified employer: 440/23,936 people (1.8382%).
- Archival disposition assessed: 12,128/23,936 people (50.6684%).
- Not started: 10,274 people; in progress: 1,889 people.
- Public projection: 23,936 profiles, 3,057 affiliations, 1,127
  organizations, 5,559 sources and 8,297 claims.

## Publication verification

Pending content commit, GitHub Actions, Pages deployment and unauthenticated
byte-for-byte verification. Local QA is not publication.
