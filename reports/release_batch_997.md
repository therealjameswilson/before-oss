# Batch 997 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 489, rows 1-23: Inovar A. Wallace through Michel Walon.
  Page 489, row 24, James B. Walsh, is the next cohort boundary.
- All 23 printed rows remain separate people and have saved terminal research
  outcomes: 5 `occupation_only_found`, 1 `needs_temporal_review`, 15
  `requires_archival_review` and 2 `verified_employer_found`.
- Identity disposition is 5 confirmed, 3 high-confidence and 15 unresolved
  people.
- Six official Army identity bridges were accepted. Five support only
  qualified historical occupation categories and no named employer or exact
  Army-to-OSS sequence. The sixth connects the indexed Inovar A. Wallace to
  Ingvar A. Wallace, but its November 1945 Army entry postdates the OSS and
  was not published as evidence of a pre-OSS occupation.
- Warrack Wallace has a high-confidence rare-name identity and two cited
  civilian affiliations: Baker & Daniels as his last civilian employer, and
  earlier work for Standard Oil Company in China. The oil organization remains
  explicitly entity-unspecified rather than being silently merged with a
  named subsidiary or successor.
- John Henry Waller has a high-confidence identity and an explicit immediate
  government assignment: the cited CIA release says that he joined OSS from
  the State Department in 1944. It is modeled as a government assignment, not
  a private employer.
- Michel Walon's printed French S/Lt. classification remains foreign or Allied
  commissioned-officer service.
- Tempting namesake biographies for Jean Browne Wallace, Paul Kimball Wallace
  and Helen Wallin were not assigned without a direct personnel-file bridge.
- No authenticated NARA Catalog API request was used.

## Reproducible local release checks

- Audited content commit:
  `796137efd47f8146f75c7875db63688d3228d61e`.
- Evidence-bundle SHA-256:
  `66d1653a883724f66a500630652d412eee6d6370500f9865b296e1eeb885a3cc`.
- Durable import: 6 sources, 3 organizations, 8 affiliations, 16 claims, 34
  claim-source links, 23 person updates and 23 research attempts.
- Batch claim confidence: 5 confirmed, 6 high and 5 medium; publication
  disposition is 11 normal claims and 5 qualified claims.
- Review decisions: six accepted official Army identity candidates.
- Complete ingest audit: every check passed for 23,978 rows and 522 pages.
- Stratified profile audit: every check passed for 200 profiles.
- Python: 149 tests passed with the CI-equivalent `unittest discover`
  command.
- Targeted Batch browser matrix: 33/33 checks passed across desktop, phone and
  tablet.
- Clean-archive browser release suite: 102/102 current-batch, core-route,
  analysis and accessibility checks passed, including 30 axe scans with no
  serious violations.
- Clean-archive Astro build: 628 files checked with zero diagnostics; 25,301
  canonical static pages built.
- Clean-archive internal links: 25,301 HTML files checked; all links resolve;
  52,243 unique external URLs were inventoried separately.
- Public identifier audit: the local and independent CI checks found zero
  aggregate, manifest-size or unexpected boundary matches in the public
  projection.
- Public manifest: 67 canonical assets, 133,630,959 bytes, SHA-256
  `08369e3ccae1094587a2330c6b33e852c5d24a2929dffb8d40ff85f95949b54d`.
- Public tree: 70 files, 135,978,115 bytes, SHA-256
  `cb6b7fe2e4e112a02d6120067f3b04bea77ccddf7f37bd49c703ea53cdf8d916`.
- Determinism: two consecutive clean builds reproduced 25,373 files,
  423,891,555 bytes and tree SHA-256
  `5b97b9c6dc99c7d3b00db81066a9b81224996272368bc282d185ae50692d6f9d`.
- Production dependency audit: zero vulnerabilities.
- GitHub noted non-blocking future runner-maintenance warnings for Node 20-
  based action internals and the `ubuntu-latest` image migration. No test,
  build, privacy-audit or deployment step failed.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,863/23,936 people (66.2726%).
- Verified affiliation: 1,145/23,936 people (4.7836%).
- Verified employer: 518/23,936 people (2.1641%).
- Archival disposition assessed: 14,338/23,936 people (59.9014%).
- Not started: 8,068 people; in progress: 1,883 people.
- Possible-duplicate groups: 679; conflicts: 535.
- Claim confidence: 1,752 confirmed; 5,357 high; 2,612 medium; 255 low;
  443 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 3,998 affiliations, 1,313
  organizations, 6,520 sources and 10,160 published, qualified or conflict
  claims.
- Citations: 7,807 across 4,357 unique source documents.

## Publication verification

- Immutable published release commit:
  `796137efd47f8146f75c7875db63688d3228d61e`.
- GitHub Actions Test run `41665142819` completed successfully at
  `2026-11-03T15:40:20Z`.
- GitHub Pages run `41665143145` completed successfully at
  `2026-11-03T15:36:18Z`.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and the Batch 997 evidence
  bundle. It verified all 67 public assets (133,630,959 bytes; manifest
  SHA-256
  `08369e3ccae1094587a2330c6b33e852c5d24a2929dffb8d40ff85f95949b54d`),
  all eight core routes, all 44 source-register pages and all 23 direct Batch
  997 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
