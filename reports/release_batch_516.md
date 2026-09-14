# Batch 516 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 516 preserves and researches personnel-index PDF page 103 rows 2-11,
Edmund Czaplinski through Arnold Daane. Rows 2-10 are in Box 162 and row 11
is in Box 163, all at archival location 230/86/29/05. The complete index page,
the relevant Army occupation-code pages and page 75 of the official 1943 New
York State military report were rendered and visually inspected.

- An archive-based Project Eagle monograph supports high-confidence identities
  and an explicit Polish military pathway for Edmund Czaplinski, Wiktor
  Czarnecki and Jozef Czogowski. The Independent Grenadier Company is modeled
  as a military assignment, not employment; index and book rank variants remain
  visible. Forced German service remains a qualified earlier assignment, and
  Jozef's unnamed factory role is not turned into a named employer.
- Exact private-identifier and name matches confirm John Czebely, Joseph F.
  Czechlewski, Edward J. Czop and Fred C. Czufin. The Army file supports only
  qualified occupation or status categories for John, Edward and Fred; no farm,
  company or school is inferred.
- An official New York State report and two institutional biographical entries
  confirm Joseph F. Czechlewski's identity and support the New York County
  District Attorney's Office as his high-confidence last civilian government
  employer. His earlier private law practice remains separate. The Army-file
  police/detective occupation code conflicts with the lawyer chronology and is
  published as a conflict rather than silently reconciled.
- Stephanie Czech's existing high-confidence Texas Oil Company and WAAC/WAC
  sequence is preserved. A compatible name-only WAC row is not assigned because
  it lacks the index identifier.
- Maryland State Archives documents newspaper publisher Arnold Daane, but the
  name-only Box 163 row supplies no direct OSS bridge. The affiliation is
  published conditionally at medium confidence, excluded from default analytics
  and not labeled immediate or last civilian.
- William S. Czyzewski remains unresolved after the recorded protocol. The
  incomplete Army file's non-hit is not negative proof, and the profile directs
  researchers to Box 162.

Ten bounded CIA Reading Room checks and ten current Library of Congress checks
returned no candidates or errors. The complete 9,200,232-row Army merged file
was scanned transiently. No authenticated NARA Catalog API request was made.

The reviewed bundle adds eleven source records, two net-new organizations plus
two canonical organization upserts, thirteen affiliations, twenty-two claims,
fifty-seven claim-source links, ten person updates and ten synthesized terminal
research outcomes. A repeat import produced no duplicate evidence rows.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,927 | 23,940 | 20.5806% |
| Verified affiliation found | 562 | 23,940 | 2.3475% |
| Verified employer found | 250 | 23,940 | 1.0443% |
| Archival disposition assessed | 4,882 | 23,940 | 20.3926% |
| Not started | 19,013 | 23,940 | 79.4194% |

Published data contains 1,955 affiliations, 610 organizations, 3,332 sources
and 3,887 claims. The private validated database contains 1,967 affiliations,
622 organizations, 4,506 citation records, 2,049 unique source documents,
4,053 claims, 7,551 research attempts and 9,580 claim-source links. Claim-
confidence totals are 1,159 confirmed, 1,446 high, 1,179 medium, 163 low and
106 conflicting. Ninety-nine conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,269 active people, documented as not
commissioned for 5,916 and unknown for 15,755. Personnel categories include
2,136 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,224 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,635 unknown or
indeterminate.

Active identity-status counts are 996 confirmed, 698 high confidence, 155
probable, 214 ambiguous, 94 conflicting and 21,783 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 141 |
| conflicting_sources | 93 |
| documented_prewar_employer_found | 99 |
| in_progress | 44 |
| needs_identity_review | 270 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,013 |
| occupation_only_found | 893 |
| requires_archival_review | 3,044 |
| verified_employer_found | 235 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. The cohort page and supporting Army and New York State
  report pages received separate visual checks.
- The strict evidence bundle imports idempotently as eleven sources, four
  organization upserts, thirteen affiliations, twenty-two claims, fifty-seven
  claim-source links, ten person updates and ten synthesized outcomes.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 21/21 Batch 516 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 141 source files with zero errors, warnings or hints and built
  24,558 HTML pages / 24,630 artifacts.
- Link audit: all 24,558 internal HTML pages resolve; 49,905 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,105 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size boundary matches across 24,630 artifacts. The six complete
  private identifiers printed in this cohort appear neither in the evidence
  bundle nor in the public projection.
- Credential audit found no local `.env` file and no populated `NARA_API_KEY`
  assignment outside excluded database, build and dependency trees.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `9b6f8d99d0e92a76e7b8fcf06f6d0f4b76626f94c2af20003d0fc2fda03bb517`;
  the 24,630-file production-tree digest is
  `1187d90a0f0ef5d9c0a489d34ad274e47b32654cbe169b7684120fa489cb21a0`.
  The 67-file public manifest covers 91,655,994 bytes and has SHA-256
  `7c3f039ad2c8965ad2a4c415d2aceed50d1f52428b7bcfbcbf6854837431da4d`.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-three-edmund-czaplinski-through-arnold-daane-pathways_batch-516_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release
python3 -m oss_research audit-profiles --sample-size 200
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
```

Research resumes with page 103 rows 12-21, William C Dabney through Clarence
Dahl, all in Box 163.

## Release boundary

Batch 516 was merged in pull request #211 as commit
`a013b9372469b8029c75256c4434342413915202`. PR test run 34826996806, main
test run 34827638455 and Pages run 34827638457 succeeded. The deployed verifier
matched all 67 manifest assets (91,655,994 bytes), seven core routes and ten
direct Batch 516 profiles to that commit. No authenticated NARA Catalog API
request was made. The research goal remains active because 19,013 person
entities have not yet started the protocol. The generated entity-resolution
report retains its pre-existing warning that not every possible duplicate
group is marked for manual review; Batch 516 creates no new merge or silent
conflation.
