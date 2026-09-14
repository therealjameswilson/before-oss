# Batch 505 release report

Run: 2026-09-13 UTC

## Scope

Batch 505 preserves and researches personnel-index PDF page 100 rows 30-39,
Ruth B Culbertson through Carson W Culp, all in Box 158 at archival location
230/86/29/04. The index page, newly needed occupation-code passage and five
institutional finding-aid pages were rendered and visually inspected.

The next unprocessed sequence is page 100 rows 40-46 and page 101 rows 1-3,
Richard T Culp through Philip H Cummings, crossing from Box 158 to Box 159.

## Research outcomes

- The Library of Congress William Smith Culbertson Papers finding aid directly
  links a distinctive exact-name identity to War Department Military
  Intelligence and the OSS Planning Group. It explicitly documents Colonel,
  U.S. Army service, supporting commissioned classification without
  interpreting the private index value.
- Military Intelligence is the best-supported immediate pre-OSS affiliation,
  but the source does not state the precise transfer or overlap. It remains a
  qualified `probable_immediate` claim at medium confidence.
- Culbertson's Georgetown University employment, private law practice, Tariff
  Commission service and diplomatic postings are distinct affiliations.
  Georgetown is a named employer, but no reviewed source proves that it or the
  law practice was the last civilian employer before Army service.
- Exact private identifiers confirm William D Culbertson and Thomas M Cullens
  as enlisted Army personnel. Their official historical codes support only a
  checker occupation and a grouped garage-laborer/car-washer/greaser category;
  neither source names an employer or workplace.
- A State Historical Society of Missouri finding aid supports a probable James
  S Cullison identity and qualified Missouri School of Mines employment from
  1930 to 1945. With no OSS or Box 158 bridge, the claim is excluded from
  default employer analytics. His 1942 state-survey project is separate and
  temporally uncertain.
- Ruth B Culbertson, Helen M Culgen, Augustine Cullinan, Charles H Cullinan,
  Caroline E Cullings and Carson W Culp remain unresolved with Box 158 archival
  guidance. No weak namesake is promoted.
- Ten CIA checks returned no candidates. Sixteen actual Library of Congress
  attempts produced 18 candidates: one 1933 William S Culbertson item was
  accepted as corroborative identity evidence and 17 false, wrong-initial,
  spouse-only or postwar candidates were rejected in the durable review ledger.

No employer was inferred from an occupation, military assignment, namesake,
private identifier or search snippet. Immediate affiliation, last civilian
employer and earlier documented work remain separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,818 | 23,940 | 20.1253% |
| Verified affiliation found | 549 | 23,940 | 2.2932% |
| Verified employer found | 244 | 23,940 | 1.0192% |
| Archival disposition assessed | 4,773 | 23,940 | 19.9373% |
| Not started | 19,122 | 23,940 | 79.8747% |

Published data contains 1,910 affiliations, 598 organizations, 3,262 sources
and 3,801 claims. The private validated database contains 1,922 affiliations,
610 organizations, 4,432 citation records, 2,025 unique source documents,
3,934 claims and 7,206 research attempts. Claim-confidence totals are 1,137
confirmed, 1,417 high, 1,147 medium, 130 low and 103 conflicting. Ninety-seven
conflicts and 241 possible-duplicate groups remain visible.

Commissioned status is documented for 2,264 active people, documented as not
commissioned for 5,893 and unknown for 15,783. Personnel categories include
2,131 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,205 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,660 unknown or
indeterminate.

Identity-status counts are 974 confirmed, 687 high confidence, 151 probable,
189 ambiguous, 92 conflicting and 21,847 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 137 |
| conflicting_sources | 91 |
| documented_prewar_employer_found | 96 |
| in_progress | 44 |
| needs_identity_review | 241 |
| needs_temporal_review | 17 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,122 |
| occupation_only_found | 878 |
| requires_archival_review | 2,994 |
| verified_employer_found | 230 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed. Page
  100 rows 30-39 and the new official code-list passage were separately
  rendered and visually checked; the Culbertson and Cullison finding-aid pages
  used for publication were also rendered and inspected.
- The review ledger contains one accepted and 17 rejected LoC candidates and
  replays idempotently. The evidence bundle validates under the strict Pydantic
  schema and imports idempotently as seven sources, six organization inputs,
  nine affiliations, fifteen claims, ten person updates and ten synthesized
  research outcomes.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 21/21 Batch 505 checks passed across desktop, phone and
  tablet.
- Bounded core browser QA: 42/42 selected search, filter, direct-route,
  citation, organization, analysis and download checks passed across three
  viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.6 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 129 source files with zero errors, warnings or hints and built
  24,546 HTML pages / 24,618 artifacts.
- Link audit: all 24,546 internal HTML pages resolve; 49,869 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,102 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size matches across 24,618 artifacts. The evidence bundle and
  review ledger contain no raw strict private identifiers.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The 70-file
  public-tree digest is
  `99aa93b4d7e5a103130e81a50498ae1c4c4bb638e55bc279f63db05954d652b1`;
  the 24,618-file production-tree digest is
  `13e5fb94c28c82ef39cfab713c37d882c05f509b78640c915c91767a16b7af17`.
  The 67-file public manifest covers 90,852,990 bytes and has SHA-256
  `7fde8aa35508664fc1f53ba9f9309ec73396b508194be53ac9f423daacf00679`.

## Resume commands

From the repository root, Batch 505 can be reproduced and checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch505.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-ruth-culbertson-through-carson-culp-pathways_batch-505_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch505.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
```

Research resumes with page 100 rows 40-46 and page 101 rows 1-3, Richard T
Culp through Philip H Cummings.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research goal
remains active because 19,122 person entities have not yet started the research
protocol. The generated entity-resolution report retains its pre-existing
warning that not every possible duplicate group is marked for manual review;
Batch 505 creates no new duplicate group, merge or silent conflation.
