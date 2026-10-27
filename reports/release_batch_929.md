# Batch 929 release audit

Date: 2026-10-27 America/New_York

## Release contents

- NARA index page 455, rows 1-23: Mitsue M. Sugimachi through the first of
  three separately printed John L. Sullivan rows.
- 23 immutable source rows, 23 separate active person entities and 23 saved
  terminal research outcomes.
- Six accepted official Army identity bridges; no full protected identifier
  appears in public data.
- William G. Suhling is a high-confidence match to William Gerhard Suhling
  Jr. His 1939 presidency of Suhling & Co., Inc. is published as qualified
  earlier employment, not as an immediate affiliation or last civilian
  employer because the available source states no separation date.
- Yaemitsu Sugimachi's 1932 Rafu Shimpo reporting and a separate 1942
  teacher-status record remain qualified, probable-identity evidence. No
  school, employer after 1932 or OSS function is inferred.
- Mitsue M. Sugimachi's probable name expansion, Jacques Suissa's Allied
  mission service and Orman Suker's Field Artillery OCS chronology are
  preserved without converting them into unsupported employer claims.
- Army occupation categories for Joseph Suhovich, Albert F. Suitor, Edmund
  F. Sullivan, Francis L. Sullivan and Herbert M. Sullivan name no workplace,
  farm, school or employer. Boyd S. Sullivan's 1946 record is used for
  identity and classification only because it postdates OSS dissolution.
- The three consecutive John L. Sullivan rows remain separate. The first is
  flagged for joint Box 757 review; rows 24 and 25 remain not started for
  Batch 930.
- A David Sugimoto/Agar Company lead and common-name Sullivan biographies
  remain rejected discovery candidates for lack of a sufficient identity
  bridge.
- The oil-company category remains unchanged at 14 people linked to 15
  historically named companies.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass, plus 84 schema subtests.
- Astro: 560 files checked with zero errors, warnings or hints; 25,149 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,149 HTML files checked; all links resolve. The checker
  separately inventories 51,754 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,221 production artifacts; 1,409 candidate substrings were
  inspected. Aggregate and manifest-size false positives were classified
  separately and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 123,766,159 bytes, SHA-256
  `ae94f77cb01fbc7c25f9b189e3538ddb6b2edec99d1cbb72b8804887eb9309ab`.
- Public tree: 70 files, 126,113,296 bytes, SHA-256
  `092b90ae360bb61add8c3f2d2c719486dafeb16ac84ce429e8909f4fa555491c`.
- Two consecutive output trees: 25,221 files and 407,679,735 bytes each, with
  identical SHA-256
  `8c72ce5a533daaa01a283a0bf29bb650dd081d76a39fe4eba92de4765ade8a5a`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage at release candidate

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,314/23,936 people (59.8011%).
- Verified affiliation: 1,014/23,936 people (4.2363%).
- Verified employer: 458/23,936 people (1.9134%).
- Archival disposition assessed: 12,787/23,936 people (53.4216%).
- Not started: 9,617 people; in progress: 1,886 people.
- Durable research attempts or plans: 28,434.
- Possible-duplicate groups: 629; conflicts: 491.
- Claim confidence: 1,650 confirmed; 4,662 high; 2,067 medium; 252 low;
  413 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,303 affiliations, 1,166
  organizations, 5,820 sources and 8,788 claims.
- Evidence ledger: 7,099 citations across 3,901 unique source documents.

## Publication verification

Publication verification will be recorded after the immutable content commit
passes GitHub Actions and the unauthenticated deployment matches the committed
manifest and changed-profile set.
