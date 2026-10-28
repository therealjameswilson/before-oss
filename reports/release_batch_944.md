# Batch 944 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 462, rows 24-46: Ivan M. Tchok through Harry M. Templeton.
- 23 immutable source rows, 23 separate people and terminal outcomes for the
  full cohort; 22 new saved research attempts because Lucille E. Temple already
  had a completed protocol outcome.
- Ivan M. Tchok's documented legal practice and association leadership,
  Darwin L. Teilhet's Stanford teaching and Ina Telberg's Ohio State work are
  published only as earlier documented pre-OSS affiliations, not immediate or
  last-civilian predecessors.
- Six accepted Army matches publish qualified dated occupation or student-
  status categories without inventing employers, workplaces or schools.
- William J. Techtmann retains the Robert J. Mertes identifier/name conflict;
  no Army fields cross it. Three plausible namesake candidates remain
  unassigned, and Kate Teichner's printed number is not reinterpreted.
- Ten rows retain explicit Box 768 archival-review outcomes, including Lucille
  E. Temple's pre-existing completed protocol disposition.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle generation reproduces SHA-256
  `9dec51b03e99c853e30f45a1beb4a31bc854bcacfb17eb8a74f4bc3c92ba4d80`.
- An isolated replay from the pre-Batch-944 backup imports all seven review
  decisions and 22 new outcomes; a second import is idempotent. Its affiliation,
  claim, source, attempt and review-decision totals match the canonical SQLite
  database.
- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 575 files checked with zero errors, warnings or hints; 25,190 static
  pages built.
- Batch browser suite: 33/33 checks pass on desktop, phone and tablet.
- Browser release suite: 102/102 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,190 HTML files checked; all links resolve. The checker
  separately inventories 51,875 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,261 public artifacts; 1,421 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 125,994,995 bytes, SHA-256
  `6aa654b0a946c5127610ccf7d770fcb797174ad9dad2a505b2ceee4532ea481c`.
- Public tree: 70 files, 128,342,139 bytes, SHA-256
  `2094344b01d1693cfdd65b50a3d176131b5f4a983f3428b030c7a76612630d97`.
- Two consecutive output trees: 25,262 files and 411,322,724 bytes each, with
  identical SHA-256
  `e3ab630af4566244400bb51f8e6e9daddbfed61efc201c9249ab50d4ac305513`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,653/23,936 people (61.2174%).
- Verified affiliation: 1,042/23,936 people (4.3533%).
- Verified employer: 469/23,936 people (1.9594%).
- Archival disposition assessed: 13,127/23,936 people (54.8421%).
- Not started: 9,278 people; in progress: 1,885 people.
- Durable research attempts or plans: 28,778.
- Possible-duplicate groups: 641; conflicts: 511.
- Claim confidence: 1,654 confirmed; 4,817 high; 2,186 medium; 252 low;
  427 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,458 affiliations, 1,206 organizations,
  5,977 sources and 9,080 claims.
- Evidence ledger: 7,256 citations across 4,009 unique source documents.

## Publication verification

Batch 944 is public from immutable content commit
`89cd98fb87bbbb2d6c1eb13db9cc330239390baf`. GitHub Actions Test run
`40655154269` and Pages run `40655154277` completed successfully. The
unauthenticated verifier matched all **67** manifest assets across
**125,994,995** bytes at manifest SHA-256
`6aa654b0a946c5127610ccf7d770fcb797174ad9dad2a505b2ceee4532ea481c`,
plus eight core routes, 40 source-register pages and all 22 profiles changed
by the Batch 944 evidence bundle. Lucille E. Temple's profile was unchanged
because she already had a completed protocol outcome; her cohort route was
verified separately at HTTP 200 with the correct indexed-name heading. The
live statistics and oil-company category route also returned HTTP 200 and
matched the committed Batch 944 counters.
