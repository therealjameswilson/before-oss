# Batch 954 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 467, rows 24-46: George Thornton through Walter H Thurn.
  Arthur M Thurston on page 468, row 1 is the next cohort boundary.
- 23 immutable source rows, 23 separate people and one saved terminal research
  outcome for every person in the cohort.
- Eleven accepted Army identity bridges carry qualified dated historical
  categories. George Thornton is recorded only as a student; the other ten
  categories identify occupations but no employer or workplace. None is
  promoted to an immediate OSS predecessor or last civilian employer.
- Twelve people retain explicit Box 776 or 777 archival-review outcomes after
  the staged online protocol. Namesake leads and an unavailable CIA item were
  not substituted for inspected evidence. No authenticated NARA Catalog API
  request was used.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `fa753369eb5c973b0dbd6458a53bf069042cd41111930390e5fa297122aebdb3`.
- An isolated replay imports eleven review decisions, eleven affiliations, 22
  claims, 23 person updates, 23 research attempts, four sources and 55
  claim-source links; a second import is idempotent. SQLite integrity is ok
  and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 585 files checked with zero errors, warnings or hints; 25,195 static
  pages built.
- Batch browser suite: 21/21 checks pass on desktop, phone and tablet.
- Browser release suite: 90/90 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,195 HTML files checked; all links resolve. The checker
  separately inventories 51,906 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,267 public artifacts; 1,420 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 127,164,422 bytes, SHA-256
  `7dc3120a7313c8a32f884f5a7c0ec81522f2d00f528784dc3ae79521b2d735da`.
- Public tree: 70 files, 129,511,578 bytes, SHA-256
  `c21e325bea46089fd08f95bdce3d7deeca84034e2a9977a65bd4aecb7da5623a`.
- Two consecutive output trees: 25,267 files and 413,193,206 bytes each, with
  identical SHA-256
  `b3e31caaa20222ae89d6bf28042c9ab16aca5a55dec6cb4a61a72da30b0ef371`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,881/23,936 people (62.1700%).
- Verified affiliation: 1,053/23,936 people (4.3992%).
- Verified employer: 472/23,936 people (1.9719%).
- Archival disposition assessed: 13,357/23,936 people (55.8030%).
- Not started: 9,050 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,099.
- Possible-duplicate groups: 648; conflicts: 514.
- Claim confidence: 1,662 confirmed; 4,905 high; 2,251 medium; 254 low;
  429 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,540 affiliations, 1,210 organizations,
  6,052 sources and 9,243 claims.
- Evidence ledger: 7,335 citations across 4,054 unique source documents.

## Publication verification

Publication verification is pending the immutable content commit, successful
GitHub Test and Pages runs, and an unauthenticated comparison of the deployed
manifest and all 23 direct Batch 954 profile routes with that commit.
