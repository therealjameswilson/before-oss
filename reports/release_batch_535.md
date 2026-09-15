# Batch 535 release report

Run: 2026-09-14 ET / 2026-09-15 UTC

## Scope and outcomes

Batch 535 preserves and researches personnel-index PDF page 107 rows 10-19,
Charlotte M Davis through the indexed spelling Emiliy C Davis. The first nine
rows are in Box 169 and the final row is in Box 170 at archival location
230/86/29/06. The index page and cited Army occupation-code page were rendered
and visually inspected.

- Exact private-identifier and full-name evidence confirms David M Davis as
  enlisted Army personnel at entry on December 15, 1942.
- His Army occupation value `944` is not published as an occupation. The
  official code table defines `5-44` and `7-44`, but not `9-44`; the project
  does not silently substitute a related code.
- Charlotte M Davis, Cleveland Davis, Cora J Davis, Curtis C Davis, David R
  Davis, Doris Davis, Dorothy Davis, Elizabeth T Davis and Emiliy C Davis
  remain unresolved after the minimum protocol and direct researchers to
  Boxes 169-170.
- `Emiliy` remains the indexed spelling. `Emily` is recorded only as a search
  alias, not a correction.

Ten bounded CIA Reading Room checks returned no candidates or errors. Sixteen
current Library of Congress attempts returned 45 candidates; all were reviewed
in official item or full-text context and rejected through the durable review
workflow. The resumable adapter recovered from one transient incomplete
response without repeating six completed request fingerprints. The complete
9,200,232-row Army merged file was scanned transiently; one eligible private
value produced one strict match. Full identifiers and raw Army rows were not
retained. No authenticated NARA Catalog API request was made.

The reviewed bundle contains three sources, no organizations or affiliations,
one identity claim, two claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,118 | 23,940 | 21.3784% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,073 | 23,940 | 21.1905% |
| Not started | 18,822 | 23,940 | 78.6216% |

Published data contains 2,023 affiliations, 623 organizations, 3,429 sources
and 4,026 claims. The private validated database contains 2,035 affiliations,
635 organizations, 4,607 citation records, 2,084 unique source documents,
4,195 claims, 8,140 research attempts and 9,930 claim-source links. Claim-
confidence totals are 1,216 confirmed, 1,467 high, 1,239 medium, 166 low and
107 conflicting. Ninety-eight conflicting identities and 243 possible-
duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,968 and unknown for 15,699. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,274 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,582 unknown or
indeterminate.

Active identity-status counts are 1,050 confirmed, 708 high confidence, 160
probable, 238 ambiguous, 98 conflicting and 21,686 unresolved.

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
| no_reliable_result_after_protocol | 130 |
| not_started | 18,822 |
| occupation_only_found | 942 |
| requires_archival_review | 3,112 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Index page 107 and Army code page 174 received separate
  visual checks.
- Focused browser QA passes all 45 Batch 535 checks across desktop, phone and
  tablet.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests passed.
- Bounded core browser QA passed 18/18; analysis browser QA passed 6/6.
- Accessibility passed 27/27 route-and-viewport axe cases in 1.6 minutes with
  no serious violations.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,831,424
  bytes at manifest SHA-256
  `348184d44f06d191cffe98babd1df1258c01ce4a199705f7477e338a7dd2751e`.
- The clean publish replay's Astro check covered 160 source files with zero
  errors, warnings or hints and built
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,946
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,102 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree.
- Three consecutive builds were byte-identical. Under the documented relative-
  path/content digest, the 70-file public tree covers 95,178,557 bytes at
  SHA-256
  `a0a11d0e7f2fa7fc96078df432d8a79ae029fc5f1040882223fd6ac30537b1d4`;
  the 24,643-file production tree covers 283,745,480 bytes at SHA-256
  `0834e4235c1978f0d5ddee48fee727b9d3d3528ec9d4166648581c06a4b9167e`.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch535.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-seven-charlotte-m-davis-through-emiliy-c-davis-pathways_batch-535_2026-09-14.json
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

Research resumes with PDF page 107 rows 20-29: Emiscah Davis through Howard
Davis, all in Box 170 at location 230/86/29/06.

## Release boundary

Batch 535 is a fully validated local release candidate. Batch 534 remains the
current exact-verified public release until the Batch 535 pull request, main-
branch checks, Pages deployment and exact live verification succeed. The goal
remains active.
