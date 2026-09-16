# Batch 557 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 557 researches personnel-index PDF page 111 row 46 and page 112 rows
1-9, Joseph H Delgoffe through John A Dellangelo. All ten rows are in Box 178
at `230/86/29/07`. Both index pages, four official Army code pages and one
French resistance-index page were rendered and visually inspected. Eight
private index values remain masked publicly.

- Exact protected-identifier and name agreement confirms the serial-bearing
  John W Delgreco, Mark M D'Elia, Norman M Delisle and William M Delkin as
  unique Army-file matches.
- Their official Army-entry categories support only stenographer or typist,
  carpenter, student, and bookkeeper or cashier except bank cashier. None
  identifies an employer, immediate OSS predecessor or last civilian employer.
- The adjacent no-identifier John W DelGreco row remains a separate ambiguous
  entity. Both rows share one visible possible-duplicate group; the Army
  occupation is not copied across.
- Exact name, French rank and OSS context support Marcel Delhomme at high
  identity confidence. Two official SHD resistance dossiers remain visible
  alternatives requiring comparison with Box 178.
- A same-name John A DeLisa Army candidate was rejected because its identifier
  conflicts with the protected index value. No occupation or date is assigned.
- Joseph H Delgoffe, Elizabeth Della and John A Dellangelo remain unresolved
  with critical-priority Box 178 actions and dignified research-status claims.

Ten CIA checks and ten Library of Congress checks returned no accepted
candidates. Ten web plans were retained before targeted manual review. The
complete 9,200,232-row Army file was scanned twice during validation. No
authenticated NARA Catalog API request was made and no credential or raw live
response was stored.

The reviewed bundle contains six sources, four affiliations, fifteen claims,
thirty claim-source links, ten person updates and twenty review/synthesis
attempts. With thirty adapter attempts, the batch adds fifty durable attempts
and advances terminal research and archival-disposition coverage by ten
people.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,337 | 23,940 | 22.2932% |
| Verified affiliation found | 582 | 23,940 | 2.4311% |
| Verified employer found | 258 | 23,940 | 1.0777% |
| Archival disposition assessed | 5,292 | 23,940 | 22.1053% |
| Not started | 18,603 | 23,940 | 77.7068% |

Published data contains 2,110 affiliations, 656 organizations, 3,565 sources
and 4,223 claims. The private validated database contains 2,123 affiliations,
669 organizations, 4,747 citation records, 2,159 unique source documents,
4,398 claims, 9,163 research attempts and 10,356 claim-source links. Claim-
confidence totals are 1,264 confirmed, 1,525 high, 1,314 medium, 172 low and
123 conflicting. There are 249 visible possible-duplicate groups.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 146 |
| conflicting_sources | 111 |
| documented_prewar_employer_found | 109 |
| in_progress | 44 |
| needs_identity_review | 302 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,603 |
| occupation_only_found | 987 |
| requires_archival_review | 3,161 |
| verified_employer_found | 241 |

Identity-status counts are 258 ambiguous, 1,098 confirmed, 113 conflicting,
729 high confidence, 172 probable and 21,570 unresolved. Commissioned-status
counts are 2,280 commissioned, 6,014 not commissioned and 15,646 unknown.

## Validation

- Evidence validation accepts all six sources, four affiliations, fifteen
  claims, ten person updates and twenty attempts. A second evidence import
  leaves the stable-ID row set unchanged.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- The two source pages and all code/index pages used in this batch were
  visually inspected after rendering.
- Python: 95/95 unit tests pass.
- Focused Batch 557 browser QA passes 24/24 checks across desktop, phone and
  tablet. The bounded release suite passes 78/78 checks: 24 current-batch, 21
  core route and interaction, 6 analysis, and 27 accessibility tests. Its core
  checks also verify the oil-company category across all three viewports.
- Astro checks 182 source files with zero errors, warnings or hints and builds
  24,604 HTML pages. All internal links resolve; 50,033 external URLs are
  inventoried for separate live checking.
- Three consecutive production builds produce the identical 24,676-file,
  286,311,583-byte tree at SHA-256
  `2b5dec35b9ff86d222d2410c3f43d3da8066a3e6fe3c3f55c6671b344d634ce6`.
- The local public-manifest guard verifies all 67 listed assets and 94,477,888
  bytes at manifest SHA-256
  `9ad26ae71a220d57e7b24e348080fc53ebac3a44ef0a47d55c5268755b0e8914`.
- The 70-file public tree covers 96,825,013 bytes at deterministic SHA-256
  `6575381ef9650c6a0d5e0623ba52a3e7580733b009d4ca2e7c32878886dded6d`.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary matches across
  all 24,676 artifacts.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-eleven-joseph-h-delgoffe-through-john-a-dellangelo-pathways_batch-557_2026-09-15.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 scripts/verify_deployed_release.py --local-public-root site/public
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release
npm --prefix site run check:links
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Batch 557 completes the protocol for page 111 row 46 and page 112 rows 1-9.
Research resumes with page 112 rows 10-19. The overall goal remains active.
