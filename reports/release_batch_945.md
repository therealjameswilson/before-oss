# Batch 945 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 463, rows 1-23: Kenneth S. Templeton through William B.
  Terrell.
- 23 immutable source rows, 23 separate people and one saved terminal research
  outcome for every person in the cohort.
- Edward A. Tenenbaum's Yale student status and Army Air Forces service remain
  distinct from civilian employment and from an explicit immediate
  predecessor.
- Helen B. Tenny's probable Helen B. Tenney identity and 1942 Short Wave
  Research-to-OSS sequence remain visibly qualified and excluded from default
  employer analytics.
- Lazare Teper row 11 has documented earlier ILGWU employment, but the separate
  row 12 person receives none of that evidence. Ethel M. Terhaar's probable
  University of Minnesota employment also remains qualified and earlier only.
- Four accepted Army matches publish qualified dated occupation categories
  without inventing employers or workplaces. Fifteen rows retain explicit Box
  768 or 769 archival-review outcomes.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `38cedf6e3ea6584b2f84f72a4c6b85200e131a516a71e6c844910186ae9b3a87`.
- An isolated replay from the pre-Batch-945 backup imports all four review
  decisions and 23 research outcomes; a second import is idempotent. Its
  affiliation, claim, source, attempt and review-decision totals match the
  canonical SQLite database.
- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 576 files checked with zero errors, warnings or hints; 25,191 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,191 HTML files checked; all links resolve. The checker
  separately inventories 51,885 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,262 public artifacts; 1,417 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 126,152,987 bytes, SHA-256
  `b09f2cf10288560d672c2694fba15f3a6c1958f7a9c3d5d3186359ce0eca03eb`.
- Public tree: 70 files, 128,500,142 bytes, SHA-256
  `54bf23dd065a38f0814cf666b3697d121e7aca3e046f4fe96fa4d1b4d6777e0d`.
- Two consecutive output trees: 25,263 files and 411,567,844 bytes each, with
  identical SHA-256
  `86c40a2c8dac3abb8b79f1fcf5faedca0f5d8754b56f23ee851c031c6eddaea3`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,676/23,936 people (61.3135%).
- Verified affiliation: 1,044/23,936 people (4.3616%).
- Verified employer: 470/23,936 people (1.9636%).
- Archival disposition assessed: 13,150/23,936 people (54.9382%).
- Not started: 9,255 people; in progress: 1,885 people.
- Durable research attempts or plans: 28,801.
- Possible-duplicate groups: 642; conflicts: 511.
- Claim confidence: 1,654 confirmed; 4,825 high; 2,194 medium; 252 low;
  427 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,467 affiliations, 1,207 organizations,
  5,990 sources and 9,096 claims.
- Evidence ledger: 7,269 citations across 4,019 unique source documents.

## Publication verification

Pending the immutable Git commit, GitHub Actions Test and Pages runs, and
unauthenticated public-manifest verification.
