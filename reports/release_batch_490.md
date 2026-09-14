# Batch 490 release report

Run: 2026-09-13 UTC

## Scope

Batch 490 preserves and researches ten source rows on personnel-index PDF
page 97 rows 18-27: Robert E Cramer through Wallen L Crane. Robert E Cramer is
in Box 151; the remaining nine rows are in Box 152. All are at archival
location 230/86/29/03.

The next unprocessed row is page 97, row 28, Virginia Crate, Box 152.

## Research outcomes

- A Franklin Institute institutional finding aid supports a high-confidence
  match between the indexed Burton Crane and Louis Burton Crane Jr. It
  explicitly documents his New York Times work from 1937 and his wartime OSS
  intelligence post in Kunming. The newspaper is therefore his best-supported
  last civilian employer, with `probable_immediate` temporal basis because the
  source does not state a direct transfer or exact date.
- The same finding aid documents Burton Crane's 1925-1936 financial-editor
  employment at The Japan Advertiser. It remains a separate earlier prewar
  affiliation, not the immediate predecessor. His commissioned status remains
  unknown because neither the index nor the biography supplies a military
  grade.
- Exact full-name and private-identifier Army matches confirm Joseph Crampes,
  Rufus S Crane Jr. and Wallen L Crane as enlisted Army personnel. Their
  official Army-entry categories are respectively cooks except private family,
  actors and actresses, and managers and officials not elsewhere classified.
  Each is qualified as an occupation; none becomes a named employer or a
  proved Army-to-OSS sequence.
- Robert E Cramer, Donald J Crane, Elizabeth J Crane, Gordon Crane, Milton
  Crane and Robert Crane remain unresolved after the minimum online research
  protocol. Their officer status remains unknown and their profiles route the
  open questions to Boxes 151 or 152.
- Gordon Crane's literal seven-digit value was never padded or used as an
  identifier. Name-only Army rows and later or incompatible namesakes remain
  unassigned.
- All ten Library of Congress candidates were reviewed in official OCR
  context and rejected; a repeat import skipped all ten, demonstrating
  idempotency.

No employer was inferred from an occupation code, a name-only record, a later
career or a prominent namesake.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,668 | 23,940 | 19.4987% |
| Verified affiliation found | 534 | 23,940 | 2.2306% |
| Verified employer found | 237 | 23,940 | 0.9900% |
| Archival disposition assessed | 4,623 | 23,940 | 19.3108% |
| Not started | 19,272 | 23,940 | 80.5013% |

Published data now contains 1,828 affiliations, 568 organizations, 3,151
sources and 3,679 claims. The private validated database contains 1,839
affiliations, 580 organizations, 4,317 citations and 1,971 unique source
documents. Claim-confidence totals are 1,113 confirmed, 1,371 high, 1,095
medium, 102 low and 103 conflicting. Ninety-six conflicts and 240 possible-
duplicate groups remain visible.

Terminal and active research-status counts:

| Status | Count |
| --- | ---: |
| candidate_found | 7 |
| completed | 133 |
| conflicting_sources | 90 |
| documented_prewar_employer_found | 91 |
| in_progress | 44 |
| needs_identity_review | 203 |
| needs_temporal_review | 15 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,272 |
| occupation_only_found | 842 |
| requires_archival_review | 2,938 |
| verified_employer_found | 223 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- SQLite: `quick_check` returns `ok`; foreign-key check returns no rows.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 15/15 checks passed across desktop, phone and tablet.
- Complete browser and accessibility matrix: 2,853/2,853 passed in 26.3
  minutes across the same viewports, with retries disabled.
- Astro: 114 source files checked with zero errors, warnings or hints.
- Production build: 24,516 HTML pages and 24,588 artifacts.
- Link audit: all 24,516 internal HTML pages resolve; 49,792 unique external
  URLs were inventoried. All five Batch 490 citation endpoints returned HTTP
  200.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,099 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,588 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Production dependency audit: zero vulnerabilities.
- Two clean builds were byte-identical. The 70-file public-tree digest is
  `bd63ff46c15795294658e0c952069ab353543aefd3cb8cd985df3261c897867c`.
  The 24,588-file production-tree digest is
  `412e17251e8619e7001230a8e4a3240b6f4acfde10b2aaa2e02cbdb92d2d650e`.
  The 67-file public manifest covers 89,553,969 bytes and has SHA-256
  `24d36b6d83b77ce20ea7fed773ef08486e15b4a64c9c677b10777adffe930c08`.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog request was made. The research goal
remains active because 19,272 person entities have not yet started the
research protocol.
