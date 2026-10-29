# Batch 955 release audit

Date: 2026-10-29 America/New_York

## Release contents

- NARA index page 468, rows 1-23: Arthur M Thurston through Aaron L
  Tietelbaum. Francis E Tifft on row 24 is the next cohort boundary.
- 23 immutable source rows and 22 people. The two identical Philip D Tierney
  rows remain separately auditable and are cautiously linked to one person.
  Every person in the cohort has a saved terminal research outcome.
- Arthur M Thurston has one high-confidence documented earlier government
  assignment: FBI legal attaché at the American Embassy in London on 18 August
  1943. It is not presented as his immediate pre-OSS affiliation or civilian
  employer because the transfer chronology is not established.
- Nine accepted Army identity bridges carry qualified dated historical
  categories that identify no employer or workplace. Twelve people retain
  explicit Box 777 or 778 archival-review outcomes. A protected identifier
  conflict was rejected without transferring facts. No authenticated NARA
  Catalog API request was used.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `8580a4766e7646a151610050392cd2371dbfba92039b8e9c331002fa7e31b900`.
- An isolated replay imports eleven review decisions, ten affiliations, 20
  claims, 22 person updates, 22 research attempts, six sources, one reused
  organization and 49 claim-source links; a second import is idempotent.
  SQLite integrity is ok and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 586 files checked with zero errors, warnings or hints; 25,195 static
  pages built.
- Batch browser suite: 21/21 checks pass on desktop, phone and tablet.
- Browser release suite: 90/90 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,195 HTML files checked; all links resolve. The checker
  separately inventories 51,908 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,267 public artifacts; 1,421 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 127,287,954 bytes, SHA-256
  `59ada5c84a4ed6b1ece258aaf0054d46d2e6c58ab638236e52af47f5e9f9ebf6`.
- Public tree: 70 files, 129,635,113 bytes, SHA-256
  `13113d11a53e0d6fadb9a981d8d570831d184b1a95b1c3de3f09537d280046a6`.
- Two consecutive output trees: 25,267 files and 413,393,563 bytes each, with
  identical SHA-256
  `d76cb452774517b7f3434d8b44212608c852cad20d789b69572acaa0dd3f40e1`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,903/23,936 people (62.2619%).
- Verified affiliation: 1,054/23,936 people (4.4034%).
- Verified employer: 472/23,936 people (1.9719%).
- Archival disposition assessed: 13,379/23,936 people (55.8949%).
- Not started: 9,028 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,121.
- Possible-duplicate groups: 648; conflicts: 514.
- Claim confidence: 1,662 confirmed; 4,916 high; 2,260 medium; 254 low;
  429 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,550 affiliations, 1,210 organizations,
  6,058 sources and 9,263 claims.
- Evidence ledger: 7,341 citations across 4,057 unique source documents.

## Publication verification

Publication is pending. Local validation does not by itself establish that
GitHub Actions passed or that the unauthenticated public site serves this
release. Record the immutable content commit, Test run, Pages run and deployed
manifest verification here after those checks succeed.
