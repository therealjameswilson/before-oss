# Batch 498 release report

Run: 2026-09-13 UTC

## Scope

Batch 498 preserves and researches ten source rows on personnel-index PDF page
99, rows 6-15, Raymond A Cromley through Claire F Crook, in Box 155 at archival
location 230/86/29/04.

The next unprocessed row is page 99, row 16, Compton N Crook.

## Research outcomes

- Raymond A Cromley is a high-confidence identity match and commissioned Army
  officer. The best-supported last civilian employer before detention and Army
  service is the Wall Street Journal, where he was a Tokyo correspondent. The
  Japan Advertiser is preserved as an earlier documented employer. Because Army
  service intervened, neither is labeled his immediate pre-OSS affiliation.
- Doris D Cromwell is a high-confidence identity match based on exact name
  components and mutually corroborating contemporary and institutional sources.
  A contemporary newspaper documents full-time employment with United Seamen's
  Service in June 1944 at one dollar per year. That employment is published at
  medium confidence with uncertain temporal relation to OSS service, not as an
  immediate affiliation. Her Duke Endowment trusteeship is separately modeled
  as a professional affiliation, not employment, with the source's date
  discrepancy retained.
- Howard L Cromwell, John L Cronkrite and Joseph J Crooch have confirmed
  index-to-Army identities based on exact private identifiers and are classified
  as enlisted Army personnel. Their qualified Army-entry occupations are,
  respectively, technicians except laboratory; managers and officials not
  elsewhere classified; and welders and flame cutters. None names an employer.
- Dorothea Cronin is a high-confidence identity match to a federal court opinion
  that explicitly identifies her as a former OSS employee. No reliable pre-OSS
  employer was established.
- Frederick Cromwell, William H Cronin Jr. and Claire F Crook remain unresolved.
  Edward R Cronin remains ambiguous after two exact-name Army candidates were
  rejected; his commissioned status remains unknown. Unfamiliar and short source
  identifier values were preserved without padding or reinterpretation.
- All twenty CIA and Library of Congress adapter searches succeeded. Six Library
  of Congress candidates were reviewed; one was accepted for Doris D Cromwell
  and five were rejected with reasons. CIA returned no candidates.

No employer was inferred from an occupation code, later career, namesake,
search-result snippet, modern institutional relationship or source that could
not establish the relevant chronology. Immediate pre-OSS affiliation, last
civilian employer and earlier documented employment remain separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,748 | 23,940 | 19.8329% |
| Verified affiliation found | 543 | 23,940 | 2.2682% |
| Verified employer found | 242 | 23,940 | 1.0109% |
| Archival disposition assessed | 4,703 | 23,940 | 19.6449% |
| Not started | 19,192 | 23,940 | 80.1671% |

Published data now contains 1,866 affiliations, 582 organizations, 3,213
sources and 3,747 claims. The private validated database contains 1,877
affiliations, 594 organizations, 4,380 citations and 2,001 unique source
documents. Claim-confidence totals are 1,130 confirmed, 1,397 high, 1,120
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
| needs_identity_review | 226 |
| needs_temporal_review | 17 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,192 |
| occupation_only_found | 861 |
| requires_archival_review | 2,964 |
| verified_employer_found | 227 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved.
- SQLite: `quick_check` returns `ok`; foreign-key check returns no rows.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 18/18 Batch 498 checks passed across desktop, phone and
  tablet. Three initial test-only capitalization or label mismatches were
  corrected without changing evidence or site behavior.
- Accessibility: all 27 route-and-viewport axe cases passed in 2.3 minutes.
- Astro: 122 source files checked with zero errors, warnings or hints.
- Production build: 24,530 HTML pages and 24,602 artifacts.
- Link audit: all 24,530 internal HTML pages resolve; 49,834 unique external
  URLs were inventoried. Eight of ten Batch 498 citation endpoints returned
  HTTP 200 to the generic checker. Library of Congress and Justia returned HTTP
  403; their cited material had already been reviewed through permitted access.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,099 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,602 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Two consecutive clean public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `aa0be10e95dfb53390af158f1e8863d8347fc76faa0a688b325e96948b11f68a`.
  The 24,602-file production-tree digest is
  `010e96925401c54911875add7b299f6f4a74dbd264b7c97454558305ca32c516`.
  The 67-file public manifest covers 90,219,358 bytes and has SHA-256
  `7236fa29343d982534ed3e52cf1ace28db606c33fd1bd4889f9b4cb41beb282e`.

## Resume commands

From the repository root, the imported Batch 498 state can be reproduced and
checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch498.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-nine-raymond-a-cromley-through-claire-f-crook-pathways_batch-498_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
npm --prefix site run build
```

Research resumes with Compton N Crook, PDF page 99 row 16, followed by the next
nine immutable source rows.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research goal
remains active because 19,192 person entities have not yet started the research
protocol.
