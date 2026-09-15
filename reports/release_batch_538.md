# Batch 538 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 538 preserves and researches personnel-index PDF page 107 rows 40-46
and page 108 rows 1-3, John T Davis through Mary L Davis. John R Davis Jr. is
in Box 170; the other nine rows are in Box 171 at archival location
230/86/29/06. Both index pages and the cited Army occupation-code pages were
rendered and visually inspected.

- Exact protected-identifier and full-name evidence confirms John R Davis Jr.
  as enlisted Army personnel at entry on September 23, 1942. His Army row
  carries occupation value `992`; NARA's official table defines `4-92`,
  `6-92`, and `8-92`, but not `9-92`, so the value remains uninterpreted.
- Exact protected-identifier and full-name evidence confirms Lloyd G Davis as
  enlisted Army personnel at entry on October 30, 1940. NARA's official Code
  No. 30 table defines his entry-time occupation value `137` as
  “Stenographers and typists.” This supports a qualified occupation finding,
  not an employer, workplace, exact job title, or immediate-OSS-affiliation
  finding.
- Leonard R Davis retains the index-derived commissioned Army classification
  from printed rank `Lt`; Louie D Davis retains the index-derived enlisted
  classification from `Sgt`. Neither classification resolves the person's
  identity to an outside Army row.
- John T Davis, Joseph W Davis, Leonard R Davis, Louie D Davis, Louis B Davis,
  Malcolm W Davis, Marion R Davis, and Mary L Davis remain unresolved after
  the minimum protocol. The profiles preserve rejection reasons and point to
  Box 171 for archival examination.
- The well-documented international-affairs official named Malcolm W. Davis
  remains an unassigned lead because no reviewed source connects that
  biography to the OSS index row or Box 171.

Ten bounded CIA Reading Room checks completed with no candidates or errors.
Ten current Library of Congress query requests returned 25 newspaper-page
candidates; all 25 official page contexts were inspected and rejected through
the durable human-review workflow. The complete 9,200,232-row Army merged file
was scanned transiently. Strict matching supported the two accepted identities;
all name-only candidates remain unassigned. Seven-character private values
were never padded, full identifiers and raw Army rows were not retained, and
no authenticated NARA Catalog API request was made.

The reviewed bundle contains three sources, no organizations, one occupation
affiliation, three claims, six claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports
idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,148 | 23,940 | 21.5038% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,103 | 23,940 | 21.3158% |
| Not started | 18,792 | 23,940 | 78.4962% |

Published data contains 2,027 affiliations, 623 organizations, 3,438 sources
and 4,036 claims. The private validated database contains 2,039 affiliations,
635 organizations, 4,616 citation records, 2,084 unique source documents,
4,205 claims, 8,260 research attempts and 9,950 claim-source links. Claim-
confidence totals are 1,221 confirmed, 1,467 high, 1,243 medium, 166 low and
108 conflicting. Ninety-nine conflicting identities, 104 people with a
published conflict and 243 possible-duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,973 and unknown for 15,694. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,279 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,577 unknown or
indeterminate.

Active identity-status counts are 1,055 confirmed, 708 high confidence, 160
probable, 238 ambiguous, 99 conflicting and 21,680 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 98 |
| documented_prewar_employer_found | 101 |
| in_progress | 44 |
| needs_identity_review | 285 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 154 |
| not_started | 18,792 |
| occupation_only_found | 946 |
| requires_archival_review | 3,113 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Index pages 107-108 and Army code physical pages 171,
  176 and 177 received separate visual checks.
- Focused browser QA passes all 51 Batch 538 checks across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis QA passed 6/6.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests and all 43 subtests passed.
- Accessibility passed 27/27 route-and-viewport axe cases in 1.7 minutes with
  no serious violations.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,913,597
  bytes at manifest SHA-256
  `2021ddc832d044fc9edfe5725f345a52f9f1e60904ed305df57f7b648ffaf84e`.
- Astro checked 163 source files with zero errors, warnings or hints and built
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,946
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,100 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree; the tracked
  `.env.example` retains only a blank placeholder.
- Three exact GitHub Pages-configured builds were byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,260,728 bytes at SHA-256
  `bf20ecf83d8a275e29186ddfcfc3312b015751917a97790592e45234cbbf34b8`;
  the 24,643-file production tree covers 283,868,230 bytes at SHA-256
  `dbb3e9a6a9add241a5e253d56d98891878790b352e0674dc217a6134d6015eb9`.
- An exploratory full browser run passed 741 cases before surfacing five stale
  Batch 187, 201 and 382 expectations for an earlier corrected Army
  occupation label. Those expectations were corrected, their 21 targeted
  viewport cases pass, and the current focused, core and analysis release
  suites pass.
- The long-standing entity-resolution advisory remains explicit:
  `all_duplicate_groups_require_review` is not yet satisfied for every broad
  possible-duplicate cluster. Automatic name-only merges remain prohibited,
  the 243 groups stay visible and the profile-level duplicate review check
  passes.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-15_batch538.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-seven-john-t-davis-through-page-one-hundred-and-eight-mary-l-davis-pathways_batch-538_2026-09-15.json
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

Research resumes with personnel-index PDF page 108 rows 4-13, Mary P Davis
through Robert T Davis. All ten rows are at location 230/86/29/06; Robert W
Davis is in Box 172 and the other nine are in Box 171. Re-render and inspect
the relevant page region, preserve every row and private value independently,
and do not merge the four Robert Davis entries by normalized name.

## Release boundary

Batch 538 is the current local release candidate. Batch 537 remains the
exact-verified public release at merge commit
`189d1612fd0afa49ec8c13aeea58b9a2d0b1f8a7`. The goal remains active.
