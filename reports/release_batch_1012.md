# Batch 1012 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 502, rows 1-46: Jack Whitley through Max Wiener. All 46
  printed rows remain separately recoverable as 46 cautious person entities.
- Every cohort person has a saved research attempt and terminal review outcome:
  30 `requires_archival_review`, 11 `occupation_only_found`, two
  `verified_employer_found`, two `documented_prewar_employer_found` and one
  `conflicting_sources`.
- Identity disposition is 11 confirmed, four high-confidence, one conflicting
  and 30 unresolved cohort people.
- Eleven exact-name, nonshared protected-identifier Army bridges received
  explicit acceptance review. The safely decoded historical occupation
  categories remain visibly qualified and are not converted into a named
  employer, workplace or exact OSS-transfer date.
- The page-502 Charles W. Whittaker and page-500 Charles W. Whitaker remain
  separate conflicting entities despite sharing a protected index identifier.
  The private identifier is not published.
- Contemporary official and institutional evidence documents Thomas Porter
  Whitney as a Bennett College social-sciences instructor before OSS analyst
  service without silently assigning a campus. George D. Whittinghill's State
  Department clerk and vice-consul roles remain documented civilian government
  service rather than an asserted immediate pre-OSS assignment.
- A direct May 1944 OSS personnel-board report confirms Robert B. Whittinghill
  and identifies his immediate military assignment as the Prisoner of War
  Section, G-2, AFHQ. His separate Time magazine and private-school teaching
  work is not ordered beyond the evidence.
- Derwent Stainthorpe Whittlesey's Harvard geography employment is documented
  prewar but not marked immediate.
- The bounded CIA adapter check was refused under the host's robots policy and
  the Library of Congress adapter check timed out. Both errors remain auditable
  and are not treated as negative search results.
- All 46 page-502 rows and relevant cited source pages were reviewed. No
  authenticated NARA Catalog API request was used.

## Reproducible release checks

- Audited content commit:
  `4396b0a1cd79a17f9b71af0d6c7bacc97b54f63f`.
- Evidence-bundle SHA-256:
  `71f87ec3ea4f8e6b298c65ac7358a8b53aea8d84d15708e0b04ba567c2b936a9`.
- Army/LoC review-decision SHA-256:
  `d0e65259cbdb389f4ba8f89c03bfcb73af82d12061a6d2caaa43877a74eb630e`.
- Durable import: ten sources, five organization inputs, 17 affiliations, 34
  claims, 46 person updates, 46 research attempts and 87 claim-source links.
  A second import produced identical database counts.
- Batch claim confidence: 14 confirmed, seven high, 12 medium and one
  conflicting. Publication disposition is 21 published, 12 visibly qualified
  and one conflict claim.
- Python: all 154 tests and 87 subtests passed locally.
- SQLite foreign-key, quick and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 136,654,118 bytes,
  SHA-256
  `171f95873611a522631e92890e01fede3a30734ae092593f98492c02e911f7b7`.
- Clean Astro check: 643 files with zero errors, warnings or hints.
- Clean static build: 25,336 pages.
- Bounded browser release suite: 96/96 checks passed across desktop, phone and
  tablet: 27 Batch 1012 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,336 HTML files checked; all links resolve. The checker
  inventoried 52,339 unique external URLs separately.
- Local public-identifier audit: 25,408 artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,555 candidate substrings and found zero aggregate, manifest-size or
  unexpected boundary matches.
- Two consecutive builds reproduced 25,408 artifacts and 428,907,914 bytes at
  output-tree SHA-256
  `4b1462589881e9362ac841f3a874acefc3d0c8989f7a38caf38d8b7c1ee5af8b`.
- The production dependency audit found zero vulnerabilities.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,480/23,935 people (68.8531%).
- Verified affiliation: 1,168/23,935 people (4.8799%).
- Verified employer: 533/23,935 people (2.2269%).
- Archival disposition assessed: 14,957/23,935 people (62.4901%).
- Not started: 7,450 people; in progress: 1,882 people.
- Research outcomes include 1,832 `occupation_only_found`, 9,130
  `requires_archival_review`, 448 `verified_employer_found`, 289
  `documented_prewar_employer_found` and 466 `conflicting_sources` people.
- Possible-duplicate groups: 688; conflicts: 546.
- Claim confidence: 1,873 confirmed; 5,438 high; 2,783 medium; 259 low;
  454 conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,210 affiliations, 1,348 organizations,
  6,648 sources and 10,544 published, qualified or conflict claims.
- Citations: 7,939 across 4,438 unique source documents.

## Publication verification

- Immutable published release commit:
  `4396b0a1cd79a17f9b71af0d6c7bacc97b54f63f`.
- GitHub Actions Test run
  [41783943486](https://github.com/therealjameswilson/before-oss/actions/runs/41783943486)
  completed successfully on 2026-11-04.
- GitHub Pages run
  [41783943435](https://github.com/therealjameswilson/before-oss/actions/runs/41783943435)
  completed successfully on 2026-11-04.
- On 2026-11-04, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (136,654,118 bytes; manifest SHA-256
  `171f95873611a522631e92890e01fede3a30734ae092593f98492c02e911f7b7`),
  all eight core routes, all 45 source-register pages and all 46 directly
  affected profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
