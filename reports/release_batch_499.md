# Batch 499 release report

Run: 2026-09-13 UTC

## Scope

Batch 499 preserves and researches ten source rows on personnel-index PDF page
99, rows 16-25, Compton N Crook through Margaret Crosby, spanning Boxes
155-156 at archival location 230/86/29/04.

The next unprocessed row is page 99, row 26, Paul L Crosby.

## Research outcomes

- Compton N Crook is a high-confidence match to biologist Compton Newby Crook.
  Towson documents earlier work as a national park ranger in Yellowstone and
  later biology teaching. A historical-society biography dates the Towson
  appointment to 1939, while Towson's own retrospective says “in the 1940s.”
  Both pathways are published at medium confidence with the conflict visible;
  neither is labeled immediate pre-OSS or last civilian employer.
- Robert L Croop and Isiah Crosby have confirmed index-to-Army identities based
  on exact private identifiers and are classified as enlisted Army personnel.
  Their qualified Army-entry occupations are, respectively, attendants at
  filling stations or parking lots, and chauffeurs or drivers. Neither code
  names an employer, workplace, vehicle, or immediate OSS sequence. The raw
  `CROSBY ISAIAH TRD` conversion remains explicit, and `TRD` is not interpreted.
- Rene Cros is a high-confidence match to René Cros, whose official French
  military-archive entry indexes a 1940-1944 resistance-network dossier. The
  index's `S/Lt` rank and `French` note support foreign-or-Allied commissioned
  classification. The dossier inventory does not supply a pre-OSS employer.
- Margaret Crosby is a high-confidence match to the archaeologist whom Bryn
  Mawr identifies as an OSS Greek Desk worker. American School of Classical
  Studies records document a 1935-1939 Agora fellowship and her responsibility
  for Section BB. The fellowship is professional affiliation, not employment,
  and is not labeled immediately pre-OSS.
- George Crook remains ambiguous after one name-only Army candidate and five
  unrelated newspaper candidates were rejected. Hazel Cropsey, Caleb P
  Crosby, Cushing M Crosby and Helen P Crosby remain unresolved. Short source
  values were preserved without padding or reinterpretation.
- All twenty CIA and Library of Congress adapter searches succeeded. Five
  Library of Congress candidates were reviewed and rejected with reasons. CIA
  returned no candidates.

No employer was inferred from an occupation code, academic fellowship, later
career, namesake, search-result snippet, modern institutional relationship or
source that could not establish the relevant chronology. Immediate pre-OSS
affiliation, last civilian employer and earlier documented affiliation remain
separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,758 | 23,940 | 19.8747% |
| Verified affiliation found | 544 | 23,940 | 2.2723% |
| Verified employer found | 242 | 23,940 | 1.0109% |
| Archival disposition assessed | 4,713 | 23,940 | 19.6867% |
| Not started | 19,182 | 23,940 | 80.1253% |

Published data now contains 1,871 affiliations, 585 organizations, 3,223
sources and 3,757 claims. The private validated database contains 1,882
affiliations, 597 organizations, 4,390 citations and 2,007 unique source
documents. Claim-confidence totals are 1,132 confirmed, 1,401 high, 1,124
medium, 103 low and 103 conflicting. Ninety-six conflicts and 241 possible-
duplicate groups remain visible.

Commissioned status is documented for 2,262 active people, documented as not
commissioned for 5,871 and remains unknown for 15,807. Personnel categories
include 2,129 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,184 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,511 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel, and 15,684 unknown or
indeterminate.

Identity-status counts are 955 confirmed, 683 high confidence, 148 probable,
178 ambiguous, 92 conflicting and 21,884 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 135 |
| conflicting_sources | 90 |
| documented_prewar_employer_found | 95 |
| in_progress | 44 |
| needs_identity_review | 227 |
| needs_temporal_review | 17 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,182 |
| occupation_only_found | 863 |
| requires_archival_review | 2,970 |
| verified_employer_found | 227 |

## Validation

- PDF ingest audit: 522/522 pages processed, 23,978/23,978 rows linked, and all
  32 parser warnings visually resolved. Page 99 rows 16-25 and each supporting
  archival PDF passage were separately rendered and visually checked.
- SQLite: `quick_check` returns `ok`; foreign-key check returns no rows.
- Python: 94/94 tests passed, including 43 subtests.
- Focused browser QA: 21/21 Batch 499 checks passed across desktop, phone and
  tablet.
- Core browser QA: 24/24 search, filter, direct-route, citation, organization,
  analysis and download checks passed across the three viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.9 minutes.
- Astro: 123 source files checked with zero errors, warnings or hints.
- Production build: 24,533 HTML pages and 24,605 artifacts.
- Link audit: all 24,533 internal HTML pages resolve; 49,842 unique external
  URLs were inventoried. All ten Batch 499 citation endpoints returned HTTP
  200 to the generic checker.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  1,095 candidate substrings and zero unexpected boundary, aggregate or
  manifest-size matches across 24,605 artifacts.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `39233424dbe584f036f7c64af5a47afdd59edeae9dec480d88e39691fc47cfa7`.
  The 24,605-file production-tree digest is
  `b3c8eb02ef0838fda4c0912390af092f506b094d1e70dcf404b61636a7446a00`.
  The 67-file public manifest covers 90,325,499 bytes and has SHA-256
  `3542132ff0f457b9da70709ec0dafa557d4c6c1c0b80ba0793ae968f10e0dff3`.

The accumulated historical browser matrix now contains 3,000 cases. Its
default local run exhausted Node's 4 GB heap during discovery. A 12 GB rerun
passed 122 cases without an assertion failure before being deliberately
stopped; it was not reported as a complete pass. The new cohort, core-site and
accessibility subsets above were each completed. This remaining full-matrix
run is documented QA debt rather than a hidden success claim.

## Resume commands

From the repository root, the imported Batch 499 state can be reproduced and
checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch499.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-nine-compton-n-crook-through-margaret-crosby-pathways_batch-499_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
npm --prefix site run build
```

Research resumes with Paul L Crosby, PDF page 99 row 26, followed by the next
nine immutable source rows.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research goal
remains active because 19,182 person entities have not yet started the research
protocol.
