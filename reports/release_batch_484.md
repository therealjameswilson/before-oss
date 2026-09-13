# Before OSS Batch 484 release-candidate report

Generated 2026-09-12 UTC. This report covers PDF page 96 rows 4-13,
Katehrine M Cowen through Donald J Cox.

## Research outcome

- All ten people received saved, reviewable Batch 484 outcomes and terminal
  research statuses. Research-attempt coverage increased by ten people: one
  completed profile, three occupation-only profiles, and six archival-review
  profiles.
- Exact private identifiers confirm Lawrence L Cowger, David O Cowles,
  Clarence R Cox, and Donald J Cox as Army entrants recorded as privates.
  Their full identifiers remain private.
- The official Army code list supports qualified occupation claims for David
  Cowles in radio and phonograph manufacture, Clarence Cox as an animal and
  livestock farm hand, and Donald Cox in photographic process work. None
  identifies an employer. Lawrence Cowger's value 999 remains deliberately
  uninterpreted.
- Official National Park Service histories and an independent Lehigh
  University biography establish a high-confidence identity for Lieutenant
  Colonel Alfred T Cox. His best-supported immediate predecessor is a
  guerrilla-warfare instructor assignment at the U.S. Army Infantry School,
  Fort Benning. Lehigh is modeled separately as a prewar student affiliation,
  never as an employer.
- Katehrine M Cowen, Wilbur A Cowett, John F Cowgill, Arthur M Cox, and Charles
  W Cox remain unresolved. The printed Katehrine spelling and British A note
  are preserved without silent correction or expansion. Short identifiers,
  name-only Army rows, and common-name results were not transferred.
- Ten Library of Congress newspaper candidates across four profiles were
  opened in official OCR context and rejected for conflicting initials,
  unrelated company or family context, incompatible dates, or lack of an OSS
  and Box 150 bridge.
- No civilian employer was established in this cohort, and no authenticated
  NARA Catalog API request was made.

## Updated coverage

- Index: 23,978 / 23,978 source rows linked (100.0000%).
- Research attempted: 4,609 / 23,940 people (19.2523%).
- Verified affiliation: 530 / 23,940 people (2.2139%).
- Verified employer: 235 / 23,940 people (0.9816%).
- Archival review assessed: 4,564 / 23,940 people (19.0643%).
- Research not started: 19,331 people.
- Published affiliations: 1,804; public sources: 3,111; published claims:
  3,638.
- Claim confidence: confirmed 1,099; high 1,362; medium 1,079; low 101;
  conflicting 101.
- Citations: 4,276; unique source documents: 1,955; visible conflict count: 94;
  possible duplicate groups: 238.
- Research status: candidate found 7; completed 133; conflicting sources 88;
  documented prewar employer 89; in progress 44; identity review 203; temporal
  review 15; no reliable result after protocol 82; occupation only 828;
  archival review required 2,899; verified employer 221; not started 19,331.

## Verification

- Reviewed-evidence schema: 7 source upserts, 2 organizations, 5
  affiliations, 10 claims, 29 claim-source links, 10 person updates and 10
  consolidated research attempts; passed first in a disposable database and
  then in the durable research database.
- Bounded current-source adapters: 10 CIA searches and 11 staged Library of
  Congress searches; ten LoC candidates and zero errors. All ten candidates
  have imported rejection decisions.
- Army merged-file review: one complete 9,200,232-record transient scan; four
  exact-identifier matches and all name-only candidates adjudicated.
- SQLite integrity and foreign-key checks: passed.
- Python unit suite: 94 / 94 passed.
- Batch 484 Playwright suite: 15 / 15 passed across desktop, phone and tablet.
- Axe accessibility route suite: 27 / 27 passed across desktop, phone and
  tablet.
- Astro check: 108 files, zero errors, warnings or hints.
- Static build: 24,507 pages; all internal links resolve; 49,769 external URLs
  inventoried.
- Public-identifier audit: 24,579 artifacts, 12,926 identifiers, 120 formatted
  variants, 1,092 candidate substrings and zero unexpected identifier,
  aggregate or manifest-size matches.
- Stratified profile audit: 200 profiles; all seven structural and
  data-quality checks passed.
- Determinism: two exact public-data and Pages builds reproduced the 70-file
  public tree at
  `50e99c9a395c1643901aa404c3bdace470cc0dbaa5e2a171ffa73d2db501b5ca`
  and the 24,579-file production tree at
  `5777a6a90a7822f30f2511cbc4687a9cabaaa133f53c2c389f3d3fba966a660b`.
- Public manifest: 67 assets / 89,133,609 bytes; SHA-256
  `e643f3fb89ed05472fdc2f3934a8e6164f69fe2814d6da90c40dbec8ffc84e9d`.

## Release boundary

The release candidate is validated locally but is not pushed or deployed in
this batch. Independent GitHub Actions and pinned-live verification remain
pending. The long-running project remains incomplete: 19,331 active people
still have `not_started` research status, and unresolved cases remain visible
rather than being converted into unsupported employer claims.
