# Batch 937 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 459, rows 1-23: Dezso Szenes through Kengo Tajima.
- 23 immutable source rows, 23 separate people and 23 saved terminal research
  attempts.
- Three accepted official Army identity bridges. Two dated historical
  occupation categories are published as occupation evidence only, never as
  inferred employers or workplaces.
- Tadeuss Szumowski is a high-confidence spelling variant of Tadeusz
  Szumowski, with a qualified Polish Project Eagle military pathway.
- Anna G. Szynal's Becker College affiliation is explicitly modeled as student
  status, not employment.
- Tadami Tachino's 1942 Poston Camp 3 translator role is qualified and retains
  wartime-incarceration context; it is not promoted to an immediate pre-OSS
  affiliation without direct file evidence.
- Spiros T. Taflambas has waiter work preserved as his last stated civilian
  occupation before the 1942 draft and earlier grocery-delivery work, with no
  employer invented.
- Spencer L. Taggart has an explicit Justice Department Special War Policies
  Unit and Foreign Agents Registration Section pathway to OSS's Foreign
  Nationalities Branch.
- Masami Taiji is confirmed in a December 1944 Military Intelligence Service
  Language School class and Headquarters Company; his undefined Army code is
  left uninterpreted.
- Kengo Tajima remains ambiguous. A same-name pastor is not assigned to the
  indexed person without a direct Box 763 identity bridge.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 568 files checked with zero errors, warnings or hints; 25,172 static
  pages built.
- Batch browser suite: 36/36 checks pass on desktop, phone and tablet.
- Browser release suite: 105/105 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,172 HTML files checked; all links resolve. The checker
  separately inventories 51,812 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,244 public artifacts; 1,417 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 124,909,741 bytes, SHA-256
  `0798acdee71941ae133dd7e255ce1aff3bf5d076c41ce972daa25e237228b810`.
- Public tree: 70 files, 127,256,894 bytes, SHA-256
  `7b03aa4bb8c7d8e757ec3cb330c3ae6ffadc16d6fa5947ed11e1b5534f109708`.
- Two consecutive output trees: 25,244 files and 409,569,486 bytes each, with
  identical SHA-256
  `d3c7120384751ef97f3852294c39b9d4fd8ea57e48aac9ecc072cf4dfbe70087`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,495/23,936 people (60.5573%).
- Verified affiliation: 1,025/23,936 people (4.2823%).
- Verified employer: 463/23,936 people (1.9343%).
- Archival disposition assessed: 12,968/23,936 people (54.1778%).
- Not started: 9,436 people; in progress: 1,886 people.
- Durable research attempts or plans: 28,618.
- Possible-duplicate groups: 634; conflicts: 498.
- Claim confidence: 1,652 confirmed; 4,740 high; 2,127 medium; 252 low;
  419 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,383 affiliations, 1,188 organizations,
  5,896 sources and 8,934 claims.
- Evidence ledger: 7,175 citations across 3,950 unique source documents.

## Publication verification

Pending the immutable content commit, GitHub Actions Test and Pages runs, and
the unauthenticated public verifier.
