# Batch 543 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 543 preserves and researches personnel-index PDF page 108 rows 44-46 and
page 109 rows 1-7, Richard A Day Jr. through Louis R DeAlva, crossing Boxes
173-174 at archival location 230/86/29/06. Both index-page regions and the
cited Army occupation-code page were rendered and visually inspected.

- Exact protected-identifier and full-name agreement confirms James L Dayley
  as enlisted Army personnel. His official Army entry records occupation value
  `992`; Code No. 30 physical page 304 defines `9-92` as “Students.” The result
  is a qualified entry-time student-status finding, not a named institution,
  employer, occupation or immediate OSS predecessor.
- A scholarly biography based chiefly on declassified OSS files supports a
  high-confidence Nicholas L Deak identity and documents Korody and Co. Inc.
  as his employer before enlistment. It also documents earlier teaching roles
  at Perkiomen School and City College of New York. A contemporary UPI obituary
  instead says that he founded Deak & Co. in 1940. Both accounts remain
  visible, the UPI pathway is conflicting and excluded from analytics, and
  Deak's profile directs review to Box 174.
- An Arthur R Dayton lead from a scholarly monograph lacks an index-specific
  identity bridge and is withheld at low confidence. A Louis R Dealva military
  namesake and Bruce Deahl directory/register namesakes were rejected because
  they establish neither the indexed identity nor pre-OSS employment.
- Richard A Day Jr., Christine W Dayton, Thomas P Dazey and Ada E Deakman
  remain unresolved. Arthur Dayton and Louis R DeAlva require archival review.
  The ranked and unranked Bruce E Deahl rows remain separate ambiguous entities
  in a visible manual-review duplicate group.

Ten bounded CIA Reading Room checks completed with zero candidates or errors;
one duplicate request fingerprint was skipped. Twenty current Library of
Congress API searches returned no candidates. Ten web searches were preserved
as dry-run plans. The complete 9,200,232-row Army merged file was scanned
transiently. Four private index values are masked publicly; full identifiers,
unrelated subjects' names and raw Army rows were not retained. No authenticated
NARA Catalog API request was made.

The reviewed bundle contains six sources, four organization upserts, six
affiliations, nine claims, sixteen claim-source links, ten person updates and
ten synthesized terminal research outcomes. Repeated imports preserve the same
logical rows and counts.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,198 | 23,940 | 21.7126% |
| Verified affiliation found | 571 | 23,940 | 2.3851% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,153 | 23,940 | 21.5246% |
| Not started | 18,742 | 23,940 | 78.2874% |

Published data contains 2,045 affiliations, 629 organizations, 3,466 sources
and 4,069 claims. The private validated database contains 2,058 affiliations,
642 organizations, 4,647 citation records, 2,101 unique source documents,
4,244 claims, 8,470 research attempts and 10,032 claim-source links. Claim-
confidence totals are 1,231 confirmed, 1,473 high, 1,257 medium, 172 low and
111 conflicting. One hundred one active identities have published conflict
notices; 107 people have conflicts under the broader coverage calculation and
247 possible-duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 145 |
| conflicting_sources | 101 |
| documented_prewar_employer_found | 102 |
| in_progress | 44 |
| needs_identity_review | 285 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 180 |
| not_started | 18,742 |
| occupation_only_found | 954 |
| requires_archival_review | 3,123 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved and all 92 selected
  pages are reviewed. Index pages 108-109 and Army-code physical page 304
  received separate visual checks.
- Focused browser QA passes all 60 Batch 543 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests pass.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 111/111.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 93,231,152
  bytes at manifest SHA-256
  `9619e5669f2e125e77bdcb91475d96f4b2fe96cc41d954abda7ba21811e4e435`.
- Astro checks 168 source files with zero errors, warnings or hints and builds
  24,577 HTML pages / 24,649 artifacts. All internal links resolve; external
  URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,649 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  95,578,295 bytes at SHA-256
  `f504c9d21d87dd1da762fbc5347083f3d34ab53c3e56f69fc29627826cd42c3f`;
  the 24,649-file production tree covers 284,351,751 bytes at SHA-256
  `0e4f7d6e77534bb3453cf3ad7969043fc060a705e6c1372e235efa04dd2e2b12`.
- The current online dependency advisory check could not run because the
  sandbox denied external package-registry metadata access. Dependencies and
  the lockfile are unchanged from Batch 542, whose audit reported zero
  vulnerabilities. No current result is inferred from that earlier run.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The first focused run exposed a stale production build that lacked the new
  Korody organization route. Rebuilding from the generated public data fixed
  the route; the complete final suite passes 111/111.
- The long-standing entity-resolution advisory remains explicit:
  `all_duplicate_groups_require_review` is not yet satisfied for every broad
  possible-duplicate cluster. Automatic name-only merges remain prohibited,
  the 247 groups stay visible and the profile-level duplicate review check
  passes.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-pages-one-hundred-and-eight-and-nine-richard-a-day-jr-through-louis-r-dealva-pathways_batch-543_2026-09-15.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release -- batch543.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Research resumes with personnel-index PDF page 109 rows 8-17, Harlowe F Dean
Jr. through Nato DeAngeles, all in Box 174. Re-render and inspect the cohort
region before research; keep William Dean and William A Dean separate unless
direct evidence establishes duplication.

## Release boundary

Batch 543 is released and exact-verified in production. Pull request 239 used
branch commit `1b744e6f93bde6b9832268b3b986397c6de7feb4` and merged as commit
`12f4ea9a3abc07ea6e89a244f1ccad6b867d4b13`. PR Test run 34956370238, main
Test run 34957513189 and Pages run 34957513184 succeeded. The independent live
verifier matched all 67 manifest assets, 93,231,152 bytes, seven core routes
and ten direct Batch 543 profiles against that immutable merge commit. The
goal remains active.
