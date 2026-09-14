# Batch 509 release report

Run: 2026-09-14 UTC

## Scope

Batch 509 preserves and researches personnel-index PDF page 101 rows 24-33,
Mary Cunningham through Sanford C Curcie, at archival location 230/86/29/04.
Rows 24-29 are in Box 159; rows 30-33 are in Box 160. The rendered index page
and the relevant Army occupation-code page were visually inspected. `Capt` for
Roy H Cunningham is the cohort's only printed rank.

The next unprocessed sequence is page 101 rows 34-43, Mary T Curio through
Teresita Currie, all in Box 160.

## Research outcomes

- Murray O Cunningham is confirmed by exact name and an exact private-
  identifier match between the OSS index and official Army merged file. The
  Army row records entry on September 15, 1942 as a Private and occupation
  value 056. NARA's official code list supplies the historical category
  `Photographers`. It is published as a medium-confidence, strongly date-
  bounded occupation only; it names no employer, studio, publication,
  specialty, client or immediate OSS predecessor.
- Richard H Cunningham, Robert H Cunningham, Robert J Cunningham, Robert A
  Cunningham and Walter W Cunningham remain ambiguous after five, eleven,
  twenty-seven, thirteen and two exact-name Army candidates respectively. The
  indexed private value for Robert A does not occur in the converted Army file;
  documented conversion gaps make that a review problem, not negative proof.
- Roy H Cunningham remains an ambiguous identity while retaining the index's
  commissioned Army officer classification. Two exact-name Army rows record
  Private grade at entry, but neither supplies a later commission, OSS, service
  or Box 160 bridge and neither is assigned.
- Mary Cunningham, Alberto Cupelli and Sanford C Curcie remain unresolved.
  Contemporary media namesake leads for Cupelli and postwar namesake leads for
  Curcie are withheld because they lack an independent OSS or personnel-file
  bridge.
- Ten bounded CIA checks returned no candidates. Eighteen actual Library of
  Congress attempts created 28 candidates; full-page text review showed social
  notices, wrong middle initials, postwar legal or memorial notices, or
  chronologically irrelevant namesakes. All 28 rejections are durable and
  replay idempotently.
- The complete 9,200,232-row Army merged file was scanned transiently. Its
  no-hit outcomes are not treated as negative proof because it is neither
  complete nor an OSS, officer, Navy, civilian or foreign roster.

The batch adds four official source records, one qualified occupation
affiliation, one confirmed identity claim, one medium occupation claim and
nine low-confidence identity claims withheld from publication. It adds no
organization and no employer. Public profiles preserve exact index locators,
masked private fields, identity uncertainty, research status and archival next
actions.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,858 | 23,940 | 20.2924% |
| Verified affiliation found | 553 | 23,940 | 2.3099% |
| Verified employer found | 246 | 23,940 | 1.0276% |
| Archival disposition assessed | 4,813 | 23,940 | 20.1044% |
| Not started | 19,082 | 23,940 | 79.7076% |

Published data contains 1,920 affiliations, 603 organizations, 3,279 sources
and 3,818 claims. The private validated database contains 1,932 affiliations,
615 organizations, 4,453 citation records, 2,031 unique source documents,
3,984 claims, 7,341 research attempts and 9,400 claim-source links. Claim-
confidence totals are 1,143 confirmed, 1,422 high, 1,152 medium, 163 low and
104 conflicting. Ninety-eight conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,264 active people, documented as not
commissioned for 5,897 and unknown for 15,779. Personnel categories include
2,131 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,209 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,656 unknown or
indeterminate.

Identity-status counts are 980 confirmed, 687 high confidence, 151 probable,
205 ambiguous, 93 conflicting and 21,824 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 138 |
| conflicting_sources | 92 |
| documented_prewar_employer_found | 97 |
| in_progress | 44 |
| needs_identity_review | 257 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,082 |
| occupation_only_found | 880 |
| requires_archival_review | 3,011 |
| verified_employer_found | 231 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed. The
  cohort index page and occupation-code page were separately rendered and
  inspected.
- The review ledger contains 28 rejected LoC candidates and replays
  idempotently. The evidence bundle validates under the strict Pydantic schema
  and imports idempotently as four sources, zero organizations, one
  affiliation, eleven claims, ten person updates and ten synthesized research
  outcomes.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 15/15 Batch 509 checks passed across desktop, phone and
  tablet. Initial test-only public-field and capitalization expectations were
  corrected without changing the evidence or rendered site behavior.
- Bounded core browser QA: 39/39 search, officer-filter, direct-route,
  citation, organization, analysis, download and exact-name checks passed
  across three viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.6 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 133 source files with zero errors, warnings or hints and built
  24,551 HTML pages / 24,623 artifacts.
- Link audit: all 24,551 internal HTML pages resolve; 49,881 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,102 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size matches across 24,623 artifacts. The evidence bundle and
  review ledger contain no raw strict private identifiers.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `34c73a7f3e83bcb96f4c908292136b2d8b6d0ee57060ee786ee07bffe3d4dcba`;
  the 24,623-file production-tree digest is
  `18742ebed32af4c50d908ab28e2a3cbe1b568ec32c795c59d2118abaca8a86b6`.
  The 67-file public manifest covers 91,047,338 bytes and has SHA-256
  `0ede94f1efc7cb2d86f08ee9897d64031b544612977aab9ce3a602549df540cf`.

## Resume commands

From the repository root, Batch 509 can be reproduced and checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch509.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-one-mary-cunningham-through-sanford-c-curcie-pathways_batch-509_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch509.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
```

Research resumes with page 101 rows 34-43, Mary T Curio through Teresita
Currie, all in Box 160.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research goal
remains active because 19,082 person entities have not yet started the research
protocol. The generated entity-resolution report retains its pre-existing
warning that not every possible duplicate group is marked for manual review;
Batch 509 creates no new duplicate group, merge or silent conflation.
