# Batch 565 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 565 researches personnel-index PDF page 113 rows 34-43, William Denit
through John M Dennis, all in Box 180 at `230/86/29/07`. The complete source
page, the relevant Army occupation-code page and Anthony Denneau's official
OSS transfer-memorandum page were rendered and visually inspected. Six private
index values remain masked in every public artifact.

- William Denit is a probable match to W. Darlington Denit. A reputable
  obituary explicitly links the rare surname to OSS and documents earlier
  accounting-clerk work at the Department of Agriculture. Other wartime agency
  roles are not ordered relative to OSS, so Agriculture is published only as
  documented prewar employment.
- Anthony J Denneau is identity-confirmed through an exact protected-identifier
  Army match, a January 1945 OSS transfer memorandum and an official National
  Park Service history. His Army-entry code supports stock-clerk occupation,
  not a named employer. His SO-ET to SO-CBI transfer remains internal OSS
  context and is not mislabeled as pre-OSS affiliation.
- Daniel C Dennet Jr. is a high-confidence spelling variant of Daniel Clement
  Dennett Jr. A first-person family account and independent New Yorker profile
  converge on full name, suffix, academic specialty, Beirut context and OSS
  recruitment. Clark University is qualified as a medium-confidence probable
  immediate and last civilian employer; American University of Beirut is
  preserved separately as earlier documented prewar employment. Harvard
  doctoral study is not converted into employment.
- Exact Army matches confirm Donald J Dennhardt, Edward J Dennis, James H
  Dennis and John M Dennis. Donald's and John's code 992 supports student
  status at Army entry, but no school or employer. Edward's undocumented
  occupation value is withheld. James H's 3 October 1945 entry postdates OSS
  dissolution and is not projected backward as pre-OSS evidence.
- Alfred P Dennis, 1st Lt James A Dennis and James S Dennis remain unresolved.
  Generic namesake candidates lacked the identity and temporal bridge required
  for attribution. James A's commissioned-officer status remains sourced only
  to the index, and the incomplete Army file is not treated as negative proof.

Ten CIA checks, ten Library of Congress checks and ten web query plans were
saved. The complete 9,200,232-row Army file was scanned. The reviewed bundle
adds twenty manual review/synthesis attempts, for fifty durable attempts in the
batch. No authenticated NARA Catalog API request was made, and no credential,
request header, raw live response or full private identifier entered the
repository.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,416 | 23,940 | 22.6232% |
| Verified affiliation found | 585 | 23,940 | 2.4436% |
| Verified employer found | 259 | 23,940 | 1.0819% |
| Archival disposition assessed | 5,371 | 23,940 | 22.4353% |
| Not started | 18,524 | 23,940 | 77.3768% |

Published data contains 2,133 affiliations, 661 organizations, 3,612 sources
and 4,352 claims. The private validated database contains 2,147 affiliations,
675 organizations, 4,800 citation records, 2,187 unique source documents,
4,533 claims, 9,560 research attempts and 10,602 claim-source links. Claim-
confidence totals are 1,286 confirmed, 1,605 high, 1,335 medium, 178 low and
129 conflicting. The coverage report retains 122 conflict records and 254
visible possible-duplicate groups.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 147 |
| conflicting_sources | 114 |
| documented_prewar_employer_found | 111 |
| in_progress | 44 |
| needs_identity_review | 316 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,524 |
| occupation_only_found | 1,004 |
| requires_archival_review | 3,202 |
| verified_employer_found | 242 |

Identity-status counts are 269 ambiguous, 1,121 confirmed, 116 conflicting,
734 high confidence, 176 probable and 21,524 unresolved. Commissioned-status
counts are 2,284 commissioned, 6,039 not commissioned and 15,617 unknown.

## Validation

- Evidence validation accepts nine sources, three organizations, six
  affiliations, twenty-four claims, fifty-three claim-source links, ten person
  updates and twenty attempts.
- The sanitized adapter checkpoint preserves 4,135 bounded CIA, Library of
  Congress, web and NARA adapter attempts without query text, response payloads,
  credentials or private research notes.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Entity-resolution QA passes all corpus-wide checks: every source row is
  linked, no name-only automatic merge exists, and all 254 possible-duplicate
  groups require review.
- Python: 95/95 unit tests pass.
- Astro checks 190 source files with zero errors, warnings or hints and builds
  24,609 HTML pages.
- Final CI-mode browser QA passes 84/84 checks: 27 current-batch, 24 core route
  and interaction, 6 analysis, and 27 accessibility checks across desktop,
  phone and tablet. The oil-company category tests pass in every viewport.
- All internal links resolve; 50,050 unique external URLs are inventoried for
  separate live checking.
- The local public-manifest guard verifies all 67 listed assets and 95,138,834
  bytes at manifest SHA-256
  `3d7f6ae80a20b9b4743ec16c232bddffcf5de24a5114969433b444d4dbb3dec4`.
- The 70-file public tree covers 97,485,969 bytes at deterministic SHA-256
  `3fdaebb4ef121b0c85ab77b1f44d6b555133c157076c6a6c7d674a0d9c87d2db`.
- The production tree contains 24,681 files and 289,497,664 bytes at SHA-256
  `267cfc715be5cb049b59e2599e736ab59cfca314cd747df5c500f2c6852cfcd3`.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,100 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,681 artifacts.
- A detached clean replay from release-candidate commit `21bff79` completed
  successfully. It reproduced the exact public-manifest, public-tree and
  production-tree hashes above, passed all 95 Python tests, and repeated the
  zero-false-positive public-identifier audit across all 24,681 artifacts.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

## Publication verification

Pull request #263 merged as main commit
`25b75758ee538f31f6fde0d4c323572f3aedbb19`. PR Test run 35103625940,
main Test run 35104404734 and Pages run 35104404934 succeeded. The
unauthenticated live verifier matched all 67 manifest assets, 95,138,834 bytes,
seven core routes and all ten direct Batch 565 profiles at manifest SHA-256
`3d7f6ae80a20b9b4743ec16c232bddffcf5de24a5114969433b444d4dbb3dec4`.
The deployed personnel directory retains the tested oil-company employee
category and its employment-only filter.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-thirteen-william-denit-through-john-m-dennis-pathways_batch-565_2026-09-16.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m oss_research validate-ingest
python3 -m oss_research audit-profiles --sample-size 200
python3 -m unittest discover -s tests -q
npm --prefix site run build
CI=1 npm --prefix site run test:release
npm --prefix site run check:links
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Batch 565 completes the accessible-source protocol for page 113 rows 34-43.
Research resumes with page 113 rows 44-46 and page 114 rows 1-7, Nancy Dennis
through Robert P Dent. The overall goal remains active.
