# Batch 1049 release audit

Research date: 2026-11-06 America/New_York.

Release date: 2026-11-11 America/New_York

## Release contents

- NARA index page 304, rows 1-46: Thomas A. McCann through Grant S.
  McClelian. All 46 printed rows remain separately recoverable as 46 cautious
  person entities, and every entity has a saved terminal research outcome.
- The cohort contains 24 `requires_archival_review`, ten
  `needs_identity_review`, ten `occupation_only_found`, one
  `documented_prewar_employer_found`, and one `conflicting_sources` outcome.
- Ten accepted Army identity bridges support broad, date-bounded occupation
  or student categories only. They do not establish a named employer,
  institution, workplace, or immediate pre-OSS affiliation.
- An official 3 May 1944 OSS board report confirms Thomas A. McCart's transfer
  from the Vth Army Replacement Center on 12 October 1943 and separately
  documents RCA employment in civilian life. The Army pathway is explicit
  immediate evidence; RCA remains other documented prewar employment rather
  than an unsupported last-civilian-employer claim.
- Rex H. McCauley's protected identifier conflicts with an official Army
  record for a different person. Similar spellings, repeated names, and
  common-name candidates remain separate and visibly reviewable.
- No protected identifier, raw Army row, or authenticated NARA Catalog API
  payload entered public data. No authenticated NARA Catalog API request was
  used.

## Evidence and import

- Reviewed evidence bundle: five sources, two organizations, 12 affiliations,
  13 claims, 44 claim-source links, 46 person updates, and 46 research
  attempts. All 12 public affiliations have claim-level citations.
- Evidence and person-state imports were tested twice against a disposable
  database and remained idempotent on re-import.
- The durable post-import SQLite database has SHA-256
  `1f12f33f4e2b2d5cc1d54f123b3f8e612d20b0976e014f07c8cb12dc88fe4948`.
  The transient pre-import backup was observed at SHA-256
  `f14813a48b35f6245a6e52bff03a0c38d272ced7987b34c4072a36a439d05898`
  before the temporary release workspace was automatically pruned; it is not
  represented as a retained artifact.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations, and there are zero uncited public claims.
- Evidence-bundle SHA-256:
  `80a1d4905ca4c80e797467464db7c0c9dd323c823d6b3ea46ffea563c220c050`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,899/23,935 people (74.7817%). This value is unchanged
  because every newly terminal person already had a saved earlier attempt.
- Verified affiliation: 1,247/23,935 people (5.2099%).
- Verified employer: 569/23,935 people (2.3773%).
- Archival disposition assessed: 16,567/23,935 people (69.2166%).
- Not started: 6,031 people; in progress: 1,667 people.
- Research outcomes include 2,275 `occupation_only_found`, 10,149
  `requires_archival_review`, 481 `verified_employer_found`, 308
  `documented_prewar_employer_found`, 659 `needs_identity_review`, 53
  `needs_temporal_review`, and 496 `conflicting_sources` people.
- Claim confidence: 2,046 confirmed; 5,656 high; 3,282 medium; 263 low; 480
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,814 affiliations, 1,427 organizations,
  7,008 sources, and 11,460 published, qualified, or conflict claims.
- Citations: 8,303 across 4,675 unique source documents.
- Possible duplicate groups: 710. Total conflict flags: 579.
- Private derived exports contain 4,841 affiliations, 1,441 organizations,
  8,303 citation rows, 32,767 research attempts, 20,540 unresolved rows, and
  23,496 NARA pull-list rows.

## Local publication verification

- Python: 385 pytest cases and 87 subtests passed; independent unittest
  discovery also passed all 154 tests.
- SQLite integrity is `ok`, foreign-key violations are zero, and uncited
  published or publish-qualified claims are zero.
- Clean Astro check: 680 files with zero errors, warnings, or hints.
- Clean static build: 25,417 pages and 25,489 total output artifacts.
- Bounded browser release suite: 81/81 checks passed across desktop, phone,
  and tablet: 12 Batch 1049 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,417 HTML files checked; all links resolve. The checker
  inventoried 52,590 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 144,190,105 bytes,
  SHA-256
  `c9912c371b131d6c7e220a21d9438c073b1cc6accbf14cb39570a734908a250c`.
- Public-identifier audit: 25,489 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,588 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,489 artifacts totaling
  441,453,638 bytes at output-tree SHA-256
  `d16d4f9a080f6c88092259578005816b720a5b820ef59aae68cab3348e3c7ac9`.
- The deterministic 200-profile stratified audit passed all defined gates.
- The production dependency audit found zero vulnerabilities.

## Deployment status

Publication, GitHub Actions, Pages deployment, and immutable live-manifest
verification are pending the release commit.

Public base URL: <https://therealjameswilson.github.io/before-oss/>.
