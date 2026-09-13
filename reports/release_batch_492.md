# Batch 492 release report

Run: 2026-09-13 UTC

## Scope

Batch 492 preserves and researches ten source rows across personnel-index PDF
page 97 rows 38-46 and page 98 row 1: Hilary Crawford through James W
Crayhon. The cohort spans Boxes 152 and 153 at archival location
230/86/29/03.

The next unprocessed row is page 98, row 2, Robert N Creadick, Box 153. Its
short printed value must remain literal unless direct evidence resolves it.

## Research outcomes

- Exact full-name and private-identifier Army matches confirm Jack B
  Crawford, John E Crawford Jr. and Samuel J Crawford as enlisted Army
  personnel. Their tool-sharpeners-and-dressers, general-office-clerk and
  carpenter categories are published only as qualified Army-entry
  occupations, never as named employers or proved immediate predecessors.
- William E Crawford's exact identifier confirms identity among 28 same-name
  Army candidates. His selected Army entry is dated 21 November 1945, after
  OSS dissolution, so the record does not support a pre-OSS occupation,
  military assignment or commissioned classification.
- Hilary Crawford, William S Crawford Jr. and Alton O Crawley remain
  ambiguous. Their short or missing identifiers were not padded, and
  unrelated suffix collisions or name-only Army rows were not assigned.
- Ruth E Crawford and Carlotta B Crawley remain unresolved with archival-file
  review required.
- Two independent sources support a probable James W Crayhon identity and a
  medium-confidence 1938 Associated Press photo city assignment editor role.
  Because neither gives middle initial W or links the role to OSS chronology,
  it is visibly qualified as documented prewar, is neither immediate nor last
  civilian, and is excluded from default employer analytics.
- All ten Library of Congress candidates were reviewed in official OCR
  context and rejected; a repeat import skipped all ten, demonstrating
  idempotency.

No employer was inferred from an occupation code, a post-OSS military record,
a short identifier, a name-only candidate, a later career or a prominent
namesake.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,688 | 23,940 | 19.5823% |
| Verified affiliation found | 534 | 23,940 | 2.2306% |
| Verified employer found | 237 | 23,940 | 0.9900% |
| Archival disposition assessed | 4,643 | 23,940 | 19.3943% |
| Not started | 19,252 | 23,940 | 80.4177% |

Published data now contains 1,834 affiliations, 568 organizations, 3,161
sources and 3,688 claims. The private validated database contains 1,845
affiliations, 580 organizations, 4,327 citations and 1,973 unique source
documents. Claim-confidence totals are 1,116 confirmed, 1,371 high, 1,101
medium, 102 low and 103 conflicting. Ninety-six conflicts and 240 possible-
duplicate groups remain visible.

Terminal and active research-status counts:

| Status | Count |
| --- | ---: |
| candidate_found | 7 |
| completed | 133 |
| conflicting_sources | 90 |
| documented_prewar_employer_found | 92 |
| in_progress | 44 |
| needs_identity_review | 210 |
| needs_temporal_review | 16 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,252 |
| occupation_only_found | 847 |
| requires_archival_review | 2,944 |
| verified_employer_found | 223 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- SQLite: `quick_check` returns `ok`; foreign-key check returns no rows.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 18/18 Batch 492 checks passed across desktop, phone and
  tablet.
- Accessibility: the main route run passed 26/27; the one tablet Sources-page
  case timed out without an axe finding and passed 1/1 on an isolated clean
  rerun. All 27 route-and-viewport cases therefore have a passing final result.
- Astro: 116 source files checked with zero errors, warnings or hints.
- Production build: 24,516 HTML pages and 24,588 artifacts.
- Link audit: all 24,516 internal HTML pages resolve; 49,794 unique external
  URLs were inventoried. Five of six Batch 492 citation endpoints returned
  HTTP 200. The stable Columbia handle redirected to a HathiTrust endpoint
  that returned HTTP 403 to the checker; the exact report and cited page were
  separately downloaded from a public mirror, rendered and visually checked.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,100 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,588 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Production dependency audit: zero vulnerabilities.
- Two clean builds were byte-identical. The 70-file public-tree digest is
  `8306774bb888567217a2934b69a3f3f8741ce3cf0d895cbe28c6679cdb91ffca`.
  The 24,588-file production-tree digest is
  `18b371a28ad9a44c1fb2db3e454955957f1bee4b0536ce0dcf2db078432a22a3`.
  The 67-file public manifest covers 89,659,454 bytes and has SHA-256
  `bf475ebc0732866e4b48b1f94c7dc9521ab6013456315d690bee89d1bccf690c`.

## Resume commands

From the repository root, the imported Batch 492 state can be reproduced and
checked with:

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-seven-hilary-crawford-through-page-ninety-eight-james-w-crayhon-pathways_batch-492_2026-09-13.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
npm --prefix site run check
npm --prefix site run build
```

Research resumes with Robert N Creadick, PDF page 98 row 2, followed by the
next nine immutable source rows. The short printed value must be treated as a
literal discovery clue rather than a normalized service number.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research
goal remains active because 19,252 person entities have not yet started the
research protocol.
