# Batch 1052 release audit

Research and release date: 2026-11-11 America/New_York.

## Release contents

- NARA index page 307, rows 1-46: Charles W. McDaniel through Michael V.
  McDowell. The official 522-page PDF was downloaded afresh, its SHA-256
  matched the frozen provenance manifest, and page 307 was rendered and
  visually checked. All 46 printed rows remain separately recoverable as 46
  cautious person entities, and every entity has a saved terminal research
  outcome.
- The cohort contains 35 `requires_archival_review`, eight
  `occupation_only_found`, and three `conflicting_sources` outcomes.
- Eight accepted, nonshared, wartime-dated Army identity links support two
  student classifications and six broad occupational classifications:
  sheet-metal worker, foreman not elsewhere classified, sawmill occupation not
  elsewhere classified, miscellaneous occupation not elsewhere classified,
  construction or maintenance painter, and millwright. These classifications
  identify no named employer or institution and do not establish an
  Army-to-OSS chronology.
- The official Army code-list pages were rendered and visually checked before
  those categories were published. Paul J. McDougall's code 993 remains
  undefined and was not converted into an occupation or affiliation.
- Three protected-identifier conflicts remain visible for James E. McDaniel,
  Raymond W. McDonald, and Roy W. McDonald. No Army occupation or unbridged
  namesake biography was assigned to them.
- The Dervey A. McDonald / Hervey A. McDonald pair and the two Robert L.
  McDougal rows remain four separate people in two explicit duplicate-review
  groups.
- Every person received exact-name OSS discovery, a CIA-domain discovery
  check, and the previously recorded Library of Congress employment search.
  The CIA-domain searches returned no person-specific result; that discovery
  outcome is recorded as a limitation, not treated as proof of absence.
- Search snippets, people-finder and genealogy results, modern namesakes, and
  candidates without an identity bridge were rejected. No private identifier,
  raw Army record, authenticated NARA API payload, or full copyrighted source
  entered public data. No authenticated NARA Catalog API request was made.

## Evidence and import

- Reviewed evidence bundle: four sources, no new organizations, eight
  affiliations, 17 claims, 50 claim-source links, 46 person updates, and 46
  research attempts.
- Evidence and person-state imports were tested twice against a disposable
  database and remained idempotent on re-import: 8,324 sources, 4,877
  affiliations, 11,787 claims, 26,673 claim-source links, and 32,907 research
  attempts after both the first and second imports.
- Evidence-bundle SHA-256:
  `cf249d910000a60ee00c79e5d5c84d0345e7508a127cb9adeca866c4db5b5199`.
- The canonical pre-import backup had SHA-256
  `47f765105b48fee2cc6ee8dfba7f09d939cbf8f4eb934f17191c2e01dc0fca88`.
  After the audited export and profile-audit pipeline runs, the current release
  database has SHA-256
  `8320aa79bcb554d662166ccab5d8d0ee96e0c71d551ccbf1bd1d15c220c02ff1`.
- SQLite integrity is `ok`, foreign-key violations are zero, all 46 page-307
  people have terminal outcomes, and uncited public claims are zero.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,922/23,935 people (74.8778%).
- Verified affiliation: 1,253/23,935 people (5.2350%).
- Verified employer: 573/23,935 people (2.3940%).
- Archival disposition assessed: 16,688/23,935 people (69.7222%).
- Not started: 6,013 people; in progress: 1,569 people.
- Research outcomes include 2,297 `occupation_only_found`, 10,256
  `requires_archival_review`, 485 `verified_employer_found`, 308
  `documented_prewar_employer_found`, 641 `needs_identity_review`, 53
  `needs_temporal_review`, and 497 `conflicting_sources` people.
- Claim confidence: 2,050 confirmed; 5,686 high; 3,306 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,850 affiliations, 1,432 organizations,
  7,029 sources, and 11,518 published, qualified, or conflict claims.
- Citations: 8,324 across 4,687 unique source documents.
- Possible duplicate groups: 710. Total conflict flags: 580.
- Private derived data contain 4,877 affiliations, 1,446 organizations,
  32,907 research attempts, 20,514 unresolved rows, and 23,492 NARA pull-list
  rows.

## Local publication verification

- Targeted Batch 1052 and evidence tests: 21/21 passed. Independent unittest
  discovery passed all 154 tests.
- SQLite integrity is `ok`, foreign-key violations are zero, and uncited
  published, publish-qualified, or conflict claims are zero.
- Astro application check: 24 files with zero errors, warnings, or hints;
  strict TypeScript validation also covered the Playwright configuration and
  all test files.
- Static build: 25,422 pages. The resilient public-asset copy verified 70
  files totaling 146,974,302 bytes.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1052 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious or critical axe
  violations.
- Internal links: 25,422 HTML files checked; all links resolve. The checker
  inventoried 52,604 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 144,627,149 bytes,
  SHA-256
  `5e1b716b1e72a0af940f5ec86e708b2aa342e5e755e7ec120cc29548ba14a037`.
- Public-identifier audit: 25,494 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,585 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,494 artifacts totaling
  442,178,126 bytes at output-tree SHA-256
  `a5dbde5654fa3de223f7448ef9f63b2346f33cbf76f8b8d9f03d9897f30ae32e`.
- The deterministic 200-profile stratified audit passed all defined gates.
- The production dependency audit found zero vulnerabilities.

## Deployment status

Publication is pending the content commit, GitHub Actions checks, GitHub Pages
deployment, and deployed-release verification.

Public base URL: <https://therealjameswilson.github.io/before-oss/>.

Full-index historical research remains unfinished.
