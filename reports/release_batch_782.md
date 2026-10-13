# Batch 782 release record

Date: 2026-10-13 America/New_York

## Scope

Batch 782 covers PDF page 381, rows 1-23, William A Pye through the second
Edmund P Quereau entry. All 23 printed rows remain preserved and linked to 23
distinct person entities. Every person received a saved, terminal research
outcome. The next indexed boundary is page 381, row 24, John P Quertermous.

## Research outcome

- All 23 people have the terminal status "requires_archival_review".
- Official Army evidence supports high-confidence identity matches for Ted S
  Pytlinski, Emil J Quayle, and Vincent J Quercia. Army occupation codes were
  used only as identity evidence and were not converted into employment claims.
- The Army record associated with Patsy A Quagliato's protected identifier
  names John A OConnell. The record associated with Paul P Quayle's protected
  identifier spells the surname Quealy. Both conflicts remain visible and no
  coded fields were transferred.
- A San Antonio Express-News obituary probably identifies the historical
  Edmund Packard Quereau and documents French teaching at the University of
  Texas, doctoral study at the University of Chicago, Army Signal Security
  Service, and transfer to OSS. The evidence cannot select between the captain
  and major source rows, so both remain distinct. The chronology is published
  only as a qualified shared-person lead and contributes no affiliation or
  employer row to analytics.
- Richard R Quay and Jean Y Quentel each remain as two distinct indexed entities
  in visible possible-duplicate groups pending personnel-file comparison.
  Elene C Queen and Elene S Queen remain distinct because different middle
  initials and record details do not justify a merge.
- The clipped index note "Also 337" and both occurrences of "French" remain
  exactly as printed and were not expanded or interpreted.
- NARA Catalog work was dry-run only: 20 distinct searches planned, three safe
  duplicate-query reuses, and zero authenticated requests. CIA Reading Room and
  Library of Congress adapters failed closed on their first eligible requests.
  Source-access limitations were not treated as negative historical evidence.

## Exact coverage at export

- Index: 23,978/23,978 linked rows (100%).
- Active person entities: 23,939.
- Research attempted: 10,986/23,939 (45.8916%).
- Verified employer: 357/23,939 (1.4913%).
- Verified affiliation: 800/23,939 (3.3418%).
- Archival review assessed: 9,445/23,939 (39.4544%).
- Not started: 12,948.
- Possible duplicate groups: 547.
- Conflicts: 372.
- Claims: 1,411 confirmed; 3,397 high; 1,600 medium; 202 low; 322
  conflicting; two unresolved.
- Citations: 5,983 records representing 3,091 unique source documents.
- Public data: 2,592 published affiliations, 924 organizations, 4,758 public
  sources, and 6,726 published claims.
- Research statuses: one "blocked_by_source_access"; 333 "candidate_found"; 198
  "completed"; 313 "conflicting_sources"; 182
  "documented_prewar_employer_found"; 1,901 "in_progress"; 535
  "needs_identity_review"; 25 "needs_temporal_review"; 1,156
  "no_reliable_result_after_protocol"; 12,948 "not_started"; 1,058
  "occupation_only_found"; 4,984 "requires_archival_review"; and 305
  "verified_employer_found".

## Local release gates

- Python: 141 tests passed, including 81 parameterized subtests.
- Ingest: all 23,978 rows, 522 pages, 32 parser-warning rows, selected visual-QA
  pages, SQLite integrity, and foreign keys passed.
- Astro: 416 source files checked with zero errors, warnings, or hints; 24,903
  HTML pages built.
- Browser: 87/87 desktop, phone, tablet, analysis, and accessibility checks
  passed: 18 Batch 782 checks, 33 core-site checks, six analysis checks, and 30
  axe checks.
- Links: all 24,903 generated HTML files passed internal-link checks; 50,950
  unique external URLs were inventoried.
- Redaction: zero unexpected private-identifier boundary matches across 24,975
  artifacts.
- Dependencies: the production audit found zero vulnerabilities.
- Manifest: 67 assets, 109,649,182 bytes, SHA-256
  "b6bc0841407b49f3f7c3bc39261a9ffcea446fcbe71f85f195f9f8f28da5be77".
- Determinism: two consecutive builds produced public-tree SHA-256
  "236defe1eadb8f9b77c3353469097fd1264daeb8b3a9b7e58f4a216f95cd4228"
  across 70 files and 111,996,331 bytes, and production-tree SHA-256
  "7fd2d3903d172c392c3d8b1aa39e0f6f933ed359cabdb7e095e3fbd24b416779"
  across 24,975 files and 313,967,865 bytes.

## Publication

- Release commit:
  "1d0dabf512046c360a287cfcf9c60fabeea8dfb5".
- The [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38439616498)
  completed successfully.
- The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38439616434)
  completed successfully.
- Immutable live verification against the release commit confirmed all 67
  manifest assets and 109,649,182 bytes, all eight core routes, all 32 source
  register pages, and all 23 directly affected profile routes. The deployed
  manifest SHA-256 is
  "b6bc0841407b49f3f7c3bc39261a9ffcea446fcbe71f85f195f9f8f28da5be77".
- Live site: <https://therealjameswilson.github.io/before-oss/>.

Both workflows emitted maintenance notices that selected GitHub actions still
target Node.js 20 and that "ubuntu-latest" is scheduled to migrate to Ubuntu 26.
GitHub ran the affected actions on Node.js 24; neither notice failed or altered
this release.

The full project remains unfinished. Batch 782 is published, but 12,948 active
person entities remain "not_started"; work resumes at page 381, row 24, John P
Quertermous.
