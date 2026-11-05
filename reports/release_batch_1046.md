# Batch 1046 release audit

Date: 2026-11-05 America/New_York

## Release contents

- NARA index page 301, rows 1-46: Josef Matuszowicz through Lewis L. May.
  All 46 printed rows remain separately recoverable as 45 cautious person
  entities, and every entity has a saved terminal research outcome. The two
  Joseph P. Mauro rows remain immutable source records linked to one person
  only because the exact name and nonshared protected identifier agree.
- The cohort contains 28 `requires_archival_review`, 14
  `occupation_only_found`, two `needs_identity_review`, and one
  `conflicting_sources` outcome.
- Seventeen prior protected-linkage Army candidates were explicitly reviewed:
  15 were accepted, Erwin Mauss remains conflicting, and the MAXWELC CHARLES R
  candidate for Charles Maxwell remains probable and private. No protected
  identifier is present in the public bundle.
- Reviewed Army code-list evidence supports 14 broad, date-bounded occupation
  or student categories. It does not establish a named employer, institution,
  workplace, or immediate pre-OSS affiliation. Code 993 for Joseph P. Mautner
  remains uninterpreted because no sufficiently reliable definition was found
  in the reviewed list.
- An official declassified RG 226 Detachment 101 promotion-board record
  confirms Floyd E. Maves's wartime identity and corporal-to-sergeant
  progression in April 1945. It does not identify a pre-OSS employer or
  predecessor affiliation.
- The officer and enlisted Georges May rows remain separate because their
  ranks and protected identifiers differ. Only the enlisted row has an
  accepted Army bridge, which adds middle initial C and a qualified
  secondary-school-teacher-or-principal category.
- Direct CIA adapter access failed closed under the current robots policy. The
  access restriction was recorded and was not converted into a negative
  biographical result. No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: five sources, no new organizations, 14
  affiliations, 19 claims, 67 claim-source links, 45 person updates, and 45
  research attempts. All 14 public affiliations have claim-level citations.
- Evidence and person-state imports were tested twice against a disposable
  database and remained idempotent on re-import.
- A pre-import SQLite backup is retained outside the tracked release tree as
  `research-pre-batch1046-2026-11-05.sqlite`, SHA-256
  `b43943edae816cc849668a51a4dc5f32ce569d4bda1db964219e739c5913ac4b`.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `00fd515e449f5490d9e8259353a7535fb6f5fbd1e034008c9254bd88bf7a4ea0`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,899/23,935 people (74.7817%).
- Verified affiliation: 1,240/23,935 people (5.1807%).
- Verified employer: 565/23,935 people (2.3606%).
- Archival disposition assessed: 16,447/23,935 people (68.7153%).
- Not started: 6,031 people; in progress: 1,789 people.
- Research outcomes include 2,249 `occupation_only_found`, 10,066
  `requires_archival_review`, 479 `verified_employer_found`, 304
  `documented_prewar_employer_found`, 655 `needs_identity_review`, 52
  `needs_temporal_review`, and 495 `conflicting_sources` people.
- Claim confidence: 2,039 confirmed; 5,637 high; 3,254 medium; 262 low; 479
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,771 affiliations, 1,423 organizations,
  6,979 sources, and 11,405 published, qualified, or conflict claims.
- Citations: 8,272 across 4,657 unique source documents.
- Possible duplicate groups: 708. Total conflict flags: 579.
- Private derived exports contain 4,798 affiliations, 1,437 organizations,
  8,272 citation rows, 32,634 research attempts, 20,573 unresolved rows, and
  23,498 NARA pull-list rows.

## Local publication verification

- Python: 356 pytest cases and 87 subtests passed; the independent unittest
  discovery run also passed all 154 tests.
- Clean Astro check: 677 files with zero errors, warnings, or hints.
- Clean static build: 25,413 pages and 25,485 total output artifacts.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1046 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,413 HTML files checked; all links resolve. The checker
  inventoried 52,575 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 143,722,382 bytes, SHA-256
  `db27c78dcbe63e93d08e82fd165df9548f9e7d02cae2173ce2cf7c495266a3e0`.
- Public-identifier audit: 25,485 output artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,586 candidate substrings, allowed two manifest-size coincidences, and found
  zero aggregate or unexpected boundary matches.
- Two consecutive local builds reproduced 25,485 artifacts totaling
  440,698,297 bytes at output-tree SHA-256
  `4b4d77ecb63fa26eab08ee7e242b2a963dbd2b3c88de7b10f7b6ddee5ef5ee22`.
- The complete 522-page ingest audit and deterministic 200-profile stratified
  audit passed all defined gates.

## Deployment status

- Publication commit: pending.
- GitHub Actions Test run: pending.
- GitHub Pages run: pending.
- Deployed-release verification: pending.
- Public base URL: <https://therealjameswilson.github.io/before-oss/>.
