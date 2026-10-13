# Batch 786 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 786 covers PDF page 383, rows 1-24, Peter Rago through Angelo Ramirez.
All 24 printed rows remain preserved as distinct source records linked to 24
person entities, and every person received a saved terminal research outcome.
The next indexed boundary is page 383, row 25, Tommie I Rammage.

## Research outcome

- All 24 people have the terminal status `requires_archival_review`.
- Seven official Army candidate rows were accepted as high-confidence identity
  evidence for Peter Rago, Maurice T Ragsdale, Charles E Rahn, Milton E Raichle,
  Archie B Rainey, Matti Raivio, and Floyd B Rambin. Army occupation codes were
  not converted into employer or affiliation claims.
- A declassified 1946 U.S. Army record identifies Lieutenant Michael Rajacich
  in military-intelligence context, and a Department of Defense history places
  him on the OSS Operation Halyard team. These official sources support a
  high-confidence identity match but do not establish a pre-OSS employer.
- A discovery-only claim that Rajacich worked for the War Department before
  OSS was withheld because the underlying source was not directly inspected.
- The clipped notes "Polish Ar", "Also Ann", and "Also Par" and the printed
  note "French" remain exactly as indexed and were not expanded or interpreted.
- No new confirmed or high-confidence civilian employer was added. Unresolved
  profiles direct researchers to the indexed personnel files rather than
  implying that no prior employment existed.
- NARA Catalog and web work was dry-run only: 24 planned searches per adapter
  and zero authenticated NARA requests. The CIA Reading Room and Library of
  Congress adapters each failed closed on the first eligible request. These
  source-access limitations were not treated as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 11,078/23,939 (46.2760%).
- Verified employer: 358/23,939 (1.4955%).
- Verified affiliation: 803/23,939 (3.3544%).
- Archival review assessed: 9,537/23,939 (39.8388%).
- Not started: 12,856.
- Possible duplicate groups: 547.
- Conflicts: 375.
- Claims: 1,411 confirmed; 3,431 high; 1,606 medium; 202 low; 325
  conflicting; two unresolved.
- Citations: 6,004 records representing 3,107 unique source documents.
- Public data: 2,600 published affiliations, 929 organizations, 4,779 public
  sources, and 6,769 published claims.

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, selected visual-QA
  pages, SQLite integrity, and foreign keys passed.
- Astro: 420 source files checked with zero errors, warnings, or hints; 24,908
  HTML pages built.
- Browser: 81/81 desktop, phone, tablet, analysis, and accessibility checks
  passed: 12 Batch 786 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,908 generated HTML files passed internal-link checks; 50,967
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,980
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,908,100 bytes, SHA-256
  `9e545d71e0f2019dad82d14ce618e887ddc3d8dbc08932cfe3b17040155fedc6`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `3cadb1407c4d73f81954b2d1297bc565b9cf1c98d70ab53007335b44b9885e98`
  across 70 files and 112,255,243 bytes, and production-tree SHA-256
  `44d4bfe3ba0e8fce03e2a8086365e88789ada4bb0686dccb2f7d1e4132c6a041`
  across 24,980 files and 314,387,833 bytes.

## Publication

- Release commit:
  `9524a9a65ea66dd378c591f151364ebf1738cf2d`.
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38457119791)
  completed successfully. Its first deploy attempt encountered a transient
  GitHub ID-token request timeout after the build and artifact upload passed;
  the failed deploy job was retried without rebuilding or changing content and
  succeeded.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38457119579)
  completed successfully.
- Immutable live verification against the release commit confirmed all 67
  manifest assets and 109,908,100 bytes, all eight core routes, all 32 source
  register pages, and all 24 directly affected profile routes. The deployed
  manifest SHA-256 is
  `9e545d71e0f2019dad82d14ce618e887ddc3d8dbc08932cfe3b17040155fedc6`.
- Live site: <https://therealjameswilson.github.io/before-oss/>.

Both workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26.
GitHub ran the affected actions on Node.js 24; neither notice failed or altered
this release.

The full project remains unfinished. Batch 786 is published, but 12,856
active person entities remain `not_started`; work resumes at page 383, row 25,
Tommie I Rammage.
