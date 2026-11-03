# Batch 1002 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 492, rows 1-46: Donald O. Waters through Lee J. Watters.
  All 46 printed rows remain separately recoverable.
- Every cohort person has a saved research attempt and a terminal review
  outcome: 36 `requires_archival_review`, 9 `occupation_only_found` and 1
  `conflicting_sources`.
- Identity disposition is 10 confirmed, 1 high-confidence, 1 conflicting and
  34 unresolved people.
- Ten official Army bulk-record bridges were accepted after exact-name and
  protected-identifier review. Nine public profiles preserve only the
  qualified historical occupation or student category recorded at Army
  entry. Oscar L. Watson's official code does not support an occupation, so
  his profile confirms only the identity bridge and requires archival review.
  No named employer, workplace, school or OSS-transfer date was inferred.
- Fred S. Watson Jr. remains conflicting because his protected identifier is
  also printed for a different index person. No Army identity or occupation
  was transferred, and the protected identifier remains private.
- A contemporary Congressional Record item and a Columbia University
  archival collection support a high-confidence Armitage Watkins identity
  and a qualified government assignment in Overseas Publications at the
  United States Office of War Information. The sequence relative to OSS is
  unresolved, so the profile does not call this an immediate predecessor.
- All 46 source rows were checked against layout-preserving text and an
  original-detail render. Relevant Army occupation-code pages were also
  inspected.
- No authenticated NARA Catalog API request was used.

## Reproducible release checks

- Audited content commit:
  `c1122ee26751d4ddcba33f3f20c6d824a1dece88`.
- Evidence-bundle SHA-256:
  `6b8a7c32c2abd29ff2973f5b4d8530f23c47cd7e17bcfeabb00c47f300208ca2`.
- Re-running the bundle generator reproduced the same evidence hash.
- Durable import: 6 sources, 1 organization input, 10 affiliations, 22
  claims, 53 claim-source links, 46 person updates and 46 research attempts.
- Batch claim confidence: 10 confirmed, 1 high, 10 medium and 1 conflicting.
  Publication disposition is 11 published, 10 qualified and 1 conflict claim.
- Review decisions: ten accepted and one conflicting official Army
  candidate.
- Python: 154 tests passed locally and in the independent GitHub Actions run.
- Checked-in public manifest: 67 canonical assets, 134,400,382 bytes,
  SHA-256
  `c63c496f24f1df8320c833593ef1779411ff776320d6a82644c6262c1edff3fe`.
- Clean GitHub Actions Astro check: zero errors, zero warnings and zero hints.
- Clean static build: 25,309 pages.
- Bounded browser release suite: 96/96 checks passed across desktop, phone and
  tablet: 27 latest-batch checks, 33 core-route and interaction checks, 6
  analysis checks, and 30 accessibility scans with no serious axe
  violations.
- Internal links: 25,309 HTML files checked; all links resolve. The checker
  inventoried 52,270 unique external URLs separately.
- Public identifier audit: 25,381 artifacts checked against 12,926 normalized
  private identifiers and 120 formatted variants. It found zero aggregate
  false positives, zero manifest-size false positives and zero unexpected
  boundary matches.
- Production dependency audit: zero vulnerabilities.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,024/23,936 people (66.9452%).
- Verified affiliation: 1,149/23,936 people (4.8003%).
- Verified employer: 521/23,936 people (2.1766%).
- Archival disposition assessed: 14,499/23,936 people (60.5740%).
- Not started: 7,907 people; in progress: 1,883 people.
- Research outcomes include 1,730 `occupation_only_found`, 8,807
  `requires_archival_review`, 437 `verified_employer_found`, 285
  `documented_prewar_employer_found` and 459 `conflicting_sources` people.
- Possible-duplicate groups: 679; conflicts: 539.
- Claim confidence: 1,788 confirmed; 5,374 high; 2,659 medium; 255 low;
  447 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 4,049 affiliations, 1,321
  organizations, 6,560 sources and 10,264 published, qualified or conflict
  claims.
- Citations: 7,847 across 4,381 unique source documents.

## Publication verification

- Immutable published release commit:
  `c1122ee26751d4ddcba33f3f20c6d824a1dece88`.
- GitHub Actions Test run `41710905304` completed successfully at
  `2026-11-03T20:21:36Z`.
- GitHub Pages run `41710905360` completed successfully at
  `2026-11-03T20:19:02Z`.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (134,400,382 bytes; manifest SHA-256
  `c63c496f24f1df8320c833593ef1779411ff776320d6a82644c6262c1edff3fe`),
  all eight core routes, all 44 source-register pages and all 46 direct Batch
  1002 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
