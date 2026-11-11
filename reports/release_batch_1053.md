# Batch 1053 release audit

Research and release date: 2026-11-11 America/New_York.

## Release contents

- NARA index page 308, rows 1-46: Robert H. McDowell through William M.
  McGhee. The official 522-page PDF was downloaded afresh, its SHA-256
  matched the frozen provenance manifest, and page 308 was rendered and
  visually checked. All 46 printed rows remain separately recoverable as 44
  cautious person entities; Robert D. McFadden and Stuart P. McFadden each
  retain two source rows. Every entity has a saved terminal research outcome.
- The cohort contains 28 `requires_archival_review`, 11
  `occupation_only_found`, three `needs_identity_review`, one
  `conflicting_sources`, and one `documented_prewar_employer_found` outcome.
- Ten accepted, nonshared, wartime-dated Army identity links support one
  student classification and nine broad occupational classifications. None
  identifies a named employer, and none establishes an Army-to-OSS chronology.
  The official Army code-list pages were rendered and visually checked before
  those categories were published. Undefined codes 993 and 999 remain
  uninterpreted.
- A November 1941 issue of *The Shield of Phi Kappa Psi* documents Lawrence B.
  McFaddin as an Indiana University student and a Phi Kappa Psi Indiana Beta
  pledgee. The index spelling `Lawerence` remains preserved. These are
  institutional affiliations, not employer claims and not evidence of the
  immediate pre-OSS role.
- The official 1932-33 Nebraska Educational Directory documents Darel D.
  McFerren as a Gordon High School history and economics teacher. A separately
  qualified obituary reports that he and Kathleen McFerren taught and
  administered a Methodist mission school in Medan from 1937 through 1942.
  The latter is published at medium confidence as the last documented civilian
  role before wartime service, not as an immediate pre-OSS affiliation.
- Edward C. McElroy remains conflicting because the protected Army identifier
  resolves to a different name; no Army data were transferred. William C.
  McGaragle and the Edward A. McGaughy / Edward McGaughy pair remain explicit
  identity-review cases. Duplicate rows and spelling variants remain visible.
- Search snippets, people-finder and unsourced genealogy results, modern
  namesakes, and candidates without an identity bridge were rejected. No
  private identifier, raw Army record, authenticated NARA API payload, or full
  copyrighted source entered public data. No authenticated NARA Catalog API
  request was made.

## Evidence and import

- Reviewed evidence bundle: eight sources, four organizations, 14
  affiliations, 15 claims, 54 claim-source links, 44 person updates, and 44
  research attempts.
- Evidence and person-state imports were tested twice against a disposable
  database and remained idempotent on re-import.
- Evidence-bundle SHA-256:
  `58c342a026b078d17b1b27fe00577e5bf327593377cc4055e89ba06046ec1bb5`.
- The canonical pre-import backup had SHA-256
  `8320aa79bcb554d662166ccab5d8d0ee96e0c71d551ccbf1bd1d15c220c02ff1`.
  After the audited import, export, and profile-audit runs, the release database
  has SHA-256
  `143f2d743aff5e22078372ac63eacd2f4c7fa3655f19128983955187aab6fd6f`.
- SQLite integrity is `ok`, foreign-key violations are zero, all 44 page-308
  people have terminal outcomes, and uncited public claims are zero.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,922/23,935 people (74.8778%).
- Verified affiliation: 1,255/23,935 people (5.2434%).
- Verified employer: 574/23,935 people (2.3982%).
- Archival disposition assessed: 16,716/23,935 people (69.8391%).
- Not started: 6,013 people; in progress: 1,529 people.
- Research outcomes include 2,308 `occupation_only_found`, 10,284
  `requires_archival_review`, 485 `verified_employer_found`, 309
  `documented_prewar_employer_found`, 641 `needs_identity_review`, 53
  `needs_temporal_review`, and 497 `conflicting_sources` people.
- Claim confidence: 2,050 confirmed; 5,690 high; 3,317 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,864 affiliations, 1,436 organizations,
  7,037 sources, and 11,533 published, qualified, or conflict claims.
- Citations: 8,332 across 4,692 unique source documents.
- Possible duplicate groups: 710. Total conflict flags: 580.
- Private derived data contain 4,891 affiliations, 1,450 organizations,
  32,951 research attempts, 20,474 unresolved rows, and 23,492 NARA pull-list
  rows.

## Local publication verification

- Targeted Batch 1053 and evidence tests: 23/23 passed. Independent unittest
  discovery passed all 154 tests.
- SQLite integrity is `ok`, foreign-key violations are zero, and uncited
  published, publish-qualified, or conflict claims are zero.
- Astro application check: 24 files with zero errors, warnings, or hints;
  strict TypeScript validation also covered the Playwright configuration and
  all test files.
- Static build: 25,426 pages. The public-asset copy contains 70 files totaling
  147,136,877 bytes.
- Bounded browser release suite: 93/93 checks passed across desktop, phone,
  and tablet: 24 Batch 1053 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious or critical axe
  violations.
- Internal links: 25,426 HTML files checked; all links resolve. The checker
  inventoried 52,612 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 144,789,711 bytes,
  SHA-256
  `08a2672158db2f8ff602ebcfd4068254511f89b555c19d23d69f1f49e4d40d0d`.
- Public-identifier audit: 25,498 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,587 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- The deterministic 200-profile stratified audit passed all defined gates.
- The production dependency audit found zero vulnerabilities.

## Deployment status

Publication commit, GitHub Actions runs, and deployed-release verification are
recorded here after the release is pushed and the live site matches the audited
manifest.

Public base URL: <https://therealjameswilson.github.io/before-oss/>.

Full-index historical research remains unfinished.
