# Before OSS Batch 485 release-candidate report

Generated 2026-09-13 UTC. This report covers PDF page 96 rows 14-23,
Dorotothy H Cox through Keith C Cox.

## Research outcome

- All ten people received saved, reviewable Batch 485 outcomes and terminal
  research statuses. Research-attempt coverage increased by ten people: four
  occupation-only profiles and six archival-review profiles.
- Exact private identifiers confirm Edward N Cox, Fred E Cox, Johnie L Cox,
  and Keith C Cox as Army entrants. Their full identifiers remain private.
- The official Army code list supports qualified occupation claims for Edward
  as a decorator or window dresser, Fred as a recreation or amusement
  attendant, and Johnie as a general-farm hand. None identifies an employer.
  Fred's damaged grade is not expanded. Keith's matching Army record is dated
  11 October 1945, after NARA's documented OSS termination date, so its
  occupation is not modeled as pre-OSS evidence.
- The printed `Dorotothy H Cox` spelling was visually confirmed and remains the
  index display name. NARA, Bryn Mawr College, and corroborative archaeological
  evidence establish a high-confidence Dorothy Hannah Cox identity. Her
  archaeology, excavation-architecture, and numismatics work is published as
  a medium-confidence probable immediate pre-OSS occupation without inventing
  an employer or silently closing the 1939-to-recruitment gap. Wartime War
  Relief Association activity is not retrojected as pre-OSS employment.
- Evelyn L Cox, Frederic S Cox, Glenn L Cox, and Jane M Cox remain unresolved.
  John H Cox remains ambiguous: a museum source documents a compatible British
  Team IVOR captain, but the index supplies no rank, nationality, identifier,
  or second corroborating attribute. The lead remains a low-confidence,
  unpublished candidate.
- Thirteen Library of Congress newspaper candidates across five profiles were
  opened in official OCR context and rejected for conflicting names, family or
  property context, OCR error, or lack of an OSS and Box 150 bridge.
- No civilian employer was established in this cohort, and no authenticated
  NARA Catalog API request was made.

## Updated coverage

- Index: 23,978 / 23,978 source rows linked (100.0000%).
- Research attempted: 4,619 / 23,940 people (19.2941%).
- Verified affiliation: 530 / 23,940 people (2.2139%).
- Verified employer: 235 / 23,940 people (0.9816%).
- Archival review assessed: 4,574 / 23,940 people (19.1061%).
- Research not started: 19,321 people.
- Published affiliations: 1,808; public sources: 3,119; published claims:
  3,647.
- Claim confidence: confirmed 1,103; high 1,363; medium 1,083; low 102;
  conflicting 101.
- Citations: 4,285; unique source documents: 1,959; visible conflict count: 94;
  possible duplicate groups: 238.
- Research status: candidate found 7; completed 133; conflicting sources 88;
  documented prewar employer 89; in progress 44; identity review 203; temporal
  review 15; no reliable result after protocol 82; occupation only 832;
  archival review required 2,905; verified employer 221; not started 19,321.

## Verification

- Reviewed-evidence schema: 9 source upserts, 0 organizations, 4
  affiliations, 10 claims, 31 claim-source links, 10 person updates and 10
  consolidated research attempts; imported idempotently into the durable
  research database.
- Bounded current-source adapters: 10 CIA searches and 10 staged Library of
  Congress searches; thirteen LoC candidates and zero adapter errors. All
  thirteen candidates have imported rejection decisions.
- Army merged-file review: one complete 9,200,232-record transient scan; four
  exact-identifier matches and all name-only candidates adjudicated.
- SQLite integrity and foreign-key checks: passed.
- Python unit suite: 94 / 94 passed.
- Batch 485 Playwright suite: 15 / 15 passed across desktop, phone and tablet.
- Axe accessibility route suite: 27 / 27 passed across desktop, phone and
  tablet in the clean isolated run. An earlier retry lost its shared preview
  server after two runs overlapped; it reported connection refusal rather than
  an accessibility violation.
- Astro check: 109 files, zero errors, warnings or hints.
- Static build: 24,507 pages; all internal links resolve; 49,772 external URLs
  inventoried.
- Public-identifier audit: 24,579 artifacts, 12,926 identifiers, 120 formatted
  variants, 1,092 candidate substrings and zero unexpected identifier,
  aggregate or manifest-size matches.
- Stratified profile audit: 200 profiles; all seven structural and
  data-quality checks passed.
- Determinism: two exact public-data and Pages builds reproduced the 70-file
  public tree at
  `a23d226662c7e765793be826c98c4746a46f32acc76716466ce39a5000eb0890`
  and the 24,579-file production tree at
  `adb59672ecfd2b25537cad0816e7fc15ca52d4a5ae12d4991dad682f779764c3`.
- Public manifest: 67 assets / 89,206,272 bytes; SHA-256
  `41d79c342eb1c8b64e55a8f9c37e02fcbef03808f5ddb4bbf92ba533dc4f53a7`.

## Release boundary

The release candidate is validated locally but is not pushed or deployed in
this batch. Independent GitHub Actions and pinned-live verification remain
pending. The long-running project remains incomplete: 19,321 active people
still have `not_started` research status, and unresolved cases remain visible
rather than being converted into unsupported employer claims.
