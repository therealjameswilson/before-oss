# Batch 1050 release audit

Research and release date: 2026-11-11 America/New_York.

## Release contents

- NARA index page 305, rows 1-46: Margaret J. McClellan through Charles H.
  McCormick. All 46 printed rows remain separately recoverable as 46 cautious
  person entities, and every entity has a saved terminal research outcome.
- The cohort contains 33 `requires_archival_review`, nine
  `occupation_only_found`, three `verified_employer_found`, and one
  `conflicting_sources` outcome.
- Ten accepted Army identity bridges support broad, date-bounded occupation
  or student categories only. They do not establish a named employer,
  institution, workplace, or immediate pre-OSS affiliation. Oscar D.
  McCollum's accepted Army entry is dated 27 April 1946, so its draftsman code
  is withheld from pre-OSS publication pending a service chronology.
- Institutional and contemporary sources support three verified-employer
  profiles. Stewart McClintic's Mellon National Bank and Trust Company
  employment remains separate from his immediate VIII Bomber Command
  pathway. Harold C. McCollom Jr.'s Benton & Bowles account-executive role is
  sequenced before two years of military service without inferring an OSS
  unit. James Lukens McConaughy's United China Relief presidency is modeled
  as his immediate professional affiliation, while Wesleyan University is his
  probable last civilian employer and his earlier academic employment remains
  separate.
- Repeated and similar-name rows remain separate where direct evidence does
  not justify a merge. The Elmer L. McCcollum/McCollum spelling and rank
  conflict remains visible.
- No protected identifier, raw Army row, full copyrighted source, or
  authenticated NARA Catalog API payload entered public data. No authenticated
  NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: eight sources, eight organizations, 18
  affiliations, 20 claims, 57 claim-source links, 46 person updates, and 46
  research attempts. All 18 public affiliations have claim-level citations.
- Evidence and person-state imports were tested twice against disposable
  databases and remained idempotent on re-import.
- The durable post-import SQLite database has SHA-256
  `b22988a5f3434c30f59be56766eb2798b46155fd75fbfb51e85c333f40d0fbdd`.
  The transient pre-import backup had SHA-256
  `b178ea4a160d789bb518986f60bf2887f487971e00a0ac1369ab7c5966f39acf`.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations, and there are zero uncited public claims.
- Evidence-bundle SHA-256:
  `b941eda0baf1410394b5f1e6ea9607b8bfa0112b3dbca863495289481ddae7f6`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,899/23,935 people (74.7817%). This value is unchanged
  because every newly terminal person already had a saved earlier attempt.
- Verified affiliation: 1,250/23,935 people (5.2225%).
- Verified employer: 572/23,935 people (2.3898%).
- Archival disposition assessed: 16,607/23,935 people (69.3837%).
- Not started: 6,031 people; in progress: 1,627 people.
- Research outcomes include 2,284 `occupation_only_found`, 10,182
  `requires_archival_review`, 484 `verified_employer_found`, 308
  `documented_prewar_employer_found`, 653 `needs_identity_review`, 53
  `needs_temporal_review`, and 497 `conflicting_sources` people.
- Claim confidence: 2,047 confirmed; 5,665 high; 3,292 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,832 affiliations, 1,430 organizations,
  7,016 sources, and 11,480 published, qualified, or conflict claims.
- Citations: 8,311 across 4,680 unique source documents.
- Possible duplicate groups: 710. Total conflict flags: 580.
- Private derived exports contain 4,859 affiliations, 1,444 organizations,
  32,813 research attempts, 20,528 unresolved rows, 23,493 NARA pull-list
  rows, and 7,364 Army review-queue rows.

## Local publication verification

- Python: 392 pytest cases and 87 subtests passed; independent unittest
  discovery also passed all 154 tests.
- SQLite integrity is `ok`, foreign-key violations are zero, and uncited
  published, publish-qualified, or conflict claims are zero.
- Clean Astro check: 681 files with zero errors, warnings, or hints.
- Clean static build: 25,420 pages and 25,492 total output artifacts.
- Bounded browser release suite: 87/87 checks passed across desktop, phone,
  and tablet: 18 Batch 1050 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,420 HTML files checked; all links resolve. The checker
  inventoried 52,597 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 144,375,604 bytes,
  SHA-256
  `f5789e120d94e43b343b304cc851ad40bf5ba7b8b846f0484daa7ec49e50f586`.
- Public-identifier audit: 25,492 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,586 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,492 artifacts totaling
  441,756,595 bytes at output-tree SHA-256
  `139f29434cb0fb65d31ab764d48163c6708f98c43f6d049790c5e540610fc0c5`.
- The deterministic 200-profile stratified audit passed all defined gates.
- The production dependency audit found zero vulnerabilities.

## Deployment status

- Publication commit:
  [`b440f0dffb8322be5d0d4347db48eed2992668a8`](https://github.com/therealjameswilson/before-oss/commit/b440f0dffb8322be5d0d4347db48eed2992668a8).
- GitHub Actions Test run
  [43020123006](https://github.com/therealjameswilson/before-oss/actions/runs/43020123006)
  completed successfully, including the Python suite, checked-in manifest
  verification, bounded browser release suite, rebuilt private-identifier
  audit source, and public redaction audit.
- GitHub Pages run
  [43020122651](https://github.com/therealjameswilson/before-oss/actions/runs/43020122651)
  completed successfully for the same publication commit.
- Deployed-release verification matched all 67 canonical assets totaling
  144,375,604 bytes at manifest SHA-256
  `f5789e120d94e43b343b304cc851ad40bf5ba7b8b846f0484daa7ec49e50f586`.
  The verifier also passed eight core routes, 47 source-register pages, and all
  46 newly updated direct profile URLs.

Public base URL: <https://therealjameswilson.github.io/before-oss/>.
