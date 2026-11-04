# Batch 1026 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 516, rows 1-46: William J. Wynn through George Yasukochi.
  All 46 printed rows remain separately recoverable as 46 cautious person
  entities, including the incomplete printed `* X` row.
- Every cohort person has a saved terminal outcome: 25
  `requires_archival_review`, 12 `occupation_only_found`, three
  `needs_identity_review`, two `documented_prewar_employer_found`, one
  `completed`, one `conflicting_sources`, one `needs_temporal_review`, and one
  `verified_employer_found`.
- Eleven protected-identifier Army candidates were accepted. The John Yarmey
  candidate was rejected because the protected identifier points to a record
  for Louis M. Fossarelli; no evidence was transferred between those people.
  Full identifiers remain private.
- Bernard Yarrow's official Eisenhower Library finding aid explicitly dates
  his work in the New York County District Attorney's office through November
  1942 and states that he resigned to join the OSS. The evidence supports the
  office as both his immediate pre-OSS affiliation and last civilian employer.
- Waseda University explicitly identifies `Ohitoshi Yanaga` as a misspelling
  of Chitoshi Yanaga. Its dated chronology, corroborated by official CIA FBIS
  history, supports the Foreign Broadcast Intelligence Service as Yanaga's
  immediate pre-OSS government affiliation and the University of California,
  Berkeley, as his last documented civilian employer before wartime service.
  The original index spelling remains visible.
- Teizo Yahanda, Sannosuke Yamamoto, Tomomasa Yamazaki, and Adam Yarmolinsky
  have qualified identity or chronology evidence, but none is presented as a
  settled immediate pre-OSS employer without a direct bridge.
- Sumner J. Yaffe's Harvard status is modeled as `student`, not employment.
- Louis J. Xanthopoulos has an exact Army match and direct official evidence of
  OSS 31st Field Detachment battle participation; the record does not infer a
  civilian employer.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: 16 sources, 14 organizations, 25 affiliations, 34
  claims, 77 claim-source links, 46 person updates, and 46 research attempts.
- Twelve Army identity-review decisions were imported: 11 accepted and one
  rejected.
- The import was tested twice against a disposable database before the durable
  database update. The second import was idempotent.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `edcfdde8a9fc287a2cfa4c71ff7f4f176abca96ec8f67e9a547e030a0bbb38de`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,116/23,935 people (71.5103%).
- Verified affiliation: 1,200/23,935 people (5.0136%).
- Verified employer: 551/23,935 people (2.3021%).
- Archival disposition assessed: 15,597/23,935 people (65.1640%).
- Not started: 6,814 people; in progress: 1,879 people.
- Research outcomes include 1,967 `occupation_only_found`, 9,579
  `requires_archival_review`, 463 `verified_employer_found`, 297
  `documented_prewar_employer_found`, 607 `needs_identity_review`, and 480
  `conflicting_sources` people.
- Claim confidence: 2,010 confirmed; 5,540 high; 2,945 medium; 261 low; 465
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,420 affiliations, 1,382 organizations,
  6,778 sources, and 10,956 published, qualified, or conflict claims.
- Citations: 8,071 across 4,534 unique source documents.
- Possible duplicate groups: 697. Total conflict flags: 560.

## Local publication verification

- Python: all 189 tests passed, including 87 subtests. The Batch 1026
  generator's six focused tests and complete schema validation are included.
- Clean Astro check: 657 files with zero errors, warnings, or hints.
- Clean static build: 25,371 pages.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1026 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,371 HTML files checked; all links resolve. The checker
  inventoried 52,449 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 139,825,103 bytes,
  SHA-256
  `a2e3f2b5eb7c3961f14b95e3ae356f6864d24ef34feb182eaf760a459279c303`.
- Public-identifier audit: 25,443 public artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,583 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,443 artifacts totaling
  434,206,375 bytes at output-tree SHA-256
  `4337bd6023a9631f5af5c7364708acf6c6cb3505f1e22522159eadb61caedf7c`.

## Public deployment verification

Publication and immutable live verification are pending the Batch 1026 content
commit and GitHub Pages workflows.
