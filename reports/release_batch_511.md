# Batch 511 release report

Run: 2026-09-14 UTC

## Scope

Batch 511 preserves and researches personnel-index PDF page 101 rows 44-46
and page 102 rows 1-7, Richard Currier through John N Curtis, all in Box 160
at archival location 230/86/29/04. Both complete index pages and the relevant
Army occupation-code pages were visually inspected. Horace M Curtis is the
only cohort member with a printed rank: `T/Sgt`.

The next unprocessed sequence is page 102 rows 8-17, Joseph T Curtis through
John S Curtiss, all in Box 161.

## Research outcomes

- William B Curry is confirmed by exact name and an exact private-identifier
  match between the OSS index and official Army merged file. The Army row
  records entry on July 14, 1941 as a Private. Occupation value 999 remains
  uninterpreted and creates no affiliation.
- Earle J Curtis is likewise confirmed by exact name and private identifier.
  His Army-entry row is dated July 9, 1942 and carries occupation value 306,
  which NARA's official code list defines as `General farmers`. It is
  published only as a medium-confidence, strongly date-bounded occupation;
  it establishes no named farm, ownership status, employer, location or
  immediate OSS predecessor.
- Floyd J Curtis has one exact-name Army row and an agreeing private-
  identifier match. The February 13, 1945 entry carries occupation value 266,
  defined as `Policemen and detectives, public service`. It does not identify
  an agency, jurisdiction, exact role, employer or Army-to-OSS chronology.
- Horace M Curtis has one exact-name Army row and an agreeing private-
  identifier match. The September 16, 1942 entry carries occupation value
  048, defined as `Draftsmen`. Damaged grade bytes in the Army row are not
  interpreted; enlisted classification rests on the OSS index's printed
  `T/Sgt`.
- A September 1940 newspaper report names Colonel Charles C Curtis of the
  213th Coast Artillery. The OSS index supplies neither rank nor a
  differentiating identifier and no source connects that colonel to OSS or
  Box 160. The lead therefore remains plausible and unpublished pending
  identity review.
- Richard Currier, Anne Curtis, Eleanor R Curtis, Helen D Curtis and John N
  Curtis remain unresolved. No unbridged common-name, Australian-service or
  Roosevelt-family candidate is published.
- Ten bounded CIA checks returned no candidates. Ten actual Library of
  Congress attempts created sixteen candidates; full-page review rejected
  fifteen and retained only the qualified Charles Curtis lead. The decisions
  are durable and replay idempotently.
- The complete 9,200,232-row Army merged file was scanned transiently. Its
  no-hit outcomes are not treated as negative proof because it is neither
  complete nor an OSS, officer, Navy, civilian or foreign roster.

The batch adds four official source records, three affiliations, seven claims
and twenty-one claim-source links. Public profiles preserve exact index
locators, masked private fields, identity uncertainty, research status and
archival next actions.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,878 | 23,940 | 20.3759% |
| Verified affiliation found | 554 | 23,940 | 2.3141% |
| Verified employer found | 246 | 23,940 | 1.0276% |
| Archival disposition assessed | 4,833 | 23,940 | 20.1880% |
| Not started | 19,062 | 23,940 | 79.6241% |

Published data contains 1,926 affiliations, 603 organizations, 3,288 sources
and 3,832 claims. The private validated database contains 1,938 affiliations,
615 organizations, 4,462 citation records, 2,031 unique source documents,
3,998 claims, 7,401 research attempts and 9,439 claim-source links. Claim-
confidence totals are 1,150 confirmed, 1,424 high, 1,157 medium, 163 low and
104 conflicting. Ninety-eight conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,265 active people, documented as not
commissioned for 5,903 and unknown for 15,772. Personnel categories include
2,132 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,215 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,649 unknown or
indeterminate.

Active identity-status counts are 987 confirmed, 688 high confidence, 151
probable, 205 ambiguous, 93 conflicting and 21,816 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 138 |
| conflicting_sources | 92 |
| documented_prewar_employer_found | 97 |
| in_progress | 44 |
| needs_identity_review | 258 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,062 |
| occupation_only_found | 885 |
| requires_archival_review | 3,025 |
| verified_employer_found | 231 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed. The
  two cohort index pages and occupation-code pages were separately rendered
  and inspected.
- The review ledger contains fifteen rejected and one plausible Library of
  Congress candidate and replays idempotently. The evidence bundle validates
  under the strict Pydantic schema and imports idempotently as four sources,
  three affiliations, seven claims, twenty-one claim-source links, ten person
  updates and ten synthesized research outcomes.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 15/15 Batch 511 checks passed across desktop, phone and
  tablet.
- Bounded core browser QA: 18/18 search, filter, route, citation and downloads
  checks passed; analysis browser QA passed 6/6 across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.6 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 136 source files with zero errors, warnings or hints and built
  24,551 HTML pages / 24,623 artifacts.
- Link audit: all 24,551 internal HTML pages resolve; 49,881 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size matches across 24,623 artifacts. The evidence bundle and
  review ledger contain no raw strict private identifiers.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `fb38e1ce316d5d2d0461c3402ad114e5904d5120e1a4ea4a7b34b57e4b38dfd8`;
  the 24,623-file production-tree digest is
  `7b06e220051399136b8e5377a5dea0cb0b022c22b7b0c8d4935ad93c6e354221`.
  The 67-file public manifest covers 91,151,036 bytes and has SHA-256
  `cd3359c8039764d0a648aad7fc0e45c1561ec1ecf1bad38a061ce1baed61fc4d`.

## Resume commands

From the repository root, Batch 511 can be reproduced and checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch511.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-one-and-one-hundred-and-two-richard-currier-through-john-n-curtis-pathways_batch-511_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch511.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
```

Research resumes with page 102 rows 8-17, Joseph T Curtis through John S
Curtiss, all in Box 161.

## Release boundary

Batch 511 is a validated local release candidate and has not yet been pushed
or deployed. No authenticated NARA Catalog API request was made. The research
goal remains active because 19,062 person entities have not yet started the
research protocol. The generated entity-resolution report retains its
pre-existing warning that not every possible duplicate group is marked for
manual review; Batch 511 creates no new duplicate group, merge or silent
conflation.
