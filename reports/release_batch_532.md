# Batch 532 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 532 preserves and researches personnel-index PDF page 106 rows 26-35,
the second of two consecutive Elizabeth Davey rows through Jean A Davidson.
Rows 26-34 are in Box 168 at archival location 230/86/29/05; row 35 is in
Box 169 at 230/86/29/06. The index page, three cited Army occupation-code
pages and the NARA-hosted Homer David evidence page were rendered and visually
inspected.

- Exact private-identifier evidence confirms Charles W David, Donald J
  Davidson and George B Davidson as enlisted Army personnel at entry.
- Their Army-entry occupation categories are clerks, sales; actors and
  actresses; and machine shop and related occupations, not elsewhere
  classified. These are qualified occupations, not named employers.
- A direct official wartime OSS memorandum supports a high-confidence match
  between the indexed Major Homer David Jr. and Major Homer David at an August
  1945 OSS European Theater awards-board meeting. The suffix omission and lack
  of a private-identifier bridge remain explicit; the source provides no pre-
  OSS employer.
- The second Elizabeth Davey row remains a separate unresolved entity in the
  same possible-duplicate group as the first. The Elizabeth Davey Velen lead
  remains low-confidence, withheld and unassigned to either row.
- David Davidian remains ambiguous after his printed value produced no Army
  hit and two exact-name alternatives proved non-assignable.
- Abraham Davidson has a documented official-record conflict: the printed
  private value selects an Army row under a different full name, while seven
  exact-name Army rows carry other identifiers. No Army record is assigned.
- Nathan H David, Henrietta Davidson and Jean A Davidson remain unresolved
  after the minimum protocol.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks returned seven candidates; all were
visually or contextually reviewed and rejected through the durable review
workflow as OCR collisions, different namesakes or postwar evidence without an
OSS bridge. The complete 9,200,232-row Army merged file was scanned
transiently. Five private values were eligible for strict comparison and three
people received accepted identifier-and-name matches. Full identifiers and raw
Army rows were not retained. No authenticated NARA Catalog API request was
made.

The reviewed bundle contains five sources, no organizations, three
affiliations, eight claims, 16 claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,088 | 23,940 | 21.2531% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,043 | 23,940 | 21.0652% |
| Not started | 18,852 | 23,940 | 78.7469% |

Published data contains 2,017 affiliations, 623 organizations, 3,421 sources
and 4,013 claims. The private validated database contains 2,029 affiliations,
635 organizations, 4,598 citation records, 2,084 unique source documents,
4,182 claims, 8,044 research attempts and 9,904 claim-source links. Claim-
confidence totals are 1,209 confirmed, 1,467 high, 1,233 medium, 166 low and
107 conflicting. Ninety-eight conflicting identities and 243 possible-
duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,961 and unknown for 15,706. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,267 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,589 unknown or
indeterminate.

Active identity-status counts are 1,043 confirmed, 708 high confidence, 160
probable, 238 ambiguous, 98 conflicting and 21,693 unresolved.

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
| no_reliable_result_after_protocol | 107 |
| not_started | 18,852 |
| occupation_only_found | 936 |
| requires_archival_review | 3,111 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Index page 106, Army code pages 170, 176 and 177, and
  the NARA-hosted OSS memorandum's physical page 120 received separate visual
  checks.
- Focused browser QA passes all 54 Batch 532 checks across desktop, phone and
  tablet.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests passed.
- Bounded core browser QA passed 18/18; analysis browser QA passed 6/6.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.6 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,734,734
  bytes at manifest SHA-256
  `a5ef6a76e37695f9364dc8c1c7fc2fe29ebf00a8b60c254c6c47c6dd1400982c`.
- The clean publish clone's Astro check covered 157 source files with zero
  errors, warnings or hints and built
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,946
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree.
- Three consecutive builds were byte-identical. Under the documented relative-
  path/content digest, the 70-file public tree covers 95,081,873 bytes at
  SHA-256
  `2921d5e720d23c07811956a4cad8528b4723eef060aa0343d9763e6bea5b6087`;
  the 24,643-file production tree covers 283,600,849 bytes at SHA-256
  `f6f6471971d93866044660347f37b8ac74a9d3b7afd4b6d7e2267a34e988c759`.
- Pull request #228 was merged as commit
  `6a7fb2fe0e0444bd6ac4ea84e1aadd49ec4afc18`. PR Test run 34911041876
  passed in 5m28s, main Test run 34911466381 passed in 5m53s and Pages run
  34911466384 passed (build 1m19s and deploy 13s). The live verifier matched
  all 67 manifest assets / 92,734,734 manifest bytes, seven core routes and
  ten direct cohort profiles to that immutable commit. GitHub emitted a non-
  blocking maintenance warning that several v4/v5 actions still declare
  Node.js 20 and are currently forced onto Node.js 24.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch532.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-six-elizabeth-davey-through-jean-davidson-pathways_batch-532_2026-09-14.json
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

Research resumes with PDF page 106 rows 36-45: John J Davidson through F T
Davies, all in Box 169 at location 230/86/29/06.

## Release boundary

Batch 532 is the current exact-verified public release. The release boundary
is merge commit `6a7fb2fe0e0444bd6ac4ea84e1aadd49ec4afc18`, independently passed by
the pull-request and main-branch Test workflows, deployed by GitHub Pages, and
verified live against the checked-in manifest and all ten cohort profiles.
