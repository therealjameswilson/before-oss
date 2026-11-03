# Batch 996 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 488, rows 24-46: Mary Virginia Walker through Elery P.
  Wallace. Page 489, row 1, Inovar A. Wallace, is the next cohort boundary.
- All 23 printed rows remain separate people and have saved terminal research
  outcomes: 6 `occupation_only_found`, 1 `conflicting_sources`, 15
  `requires_archival_review` and 1 `blocked_by_source_access`.
- Identity disposition is 4 confirmed, 2 high-confidence, 1 conflicting and
  16 unresolved people.
- Six official Army identity bridges support only qualified historical
  occupation or student-status categories: student; secondary-school teacher
  or principal; general-farm hand; actor; student; and photographer. No named
  employer, workplace or exact Army-to-OSS sequence was inferred.
- Raymond E. Walker's indexed private identifier points to an Army record
  under a wholly different name. The candidate was rejected, all unrelated
  Army fields were withheld, and the public profile retains a visible identity
  conflict.
- An official NSA search index exposed a strong Robert N. Walker candidate,
  but direct retrieval of the underlying PDF returned an access-denied page.
  The access restriction was not bypassed, the search snippet was not admitted
  as final evidence, and no claim or affiliation was published from it.
- Adjacent Robert M. Walker index rows remain separate; only the row supported
  by the accepted official Army bridge received derived fields.
- Fifteen other unresolved identities retain archival-review guidance and no
  invented affiliations.
- No authenticated NARA Catalog API request was used.

## Reproducible local release checks

- Audited content commit:
  `448d1bdf71e09abe883e6e191a5ba014f3c99bae`.
- Evidence-bundle SHA-256:
  `260d5fbc1e50ba6df23ff5a54e69d18588d8547e5c93cdb7205eb2b09e35543e`.
- Durable import: 4 sources, 0 organization updates, 6 affiliations, 13
  claims, 32 claim-source links, 23 person updates and 23 research attempts.
- Batch claim confidence: 4 confirmed, 2 high, 6 medium and 1 conflicting;
  publication disposition is 6 normal identity claims, 6 qualified
  occupation or student-status claims and 1 conflict claim.
- Review decisions: six accepted and one rejected official Army identity
  candidate.
- Complete ingest audit: every check passed for 23,978 rows and 522 pages.
- Stratified profile audit: every check passed for 200 profiles.
- Python: 149 tests passed with the CI-equivalent `unittest discover`
  command.
- Targeted Batch browser matrix: 30/30 checks passed across desktop, phone and
  tablet.
- Clean-archive browser release suite: 99/99 current-batch, core-route,
  analysis and accessibility checks passed, including 30 axe scans with no
  serious violations.
- Clean-archive Astro build: 627 files checked with zero diagnostics; 25,299
  canonical static pages built.
- Clean-archive internal links: 25,299 HTML files checked; all links resolve;
  52,239 unique external URLs were inventoried separately.
- Clean-archive identifier audit: 12,926 normalized identifiers and 120
  formatted variants checked across 25,371 artifacts; 1,470 candidate
  substrings and zero unexpected matches.
- Public manifest: 67 canonical assets, 133,516,556 bytes, SHA-256
  `dad013f191b9e4d5f0853d919bc052afeb04ca25fda02bd5128ab04a57bc9953`.
- Public tree: 70 files, 135,863,716 bytes, SHA-256
  `5d7d9b91f5bf802ccb643b2207ab2a38fe995e697ce9671f95842d4ae342fdd0`.
- Determinism: two consecutive clean builds reproduced 25,371 files,
  423,698,608 bytes and tree SHA-256
  `e3c27d29625c96a4fe5979daf8f11b682ea9cd9aa855e219cee0e5d647704f61`.
- Production dependency audit: zero vulnerabilities.
- GitHub noted non-blocking future runner-maintenance warnings for Node 20-
  based action internals and the `ubuntu-latest` image migration. No test,
  build, privacy-audit or deployment step failed.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,840/23,936 people (66.1765%).
- Verified affiliation: 1,143/23,936 people (4.7752%).
- Verified employer: 517/23,936 people (2.1599%).
- Archival disposition assessed: 14,315/23,936 people (59.8053%).
- Not started: 8,091 people; in progress: 1,883 people.
- Possible-duplicate groups: 679; conflicts: 535.
- Claim confidence: 1,747 confirmed; 5,351 high; 2,607 medium; 255 low;
  443 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 3,990 affiliations, 1,311
  organizations, 6,514 sources and 10,144 published, qualified or conflict
  claims.
- Citations: 7,801 across 4,354 unique source documents.

## Publication verification

- Immutable published release commit:
  `448d1bdf71e09abe883e6e191a5ba014f3c99bae`.
- GitHub Actions Test run `41659659470` completed successfully at
  `2026-11-03T15:08:03Z`.
- GitHub Pages run `41659659252` completed successfully at
  `2026-11-03T15:05:10Z`.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and the Batch 996 evidence
  bundle. It verified all 67 public assets (133,516,556 bytes; manifest
  SHA-256
  `dad013f191b9e4d5f0853d919bc052afeb04ca25fda02bd5128ab04a57bc9953`),
  all eight core routes, all 44 source-register pages and all 23 direct Batch
  996 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
