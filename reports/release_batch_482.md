# Before OSS Batch 482 release-candidate report

Generated 2026-09-12 UTC. This report covers PDF page 95 rows 30-39, Charles
Coussoule through John Covello Jr.

## Research outcome

- All ten people received saved, reviewable Batch 482 outcomes and terminal or
  explicit review statuses. Research-attempt coverage increased by ten people.
- Four exact-name, exact-private-identifier Army matches were adjudicated.
  Henry J Couture is recorded as a student at Army entry; Theodore O Couture
  and John Covello Jr. receive only broad historical occupation categories;
  Costa G Couvaras is confirmed across the index, Army record and an
  independent institutional history.
- Couvaras's United States Army service and Camp Ritchie training are modeled
  as his immediate military affiliation before OSS. The National Herald is
  separately modeled as his last civilian employer, with Assyrmatos and the
  1939 Greek Pavilion retained as earlier employment.
- Miguel Covarrubias is a high-confidence match to the Mexican artist whose
  OSS drawing work is explicitly documented by the Metropolitan Museum. The
  source does not establish formal personnel status or rank, so those fields
  remain indeterminate. A 1933 Vanity Fair contribution is a professional
  affiliation, not an employer claim.
- Charles Coussoule remains a separate probable duplicate of the Box 140
  Charles Conssoule entity. No officer classification or affiliation crosses
  the unresolved file boundary.
- Gregory Coutoupis, Francis Covaleski, Richard Covel and James Covell remain
  unresolved with specific Box 149 archival actions. Name-only Army,
  directory, commemorative-booklet, burial and roster candidates were
  rejected.
- No authenticated NARA Catalog API request was made.

## Updated coverage

- Index: 23,978 / 23,978 source rows linked (100.0000%).
- Research attempted: 4,589 / 23,940 people (19.1688%).
- Verified affiliation: 529 / 23,940 people (2.2097%).
- Verified employer: 235 / 23,940 people (0.9816%).
- Archival review assessed: 4,544 / 23,940 people (18.9808%).
- Research not started: 19,351 people.
- Published affiliations: 1,799; public sources: 3,104; published claims:
  3,628.
- Claim confidence: confirmed 1,095; high 1,359; medium 1,076; low 101;
  conflicting 101.
- Citations: 4,267; unique source documents: 1,953; visible conflict count: 94;
  possible duplicate groups: 238.
- Research status: candidate found 7; completed 132; conflicting sources 88;
  documented prewar employer 89; in progress 44; identity review 203; temporal
  review 15; no reliable result after protocol 82; occupation only 825;
  archival review required 2,883; verified employer 221; not started 19,351.

## Verification

- Reviewed-evidence schema: 7 sources, 5 organization upserts, 9
  affiliations, 14 claims, 10 person updates, 10 consolidated research
  attempts and 31 claim-source links; passed.
- Bounded current-source adapters: 10 CIA and 10 Library of Congress queries;
  zero candidate matches and zero errors. Their attempts remain separately
  auditable in SQLite.
- Army merged-file review: one complete 9,200,232-record transient scan; four
  exact identifier matches and four name-only candidate sets adjudicated;
  official field and occupation-code documentation visually checked.
- SQLite integrity and foreign-key checks: passed.
- Python unit suite: 94 / 94 passed.
- Batch 482 Playwright suite: 18 / 18 passed across desktop, phone and tablet.
- Axe accessibility route suite: 27 / 27 passed across desktop, phone and
  tablet.
- Astro check: 106 files, zero errors, warnings or hints.
- Static build: 24,506 pages; all internal links resolve; 49,767 external URLs
  inventoried.
- Public-identifier audit: 24,578 artifacts, 1,094 candidate substrings and
  zero unexpected identifier, aggregate or manifest-size matches.
- Stratified profile audit: 200 profiles; all seven structural and data-quality
  checks passed.
- Determinism: two exact public-data and Pages builds reproduced the 70-file
  public tree at
  `03db07bed1c2c0dfdb26b9a6610f2dbd9d59baccff50d86b8143f7d06bb6d6c9`
  and the 24,578-file production tree at
  `ca988300a080bfd6ea9b6973b69a48aa549ad04e1edef6811ceb3144e65e94a0`.
- Public manifest: 67 assets / 89,033,982 bytes; SHA-256
  `ba36e700e594ad9a31501ce05015016754bddd1a716eae00c0a67e6835fa6fa5`.

## Release boundary

The release candidate is validated locally but is not pushed or deployed in
this batch. Independent GitHub Actions and pinned-live verification remain
pending. The long-running project remains incomplete: 19,351 active people
still have `not_started` research status, and unresolved cases remain visible
rather than being converted into unsupported employer claims.
