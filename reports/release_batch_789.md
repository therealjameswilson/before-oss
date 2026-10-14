# Batch 789 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 789 covers PDF page 384, rows 24-46, Maurice H Rapf through Michael
Ratushni. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities, and every person received a saved terminal research
outcome. The next indexed boundary is page 385, row 1, Clement Rault.

## Research outcome

- Twenty people have the terminal status `requires_archival_review`; Maurice H
  Rapf has `documented_prewar_employer_found`, Virginia Rathbun has
  `occupation_only_found`, and Seymour A Rattenberg has `conflicting_sources`.
- Nine official Army candidate rows were accepted as high-confidence identity
  evidence for Erwin E Raphael, Milton J Raport, Manuel C Raposa, Alfred M
  Rasero, Dale M Raska, George P Rasmussen, Charles Rata, William H Rath, and
  Michael Ratushni. Army occupation codes were not converted into employer or
  affiliation claims.
- A Dartmouth Libraries archival description supports a probable identity match
  for Maurice Harry Rapf and documents his prewar freelance screenwriting in
  Hollywood. The work is published as medium-confidence self-employment with a
  `documented_prewar` temporal basis. No studio employer and no immediate or
  last-civilian relationship were inferred.
- A Skidmore College institutional biography and National Archives item NAID
  542171 support the Virginia Rathbun Stuart identity. Skidmore is published as
  her immediate pre-OSS student affiliation, strongly date-bounded between her
  1943 graduation and November 1943 OSS entry, never as an employer.
- The separately printed Seymour A Rattenberg and Saymour A Rottenberg rows
  remain distinct person entities in one visible possible-duplicate group. Their
  shared protected identifier is retained privately, masked publicly, and
  treated as a conflict requiring archival comparison rather than an automatic
  merge.
- An Andre Rapicault French-registry namesake, contradictory Anastas Rapoff
  genealogy leads, and a postwar Michael Ratushni student-list namesake were
  rejected. Other unsupported namesakes were likewise not converted into
  claims.
- The clipped notes `see file`, `Record`, and `photogra`, and Edward G
  Ratcliffe's unusual printed identifier form, remain exactly preserved in the
  private source record. Public serial displays are masked.
- NARA Catalog and web work was dry-run only: 23 planned searches per adapter
  and zero live requests. Manual exact-name query families were completed for
  all 23 people. The CIA Reading Room and Library of Congress adapters each
  failed closed on the first eligible request. These source-access limitations
  were not treated as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 11,145/23,939 (46.5558%).
- Verified employer: 360/23,939 (1.5038%).
- Verified affiliation: 806/23,939 (3.3669%).
- Archival review assessed: 9,604/23,939 (40.1186%).
- Not started: 12,789.
- Possible duplicate groups: 550.
- Conflicts: 379.
- Claims: 1,412 confirmed; 3,463 high; 1,608 medium; 202 low; 329
  conflicting; two unresolved.
- Citations: 6,018 records representing 3,118 unique source documents.
- Public data: 2,607 published affiliations, 930 organizations, 4,793 public
  sources, and 6,808 published claims.

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, all 92 selected
  visual-QA pages, SQLite integrity, and foreign keys passed.
- Profile audit: all seven audit checks passed across a stratified sample of
  200 profiles.
- Astro: 423 source files checked with zero errors, warnings, or hints; 24,909
  HTML pages built.
- Browser: 87/87 desktop, phone, tablet, analysis, and accessibility checks
  passed: 18 Batch 789 checks, 33 core-site checks, six analysis checks, and 30
  axe checks. The Batch 789 redaction tests use format checks without embedding
  complete protected identifiers.
- Links: all 24,909 generated HTML files passed internal-link checks; 50,975
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,981
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 110,148,453 bytes, SHA-256
  `8ef230abed82cb2f9b7ff6cc88e53b568b8704676a1422c397720f5b52b1ab69`.
- Determinism: two consecutive builds produced public-tree SHA-256
  `f84d470c16fa5acbd6e732c27154832169017c48b3903bb1883c7429eb7e16d9`
  across 70 files and 112,495,593 bytes, and production-tree SHA-256
  `c68ff27e31dfd76b8abf205a23d7567f4f5759f0a6e0329749d0ff0b10254bdc`
  across 24,981 files and 314,762,836 bytes.

## Publication

- Release payload commit:
  `8e295abc70a8c8abfa4590d3fb56f72f644ee724`.
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38487940137)
  completed successfully.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38487940266)
  completed successfully, including the independent public-identifier audit.
- Immutable live verification against the release payload confirmed all 67
  manifest assets and 110,148,453 bytes, all eight core routes, all 32 source
  register pages, and all 23 directly affected profile routes. The deployed
  manifest SHA-256 is
  `8ef230abed82cb2f9b7ff6cc88e53b568b8704676a1422c397720f5b52b1ab69`.
- Live site: <https://therealjameswilson.github.io/before-oss/>.

The workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that `ubuntu-latest` is scheduled to migrate to Ubuntu
26. GitHub ran the affected actions on Node.js 24; neither notice failed or
altered this release.

The full project remains unfinished. Batch 789 is published, but 12,789 active
person entities remain `not_started`; work resumes at page 385, row 1, Clement
Rault.
