# Batch 1044 release audit

Date: 2026-11-05 America/New_York

## Release contents

- NARA index page 299, rows 1-46: Nicholas G. Maslikosa through William A.
  Mathewson. All 46 printed rows remain separately recoverable as 46 cautious
  person entities, and every entity has a saved terminal research outcome.
- The cohort contains 28 `requires_archival_review`, 14
  `occupation_only_found`, two `verified_employer_found`, and two
  `needs_identity_review` outcomes. Edward S. Mason retained his existing
  verified evidence without duplicate claims or affiliations.
- Fifteen protected-linkage Army candidates received explicit review: 14 were
  accepted and one was rejected. The rejected Eugene K. Mathews candidate
  transferred no Army fields because the protected identifiers conflict.
- Reviewed Army code-list evidence supports only broad, date-bounded
  occupation or student categories. It does not establish a named employer,
  institution, workplace, or immediate pre-OSS affiliation.
- The best-supported immediate pathway for Albert R. Materazzi is a 1942 Army
  engineering assignment preceding his documented early-1943 OSS recruitment.
  His Army Map Service chemist role in 1940 is published separately as the last
  identified civilian employer at medium confidence; continuity through his
  1942 commission is not assumed.
- Distinctive wartime evidence strengthened the identities of Nicholas G.
  Maslikosa, Edward S. Maslowsky, and Steve J. Mastros but did not identify a
  predecessor employer. Thomas Masuda remains ambiguous, and the contemporary
  attorney lead transferred no profession or employer.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: ten sources, two organizations, 16 affiliations,
  21 claims, 72 claim-source links, 46 person updates, and 46 research
  attempts. All 16 public affiliations have claim-level citations.
- Fifteen Army identity-review decisions were imported: 14 accepted and one
  rejected. Decision and evidence imports were tested against a disposable
  database and remained idempotent on re-import.
- A pre-import SQLite backup is retained outside the tracked release tree as
  `research-pre-batch1044-2026-11-05.sqlite`, SHA-256
  `3eb5c8b70ab0fafabad8f1f6cabd4ab7ee032644e298704b150393f946990baa`.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `5c163d94fbf892a381546debcea257bda0bdb0d4ce41139a165e77c057492832`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,853/23,935 people (74.5895%).
- Verified affiliation: 1,239/23,935 people (5.1765%).
- Verified employer: 565/23,935 people (2.3606%).
- Archival disposition assessed: 16,362/23,935 people (68.3601%).
- Not started: 6,077 people; in progress: 1,831 people.
- Research outcomes include 2,219 `occupation_only_found`, 10,010
  `requires_archival_review`, 479 `verified_employer_found`, 304
  `documented_prewar_employer_found`, 653 `needs_identity_review`, 52
  `needs_temporal_review`, and 495 `conflicting_sources` people.
- Claim confidence: 2,037 confirmed; 5,633 high; 3,223 medium; 261 low; 475
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,739 affiliations, 1,421 organizations,
  6,965 sources, and 11,364 published, qualified, or conflict claims.
- Citations: 8,258 across 4,652 unique source documents.
- Possible duplicate groups: 708. Total conflict flags: 579.
- Private derived exports contain 4,766 affiliations, 1,435 organizations,
  8,258 citation rows, 32,497 research attempts, 20,603 unresolved rows, and
  23,498 NARA pull-list rows.

## Local publication verification

- Python: 337 pytest cases and 87 subtests passed.
- Clean Astro check: 674 files with zero errors, warnings, or hints.
- Clean static build: 25,411 pages and 25,483 total output artifacts.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1044 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,411 HTML files checked; all links resolve. The checker
  inventoried 52,571 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 143,377,424 bytes, SHA-256
  `8f3a10c45e618e6ec39d59b768d193dbe912d55b6089d475b217ea3a19439d4c`.
- Public-identifier audit: 25,483 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,586 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,483 artifacts totaling
  440,125,646 bytes at output-tree SHA-256
  `87ac16d6331f590d1835016da3d4fc9960936603e46ef2376be2974808c1cfa9`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit: pending.
- GitHub Actions Test run: pending.
- GitHub Pages run: pending.
- Public base URL: <https://therealjameswilson.github.io/before-oss/>.
