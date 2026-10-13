# Batch 773 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 773 covers PDF page 376, rows 25-46, Philip P Pratt through Julia J
Preston. All 22 printed rows remain preserved and linked to 22 distinct person
entities. Each person received a new terminal manual research attempt. The next
indexed boundary is page 377, row 1, Thomas G Presutti.

## Research outcome

- The batch records 21 `requires_archival_review` outcomes and one
  `conflicting_sources` outcome.
- John E Preston has a high-confidence exact-name plus protected-identifier
  Army match. The Army coded occupation is not employer evidence.
- Howard V Prenzel remains a visible identity conflict because the agreeing
  protected identifier points to an Army record printed as `RE E HOWARD V`.
- The Howard J Preston Library of Congress candidate was rejected after page
  OCR showed Howard K Preston. A low-confidence Julio Prester archival lead is
  retained privately and withheld from public claims.
- Three review decisions are preserved: one accepted, one conflicting, and one
  rejected. No full service identifier is published.
- NARA Catalog work was dry-run only: 22 planned searches and zero
  authenticated requests. CIA access failed closed; LoC completed three
  searches before a later timeout. Exact-name OSS and employment/occupation
  searches were completed for every person. Access errors were not treated as
  negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 10,781/23,939 (45.0353%).
- Verified employer: 352/23,939 (1.4704%).
- Verified affiliation: 791/23,939 (3.3042%).
- Archival review assessed: 9,239/23,939 (38.5939%).
- Not started: 13,153.
- Possible duplicate groups: 540.
- Conflicts: 365.
- Claims: 1,408 confirmed; 3,308 high; 1,586 medium; 202 low; 318
  conflicting; two unresolved.
- Citations: 5,931 records representing 3,052 unique source documents.

## Local release gates

- Python: 139 tests plus 78 subtests passed.
- Profile audit: all seven checks passed for the deterministic 200-profile
  sample.
- Astro: 407 source files checked with zero errors, warnings, or hints; 24,892
  HTML pages built.
- Browser: 93/93 desktop, phone, tablet, analysis, and accessibility checks
  passed, including 30 axe checks and all 24 Batch 773 checks.
- Extraction: 522/522 pages and 23,978/23,978 rows validated; all 32 parser
  warnings have completed visual review.
- Links: all 24,892 generated HTML files passed internal-link checks; 50,911
  unique external URLs were inventoried.
- Redaction: zero unexpected full service-number matches across 24,964
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,045,103 bytes, SHA-256
  `8234ed632345793a03e809ece1351b5a0a21ed9472eb79f54d3858f83276643c`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `5ea33aeede95e22642c3775bd2fd6411cd4462968adfc4b5ecdb1a090fe91d3d`
  across 70 files and 111,392,254 bytes, and production-tree SHA-256
  `fc8784de47e9a90696825479b60cba28fcb8055d7f11714f463f8b7e14d32cde`
  across 24,964 files and 312,973,539 bytes.

## Publication

- Release commit:
  `b2a7e8540753daa215f52ecf79f78cbb8221ba92`.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38390745339)
  completed successfully at 2026-10-13T11:35:51Z.
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38390745359)
  completed successfully at 2026-10-13T11:33:06Z.
- Immutable live verification against the release commit confirmed all 67
  manifest assets and 109,045,103 bytes, all eight core routes, all 32 source
  register pages, and all 22 Batch 773 profile routes. The deployed manifest
  SHA-256 is
  `8234ed632345793a03e809ece1351b5a0a21ed9472eb79f54d3858f83276643c`.
- Live site: <https://therealjameswilson.github.io/before-oss/>.

Both workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26.
GitHub ran the affected actions on Node.js 24; neither notice failed or altered
this release.
