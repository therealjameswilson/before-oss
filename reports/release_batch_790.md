# Batch 790 release record

Date: 2026-10-14 America/New_York

## Scope

Batch 790 covers PDF page 385, rows 1-23, Clement Rault through Gregory S
Razran. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities, and every person received a saved terminal research
outcome. The next indexed boundary is page 385, row 24.

## Research outcome

- Gregory S Razran has the terminal status `verified_employer_found`; Eugene A
  Ray and George E Ray have `conflicting_sources`; the other 20 people have
  `requires_archival_review`.
- A Queens College institutional history and a contemporary TIME item support a
  high-confidence identity match for Gregory S Razran. Queens College is the
  best-supported immediate pre-OSS affiliation and last civilian employer, with
  an explicit qualification that his professorship continued during his OSS
  statistical consulting. Columbia University is separately published only as
  an earlier documented prewar affiliation.
- Pierre Ravarre is identified at high confidence as the French radio operator
  Jean Vernez associated with OSS Sussex and Ossex missions. No reliable
  pre-OSS employer was found in the accessible sources; the indexed personnel
  file requires archival review.
- Daniel Ravenel is identified at high confidence as Lieutenant Commander
  Daniel Ravenel Jr., USNR, officer in charge of the Naval Command OSS Liaison
  Division. His wartime military assignment is not labeled as a civilian
  employer, and his indexed personnel file requires archival review.
- Official Army bulk data supports high-confidence identity matches for David
  Rawle and John M Rawlins. Coded Army fields were retained as identity evidence
  and were not converted into employer claims.
- The Army candidates for Eugene A Ray and George E Ray conflict with the
  printed index identities. Both conflicts remain explicit and neither record
  was silently corrected or merged.
- Unsupported namesakes and temporally irrelevant candidates were rejected
  rather than converted into claims. Public service-number displays remain
  masked.
- NARA Catalog and web work was dry-run only. Manual exact-name query families
  were completed for all 23 people. Source-access limitations were not treated
  as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 11,167/23,939 (46.6477%).
- Verified employer: 361/23,939 (1.5080%).
- Verified affiliation: 807/23,939 (3.3711%).
- Archival review assessed: 9,627/23,939 (40.2147%).
- Not started: 12,767.
- Possible duplicate groups: 550.
- Conflicts: 381.
- Claims: 1,412 confirmed; 3,471 high; 1,608 medium; 202 low; 331
  conflicting; two unresolved.
- Citations: 6,025 records representing 3,122 unique source documents.
- Public data: 2,609 published affiliations, 930 organizations, 4,800 public
  sources, and 6,818 published claims.

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, all 92 selected
  visual-QA pages, SQLite integrity, and foreign keys passed.
- Profile audit: all seven audit checks passed across a stratified sample of
  200 profiles.
- Astro: 424 source files checked with zero errors, warnings, or hints; 24,909
  HTML pages built.
- Browser: 87/87 desktop, phone, tablet, analysis, and accessibility checks
  passed: 18 Batch 790 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,909 generated HTML files passed internal-link checks; 50,978
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,981
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 110,214,810 bytes, SHA-256
  `5ac0934aeb3fc1e0dd51c3a8e74516ab23686c21bc8c83830f320dfea19e064b`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `9e1936d56dc29a62241915bb119c44b9100e0fc10772a0bf68fb7b7a588fd96f`
  across 70 files and 112,561,968 bytes, and production-tree SHA-256
  `d2103868e04f8302ce5041ba2db5abc69d24431c32e3afdb591ce2e928a222ba`
  across 24,981 files and 314,863,839 bytes.

## Publication

- Release payload commit:
  `859cf7a931fbc379cabdf0a0f81e8b030c87d44e`.
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38588905299)
  completed successfully.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38588905293)
  completed successfully, including the independent public-identifier audit.
- Immutable live verification against the release payload confirmed all 67
  manifest assets and 110,214,810 bytes, all eight core routes, all 32 source
  register pages, and all 23 directly affected profile routes. The deployed
  manifest SHA-256 is
  `5ac0934aeb3fc1e0dd51c3a8e74516ab23686c21bc8c83830f320dfea19e064b`.
- Live site: <https://therealjameswilson.github.io/before-oss/>.

The workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that `ubuntu-latest` is scheduled to migrate to Ubuntu
26. GitHub ran the affected actions on Node.js 24; neither notice failed or
altered this release.

The full project remains unfinished. Batch 790 is published, but 12,767 active
person entities remain `not_started`; work resumes at page 385, row 24.
