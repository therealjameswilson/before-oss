# Batch 1036 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 291, rows 1-46: Sylvester Maiza through William J. Malone.
  All 46 rows remain separately recoverable as 46 cautious person entities,
  and all now have saved terminal research outcomes.
- The cohort contains 23 `requires_archival_review`, 15
  `occupation_only_found`, seven `needs_identity_review`, and one `completed`
  outcome.
- Eighteen protected-identifier Army candidates received explicit review: 17
  were accepted and one materially different Thomas B. Majure candidate was
  rejected. No fields were transferred from the rejected candidate.
- Fifteen accepted Army-entry records support broad, date-bounded occupation
  or student categories only; no coded occupation was converted into a named
  employer, institution, workplace, or immediate pre-OSS affiliation.
- Toivo W. Maki's June 1945 Army record supports identity only because the
  chronology is unsafe for a pre-OSS claim. Clarence J. Malakowsky's undefined
  occupation code remains uninterpreted.
- A Congressional Record chronology identifies Wilfred Malenbaum as an Office
  of Price Administration economist in 1941 before his 1941-45 OSS service.
  OPA is modeled as a probable immediate government assignment; Harvard is
  retained separately as documented student status, not employment.
- A direct OSS Greek Operational Group roster confirms Lambros G. Makris's
  identity. A historical BCRA/SOE infiltration table supports Maxime
  Malfettes, Tartuffe, and Maxime Brunet at high identity confidence. Neither
  source establishes a pre-OSS employer.
- John Malandre/John Malanore, Victor Malaspina/Victor Malispino, and Patricia
  C. Malmsted/Patricia C. Malmstedt remain separate person entities in three
  visible possible-duplicate groups.
- Gene Mako and Julius B. Maller remain ambiguous; famous or professional
  biographies were not assigned by name alone.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: eight sources, two organizations, 17
  affiliations, 22 claims, 75 claim-source links, 46 person updates, and 46
  research attempts.
- Eighteen Army identity-review decisions were imported. Decision and evidence
  imports were tested against a disposable database before the durable update.
- A pre-import SQLite backup is retained at
  `/private/tmp/before-oss-pre-b1036-20261104.sqlite` for local recovery.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations; all 22 new claims have citation links.
- Evidence-bundle SHA-256:
  `3ef2bc747c7aec091ac88a1b8dc7948f6aff7a8bb4002bf67cb7588a533fcc08`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,492/23,935 people (73.0813%).
- Verified affiliation: 1,224/23,935 people (5.1139%).
- Verified employer: 558/23,935 people (2.3313%).
- Archival disposition assessed: 16,013/23,935 people (66.9020%).
- Not started: 6,438 people; in progress: 1,832 people.
- Research outcomes include 2,106 `occupation_only_found`, 9,813
  `requires_archival_review`, 470 `verified_employer_found`, 298
  `documented_prewar_employer_found`, 629 `needs_identity_review`, 50
  `needs_temporal_review`, and 487 `conflicting_sources` people.
- Claim confidence: 2,020 confirmed; 5,602 high; 3,098 medium; 261 low; 473
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,600 affiliations, 1,401
  organizations, 6,884 sources, and 11,189 published, qualified, or conflict
  claims.
- Citations: 8,177 across 4,599 unique source documents.
- Possible duplicate groups: 702. Total conflict flags: 567.

## Local publication verification

- Python: 276 pytest cases and 87 subtests passed.
- Clean Astro check: 667 files with zero errors, warnings, or hints.
- Clean static build: 25,390 pages and 25,462 total output artifacts.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1036 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,390 HTML files checked; all links resolve. The checker
  inventoried 52,514 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 141,777,611 bytes,
  SHA-256
  `68db635e63266f9c99d37722e85d6e418d6db88f0969531a36980521ae4bdd66`.
- Public-identifier audit: 25,462 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,583 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,462 artifacts totaling
  437,444,272 bytes at output-tree SHA-256
  `bc87a0fec46d4a3b69495453a731e16dba718753d58356d3b60779a1cfec059d`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit: pending.
- GitHub Actions Test run: pending.
- GitHub Pages run: pending.
- Deployed immutable-release verification: pending.
- Public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
