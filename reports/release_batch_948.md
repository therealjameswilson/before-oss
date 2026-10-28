# Batch 948 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 464, rows 24-46: Costas A. Theodorou through Corcoran
  Thom. Robert Thomale on page 465 is the next cohort boundary; this corrects
  the earlier Batch 947 handoff.
- 23 immutable source rows, 23 separate people and one saved terminal research
  outcome for every person in the cohort.
- Sotiris Theodorou's direct OSS board record separates an explicit Army-to-OSS
  pathway, civilian lawyer-and-contractor occupation and University of Athens
  student affiliation.
- Alphonse P. Thiele's direct OSS board record confirms recruitment from the
  Army at Camp Mackall and an earlier civilian machinist occupation without
  inventing an employer.
- Corcoran Thom's Riggs National Bank career is published only as the last
  civilian employer before wartime service; the exact OSS relationship remains
  a Box 772 archival-review question.
- Six accepted Army occupation categories remain qualified and unnamed.
  Edison P. Thibodeaux's code 993 is not interpreted.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `6b8722059835af89a88acd1c6f9616a1543972d9f3669cc7120fd734d52df6c3`.
- An isolated replay from the pre-Batch-948 backup imports all seven review
  decisions and 23 research outcomes; a second import is idempotent. SQLite
  integrity is ok and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 579 files checked with zero errors, warnings or hints; 25,194 static
  pages built.
- Batch browser suite: 21/21 checks pass on desktop, phone and tablet.
- Browser release suite: 90/90 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,194 HTML files checked; all links resolve. The checker
  separately inventories 51,897 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,266 public artifacts; 1,415 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 126,620,757 bytes, SHA-256
  `e320e86f8268a6ec0e79a127b8fc456c753fe282bbedb22fcb6130124ed83ea4`.
- Public tree: 70 files, 128,967,911 bytes, SHA-256
  `11269e01d5e37fcc79a3e1c20b0a173628b00ded8989f35fd3ecb0e1983e6982`.
- Two consecutive output trees: 25,266 files and 412,315,477 bytes each, with
  identical SHA-256
  `b8910ff32911ab0651950f65e59e227728e923b5edb55f907f4c4b71232c0574`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,745/23,936 people (61.6018%).
- Verified affiliation: 1,049/23,936 people (4.3825%).
- Verified employer: 471/23,936 people (1.9677%).
- Archival disposition assessed: 13,219/23,936 people (55.2264%).
- Not started: 9,186 people; in progress: 1,885 people.
- Durable research attempts or plans: 28,870.
- Possible-duplicate groups: 648; conflicts: 512.
- Claim confidence: 1,658 confirmed; 4,863 high; 2,220 medium; 252 low;
  428 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,502 affiliations, 1,209 organizations,
  6,016 sources and 9,165 claims.
- Evidence ledger: 7,295 citations across 4,033 unique source documents.

## Publication verification

Publication verification is pending the immutable content commit, GitHub Test
and Pages runs, and unauthenticated deployed-release comparison.
