# Batch 537 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 537 preserves and researches personnel-index PDF page 107 rows 30-39,
Howell A Davis Jr. through Jean Davis. All ten rows are in Box 170 at archival
location 230/86/29/06. The index page and cited Army occupation-code page were
rendered and visually inspected.

- Exact protected-identifier and full-name evidence confirms James M Davis as
  enlisted Army personnel at entry on March 1, 1942.
- His identifier-matched Army row carries civilian-occupation value `684`.
  NARA's official Code No. 30 table defines `6-84` as “Structural- and
  ornamental-metal workers.” This is a qualified entry-time occupation
  finding, not an employer, specific trade, workplace or immediate-OSS-
  affiliation finding.
- Irvin P Davis remains conflicting rather than resolved. His protected
  identifier returns an entirely different full name, while the exact-name
  Army row carries another identifier. Neither record's occupation or personal
  details are assigned, and the unrelated Army subject's identity is not
  retained in the reviewed bundle or public projection.
- Howell A Davis Jr., Hoyt B Davis, Isabelle M Davis, Jack E Davis, James A
  Davis, James E Davis, Jane M Davis and Jean Davis remain unresolved after
  the minimum protocol and direct researchers to Box 170.

Ten bounded CIA Reading Room checks and forty current Library of Congress
attempts completed with no candidates or errors. The complete 9,200,232-row
Army merged file was scanned transiently. Strict matching supported the one
accepted identity and exposed the one conflict; name-only candidates remain
unassigned. Full identifiers and raw Army rows were not retained. No
authenticated NARA Catalog API request was made.

The reviewed bundle contains three sources, no organizations, one occupation
affiliation, three claims, six claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports
idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,138 | 23,940 | 21.4620% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,093 | 23,940 | 21.2740% |
| Not started | 18,802 | 23,940 | 78.5380% |

Published data contains 2,026 affiliations, 623 organizations, 3,435 sources
and 4,033 claims. The private validated database contains 2,038 affiliations,
635 organizations, 4,613 citation records, 2,084 unique source documents,
4,202 claims, 8,230 research attempts and 9,944 claim-source links. Claim-
confidence totals are 1,219 confirmed, 1,467 high, 1,242 medium, 166 low and
108 conflicting. Ninety-nine conflicting identities, 104 people with a
published conflict and 243 possible-duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,971 and unknown for 15,696. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,277 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,579 unknown or
indeterminate.

Active identity-status counts are 1,053 confirmed, 708 high confidence, 160
probable, 238 ambiguous, 99 conflicting and 21,682 unresolved.

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
| no_reliable_result_after_protocol | 146 |
| not_started | 18,802 |
| occupation_only_found | 945 |
| requires_archival_review | 3,112 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Index page 107 and Army code physical page 178 / printed
  page XXV received separate visual checks.
- Focused browser QA passes all 48 Batch 537 checks across desktop, phone and
  tablet.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests and all 43 subtests passed.
- Bounded core browser QA passed 18/18; analysis browser QA passed 6/6.
- Accessibility passed 27/27 route-and-viewport axe cases in 1.6 minutes with
  no serious violations.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,888,056
  bytes at manifest SHA-256
  `ba14dbf76dc11db6dea909a73f870f927ef91cefb5409329528516c487c58a9a`.
- Astro checked 162 source files with zero errors, warnings or hints and built
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,946
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree; the tracked
  `.env.example` retains only a blank placeholder.
- Three exact GitHub Pages-configured builds were byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,235,186 bytes at SHA-256
  `eef30b8d4ec37d8d7cd3e7ab73223380319f2f7d0e53fb0020931753cb01af62`;
  the 24,643-file production tree covers 285,099,539 bytes at SHA-256
  `5fa7c6e1eaef9346a0319fa2c51189463fcc4c8335c0d3e9b6ac2369374ec303`.
- The long-standing entity-resolution advisory remains explicit:
  `all_duplicate_groups_require_review` is not yet satisfied for every broad
  possible-duplicate cluster. Automatic name-only merges remain prohibited,
  the 243 groups stay visible and the profile-level duplicate review check
  passes.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-seven-howell-a-davis-jr-through-jean-davis-pathways_batch-537_2026-09-15.json
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

Research resumes with personnel-index PDF page 107 rows 40-46 and page 108
rows 1-3, beginning John T Davis and continuing through the next ten
contiguous source rows. Both pages require rendering and visual inspection
before research.

## Release boundary

Batch 537 is the current exact-verified public release. Pull request #233 was
merged as commit `189d1612fd0afa49ec8c13aeea58b9a2d0b1f8a7`; PR Test run
34932227187, main Test run 34932770088 and Pages run 34932770066 succeeded. The immutable live verifier
matched all 67 manifest assets, 92,888,056 manifest bytes, seven core routes
and ten direct Batch 537 profiles at that merge commit. The goal remains active.
