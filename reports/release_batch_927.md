# Batch 927 release audit

Date: 2026-10-26 America/New_York

## Release contents

- NARA index page 454, rows 1-23: Richard W. Stubbs through Anton M.
  Sturrett.
- 23 immutable source rows, 23 separate active person entities and 23 saved
  terminal research outcomes.
- Ten accepted official Army identity bridges; no full protected identifier
  appears in public data.
- Milburn H. Stuckwish's contemporary radio-trade notice identifies WSOY as
  his last civilian employer before Signal Corps service. The Signal Corps is
  separately modeled as a qualified probable immediate military pathway.
- Eight dated Army occupation or status findings identify no named employer,
  school, mine, farm or workplace.
- The two Andre Studler rows retain their different protected identifiers,
  remain separate and are visibly linked. A museum biography naming work at
  an unidentified distillery is retained as a low-confidence candidate and is
  not published against either person.
- Official Army occupation codes 093 and 993 remain uninterpreted rather than
  being forced into unsupported categories.
- The next boundary, Donald B. Sturtevant on page 454 row 24, was confirmed
  from the canonical source record.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 558 files checked with zero errors, warnings or hints; 25,145 static
  pages built.
- Batch browser suite: 24/24 checks pass on desktop, phone and tablet.
- Browser release suite: 93/93 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,145 HTML files checked; all links resolve. The checker
  separately inventories 51,738 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,217 production artifacts; 1,413 candidate substrings
  inspected and zero unexpected boundary, aggregate or manifest-size matches.
- Public manifest: 67 assets, 123,516,034 bytes, SHA-256
  `f2f6a7578a9ab593cd6bc2c57da242d4ff12b3b9f4ce4d13183ade19f59f8b97`.
- Public tree: 70 files, 125,863,189 bytes, SHA-256
  `d326ada0561377c52ff3458a75a9ba079ca55ff45f0783283586693400b62de4`.
- Two consecutive output trees: 25,217 files and 407,271,383 bytes each, with
  identical SHA-256
  `89d15b36121fc4f207ddb310a07ff70929a160a73b09cd7fc5216049ffbdfc77`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,268/23,936 people (59.6090%).
- Verified affiliation: 1,013/23,936 people (4.2321%).
- Verified employer: 457/23,936 people (1.9093%).
- Archival disposition assessed: 12,741/23,936 people (53.2294%).
- Not started: 9,663 people; in progress: 1,886 people.
- Possible-duplicate groups: 627; conflicts: 491.
- Claim confidence: 1,649 confirmed; 4,648 high; 2,052 medium; 251 low;
  413 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,289 affiliations, 1,162 organizations,
  5,797 sources and 8,758 claims.
- Evidence ledger: 7,076 citations across 3,887 unique source documents.

## Publication verification

- Batch 927 is public from immutable content commit
  `dae5cc806266d7ff589c92cfe35c1084b66a4e5a`.
- GitHub Actions Test run `40445289395` completed successfully, including the
  147-test Python suite, committed-manifest verification, browser release suite
  and public-identifier audit.
- GitHub Pages run `40445289430` completed successfully.
- The unauthenticated deployment verifier matched all 67 assets and
  123,516,034 bytes to the committed manifest SHA-256
  `f2f6a7578a9ab593cd6bc2c57da242d4ff12b3b9f4ce4d13183ade19f59f8b97`.
  It also verified eight core routes, 39 source-register pages and all 23
  profiles changed by the evidence bundle.
- The live statistics asset reports the exact release-candidate counts above.
  Public site: <https://therealjameswilson.github.io/before-oss/>.
