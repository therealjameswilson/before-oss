# Batch 809 release record

Date: 2026-10-15 America/New_York

## Scope

Batch 809 covers PDF page 394, rows 24-46, Warren D Robbins through H B
Roberts. All 23 printed rows remain preserved as source records and map to 23
active person entities. All 23 profiles have terminal attempted research
outcomes. The next indexed boundary is page 395, row 1, Henry B Roberts.

## Research outcome

- Exact private-identifier comparisons confirm official Army entry records for
  Felix W. Robbio and Eston J. Roberts. Their public identity claims omit full
  identifiers and coded occupations and do not imply an employer or immediate
  OSS predecessor.
- Joseph M. Roberto's exact identifier match points to a June 1946 Army entry
  date, after OSS dissolution. The public profile preserves the chronology
  problem and makes no employment, occupation, or immediate-affiliation claim.
- The PDF spelling `Authur P Roberta` remains authoritative. `Arthur P
  Roberta` is stored only as a documented search variant.
- H B Robert in Box 649 and H B Roberts in Box 650 remain separate unresolved
  entities; initials-only name similarity does not merge them.
- Jacques Robert-Rewez was rejected as an identity candidate because no source
  connects him to this Box 649 row or supplies corroborating identifiers.
- The indexed `French` notes remain uninterpreted. The other unresolved
  profiles direct researchers to Boxes 649-650 rather than claiming that no
  prior employer existed.
- NARA Catalog requests remained dry-run plans because no API key was available
  in the local process environment. Targeted CIA and Library of Congress
  adapter attempts failed after bounded handling. Neither access failure was
  counted as a negative historical result.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,938.
- Research attempted: 11,594/23,938 (48.4335%).
- Verified employer: 374/23,938 (1.5624%).
- Verified affiliation: 831/23,938 (3.4715%).
- Archival review assessed: 10,057/23,938 (42.0127%).
- Not started: 12,339.
- Possible duplicate groups: 552.
- Conflicts: 395.
- Claims: 1,436 confirmed; 3,631 high; 1,633 medium; 202 low; 339
  conflicting; two unresolved.
- Citations: 6,142 records representing 3,217 unique source documents.
- Public data: 2,665 published affiliations, 956 organizations, 4,917 public
  sources, and 7,035 published claims.
- Total saved research attempts and plans: 22,586.

## Local release gates

- Clean replay: the database, exports, and site were rebuilt from the source
  PDF, page-review bundles, adapter checkpoints, review decisions, and reviewed
  evidence bundles. Batch 809 reproduced 22 archival-review outcomes, one
  temporal-review outcome, and 23 non-planned research outcomes.
- Python: 141 tests and 81 subtests passed.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, 92 selected
  visual-QA pages, SQLite integrity, and foreign keys passed.
- Profile audit: all seven audit checks passed across a stratified sample of
  200 profiles.
- Astro: 443 source files checked with zero errors, warnings, or hints; 24,935
  HTML pages built.
- Browser: 93/93 desktop, phone, tablet, analysis, and accessibility checks
  passed: 24 Batch 809 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,935 generated HTML files passed internal-link checks; 51,072
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 25,007
  public artifacts, with zero aggregate or manifest false positives.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 111,648,118 bytes, SHA-256
  `aabc428393dce2598a7b6d747d7bf2d69c5a494c60a94c9710b8833ee2af6129`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `9f7307cdcafa6cc28f48907696912c7d98712160b280674799c665f0dedc63a6`
  across 70 files and 113,995,262 bytes, and production-tree SHA-256
  `3151fda6ce769d5d18e6d8a09eb7da2b1538c998a2ede86db0aebfa7f3050496`
  across 25,007 files and 317,162,632 bytes.

## Publication

Publication evidence will be added after the research commit, GitHub Pages
deployment, CI run, and immutable HTTPS verification all complete.

The full project remains unfinished: 12,339 active person entities remain
`not_started`. Research resumes at page 395, row 1, Henry B Roberts.
