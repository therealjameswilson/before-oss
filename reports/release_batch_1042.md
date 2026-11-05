# Batch 1042 release audit

Date: 2026-11-05 America/New_York

## Release contents

- NARA index page 297, rows 1-46: Paul P. Martaus through Maurice Martin. All
  46 printed rows remain separately recoverable as 46 cautious person entities,
  and every entity has a saved terminal research outcome.
- The cohort contains 31 `requires_archival_review`, ten
  `occupation_only_found`, three `needs_identity_review`, one
  `needs_temporal_review`, and one `verified_employer_found` outcome.
- Fourteen protected-linkage Army candidates received explicit review: eleven
  were accepted and three rejected. The rejected Frank J. Martel/Martell, Benn
  W. Martin/Ben, and Mark S. Martin/Marten M. R. candidates transferred no
  fields.
- The accepted Army records support identity and broad, date-bounded occupation
  or student categories only. No coded occupation became a named employer,
  workplace, institution, or immediate pre-OSS affiliation.
- Direct official OSS Personnel Board minutes document Garibaldi Martellacci's
  shoe-factory occupation and Mazzini Society propaganda activity. The factory
  remains unnamed, and the society is modeled as a professional affiliation,
  not employment or an immediate predecessor.
- Official Library of Congress and Truman Library records support the
  high-confidence Edwin McCammon Martin identity. His War Production Board
  assignment is explicitly sequenced into OSS service in late May 1944 and is
  modeled as both his immediate civilian government affiliation and last
  civilian affiliation before OSS.
- Paulette Marteliere and Kaj Martens receive qualified identity evidence only;
  neither receives an invented employer. Maurice Martin's reviewed Army record
  supports student status but names no institution, while a separate Maurice L.
  Martin radio-operator lead remains unbridged. Charles H. Martin remains in
  temporal review because the linked Army-entry date follows OSS dissolution.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: nine sources, two organizations, 12 affiliations,
  17 claims, 56 claim-source links, 46 person updates, and 46 research
  attempts. All 17 public claims have citation links.
- Fourteen Army identity-review decisions were imported: eleven accepted and
  three rejected. Decision and evidence imports were tested against a
  disposable database before the durable update and remained idempotent on
  re-import.
- A pre-import SQLite backup is retained as
  `research-pre-batch1042-2026-11-05.sqlite`, SHA-256
  `13dc2f7d6bd61bf14d762f91f7cd1ec0d3091ef266de4890ccb6db1e8ed794a2`.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `2ad2b8aeb8c7ea38232934e1b159bf43efe36d2c0ce18baadcda801a1be1604c`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,762/23,935 people (74.2093%).
- Verified affiliation: 1,238/23,935 people (5.1723%).
- Verified employer: 565/23,935 people (2.3606%).
- Archival disposition assessed: 16,272/23,935 people (67.9841%).
- Not started: 6,168 people; in progress: 1,831 people.
- Research outcomes include 2,191 `occupation_only_found`, 9,952
  `requires_archival_review`, 478 `verified_employer_found`, 304
  `documented_prewar_employer_found`, 649 `needs_identity_review`, 52
  `needs_temporal_review`, and 495 `conflicting_sources` people.
- Claim confidence: 2,033 confirmed; 5,628 high; 3,194 medium; 261 low; 473
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,709 affiliations, 1,420 organizations,
  6,947 sources, and 11,324 published, qualified, or conflict claims.
- Citations: 8,240 across 4,639 unique source documents.
- Possible duplicate groups: 708. Total conflict flags: 577.

## Local publication verification

- Python: 321 pytest cases and 87 subtests passed.
- Clean Astro check: 673 files with zero errors, warnings, or hints.
- Clean static build: 25,410 pages and 25,482 total output artifacts.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1042 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,410 HTML files checked; all links resolve. The checker
  inventoried 52,564 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 143,016,544 bytes, SHA-256
  `b4db739d651691805cfa73848a36361d7c11869a9081857a7e0ed988b3a2efcc`.
- Public-identifier audit: 25,482 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,583 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,482 artifacts totaling
  439,533,957 bytes at output-tree SHA-256
  `b1e5228cb0f0d67f0aca3a15c17f11974902315401cc522d0c9788020982bc6e`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit, GitHub Actions Test run, GitHub Pages run, and deployed
  asset/profile verification will be recorded after publication.
- Public base URL: <https://therealjameswilson.github.io/before-oss/>.
