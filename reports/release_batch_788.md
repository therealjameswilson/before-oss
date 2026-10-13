# Batch 788 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 788 covers PDF page 384, rows 1-23, Joseph J Randazza through Michel
Rapaport. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities, and every person received a saved terminal research
outcome. The next indexed boundary is page 384, row 24, Maurice H Rapf.

## Research outcome

- Twenty-two people have the terminal status `requires_archival_review`; Thomas
  J Ransom has `conflicting_sources` pending archival comparison of a protected
  identifier also printed for Paul P Christopher.
- Seven official Army candidate rows were accepted as high-confidence identity
  evidence for Joseph J Randazza, Stephen T Randolph, Joseph S Ransmeier,
  Robert E Ransom, Thomas J Ranson, Richard Raoul-Duval, and Bergen B Rapalyea.
  Sourced junior suffixes were retained only as variants. Army occupation codes
  were not converted into employer or affiliation claims.
- Dartmouth institutional biographies support a high-confidence identity match
  for Joseph S Ransmeier and document his Vanderbilt University economics
  instructorship immediately before Army enlistment. Vanderbilt is published
  as his last civilian employer before wartime service, with a strongly
  date-bounded temporal basis, not as an explicitly immediate pre-OSS
  affiliation. His 1939-40 Brookings Institution research fellowship is
  published separately as an earlier professional affiliation.
- An official Archives nationales finding aid links Lieutenant Richard
  Raoul-Duval, alias Dorsay, to mission Freelance in 1944. A 1938 San Francisco
  classified telephone directory independently documents his attorney's office
  in the Hibernia Bank Building. The legal practice is published as earlier
  self-employment, not as immediate or last-civilian employment; the building is
  treated only as an address, never as an employer.
- The two separately printed Richard Raoul-Duval rows and the two separately
  printed Bergen B Rapalyea rows remain distinct person entities in possible-
  duplicate groups. Evidence accepted for one row was not silently transferred
  to the adjacent row.
- Protected-identifier conflicts for Thomas J Ransom / Paul P Christopher and
  Vincent P Rao / Joseph Veselinovich remain private, visible as conflicts, and
  subject to archival review. A name-conflicting Army row associated with
  Robert E Ransom was rejected as identity evidence but preserved as an
  auditable source anomaly.
- The incomplete `* Raoul` row remains unresolved and was not linked by page
  proximity alone.
- A Pan American World Airways finding-aid and directory lead for Bergen B
  Rapalyea was rejected because the material was postwar or undated and could
  not establish a pre-OSS affiliation.
- The clipped notes `photogra`, `Record`, `Honorab`, and `no first n` remain
  exactly as indexed and were not expanded or interpreted.
- NARA Catalog and web work was dry-run only: 23 planned searches per adapter,
  zero authenticated NARA requests, and no API response bodies stored. Two
  deterministic duplicate searches were skipped. The CIA Reading Room and
  Library of Congress adapters each failed closed on the first eligible
  request. These source-access limitations were not treated as negative
  historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 11,122/23,939 (46.4598%).
- Verified employer: 360/23,939 (1.5038%).
- Verified affiliation: 805/23,939 (3.3627%).
- Archival review assessed: 9,581/23,939 (40.0226%).
- Not started: 12,812.
- Possible duplicate groups: 550.
- Conflicts: 378.
- Claims: 1,411 confirmed; 3,453 high; 1,606 medium; 202 low; 328
  conflicting; two unresolved.
- Citations: 6,013 records representing 3,114 unique source documents.
- Public data: 2,605 published affiliations, 929 organizations, 4,788 public
  sources, and 6,794 published claims.

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, selected visual-QA
  pages, SQLite integrity, and foreign keys passed.
- Profile audit: all seven audit checks passed across a stratified sample of
  200 profiles.
- Astro: 422 source files checked with zero errors, warnings, or hints; 24,908
  HTML pages built.
- Browser: 90/90 desktop, phone, tablet, analysis, and accessibility checks
  passed: 21 Batch 788 checks, 33 core-site checks, six analysis checks, and 30
  axe checks. Two initially overbroad test assertions were corrected before the
  final clean run; neither represented a product defect.
- Links: all 24,908 generated HTML files passed internal-link checks; 50,971
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,980
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 110,070,087 bytes, SHA-256
  `9c1df1e7497b9a8d86f7c8f3eba94b0c61c0eef696d915bfc4ea3cc334c263df`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `310033c240757479613ef1ba21c1e495e653e3bd0494270c201cfbfdbf8a0745`
  across 70 files and 112,417,223 bytes, and production-tree SHA-256
  `0b33de2db609ca37e72304c38660db80b6fd022a9b9cc89e2b226e5483a88633`
  across 24,980 files and 314,636,955 bytes.

## Publication

- Release payload commit:
  `f12506ba060e0d1323fdaf04495b780cc24fb01a`.
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38484938165)
  completed successfully.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38484938131)
  completed successfully.
- Immutable live verification against the release payload confirmed all 67
  manifest assets and 110,070,087 bytes, all eight core routes, all 32 source
  register pages, and all 23 directly affected profile routes. The deployed
  manifest SHA-256 is
  `9c1df1e7497b9a8d86f7c8f3eba94b0c61c0eef696d915bfc4ea3cc334c263df`.
- The first immutable-verification attempt encountered a transient GitHub Pages
  HTTP 503. An immediate full retry succeeded with no content mismatch.
- Live site: <https://therealjameswilson.github.io/before-oss/>.

The workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that `ubuntu-latest` is scheduled to migrate to Ubuntu
26. GitHub ran the affected actions on Node.js 24; neither notice failed or
altered this release.

The full project remains unfinished. Batch 788 is published, but 12,812 active
person entities remain `not_started`; work resumes at page 384, row 24, Maurice
H Rapf.
