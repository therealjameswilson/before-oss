# Batch 506 release report

Run: 2026-09-13 UTC

## Scope

Batch 506 preserves and researches personnel-index PDF page 100 rows 40-46 and
page 101 rows 1-3, Richard T Culp through Philip H Cummings, crossing from Box
158 to Box 159 at archival location 230/86/29/04. Both index pages, the newly
needed Army occupation-code passage and two institutional-history pages were
rendered and visually inspected.

The next unprocessed sequence is page 101 rows 4-13, Roger Cummings through
Matthew J Cunic, all in Box 159.

## Research outcomes

- Exact private-identifier evidence confirms Tom S Culverwell as enlisted Army
  personnel. An official code supports `Commercial artist` as his occupation at
  Army entry, not as an employer.
- Two institutional histories identify him as Thomas Speiden Culverwell,
  document Forest Service illustration and drafting work before World War II,
  and explicitly connect the same distinctive person to wartime OSS map work.
- The United States Forest Service is published as his high-confidence,
  strongly date-bounded last civilian employer before wartime service.
- The U.S. Army is a separate, medium-confidence, `probable_immediate`
  military affiliation because the exact Army-to-OSS transfer remains
  undocumented in accessible sources.
- His earlier artwork supplied to the *Washington Daily News* is kept as an
  unknown relationship rather than silently converted into employment or
  self-employment.
- Richard T Culp, William C Culp, David J Culver, Lester E Culverson and Philip
  H Cummings remain ambiguous. Exact-name Army candidates are retained without
  assignment because direct identifiers or additional selectors are absent.
- Maynard L Cumbers, William J Cummens, Louise D Cumming and Josephine C
  Cummings remain unresolved with Box 159 guidance. Source spellings and
  uncertainty are preserved.
- Ten CIA checks returned no candidates. Two Library of Congress newspaper
  candidates were rejected from full OCR context because they named William L.
  and William A. Culp, not William C. Culp.

No employer was inferred from an occupation, military assignment, namesake,
private identifier, later career or search snippet. Immediate affiliation,
last civilian employer and earlier documented work remain separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,828 | 23,940 | 20.1671% |
| Verified affiliation found | 550 | 23,940 | 2.2974% |
| Verified employer found | 245 | 23,940 | 1.0234% |
| Archival disposition assessed | 4,783 | 23,940 | 19.9791% |
| Not started | 19,112 | 23,940 | 79.8329% |

Published data contains 1,914 affiliations, 599 organizations, 3,267 sources
and 3,806 claims. The private validated database contains 1,926 affiliations,
611 organizations, 4,438 citation records, 2,027 unique source documents,
3,948 claims, 7,243 research attempts and 9,328 claim-source links. Claim-
confidence totals are 1,138 confirmed, 1,418 high, 1,150 medium, 139 low and
103 conflicting. Ninety-seven conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,264 active people, documented as not
commissioned for 5,894 and unknown for 15,782. Personnel categories include
2,131 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,206 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,659 unknown or
indeterminate.

Identity-status counts are 975 confirmed, 687 high confidence, 151 probable,
194 ambiguous, 92 conflicting and 21,841 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 137 |
| conflicting_sources | 91 |
| documented_prewar_employer_found | 96 |
| in_progress | 44 |
| needs_identity_review | 246 |
| needs_temporal_review | 17 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,112 |
| occupation_only_found | 878 |
| requires_archival_review | 2,998 |
| verified_employer_found | 231 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed. The
  two cohort pages, official code-list passage and both institutional-history
  pages used for publication were separately rendered and visually checked.
- The review ledger contains two rejected LoC candidates and replays
  idempotently. The evidence bundle validates under the strict Pydantic schema
  and imports idempotently as six sources, three organization inputs, four
  affiliations, fourteen claims, ten person updates and ten synthesized
  research outcomes.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 21/21 Batch 506 checks passed across desktop, phone and
  tablet.
- Bounded core browser QA: 57/57 selected search, filter, direct-route,
  citation, organization, analysis and download checks passed across three
  viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 130 source files with zero errors, warnings or hints and built
  24,547 HTML pages / 24,619 artifacts.
- Link audit: all 24,547 internal HTML pages resolve; 49,872 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,098 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size matches across 24,619 artifacts. The evidence bundle and
  review ledger contain no raw strict private identifiers.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `51ff6ca0c5a8e554ca1df0b78dbff52a91e00bd23690ee36a38387cf6e269dcb`;
  the 24,619-file production-tree digest is
  `ac7a1f8f30f55d38931810e869d07c84f7eb0be400ce29767ffe734e6f1941c4`.
  The 67-file public manifest covers 90,919,533 bytes and has SHA-256
  `52e8844a162b43c54d6c00b35561d17ada19f2207ea8cadac7edb6075d1c3301`.

## Resume commands

From the repository root, Batch 506 can be reproduced and checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch506.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-one-richard-culp-through-philip-cummings-pathways_batch-506_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch506.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
```

Research resumes with page 101 rows 4-13, Roger Cummings through Matthew J
Cunic.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research goal
remains active because 19,112 person entities have not yet started the research
protocol. The generated entity-resolution report retains its pre-existing
warning that not every possible duplicate group is marked for manual review;
Batch 506 creates no new duplicate group, merge or silent conflation.
