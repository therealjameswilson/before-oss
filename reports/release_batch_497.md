# Batch 497 release report

Run: 2026-09-13 UTC

## Scope

Batch 497 preserves and researches ten source rows across personnel-index PDF
page 98 rows 42-46 and page 99 rows 1-5, Diana I Croft through Russell H
Cromes, in Boxes 154-155 at archival locations 230/86/29/03 and 230/86/29/04.

The next unprocessed row is page 99, row 6, Raymond A Cromley, Box 155.

## Research outcomes

- Eddie L Croft, Robert J Croken, Flavus Cromeans and Russell H Cromes each
  have confirmed index-to-Army identities based on an exact complete private
  identifier. Each is classified as enlisted Army personnel.
- Their Army-entry rows support qualified occupation categories: roofers and
  slaters; metallurgists, assayers, and chemists; general farmers; and pressmen
  and plate printers. None names an employer, workplace, farm, or immediate
  pre-OSS affiliation.
- Russell's identifier-linked Army row spells the surname Cromez. That variant
  is published with the exact-identifier explanation while Cromes remains the
  preserved index spelling.
- Diana I Croft and Diana Crofts remain separate person entities and source
  rows in one visible possible-duplicate group. Adjacency and same box are not
  enough to merge them.
- Ann Crolius, Jeannette P Crolius and Joseph D Croll remain unresolved. The
  printed Anne B Croliuus row remains unresolved and needs identity review;
  later Anne B Crolius sources do not directly prove the correction or match.
- All twenty CIA and Library of Congress adapter searches succeeded without a
  candidate. The header-only review ledger was imported twice with no state
  changes.

No employer was inferred from an occupation code, postwar directory, family
entry, genealogy page, search-result snippet, adjacent index row, modern
namesake or spelling resemblance. Immediate pre-OSS affiliation, last civilian
employer and earlier documented occupation remain separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,738 | 23,940 | 19.7911% |
| Verified affiliation found | 541 | 23,940 | 2.2598% |
| Verified employer found | 241 | 23,940 | 1.0067% |
| Archival disposition assessed | 4,693 | 23,940 | 19.6032% |
| Not started | 19,202 | 23,940 | 80.2089% |

Published data now contains 1,859 affiliations, 578 organizations, 3,203
sources and 3,734 claims. The private validated database contains 1,870
affiliations, 590 organizations, 4,370 citations and 1,995 unique source
documents. Claim-confidence totals are 1,127 confirmed, 1,391 high, 1,116
medium, 103 low and 103 conflicting. Ninety-six conflicts and 241 possible-
duplicate groups remain visible.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 135 |
| conflicting_sources | 90 |
| documented_prewar_employer_found | 94 |
| in_progress | 44 |
| needs_identity_review | 225 |
| needs_temporal_review | 16 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,202 |
| occupation_only_found | 858 |
| requires_archival_review | 2,960 |
| verified_employer_found | 226 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- SQLite: `quick_check` returns `ok`; foreign-key check returns no rows.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 15/15 Batch 497 checks passed across desktop, phone and
  tablet after correcting one test-only label expectation to match the already
  correct public duplicate-group wording.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.6 minutes.
- Astro: 121 source files checked with zero errors, warnings or hints.
- Production build: 24,526 HTML pages and 24,598 artifacts.
- Link audit: all 24,526 internal HTML pages resolve; 49,824 unique external
  URLs were inventoried. All four Batch 497 official citation endpoints
  returned HTTP 200 to the generic checker.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,095 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,598 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Two consecutive clean public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `cef4b633e96d8376f2b31d9f4f1e25d29fdfb1ea12bb6f4eddbe5405451592dd`.
  The 24,598-file production-tree digest is
  `2cd6abb4a0e90c70ca2d67d2ec3a58e7d9c4a04d5adcc86eb87e374f97cf0926`.
  The 67-file public manifest covers 90,093,383 bytes and has SHA-256
  `492c10c8cff8f94df3b80aaa16fe6d056c1a6dbe6b7d1ba7c8b009bd6aa0a169`.

## Resume commands

From the repository root, the imported Batch 497 state can be reproduced and
checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch497.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-eight-and-ninety-nine-diana-i-croft-through-russell-h-cromes-pathways_batch-497_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
npm --prefix site run build
```

Research resumes with Raymond A Cromley, PDF page 99 row 6, followed by the
next nine immutable source rows.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research
goal remains active because 19,202 person entities have not yet started the
research protocol.
