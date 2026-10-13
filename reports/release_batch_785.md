# Batch 785 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 785 covers PDF page 382, rows 25-46, Edwin R Raddatz through Philip E
Ragan. All 22 printed rows remain preserved as distinct source records linked
to 22 person entities. Every person received a saved, terminal research
outcome. The next indexed boundary is page 383, row 1, Peter Rago.

## Research outcome

- Nineteen people have the terminal status "requires_archival_review"; Eugene
  Radzikowski and Nathan Raenoff have "conflicting_sources"; Aldo L Raffa has
  "documented_prewar_employer_found".
- Five official Army candidate rows were accepted as high-confidence identity
  evidence for Alan R Rado, Charles C Raftell, Clarence T Rader, Harold R
  Raemer, and Vjekoslav Radic. Army occupation codes were not converted into
  employer or affiliation claims.
- Edwin R Raddatz remains a probable identity match because the official Army
  row spells the surname "RADDARZ." Eugene Radzikowski remains conflicting
  because one exact-name Army row and three incompatible names share the
  printed identifier. Nathan Raenoff remains conflicting because the official
  Army row tied to the printed identifier names a different person.
- Mikkel Dack's Cambridge University Press history identifies Maj. Aldo Raffa
  as a political-science instructor at Georgetown University, states that the
  instructor had originally been recruited by OSS, and cites the identically
  named RG 226 Box 630 personnel file. Georgetown is published as Raffa's
  medium-confidence, probable-immediate last civilian employer, not as a
  verified immediate predecessor.
- The clipped notes "Docume" and "file retai" and the printed note "French"
  remain exactly as indexed and were not expanded or interpreted.
- No new confirmed or high-confidence civilian employer was added, so default
  verified-employer analytics remain unchanged. Unresolved profiles direct
  researchers to the indexed personnel files rather than implying that no
  prior employment existed.
- NARA Catalog and web work was dry-run only: 22 planned searches per adapter
  and zero authenticated NARA requests. The CIA Reading Room and Library of
  Congress adapters each failed closed on the first eligible request. These
  source-access limitations were not treated as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 11,054/23,939 (46.1757%).
- Verified employer: 358/23,939 (1.4955%).
- Verified affiliation: 803/23,939 (3.3544%).
- Archival review assessed: 9,513/23,939 (39.7385%).
- Not started: 12,880.
- Possible duplicate groups: 547.
- Conflicts: 375.
- Claims: 1,411 confirmed; 3,423 high; 1,606 medium; 202 low; 325
  conflicting; two unresolved.
- Citations: 6,000 records representing 3,104 unique source documents.
- Public data: 2,600 published affiliations, 929 organizations, 4,775 public
  sources, and 6,761 published claims.

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, selected visual-QA
  pages, SQLite integrity, and foreign keys passed.
- Astro: 419 source files checked with zero errors, warnings, or hints; 24,908
  HTML pages built.
- Browser: 84/84 desktop, phone, tablet, analysis, and accessibility checks
  passed: 15 Batch 785 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,908 generated HTML files passed internal-link checks; 50,965
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,980
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,863,218 bytes, SHA-256
  "d98b3882dbd870b9866e37368ea9a6e1cc270f67136cdf723a828a2c3c3611a9".
- Determinism: two consecutive builds produced public-tree SHA-256
  "bd5acc429ce056a9d440b0148b3cb2a92b5d122c64a4deafe46a7ba4cae620f7"
  across 70 files and 112,210,362 bytes, and production-tree SHA-256
  "ed367d8f123e5b1912cf4f74da2a83b1012f4448cc9effef1d4691c3afb33ee6"
  across 24,980 files and 314,317,014 bytes.

## Publication

- Release commit:
  "157ae52a8521b6f1218d029e818b0f4c2ef3d002".
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38453462328)
  completed successfully.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38453462369)
  completed successfully.
- Immutable live verification against the release commit confirmed all 67
  manifest assets and 109,863,218 bytes, all eight core routes, all 32 source
  register pages, and all 22 directly affected profile routes. The deployed
  manifest SHA-256 is
  "d98b3882dbd870b9866e37368ea9a6e1cc270f67136cdf723a828a2c3c3611a9".
- Live site: <https://therealjameswilson.github.io/before-oss/>.

Both workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that "ubuntu-latest" is scheduled to migrate to Ubuntu 26.
GitHub ran the affected actions on Node.js 24; neither notice failed or altered
this release.

The full project remains unfinished. Batch 785 is published, but 12,880 active
person entities remain "not_started"; work resumes at page 383, row 1, Peter
Rago.
