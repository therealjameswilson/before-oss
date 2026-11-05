# Batch 1047 release audit

Date: 2026-11-05 America/New_York

## Release contents

- NARA index page 302, rows 1-46: Philip J. May through Richard Mazzarini.
  All 46 printed rows remain separately recoverable as 46 cautious person
  entities, and every entity has a saved terminal research outcome. Two
  Frederick Mayer entities already had terminal, sourced outcomes and were
  preserved unchanged; the other 44 people received new reviewed outcomes.
- The full cohort contains 30 `requires_archival_review`, eight
  `occupation_only_found`, four `needs_identity_review`, three
  `documented_prewar_employer_found`, and one `completed` outcome.
- Eight reviewed Army identity bridges support broad, date-bounded occupation
  categories only. They do not establish a named employer, institution,
  workplace, or immediate pre-OSS affiliation, and no protected identifier or
  raw Army row entered the public bundle.
- Hoover Presidential Library evidence supports Ferdinand Lathrop Mayer's
  State Department and Foreign Service career through 1940, including service
  as Ambassador to Haiti beginning in 1937. It is published as documented
  prewar government employment, not as a proven immediate OSS predecessor.
- MIT's institutional biography supports Bruce H. Mazlish's 1940 Columbia
  graduation and OSS identity. Columbia is correctly classified as student
  status rather than an employer.
- A National Archives award-citation scan confirms Wendell Mayfield's wartime
  identity and Chief Yeoman assignment under Naval Personnel. It supplies no
  pre-OSS employer and is not stretched into one.
- A contemporary Bailey County Journal profile, corroborated by an official
  Medal of Freedom list, supports Richard Mazzarini's Pan American Airways
  air-cargo employment from 1929 and wartime leave before OSS service. Because
  the exact transition date is not explicit, this is a qualified,
  medium-confidence last civilian employer and `probable_immediate` pathway,
  not an unqualified immediate-predecessor claim.
- Gerald Mayer's unbridged common-name candidate, Jean Mazou's unbridged French
  military candidate, and Riccardo Mazzarini's adjacent conflicting-name row
  remain private or visibly unresolved. No evidence was transferred across the
  Richard/Riccardo rows. No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: 12 sources, three reused organizations, 11
  affiliations, 17 claims, 54 claim-source links, 44 person updates, and 44
  research attempts. All 11 public affiliations have claim-level citations.
- Evidence and person-state imports were tested twice against a disposable
  database and remained idempotent on re-import. The two prior Frederick Mayer
  outcomes remained byte-for-byte unchanged in the comparison audit.
- A pre-import SQLite backup is retained outside the tracked release tree as
  `research-pre-batch1047-2026-11-05.sqlite`, SHA-256
  `f8a41c09c86f2f289d8391bd6917a0a8a0cdb46b2b46e11dc52b2d18b7f05162`.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `43b37b0eabc12e8ee107229b83fa675c90cbbc98eb73773a6dfe8638166d4675`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,899/23,935 people (74.7817%).
- Verified affiliation: 1,242/23,935 people (5.1891%).
- Verified employer: 565/23,935 people (2.3606%).
- Archival disposition assessed: 16,491/23,935 people (68.8991%).
- Not started: 6,031 people; in progress: 1,745 people.
- Research outcomes include 2,257 `occupation_only_found`, 10,096
  `requires_archival_review`, 479 `verified_employer_found`, 306
  `documented_prewar_employer_found`, 658 `needs_identity_review`, 52
  `needs_temporal_review`, and 495 `conflicting_sources` people.
- Claim confidence: 2,040 confirmed; 5,642 high; 3,263 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,782 affiliations, 1,423 organizations,
  6,989 sources, and 11,421 published, qualified, or conflict claims.
- Citations: 8,284 across 4,666 unique source documents.
- Possible duplicate groups: 709. Total conflict flags: 579.
- Private derived exports contain 4,809 affiliations, 1,437 organizations,
  8,284 citation rows, 32,678 research attempts, 20,562 unresolved rows, and
  23,498 NARA pull-list rows.

## Local publication verification

- Python: 366 pytest cases and 87 subtests passed; the independent unittest
  discovery run also passed all 154 tests.
- Clean Astro check: 678 files with zero errors, warnings, or hints.
- Clean static build: 25,413 pages and 25,485 total output artifacts.
- Bounded browser release suite: 93/93 checks passed across desktop, phone,
  and tablet: 24 Batch 1047 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,413 HTML files checked; all links resolve. The checker
  inventoried 52,580 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 143,866,400 bytes, SHA-256
  `5c702ec8990fa969014399e6160ec7c02cc6247aa5c82340a6fed628d01580c7`.
- Public-identifier audit: 25,485 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,587 candidate substrings, allowed two manifest-size coincidences, and found
  zero aggregate or unexpected boundary matches.
- Two consecutive local builds reproduced 25,485 artifacts totaling
  440,926,628 bytes at output-tree SHA-256
  `e52d5b0d47cc72efd625a3029ce9d005dc4595a3a0c471fb4e074efaa5c57caf`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit:
  [`2512b0ab157bf81b23aea4c933c265ce9899ee2a`](https://github.com/therealjameswilson/before-oss/commit/2512b0ab157bf81b23aea4c933c265ce9899ee2a).
- GitHub Actions Test run:
  [42083037873](https://github.com/therealjameswilson/before-oss/actions/runs/42083037873)
  completed successfully, including the Python suite, checked-in manifest
  verification, bounded browser release suite, rebuilt private-identifier
  audit source, and public redaction audit.
- GitHub Pages run:
  [42083037921](https://github.com/therealjameswilson/before-oss/actions/runs/42083037921)
  completed successfully for the same publication commit.
- Deployed-release verification matched all 67 canonical assets totaling
  143,866,400 bytes at manifest SHA-256
  `5c702ec8990fa969014399e6160ec7c02cc6247aa5c82340a6fed628d01580c7`.
  The verifier also passed eight core routes, 47 source-register pages, and all
  44 newly updated direct profile URLs.
- Public base URL: <https://therealjameswilson.github.io/before-oss/>.
