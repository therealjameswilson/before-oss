# Batch 1034 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 289, rows 1-46: Cyril MacLeod through Tore Maehle. All 46
  rows remain separately recoverable as 46 cautious person entities.
- Forty-five people received new saved research outcomes; Gus Macriyanni's
  previously terminal outcome and 18 recorded attempts were preserved without
  replacement. The full cohort contains 30 `requires_archival_review`, ten
  `occupation_only_found`, three `needs_identity_review`, two
  `verified_employer_found`, and one `completed` outcome.
- Ten protected-identifier Army candidates received explicit accepted
  decisions. Their Army-entry records support only broad occupation or student
  categories; no coded occupation was converted into a named employer.
- William B. Macomber is published with the U.S. Marine Corps Reserve as his
  immediate military predecessor and Yale University as a separate student
  relationship. The official Marine Corps history explicitly traces the
  sequence to his planned OSS assignment.
- Louis E. Madison is published with the U.S. Army as his immediate military
  pathway, the U.S. Department of Labor as his last civilian employer, and
  George Washington University as a separate student relationship. A CIA OSS
  record independently corroborates his wartime identity and assignment.
- Max T. Madson's Department of Agriculture motion-picture work is published
  as a qualified last civilian employer. The evidence does not establish it as
  the immediate predecessor to OSS, so no immediate affiliation is asserted.
- George H. Maddock receives only the date-bounded student category recorded at
  Army entry. Official park history supplies direct OSS team context but does
  not establish a pre-OSS organization.
- The three Robert B. MacLeod rows remain separate ambiguous entities in one
  visible possible-duplicate group, with no affiliations transferred between
  them.
- The cohort identity assessment is four confirmed, nine high-confidence,
  three ambiguous, and 30 unresolved people.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: ten sources, six organizations, 16 affiliations,
  16 claims, 55 claim-source links, 45 person updates, and 45 research
  attempts.
- Ten Army identity-review decisions were imported. Decision and evidence
  imports were tested against a disposable database before the durable update.
- A pre-import SQLite backup is retained at
  `/private/tmp/before-oss-pre-b1034-20261104.sqlite` for local recovery.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `9e4008be9b4b93bf4c18184064d03829e29a9ffddf3f1e2a9e59ebe9f59c7b8b`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,447/23,935 people (72.8933%).
- Verified affiliation: 1,223/23,935 people (5.1097%).
- Verified employer: 558/23,935 people (2.3313%).
- Archival disposition assessed: 15,922/23,935 people (66.5218%).
- Not started: 6,483 people; in progress: 1,878 people.
- Research outcomes include 2,076 `occupation_only_found`, 9,760
  `requires_archival_review`, 470 `verified_employer_found`, 298
  `documented_prewar_employer_found`, 622 `needs_identity_review`, 50
  `needs_temporal_review`, and 487 `conflicting_sources` people.
- Claim confidence: 2,018 confirmed; 5,597 high; 3,067 medium; 261 low; 473
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,568 affiliations, 1,401
  organizations, 6,871 sources, and 11,151 published, qualified, or conflict
  claims.
- Citations: 8,164 across 4,594 unique source documents.
- Possible duplicate groups: 699. Total conflict flags: 567.

## Local publication verification

- Python: 259 pytest cases and 87 subtests passed.
- Clean Astro check: 665 files with zero errors, warnings, or hints.
- Clean static build: 25,390 pages and 25,462 total output artifacts.
- Bounded browser release suite: 87/87 checks passed across desktop, phone,
  and tablet: 18 Batch 1034 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,390 HTML files checked; all links resolve. The checker
  inventoried 52,513 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 141,442,769 bytes,
  SHA-256
  `039c76313ba67f15fce179f74de6112f7e5c955f011fd959c9927d015095154c`.
- Public-identifier audit: 25,462 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,584 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,462 artifacts totaling
  436,895,246 bytes at output-tree SHA-256
  `bb6085811035f39f1951be235233c975341181440b3a4f3db1b8551c59c9f874`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit:
  [`3411a27be0f1f7fa94a4d3ce7f78e33863278b6e`](https://github.com/therealjameswilson/before-oss/commit/3411a27be0f1f7fa94a4d3ce7f78e33863278b6e).
- GitHub Actions Test run
  [41927979996](https://github.com/therealjameswilson/before-oss/actions/runs/41927979996)
  passed, including Python tests, the public-manifest check, the clean static
  build, the bounded browser suite, and a rebuilt private-identifier audit.
- GitHub Pages run
  [41927979832](https://github.com/therealjameswilson/before-oss/actions/runs/41927979832)
  built and deployed successfully.
- The unauthenticated deployed-release verifier matched all 67 manifested
  assets and 141,442,769 bytes at SHA-256
  `039c76313ba67f15fce179f74de6112f7e5c955f011fd959c9927d015095154c`,
  then checked eight core routes, all 46 source-register pages, and all 45
  newly reviewed direct profile URLs against the immutable content commit.
  Gus Macriyanni's preserved 46th cohort profile was checked separately at
  its direct public URL and returned HTTP 200 with the expected unresolved,
  archival-review outcome.
- The deployed stats endpoint exactly reports the Batch 1034 totals recorded
  above.
- Public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
