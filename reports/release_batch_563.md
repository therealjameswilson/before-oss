# Batch 563 release report

Run: 2026-09-16 UTC

## Scope and outcomes

Batch 563 researches personnel-index PDF page 113 rows 14-23, John D Dempsey
through Gusbert DenBesten, in Boxes 179-180 at `230/86/29/07`. The complete
source page and the 1942 Cincinnati directory entry at printed page 284 / PDF
page 288 were rendered at 180 dpi and visually inspected. Five private index
values remain masked in every public artifact. John F Dempsey's seven-digit
printed value remains unchanged and was not silently padded.

- A direct May 1944 OSS report confirms Joseph Denaro by exact name and
  protected-identifier agreement. It dates his OSS entry and subsequent Army
  induction through OSS and reports that he supervised beauty-salon personnel
  in civilian life.
- The 1942 Cincinnati directory independently lists Joseph Denaro as a
  hairdresser at Mabley's. Exact name, city, occupation and close chronology
  support a high-confidence employer claim. Mabley's is modeled separately as
  his immediate pre-OSS affiliation and last civilian employer, not collapsed
  into a single generic employer field.
- John D Dempsey's discovery-only Burma OSS obituary lead remains
  low-confidence and unpublished. Official French inventory file
  `GR 16 P 174420` for Jean Pierre Denamiel is also retained only as an
  identity lead pending direct comparison.
- Livia M Denain and Livia M Demian remain separate in their visible
  possible-duplicate group. John F Dempsey, Mary E Demsford, Robert E Demuth,
  Lorene Denard, Dennis Denaxas and Gusbert DenBesten remain unresolved.
  Gusbert's index note `possibly` is preserved.

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
| Research attempted | 5,396 | 23,940 | 22.5397% |
| Verified affiliation found | 585 | 23,940 | 2.4436% |
| Verified employer found | 259 | 23,940 | 1.0819% |
| Archival disposition assessed | 5,351 | 23,940 | 22.3517% |
| Not started | 18,544 | 23,940 | 77.4603% |

Published data contains 2,125 affiliations, 658 organizations, 3,596 sources
and 4,313 claims. The private validated database contains 2,139 affiliations,
672 organizations, 4,784 citation records, 2,176 unique source documents,
4,493 claims, 9,460 research attempts and 10,513 claim-source links. Claim-
confidence totals are 1,280 confirmed, 1,586 high, 1,325 medium, 177 low and
125 conflicting. The coverage report retains 121 conflict records and 253
visible possible-duplicate groups.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 147 |
| conflicting_sources | 113 |
| documented_prewar_employer_found | 109 |
| in_progress | 44 |
| needs_identity_review | 313 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 210 |
| not_started | 18,544 |
| occupation_only_found | 999 |
| requires_archival_review | 3,193 |
| verified_employer_found | 242 |

Identity-status counts are 266 ambiguous, 1,113 confirmed, 115 conflicting,
732 high confidence, 175 probable and 21,539 unresolved. Commissioned-status
counts are 2,283 commissioned, 6,033 not commissioned and 15,624 unknown.

## Validation

- Evidence validation accepts six sources, one organization, one affiliation,
  fourteen claims, twenty-one claim-source links, ten person updates and twenty
  attempts. Two consecutive reimports leave all stable-ID table counts
  unchanged.
- The sanitized adapter checkpoint preserves 4,075 bounded CIA, Library of
  Congress, web and NARA adapter attempts without query text, response payloads,
  credentials or private research notes.
- Public-data construction reports 23,978 rows, 23,940 active people, 26
  profile shards and passing redaction checks.
- Entity-resolution QA passes all corpus-wide checks: every source row is
  linked, no name-only automatic merge exists, and all 253 possible-duplicate
  groups require review.
- Python: 95/95 unit tests pass.
- Astro checks 188 source files with zero errors, warnings or hints and builds
  24,606 HTML pages.
- Final CI-mode browser QA passes 78/78 checks: 21 current-batch, 24 core route
  and interaction, 6 analysis, and 27 accessibility checks across desktop,
  phone and tablet. The large Sources accessibility route completed in
  25.9-26.6 seconds with no serious violations.
- All internal links resolve; 50,041 unique external URLs are inventoried for
  separate live checking.
- The local public-manifest guard verifies all 67 listed assets and 94,921,623
  bytes at manifest SHA-256
  `3f3e3e988d2b005fcba9f2201cc68e0c8fe4b9180a477576e96d16dbba6de9c4`.
- The 70-file public tree covers 97,268,760 bytes at deterministic SHA-256
  `34599bcc2b607bc66267377b53843b8e0a91896eda47f91fe1ae6a7e56d6dc2f`.
- The production tree contains 24,678 files and 289,155,721 bytes at SHA-256
  `021576cd8993fdcdfae2d40d0d497dfe3d3f4125f81836ac1826367644a0154a`.
- The 200-profile stratified structural audit passes all seven checks. This is
  not an independent historical rereview.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 candidate substrings produce zero unexpected boundary, aggregate or
  manifest-size matches across all 24,678 artifacts.
- A detached archive replay from commit `7e87431bdedeafe229dc726a00243f03b80ebdc5`
  copied only the frozen source PDF (SHA-256
  `7268492342ab131d3b6d2697cfa4f6856cbdcd16e0ed3877e8d6a0478f58c02b`),
  rebuilt the database and public assets, installed 276 locked npm packages,
  and repeated Astro's 188-file check and 24,606-page build. It reproduced the
  70-file public tree, 24,678-file production tree and 67-asset manifest at the
  exact hashes reported above.
- No local `.env` or credential file is included in the release tree; tracked
  ignore rules cover `.env` while `.env.example` remains allowed.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-thirteen-john-d-dempsey-through-gusbert-denbesten-pathways_batch-563_2026-09-16.json
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

Batch 563 completes the accessible-source protocol for page 113 rows 14-23.
Research resumes with page 113 rows 24-33. The overall goal remains active.
