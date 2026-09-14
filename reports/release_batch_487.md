# Batch 487 release report

Run: 2026-09-13 UTC

## Scope

Batch 487 preserves and researches ten source rows on personnel-index PDF
page 96, rows 34-43: Jean L Coyat through Lillian E Crabbe. All ten rows are
in Box 151 at archival location 230/86/29/03.

The next unprocessed row is page 96, row 44, Pierre Crabites, Box 151.

## Research outcomes

- Jean L Coyat and Nicholas A Cozzone have exact name-and-private-identifier
  matches in the complete official Army merged-file scan. The records support
  qualified broad occupations at Army entry, but neither names an employer or
  establishes the immediate pre-OSS relationship.
- Hubert E Coyer is a high-confidence commissioned Army officer. An
  institutional military index supplies the officer prefix omitted from the
  OSS row; an official New York report establishes earlier state-guard service;
  and a 1931 Rochester directory establishes qualified, documented-prewar
  teaching employment. The exact Army-to-OSS and last-civilian chronology
  remains an archival question.
- Terence A Coyne is confirmed by a NARA account grounded in his OSS personnel
  file, NAID 2170299. It establishes his immediate pre-OSS assignment at U.S.
  Naval Hospital Great Lakes, his last civilian employer at the U.S. Railway
  Mail Service, and earlier CWA and WPA federal work. The military and civilian
  pathways remain separately modeled.
- William R Coyle, Joseph Coyne, Yves J Cozic, Arthur B Cozzens, James W
  Cozzens and Lillian E Crabbe remain unresolved after the minimum online
  research protocol. Their indexed personnel files are routed for archival
  review.
- Two Library of Congress candidates were reviewed in context and rejected.
  The Arthur Bertrand Cozzens geographer candidate also remains unlinked; no
  postwar occupation was back-projected onto the source row.

No employer was inferred from occupation, education, a postwar record or a
name-only match.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | — | — |
| Research attempted | 4,639 | 23,940 | 19.3776% |
| Verified affiliation found | 532 | 23,940 | 2.2222% |
| Verified employer found | 236 | 23,940 | 0.9858% |
| Archival disposition assessed | 4,594 | 23,940 | 19.1896% |
| Not started | 19,301 | 23,940 | 80.6224% |

Published data now contains 1,818 affiliations, 565 organizations, 3,136
sources, 3,665 claims, 4,302 citations and 1,967 unique source documents.
Claim-confidence totals are 1,111 confirmed, 1,367 high, 1,088 medium, 102
low and 102 conflicting. Ninety-five conflicts and 238 possible-duplicate
groups remain visible.

Terminal and active research-status counts:

| Status | Count |
| --- | ---: |
| candidate_found | 7 |
| completed | 133 |
| conflicting_sources | 89 |
| documented_prewar_employer_found | 91 |
| in_progress | 44 |
| needs_identity_review | 203 |
| needs_temporal_review | 15 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,301 |
| occupation_only_found | 835 |
| requires_archival_review | 2,918 |
| verified_employer_found | 222 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 18/18 checks passed across desktop, phone and tablet.
- Accessibility: 27/27 isolated axe checks passed across the same viewports.
- Astro: 111 source files checked with zero errors, warnings or hints.
- Production build: 24,513 HTML pages and 24,585 artifacts.
- Link audit: all 24,513 internal HTML pages resolve; 49,785 unique external
  URLs were inventoried.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,095 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,585 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Two clean builds were byte-identical. The 70-file public-tree digest is
  `34ae474c421ff66d4dd70060545c93dfa1f7b576942ba99ddace3faef32b41b0`.
  The 24,585-file production-tree digest is
  `302bd8e835709944cc1bf8412af9d76f7d1e3a4346dc19eeaed63c688773daf7`.
  The 67-file public manifest covers 89,391,578 bytes and has digest
  `63ad61689f5a5d7255522ee4985937701b981eddc83ae069178931d6ea7cf895`.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog request was made. The research goal
remains active because 19,301 person entities have not yet started the
research protocol.
