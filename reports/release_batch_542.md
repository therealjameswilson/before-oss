# Batch 542 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 542 preserves and researches personnel-index PDF page 108 rows 34-43,
Chiles W Dawson through Raymond L Day. All ten rows are in Box 173 at archival
location 230/86/29/06. The index page and both cited Army occupation-code pages
were rendered and visually inspected.

- Captain Joseph T Dawson is confirmed as Joseph Turner Dawson through exact
  protected-identifier agreement with a public military-awards register, plus
  matching name and rank. A reproduced 1944 general order directly places him
  in Company G, 2d Battalion, 16th Infantry Regiment, 1st Infantry Division.
  A dated biography says his OSS transfer followed his Aachen command and
  hospitalization, so the division is published as a medium-confidence
  probable-immediate military assignment, not a civilian employer.
- A named 1998 *Corpus Christi Caller-Times* obituary documents Dawson's work
  as a geologist for Humble Oil and Renwar Oil and his 1941 enlistment. A
  discovery-only chronology places Ren-War from 1938 to enlistment. Ren-War is
  therefore published as the best-supported last civilian employer and Humble
  Oil as an earlier prewar employer, both visibly qualified at medium
  confidence pending Box 173 confirmation. The discovery source is retained
  only for context and is never the sole final evidence.
- Exact protected-identifier and full-name agreement confirms Titus C Dawson,
  Linard F Day and Paul W Day as enlisted Army personnel at entry. Their
  official occupation values map respectively to “Construction occupations,
  n. e. c.,” “Newsboys,” and “Chauffeurs and drivers, bus, taxi, truck, and
  tractor.” These support qualified entry-time occupation findings, not named
  employers, workplaces, exact duties or immediate OSS predecessors.
- Chiles W Dawson, Audrey S Day, Cletis O Day, Elizabeth A Day, Ernest A Day
  and Raymond L Day remain unresolved after the minimum protocol, with
  critical-priority Box 173 guidance. Raymond's exact-name Army candidate was
  rejected because its protected identifier differs.

Ten bounded CIA Reading Room checks completed with zero candidates or errors.
Ten current Library of Congress API searches returned fifteen candidates, all
context-reviewed and rejected through the durable decision workflow. The
complete 9,200,232-row Army merged file was scanned transiently. Seven private
index values are masked publicly; full identifiers, unrelated subjects' names
and raw Army rows were not retained. No authenticated NARA Catalog API request
was made.

The reviewed bundle contains seven sources, three organizations, six
affiliations, ten claims, twenty-three claim-source links, ten person updates
and ten synthesized terminal research outcomes. Repeated imports preserve the
same logical rows and counts.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,188 | 23,940 | 21.6708% |
| Verified affiliation found | 571 | 23,940 | 2.3851% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,143 | 23,940 | 21.4829% |
| Not started | 18,752 | 23,940 | 78.3292% |

Published data contains 2,040 affiliations, 627 organizations, 3,461 sources
and 4,062 claims. The private validated database contains 2,052 affiliations,
639 organizations, 4,641 citation records, 2,096 unique source documents,
4,235 claims, 8,420 research attempts and 10,016 claim-source links. Claim-
confidence totals are 1,230 confirmed, 1,471 high, 1,254 medium, 170 low and
110 conflicting. One hundred active identities have published conflict
notices; 106 people have conflicts under the broader coverage calculation and
246 possible-duplicate groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,978 and unknown for 15,689. Personnel categories include
2,136 commissioned Army officers, 89 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,284 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,572 unknown or
indeterminate.

Active identity-status counts are 1,064 confirmed, 710 high confidence, 160
probable, 243 ambiguous, 101 conflicting and 21,662 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 145 |
| conflicting_sources | 100 |
| documented_prewar_employer_found | 102 |
| in_progress | 44 |
| needs_identity_review | 285 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 176 |
| not_started | 18,752 |
| occupation_only_found | 953 |
| requires_archival_review | 3,119 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved and all 92 selected
  pages are reviewed. Index page 108 and Army-code physical pages 171 and 174
  received separate visual checks.
- Focused browser QA passes all 57 Batch 542 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests pass.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 108/108.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,158,889
  bytes at manifest SHA-256
  `4d3dd625bfae482d947bcdf37e26d9317d83915f909c3a7891d0ea051a622ace`.
- Astro checks 167 source files with zero errors, warnings or hints and builds
  24,575 HTML pages / 24,647 artifacts. All internal links resolve; 49,960
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,104 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,647 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree; the tracked
  `.env.example` retains only a blank placeholder.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,506,028 bytes at SHA-256
  `a593bd041082fbe232605ac19af7160a48c6bb866872a6c1280bb4aa196e24ac`;
  the 24,647-file production tree covers 284,239,334 bytes at SHA-256
  `d1fc8475c6d650db2cb4e92c28b4111e9db4fdc5775112cc051473014cbc64ba`.
- The first focused run correctly exposed six assertions that referenced the
  wrong statistics property or used incorrect capitalization. The assertions
  were corrected to the actual generated schema and visible labels; the final
  focused suite passes 57/57 with no product-data change.
- The long-standing entity-resolution advisory remains explicit:
  `all_duplicate_groups_require_review` is not yet satisfied for every broad
  possible-duplicate cluster. Automatic name-only merges remain prohibited,
  the 246 groups stay visible and the profile-level duplicate review check
  passes.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-eight-chiles-w-dawson-through-raymond-l-day-pathways_batch-542_2026-09-15.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-15_batch542.csv
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release -- batch542.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Research resumes with personnel-index PDF page 108 rows 44-46 and page 109
rows 1-7, Richard A Day Jr. through Louis R DeAlva, crossing Boxes 173-174.
Re-render and inspect both cohort regions before research; keep the adjacent
ranked and unranked Bruce E Deahl rows separate unless direct evidence
establishes duplication.

## Release boundary

Batch 542 is exact-verified in production. Pull request #238 used branch commit
`be754deb792eed60146d74a0164e2b1aa15d8c11` and merged as
`41eb10b98488da48a094ef8a1795e423837b17f7`. PR Test run 34951716727, main
Test run 34952390247 and Pages run 34952390156 all completed successfully. The
production verifier matched all 67 manifest assets, 93,158,889 bytes, seven
core routes and ten direct Batch 542 profiles at manifest SHA-256
`4d3dd625bfae482d947bcdf37e26d9317d83915f909c3a7891d0ea051a622ace`.
The goal remains active.
