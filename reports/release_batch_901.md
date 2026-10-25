# Batch 901 release audit

Date: 2026-10-25 America/New_York

## Release contents

- NARA index page 440, rows 24-46: Marion J Spence through Jerome Sperling.
- 23 immutable source rows, 22 person entities, 22 terminal research outcomes
  and 22 manual research-attempt records.
- Four accepted official Army identity bridges; their historical occupation or
  student categories remain qualified and name no employer or workplace.
- The two Deforest Spencer rows remain one cautiously resolved person with both
  printed source rows preserved.
- The two Harry G Sperling rows remain separate; art-dealer and disputed Army
  evidence stays withheld.
- Edmond Speraber's medical practice and Jerome Sperling's Yale University
  employment are published at high confidence, with immediate chronology
  visibly qualified.
- The next boundary, Ann Sperry on page 441 row 1, and the following same-name
  cluster were visually confirmed.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 146 tests and 84 parameterized subtests pass.
- Astro: 532 files checked with zero errors, warnings or hints; 25,111 static
  pages built.
- Browser release suite: 96/96 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,111 HTML files checked; all links resolve. The checker
  separately inventories 51,603 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across the 70-file public tree and 25,183-file output tree; zero
  unexpected matches.
- Public manifest: 67 assets, 120,236,337 bytes, SHA-256
  `d72d5297c33e4d16528c564238426d689ed9f75478fed3a69d261ae97a133d4b`.
- Two consecutive public trees: 70 files, 122,583,482 bytes, SHA-256
  `6c6878cf6ba72e685ea05d2f3a13a1b7bdc0426bddbdcb9f172ee23f19747353`.
- Two consecutive output trees: 25,183 files, 331,065,210 bytes, SHA-256
  `69283804d60d18617803f348f12230098f09e61159ed2a921290f527893a3adf`.
- Production dependency audit: zero vulnerabilities.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 13,679/23,936 people (57.1482%).
- Verified affiliation: 981/23,936 people (4.0984%).
- Verified employer: 442/23,936 people (1.8466%).
- Archival disposition assessed: 12,150/23,936 people (50.7604%).
- Not started: 10,252 people; in progress: 1,889 people.
- Public projection: 23,936 profiles, 3,064 affiliations, 1,129
  organizations, 5,571 sources and 8,315 claims.

## Publication verification

Publication is pending the immutable content commit, GitHub Actions tests,
Pages deployment and unauthenticated deployed-release verification.
