# Batch 995 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 488, rows 1-23: Richard D. Walk through Marjorie K.
  Walker. Page 488, row 24, Mary Virginia Walker, is the next cohort
  boundary.
- All 23 printed rows remain separate people and have saved terminal research
  outcomes: 4 `occupation_only_found`, 1 `conflicting_sources` and 18
  `requires_archival_review`.
- Identity disposition is 3 confirmed, 1 high-confidence, 1 conflicting and
  18 unresolved people.
- Four official Army identity bridges support only qualified historical
  occupation categories: architect; surveying chainman, rodman or axman;
  general-farm hand; and professional occupation not elsewhere classified.
  No named employer, workplace or exact Army-to-OSS sequence was inferred.
- Gordon A. Walker's indexed private identifier points to an Army record under
  a wholly different name. The candidate was rejected, all unrelated Army
  fields were withheld, and the public profile retains a visible identity
  conflict.
- A compatible 36th Division namesake lead for Fred L. Walker Jr. remained
  unassigned because no OSS, private-identifier or personnel-file bridge was
  found.
- Eighteen unresolved identities retain archival-review guidance and no
  invented affiliations.
- No authenticated NARA Catalog API request was used.

## Reproducible local release checks

- Audited content commit:
  `d2fcd80c1776faba3f5dcd940fed00fbf94eb799`.
- Evidence-bundle SHA-256:
  `77fe80266e796118ef38f0a9c213ce2602b2e8b13497c33a4c39f090b956df55`.
- Durable import: 4 sources, 0 organization updates, 4 affiliations, 9
  claims, 22 claim-source links, 23 person updates and 23 research attempts.
- Batch claim confidence: 3 confirmed, 1 high, 4 medium and 1 conflicting;
  publication disposition is 4 normal, 4 qualified and 1 conflict claim.
- Review decisions: four accepted and one rejected official Army identity
  candidate.
- Complete ingest audit: every check passed for 23,978 rows and 522 pages.
- Stratified profile audit: every check passed for 200 profiles.
- Python: 149 tests passed with the CI-equivalent `unittest discover`
  command.
- Targeted Batch browser matrix: 27/27 checks passed across desktop, phone and
  tablet.
- Clean-archive browser release suite: 96/96 current-batch, core-route,
  analysis and accessibility checks passed, including 30 axe scans with no
  serious violations.
- Clean-archive Astro build: 626 files checked with zero diagnostics; 25,299
  canonical static pages built.
- Clean-archive internal links: 25,299 HTML files checked; all links resolve;
  52,239 unique external URLs were inventoried separately.
- Clean-archive identifier audit: 12,926 normalized identifiers and 120
  formatted variants checked across 25,371 artifacts; 1,465 candidate
  substrings and zero unexpected matches.
- Public manifest: 67 canonical assets, 133,427,482 bytes, SHA-256
  `8b332d3a6832d5f8009c5d170a6ebf49ae09a16333a10a8b96bb8a8a2a9121b6`.
- Public tree: 70 files, 135,774,636 bytes, SHA-256
  `436f8be73280053aaf80d3b3d4d4d4043b95020e445a67b8daec3c2760d13437`.
- Determinism: two consecutive clean builds reproduced 25,371 files,
  423,552,384 bytes and tree SHA-256
  `aab15bd11e6b93df33c61722fb960accdba9bdb7fe4212fc09a608bce97ca963`.
- Production dependency audit: zero vulnerabilities.
- GitHub noted non-blocking future runner-maintenance warnings for Node 20-
  based action internals and the `ubuntu-latest` image migration. No test,
  build, privacy-audit or deployment step failed.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,817/23,936 people (66.0804%).
- Verified affiliation: 1,143/23,936 people (4.7752%).
- Verified employer: 517/23,936 people (2.1599%).
- Archival disposition assessed: 14,292/23,936 people (59.7092%).
- Not started: 8,114 people; in progress: 1,883 people.
- Possible-duplicate groups: 679; conflicts: 534.
- Claim confidence: 1,743 confirmed; 5,349 high; 2,601 medium; 255 low;
  442 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 3,984 affiliations, 1,311
  organizations, 6,510 sources and 10,131 published, qualified or conflict
  claims.
- Citations: 7,797 across 4,353 unique source documents.

## Publication verification

- Immutable published release commit:
  `d2fcd80c1776faba3f5dcd940fed00fbf94eb799`.
- GitHub Actions Test run `41655492917` completed successfully at
  `2026-11-03T14:42:47Z`.
- GitHub Pages run `41655492232` completed successfully; its deploy job
  completed at `2026-11-03T14:40:36Z`.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and the Batch 995 evidence
  bundle. It verified all 67 public assets (133,427,482 bytes; manifest
  SHA-256
  `8b332d3a6832d5f8009c5d170a6ebf49ae09a16333a10a8b96bb8a8a2a9121b6`),
  all eight core routes, all 44 source-register pages and all 23 direct Batch
  995 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
