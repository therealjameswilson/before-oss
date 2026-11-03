# Batch 998 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 489, rows 24-46: James B. Walsh through Lenore B.
  Walters. Page 490, row 1, Robert E. Walters, is the next cohort boundary.
- All 23 printed rows remain separate people and have saved terminal research
  outcomes: 3 `occupation_only_found` and 20 `requires_archival_review`.
- Identity disposition is 3 confirmed and 20 unresolved people.
- Three official Army identity bridges were accepted: John P. Walsh, Billy H.
  Walter and Carroll R. Walters. They support only qualified historical
  occupation categories (machinist, chauffeur or driver, and general-farm
  hand respectively), not named employers or an immediate Army-to-OSS
  sequence.
- Robert B. Walter's printed `PhM 1/c, USNR` entry is now classified as
  enlisted naval personnel. The transparent normalization repair also
  upgraded seven other source rows with Pharmacy Mate variants, affecting
  seven people in total including Walter.
- Tempting namesake material for Louis A. Walsh Jr., Richard L. Walsh, William
  B. Walsh and other Walter or Walters candidates was rejected when the
  identifier, chronology, occupation or available context did not establish
  the indexed person.
- Exact-name CIA Reading Room searches and staged web, obituary,
  institutional and Library of Congress searches produced no additional
  publishable employer or identity evidence for this cohort.
- No authenticated NARA Catalog API request was used.

## Reproducible local release checks

- Audited content commit:
  `ba92121419bd8cad3179b5a71e12ca127bd80634`.
- Evidence-bundle SHA-256:
  `e9982b2e5c0700ab09170089c71972b1bd930fb5ee42802f509ab2613826bd06`.
- Durable import: 4 sources, 0 organizations, 3 affiliations, 6 claims, 15
  claim-source links, 23 person updates and 23 research attempts.
- Batch claim confidence: 3 confirmed and 3 medium; publication disposition
  is 3 normal identity claims and 3 qualified occupation claims.
- Review decisions: three accepted official Army identity candidates.
- Complete ingest audit: every check passed for 23,978 rows and 522 pages.
- Stratified profile audit: every check passed for 200 profiles.
- Python: 150 tests passed with the CI-equivalent `unittest discover`
  command.
- Targeted Batch browser matrix: 21/21 checks passed across desktop, phone and
  tablet.
- Clean-archive browser release suite: 90/90 current-batch, core-route,
  analysis and accessibility checks passed, including 30 axe scans with no
  serious violations.
- Clean-archive Astro build: 629 files checked with zero diagnostics; 25,301
  canonical static pages built.
- Clean-archive internal links: 25,301 HTML files checked; all links resolve;
  52,243 unique external URLs were inventoried separately.
- Public identifier audit: the local and independent CI checks found zero
  aggregate, manifest-size or unexpected boundary matches in the public
  projection.
- Public manifest: 67 canonical assets, 133,688,539 bytes, SHA-256
  `7cf2f4ec4de27880db371d7ca09be860b2e9e670434dffa39ddb2027ecb2ac01`.
- Public tree: 70 files, 136,035,690 bytes, SHA-256
  `14c0ad29e643a9d9ce00059894f3a99af10d4f201f173d077d10da874abbdfcd`.
- Determinism: two consecutive clean builds reproduced 25,373 files,
  423,984,655 bytes and tree SHA-256
  `15fda92a8deef980a6ff49c33b82f33cd31985d38af36f61e8b97f59360cc3f0`.
- Production dependency audit: zero vulnerabilities.
- GitHub noted non-blocking future runner-maintenance warnings for Node 20-
  based action internals and the `ubuntu-latest` image migration. No test,
  build, privacy-audit or deployment step failed.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 15,886/23,936 people (66.3686%).
- Verified affiliation: 1,145/23,936 people (4.7836%).
- Verified employer: 518/23,936 people (2.1641%).
- Archival disposition assessed: 14,361/23,936 people (59.9975%).
- Not started: 8,045 people; in progress: 1,883 people.
- Research outcomes include 1,699 `occupation_only_found` and 8,709
  `requires_archival_review` people.
- Possible-duplicate groups: 679; conflicts: 535.
- Claim confidence: 1,755 confirmed; 5,357 high; 2,615 medium; 255 low;
  443 conflicting; and 2 unresolved.
- Public projection: 23,936 profiles, 4,001 affiliations, 1,313
  organizations, 6,524 sources and 10,166 published, qualified or conflict
  claims.
- Citations: 7,811 across 4,358 unique source documents.

## Publication verification

- Immutable published release commit:
  `ba92121419bd8cad3179b5a71e12ca127bd80634`.
- GitHub Actions Test run `41676162559` completed successfully at
  `2026-11-03T16:42:43Z`.
- GitHub Pages run `41676162676` completed successfully at
  `2026-11-03T16:40:23Z`.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and the Batch 998 evidence
  bundle. It verified all 67 public assets (133,688,539 bytes; manifest
  SHA-256
  `7cf2f4ec4de27880db371d7ca09be860b2e9e670434dffa39ddb2027ecb2ac01`),
  all eight core routes, all 44 source-register pages and all 23 direct Batch
  998 profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
