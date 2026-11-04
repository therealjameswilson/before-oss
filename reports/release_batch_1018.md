# Batch 1018 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 508, rows 1-46: Gladys A. Wilson through Frederick C.
  Wing. All 46 printed rows remain separately recoverable as 46 cautious
  person entities.
- Every cohort person has a saved terminal or explicit review outcome: 27
  `requires_archival_review`, 16 `occupation_only_found`, one
  `documented_prewar_employer_found`, one `needs_identity_review` and one
  `conflicting_sources`.
- Identity disposition is 16 confirmed, three high-confidence, one probable,
  one conflicting and 25 unresolved cohort people.
- Eighteen protected-identifier Army candidates received explicit review:
  seventeen were accepted and one was classified conflicting. Sixteen
  accepted records support historical occupation categories only. The
  categories stay visibly qualified and are not converted into named
  employers, workplaces or exact OSS-transition dates.
- The John H. Wilson candidate's protected identifier points to the
  incompatible Army name Roy H. Mc Adams. No Army identity, grade,
  occupation or chronology is transferred.
- Direct OSS, institutional and scholarly evidence confirms Sivert Windh's
  identity, including the full-name form Kjell Rune Sivert Windh, while
  retaining only the qualified Army-entry occupation category. No employer
  is invented.
- John Skinner Wilson's Gilwell Park work is published as a documented prewar
  professional affiliation, not employment or an immediate pre-OSS
  predecessor.
- Major Gerald K. Wines has qualified documented-prewar employment as an
  advertising representative for an unnamed major Dallas-area newspaper. The
  newspaper is not guessed. His adjacent index row remains a separate
  probable entity in a visible possible-duplicate group because the evidence
  does not justify a merge.
- Leonard S. Wilson is correctly classified as a commissioned naval officer.
- A bounded CIA adapter check encountered `CiaRobotsUnavailable`, and a
  Library of Congress check encountered `URLError`. Both failures remain
  auditable and are not treated as negative results. No authenticated NARA
  Catalog API request was used.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,752/23,935 people (69.9896%).
- Verified affiliation: 1,181/23,935 people (4.9342%).
- Verified employer: 542/23,935 people (2.2645%).
- Archival disposition assessed: 15,232/23,935 people (63.6390%).
- Not started: 7,178 people; in progress: 1,880 people.
- Research outcomes include 1,896 `occupation_only_found`, 9,318
  `requires_archival_review`, 454 `verified_employer_found`, 293
  `documented_prewar_employer_found`, 603 `needs_identity_review` and 474
  `conflicting_sources` people.
- Claim confidence: 1,948 confirmed; 5,472 high; 2,853 medium; 261 low; 462
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,298 affiliations, 1,356 organizations,
  6,709 sources and 10,731 published, qualified or conflict claims.
- Citations: 8,001 across 4,478 unique source documents.

## Local publication verification

- Evidence-bundle SHA-256:
  `88585123a86a2006a56cab0ab69703fc1a3eae66e946b4abbc3bc8f2b5446983`.
- Army review-decision SHA-256:
  `3a0e24bac5d37b8154290573278d2f56d07120342657b7ed4d3859887d7bc597`.
- Evidence-bundle and Army decision files validate without exposing secrets,
  full identifiers or raw bulk records.
- Python: all 154 tests passed.
- SQLite foreign-key, integrity and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 138,065,031 bytes, SHA-256
  `901474de1b1b2adf7b4fe96b8f141355855fb1500cd50d987b4be05e4af28204`.
- Clean Astro check: 649 files with zero errors, warnings or hints.
- Clean static build: 25,344 pages.
- Bounded browser release suite: 96/96 checks passed across desktop, phone and
  tablet: 27 Batch 1018 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,344 HTML files checked; all links resolve. The checker
  inventoried 52,378 unique external URLs separately.
- Public-identifier audit: 25,414 artifacts checked against 12,926 normalized
  private identifiers and 120 formatted variants. It inspected 1,563
  candidate substrings and found zero aggregate, manifest-size or unexpected
  boundary matches.
- Two consecutive local builds reproduced 25,416 artifacts and 431,248,203
  bytes at output-tree SHA-256
  `ba11ba21ca3664b7e8a8a65123b00f38350d1043c22b100eb63cdce3506b3db0`.
- The production dependency audit found zero vulnerabilities.

Content commit `96699662bab9ec7a9347ae80a1d44d86c4e995ea` passed the full
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/41813811122)
and the
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/41813811129).
The unauthenticated deployed-release verifier matched all 67 canonical assets
and 138,065,031 bytes to the committed manifest at SHA-256
`901474de1b1b2adf7b4fe96b8f141355855fb1500cd50d987b4be05e4af28204`.
It also returned successful main content for all eight core routes, all 45
source-register pages and all 46 Batch 1018 direct profile URLs.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
