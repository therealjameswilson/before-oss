# Batch 531 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 531 preserves and researches personnel-index PDF page 106 rows 16-25,
Isabelle Davenport through the first of two consecutive Elizabeth Davey rows.
All ten immutable rows are in Box 168 at archival location 230/86/29/05. The
index page, the two cited Army occupation-code pages and the Elizabeth Davey
institutional source page were rendered and visually inspected.

- Exact private-identifier evidence confirms James L Davenport, John H
  Davenport Jr. and page-106 row-23 Donald L Davey as enlisted Army personnel
  at entry.
- Their Army-entry occupation categories are carpenter; occupations in
  manufacture of textiles, not elsewhere classified; and linemen and
  servicemen in telegraph, telephone and power. These are qualified
  occupations, not named employers.
- The second Donald L Davey row remains a separate unresolved entity in the
  same possible-duplicate group. The first row's Army record was neither
  copied to nor used to merge the second.
- Leo Davenport has a documented official-record conflict: the printed private
  identifier selects an Army row under a different full name, while the
  exact-name Army hit carries a different identifier. Neither record is
  assigned, and the profile directs researchers to Box 168.
- Isabelle Davenport, John S Davenport III, Riley Davenport and Roslyn
  Davenport remain unresolved after the minimum protocol.
- A Lovell Historical Society article identifies an Elizabeth Davey Velen as
  an OSS member, but it cannot distinguish the two consecutive Elizabeth
  Davey index rows. The identity lead remains private, low-confidence,
  withheld and unassigned. Radcliffe attendance is not classified as
  employment and a later United Nations career is not recast as pre-OSS.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks returned four candidates; official OCR
showed three different James Davenport namesakes and a Second Lt. John B.
Davenport Jr., and all were rejected through the durable review workflow. The
complete 9,200,232-row Army merged file was scanned transiently. Five private
values were eligible for strict comparison, three people received accepted
identifier-and-name matches, Leo Davenport produced a conflicting result and
Riley Davenport had no Army hit. Full identifiers and raw Army rows were not
retained. No authenticated NARA Catalog API request was made.

The reviewed bundle contains four sources, no organizations, three
affiliations, seven claims, 14 claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports
idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,078 | 23,940 | 21.2114% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,033 | 23,940 | 21.0234% |
| Not started | 18,862 | 23,940 | 78.7886% |

Published data contains 2,014 affiliations, 623 organizations, 3,417 sources
and 4,006 claims. The private validated database contains 2,026 affiliations,
635 organizations, 4,593 citation records, 2,083 unique source documents,
4,174 claims, 8,014 research attempts and 9,888 claim-source links. Claim-
confidence totals are 1,206 confirmed, 1,466 high, 1,230 medium, 165 low and
107 conflicting. Ninety-seven conflicting identities and 243 possible-
duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,958 and unknown for 15,709. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,264 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,592 unknown or
indeterminate.

Active identity-status counts are 1,040 confirmed, 707 high confidence, 160
probable, 237 ambiguous, 97 conflicting and 21,699 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 96 |
| documented_prewar_employer_found | 101 |
| in_progress | 44 |
| needs_identity_review | 284 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 104 |
| not_started | 18,862 |
| occupation_only_found | 933 |
| requires_archival_review | 3,109 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Index page 106, Army code pages 173-174 and the Lovell
  article's physical page 6 received separate visual checks.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests passed.
- Focused browser QA passes all 54 Batch 531 checks across desktop, phone and
  tablet.
- Bounded core browser QA passed 18/18; analysis browser QA passed 6/6.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,682,273
  bytes at manifest SHA-256
  `1203c94e6c3d5a0c9287afe8d591a7ed8ffde8ed74aadb0dda6c7aa6b485b1b3`.
- Astro checked 156 source files with zero errors, warnings or hints and built
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,946
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,103 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree.
- Three consecutive builds were byte-identical. Under the documented relative-
  path/content digest, the 70-file public tree covers 95,029,412 bytes at
  SHA-256
  `c814aeaa33577a7188ecdcf8b7997faa1fd0d4406c23d93e2984492eee268f12`;
  the 24,643-file production tree covers 283,523,570 bytes at SHA-256
  `866fe4dcc614411975badaa4e768d60dd289dd0edbfd512a53112a6237b84974`.
- Pull request #227 was merged as commit
  `a54a2c00c6853aa6cd22ffc982cd1a6260178d6f`. PR Test run 34902061949,
  main Test run 34902691961 and Pages run 34902691962 succeeded. The live
  verifier matched all 67 manifest assets / 92,682,273 manifest bytes, seven
  core routes and ten direct cohort profiles to that immutable commit. GitHub
  emitted a non-blocking maintenance warning that several v4 actions still
  declare Node.js 20 and are currently forced onto Node.js 24.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch531.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-six-isabelle-davenport-through-elizabeth-davey-pathways_batch-531_2026-09-14.json
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

Research resumes with PDF page 106 rows 26-35: the second Elizabeth Davey row
through Jean A Davidson. The Elizabeth duplicate-name relationship must carry
forward without merging the source rows unless direct evidence supports it.

## Release boundary

Batch 531 is the current exact-verified public release. The release boundary is
merge commit `a54a2c00c6853aa6cd22ffc982cd1a6260178d6f`, independently passed
by the pull-request and main-branch Test workflows, deployed by GitHub Pages,
and verified live against the checked-in manifest and all ten cohort profiles.
