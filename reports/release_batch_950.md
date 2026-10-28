# Batch 950 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 465, rows 24-46: Lewis V Thomas through Allen J Thompson.
  Austin H Thompson on page 466, row 1, is the next cohort boundary.
- 23 immutable source rows, 23 separate people and one saved terminal research
  outcome for every person in the cohort.
- Lorres C Thomas is confirmed as Lorres Charles Thomas. His West Point cadet
  status and Corps of Engineers commission remain separate student and military
  relationships with uncertain temporal relation to OSS service.
- Paul P Thomle is confirmed from an official Army casualty record without
  inferring an employer, affiliation or OSS sequence from casualty status.
- Three accepted Army occupation categories remain qualified and unnamed.
- Eighteen unresolved people retain explicit archival-review outcomes; rare or
  later namesakes are not assigned without a defensible identity bridge.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `ab6b8420d750fa7b1cb1acbcb519daeba2afb84338d54eff8715a0d847ec7518`.
- An isolated replay from the pre-Batch-950 backup imports all three review
  decisions, five affiliations, ten claims, two reused organizations, 23 person
  updates, 23 research attempts, six sources and 21 claim-source links; a
  second import is idempotent. SQLite integrity is ok and foreign-key
  violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 581 files checked with zero errors, warnings or hints; 25,194 static
  pages built.
- Batch browser suite: 18/18 checks pass on desktop, phone and tablet.
- Browser release suite: 87/87 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,194 HTML files checked; all links resolve. The checker
  separately inventories 51,900 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,266 public artifacts; 1,416 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 126,794,986 bytes, SHA-256
  `20d6ff6ca588757727707ef1380adc97b8c4941c14a37d9547a353411a5e029d`.
- Public tree: 70 files, 129,142,142 bytes, SHA-256
  `93177c123b637a00298d696e4e29958ba4d127696a4e141d7a5615a3cbffd4ee`.
- Two consecutive output trees: 25,266 files and 412,593,432 bytes each, with
  identical SHA-256
  `db832602b1d6c2e88fde3b5008c51d3cd4b317540ededbc4b02fac2bd1685b36`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,790/23,936 people (61.7898%).
- Verified affiliation: 1,050/23,936 people (4.3867%).
- Verified employer: 471/23,936 people (1.9677%).
- Archival disposition assessed: 13,265/23,936 people (55.4186%).
- Not started: 9,141 people; in progress: 1,884 people.
- Durable research attempts or plans: 28,916.
- Possible-duplicate groups: 648; conflicts: 512.
- Claim confidence: 1,662 confirmed; 4,875 high; 2,229 medium; 252 low;
  428 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,514 affiliations, 1,209 organizations,
  6,028 sources and 9,190 claims.
- Evidence ledger: 7,307 citations across 4,038 unique source documents.

## Publication verification

Publication verification is pending the immutable content commit, successful
GitHub Test and Pages runs, and an unauthenticated manifest and direct-profile
check against the deployed commit.
