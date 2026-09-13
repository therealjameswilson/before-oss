# Batch 500 release report

Run: 2026-09-13 UTC

## Scope

Batch 500 preserves and researches ten source rows on personnel-index PDF page
99, rows 26-35, Paul L Crosby through Paul W Crouch, all in Box 156 at archival
location 230/86/29/04. The source page and the relevant Army technical-code
pages were rendered at 180 dpi and visually inspected.

The next unprocessed row is page 99, row 36, Sherman J Crough.

## Research outcomes

- Exact private-identifier matches confirm Paul L Crosby, Vernon R Crosby and
  Allan B Cross as enlisted Army personnel. Their Army-entry categories are
  published as qualified occupations: warehousing/material handling, railroad
  clerk, and semiskilled radio/phonograph manufacturing. None names an
  employer or proves an immediate OSS sequence.
- Allan Cross's Army row has an impossible 1932 birth-year code beside a 1942
  entry date. The value remains a visible source anomaly and was not used for
  identity resolution.
- Institutional obituary evidence supports a high-confidence match between
  Gregg E Crouch and Gregg Elwyn Crouch: 1925 birth in Cherokee, Iowa, 1943
  Washta High School graduation, and service in both the Air Corps and OSS.
  Washta is modeled as student status, the Air Corps as military assignment,
  and the Army occupation as a qualified category. A one-character conflict
  between the printed index identifier and the exact-name Army row remains
  explicit, so the overall research status is `conflicting_sources`.
- Richard Crosby, J A Cross, James E Cross, Arthur W Crossley, Phyllis R
  Croswell and Paul W Crouch remain unresolved or ambiguous. Arthur's
  different-identifier Army occupation lead remains private and low confidence.
  Six-digit and W-prefixed source values were preserved literally and were not
  padded or reinterpreted.
- All twenty CIA and Library of Congress adapter searches succeeded. Ten
  Library of Congress candidates were inspected and rejected with item-level
  reasons; the review import was idempotent. CIA returned no candidates.
- Visual checking corrected occupation code 699 in three earlier evidence
  bundles: Herbert G Benshadle, Frank B Bessac and Vincent T Catalano now show
  radio/phonograph manufacturing rather than electrical-machinery
  manufacturing. Stable claim identifiers were retained and no duplicate
  claims or affiliations were created.

No employer was inferred from an occupation, student affiliation, later
career, namesake, snippet or undated source. Immediate pre-OSS affiliation,
last civilian employer and earlier documented affiliation remain separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,768 | 23,940 | 19.9165% |
| Verified affiliation found | 544 | 23,940 | 2.2723% |
| Verified employer found | 242 | 23,940 | 1.0109% |
| Archival disposition assessed | 4,723 | 23,940 | 19.7285% |
| Not started | 19,172 | 23,940 | 80.0835% |

Published data contains 1,877 affiliations, 587 organizations, 3,228 sources
and 3,764 claims. The private validated database contains 1,889 affiliations,
599 organizations, 4,395 citation rows, 2,008 unique source documents, 3,871
claims and 7,043 research attempts. Claim-confidence totals are 1,132
confirmed, 1,403 high, 1,129 medium, 104 low and 103 conflicting. Ninety-seven
conflicts and 241 possible-duplicate groups remain visible.

Commissioned status is documented for 2,262 active people, documented as not
commissioned for 5,875 and unknown for 15,803. Personnel categories include
2,129 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,188 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,511 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel, and 15,680 unknown or
indeterminate.

Identity-status counts are 958 confirmed, 684 high confidence, 148 probable,
180 ambiguous, 92 conflicting and 21,878 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 135 |
| conflicting_sources | 91 |
| documented_prewar_employer_found | 95 |
| in_progress | 44 |
| needs_identity_review | 230 |
| needs_temporal_review | 17 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,172 |
| occupation_only_found | 866 |
| requires_archival_review | 2,973 |
| verified_employer_found | 227 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  and all 32 parser warnings visually resolved. Page 99 rows 26-35 and the
  supporting code passages were separately rendered and visually checked.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 21/21 Batch 500 checks passed across desktop, phone and
  tablet. The first pass exposed one test-only wording mismatch; the evidence
  and application were already correct.
- Core browser QA: 24/24 bounded search, filter, direct-route, citation,
  organization, analysis and download checks passed across three viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Astro: 124 source files checked with zero errors, warnings or hints.
- Production build: 24,535 HTML pages and 24,607 artifacts.
- Link audit: all 24,535 internal HTML pages resolve; 49,845 unique external
  URLs were inventoried. All five Batch 500 citation destinations returned
  HTTP 200 to the generic checker.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,097 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,607 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `79d5df750455f2068bc6cda1260992746b7a923e3b0a1776f96317c3a5a9419c`.
  The 24,607-file production-tree digest is
  `16376a4697f8681cb59beb4f7542ae44991b5e50c215b33eab72d7c195f319b2`.
  The 67-file public manifest covers 90,404,647 bytes and has SHA-256
  `7f0176e6488c235ac26b685a2916347cf14e5b22ca68c8a2bd6bf2faf5aa298a`.

The accumulated historical browser matrix contains 3,021 cases after adding
Batch 500. A diagnostic run reached 88 passing cases before it was deliberately
stopped; the interrupted 89th case was not an assertion failure. Earlier full
discovery exhausted Node's default 4 GB heap. The new cohort, bounded core and
accessibility subsets were each completed. The full-matrix run remains
documented QA debt rather than a hidden success claim.

## Resume commands

From the repository root, Batch 500 can be reproduced and checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch500.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-nine-paul-l-crosby-through-paul-w-crouch-pathways_batch-500_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
npm --prefix site run build
```

Research resumes with Sherman J Crough, PDF page 99 row 36, followed by the
next nine immutable source rows.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research goal
remains active because 19,172 person entities have not yet started the research
protocol.
