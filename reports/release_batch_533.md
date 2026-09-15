# Batch 533 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 533 preserves and researches personnel-index PDF page 106 rows 36-45,
John J Davidson through F T Davies, all in Box 169 at archival location
230/86/29/06. The index page and four cited Army occupation-code pages were
rendered and visually inspected.

- Exact private-identifier evidence confirms John J Davidson, John T
  Davidson Jr. and Kenneth E Davidson as enlisted Army personnel at entry.
  John T Davidson Jr.'s exact identifier selects the token-equivalent Army
  name `DAVIDSON JOHN T JR`; the index's raw column order explains the suffix
  placement difference.
- Their Army-entry occupation categories are managers and officials, not
  elsewhere classified; stenographers and typists; and farm hands on general
  farms. These are qualified occupations, not named employers.
- Milton Davidson, Rebecca D Davidson, Thomas Davidson, Alfred Davies, David
  M Davies, Elspeth V Davies and F T Davies remain unresolved after the
  minimum protocol. Name-only Army rows and online namesakes remain
  unassigned.
- David M Davies retains the indexed `T-3` enlisted classification without an
  external identity claim. F T Davies retains the indexed `Col` and foreign-
  or-Allied classification while commissioned status remains unknown.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks returned 14 candidates; all were reviewed
in official item or full-text context and rejected through the durable review
workflow. The complete 9,200,232-row Army merged file was scanned
transiently. Three private values were eligible for strict comparison and all
three people received accepted identifier-and-compatible-name matches. Full
identifiers and raw Army rows were not retained. No authenticated NARA
Catalog API request was made.

The reviewed bundle contains three sources, no organizations, three
affiliations, six claims, 12 claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,098 | 23,940 | 21.2949% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,053 | 23,940 | 21.1069% |
| Not started | 18,842 | 23,940 | 78.7051% |

Published data contains 2,020 affiliations, 623 organizations, 3,424 sources
and 4,019 claims. The private validated database contains 2,032 affiliations,
635 organizations, 4,601 citation records, 2,084 unique source documents,
4,188 claims, 8,074 research attempts and 9,916 claim-source links. Claim-
confidence totals are 1,212 confirmed, 1,467 high, 1,236 medium, 166 low and
107 conflicting. Ninety-eight conflicting identities and 243 possible-
duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,964 and unknown for 15,703. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,270 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,586 unknown or
indeterminate.

Active identity-status counts are 1,046 confirmed, 708 high confidence, 160
probable, 238 ambiguous, 98 conflicting and 21,690 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 97 |
| documented_prewar_employer_found | 101 |
| in_progress | 44 |
| needs_identity_review | 285 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 114 |
| not_started | 18,842 |
| occupation_only_found | 939 |
| requires_archival_review | 3,111 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Index page 106 and Army code pages 171, 176, 177 and 178
  received separate visual checks.
- Focused browser QA passes all 51 Batch 533 checks across desktop, phone and
  tablet.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests passed.
- Bounded core browser QA passed 18/18; analysis browser QA passed 6/6.
- Accessibility: 25/27 cases passed in the aggregate run; the desktop Sources
  and tablet Analysis cases timed out under browser/display pressure, then each
  passed in focused reruns. All 27 route-and-viewport cases therefore have a
  passing Batch 533 result with no serious axe violations.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,776,434
  bytes at manifest SHA-256
  `f83b25d61879945e1dae3d6f0dc5613f654780cca5f3d61e8975eb07bd980a53`.
- The clean publish clone's Astro check covered 158 source files with zero
  errors, warnings or hints and built
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,946
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,102 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree.
- Three consecutive builds were byte-identical. Under the documented relative-
  path/content digest, the 70-file public tree covers 95,123,571 bytes at
  SHA-256
  `1eba7a4e036f2e609b02406ffd24b00d3bfb4708c6cded46fdcbc50b3061c7d9`;
  the 24,643-file production tree covers 283,663,242 bytes at SHA-256
  `6c71935bc5f67f362280058b128ab83a7fbe40438d7fa73e4db8eee61e9937d8`.
- Pull-request, main-branch and GitHub Pages workflow validation is pending.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch533.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-six-john-j-davidson-through-f-t-davies-pathways_batch-533_2026-09-14.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Research resumes with PDF page 106 row 46 and page 107 rows 1-9: John R
Davies through Charles N Davis, all in Box 169 at location 230/86/29/06.

## Release boundary

Batch 532 remains the current exact-verified public release until Batch 533's
pull request, main-branch Test workflow, Pages deployment and immutable live
verification succeed.
