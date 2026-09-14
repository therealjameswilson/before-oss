# Before OSS Batch 483 release-candidate report

Generated 2026-09-12 UTC. This report covers PDF page 95 rows 40-46 and page
96 rows 1-3, Theodore R Coverly through Joseph G Cowel.

## Research outcome

- All ten people received saved, reviewable Batch 483 outcomes and terminal
  archival-review statuses. Research-attempt coverage increased by ten people.
- Theodore R Coverly, Richard L Covington, George L Cowan and John K Cowan
  each have one exact-name Army candidate. None has a complete matching
  identifier or second corroborating identifier, so no occupation, grade,
  branch, personnel category or affiliation was transferred.
- Floyd R Covey, Albert P Coviello, Richard O Covington, Catherine Cowan and
  Joseph G Cowel remain unresolved after official, institutional, newspaper,
  obituary, directory, military and archival searches.
- John W Covill remains unresolved. An exact-name USAAF prisoner-of-war
  derivative and an unofficial OSS microfilm association require direct Box
  149 comparison before the identity or chronology can be accepted.
- Richard O. Covington Jr.'s tennis biography and a 1930 university reference
  to Catherine Cowan remain explicitly rejected namesakes rather than becoming
  education, occupation or affiliation claims.
- Five Library of Congress newspaper candidates for John K Cowan were opened
  in official OCR context and rejected as John C Cowan, a person deceased
  before 1908, or funeral-home references to John J Cowan Son.
- No authenticated NARA Catalog API request was made.

## Updated coverage

- Index: 23,978 / 23,978 source rows linked (100.0000%).
- Research attempted: 4,599 / 23,940 people (19.2105%).
- Verified affiliation: 529 / 23,940 people (2.2097%).
- Verified employer: 235 / 23,940 people (0.9816%).
- Archival review assessed: 4,554 / 23,940 people (19.0226%).
- Research not started: 19,341 people.
- Published affiliations: 1,799; public sources: 3,104; published claims:
  3,628.
- Claim confidence: confirmed 1,095; high 1,359; medium 1,076; low 101;
  conflicting 101.
- Citations: 4,269; unique source documents: 1,953; visible conflict count: 94;
  possible duplicate groups: 238.
- Research status: candidate found 7; completed 132; conflicting sources 88;
  documented prewar employer 89; in progress 44; identity review 203; temporal
  review 15; no reliable result after protocol 82; occupation only 825;
  archival review required 2,893; verified employer 221; not started 19,341.

## Verification

- Reviewed-evidence schema: 2 source upserts, zero organizations,
  affiliations, claims or claim-source links, 10 person updates and 10
  consolidated research attempts; passed first in a disposable database and
  then in the durable research database.
- Bounded current-source adapters: 10 CIA and 10 Library of Congress queries;
  five LoC candidates and zero errors. All five candidates have imported
  rejection decisions.
- Army merged-file review: one complete 9,200,232-record transient scan; four
  name-only candidates adjudicated and no eligible exact identifier.
- SQLite integrity and foreign-key checks: passed.
- Python unit suite: 94 / 94 passed.
- Batch 483 Playwright suite: 12 / 12 passed across desktop, phone and tablet.
- Axe accessibility route suite: 27 / 27 passed across desktop, phone and
  tablet.
- Astro check: 107 files, zero errors, warnings or hints.
- Static build: 24,506 pages; all internal links resolve; 49,767 external URLs
  inventoried.
- Public-identifier audit: 24,578 artifacts, 1,094 candidate substrings and
  zero unexpected identifier, aggregate or manifest-size matches.
- Stratified profile audit: 200 profiles; all seven structural and
  data-quality checks passed.
- Determinism: two exact public-data and Pages builds reproduced the 70-file
  public tree at
  `f07f31e777efad523c21118dc28f53c8ebd960d4ce1ce5feb2cf08b72cdefbbc`
  and the 24,578-file production tree at
  `723c62831ce07aa51f3ad11409e20c3f8b5e627c2ae80e8046e6480237fbbcbd`.
- Public manifest: 67 assets / 89,043,398 bytes; SHA-256
  `3ab13ee5a25d33d5383804e3b3978ab9656d46162e7f08cae9f5f01c45404189`.

## Release boundary

The release candidate is validated locally but is not pushed or deployed in
this batch. Independent GitHub Actions and pinned-live verification remain
pending. The long-running project remains incomplete: 19,341 active people
still have `not_started` research status, and unresolved cases remain visible
rather than being converted into unsupported employer claims.
