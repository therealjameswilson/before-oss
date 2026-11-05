# Batch 1048 release audit

Date: 2026-11-05 America/New_York

## Release contents

- NARA index page 303, rows 1-46: Luigi Mazzone through Richard J. McCann.
  All 46 printed rows remain separately recoverable as 46 cautious person
  entities, and every entity has a saved terminal research outcome. Three
  existing conflict outcomes were preserved unchanged; the other 43 people
  received new reviewed outcomes.
- The full cohort contains 29 `requires_archival_review`, eight
  `occupation_only_found`, three `needs_identity_review`, two
  `verified_employer_found`, two `conflicting_sources`, one
  `documented_prewar_employer_found`, and one `needs_temporal_review` outcome.
- Eight accepted Army identity bridges support broad, date-bounded occupation
  categories only. They do not establish a named employer, institution,
  workplace, or immediate pre-OSS affiliation, and no protected identifier or
  raw Army row entered the public bundle.
- An official wartime report confirms Luigi Mazzone's U.S. Naval Reserve
  pathway into OSS and separately records his last civilian occupation as an
  unnamed Pennsylvania truck driver. It is not converted into a named
  employer.
- Turner H. McBaine's University of California oral history separates his
  Naval Reserve pathway, the Law Office of John Francis Neylan as his last
  civilian employer, and Orrick, Palmer & Dahlquist as earlier prewar work.
- William McAfee's Library of Congress/ADST oral history separates his China
  Theater assignment immediately before OSS, an unnamed local high school as
  his last civilian employer before the draft, and earlier teaching including
  Ewing Christian College.
- Smithsonian institutional research supports Nancy McCandlish's employment
  at the Smithsonian Astrophysical Observatory immediately before OSS. The
  separate Nancy M. McAnolish row remains ambiguous and receives none of that
  evidence.
- Frederica McAfee's WASP service is classified as a civilian government
  assignment, not commissioned military service. Its immediate relationship
  to OSS remains visibly qualified at medium confidence.
- William C. McAragle/McGaragle remains an identity conflict because a
  protected identifier resolves to a materially different surname. Dale
  McAdoo's official OSS memo supports a qualified identity finding only. Ward
  McCabe, William W. McCabe and Curtis B. McCammon retain their prior conflict
  outcomes unchanged. No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: 14 sources, seven organizations, 20 affiliations,
  26 claims, 61 claim-source links, 43 person updates, and 43 research
  attempts. All 20 public affiliations have claim-level citations.
- Evidence and person-state imports were tested twice against a disposable
  database and remained idempotent on re-import. The three protected prior
  outcomes remained unchanged in the comparison audit.
- A pre-import SQLite backup is retained outside the tracked release tree as
  `research-pre-batch1048-2026-11-05.sqlite`, SHA-256
  `1ff828ab243b323c9cc0b47f6121e3c52498751b3b2a159a5eea6874bc06e6ca`.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `54bc99a70202bacc61f7079a69a2e7c98334cd941125550c13d180f533f1331c`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,899/23,935 people (74.7817%). This value is unchanged
  because all 43 newly terminal people already had saved in-progress attempts.
- Verified affiliation: 1,246/23,935 people (5.2058%).
- Verified employer: 568/23,935 people (2.3731%).
- Archival disposition assessed: 16,533/23,935 people (69.0746%).
- Not started: 6,031 people; in progress: 1,702 people.
- Research outcomes include 2,265 `occupation_only_found`, 10,125
  `requires_archival_review`, 481 `verified_employer_found`, 307
  `documented_prewar_employer_found`, 660 `needs_identity_review`, 53
  `needs_temporal_review`, and 495 `conflicting_sources` people.
- Claim confidence: 2,044 confirmed; 5,655 high; 3,272 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,802 affiliations, 1,427 organizations,
  7,003 sources, and 11,447 published, qualified, or conflict claims.
- Citations: 8,298 across 4,674 unique source documents.
- Possible duplicate groups: 710. Total conflict flags: 579.
- Private derived exports contain 4,829 affiliations, 1,441 organizations,
  8,298 citation rows, 32,721 research attempts, 20,551 unresolved rows, and
  23,496 NARA pull-list rows.

## Local publication verification

- Python: 378 pytest cases and 87 subtests passed; the independent unittest
  discovery run also passed all 154 tests.
- Clean Astro check: 679 files with zero errors, warnings, or hints.
- Clean static build: 25,417 pages and 25,489 total output artifacts.
- Bounded browser release suite: 93/93 checks passed across desktop, phone,
  and tablet: 24 Batch 1048 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,417 HTML files checked; all links resolve. The checker
  inventoried 52,590 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 144,074,186 bytes, SHA-256
  `16b20afec3258b6b37d14ead76cbb913c9a8df0628f99b7ac3164a2b926815f3`.
- Public-identifier audit: 25,489 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,593 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,489 artifacts totaling
  441,268,102 bytes at output-tree SHA-256
  `bd2427e7569980f57d48753afc89ace0090acd33679deb9c304c9598d410f8ff`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.
- The production dependency audit found zero vulnerabilities.

## Deployment status

- Publication is awaiting the immutable Git commit, GitHub Actions Test and
  Pages runs, and deployed-release verification.
- Public base URL: <https://therealjameswilson.github.io/before-oss/>.
