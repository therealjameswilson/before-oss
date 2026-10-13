# Batch 772 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 772 covers PDF page 376, rows 1-24, Steele Powers through Jack C Pratt.
All 24 printed rows remain preserved and linked to 24 distinct person entities.
Each person received a new terminal research attempt. The next indexed boundary
is page 376, row 25, Philip P Pratt.

## Research outcome

- The batch records 22 `requires_archival_review` outcomes, one
  `verified_employer_found` outcome, and one `conflicting_sources` outcome.
- Nelson P Poynter has a high-confidence last civilian employer at the St.
  Petersburg Times / Times Publishing Company and a separately modeled
  high-confidence immediate federal inter-American communications press
  assignment before OSS/COI.
- Four exact-name plus protected-identifier official Army matches were accepted.
  Branko Prastalo received a separate rare-name scholarly OSS identity bridge.
  No Army occupation code was treated as an employer.
- Walter E Powers remains a visible identity conflict: his protected identifier
  agrees with an Army record printed as `POWERS WALTER JR`, but `Jr` was not
  adopted as an alias.
- Five identity review decisions are preserved: four accepted and one
  conflicting. No full service identifier is published.
- NARA Catalog work was dry-run only: 24 planned searches and zero authenticated
  requests. CIA and LoC access each failed closed on the first request. Exact-name
  OSS and employment/occupation searches were completed for every person.
  Access errors were not treated as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 10,759/23,939 (44.9434%).
- Verified employer: 352/23,939 (1.4704%).
- Verified affiliation: 791/23,939 (3.3042%).
- Archival review assessed: 9,217/23,939 (38.502%).
- Not started: 13,175.
- Possible duplicate groups: 540.
- Conflicts: 364.
- Claims: 1,408 confirmed; 3,307 high; 1,586 medium; 201 low; 317
  conflicting; two unresolved.
- Citations: 5,928 records representing 3,051 unique source documents.

## Local release gates

- Python: 139 tests passed.
- Profile audit: all seven checks passed for the deterministic 200-profile
  sample.
- Astro: 406 source files checked with zero errors, warnings, or hints; 24,892
  HTML pages built.
- Browser: 90/90 desktop, phone, tablet, analysis, and accessibility checks
  passed, including 30 axe checks and all 21 Batch 772 checks.
- Extraction: 522/522 pages and 23,978/23,978 rows validated; all 32 parser
  warnings have completed visual review.
- Links: every internal link resolved; 50,911 unique external URLs were
  inventoried.
- Redaction: zero unexpected full service-number matches across 24,964
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,029,191 bytes, SHA-256
  `85042250f81995675852fbc36997b1f955fd2bae705bf61990c3365649212e5a`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `e94dfce10584b46e2cf1e9a7efe4c151c6b9e7dd16029bd4a062ab43a97fd294`
  across 70 files and 111,376,328 bytes, and production-tree SHA-256
  `a2a9392ddb64d3bbd1db14970cb44ab3471df2f06be25c2b357db18ff383ffb6`
  across 24,964 files and 312,947,368 bytes.

## Publication

Release commit `2a058b58e74555aa5de69a54589b3ac632ac3dc9` was pushed to
`main` on 2026-10-13. The hosted
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38385021828)
completed successfully at 2026-10-13T10:45:41Z, and the
[Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38385022006)
completed successfully at 2026-10-13T10:43:00Z.

The immutable live verifier checked the public site against that exact commit:
all 67 manifest assets and 109,029,191 bytes matched SHA-256 manifest digest
`85042250f81995675852fbc36997b1f955fd2bae705bf61990c3365649212e5a`;
all eight core routes, all 32 source-register pages, and all 24 Batch 772
profile routes returned their expected public content. The verified public URL
is <https://therealjameswilson.github.io/before-oss/>.
