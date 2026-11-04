# Batch 1010 release audit

Date: 2026-11-03 America/New_York

## Release contents

- NARA index page 500, rows 1-46: Harold J. Wheelock through Harold B. White.
  All 46 printed rows remain separately recoverable as 46 cautious person
  entities.
- Every cohort person has a saved research attempt and terminal review outcome:
  33 `requires_archival_review`, seven `occupation_only_found`, three
  `completed`, two `verified_employer_found` and one `conflicting_sources`.
- Identity disposition is seven confirmed, four high-confidence, one probable,
  one conflicting and 33 unresolved cohort people.
- Seven exact-name, nonshared protected-identifier Army bridges received
  explicit acceptance review. They support qualified historical occupation or
  student categories only; no occupation code is converted into a named
  employer, school, workplace or exact OSS-transfer date.
- Contemporary Morningside College evidence supports a high-confidence
  Theodore M. Whicher identity while keeping student status and Coast Artillery
  service separate.
- Contemporary newspaper and wartime-film catalog evidence supports a
  high-confidence John T. Whitaker identity. Chicago Daily News Foreign Service
  is modeled as his last documented civilian employer before wartime service;
  the New York Herald Tribune and Chattanooga News remain earlier roles. An
  exact transfer date into OSS is not asserted.
- Princeton and official NARA evidence support a high-confidence Alan Perine
  White identity. Princeton student status and 81st Infantry Division service
  remain distinct and are not counted as employment.
- Bennett S. White Jr.'s University of Kentucky authorship affiliation remains
  a probable, medium-confidence professional affiliation, not an employer
  claim, because no source bridges it directly to the OSS index person.
- A declassified FBI chronology strengthens the existing George Hunter White
  identity and documents the Federal Bureau of Narcotics as his last civilian
  government affiliation before Army service. Earlier Border Patrol work and
  private-investigator self-employment remain separate; the immediate pre-OSS
  relationship is still visibly qualified.
- The same protected index number is printed for Charles W. Whitaker and
  Charles W. Whittaker on separate rows. Both remain separate in a conflict
  group; no Army occupation is assigned. The public projection exposes only an
  opaque shared group label and never the protected number.
- All 46 page-500 rows, relevant official Army codebook pages and cited source
  pages were reviewed. No authenticated NARA Catalog API request was used.

## Reproducible release checks

- Audited content commit:
  `7840f6d038362fbacd6ad090904c50158b777f09`.
- Evidence-bundle SHA-256:
  `9c11dc0c78ac8eef6f155c6e91cafbbdb16a5cd79cc58c69020de5cdf15e1bc0`.
- Army/LoC review-decision SHA-256:
  `949e56726481853e9991adbf44913d8a9bfb93c367f4deb16e35776feb70bd4f`.
- Durable import: 11 sources, ten organization inputs, 18 affiliations, 23
  claims, 46 person updates and 46 research attempts.
- Batch claim confidence: 12 high, ten medium and one conflicting. Publication
  disposition is 12 published, ten visibly qualified and one conflict claim.
- Python: all 154 tests passed locally.
- SQLite foreign-key, quick and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 136,161,820 bytes,
  SHA-256
  `1ba039a1c86fae91feaaf0420ddf77041d01629108217389812fef2b3094da40`.
- Clean Astro check: 641 files with zero errors, warnings or hints.
- Clean static build: 25,332 pages.
- Bounded browser release suite: 102/102 checks passed across desktop, phone and
  tablet: 33 Batch 1010 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,332 HTML files checked; all links resolve. The checker
  inventoried 52,328 unique external URLs separately.
- Local public-identifier audit: 25,404 artifacts checked against 12,926
  normalized private identifiers and 120 formatted variants. It inspected
  1,485 candidate substrings and found zero unexpected boundary matches.
- Two consecutive builds reproduced 25,404 artifacts and 428,087,233 bytes at
  output-tree SHA-256
  `ee1801cd23b6330aef67f6165b47df0386ee03d12c144f8d8cdd2aefc8e0d40b`.
- The production dependency audit found zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,388/23,935 people (68.4688%).
- Verified affiliation: 1,164/23,935 people (4.8632%).
- Verified employer: 530/23,935 people (2.2143%).
- Archival disposition assessed: 14,865/23,935 people (62.1057%).
- Not started: 7,542 people; in progress: 1,882 people.
- Research outcomes include 1,808 `occupation_only_found`, 9,068
  `requires_archival_review`, 446 `verified_employer_found`, 287
  `documented_prewar_employer_found` and 465 `conflicting_sources` people.
- Possible-duplicate groups: 688; conflicts: 545.
- Claim confidence: 1,843 confirmed; 5,429 high; 2,758 medium; 258 low;
  453 conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,178 affiliations, 1,344 organizations,
  6,631 sources and 10,479 published, qualified or conflict claims.
- Citations: 7,921 across 4,428 unique source documents.

## Publication verification

- Immutable published release commit:
  `7840f6d038362fbacd6ad090904c50158b777f09`.
- GitHub Actions Test run
  [41774635455](https://github.com/therealjameswilson/before-oss/actions/runs/41774635455)
  completed successfully on 2026-11-03.
- GitHub Pages run
  [41774635575](https://github.com/therealjameswilson/before-oss/actions/runs/41774635575)
  completed successfully on 2026-11-03.
- On 2026-11-03, the unauthenticated deployed-release verifier checked the
  live GitHub Pages site against that exact commit and evidence bundle. It
  verified all 67 public assets (136,161,820 bytes; manifest SHA-256
  `1ba039a1c86fae91feaaf0420ddf77041d01629108217389812fef2b3094da40`),
  all eight core routes, all 45 source-register pages and all 46 directly
  affected profile routes.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
