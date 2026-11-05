# Batch 1043 release audit

Date: 2026-11-05 America/New_York

## Release contents

- NARA index page 298, rows 1-46: Maurice L. Martin through Frank M.
  Masiokas. All 46 printed rows remain separately recoverable as 46 cautious
  person entities, and every entity has a saved terminal research outcome.
- The cohort contains 30 `requires_archival_review`, 14
  `occupation_only_found`, and two `needs_identity_review` outcomes.
- Sixteen protected-linkage Army candidates received explicit review: 15 were
  accepted and one was rejected. The rejected Frank A. Marvian/Frank A. Marx
  candidate transferred no fields.
- James H. Martinez/James M. Martinez retains a visible identity conflict. The
  protected record is linked for review, but its occupation, entry date, and
  grade are not presented as settled public facts.
- Norman J. Martin's damaged protected record was accepted through its unique
  source linkage. Rigiberto/Rigoberto and Masenior/Masenoir remain visible as
  variants rather than silent corrections.
- Reviewed Army code-list evidence supports broad, date-bounded occupation or
  student categories only. It does not establish a named employer,
  institution, workplace, or immediate pre-OSS affiliation.
- Direct OSS evidence identifies Maurice L. Martin as the Beggar-circuit radio
  operator associated with the aliases Adam and Morange, but does not name a
  pre-OSS employer. A February 1944 OSS memorandum confirms Pierre M.
  Martinot's identity but likewise supplies no employer.
- Two federal court opinions confirm Carl A. Marzani's identity. The
  immediately preceding period is published only with the courts' qualified
  wording, “private pursuits” in New York City in 1940-41; it is modeled as an
  unknown relationship with `probable_immediate` temporal basis, not as a
  named employer or self-employment.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: eight sources, zero organizations, 14
  affiliations, 19 claims, 67 claim-source links, 46 person updates, and 46
  research attempts. All 19 public claims have citation links.
- Sixteen Army identity-review decisions were imported: 15 accepted and one
  rejected. Decision and evidence imports were tested against a disposable
  database and remained idempotent on re-import.
- A pre-import SQLite backup is retained outside the tracked release tree as
  `research-pre-batch1043-2026-11-05.sqlite`, SHA-256
  `52772ed4c8e49562f596e2c04c1dc9129830811973589bfd4fa936a007ef1656`.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `9b3ebb84ad66eb014ecb3cde02ac81cded277733f777eefa4823cc46136f66a4`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,808/23,935 people (74.4015%).
- Verified affiliation: 1,238/23,935 people (5.1723%).
- Verified employer: 565/23,935 people (2.3606%).
- Archival disposition assessed: 16,318/23,935 people (68.1763%).
- Not started: 6,122 people; in progress: 1,831 people.
- Research outcomes include 2,205 `occupation_only_found`, 9,982
  `requires_archival_review`, 478 `verified_employer_found`, 304
  `documented_prewar_employer_found`, 651 `needs_identity_review`, 52
  `needs_temporal_review`, and 495 `conflicting_sources` people.
- Claim confidence: 2,036 confirmed; 5,629 high; 3,208 medium; 261 low; 474
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,723 affiliations, 1,420 organizations,
  6,955 sources, and 11,343 published, qualified, or conflict claims.
- Citations: 8,248 across 4,644 unique source documents.
- Possible duplicate groups: 708. Total conflict flags: 579.
- Private derived exports contain 4,750 affiliations, 1,434 organizations,
  8,248 citation rows, 32,451 research attempts, 20,618 unresolved rows, and
  23,499 NARA pull-list rows.

## Local publication verification

- Python: 329 pytest cases and 87 subtests passed.
- Clean Astro check: 674 files with zero errors, warnings, or hints.
- Clean static build: 25,410 pages and 25,482 total output artifacts.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1043 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,410 HTML files checked; all links resolve. The checker
  inventoried 52,568 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 143,182,314 bytes, SHA-256
  `65b0f88a26db462a8b201a84a221acec976f21afb74029c35f2516035e4f096e`.
- Public-identifier audit: 25,482 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,583 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,482 artifacts totaling
  439,807,718 bytes at output-tree SHA-256
  `fe5ff892f1c8230f9d4838a823efbb77ff0ecd0cb598301e945bd8a17f232169`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit:
  [`162d4752ebc3652f277960f0278ecdbcd907ed74`](https://github.com/therealjameswilson/before-oss/commit/162d4752ebc3652f277960f0278ecdbcd907ed74).
- GitHub Actions Test run:
  [42056415916](https://github.com/therealjameswilson/before-oss/actions/runs/42056415916)
  completed successfully, including the Python suite, checked-in manifest
  verification, bounded browser release suite, rebuilt private-identifier
  audit source, and public redaction audit.
- GitHub Pages run:
  [42056415995](https://github.com/therealjameswilson/before-oss/actions/runs/42056415995)
  completed successfully for the same publication commit.
- Deployed-release verification matched all 67 canonical assets totaling
  143,182,314 bytes at manifest SHA-256
  `65b0f88a26db462a8b201a84a221acec976f21afb74029c35f2516035e4f096e`.
  The verifier also passed eight core routes, 47 source-register pages, and all
  46 newly updated direct profile URLs.
- Public base URL: <https://therealjameswilson.github.io/before-oss/>.
