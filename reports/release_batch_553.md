# Batch 553 release report

Run: 2026-09-15 UTC

## Scope and outcomes

Batch 553 preserves and researches personnel-index PDF page 111 rows 6-15, E
E Dehaan through John B Deik. All ten rows are in Box 177 at archival location
`230/86/29/07`. The index region, the relevant official Army code-list page
and the accepted 1938-39 directory page were rendered and visually inspected.

- Official Smithsonian records support Herbert G Deignan at high identity
  confidence. His employment in the United States National Museum's Division
  of Birds from 1938 is the best-supported immediate and last civilian pre-OSS
  pathway with `strongly_date_bounded` temporal basis. His earlier Master
  position at Prince Royal College remains separate. The Smithsonian sources'
  Assistant Curator/Associate Curator title discrepancy is disclosed.
- Protected-identifier and exact-name agreement confirms John B Deik in the
  official Army merged file. Occupation code 097 supports only `Managers and
  officials, n.e.c.` at Army entry; no employer or specific job is inferred.
- A contemporary directory supports a probable match for Bernard U DeHosson
  and the occupation term `banking`. No bank is named, so the medium-confidence
  occupation is qualified and excluded from default employer analytics.
- Rae W Dehncke remains conflicting because the exact-name Army row disagrees
  with the index's protected identifier. None of the candidate row's date,
  occupation, branch or rank fields is adopted.
- E E Dehaan, Del Dehart, Hazel A Dehart, Hilda A Dehart, Hendrik Dehartog and
  Gwendolyn M DeHaviland remain unresolved after the completed protocol. Each
  retains Box 177 guidance and the required no-reliable-employer statement.

Ten CIA checks returned no candidates or errors. Ten current Library of
Congress checks returned two E E Dehaan candidates and no errors; both were
rejected because one named only `Mr. DeHaan` and the other was William DeHaan.
Ten web searches were preserved as dry-run plans before manual review. The
complete 9,200,232-row Army file was scanned transiently. Two private index
values are masked publicly. No authenticated NARA Catalog API request was
made.

The reviewed bundle contains seven sources, two organizations, four
affiliations, eight claims, sixteen claim-source links, ten person updates and
twenty review/synthesis attempts. Together with thirty adapter attempts, the
cohort adds fifty durable attempts and leaves every person at five. The bundle
contains one confirmed, three high-confidence, three medium-confidence and one
conflicting claim.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,298 | 23,940 | 22.1303% |
| Verified affiliation found | 579 | 23,940 | 2.4185% |
| Verified employer found | 257 | 23,940 | 1.0735% |
| Archival disposition assessed | 5,253 | 23,940 | 21.9424% |
| Not started | 18,642 | 23,940 | 77.8697% |

Published data contains 2,086 affiliations, 646 organizations, 3,535 sources
and 4,164 claims. The private validated database contains 2,099 affiliations,
659 organizations, 4,716 citation records, 2,144 unique source documents,
4,339 claims, 8,960 research attempts and 10,245 claim-source links. Claim-
confidence totals are 1,252 confirmed, 1,503 high, 1,290 medium, 172 low and
122 conflicting. One hundred ten active identities have `conflicting_sources`
status; 118 people have conflicts under the broader coverage calculation and
248 possible-duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 146 |
| conflicting_sources | 110 |
| documented_prewar_employer_found | 106 |
| in_progress | 44 |
| needs_identity_review | 294 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 207 |
| not_started | 18,642 |
| occupation_only_found | 975 |
| requires_archival_review | 3,150 |
| verified_employer_found | 240 |

Identity-status counts are 251 ambiguous, 1,086 confirmed, 112 conflicting,
723 high confidence, 167 probable and 21,601 unresolved. Commissioned-status
counts are 2,277 commissioned, 5,997 not commissioned and 15,666 unknown.

## Validation

- PDF ingest validation remains complete: all 522 pages are represented,
  23,978/23,978 printed rows are linked, all 32 warning rows are visually
  resolved and all 92 selected pages retain recorded review decisions.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Python: 95/95 unit tests pass.
- Focused browser QA passes all 57 Batch 553 checks across desktop, phone and
  tablet. Bounded core browser QA passes 18/18; analysis QA passes 6/6.
- Accessibility passes 27/27 route-and-viewport axe cases with no serious
  violations. The bounded browser total is 108/108.
- Stratified profile audit: all seven structural checks pass across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verifies all 67 listed assets and 94,079,413
  bytes at manifest SHA-256
  `2e04d2046b3a08a3631e42c799aa73ce924bbae5311f74e576baa1ca1d131312`.
- Astro checks 178 source files with zero errors, warnings or hints and builds
  24,594 HTML pages / 24,666 artifacts. All internal links resolve; 50,012
  external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,099 candidate substrings produce zero unexpected boundary matches across
  all 24,666 artifacts.
- Three exact GitHub Pages-configured builds are byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  96,426,538 bytes at SHA-256
  `4d089c02f1b46b5a5fb496a9a2fd7648413989265389f07cc6314718fb386a1a`;
  the 24,666-file production tree covers 285,673,555 bytes at SHA-256
  `d0dba5c2a21878da34bb0e400450815ae35839c51b4459d99e8cef2151f1041e`.
- The npm audit covers 379 dependencies and reports zero known vulnerabilities
  at every severity.
- No local `.env` or credential file is included in the release tree; the
  tracked `.env.example` retains only a blank placeholder.
- The long-standing entity-resolution advisory remains explicit: automatic
  name-only merges are prohibited and all 248 possible-duplicate groups stay
  visible for review.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-eleven-e-e-dehaan-through-john-b-deik-pathways_batch-553_2026-09-15.json
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

Batch 553 completed personnel-index PDF page 111 rows 6-15. Research resumes
with page 111 rows 16-25, Andries Deinum through Egilio P Delaini, all in Box
177 at location `230/86/29/07`.

## Release boundary

Batch 552 at immutable commit
`07f26a7a142005e021346c3a1637e3bdd34f660a` remains the current
exact-verified public release until this Batch 553 candidate passes clean
replay, review, merge, deployment and independent live verification. The goal
remains active.
