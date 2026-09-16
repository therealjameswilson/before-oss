# Batch 561 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 561 researches personnel-index PDF page 112 rows 40-46 and page 113 rows
1-3, George C Demas through Leon M Demers. All ten printed rows are preserved
in Box 179 at `230/86/29/07`. Both complete source pages and Army code-list
physical pages 173 and 304 were rendered at 180 dpi and visually inspected.
Five private index values remain masked in all public artifacts.

- Exact protected-identifier and normalized-name agreement confirms John Demas
  Jr., Joseph A Dematteo and Gilbert Dementis as Army-file matches and Army
  privates.
- Their Army-entry records support two qualified student statuses and one broad
  machinist occupation. No school, employer, workplace, trade specialty or
  immediate Army-to-OSS transition is named, so all three remain
  occupation-only findings excluded from verified-employer counts.
- Samuel F Demastrie's protected identifier resolves to a differently named
  entrant in the separate Army conversion. The identity is explicitly
  conflicting; the unrelated name, identifier, date and occupation are not
  published or assigned.
- Leon M Demers's printed seven-digit value remains unchanged. It cannot be
  padded to select an exact-name Army row, so the candidate's occupation is not
  assigned.
- George C Demas, Priscilla DeMauduit, Anthony DeMayo, Gertrude J Dembe and
  Fernando DeMello remain unresolved after the staged protocol. Anthony's
  separately documented wartime pathfinder namesake is explicitly rejected.

Ten CIA checks, ten Library of Congress checks and ten web query plans were
saved. The complete 9,200,232-row Army file was scanned. The reviewed bundle
adds twenty manual review/synthesis attempts, for fifty durable attempts in the
batch. No authenticated NARA Catalog API request was made and no credential,
request header, raw live response or full private identifier entered the
repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,376 | 23,940 | 22.4561% |
| Verified affiliation found | 583 | 23,940 | 2.4353% |
| Verified employer found | 258 | 23,940 | 1.0777% |
| Archival disposition assessed | 5,331 | 23,940 | 22.2682% |
| Not started | 18,564 | 23,940 | 77.5439% |

Published data contains 2,121 affiliations, 656 organizations, 3,583 sources
and 4,283 claims. The private validated database contains 2,134 affiliations,
669 organizations, 4,768 citation records, 2,165 unique source documents,
4,458 claims, 9,360 research attempts and 10,461 claim-source links. Claim-
confidence totals are 1,276 confirmed, 1,562 high, 1,324 medium, 172 low and
124 conflicting. The coverage report retains 120 conflict records and 251
visible possible-duplicate groups.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 147 |
| conflicting_sources | 112 |
| documented_prewar_employer_found | 109 |
| in_progress | 44 |
| needs_identity_review | 307 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,564 |
| occupation_only_found | 997 |
| requires_archival_review | 3,183 |
| verified_employer_found | 241 |

Identity-status counts are 263 ambiguous, 1,110 confirmed, 114 conflicting,
730 high confidence, 172 probable and 21,551 unresolved. Commissioned-status
counts are 2,281 commissioned, 6,023 not commissioned and 15,636 unknown.

## Validation

- Evidence validation accepts four sources, three affiliations, seventeen
  claims, twenty-seven claim-source links, ten person updates and twenty
  attempts. Two consecutive reimports leave all stable-ID table counts
  unchanged.
- The sanitized adapter checkpoint preserves 4,015 bounded CIA, Library of
  Congress, web and NARA adapter attempts without query text, response payloads,
  credentials or private research notes.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Entity-resolution QA passes all three corpus-wide checks: every source row is
  linked, no name-only automatic merge exists, and all 251 possible-duplicate
  groups require review.
- Python: 95/95 unit tests pass.
- Final CI-mode browser QA passes 81/81 checks: 24 current-batch, 24 core route
  and interaction, 6 analysis, and 27 accessibility checks across desktop,
  phone and tablet. The large Sources accessibility route completed in
  25.4-26.1 seconds with no serious violations.
- Astro checks 185 source files with zero errors, warnings or hints and builds
  24,604 HTML pages. All internal links resolve; 50,036 unique external URLs
  are inventoried for separate live checking.
- The local public-manifest guard verifies all 67 listed assets and 94,770,534
  bytes at manifest SHA-256
  `400075865ee2b5cee293fc4fdf686854f64b95f0c369779d40753a557236ac4e`.
- The 70-file public tree covers 97,117,662 bytes at deterministic SHA-256
  `eb8ac1a589079bbb235f521b4cc362888bfee8fe77b48f8eeadda8c1e3f3971d`.
- The production tree contains 24,676 files and 288,919,486 bytes at SHA-256
  `92c9faf9784b36fef9a9787d9dce93f3a34a496897a26566424999d95ea28985`.
- A detached clean-room replay from commit `9f3139e`, using only the frozen
  522-page source PDF, versioned evidence, review decisions and sanitized
  adapter checkpoint, regenerated the exact database totals above. After a
  locked `npm ci`, it reproduced both the public-tree and production-tree
  hashes byte for byte. The first package install was blocked by sandbox DNS;
  the authorized retry completed with zero reported vulnerabilities.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,676 artifacts.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-pages-one-hundred-and-twelve-and-thirteen-george-c-demas-through-leon-m-demers-pathways_batch-561_2026-09-16.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
CI=1 npm --prefix site run test:release
npm --prefix site run check:links
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Batch 561 completes the accessible-source protocol for page 112 rows 40-46 and
page 113 rows 1-3. Research resumes with page 113 rows 4-13. The overall goal
remains active.
