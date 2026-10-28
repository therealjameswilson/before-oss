# Batch 949 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 465, rows 1-23: Robert Thomale through Josephine Thomas.
  Lewis V. Thomas on row 24 is the next cohort boundary.
- 23 immutable source rows, 23 separate people and one saved research outcome
  for every person in the cohort.
- Allison K. Thomas's institutional history separates an explicit Army-to-OSS
  pathway from an earlier civilian occupation as a lawyer in Michigan. No law
  firm, employer or self-employed practice is inferred.
- Five accepted Army occupation categories remain qualified and unnamed.
  Albert Thomas's code 345 and Francis L. Thomas's code 070 are unassigned in
  the official code list, postdate the OSS period and remain unpublished as
  occupations.
- H. Gregory Thomas is not assigned to the initial-free Gregory Thomas index
  row without a corroborating identifier.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `7bd572394b23a95444000aef75f4fcb6a71d2f796f84a31abc24417ddc3aba89`.
- An isolated replay from the pre-Batch-949 backup imports all seven review
  decisions, seven affiliations, 15 claims, 23 person updates, 23 research
  attempts and 37 claim-source links; a second import is idempotent. SQLite
  integrity is ok and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 580 files checked with zero errors, warnings or hints; 25,194 static
  pages built.
- Batch browser suite: 15/15 checks pass on desktop, phone and tablet.
- Browser release suite: 84/84 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,194 HTML files checked; all links resolve. The checker
  separately inventories 51,898 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,266 public artifacts; 1,416 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 126,720,799 bytes, SHA-256
  `11eb29d21c27f1f1624f14f8ecdf96c174db36af4a9edd4674fe9023a1150dd3`.
- Public tree: 70 files, 129,067,952 bytes, SHA-256
  `0df503330cd2ae790f80c115e6a0314e4997f85f79c76e7b9f21517158b09692`.
- Two consecutive output trees: 25,266 files and 412,473,992 bytes each, with
  identical SHA-256
  `b9677636d9360e4a5342cd2ba91cef78af0d09471a481f7dddc59a0670839c26`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,767/23,936 people (61.6937%).
- Verified affiliation: 1,050/23,936 people (4.3867%).
- Verified employer: 471/23,936 people (1.9677%).
- Archival disposition assessed: 13,242/23,936 people (55.3225%).
- Not started: 9,164 people; in progress: 1,884 people.
- Durable research attempts or plans: 28,893.
- Possible-duplicate groups: 648; conflicts: 512.
- Claim confidence: 1,658 confirmed; 4,872 high; 2,226 medium; 252 low;
  428 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,509 affiliations, 1,209 organizations,
  6,022 sources and 9,180 claims.
- Evidence ledger: 7,301 citations across 4,035 unique source documents.

## Publication verification

Publication verification is pending the immutable content commit, successful
GitHub Test and Pages runs, and a manifest-level check of the unauthenticated
deployed site.
