# Batch 536 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 536 preserves and researches personnel-index PDF page 107 rows 20-29,
Emiscah Davis through Howard Davis. All ten rows are in Box 170 at archival
location 230/86/29/06. The index page and cited Army occupation-code page were
rendered and visually inspected.

- Exact protected-identifier and full-name evidence confirms Fred C Davis and
  Howard Davis as enlisted Army personnel at entry on June 9, 1943, and March
  20, 1941, respectively.
- Their identifier-matched Army rows carry civilian-occupation value `226`.
  NARA's official Code No. 30 table defines `2-26` as “Cooks, except private
  family.” These are qualified entry-time occupation findings, not employer,
  self-employment or immediate-OSS-affiliation findings.
- Gerald W Davis remains an unresolved external identity. His printed `Maj`
  rank and commissioned Army classification remain visible as index-derived
  facts without assigning any of seven Army namesakes.
- Emiscah Davis, Eugene M Davis, Eugenia C Davis, Farrell J Davis, Foster E
  Davis, Gerald W Davis, Grover C Davis and Horace B Davis remain unresolved
  after the minimum protocol and direct researchers to Box 170.
- Horace Bancroft Davis's documented Federated Press, Simmons College and CIO
  News roles remain rejected candidates because no source links him to the
  protected value, Box 170 or OSS. A Florida-Georgia News editor lead is
  likewise not assigned to Howard Davis.

Ten bounded CIA Reading Room checks returned no candidates or errors. Forty
current Library of Congress attempts returned 114 unique candidates. Direct
official-item review reached 107 before the service returned HTTP 429; the
remaining seven Howard Davis results were screened through their public LoC
and search context. All candidates were rejected and all 114 decisions were
saved through the durable review workflow. The complete 9,200,232-row Army
merged file was scanned transiently; two eligible protected values produced
two strict matches. Full identifiers and raw Army rows were not retained. No
authenticated NARA Catalog API request was made.

The reviewed bundle contains three sources, no organizations, two occupation
affiliations, four claims, eight claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,128 | 23,940 | 21.4202% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,083 | 23,940 | 21.2322% |
| Not started | 18,812 | 23,940 | 78.5798% |

Published data contains 2,025 affiliations, 623 organizations, 3,432 sources
and 4,030 claims. The private validated database contains 2,037 affiliations,
635 organizations, 4,610 citation records, 2,084 unique source documents,
4,199 claims, 8,200 research attempts and 9,938 claim-source links. Claim-
confidence totals are 1,218 confirmed, 1,467 high, 1,241 medium, 166 low and
107 conflicting. Ninety-eight conflicting identities, 103 people with a
published conflict and 243 possible-duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,970 and unknown for 15,697. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,276 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,580 unknown or
indeterminate.

Active identity-status counts are 1,052 confirmed, 708 high confidence, 160
probable, 238 ambiguous, 98 conflicting and 21,684 unresolved.

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
| no_reliable_result_after_protocol | 138 |
| not_started | 18,812 |
| occupation_only_found | 944 |
| requires_archival_review | 3,112 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Index page 107 and Army code page 172 received separate
  visual checks.
- Focused browser QA passes all 48 Batch 536 checks across desktop, phone and
  tablet.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests passed.
- Bounded core browser QA passed 18/18; analysis browser QA passed 6/6.
- Accessibility passed 27/27 route-and-viewport axe cases in 1.7 minutes with
  no serious violations.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,861,626
  bytes at manifest SHA-256
  `0676e403a3ffc45d52c8165f2fdc138e7bda32d3656ca7987ea0f88afce92c04`.
- Astro checked 161 source files with zero errors, warnings or hints and built
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,946
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree.
- Three consecutive builds were byte-identical. Under the documented relative-
  path/content digest, the 70-file public tree covers 95,208,760 bytes at
  SHA-256
  `220c1ef6966cc6395062605660547a5b1725baebae78aede8c42255dd8dd1596`;
  the 24,643-file production tree covers 283,790,856 bytes at SHA-256
  `7fdf1238d93fb98c2aa6717489e5f44abb680a656e7e5bde09208aae5c261785`.
- The long-standing entity-resolution advisory remains explicit:
  `all_duplicate_groups_require_review` is not yet satisfied for every broad
  possible-duplicate cluster. Automatic name-only merges remain prohibited,
  the 243 groups stay visible and the profile-level duplicate review check
  passes.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-15_batch536.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-seven-emiscah-davis-through-howard-davis-pathways_batch-536_2026-09-15.json
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

Research resumes with PDF page 107 rows 30-39: Howell A Davis Jr through Jean
Davis, all in Box 170 at location 230/86/29/06.

## Release boundary

Batch 536 is the current exact-verified public release. Pull request #232 was
merged as commit `af3adc4ca850b542d458409e66e1017420bb5740`; PR Test run
34928915638, main Test run 34929378545 and Pages run 34929378541 succeeded.
The live verifier matched all 67 manifest assets, 92,861,626 manifest bytes,
seven core routes and ten direct Batch 536 profiles. The goal remains active.
