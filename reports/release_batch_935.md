# Batch 935 release audit

Date: 2026-10-27 America/New_York

## Release contents

- NARA index page 458, rows 1-23: Paul M. Sweezy through Ardeth G. Swoyer.
- 23 immutable source rows, 23 separate people and 23 saved terminal research
  attempts.
- Six accepted official Army candidates and one rejected different-name
  candidate; no full protected identifier appears in tracked evidence, review
  decisions, generated data or downloads.
- Paul M. Sweezy row 1 is a high-confidence identity with Harvard University
  published as his last civilian employer before Army service and the U.S.
  Army as his immediate pre-OSS affiliation. The separately printed row 2
  remains separate and receives no copied claim.
- Carleton B. Swift is a high-confidence identity with a visible official
  `A` versus indexed `B`/Byron middle-initial discrepancy. Navy-to-OSS and
  Swift and Co.-to-Navy chronology claims are medium-confidence and visibly
  qualified because the explicit sequence currently depends on a family
  memorial.
- Five distinct historical Army occupation labels are published as dated
  occupation or student-status evidence, never as inferred employers.
- John W. Swensen retains the indexed spelling while the official Army
  `Swenson` spelling remains a documented variant requiring Box 761 review.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- SQLite integrity: ok; foreign-key violations: zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 566 files checked with zero errors, warnings or hints; 25,170 static
  pages built.
- Batch browser suite: 27/27 checks pass on desktop, phone and tablet.
- Browser release suite: 96/96 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,170 HTML files checked; all links resolve. The checker
  separately inventories 51,801 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,242 production artifacts; 1,414 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 124,650,026 bytes, SHA-256
  `b401edff3cbee82214e7bf02f0888e19017e2115683a7d7db90ed92980846f25`.
- Public tree: 70 files, 126,997,186 bytes, SHA-256
  `a248897bf7a10578b0e0b409a1ed2fc84b4016343d9c4c74b85bcaf74ce1d0ef`.
- Two consecutive output trees: 25,242 files and 409,157,260 bytes each, with
  identical SHA-256
  `34c7515ea208cfac706237c9e8ef9c0009b7567f4927df7c864c07091eb82bcb`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,449/23,936 people (60.3651%).
- Verified affiliation: 1,024/23,936 people (4.2781%).
- Verified employer: 463/23,936 people (1.9343%).
- Archival disposition assessed: 12,922/23,936 people (53.9856%).
- Not started: 9,482 people; in progress: 1,886 people.
- Durable research attempts or plans: 28,572.
- Possible-duplicate groups: 632; conflicts: 497.
- Claim confidence: 1,650 confirmed; 4,727 high; 2,109 medium; 252 low;
  419 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,366 affiliations, 1,186 organizations,
  5,872 sources and 8,901 claims.
- Evidence ledger: 7,151 citations across 3,934 unique source documents.

## Publication verification

Pending the immutable content commit, GitHub Actions results and
unauthenticated live manifest/profile verification. Local QA is not treated as
publication.
