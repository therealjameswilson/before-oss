# Batch 952 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 466, rows 24-46: Janet F Thompson through Theodore J
  Thompson. William J Thompson on page 467, row 1 is the next cohort boundary.
- 23 immutable source rows, 23 separate people and one saved terminal research
  outcome for every person in the cohort.
- Paul A Thompson has one accepted private-identifier bridge and a qualified
  dated Machinists occupation category. The historical category names no
  employer or workplace and is not treated as an immediate OSS predecessor.
- Folklorist Nancy Sweezy, born Nancy Thompson, remains a low-confidence,
  withheld candidate because the Box 775 common-name row lacks a second
  corroborating selector. No candidate variant, student affiliation or
  biographical fact is transferred to the indexed person.
- Twenty-one people retain explicit Box 774 or 775 archival-review outcomes
  after the staged online protocol. No authenticated NARA Catalog API request
  was used.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `f91ae16e49594b0634709cbb268281a1231afe1b337ec0d68630f46e69f8aa71`.
- An isolated replay imports the one review decision, one affiliation, three
  claims, no organizations, 23 person updates, 23 research attempts, seven
  sources and nine claim-source links; a second import is idempotent. SQLite
  integrity is ok and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests and 84 subtests pass.
- Astro: 583 files checked with zero errors, warnings or hints; 25,194 static
  pages built.
- Batch browser suite: 21/21 checks pass on desktop, phone and tablet.
- Browser release suite: 90/90 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,194 HTML files checked; all links resolve. The checker
  separately inventories 51,900 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,266 public artifacts; 1,418 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 126,906,754 bytes, SHA-256
  `95e423926709c69f317b050456c33653caae45f06cd73c829956b287f0f90bb0`.
- Public tree: 70 files, 129,253,910 bytes, SHA-256
  `fb1d799d775ecb9576db2f96b76a0919fe0aba787fa5a5ead4d66a5bd6d8ab3e`.
- Two consecutive output trees: 25,266 files and 412,775,625 bytes each, with
  identical SHA-256
  `00b74a9edf0e3f2c82efd09bd9f904f7ca2c0938633126a093fab7c189f0b8df`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,835/23,936 people (61.9778%).
- Verified affiliation: 1,050/23,936 people (4.3867%).
- Verified employer: 471/23,936 people (1.9677%).
- Archival disposition assessed: 13,311/23,936 people (55.6108%).
- Not started: 9,096 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,053.
- Possible-duplicate groups: 648; conflicts: 513.
- Claim confidence: 1,662 confirmed; 4,882 high; 2,236 medium; 254 low;
  429 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,521 affiliations, 1,209 organizations,
  6,036 sources and 9,205 claims.
- Evidence ledger: 7,319 citations across 4,044 unique source documents.

## Publication verification

Pending the immutable content commit, GitHub Actions checks, Pages deployment
and unauthenticated deployed-release verification.
