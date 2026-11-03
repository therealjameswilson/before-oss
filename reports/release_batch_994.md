# Batch 994 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 487, rows 24-46: Wilma Isabel Waite through Everett G.
  Walk. Page 488, row 1, Richard D. Walk, is the next cohort boundary.
- All 23 printed rows remain separate people and have saved terminal research
  outcomes: 4 `completed`, 2 `conflicting_sources`, 1
  `documented_prewar_employer_found`, 2 `occupation_only_found`, 13
  `requires_archival_review` and 1 `verified_employer_found`.
- Identity disposition is 4 confirmed, 2 high-confidence, 2 probable, 2
  conflicting and 13 unresolved people. The Carl O. Walden and James E.
  Walden rows share a printed private identifier but remain separate conflict
  records pending joint archival review.
- Eugene Merse Waith has a verified Yale University civilian-employment claim
  and a separately modeled Army-to-OSS pathway. Nancy Wake, George O.
  Walbridge, Patrick Waldberg and Herbert F. Waldhorn retain their documented
  civilian, military, government and resistance relationships without
  collapsing them into generic employer claims.
- Three reviewed official Army identity bridges support qualified historical
  occupation categories for Richard P. Wakefield, Maturin F. Waldo and James
  A. Waldron. An unbridged official OSS historian named John Waldron was
  rejected rather than assigned to the common-name index row.
- Thirteen unresolved identities retain archival-review guidance and no
  invented affiliations.
- No authenticated NARA Catalog API request was used.

## Reproducible local release checks

- Audited content commit:
  `e2f62142ca63cc207990682c64ecc3e494890038`.
- Evidence-bundle SHA-256:
  `8bae779e47345c64b95fd942ad3c0d82a62c9800685cececfa57085baa7c83fe`.
- Durable import: 10 sources, 11 organization updates, 15 affiliations, 25
  claims, 43 claim-source links, 23 person updates and 23 research attempts.
- Batch claim confidence: 5 confirmed, 7 high, 11 medium and 2 conflicting;
  publication disposition is 12 published, 11 qualified and 2 conflict
  claims.
- Review decisions: three accepted official Army identity candidates.
- Complete ingest audit: every check passed for 23,978 rows and 522 pages.
- Stratified profile audit: every check passed for 200 profiles.
- Python: 149 tests passed with the CI-equivalent `unittest discover`
  command.
- Targeted Batch browser matrix: 30/30 checks passed across desktop, phone and
  tablet.
- Clean-archive browser release suite: 99/99 current-batch, core-route,
  analysis and accessibility checks passed, including 30 axe scans with no
  serious violations.
- Clean-archive Astro build: 625 files checked with zero diagnostics; 25,299
  canonical static pages built.
- Clean-archive internal links: 25,299 HTML files checked; all links resolve;
  52,239 unique external URLs were inventoried separately.
- Clean-archive identifier audit: 12,926 normalized identifiers and 120
  formatted variants checked across 25,371 artifacts; 1,467 candidate
  substrings and zero unexpected matches.
- Public manifest: 67 canonical assets, 133,357,302 bytes, SHA-256
  `cd499c30a75610d6b81f80145a16333b4192498f97f5e2ed552a41708f0f5c7c`.
- Public tree: 70 files, 135,704,458 bytes, SHA-256
  `7e745cf73a0d6be4a56eab4027dc351603b7a280f4fe1ba21e4b002a688653df`.
- Determinism: two consecutive clean builds reproduced 25,371 files,
  423,437,541 bytes and tree SHA-256
  `a65443831e6ddf5418afa6a943e5097f727013dd51f80d9cea362d4e0a5e4a5a`.
- Production dependency audit: zero vulnerabilities.
- GitHub noted non-blocking future runner-maintenance warnings for Node 20-
  based action internals and the `ubuntu-latest` image migration. No test,
  build, privacy-audit or deployment step failed.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,794/23,936 people (65.9843%).
- Verified affiliation: 1,143/23,936 people (4.7752%).
- Verified employer: 517/23,936 people (2.1599%).
- Archival disposition assessed: 14,269/23,936 people (59.6131%).
- Not started: 8,137 people; in progress: 1,883 people.
- Possible-duplicate groups: 679; conflicts: 533.
- Claim confidence: 1,740 confirmed; 5,348 high; 2,597 medium; 255 low;
  441 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 3,980 affiliations, 1,311
  organizations, 6,506 sources and 10,122 published, qualified or conflict
  claims.
- Citations: 7,793 across 4,352 unique source documents.

## Publication verification

- Immutable published release commit:
  `e2f62142ca63cc207990682c64ecc3e494890038`.
- GitHub Actions Test run `41650764493` completed successfully at
  `2026-11-03T14:13:42Z`.
- GitHub Pages run `41650764409` completed successfully; its deploy job
  completed at `2026-11-03T14:10:29Z`.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and the Batch 994 evidence
  bundle. It verified all 67 public assets (133,357,302 bytes; manifest
  SHA-256
  `cd499c30a75610d6b81f80145a16333b4192498f97f5e2ed552a41708f0f5c7c`),
  all eight core routes, all 44 source-register pages and all 23 direct Batch
  994 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
