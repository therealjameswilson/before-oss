# Batch 946 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 463, rows 24-46: Henry W. Terrett through Erika Teutsch.
- 23 immutable source rows, 23 separate people and one saved terminal research
  outcome for every person in the cohort.
- Erika Teutsch's Swarthmore class-of-1944 status remains a qualified student
  pathway to a documented OSS stint, not a civilian employer.
- Adrian Terzian and Leo P. Tetrealt retain their documented spelling variants.
  The Leo evidence is isolated to the protected row; the separate unprotected
  Leo P. Tetrault row receives none of it.
- Henry W. Terrett retains a visible middle-initial conflict and receives no
  Army occupation from the Henry M. Terrett record.
- Eleven accepted Army matches publish qualified dated occupation or student-
  status categories without inventing employers, workplaces or schools. Five
  rows retain explicit Box 769 or 770 archival-review outcomes.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `243513a8165b7d740ee7175d24d30be2ad789f8a72f14097ce64a322d7336f63`.
- An isolated replay from the pre-Batch-946 backup imports all 12 review
  decisions and 23 research outcomes; a second import is idempotent. Its
  affiliation, claim, source, attempt and review-decision totals match the
  canonical SQLite database.
- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 577 files checked with zero errors, warnings or hints; 25,191 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,191 HTML files checked; all links resolve. The checker
  separately inventories 51,888 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,263 public artifacts; 1,417 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 126,320,435 bytes, SHA-256
  `99847538ed10e1ea8ad3fdd8ad58d2bb282d010abc669b18cee3aeaf9f3ae9cf`.
- Public tree: 70 files, 128,667,593 bytes, SHA-256
  `2deb55ad5a2808172d90dd28cca814c4f097bb11fd3d144e817b9b04eb0b0ff0`.
- Two consecutive output trees: 25,263 files and 411,833,553 bytes each, with
  identical SHA-256
  `734bb784f0ac84cb168636d18d3739d656022156a3f844dd8218371c9cb97076`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,699/23,936 people (61.4096%).
- Verified affiliation: 1,044/23,936 people (4.3616%).
- Verified employer: 470/23,936 people (1.9636%).
- Archival disposition assessed: 13,173/23,936 people (55.0343%).
- Not started: 9,232 people; in progress: 1,885 people.
- Durable research attempts or plans: 28,824.
- Possible-duplicate groups: 645; conflicts: 512.
- Claim confidence: 1,654 confirmed; 4,837 high; 2,206 medium; 252 low;
  428 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,479 affiliations, 1,207 organizations,
  5,998 sources and 9,121 claims.
- Evidence ledger: 7,277 citations across 4,023 unique source documents.

## Publication verification

Pending the immutable Git commit, GitHub Actions Test and Pages runs, and
unauthenticated public-manifest verification.
