# Batch 1057 release audit

Research and release preparation date: 2026-11-11 America/New_York.

## Release contents

- NARA index page 312, rows 1-46: Arthur B. McLaughlin through George T.
  McNamara. The official 522-page PDF matched the frozen provenance manifest,
  and page 312 was rendered and visually checked. All 46 printed rows remain
  separately recoverable through 45 cautious active person entities. Rows 6
  and 8 are duplicate John J. McLaughlin entries linked to one entity through
  the exact normalized name and private identifier; the two source rows remain
  immutable.
- Every person in the cohort has a saved terminal outcome: 28
  `requires_archival_review`, seven `occupation_only_found`, five
  `conflicting_sources`, three `needs_identity_review`, one
  `verified_employer_found`, and one `completed`.
- Emmett F. McNamara has a high-confidence identity bridge and an explicit
  immediate pre-OSS military assignment. A National Park Service history says
  that Private McNamara, a 22-year-old radio operator from Roxbury, was
  recruited by OSS in 1943 after graduating from the Army Signal Corps school
  at Fort Monmouth. The Signal Corps is published as a military assignment,
  not a civilian employer. No last civilian employer was inferred.
- Eight accepted, nonshared, wartime-dated Army identity links support three
  student classifications and five broad occupational classifications: actor
  or actress; policeman or detective in public service; midwife or practical
  nurse; retail manager; and housekeeper, steward, or hostess. None identifies
  a named employer or proves an Army-to-OSS chronology. The relevant official
  Army code-list pages 170-172 and 304 were visually checked before those
  qualified historical categories were published.
- James A. McLuskey has an official Army identity crosswalk dated 1946. That
  post-OSS Army entry remains identity-only and its occupation was excluded
  from pre-OSS claims. A browser test exposed a duplicate identity claim created
  by the first Batch 1057 generator draft; the duplicate claim and its two links
  were removed, the generator was corrected, and a fresh disposable import
  confirmed that only the earlier reviewed identity claim remains.
- Cyril McLeod's printed row places `PFC` in the middle-initial column while the
  rank column is blank. The raw layout, parser warning, and need for visual
  review remain visible. No silent rank or name correction was made.
- Five exact-name candidates with materially different official names or middle
  initials remain conflicts rather than accepted identities: Robert C.
  McManamy, Albert J. McMenamin, James D. McMillan, Walter F. McMillan, and
  Edward F. McNair. Jack A. McMurtrie was also rejected because the official
  candidate has a different middle initial. Plausible alternatives were
  retained in private review records rather than published as facts.
- Existing reviewed evidence for Donal McLaughlin remains the cohort's verified
  employer result and was not duplicated. Exact-name official, institutional,
  obituary, archival, employment, and OSS searches for the remaining people
  were recorded as applicable. Search snippets, namesakes, and candidates
  without an identity bridge were rejected. No authenticated NARA Catalog API
  request was made.

## Evidence and import

- Reviewed evidence bundle: five sources, one canonical-organization reuse,
  nine affiliations, 18 claims, 45 person updates, and 45 research attempts.
- Eleven private Army identity decisions were imported: five accepted and six
  rejected. No full private identifier or bulk-record ordinal is present in
  public data.
- Evidence and decision imports were tested twice against a disposable database
  and remained idempotent on re-import. A fresh second import created no new
  review decisions and no duplicate James A. McLuskey claim.
- Evidence-bundle SHA-256:
  `46b58d60b3cbeee1b39e4de3fb04bd09e4f644230558655439daa67c3fe67f46`.
- After the audited import, export, validation, and profile-audit runs, the
  release database has SHA-256
  `eb60fd413ecc6cce7b4c17850459d5178e8bdd3286b9077b1cfde1d95b16ca61`.
- SQLite integrity is `ok`, foreign-key violations are zero, all 45 page-312
  people have terminal outcomes, and uncited public claims are zero.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,989/23,935 active people (75.1577%).
- Verified affiliation: 1,261/23,935 people (5.2684%).
- Verified employer: 578/23,935 people (2.4149%).
- Archival disposition assessed: 16,859/23,935 people (70.4366%).
- Not started: 5,946 people; in progress: 1,428 people.
- Research outcomes include 2,340 `occupation_only_found`, 10,403
  `requires_archival_review`, 489 `verified_employer_found`, 309
  `documented_prewar_employer_found`, 649 `needs_identity_review`, 53
  `needs_temporal_review`, and 501 `conflicting_sources` people.
- Claim confidence: 2,050 confirmed; 5,731 high; 3,355 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,912 affiliations, 1,440 organizations,
  7,071 sources, and 11,612 published, qualified, or conflict claims.
- Citations: 8,366 across 4,712 unique source documents.
- Possible duplicate groups: 712. Total conflict flags: 584.
- Private derived data contain 4,939 affiliations, 1,454 organizations,
  33,133 research attempts, 20,465 unresolved rows, and 23,488 NARA pull-list
  rows.

## Local publication verification

- All nine Batch 1057 Python unit assertions passed when invoked directly. The
  complete Python suite is reserved for the clean GitHub runner because the
  local virtual environment contains macOS cloud placeholders that can stall
  broad test discovery.
- The existing 522-page, 23,978-row ingest validation continues to pass every
  page, row, warning, visual-review, SQLite-integrity, and foreign-key gate.
- Astro validation reported zero errors, warnings, or hints.
- Static build: 25,431 pages. The public-asset copy contains 70 files totaling
  147,752,454 bytes.
- Bounded browser release suite: 87/87 checks passed across desktop, phone, and
  tablet: 18 Batch 1057 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious or critical axe
  violations.
- Internal links: 25,431 HTML files checked; all links resolve. The checker
  inventoried 52,631 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 145,405,290 bytes, SHA-256
  `6dc7e54ceec18823012cd8a1e6ca71caabd3620b03e7e54839c17f87a04006a6`.
- Public-identifier audit: 25,503 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,592 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- The deterministic 200-profile stratified audit passed all seven defined
  gates.

## Deployment status

- The reviewed Batch 1057 data and site are prepared locally but have not yet
  been committed or pushed. The clean Test and GitHub Pages workflows remain
  required before publication can be claimed.

Public base URL after successful deployment:
<https://therealjameswilson.github.io/before-oss/>.

Full-index historical research remains unfinished.
