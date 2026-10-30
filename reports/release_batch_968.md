# Batch 968 release audit

Date: 2026-10-30 America/New_York

## Release contents

- NARA index page 474, rows 24-46: Michalis Tsirmulas through Margaret E
  Tugas. Gaston E Tuggle at page 475, row 1 is the next cohort boundary.
- All 23 source rows remain separate people and have saved terminal research
  outcomes: 11 occupation-only outcomes and 12 archival-review outcomes.
- Direct and authoritative evidence records military, government, student and
  civilian-occupation pathways without turning them into unsupported employer
  claims. This batch establishes no new named employer.
- Seven accepted Army identity bridges contribute only qualified occupation,
  student or military evidence. No authenticated NARA Catalog API request was
  used.
- The oil-company category remains 14 people linked to 15 historically named
  companies.

## Reproducible local release checks

- Evidence-bundle SHA-256:
  `a3d757b130db4e76193f17d498c74b9259fa8eccfbb177add691909e525a61f3`.
- Durable import: 14 sources, 3 organization inputs, 14 affiliations, 25
  claims, 59 claim-source links, 23 person updates and 23 research attempts;
  repeated imports are idempotent.
- PDF extraction validation: 23,978 rows across 522 pages; all checks pass.
- Stratified profile audit: 200/200 profiles pass every check.
- Python: 147 tests pass.
- Astro: 599 files checked with zero errors, warnings or hints; 25,237 static
  pages built.
- Browser release suite: 99/99 checks pass, including 30 axe scans with no
  serious or critical violations.
- Internal links: 25,237 HTML files checked; all links resolve.
- Identifier audit: 12,926 normalized identifiers and 120 formatted variants
  checked across 25,309 public artifacts; zero unexpected boundary matches.
- Dependency audit: zero vulnerabilities.
- Public manifest: 67 assets, 129,586,516 bytes, SHA-256
  `597416f9aa0a914f979bdaac5fec3697dfd30935ce57de564b97d1c01261050a`.
- Public tree: 70 files, 131,933,688 bytes, SHA-256
  `0a73c5f3d9aee92fd978a2ab828d2cc65ad9fe55f918d2e84a4ff09302e06280`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,200/23,936 people (63.5027%).
- Verified affiliation: 1,094/23,936 people (4.5705%).
- Verified employer: 488/23,936 people (2.0388%).
- Archival disposition assessed: 13,676/23,936 people (57.1357%).
- Not started: 8,731 people; in progress: 1,883 people.
- Claim confidence: 1,705 confirmed; 5,070 high; 2,394 medium; 254 low;
  433 conflicting; 2 unresolved.
- Public projection: 23,936 profiles, 3,726 affiliations, 1,251 organizations,
  6,230 sources and 9,598 claims.
- Evidence ledger: 7,514 citations across 4,172 unique source documents.

## Replay disclosure

- Batch 968 evidence and review decisions replay idempotently.
- The older global replay limitation disclosed in Batch 959 remains: 473
  pre-Batch-959 person-level research-status changes are not yet represented in
  durable replay inputs. The current integrity-checked database remains
  authoritative for the public projection.

## Publication verification

Publication is pending the immutable content commit, GitHub Actions checks and
unauthenticated deployed-release verification.
