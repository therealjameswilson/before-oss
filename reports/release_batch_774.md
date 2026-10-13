# Batch 774 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 774 covers PDF page 377, rows 1-23, Thomas G Presutti through Harvey O
Price. All 23 printed rows remain preserved and linked to 23 distinct person
entities. Each person received a new terminal manual research attempt. The next
indexed boundary is page 377, row 24, Isma L Price.

## Research outcome

- The batch records 20 `requires_archival_review` outcomes, two
  `conflicting_sources` outcomes, and one
  `documented_prewar_employer_found` outcome.
- Ernest B Price has a high-confidence identity match and a documented 1938
  University of Chicago role as director of International House and professor.
  The affiliation is published as documented prewar employment, not as the
  immediate pre-OSS affiliation or last civilian employer. His postwar oil
  employment and a temporally ambiguous January 1943 lead remain excluded.
- Roger Prevost has a high-confidence Army identity match, but an official
  National Park Service history describes him as a Free French Army lieutenant
  during June 1942 OSS training while the Army bulk record gives the indexed
  grade as private. The conflict remains visible and is not treated as a
  pre-OSS affiliation.
- Francis B Price remains a visible protected-identifier conflict because an
  exact-name Army candidate and a differently named adjacent record share the
  same identifier. No employer is asserted.
- Eleven Army identity candidates were accepted, one candidate was retained as
  conflicting, and rejected namesake or postwar employment leads remain out of
  public claims. No coded Army occupation was converted into an employer.
- NARA Catalog work was dry-run only: 23 planned searches and zero
  authenticated requests. CIA and LoC adapters failed closed on their first
  requests. Exact-name OSS and employment/occupation searches were completed
  for every person. Access errors were not treated as negative historical
  evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 10,804/23,939 (45.1314%).
- Verified employer: 353/23,939 (1.4746%).
- Verified affiliation: 792/23,939 (3.3084%).
- Archival review assessed: 9,262/23,939 (38.6900%).
- Not started: 13,130.
- Possible duplicate groups: 540.
- Conflicts: 367.
- Claims: 1,408 confirmed; 3,320 high; 1,586 medium; 202 low; 320
  conflicting; two unresolved.
- Citations: 5,937 records representing 3,056 unique source documents.

## Local release gates

- Python: 139 tests plus 78 subtests passed.
- Profile audit: all seven checks passed for the deterministic 200-profile
  sample.
- Astro: 408 source files checked with zero errors, warnings, or hints; 24,893
  HTML pages built.
- Browser: 93/93 desktop, phone, tablet, analysis, and accessibility checks
  passed, including 30 axe checks and all 24 Batch 774 checks.
- Extraction: 522/522 pages and 23,978/23,978 rows validated; all 32 parser
  warnings have completed visual review.
- Links: all 24,893 generated HTML files passed internal-link checks; 50,915
  unique external URLs were inventoried.
- Redaction: zero unexpected full service-number matches across 24,965
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,117,041 bytes, SHA-256
  `6dd6c5282d7f6aba36284ea3d0d5952727e001f1b04f76feb2d57dff3388bad2`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `cb1542bfd5afef625163e85938996f1896d461467b7cff1a1d08e679b8b72f36`
  across 70 files and 111,464,196 bytes, and production-tree SHA-256
  `8cf313233304da43797d6ad8077295f3de92cc9f711b5afb68a4559cd5632a46`
  across 24,965 files and 313,093,906 bytes.

## Publication

- Release commit:
  `d6df7eb602a890e32212fce51eb1874e00786310`.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38395092993)
  completed successfully at 2026-10-13T12:13:06Z.
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38395093090)
  completed successfully at 2026-10-13T12:10:21Z.
- Immutable live verification against the release commit confirmed all 67
  manifest assets and 109,117,041 bytes, all eight core routes, all 32 source
  register pages, and all 23 Batch 774 profile routes. The deployed manifest
  SHA-256 is
  `6dd6c5282d7f6aba36284ea3d0d5952727e001f1b04f76feb2d57dff3388bad2`.
- Live site: <https://therealjameswilson.github.io/before-oss/>.

Both workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26.
GitHub ran the affected actions on Node.js 24; neither notice failed or altered
this release.
