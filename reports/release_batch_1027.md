# Batch 1027 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 517, rows 1-46: Janet C. Yasunobu through Merle S.
  Youkers. All 46 printed rows remain separately recoverable as 46 cautious
  person entities.
- Every cohort person has a saved terminal outcome: 30
  `requires_archival_review`, ten `occupation_only_found`, three
  `needs_temporal_review`, one `needs_identity_review`, one
  `verified_employer_found`, and one `conflicting_sources`.
- Eleven protected-identifier Army candidates received explicit review: ten
  were accepted and one was rejected. The rejected Merle S. Youkers candidate
  names Roger E. McCarren in the Army source; no evidence was transferred.
- Ralph T. Yempuku's 442d Regimental Combat Team assignment is modeled as his
  documented immediate military predecessor to OSS recruitment. The
  University of Hawaii is separately modeled as his last civilian employer.
- David N. Yerkes's Yale relationship is student status rather than
  employment. His Army Corps of Engineers pathway remains qualified because
  the accessible federal biography supplies sequence but no transfer date.
- Arden Yinkley's War Production Board role, Jutaro Yokoi's Methodist
  ministry, and Takehiko Yoshihashi's Office of War Information translation
  work remain qualified where identity or OSS timing is unresolved.
- A reproduced direct OSS travel order strengthens the identities of Shizuo
  Yoshida and the indexed `Usuda Yoshisada`; it does not establish either
  person's pre-OSS employer. The original index spelling remains visible and
  `Yoshisada Katoi Usuda` is preserved as a documented variant.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: ten sources, seven organizations, 17
  affiliations, 24 claims, 54 claim-source links, 46 person updates, and 46
  research attempts.
- Eleven Army identity-review decisions were imported: ten accepted and one
  rejected.
- The import was tested twice against a disposable database before the durable
  database update. The second import was idempotent.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `ec2e35d9ba3b64e54a57321178a853670679c561ee92367a5588bda18f93fc5d`.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,162/23,935 people (71.7025%).
- Verified affiliation: 1,202/23,935 people (5.0219%).
- Verified employer: 552/23,935 people (2.3062%).
- Archival disposition assessed: 15,643/23,935 people (65.3562%).
- Not started: 6,768 people; in progress: 1,879 people.
- Research outcomes include 1,977 `occupation_only_found`, 9,609
  `requires_archival_review`, 464 `verified_employer_found`, 297
  `documented_prewar_employer_found`, 608 `needs_identity_review`, 43
  `needs_temporal_review`, and 481 `conflicting_sources` people.
- Claim confidence: 2,010 confirmed; 5,547 high; 2,962 medium; 261 low; 465
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,437 affiliations, 1,383 organizations,
  6,788 sources, and 10,980 published, qualified, or conflict claims.
- Citations: 8,081 across 4,541 unique source documents.
- Possible duplicate groups: 698. Total conflict flags: 561.

## Local publication verification

- Python: all 198 tests and 87 subtests passed. Batch 1027's nine focused
  tests and complete evidence-schema validation are included.
- Clean Astro check: 658 files with zero errors, warnings, or hints.
- Clean static build: 25,372 pages.
- Bounded browser release suite: 93/93 checks passed across desktop, phone,
  and tablet: 24 Batch 1027 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,372 HTML files checked; all links resolve. The checker
  inventoried 52,454 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 140,011,103 bytes,
  SHA-256
  `716125ea74ca2e61eccdee285bb6e6ff7ce2ee903cc763824a02420233e450ce`.
- Public-identifier audit: 25,444 public artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,583 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,444 artifacts totaling
  434,512,802 bytes at output-tree SHA-256
  `9fbf55b6b045686e4d5117c4bd1c3960d69313434d67c1ac3dafd306ab89cdba`.

## Public deployment verification

- Published from commit
  `0939157e3904eb03f2c398f577e20d0f38e82fc3`.
- The Test workflow completed successfully in GitHub Actions run
  [41879111343](https://github.com/therealjameswilson/before-oss/actions/runs/41879111343).
- The Deploy GitHub Pages workflow completed successfully in run
  [41879111386](https://github.com/therealjameswilson/before-oss/actions/runs/41879111386).
- An immutable live check against that exact commit verified 67 manifest
  assets totaling 140,011,103 bytes, all eight core routes, all 46
  source-register pages, and all 46 Batch 1027 direct profile routes. The
  public manifest SHA-256 was
  `716125ea74ca2e61eccdee285bb6e6ff7ce2ee903cc763824a02420233e450ce`.
- Verified public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
