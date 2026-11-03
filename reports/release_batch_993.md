# Batch 993 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 487, rows 1-23: Albert H. Waffle through James P. Waite.
  Page 487, row 24, Wilma Isabel Waite, is the next cohort boundary.
- All 23 printed rows remain separate people and have saved terminal research
  outcomes: 1 `completed`, 2 `documented_prewar_employer_found`, 5
  `occupation_only_found` and 15 `requires_archival_review`.
- Seven accepted official Army identity bridges support five qualified
  historical occupation or student categories. The post-OSS Army-entry dates
  for Richard D. Wagner and William E. Wagner are identity evidence only.
- A Boulder County preservation record directly links Siegfried Wagener to
  OSS and documents qualified Chicago Times and KFEL relationships.
- The official U.S. House biography documents Stuyvesant Wainwright's Yale-
  to-Army chronology and command of OSS units. Yale remains student status;
  the Army remains a military assignment.
- A University of Graz institutional biography supports a probable Ludwig
  Anton Wagner identity, qualified earlier employment at *Das Kleine Blatt*
  and a separate wartime Austrian exile affiliation. None is silently made an
  immediate OSS predecessor.
- Thirteen unresolved identities retain archival-review guidance and no
  invented affiliations.
- No authenticated NARA Catalog API request was used.

## Reproducible local release checks

- Audited content commit:
  `ba5591c4cf39df3f4d126a382f9fe535cb4ca542`.
- Evidence-bundle SHA-256:
  `fd7a0e35c11606c935ad6a01f6a04f0331e39cf89dc58625a5c68ea9091adccf`.
- Durable import: 8 sources, 6 organization updates, 11 affiliations, 22
  claims, 45 claim-source links, 23 person updates and 23 research attempts.
- Review decisions: seven accepted official Army identity candidates.
- Complete ingest audit: every check passed for 23,978 rows and 522 pages.
- Stratified profile audit: every check passed for 200 profiles.
- Python: 149 tests passed with the CI-equivalent `unittest discover`
  command.
- Targeted Batch browser matrix: 30/30 checks passed across desktop, phone and
  tablet.
- Clean-archive browser release suite: 99/99 current-batch, core-route,
  analysis and accessibility checks passed, including 30 axe scans with no
  serious violations.
- Clean-archive Astro build: 624 files checked with zero diagnostics; 25,295
  canonical static pages built.
- Clean-archive internal links: 25,295 HTML files checked; all links resolve;
  52,229 unique external URLs were inventoried separately.
- Clean-archive identifier audit: 12,926 normalized identifiers and 120
  formatted variants checked across 25,367 artifacts; 1,467 candidate
  substrings and zero unexpected matches.
- Public manifest: 67 canonical assets, 133,183,387 bytes, SHA-256
  `3d6b8aa24c6bc13d11bfd940472033fb3e7f31689e23f947bee4c2e003bd47e5`.
- Public tree: 70 files, 135,530,542 bytes, SHA-256
  `f311f60e8d0f12bc450c2673a6a6c48fc2b0e3a2aa6f3b16dbb7592688f1546d`.
- Determinism: two consecutive clean builds reproduced 25,367 files,
  423,152,243 bytes and tree SHA-256
  `15e1954fe7708368a2c200a5f4d74702ebaff780fcadb80b30227c948ea133ec`.
- Production dependency audit: zero vulnerabilities.
- GitHub noted non-blocking future runner-maintenance warnings for Node 20-
  based action internals and the planned `ubuntu-latest` image migration. No
  test, build or deployment step failed.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,771/23,936 people (65.8882%).
- Verified affiliation: 1,139/23,936 people (4.7585%).
- Verified employer: 516/23,936 people (2.1557%).
- Archival disposition assessed: 14,246/23,936 people (59.5170%).
- Not started: 8,160 people; in progress: 1,883 people.
- Possible-duplicate groups: 679; conflicts: 531.
- Claim confidence: 1,735 confirmed; 5,341 high; 2,586 medium; 255 low;
  439 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 3,965 affiliations, 1,307
  organizations, 6,496 sources and 10,097 published, qualified or conflict
  claims.
- Citations: 7,783 across 4,345 unique source documents.

## Publication verification

- Immutable published release commit:
  `ba5591c4cf39df3f4d126a382f9fe535cb4ca542`.
- GitHub Actions Test run `41646553063` completed successfully at
  `2026-11-03T13:46:41Z`.
- GitHub Pages run `41646553232` completed successfully; its deploy job
  completed at `2026-11-03T13:43:24Z`.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and the Batch 993 evidence
  bundle. It verified all 67 public assets (133,183,387 bytes; manifest
  SHA-256
  `3d6b8aa24c6bc13d11bfd940472033fb3e7f31689e23f947bee4c2e003bd47e5`),
  all eight core routes, all 44 source-register pages and all 23 direct Batch
  993 profile routes.
- Independent unauthenticated HTTP checks returned status 200 for the home
  page, the oil-company category, and the Siegfried Wagener, Stuyvesant
  Wainwright, Ludwig Anton Wagner and Harvey W. Wainwright profile pages.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
