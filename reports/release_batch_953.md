# Batch 953 release audit

Date: 2026-10-28 America/New_York

## Release contents

- NARA index page 467, rows 1-23: William J Thompson through Ronald H
  Thornley. George Thornton on page 467, row 24 is the next cohort boundary.
- 23 immutable source rows, 23 separate people and one saved terminal research
  outcome for every person in the cohort.
- Ethel M Thornbury has two documented prewar academic employers, neither
  promoted to an immediate predecessor. Gordon P Thorigal has a documented
  Coast Guard Reserve pathway into OSS-attached swimmer units; it is a
  military assignment, not a civilian employer. Reginald Thorlin has
  documented Naval Academy student status and a Detachment 101 identity, with
  the intervening chronology and identifier discrepancy left for review.
- Four accepted Army bridges carry qualified historical occupation categories
  without employers or workplaces. An undefined occupation code was not
  interpreted, and a protected-identifier name conflict transfers no facts.
- Sixteen people retain explicit Box 775 or 776 archival-review outcomes after
  the staged online protocol. No authenticated NARA Catalog API request was
  used.
- The evidence-defined oil-company category remains unchanged at 14 people
  linked to 15 historically named companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `6d76852e7f39edaa5cfd13f49db631d2a002be4097ab26f124abce6670ce6128`.
- An isolated replay imports six review decisions, eight affiliations, 16
  claims, four organizations, 23 person updates, 23 research attempts, 12
  sources and 39 claim-source links; a second import is idempotent. SQLite
  integrity is ok and foreign-key violations are zero.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 584 files checked with zero errors, warnings or hints; 25,195 static
  pages built.
- Batch browser suite: 24/24 checks pass on desktop, phone and tablet.
- Browser release suite: 93/93 checks pass across desktop, phone, tablet and
  accessibility coverage, including 30 axe scans with no serious or critical
  violations.
- Internal links: 25,195 HTML files checked; all links resolve. The checker
  separately inventories 51,906 unique external URLs without claiming they
  were all live-tested in this release pass.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,267 public artifacts; 1,423 candidate substrings were
  inspected and there were zero unexpected boundary matches.
- Public manifest: 67 assets, 127,038,077 bytes, SHA-256
  `48120684b3cbfd2bee62112431282f1ef03504c16e4d01738d6c9937f0bb23a8`.
- Public tree: 70 files, 129,385,245 bytes, SHA-256
  `81a5c47c63d73e73e4706f76f48c864a7cba81b17d0cb50c2833fd86cf059a72`.
- Two consecutive output trees: 25,267 files and 412,984,366 bytes each, with
  identical SHA-256
  `bfbfea5f745d5ffb01fe4bd83381173be6547913f50448826af783eb860fea80`.
- Production dependency audit: zero vulnerabilities. Development tooling is
  not shipped with the static site.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 14,858/23,936 people (62.0739%).
- Verified affiliation: 1,053/23,936 people (4.3992%).
- Verified employer: 472/23,936 people (1.9719%).
- Archival disposition assessed: 13,334/23,936 people (55.7069%).
- Not started: 9,073 people; in progress: 1,883 people.
- Durable research attempts or plans: 29,076.
- Possible-duplicate groups: 648; conflicts: 514.
- Claim confidence: 1,662 confirmed; 4,894 high; 2,240 medium; 254 low;
  429 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,529 affiliations, 1,210 organizations,
  6,048 sources and 9,221 claims.
- Evidence ledger: 7,331 citations across 4,053 unique source documents.

## Publication verification

Publication is pending the immutable content commit, successful GitHub Test
and Pages workflows, and unauthenticated verification of the deployed
manifest, core routes and all 23 Batch 953 profile routes.
