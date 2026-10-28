# Batch 936 release audit

Date: 2026-10-27 America/New_York

## Release contents

- NARA index page 458, rows 24-46: Edward D. Sybesma through Stanley F.
  Szalamacha.
- 23 immutable source rows, 23 separate people and 23 saved terminal research
  attempts.
- Six accepted official Army identity bridges. Five dated historical
  occupation categories are published as occupation evidence only, never as
  inferred employers or workplaces.
- John W. Syphax is a high-confidence identity with Howard University
  preserved as documented prewar employment. It is not marked immediate or
  last-civilian because the 1938-43 interval remains unaccounted for.
- Ganna M. Syro-Boiarsky has a probable rare-name identity and a qualified
  1940 secretary affiliation documented by a contemporary Treasury memo. No
  employing organization is invented from the source.
- Morris A. Syrstad is a confirmed identity with a qualified probable-immediate
  pathway through Headquarters, 99th Infantry, to the NORSO II roster. His
  undefined Army occupation code is left uninterpreted.
- Willem K. and William K. Sypesteyn remain separate in an opaque
  possible-duplicate group; evidence accepted for Willem is not transferred to
  William. Stephen and Stevan Sysko likewise remain separate.
- Stanley F. Szalamacha's Army candidate remains conflicting because its
  protected identifier belongs to a separately indexed, differently named
  person. No occupation is assigned and no protected identifier is published.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 567 files checked with zero errors, warnings or hints; 25,170 static
  pages built.
- Batch browser suite: 33/33 checks pass on desktop, phone and tablet.
- Browser release suite: 102/102 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,170 HTML files checked; all links resolve. The checker
  separately inventories 51,804 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 70 public artifacts; 946 candidate substrings were inspected
  and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 124,770,581 bytes, SHA-256
  `705689f110f65852baad3cf8d44e2f450095766c78ae9d13bee7b7df8ffa627a`.
- Public tree: 70 files, 127,117,728 bytes, SHA-256
  `f0063c9079967a579a4936171652591cc3d0a15d01fea808670b351d4e883f09`.
- Two consecutive output trees: 25,242 files and 409,348,436 bytes each, with
  identical SHA-256
  `7f17eae9c126b4c64e0d0a31a5fd4357dab824a7154dfc81a704bc2c9a6b23e9`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,472/23,936 people (60.4612%).
- Verified affiliation: 1,024/23,936 people (4.2781%).
- Verified employer: 463/23,936 people (1.9343%).
- Archival disposition assessed: 12,945/23,936 people (54.0817%).
- Not started: 9,459 people; in progress: 1,886 people.
- Durable research attempts or plans: 28,595.
- Possible-duplicate groups: 634; conflicts: 498.
- Claim confidence: 1,651 confirmed; 4,733 high; 2,118 medium; 252 low;
  419 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,374 affiliations, 1,186 organizations,
  5,882 sources and 8,917 claims.
- Evidence ledger: 7,161 citations across 3,939 unique source documents.

## Publication verification

Publication verification is pending the immutable content commit, successful
GitHub Actions Test and Pages runs, and an unauthenticated live-manifest check.
