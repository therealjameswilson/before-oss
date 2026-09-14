# Batch 507 release report

Run: 2026-09-14 UTC

## Scope

Batch 507 preserves and researches personnel-index PDF page 101 rows 4-13,
Roger Cummings through Matthew J Cunic, all in Box 159 at archival location
230/86/29/04. The index page, Army occupation-code page, Ernest Cuneo finding
aid, Congressional Record page and Vassar College finding-aid page used for
publication were rendered and visually inspected.

The next unprocessed sequence is page 101 rows 14-23, Laurence W Cunningham
through Winfred P Cunningham, all in Box 159.

## Research outcomes

- Exact private identifiers confirm Melvin F Cummins and Matthew J Cunic as
  enlisted Army personnel. Cummins's 1945 Army entry postdates OSS and is not
  projected backward. Cunic's 1942 occupation code supports only an unskilled
  textile-manufacturing occupation group, never a named employer.
- Herman L Cundiff remains conflicting because his exact index identifier and
  exact name point to different Army records. Neither alternative is selected.
- Two official sources confirm Ernest Cuneo as Ernest L. Cuneo and document
  earlier New York Daily News work, a LaGuardia law-secretary assignment and a
  1936-1940 Democratic National Committee associate-general-counsel role.
- The DNC is published only as Cuneo's medium-confidence, probable-immediate
  and best-supported last civilian affiliation. The post-1940 gap remains
  visible and the claim is excluded from confirmed/high default analytics.
- A direct OSS obituary and Vassar finding aid confirm Julia Cuniberti and her
  1944 college chronology. Vassar is a student affiliation, not an employer.
- Roger Cummings, Elizabeth J Cummins and Sidney S Cummins remain unresolved;
  William H Cummings and Henry C Cummins remain ambiguous. No common-name Army
  or newspaper candidate is silently assigned.
- Ten CIA checks returned no candidates. Two Library of Congress candidates
  were rejected from full OCR context because they named William W. and
  William A. Cummings, not William H. Cummings.

No employer was inferred from an occupation, military record, student status,
namesake, private identifier, later career or search snippet. Immediate
affiliation, last civilian employer and earlier documented work remain
separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,838 | 23,940 | 20.2089% |
| Verified affiliation found | 553 | 23,940 | 2.3099% |
| Verified employer found | 246 | 23,940 | 1.0276% |
| Archival disposition assessed | 4,793 | 23,940 | 20.0209% |
| Not started | 19,102 | 23,940 | 79.7911% |

Published data contains 1,919 affiliations, 603 organizations, 3,275 sources
and 3,816 claims. The private validated database contains 1,931 affiliations,
615 organizations, 4,446 citation records, 2,031 unique source documents,
3,963 claims, 7,273 research attempts and 9,358 claim-source links. Claim-
confidence totals are 1,142 confirmed, 1,422 high, 1,151 medium, 144 low and
104 conflicting. Ninety-eight conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,264 active people, documented as not
commissioned for 5,896 and unknown for 15,780. Personnel categories include
2,131 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,208 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,657 unknown or
indeterminate.

Identity-status counts are 979 confirmed, 687 high confidence, 151 probable,
196 ambiguous, 93 conflicting and 21,834 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 138 |
| conflicting_sources | 92 |
| documented_prewar_employer_found | 97 |
| in_progress | 44 |
| needs_identity_review | 248 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,102 |
| occupation_only_found | 879 |
| requires_archival_review | 3,001 |
| verified_employer_found | 231 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed. The
  cohort index page and four supporting-source pages used for publication were
  separately rendered and visually checked.
- The review ledger contains two rejected LoC candidates and replays
  idempotently. The evidence bundle validates under the strict Pydantic schema
  and imports idempotently as eight sources, five organization inputs, five
  affiliations, fifteen claims, ten person updates and ten synthesized
  research outcomes.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 24/24 Batch 507 checks passed across desktop, phone and
  tablet.
- Bounded core browser QA: 54/54 selected search, filter, direct-route,
  citation, organization, analysis and download checks passed across three
  viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 131 source files with zero errors, warnings or hints and built
  24,551 HTML pages / 24,623 artifacts.
- Link audit: all 24,551 internal HTML pages resolve; 49,881 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,098 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size matches across 24,623 artifacts. The evidence bundle and
  review ledger contain no raw strict private identifiers.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `58f23a5cd5e666aef0f32fad35b1f93ce11e26ad73deb389f4d046e6df2bf811`;
  the 24,623-file production-tree digest is
  `2cbf488a66bddb9f261257a12705b57fbe26d0385ffbfb268259096f044546f9`.
  The 67-file public manifest covers 91,018,147 bytes and has SHA-256
  `9b06bbd69277801d2df51d0c84a624caef79bdbd19f12d945f4c53f457f7c987`.
- One initially over-broad historical-matrix command was deliberately stopped
  after 94 clean passes; its interrupted 95th case is not counted as a product
  failure or as part of the bounded result above.

## Resume commands

From the repository root, Batch 507 can be reproduced and checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch507.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-one-roger-cummings-through-matthew-cunic-pathways_batch-507_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch507.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
```

Research resumes with page 101 rows 14-23, Laurence W Cunningham through
Winfred P Cunningham.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research goal
remains active because 19,102 person entities have not yet started the research
protocol. The generated entity-resolution report retains its pre-existing
warning that not every possible duplicate group is marked for manual review;
Batch 507 creates no new duplicate group, merge or silent conflation.
