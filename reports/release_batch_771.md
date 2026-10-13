# Batch 771 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 771 covers PDF page 375, rows 25-46, Eleanor A Powell through Richard W
Powers. All 22 printed rows remain preserved and linked to 22 distinct person
entities. Each person received a new terminal research attempt. The next indexed
boundary is page 376, row 1, Steele Powers.

## Research outcome

- The batch records 20 `requires_archival_review` outcomes, one
  `documented_prewar_employer_found` outcome, and one `conflicting_sources`
  outcome.
- Eugene B Power is identified with high confidence as Eugene Barnum Power.
  Edwards Brothers, Inc. is documented as earlier pre-OSS employment, while
  University Microfilms is a medium-confidence, qualified last civilian
  affiliation before OSS. Neither is presented as an explicit immediate
  affiliation.
- Six exact-name plus protected-identifier official Army matches were accepted.
  Robert I Powell received a separate name-and-rank institutional identity
  bridge. No Army occupation code was treated as an employer.
- John Powell remains a visible surname conflict: the identifier agrees with a
  record printed as `POWELCZAK JOHN`, but that spelling was not adopted as an
  alias.
- John L Power's T/5 rank is classified as enlisted Army personnel without
  resolving him to an incompatible naval namesake.
- Fifty-one review decisions are preserved: six accepted, one conflicting, and
  44 rejected. No full service identifier is published.
- NARA Catalog work was dry-run only: 22 planned searches and zero authenticated
  requests. CIA access failed closed on the first request. LoC searches completed
  for 20 people, returned source errors for two, and produced 44 candidates that
  were individually rejected after review. Access errors were not treated as
  negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 10,735/23,939 (44.8431%).
- Verified employer: 351/23,939 (1.4662%).
- Verified affiliation: 790/23,939 (3.3001%).
- Archival review assessed: 9,193/23,939 (38.4018%).
- Not started: 13,199.
- Possible duplicate groups: 540.
- Conflicts: 363.
- Claims: 1,408 confirmed; 3,299 high; 1,586 medium; 201 low; 316
  conflicting; two unresolved.
- Citations: 5,921 records representing 3,045 unique source documents.

## Local release gates

- Python: 139 tests and 78 subtests passed.
- Profile audit: all seven checks passed for the deterministic 200-profile
  sample.
- Astro: 405 source files checked with zero errors, warnings, or hints; 24,890
  HTML pages built.
- Browser: 90/90 desktop, phone, tablet, analysis, and accessibility checks
  passed, including 30 axe checks and all 21 Batch 771 checks.
- Extraction: 522/522 pages and 23,978/23,978 rows validated; all 32 parser
  warnings have completed visual review.
- Links: every internal link resolved; 50,904 unique external URLs were
  inventoried.
- Redaction: zero unexpected full service-number matches across 24,962
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 108,962,613 bytes, SHA-256
  `ad3beb9b5726823729b23902bfdcac2e020be9e42b53e9da67233df41df2c063`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `42434f77cb2b14c7c3192f58c6cf08b13d7b2e8be2248a5afa7e90a21b0b8dfa`
  across 70 files and 111,309,762 bytes, and production-tree SHA-256
  `eda910c101492f829f4d3aac19219e8ba74a0fd0244838d748a60cedea088bae`
  across 24,962 files and 312,837,208 bytes.

## Publication

Release commit `3713cfc2758fd7a348975b49590230113f18a0eb` was pushed to
`main` on 2026-10-13. The hosted
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38381438546)
completed successfully at 2026-10-13T10:13:16Z, and the
[Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38381438515)
completed successfully at 2026-10-13T10:11:39Z.

The immutable live verifier checked the public site against that exact commit:
all 67 manifest assets and 108,962,613 bytes matched SHA-256 manifest digest
`ad3beb9b5726823729b23902bfdcac2e020be9e42b53e9da67233df41df2c063`;
all eight core routes, all 32 source-register pages, and all 22 Batch 771
profile routes returned their expected public content. The verified public URL
is <https://therealjameswilson.github.io/before-oss/>.
