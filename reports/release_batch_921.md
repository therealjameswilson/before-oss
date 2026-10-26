# Batch 921 release audit

Date: 2026-10-26 America/New_York

## Release contents

- NARA index page 451, rows 1-23: Franz T. Stone through William R. Stoppe.
- 23 immutable source rows, 23 separate person entities, 23 terminal research
  outcomes and 23 saved staged-protocol research attempt records.
- William R. Stoppe has one accepted official Army identity bridge and a
  qualified historical occupation category that names no employer.
- Norman Stone's conflicting-name Army candidate was rejected without field
  transfer.
- The two Franz T. Stone rows remain separate; their OPM and OSS namesake
  evidence is withheld until the adjacent personnel files can distinguish
  them.
- Kirk H. Stone's high-confidence COI/OSS identity and two prewar student
  affiliations are published without turning university attendance into
  employment.
- Oscar Stonorov's distinctive architect lead remains private and low
  confidence because no OSS-to-biography bridge was found.
- The next boundary, Robert G. Storey on page 451 row 24, was confirmed from
  the canonical source record.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests and 84 subtests pass.
- Astro: 552 files checked with zero errors, warnings or hints; 25,140 static
  pages built.
- Batch browser suite: 21/21 checks pass on desktop, phone and tablet.
- Browser release suite: 90/90 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,140 HTML files checked; all links resolve. The checker
  separately inventories 51,712 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,212 production artifacts; 1,404 candidate substrings
  inspected and zero unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 122,723,990 bytes, SHA-256
  `b254bf7c445336141199dcdeb9fe00e64531afce84d463d89ea3ca59e9a9e211`.
- Consecutive public trees: 70 files, 125,071,141 bytes, SHA-256
  `b9236ac7174a7e9a079c35285fe062cb3a6fabca6c35ae05c543a41251e6acc3`.
- Consecutive output trees: 25,212 files, 335,064,502 bytes, SHA-256
  `9f7ce099855011318e951b9af8e0d9157239388267e847439f16b509dfe2faa1`.
- Production dependency audit: zero vulnerabilities. Five findings remain
  confined to the build/test toolchain; no Node dependency ships with the
  static site.
- The CI-equivalent site validation ran from a `/private/tmp` clone containing
  the exact release working tree because the cloud-synced checkout's Astro
  diagnostic process did not return. Dependencies were installed from the
  local npm cache. This affected neither project files nor CI inputs.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,132/23,936 people (59.0408%).
- Verified affiliation: 1,005/23,936 people (4.1987%).
- Verified employer: 452/23,936 people (1.8884%).
- Archival disposition assessed: 12,605/23,936 people (52.6613%).
- Not started: 9,799 people; in progress: 1,886 people.
- Possible-duplicate groups: 619; conflicts: 486.
- Claim confidence: 1,646 confirmed; 4,596 high; 2,003 medium; 242 low;
  410 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,233 affiliations, 1,157 organizations,
  5,748 sources and 8,651 claims.
- Evidence ledger: 7,018 citations across 3,849 unique source documents.

## Publication verification

Publication identifiers and unauthenticated deployment-verification results
will be added after the GitHub Actions release completes.
