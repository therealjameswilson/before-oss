# Batch 515 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 515 preserves and researches personnel-index PDF page 102 rows 38-46
and page 103 row 1, Mary W Cutler through Louise L Czako, all in Box 162 at
archival location 230/86/29/05. Both index pages, relevant Army code-list
passages and the Charles S. Cutting General Orders page were visually
inspected.

- Richard W Cutler is a high-confidence match to the OSS officer documented
  by NARA. An official FBI report and an independent biographical profile
  support Donovan, Leisure, Newton and Lumbard as his last civilian employer,
  where he worked as a lawyer. His intervening service as a second lieutenant
  in the United States Army Air Forces is modeled separately as the immediate
  pre-OSS military affiliation.
- Paul Cyr is a high-confidence identity match from exact name, a compatible
  1921 birth-year field, Caledonia County, Vermont residence and official NPS
  and CIA OSS biographies. Army civilian-occupation code 002 supports only the
  qualified historical category `Actors and actresses` at Army entry on 24
  February 1941. It is not promoted to a named employer or immediate pre-OSS
  affiliation.
- Charles S Cutting is a high-confidence exact-name and Lieutenant Colonel
  rank match to the officer documented in 1947 Army General Orders. The order
  establishes Infantry service from September 1943 through July 1944 but does
  not establish an employer or immediate OSS predecessor.
- Louise L Czako remains conflicting. The exact private value printed in the
  OSS index points to an Army row that prints Louis L Czako. A compatible
  Pennsylvania obituary cannot prove an index typo. The conflict stays visible
  and the Army occupation remains withheld.
- Mary W Cutler and Robert F Cutting remain ambiguous. Stuart G Cutler, Grace M
  Cutting, Theodore S Cutting and Claire H Cyr remain unresolved. Each has a
  dignified public status page and a specific Box 162 next action.
- Ten bounded CIA checks returned no candidates or errors. Ten current Library
  of Congress searches returned six candidate pages; all six were inspected in
  context and rejected through the durable review-decision importer.
- The complete 9,200,232-row Army file was scanned transiently. Name-only rows
  for Richard W Cutler and Robert F Cutting were not silently assigned, and
  no-hit outcomes were not treated as negative proof.

The batch adds eleven citation records, two organizations, three affiliations,
seven claims, twenty-four claim-source links, ten person updates and ten
synthesized terminal research outcomes. Public profiles preserve exact index
locators, seven masked private fields, source disagreement, confidence and
archival next actions.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,918 | 23,940 | 20.5430% |
| Verified affiliation found | 558 | 23,940 | 2.3308% |
| Verified employer found | 249 | 23,940 | 1.0401% |
| Archival disposition assessed | 4,873 | 23,940 | 20.3551% |
| Not started | 19,022 | 23,940 | 79.4570% |

Published data contains 1,942 affiliations, 608 organizations, 3,321 sources
and 3,865 claims. The private validated database contains 1,954 affiliations,
620 organizations, 4,495 citation records, 2,043 unique source documents,
4,031 claims, 7,521 research attempts and 9,523 claim-source links. Claim-
confidence totals are 1,155 confirmed, 1,438 high, 1,170 medium, 163 low and
105 conflicting. Ninety-nine conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,268 active people, documented as not
commissioned for 5,910 and unknown for 15,762. Personnel categories include
2,135 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,221 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,639 unknown or
indeterminate.

Active identity-status counts are 992 confirmed, 695 high confidence, 154
probable, 214 ambiguous, 94 conflicting and 21,791 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 138 |
| conflicting_sources | 93 |
| documented_prewar_employer_found | 98 |
| in_progress | 44 |
| needs_identity_review | 270 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,022 |
| occupation_only_found | 890 |
| requires_archival_review | 3,043 |
| verified_employer_found | 234 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed. The
  cohort index pages, code-list passages and General Orders page were
  separately rendered and inspected.
- The strict evidence bundle validates and imports idempotently as eleven
  sources, two organizations, three affiliations, seven claims, twenty-four
  claim-source links, ten person updates and ten synthesized outcomes.
- Six Library of Congress candidate decisions imported successfully with
  explicit rejection rationales.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests and 43 subtests passed.
- Focused browser QA: 24/24 Batch 515 checks passed across desktop, phone and
  tablet.
- Bounded core browser QA passed 18/18; analysis browser QA passed 6/6 across
  the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 2.2 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 140 source files with zero errors, warnings or hints and built
  24,556 HTML pages / 24,628 artifacts.
- Link audit: all 24,556 internal HTML pages resolve; 49,898 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  669 public-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size matches across 70 artifacts.
- Credential audit found only the blank `.env.example` template and no
  populated `NARA_API_KEY` assignment outside excluded database, build and
  dependency trees.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive stable-source builds were byte-identical. The 70-file public
  tree digest is
  `83ba3b39f5abf1d4542769e057a90547aac772e6b663abefdd7781355b4a5509`;
  the 24,628-file production-tree digest is
  `78243964a967b0e2d944d653d2b61dd31e9826c4ffccabbfa083d7e93ca4d0b0`.
  The 67-file public manifest covers 91,456,163 bytes and has SHA-256
  `72b7b3e889a3895bc41ab05215030f75426c1d293bc7fc66bcfd20c756c27010`.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch515.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-two-mary-w-cutler-through-louise-l-czako-pathways_batch-515_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release
python3 -m oss_research audit-profiles --sample-size 200
```

Research resumes with page 103 rows 2-11, Edmund Czaplinski through Arnold
Daane, in Boxes 162-163.

## Release boundary

Batch 515 is a validated local release candidate. Deployment commit, workflow
run identifiers and live-manifest verification will be added only after merge
and successful GitHub Pages publication. No authenticated NARA Catalog API
request was made. The research goal remains active because 19,022 person
entities have not yet started the research protocol. The generated entity-
resolution report retains its pre-existing warning that not every possible
duplicate group is marked for manual review; Batch 515 creates no new duplicate
group, merge or silent conflation.
