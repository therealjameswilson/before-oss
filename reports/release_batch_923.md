# Batch 923 release audit

Date: 2026-10-26 America/New_York

## Release contents

- NARA index page 452, rows 1-23: Carl A. Strahle through William J. Strauss.
- 23 immutable source rows, 23 separate person entities, 23 terminal research
  outcomes and 23 saved staged-protocol research attempt records.
- Nine accepted official Army identity bridges and one rejected protected-
  identifier conflict; no full protected identifier appears in public data.
- Arthur Mills Stratton's 1942-1944 Robert College teaching is documented as
  his immediate employment before joining OSS.
- Irving H. Strasmich's concurrent private law practice and Rhode Island tax-
  research role are strongly date-bounded before his Army entry without being
  forced into an unsupported sequence.
- Chester U. Strait's American Baptist missionary and educational work is
  documented prewar, not claimed as immediately pre-OSS.
- Eight qualified Army occupation or status categories identify no employer
  or institution. Ralph N. Stratis's rejected Army candidate remains visible
  as an identity conflict, with no candidate field transferred.
- Jean S. Strauss's former SAS/FAFL service is a qualified military antecedent,
  not civilian employment, and remains an archival-review question.
- The next boundary, William S. Strauss on page 452 row 24, was confirmed from
  the canonical source record.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 554 files checked with zero errors, warnings or hints; 25,142 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone and tablet,
  including 30 axe scans with no serious or critical violations.
- Internal links: 25,142 HTML files checked; all links resolve. The checker
  separately inventories 51,723 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,214 production artifacts; 1,406 candidate substrings
  inspected and zero unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 123,003,139 bytes, SHA-256
  `7b875176d864e915b06f14367e4dc729a0f393b6186c329f09af7ba0be6478fe`.
- Consecutive public trees: 70 files, 125,350,290 bytes, SHA-256
  `a914c7dca377b0fbd0fccc390e998a677667e25dd477cec2fde68a614b6403da`.
- Consecutive output trees: 25,214 files, 335,504,696 bytes, SHA-256
  `cc75db9a5631aee3a56d4d574bbd9487ddf374bced4228b1a34bdede7d191f46`.
- Production dependency audit: zero vulnerabilities. Five findings remain
  confined to the build/test toolchain; no Node dependency ships with the
  static site.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,178/23,936 people (59.2330%).
- Verified affiliation: 1,009/23,936 people (4.2154%).
- Verified employer: 455/23,936 people (1.9009%).
- Archival disposition assessed: 12,651/23,936 people (52.8534%).
- Not started: 9,753 people; in progress: 1,886 people.
- Possible-duplicate groups: 619; conflicts: 488.
- Claim confidence: 1,646 confirmed; 4,620 high; 2,017 medium; 242 low;
  410 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,252 affiliations, 1,159 organizations,
  5,769 sources and 8,689 claims.
- Evidence ledger: 7,039 citations across 3,862 unique source documents.

## Publication verification

Publication is pending the immutable content commit, successful GitHub Actions
Test and Pages workflows, and unauthenticated deployed-release verification.
Local generation and local QA do not by themselves establish publication.
