# Batch 1028 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 518, rows 1-46: Cecile W. Youmanns through Renie Yuen.
  All 46 printed rows remain separately recoverable as 46 cautious person
  entities. The page 519 boundary was also visually checked.
- Every cohort person has a saved terminal outcome: 31
  `requires_archival_review`, 13 `occupation_only_found`, and two
  `verified_employer_found`.
- Fourteen protected-identifier Army candidates received explicit review and
  were accepted. Name damage and a middle-initial conflict for Billy B. Young,
  and an omitted middle initial for James B. Young, remain explicit. Neither
  an undefined category nor a post-OSS Army entry was converted into a
  pre-OSS occupation claim.
- T. Cuyler Young's University of Toronto faculty role is modeled as both the
  best-supported immediate affiliation and last civilian employer. The
  memorial supports a 1938 start but not an exact end or OSS appointment date,
  so no end date is inferred.
- Evelle J. Younger's FBI section-chief role is modeled as federal civilian
  service, immediate affiliation, and last civilian employer. No commissioned
  status is inferred from his later military career.
- Rodney Stuart Young's Greek Red Cross ambulance work is modeled as volunteer
  service rather than employment. His American School of Classical Studies
  relationship is a separate professional affiliation and not an employer.
- Dr. Peter Yovanovich's direct OSS-era record supports physician status and a
  recruitment context, but no named employer or exact recruitment disposition.
  The original indexed form `Peter, Dr. Yovanovich` remains visible alongside
  documented search and display variants.
- Historical filling-station and petroleum-refining occupation codes were not
  treated as oil-company or named-employer evidence.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: ten sources, four organizations, 17 affiliations,
  25 claims, 61 claim-source links, 46 person updates, and 46 research
  attempts.
- Fourteen Army identity-review decisions were imported and the evidence
  import was tested twice against a disposable database before the durable
  database update. The second import was idempotent.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `ebe2b437d6029621029c0e0cf3e7d059af4f3dcda517b3de9582ffe456781131`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,208/23,935 people (71.8947%).
- Verified affiliation: 1,206/23,935 people (5.0386%).
- Verified employer: 553/23,935 people (2.3104%).
- Archival disposition assessed: 15,689/23,935 people (65.5484%).
- Not started: 6,722 people; in progress: 1,879 people.
- Research outcomes include 1,990 `occupation_only_found`, 9,640
  `requires_archival_review`, 466 `verified_employer_found`, 297
  `documented_prewar_employer_found`, 608 `needs_identity_review`, 43
  `needs_temporal_review`, and 481 `conflicting_sources` people.
- Claim confidence: 2,011 confirmed; 5,559 high; 2,974 medium; 261 low; 465
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,454 affiliations, 1,384 organizations,
  6,798 sources, and 11,005 published, qualified, or conflict claims.
- Citations: 8,091 across 4,546 unique source documents.
- Possible duplicate groups: 698. Total conflict flags: 561.

## Local publication verification

- Python: all 206 tests and 87 subtests passed. Batch 1028's eight focused
  unit tests and complete evidence-schema validation are included.
- Clean Astro check: 658 files with zero errors, warnings, or hints.
- Clean static build: 25,373 pages.
- Bounded browser release suite: 93/93 checks passed across desktop, phone,
  and tablet: 24 Batch 1028 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,373 HTML files checked; all links resolve. The checker
  inventoried 52,459 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 140,210,929 bytes,
  SHA-256
  `50e0d61b88447f851cb5bb45cfa529d52477724a7fe865c0abd4a830d45ddf22`.
- Public-identifier audit: 25,445 public artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,582 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,445 artifacts totaling
  434,839,884 bytes at output-tree SHA-256
  `3dffe9065a09ba354b0543a91e1399be1a548924c17dad222642dd0e31881528`.

## Deployment status

- Local release gates pass. Publication commit, GitHub Actions test and Pages
  deploy runs, and immutable live-manifest verification will be appended after
  the release is pushed.
- Public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
