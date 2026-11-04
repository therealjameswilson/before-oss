# Batch 1030 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 520, rows 1-46: Francis E. Zdaniecki through Christian E.
  Zimmerman. All 46 printed rows remain separately recoverable as 46 cautious
  person entities.
- Every cohort person has a saved research outcome: 23
  `requires_archival_review`, 20 `occupation_only_found`, one
  `conflicting_sources`, one `needs_identity_review`, and one
  `needs_temporal_review`.
- Twenty-six protected-identifier Army candidates received explicit review:
  23 accepted, one rejected, and two retained as conflicting. Nineteen
  accepted, date-bounded occupation or student categories support qualified
  pre-OSS affiliations. Undefined, shared, conflicting, and late records were
  not converted into unsupported occupations or employers.
- Louis P. Zelenka's Carnegie alumni record directly documents his technical
  OSS assignment. It supports his wartime identity and commissioned status,
  not a pre-OSS employer.
- Evarts Ziegler's official New York State Military Museum collection record
  documents his New York National Guard service and 1940 federalization. The
  earlier military assignment remains separate from civilian employment.
- Joseph Zigman's documented prewar work as a film editor is modeled as a last
  civilian occupation because the available source does not name an employer.
  His Navy service is a separate immediate military pathway into the OSS Film
  Unit.
- Allen G. Zieber's documented student category remains student status, not
  employment. Joseph J. Zevitas, William F. Zielske Jr., and Joseph F. Zien
  receive cited OSS-assignment evidence without inventing earlier employers.
- Serge Zibell's French military-file index entry remains an identity lead
  because the accessible evidence does not bridge that officer to the OSS
  index row.
- The cohort identity assessment is 18 confirmed, nine high-confidence, 17
  unresolved, one conflicting, and one probable.
- No authenticated NARA Catalog API request was used.

## Evidence and import

- Reviewed evidence bundle: 11 sources, two organizations, 22 affiliations,
  28 claims, 76 claim-source links, 46 person updates, and 46 research
  attempts.
- Twenty-six Army identity-review decisions were imported. The decision and
  evidence imports were tested twice against a disposable database before the
  durable database update; repeated import was idempotent.
- Post-import SQLite integrity and foreign-key checks passed with zero
  violations.
- Evidence-bundle SHA-256:
  `7faf739f4bc37ee5d5d12f935b7149e51452550cf65ca1ec703480986f265632`.

## Coverage published

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 17,299/23,935 people (72.2749%).
- Verified affiliation: 1,212/23,935 people (5.0637%).
- Verified employer: 553/23,935 people (2.3104%).
- Archival disposition assessed: 15,781/23,935 people (65.9327%).
- Not started: 6,631 people; in progress: 1,878 people.
- Research outcomes include 2,029 `occupation_only_found`, 9,682
  `requires_archival_review`, 466 `verified_employer_found`, 297
  `documented_prewar_employer_found`, 611 `needs_identity_review`, 48
  `needs_temporal_review`, and 484 `conflicting_sources` people.
- Claim confidence: 2,018 confirmed; 5,575 high; 3,018 medium; 261 low; 468
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,502 affiliations, 1,393
  organizations, 6,826 sources, and 11,075 published, qualified, or conflict
  claims.
- Citations: 8,119 across 4,565 unique source documents.
- Possible duplicate groups: 699. Total conflict flags: 564.

## Local publication verification

- Python: 222 pytest cases and 87 subtests passed. The CI-compatible unittest
  discovery run also passed all 154 tests.
- Clean Astro check: 661 files with zero errors, warnings, or hints.
- Clean static build: 25,382 pages.
- Bounded browser release suite: 90/90 checks passed across desktop, phone,
  and tablet: 21 Batch 1030 checks, 33 core-route and interaction checks, six
  analysis checks, and 30 accessibility scans with no serious axe violations.
- Internal links: 25,382 HTML files checked; all links resolve. The checker
  inventoried 52,483 unique external URLs separately.
- Checked-in public manifest: 67 canonical assets, 140,692,729 bytes,
  SHA-256
  `3e1a26229d10a42c3c3c212d954136f7f6c763f6627176c6e841345d406eda3e`.
- Public-identifier audit: 25,454 public artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,583 candidate substrings and found zero aggregate, manifest-size, or
  unexpected boundary matches.
- Two consecutive local builds reproduced 25,454 artifacts totaling
  435,663,412 bytes at output-tree SHA-256
  `b81b8fd02879402a8395f0cd27119a40110a258285677a8e4ee58a939e1a2ab7`.

## Deployment status

- Publication commit:
  `c4fb307f013b0b4ee9f32132066afb2791b7809c`.
- GitHub Actions Test run
  [41899940322](https://github.com/therealjameswilson/before-oss/actions/runs/41899940322)
  passed, including the complete Python suite, checked-in manifest check,
  bounded browser release suite, and public-identifier audit.
- GitHub Pages run
  [41899940410](https://github.com/therealjameswilson/before-oss/actions/runs/41899940410)
  built and deployed successfully.
- The read-only immutable-commit verifier matched all 67 canonical public
  assets (140,692,729 bytes) to manifest SHA-256
  `3e1a26229d10a42c3c3c212d954136f7f6c763f6627176c6e841345d406eda3e`.
  It also verified eight core routes, all 46 source-register pages, and all 46
  direct Batch 1030 profile routes.
- Public base URL:
  <https://therealjameswilson.github.io/before-oss/>.
