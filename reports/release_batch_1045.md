# Batch 1045 release audit

Date: 2026-11-05 America/New_York

## Release contents

- NARA index page 300, rows 1-46: Steve P. Mathiakes through Leonard J.
  Matuszek. All 46 printed rows remain separately recoverable as 46 cautious
  person entities, and every entity has a saved terminal research outcome.
- The cohort contains 28 `requires_archival_review`, 16
  `occupation_only_found`, and two `needs_identity_review` outcomes.
- Fifteen protected-linkage Army candidates received explicit review and were
  accepted on the strength of nonshared protected identifiers plus indexed
  name agreement. No protected identifier is present in the public bundle.
- Reviewed Army code-list evidence supports only broad, date-bounded
  occupation or student categories. It does not establish a named employer,
  institution, workplace, or immediate pre-OSS affiliation.
- Official Army history supports a qualified immediate pre-OSS military
  pathway for Charles Y. Matsunaka: U.S. Army service in India before he
  volunteered to replace OSS personnel in Burma. The source does not identify
  his precise pre-OSS unit, so no narrower assignment is asserted.
- Wartime evidence identifies Joseph Matovich in an OSS communications team
  that reached Kunming from Cairo after North Africa and Mediterranean work.
  It strengthens identity and service context but does not identify a
  pre-OSS employer.
- Arturo Carlo-Felice Mathieu is published with a qualified language-teacher
  occupation and separate Princeton graduate-student affiliation. Princeton
  is not represented as an employer.
- The adjacent Eugene K. Matthews captain and second-lieutenant rows remain
  separate because their protected identifiers differ. One has an ambiguous
  spelling-variant lead and the other conflicts with a different indexed
  name; neither received transferred occupation evidence.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: nine sources, two organizations, 18 affiliations,
  23 claims, 78 claim-source links, 46 person updates, and 46 research
  attempts. All 18 public affiliations have claim-level citations.
- Fifteen Army identity-review decisions were imported and accepted. Decision
  and evidence imports were tested against a disposable database and remained
  idempotent on re-import.
- A pre-import SQLite backup is retained outside the tracked release tree as
  `research-pre-batch1045-2026-11-05.sqlite`, SHA-256
  `03c1738af6407b29e026087b89fdb93cd721d2ccc7fccfb7e1735904a385554a`.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `aa2ba6ec71f495a8c1092a908e6800a84b70359b2a9bc6b4b4ea15fc4bb24cf2`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,899/23,935 people (74.7817%).
- Verified affiliation: 1,240/23,935 people (5.1807%).
- Verified employer: 565/23,935 people (2.3606%).
- Archival disposition assessed: 16,406/23,935 people (68.5440%).
- Not started: 6,031 people; in progress: 1,831 people.
- Research outcomes include 2,235 `occupation_only_found`, 10,038
  `requires_archival_review`, 479 `verified_employer_found`, 304
  `documented_prewar_employer_found`, 655 `needs_identity_review`, 52
  `needs_temporal_review`, and 495 `conflicting_sources` people.
- Claim confidence: 2,038 confirmed; 5,636 high; 3,240 medium; 261 low; 477
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,757 affiliations, 1,423 organizations,
  6,974 sources, and 11,387 published, qualified, or conflict claims.
- Citations: 8,267 across 4,655 unique source documents.
- Possible duplicate groups: 708. Total conflict flags: 579.
- Private derived exports contain 4,784 affiliations, 1,437 organizations,
  8,267 citation rows, 32,543 research attempts, 20,587 unresolved rows, and
  23,498 NARA pull-list rows.

## Local publication verification

- Python: 347 pytest cases and 87 subtests passed; the independent unittest
  discovery run also passed all 154 tests.
- Clean Astro check: 676 files with zero errors, warnings, or hints.
- Clean static build: 25,413 pages and 25,485 total output artifacts.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1045 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,413 HTML files checked; all links resolve. The checker
  inventoried 52,575 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 143,579,067 bytes, SHA-256
  `ef29528da79955fd16682c84126f7f2b85b330cd3df4b147e9ac51c63c7e4bb0`.
- Public-identifier audit: 25,485 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,586 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,485 artifacts totaling
  440,462,765 bytes at output-tree SHA-256
  `27020fe990a2b2903ebc597f29bdfe1538eb80bafd2e40c04ee479fbbdba0121`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit: pending.
- GitHub Actions Test run: pending.
- GitHub Pages run: pending.
- Deployed-release verification: pending.
- Public base URL: <https://therealjameswilson.github.io/before-oss/>.
