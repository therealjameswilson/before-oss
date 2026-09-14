# Batch 529 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 529 preserves and researches personnel-index PDF page 105 rows 42-46
and page 106 rows 1-5, Guy G Darr through Leoni DasMousetis. The ten immutable
rows cross Boxes 167-168 at archival location 230/86/29/05. Both index pages
and the two cited Army occupation-code pages were rendered and visually
inspected.

- Exact private-identifier evidence confirms Guy G Darr, Albert L Dart and
  Harry M Daskam. Their Army-entry occupation categories are post office
  clerks; Managers and officials, n.e.c.; and photographic process
  occupations. These are occupations, not named employers.
- Albert L Dart's Army-entry private/PV3 value and later indexed `S/Sgt` rank
  are both preserved. The project does not infer a promotion sequence.
- Joseph Dasher is a high-confidence match to the military-intelligence
  officer and OSS Polish Section chief also identified as Jozef Daszewski.
  U.S. Army military intelligence is a qualified probable immediate
  affiliation. His 1926-1936 Polish-consulate work is earlier employment, not
  a proven last civilian employer because a later gap remains.
- Samuel Dashiell is a probable match to journalist Samuel Lungren Dashiell.
  A contemporary source documents newspaper-correspondent work in Algiers in
  1941-1942, but the OSS bridge is secondary. The occupation is qualified and
  excluded from default analytics; no employer is inferred.
- Ronald J Darr remains a probable archival-review lead. A specialist
  transcription aligns on exact name and captain rank, but lacks a stable item
  identifier and independent official bridge. Its low-confidence candidate is
  withheld from publication as fact.
- Lucie S Darst, Dilip Das, Sala Dasandra and Leoni DasMousetis remain
  unresolved after the minimum protocol and direct researchers to Box 167.

Ten bounded CIA Reading Room checks and ten current Library of Congress checks
returned no candidates or errors. The complete 9,200,232-row Army merged file
was scanned transiently; three eligible private values produced three strict
matches. Full identifiers and raw Army rows were not retained. No
authenticated NARA Catalog API request was made.

The reviewed bundle contains nine sources, two organizations, six
affiliations, 12 claims, 25 claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports
idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,058 | 23,940 | 21.1278% |
| Verified affiliation found | 569 | 23,940 | 2.3768% |
| Verified employer found | 253 | 23,940 | 1.0568% |
| Archival disposition assessed | 5,013 | 23,940 | 20.9398% |
| Not started | 18,882 | 23,940 | 78.8722% |

Published data contains 2,008 affiliations, 623 organizations, 3,411 sources
and 3,993 claims. The private validated database contains 2,020 affiliations,
635 organizations, 4,586 citation records, 2,082 unique source documents,
4,160 claims, 7,950 research attempts and 9,860 claim-source links. Claim-
confidence totals are 1,199 confirmed, 1,466 high, 1,224 medium, 164 low and
107 conflicting. Ninety-six conflicting identities and 241 possible-duplicate
groups remain visible.

Commissioned status is documented for 2,273 active people, documented as not
commissioned for 5,952 and unknown for 15,715. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,258 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,514 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,598 unknown or
indeterminate.

Active identity-status counts are 1,033 confirmed, 707 high confidence, 160
probable, 237 ambiguous, 96 conflicting and 21,707 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 95 |
| documented_prewar_employer_found | 101 |
| in_progress | 44 |
| needs_identity_review | 284 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 94 |
| not_started | 18,882 |
| occupation_only_found | 927 |
| requires_archival_review | 3,106 |
| verified_employer_found | 238 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Index pages 105-106 and Army code pages 171 and 175
  received separate visual checks.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 95/95 unit tests passed.
- Focused browser QA: 54/54 Batch 529 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The local public-manifest guard verified all 67 listed assets and 92,591,760
  bytes at manifest SHA-256
  `10519180118be822351be0d1d3b2d93d87b39b98512b940be4f17e90b36b4ac3`.
- Astro checked 151 source files with zero errors, warnings or hints and built
  24,571 HTML pages / 24,643 artifacts. All internal links resolve; 49,946
  unique external URLs are inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,103 candidate substrings produced zero unexpected boundary, aggregate or
  manifest-size matches across all 24,643 artifacts.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities. No local
  `.env` or credential file is included in the release tree.
- Three consecutive builds were byte-identical. Under the documented relative-
  path/content digest, the 70-file public tree covers 94,938,895 bytes at
  SHA-256
  `77e84bdb3b3fef03bfc8f1ff16e76967b0819d05c6521b08ae87c663c4aa8f49`;
  the 24,643-file production tree covers 283,386,995 bytes at SHA-256
  `2055a2feaa770d7455190ac0522af8e1162ae27dc6b0ee1b13c2d8c734cd4158`.
- PR Test run 34892869139, main Test run 34893610220 and Pages run
  34893609558 passed. The exact live verifier matched all 67 manifest assets,
  seven core routes and ten direct cohort profiles to the immutable merge
  commit.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-pages-one-hundred-and-five-and-six-guy-g-darr-through-leoni-dasmousetis-pathways_batch-529_2026-09-14.json
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

Research resumes with PDF page 106 rows 6-15: Charles Datcher, Dominick
Dattoma, Joseph A Daudelin, Joseph H Daugherty, Thomas J Daughtry, the
incomplete `Daulne *` row with indexed `Cdt` and truncated `aka Jea` note,
Frances L Dauphin, Joseph H Dauphin, Edmund D'Auriol and May J Dausch. Preserve
the unfamiliar abbreviation and truncated alias without expansion.

## Release boundary

Pull request #225 was merged as commit
`d019620c99e3bfdc766b22eb791677ad524bb070`. PR Test run 34892869139, main
Test run 34893610220 and Pages run 34893609558 succeeded. The live verifier
matched all 67 manifest assets (92,591,760 bytes), seven core routes and ten
direct Batch 529 profiles to that exact commit. Batch 529 is the current
verified public release. The research goal remains active because 18,882
person entities have not yet started the protocol.
