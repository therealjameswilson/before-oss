# Batch 787 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 787 covers PDF page 383, rows 25-46, Tommie I Rammage through Ruth E
Randall. All 22 printed rows remain preserved as distinct source records linked
to 22 person entities, and every person received a saved terminal research
outcome. Page 388 was separately inspected to verify the indexed Tommie I
Remmage variant. The next indexed boundary is page 384, row 1, Joseph J
Randazza.

## Research outcome

- Twenty-one people have the terminal status `requires_archival_review`;
  Tommie I Rammage has `conflicting_sources` pending comparison of the indexed
  files in Boxes 632 and 639.
- Eight official Army candidate rows were accepted as high-confidence identity
  evidence for Nick E Ramoundos, Charles F Ramsdell, Kenneth S Ramsey, Winters
  P Ramsey, Sgt Philip L Rancourt, Frank J Randall, Gale M Randall, and Kenneth
  C Randall. Army occupation codes were not converted into employer or
  affiliation claims.
- A British Diplomatic Oral History Programme transcript supports a
  high-confidence identity match for Major Peter E Ramsbotham and documents
  security work in the British War Office and service in the British Army
  Intelligence Corps. Both are published as other wartime affiliations with
  uncertain temporal relation to OSS, not as an immediate affiliation or
  civilian employer.
- The separately printed Tommie I Rammage and Tommie I Remmage rows remain
  separate and visibly conflicting. A protected identifier shared by the two
  rows remains private.
- The two separately printed Philip L Rancourt rows remain separate person
  entities in one possible-duplicate group. Only the sergeant row has an
  accepted official Army match.
- A 1941 Ithaca directory lead for a namesake Kenneth C Randall was rejected
  because no geographic or identity bridge tied the business proprietor to the
  indexed soldier.
- The clipped notes "One fold", "Record", and "Certificat" remain exactly as
  indexed and were not expanded or interpreted.
- No new confirmed or high-confidence civilian employer was added. Unresolved
  profiles direct researchers to the indexed personnel files rather than
  implying that no prior employment existed.
- NARA Catalog and web work was dry-run only: 22 planned searches per adapter,
  zero authenticated NARA requests, and no API response bodies stored. The CIA
  Reading Room and Library of Congress adapters each failed closed on the first
  eligible request. These source-access limitations were not treated as
  negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 11,100/23,939 (46.3679%).
- Verified employer: 358/23,939 (1.4955%).
- Verified affiliation: 803/23,939 (3.3544%).
- Archival review assessed: 9,559/23,939 (39.9307%).
- Not started: 12,834.
- Possible duplicate groups: 548.
- Conflicts: 376.
- Claims: 1,411 confirmed; 3,442 high; 1,606 medium; 202 low; 326
  conflicting; two unresolved.
- Citations: 6,007 records representing 3,109 unique source documents.
- Public data: 2,602 published affiliations, 929 organizations, 4,782 public
  sources, and 6,781 published claims.

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, selected visual-QA
  pages, SQLite integrity, and foreign keys passed.
- Profile audit: all seven audit checks passed across a stratified sample of
  200 profiles.
- Astro: 421 source files checked with zero errors, warnings, or hints; 24,908
  HTML pages built.
- Browser: 87/87 desktop, phone, tablet, analysis, and accessibility checks
  passed: 18 Batch 787 checks, 33 core-site checks, six analysis checks, and 30
  axe checks. The final revised Batch 787 test file independently passed all
  18 checks again before publication.
- Links: all 24,908 generated HTML files passed internal-link checks; 50,968
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,980
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,974,422 bytes, SHA-256
  `3f636589f0ba5aafb11358ba88e1be39afb7c846266999f7e7a8fa324fb171c6`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `b5a24d1b4620fdde052561456baa6ec9feb22f9fb6a65b66d554d016ff903f6f`
  across 70 files and 112,321,565 bytes, and production-tree SHA-256
  `50ca8d1f6ce5e22be8c965c6ae09ac63769245cfed6e17d173fd1c03012d7125`
  across 24,980 files and 314,492,095 bytes.

## Publication

- Release payload commit:
  `c5b0f229c0f74b589fb6f4a16e0efdacaa7823d7`.
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38474205476)
  completed successfully.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38474205466)
  completed successfully.
- Immutable live verification against the release payload confirmed all 67
  manifest assets and 109,974,422 bytes, all eight core routes, all 32 source
  register pages, and all 22 directly affected profile routes. The deployed
  manifest SHA-256 is
  `3f636589f0ba5aafb11358ba88e1be39afb7c846266999f7e7a8fa324fb171c6`.
- Live site: <https://therealjameswilson.github.io/before-oss/>.

The workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that `ubuntu-latest` is scheduled to migrate to Ubuntu
26. GitHub ran the affected actions on Node.js 24; neither notice failed or
altered this release.

The full project remains unfinished. Batch 787 is published, but 12,834 active
person entities remain `not_started`; work resumes at page 384, row 1, Joseph J
Randazza.
