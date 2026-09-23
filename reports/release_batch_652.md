# Batch 652 release status - pages 75-84 and Merrick-Meslin research

Research date: 2026-09-23 America/New_York. This report records the reviewed
research, extraction, and local release-verification state. Production
deployment evidence is added after the reviewed release merges.

## Historical and extraction work

All **470** printed rows on original NARA PDF pages 75-84 were compared against
the extraction at 180 dpi. Page 77 was already covered; the other nine pages
and **414** rows received their first complete visual comparison. Every row
matches. Complete-page visual review now covers **500/522 pages** and
**22,966/23,978 rows**: **22,934** match the extraction, **32** retain reviewed
corrections, and **1,012** remain unaudited. All PDF pages remain represented,
every parser warning is resolved, and SQLite integrity and foreign-key checks
pass.

The page-317 `Ray D. Merrick` through `Jerome Meslin` queue contains 22 source
rows and 22 cautious people. Every person received staged source-specific work
and a saved reviewed outcome. The bounded LoC run produced seven candidates;
all were rejected after page-context review. No authenticated NARA Catalog
request was made.

Frank C. Mesle now has a high-confidence identity bridge and a separated,
qualified chronology: University of Iowa as prewar student status, professional
Scouting in Camden as his strongly date-bounded last civilian work, and the
Corps of Engineers as his probable immediate military predecessor to OSS
training. The local Scout council and exact military transfer sequence remain
unknown, so neither medium-confidence claim is overstated.

Seven other people have high-confidence Army identity bridges without inferred
employers. Lawrencee N. Merritt, the two Charles Mersereau/Meserau rows, and
William L. Merritts remain conflicting. F Nevill Merritt's unusual printed
field order remains intact pending direct file evidence.

The cohort ends with 17 `in_progress`, four `conflicting_sources`, and one
`documented_prewar_employer_found` status. Identity statuses are eight
`high_confidence`, ten `unresolved`, and four `conflicting`. The evidence bundle
adds 15 claims: nine high, two medium, and four conflicting. The oil-company
category remains prominently available at the top of the personnel directory
and remains limited to the supported set of **seven people across nine
historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 22,966 / 23,978 rows; 500 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,097 (33.8235%) |
| People with confirmed/high employer evidence | 288 (1.2031%) |
| People with confirmed/high affiliation evidence | 643 (2.6860%) |
| Archival-review dispositions assessed | 6,553 (27.3737%) |
| Not started | 15,837 |
| Possible duplicate groups | 492 |
| Conflicts | 189 |
| Attempts or plans | 13,895 |
| Claims by confidence | confirmed 1,311; high 2,065; medium 1,406; low 189; conflicting 164 |
| Citation records / unique source documents | 5,145 / 2,445 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 148;
`documented_prewar_employer_found` 122; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,837;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 264.

The public projection contains **2,263** published affiliations, **740**
organizations, **3,935** public sources, and **4,942** published claims.
Full-index historical research remains unfinished.

## Local verification

The candidate passes **134/134 Python tests plus 75 subtests**. Playwright
successfully discovers all **21** new Batch 652 checks across desktop, phone,
and tablet projects; those checks cover the Mesle chronology, accepted Army
identities without invented employers, preserved identity conflicts and source
spellings, updated coverage, and the seven-person oil-company category at the
top of the directory.

Two isolated tracked-only Node runs stalled locally before Astro emitted a
page or diagnostic, and were stopped without modifying the release tree. The
local site build and browser execution are therefore **unverified**, not
passing. GitHub Actions' independent clean build remains the required gate
before merge.

User-owned Finder-style ` 2` files and local SQLite sidecars remain untouched
and are excluded from the release.

## Deployment

The reviewed release has not yet merged or deployed. Deployment evidence will
be recorded after GitHub Actions and the live Pages site are verified.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages75-84_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch652.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-23_batch652.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page317-merrick-meslin-review_batch-652_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published. No authenticated NARA Catalog
request was made.
