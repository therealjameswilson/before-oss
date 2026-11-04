# Batch 1025 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 515, rows 1-46: Mundy P. Wright through Hans Wyner. All
  46 printed rows remain separately recoverable as 46 cautious person
  entities.
- Every cohort person has a saved terminal outcome: 29
  `requires_archival_review`, eight `occupation_only_found`, three
  `completed`, two `verified_employer_found`, two
  `documented_prewar_employer_found`, and two `conflicting_sources`.
- Ten protected-identifier Army candidates were accepted, two shared-identifier
  candidates remain conflicting and unmerged, and one damaged-name candidate
  was rejected. Full identifiers remain private.
- John H. Wuorinen's contemporaneous Columbia annual-report evidence supports
  Columbia University employment and his OSS Scandinavian-Baltic Section role.
- Hans Wynberg's Pfizer civilian employment remains separate from his U.S.
  Army-to-OSS pathway. The Wijnberg spelling is preserved as a documented
  variant.
- Betty Jane Wylie's General Mills claim is published as medium-confidence,
  explicit-immediate evidence pending a personnel or employer record.
- Richard D. Wylly's official Marine Corps evidence is modeled as a military
  assignment, not as civilian employment.
- The separately printed Robert C. Wright and Robert G. Wright rows remain
  visible as a protected-identifier conflict and were not merged.
- No authenticated NARA Catalog API request was used.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,070/23,935 people (71.3182%).
- Verified affiliation: 1,197/23,935 people (5.0010%).
- Verified employer: 550/23,935 people (2.2979%).
- Archival disposition assessed: 15,551/23,935 people (64.9718%).
- Not started: 6,860 people; in progress: 1,879 people.
- Research outcomes include 1,955 `occupation_only_found`, 9,554
  `requires_archival_review`, 462 `verified_employer_found`, 295
  `documented_prewar_employer_found`, 604 `needs_identity_review`, and 479
  `conflicting_sources` people.
- Claim confidence: 2,009 confirmed; 5,530 high; 2,922 medium; 261 low; 465
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,395 affiliations, 1,378 organizations,
  6,765 sources, and 10,922 published, qualified, or conflict claims.
- Citations: 8,058 across 4,521 unique source documents.

## Local publication verification

- Evidence-bundle SHA-256:
  `9a1608977c9b88ed0791bfdf38a1fed14f7a7b20345fab931a1ccf396795ee5a`.
- The evidence bundle validates without exposing secrets, full identifiers, or
  raw bulk records.
- Python: all 154 unittest cases passed. The Batch 1025 generator's six focused
  tests and the complete schema validation are included.
- SQLite foreign-key, integrity, and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 139,543,342 bytes,
  SHA-256
  `099d48abc78ca6db547d37317de33b5d44eab0e5cafe4bc8457c8d939897ff87`.
- Clean Astro check: 656 files with zero errors, warnings, or hints.
- Clean static build: 25,367 pages.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1025 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,367 HTML files checked; all links resolve. The checker
  inventoried 52,435 unique external URLs separately.
- Public-identifier audit: 25,439 public artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,581 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,439 artifacts at output-tree
  SHA-256
  `0e3381e871ba47b37e50e239812810e32aa9f28986a7d5e53068e74ffb90bedf`.
- The production dependency audit found zero vulnerabilities.

## Public deployment verification

- Published from commit
  `4fc9e9662472f6bd788a869c4106bbaaeab1160b`.
- The Test workflow completed successfully in GitHub Actions run
  [41863299677](https://github.com/therealjameswilson/before-oss/actions/runs/41863299677).
- The Deploy GitHub Pages workflow completed successfully in run
  [41863299917](https://github.com/therealjameswilson/before-oss/actions/runs/41863299917).
- An immutable live check against that exact commit verified 67 manifest assets
  totaling 139,543,342 bytes, all eight core routes, all 46 source-register
  pages, and all 45 distinct direct profile routes represented by the 46-row
  batch. The public manifest SHA-256 was
  `099d48abc78ca6db547d37317de33b5d44eab0e5cafe4bc8457c8d939897ff87`.
- Verified public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
