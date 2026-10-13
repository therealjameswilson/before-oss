# Batch 783 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 783 covers PDF page 381, rows 24-46, John P Quertermous through Waldo S
Quinney. All 23 printed rows remain preserved and linked to 23 distinct person
entities. Every person received a saved, terminal research outcome. The next
indexed boundary is page 382, row 1, John E Quintrell.

## Research outcome

- Twenty-two people have the terminal status "requires_archival_review";
  Martin S Quigley has "documented_prewar_employer_found".
- Official Army evidence supports high-confidence identity matches for John P
  Quertermous, Glenford Quick, and Timothy B Quill. Army occupation codes were
  used only as identity evidence and were not converted into employment claims.
- The Army record associated with Luther P Quick's protected identifier instead
  names Quick H R P. The conflict remains visible and no coded fields were
  transferred.
- Martin S Quigley's first-person account and a career-directory biography
  support a high-confidence identity. The chronology distinguishes the Office
  of the Coordinator of Information as his immediate pre-OSS government
  affiliation from Quigley Publishing Company as his last civilian employer.
- A Washington Post obituary probably identifies LaVonne S Quidley and
  documents federal secretarial employment, but does not name OSS and attributes
  the War Department identification to family recollection. The claim remains
  medium-confidence, visibly qualified, and excluded from default analytics.
- An official Air Force unit history probably identifies Robert S Quinn as
  commander of the 50th Fighter Group from 9 November to 1 December 1943. The
  source does not establish its sequence relative to OSS service, so the
  military affiliation remains medium-confidence and temporally uncertain.
- General William W Quinn, Governor William F Quinn, and Professor Harold Scott
  Quigley were rejected as unproven namesakes rather than assigned to incomplete
  index rows.
- Jean B Quinn and Jean Q Quinn remain distinct. Their different middle
  initials, grade information, and source details do not justify a merge.
- The clipped notes "Extract fr" and "One of t" remain exactly as printed and
  were not expanded or interpreted.
- NARA Catalog work was dry-run only: 23 distinct searches planned and zero
  authenticated requests. CIA Reading Room and Library of Congress adapters
  failed closed on their first eligible requests. Source-access limitations
  were not treated as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 11,009/23,939 (45.9877%).
- Verified employer: 358/23,939 (1.4955%).
- Verified affiliation: 801/23,939 (3.3460%).
- Archival review assessed: 9,468/23,939 (39.5505%).
- Not started: 12,925.
- Possible duplicate groups: 547.
- Conflicts: 373.
- Claims: 1,411 confirmed; 3,403 high; 1,604 medium; 202 low; 323
  conflicting; two unresolved.
- Citations: 5,990 records representing 3,097 unique source documents.
- Public data: 2,596 published affiliations, 928 organizations, 4,765 public
  sources, and 6,737 published claims.
- Research statuses: one "blocked_by_source_access"; 333 "candidate_found"; 198
  "completed"; 313 "conflicting_sources"; 183
  "documented_prewar_employer_found"; 1,901 "in_progress"; 535
  "needs_identity_review"; 25 "needs_temporal_review"; 1,156
  "no_reliable_result_after_protocol"; 12,925 "not_started"; 1,058
  "occupation_only_found"; 5,006 "requires_archival_review"; and 305
  "verified_employer_found".

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, selected visual-QA
  pages, SQLite integrity, and foreign keys passed.
- Astro: 417 source files checked with zero errors, warnings, or hints; 24,907
  HTML pages built.
- Browser: 90/90 desktop, phone, tablet, analysis, and accessibility checks
  passed: 21 Batch 783 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,907 generated HTML files passed internal-link checks; 50,959
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,979
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,728,958 bytes, SHA-256
  "75d790d6312c631626ef1ce797e00c51e354f2d9e55e9a7ccb329b77cf7497f5".
- Determinism: two consecutive builds produced public-tree SHA-256
  "9e053290e900834fb7a4be29baf7bfc0df34f9e2d5100d058d48753c261ad683"
  across 70 files and 112,076,097 bytes, and production-tree SHA-256
  "ef7423af6a99475faac7f193ecc8adfeb8562966bc748218f9314ce05970f0c1"
  across 24,979 files and 314,106,169 bytes.

## Publication

- Release commit:
  "52e00fbdd04cbc75f32d06f1defb219c7cd445a4".
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38443948775)
  completed successfully.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38443948767)
  completed successfully.
- Immutable live verification against the release commit confirmed all 67
  manifest assets and 109,728,958 bytes, all eight core routes, all 32 source
  register pages, and all 23 directly affected profile routes. The deployed
  manifest SHA-256 is
  "75d790d6312c631626ef1ce797e00c51e354f2d9e55e9a7ccb329b77cf7497f5".
- Live site: <https://therealjameswilson.github.io/before-oss/>.

Both workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that "ubuntu-latest" is scheduled to migrate to Ubuntu 26.
GitHub ran the affected actions on Node.js 24; neither notice failed or altered
this release.

The full project remains unfinished. Batch 783 is published, but 12,925 active
person entities remain "not_started"; work resumes at page 382, row 1, John E
Quintrell.
