# Batch 958 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 469, rows 24-43 and 45-46, plus page 470 row 1: Gordon
  R Tobin through N S Tokutaro. Hans V Tofte at page 469 row 44 was already
  completed and was not overwritten. W C Toland at page 470 row 2 is the next
  cohort boundary.
- All 23 researched source rows remain separate people and every person in the
  cohort has a saved terminal research outcome.
- Irwin M Tobin has a confirmed Office of War Information government pathway
  and separate Rhode Island State College civilian employer. Floyd C Tobrocke,
  Honey M Toda, Paul Harold Todd Jr., Borislav J Todorovic and Tokutaro
  Nishimura Slocum retain carefully typed student, employment, military,
  government and civic affiliations without collapsing them into employers.
- Gerard A Toby and Arthur F Todd have dated historical occupational
  categories without invented workplaces. The two Paul H Todd rows remain
  separate because their private identifiers differ; only row 41 receives the
  supported biography claims.
- Fifteen unresolved people retain explicit Box 779 or Box 780 archival-review
  outcomes. No authenticated NARA Catalog API request was used.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `3f86546d35304d738c63d942c7cfbd66a8172898ac2ed3098f67b1c2e9b0141f`.
- The durable import records three review decisions, 14 affiliations, 22
  claims, 23 person updates, 23 research attempts, 14 sources, 11
  organizations and 46 claim-source links; repeated imports are idempotent.
  SQLite integrity is ok and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 589 files checked with zero errors, warnings or hints; 25,206 static
  pages built.
- Batch browser suite: 24/24 checks pass on desktop, phone and tablet.
- Browser release suite: 93/93 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,206 HTML files checked; all links resolve. The checker
  separately inventories 51,946 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,278 public artifacts; 1,419 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 127,902,071 bytes, SHA-256
  `9e4a732ae70e52cda55fffe316138a0cde061c4453c75b5c7175663b56f048d0`.
- Public tree: 70 files, 130,249,231 bytes, SHA-256
  `cc267652e7e6a31baf75e8f24a33a5ed77f3a590d61a875566f07ea3c1426044`.
- Two consecutive output trees: 25,278 files and 414,382,660 bytes each, with
  identical SHA-256
  `e2860b958cc77548f4587466b9404f8b35850c93577133e016cec89715a7649e`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,972/23,936 people (62.5501%).
- Verified affiliation: 1,071/23,936 people (4.4744%).
- Verified employer: 479/23,936 people (2.0012%).
- Archival disposition assessed: 13,448/23,936 people (56.1832%).
- Not started: 8,959 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,190.
- Possible-duplicate groups: 650; conflicts: 514.
- Claim confidence: 1,678 confirmed; 4,961 high; 2,278 medium; 254 low;
  429 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,595 affiliations, 1,221 organizations,
  6,102 sources and 9,342 claims.
- Evidence ledger: 7,385 citations across 4,089 unique source documents.

## Publication verification

Pending immutable commit, CI, Pages deployment and unauthenticated live-release
verification.
