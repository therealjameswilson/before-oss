# Batch 791 release record

Date: 2026-10-14 America/New_York

## Scope

Batch 791 covers PDF page 385, rows 24-46, Francis R M Rea through Cornelia
Reck. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities, and every person received a saved terminal research
outcome. The next indexed boundary is page 386, row 1.

## Research outcome

- Conyers Read retains the terminal status `verified_employer_found`, and
  Constantino Reboa newly has `verified_employer_found`; the other 21 people
  have `requires_archival_review`.
- A direct May 1944 OSS personnel interview identifies Constantino Reboa at
  high confidence and documents his prewar work as a radio officer in the
  Italian Merchant Marine. Because wartime internment intervened before his
  OSS service, this is published as the best-supported last civilian employer
  rather than as an immediate pre-OSS affiliation.
- A University of Pennsylvania archival finding aid continues to support the
  existing high-confidence Conyers Read identity and Yale University
  affiliation.
- A National Park Service study supports the Louis M Ream identity lead but
  does not establish a reliable pre-OSS employer. The indexed personnel file
  remains necessary to resolve that question.
- Unsupported namesakes, undated affiliations, and postwar-only records were
  rejected rather than converted into claims. Public service-number displays
  remain masked.
- NARA Catalog and web work was dry-run only. Manual exact-name query families
  were completed for all 23 people. Source-access limitations were not treated
  as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 11,189/23,939 (46.7396%).
- Verified employer: 362/23,939 (1.5122%).
- Verified affiliation: 808/23,939 (3.3752%).
- Archival review assessed: 9,649/23,939 (40.3066%).
- Not started: 12,745.
- Possible duplicate groups: 550.
- Conflicts: 381.
- Claims: 1,413 confirmed; 3,476 high; 1,608 medium; 202 low; 331
  conflicting; two unresolved.
- Citations: 6,029 records representing 3,125 unique source documents.
- Public data: 2,610 published affiliations, 931 organizations, 4,804 public
  sources, and 6,824 published claims.
- Total saved research attempts and plans: 21,278.

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, all selected
  visual-QA pages, SQLite integrity, and foreign keys passed.
- Profile audit: all seven audit checks passed across a stratified sample of
  200 profiles.
- Astro: 425 source files checked with zero errors, warnings, or hints; 24,911
  HTML pages built.
- Browser: 84/84 desktop, phone, tablet, analysis, and accessibility checks
  passed: 15 Batch 791 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,911 generated HTML files passed internal-link checks; 50,981
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,983
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 110,254,628 bytes, SHA-256
  `dd6ad9e68cf858fcf1b886e323301ccf1b429596fbd07b9d6ace2fbb0fc9c07c`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `89060b2e6b9868852b3412f72f84e6aac1c1d4285d8dda9dd198d3416e366364`
  across 70 files and 112,601,776 bytes, and production-tree SHA-256
  `df3575e6c66ed9956c8040a93c2fc4a270444493e9c15473313a5de21c26a657`
  across 24,983 files and 314,934,042 bytes.

## Publication

- Release payload commit:
  `6b50fbace8ade2d36a4cd6d0337f478b527f06d3`.
- Deployment-resilience commit:
  `293ccc64b48d42f8cb11f1c38aca0e0421d165e8`.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38596805158)
  completed successfully, including the independent public-identifier audit.
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38596805230)
  completed successfully. The Pages deployment step took 9 minutes 24 seconds,
  within the action's ten-minute maximum, after two earlier workflow attempts
  timed out or were cancelled while the backend was updating the
  tens-of-thousands-of-files static site. Those workflow-status delays did not
  change the release payload.
- Immutable live verification against the deployment-resilience commit
  confirmed all 67 manifest assets and 110,254,628 bytes, all eight core
  routes, all 33 source-register pages, and all 23 directly affected profile
  routes. The deployed manifest SHA-256 is
  `dd6ad9e68cf858fcf1b886e323301ccf1b429596fbd07b9d6ace2fbb0fc9c07c`.
- Live site: <https://therealjameswilson.github.io/before-oss/>.

The workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that `ubuntu-latest` is scheduled to migrate to Ubuntu
26. GitHub ran the affected actions on Node.js 24; neither notice failed or
altered this release.

The full project remains unfinished. Batch 791 is published and live-verified,
but 12,745 active person entities remain `not_started`; work resumes at page
386, row 1, Margot F Reck.
