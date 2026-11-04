# Batch 1014 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 504, rows 1-46: Norman B. Wiley through Arthur J.
  Williams. All 46 printed rows remain separately recoverable as 46 cautious
  person entities.
- Every cohort person has a saved research attempt and terminal outcome: 35
  `requires_archival_review`, nine `occupation_only_found`, one `completed`
  and one `conflicting_sources`.
- Identity disposition is nine confirmed, one high-confidence, one
  conflicting, six ambiguous duplicate candidates and 29 unresolved cohort
  people.
- Eight exact-name, nonshared protected-identifier Army bridges received
  explicit acceptance review. Their historical occupation categories remain
  visibly qualified and are not converted into named employers, workplaces,
  institutions or exact OSS-transfer dates.
- The same protected identifier appears on the separate Jack A. William and
  William A. Jack index rows. The Army name can be read in the opposite order,
  so neither the Army occupation nor chronology was transferred to the
  page-504 person.
- Hubert L. Will is confirmed through the official Federal Judicial Center
  chronology. His 1943 Alien Property Custodian tax-counsel assignment is
  published as the explicitly sequenced immediate and last civilian
  government affiliation before OSS; his earlier Justice Department and
  Office of Price Administration assignments remain separate.
- Max Willenz is linked at high confidence through a scholarly citation to his
  OSS Theater Service Record and personnel file in the same NARA Box 838.
  Wienbibliothek and AFI records establish pre-OSS singer and actor activity,
  but no named immediate employer is invented.
- Myra M. Wilkens or Wilkins, the two Stanley E. Willard rows, and Harriet A.
  Willetis or Willette remain three visible possible-duplicate groups. No rows
  were merged on name similarity alone.
- A bounded CIA adapter check encountered `CiaRobotsUnavailable`, and a
  Library of Congress check encountered `URLError`. Both failures remain
  auditable and are not treated as negative search results. Accessible
  official, institutional, contemporary and archival alternatives were
  reviewed. No authenticated NARA Catalog API request was used.

## Reproducible release checks

- Evidence-bundle SHA-256:
  `2a7b3b86345dc54d9fb35a69efc9c267addca81abfe63cf42bfbb538615ae92a`.
- Army review-decision SHA-256:
  `bef38273b443383a70f5422e236d9eacca0041439c47653e3ec6ac9646acc4cb`.
- Durable import: nine sources, three organization inputs, 13 affiliations,
  25 claims, 46 person updates, 46 manual research attempts and 64
  claim-source links. Two repeat imports produced identical database counts.
- Batch claim confidence: 11 confirmed, five high, eight medium and one
  conflicting. Publication disposition is 16 published, eight visibly
  qualified and one conflict claim.
- Python: all 154 tests and 87 subtests passed.
- SQLite foreign-key, integrity and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 137,093,086 bytes,
  SHA-256
  `03d81453c08cb68a0f0c6a477c2504256f2f40984b376d9a8557924115befd1c`.
- Clean Astro check: 645 files with zero errors, warnings or hints.
- Clean static build: 25,337 pages.
- Bounded browser release suite: 96/96 checks passed across desktop, phone and
  tablet: 27 Batch 1014 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,337 HTML files checked; all links resolve. The checker
  inventoried 52,352 unique external URLs separately.
- Public-identifier audit: 25,409 artifacts checked against 12,926 normalized
  private identifiers and 120 formatted variants. It inspected 1,553
  candidate substrings and found zero aggregate, manifest-size or unexpected
  boundary matches.
- Two consecutive local builds reproduced 25,409 artifacts and 429,635,111
  bytes at output-tree SHA-256
  `98e9a5e9d58603b95aaad1d4c5bb87a0d0239f69b695c002b49982f23ee72404`.
- The production dependency audit found zero vulnerabilities.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,571/23,935 people (69.2333%).
- Verified affiliation: 1,173/23,935 people (4.9008%).
- Verified employer: 536/23,935 people (2.2394%).
- Archival disposition assessed: 15,048/23,935 people (62.8703%).
- Not started: 7,359 people; in progress: 1,882 people.
- Research outcomes include 1,851 `occupation_only_found`, 9,193
  `requires_archival_review`, 451 `verified_employer_found`, 289
  `documented_prewar_employer_found` and 469 `conflicting_sources` people.
- Possible-duplicate groups: 691; conflicts: 549.
- Claim confidence: 1,898 confirmed; 5,450 high; 2,802 medium; 261 low; 457
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,239 affiliations, 1,349 organizations,
  6,668 sources and 10,603 published, qualified or conflict claims.
- Citations: 7,960 across 4,453 unique source documents.

## Publication verification

- Local release candidate is complete and verified. The content commit,
  GitHub Actions runs and unauthenticated deployed-site verification remain
  pending and will be recorded here after publication.

Public release URL: <https://therealjameswilson.github.io/before-oss/>.
