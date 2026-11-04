# Batch 1019 release audit

Date: 2026-11-04 America/New_York

## Release contents

- NARA index page 509, rows 1-46: George P. Wing through Wimon Wiriyawit.
  All 46 printed rows remain separately recoverable as 46 cautious person
  entities.
- Every cohort person has a saved terminal or explicit review outcome: 28
  `requires_archival_review`, 13 `occupation_only_found`, two
  `verified_employer_found`, one `completed`, one `needs_identity_review` and
  one `conflicting_sources`.
- Identity disposition is 12 confirmed, four high-confidence, one probable,
  one conflicting and 28 unresolved cohort people.
- Fourteen protected-identifier Army candidates received explicit review:
  thirteen were accepted and one was classified conflicting. The accepted
  records support qualified historical occupation or student categories only.
  They are not converted into named employers, workplaces, schools or exact
  OSS-transition dates.
- Visual review of NARA's original compiled code-list page corrected code 891
  to the unskilled class of “furnacemen, smelters, and pourers” before the
  evidence bundle entered the database. The rejected radio/phonograph reading
  is absent from the public projection and is covered by a regression test.
- Thomas J. Wing Wo's protected identifier points to the materially different
  Army surname Wingawo. No Army identity, grade, occupation or chronology is
  transferred.
- Kai G. Winkelhorn's War Production Board assignment is kept separate from
  his last civilian employer, Goldman, Sachs & Co. Earlier export-company work
  and New York University study are separately modeled.
- Rudolph A. Winnacker's University of Nebraska work is supported as both his
  immediate pre-OSS affiliation and last civilian employer. His earlier
  University of Michigan appointment remains an earlier prewar role.
- Wimon Wiriyawit's MIT student status immediately before Free Thai and OSS
  service is not labeled employment. His earlier Chulalongkorn University
  study is also preserved as a student affiliation.
- The adjacent George Winner and George L. Winner rows remain distinct and
  visibly grouped for Box 846 review.
- Bounded CIA and Library of Congress adapter checks failed closed with
  separately recorded access errors. The failures are not treated as negative
  results. No authenticated NARA Catalog API request was used.

## Coverage prepared for publication

- Index: 23,978/23,978 source rows linked (100.0000%).
- Research attempted: 16,797/23,935 people (70.1776%).
- Verified affiliation: 1,184/23,935 people (4.9467%).
- Verified employer: 544/23,935 people (2.2728%).
- Archival disposition assessed: 15,278/23,935 people (63.8312%).
- Not started: 7,133 people; in progress: 1,879 people.
- Research outcomes include 1,909 `occupation_only_found`, 9,346
  `requires_archival_review`, 456 `verified_employer_found`, 293
  `documented_prewar_employer_found`, 604 `needs_identity_review` and 475
  `conflicting_sources` people.
- Claim confidence: 1,960 confirmed; 5,485 high; 2,866 medium; 261 low; 463
  conflicting; and two unresolved.
- Public projection: 23,935 profiles, 4,319 affiliations, 1,364 organizations,
  6,720 sources and 10,770 published, qualified or conflict claims.
- Citations: 8,012 across 4,484 unique source documents.

## Local publication verification

- Evidence-bundle SHA-256:
  `1444202424c27aa35d4d3d36bab2725bd3e868af03b75e0c745196c8f739fba0`.
- Army review-decision SHA-256:
  `426f4cc5f3914530f8b7ef58b9c562368dce4fa4b99851e1901220c1141d311a`.
- Evidence-bundle and Army decision files validate without exposing secrets,
  full identifiers or raw bulk records.
- Python: all 154 tests passed.
- SQLite foreign-key, integrity and complete 522-page ingest checks passed.
- The deterministic 200-profile stratified audit passed all seven invariants.
- Checked-in public manifest: 67 canonical assets, 138,363,351 bytes, SHA-256
  `c5b27ca05a7d45b55799adeaf03e688e4d83475c112e762dc55c6ee37bf3e72c`.
- Clean Astro check: 650 files with zero errors, warnings or hints.
- Clean static build: 25,352 pages.
- Bounded browser release suite: 96/96 checks passed across desktop, phone and
  tablet: 27 Batch 1019 checks, 33 core-route and interaction checks, six
  analysis checks and 30 accessibility scans with no serious axe violations.
- Internal links: 25,352 HTML files checked; all links resolve. The checker
  inventoried 52,391 unique external URLs separately.
- Public-identifier audit: 25,424 artifacts checked against 12,926 normalized
  private identifiers and 120 formatted variants. It inspected 1,586
  candidate substrings and found zero aggregate, manifest-size or unexpected
  boundary matches.
- Two consecutive local builds reproduced 25,424 artifacts and 431,762,485
  bytes at output-tree SHA-256
  `0c6399566efaa58bbb36a4f7297905ff2c290a6fa3b4511c59cd23ef6f93e1cb`.
- The production dependency audit found zero vulnerabilities.

CI, GitHub Pages and unauthenticated live-release verification are separate
gates and are recorded here only after they succeed.
