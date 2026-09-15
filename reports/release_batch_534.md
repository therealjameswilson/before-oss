# Batch 534 release report

Run: 2026-09-14 ET / 2026-09-15 UTC

## Scope and outcomes

Batch 534 preserves and researches personnel-index PDF page 106 row 46 and
page 107 rows 1-9, John R Davies through Charles N Davis, all in Box 169 at
archival location 230/86/29/06. The two index pages and three cited Army
occupation-code pages were rendered and visually inspected.

- Exact private-identifier evidence confirms Amos Davis, Buster B Davis and
  Charles C Davis as enlisted Army personnel at entry.
- Their Army-entry occupation categories are farm hands on general farms;
  pressmen and plate printers, printing; and secondary-school teachers and
  principals. These are qualified occupations, not named employers.
- John R Davies, John H Davies, Martha A Davies, Thomas M Davies, W O Davies,
  Charles T Davis and Charles N Davis remain unresolved after the minimum
  protocol. Name-only Army rows and online namesakes remain unassigned.
- John R Davies retains the indexed `T/Sgt` enlisted classification without
  an external identity claim. The other unresolved profiles remain unknown or
  indeterminate rather than being forced into a personnel category.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks returned 34 candidates; all were reviewed
in official item or full-text context and rejected through the durable review
workflow. The complete 9,200,232-row Army merged file was scanned transiently.
Three private values were eligible for strict comparison and all three people
received accepted identifier-and-name matches. Full identifiers and raw Army
rows were not retained. No authenticated NARA Catalog API request was made.

The reviewed bundle contains three sources, no organizations, three
affiliations, six claims, 12 claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,108 | 23,940 | 21.3367% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,063 | 23,940 | 21.1487% |
| Not started | 18,832 | 23,940 | 78.6633% |

Published data contains 2,023 affiliations, 623 organizations, 3,427 sources
and 4,025 claims. The private validated database contains 2,035 affiliations,
635 organizations, 4,604 citation records, 2,084 unique source documents,
4,194 claims, 8,104 research attempts and 9,928 claim-source links. Claim-
confidence totals are 1,215 confirmed, 1,467 high, 1,239 medium, 166 low and
107 conflicting. Ninety-eight conflicting identities and 243 possible-
duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,967 and unknown for 15,700. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,273 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,583 unknown or
indeterminate.

Active identity-status counts are 1,049 confirmed, 708 high confidence, 160
probable, 238 ambiguous, 98 conflicting and 21,687 unresolved.

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
| no_reliable_result_after_protocol | 121 |
| not_started | 18,832 |
| occupation_only_found | 942 |
| requires_archival_review | 3,111 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Index pages 106-107 and Army code pages 171, 173 and 176
  received separate visual checks.
- Focused browser QA passes all 48 Batch 534 checks across desktop, phone and
  tablet.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests passed.
- Bounded core browser QA passed 18/18; analysis browser QA passed 6/6.
- Accessibility passed 27/27 route-and-viewport axe cases in 1.6 minutes with
  no serious violations.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,816,730
  bytes at manifest SHA-256
  `8df9e3acfb9f64d47199584e63494d64e22456602a3e705dba2edc3dd13f11b3`.
- The clean replay's Astro check covered 159 source files with zero errors,
  warnings or hints and built
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,946
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,103 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree.
- Three consecutive builds were byte-identical. Under the documented relative-
  path/content digest, the 70-file public tree covers 95,163,863 bytes at
  SHA-256
  `6dc4e7279f7457ad350644fb55afe219282b105434809e8738f5417fbb1aa62e`;
  the 24,643-file production tree covers 283,724,050 bytes at SHA-256
  `bdaa22a5a65e65dbb285e458dfe7204c9761eca226e2864972b9c5a1f8ed57f9`.
- Pull request #230 was merged as commit
  `b8b0e2ea9c2e7b4c7053d708207dd8c94a984452`. PR Test run 34921536919,
  main Test run 34921981099 and Pages run 34921981119 passed. The live verifier
  matched all 67 manifest assets, 92,816,730 manifest bytes, seven core routes
  and all ten direct cohort profiles to that immutable commit.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch534.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-six-and-one-hundred-and-seven-john-r-davies-through-charles-n-davis-pathways_batch-534_2026-09-14.json
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

Research resumes with PDF page 107 rows 10-19: Charlotte M Davis through the
indexed spelling Emiliy C Davis, crossing from Box 169 to Box 170 at location
230/86/29/06.

## Release boundary

Batch 534 is the current exact-verified public release. The goal remains
active and research resumes with Batch 535.
