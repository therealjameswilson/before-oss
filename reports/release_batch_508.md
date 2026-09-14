# Batch 508 release report

Run: 2026-09-14 UTC

## Scope

Batch 508 preserves and researches personnel-index PDF page 101 rows 14-23,
Ramon C Cunill through Lou Cunningham, all in Box 159 at archival location
230/86/29/04. The index page and Army-file technical documentation were
visually inspected. `Riuth` is confirmed as the printed spelling; `Ruth` is
retained only as a marked search alias.

The next unprocessed sequence is page 101 rows 24-33, Mary Cunningham through
Sanford C Curcie. It crosses from Box 159 to Box 160 at Roy H Cunningham.

## Research outcomes

- Ramon C Cunill, Riuth M Cunniff, Anvilla P Cunningham, Clotilde Cunningham,
  Jane Cunningham, Joan Cunningham and Lou Cunningham remain unresolved with
  critical Box 159 archival-review guidance.
- Harry G Cunningham remains ambiguous. Two incompatible exact-name Army rows,
  a drafting-machine inventor and a wartime-camera designer lack any Box 159,
  service, OSS or second biographical selector. None is assigned.
- Helen M Cunningham remains ambiguous. Two exact-name Women's Army Corps rows
  have different entry dates, grades, residences, birth-year codes and
  occupations. Neither is assigned.
- Hugh T Cunningham remains ambiguous. The one exact-name Army row has an
  identifier different from the private index value. Two official postwar CIA
  documents name a Hugh Cunningham but do not connect that official to the
  middle initial, index value, Box 159 or wartime OSS service.
- Ten CIA checks returned no candidates. Ten Library of Congress checks
  produced five candidates; full-page official OCR showed two different Harry
  middle names, a Mary Jane rather than Jane identity, and two postwar Joan
  references. All five rejections are durable and idempotent.
- The complete 9,200,232-row Army merged file was scanned transiently. The
  seven no-name-hit outcomes are not treated as negative proof because the file
  is neither complete nor an OSS, officer, Navy, civilian or foreign roster.

The batch adds no organization or affiliation. Ten low-confidence identity
claims remain private and withheld from publication. Public profiles present
the exact source row, masked private value where applicable, uncertainty,
research status and archival next action without inventing an employer.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,848 | 23,940 | 20.2506% |
| Verified affiliation found | 553 | 23,940 | 2.3099% |
| Verified employer found | 246 | 23,940 | 1.0276% |
| Archival disposition assessed | 4,803 | 23,940 | 20.0627% |
| Not started | 19,092 | 23,940 | 79.7494% |

Published data contains 1,919 affiliations, 603 organizations, 3,275 sources
and 3,816 claims. The private validated database contains 1,931 affiliations,
615 organizations, 4,449 citation records, 2,031 unique source documents,
3,973 claims, 7,303 research attempts and 9,374 claim-source links. Claim-
confidence totals are 1,142 confirmed, 1,422 high, 1,151 medium, 154 low and
104 conflicting. Ninety-eight conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,264 active people, documented as not
commissioned for 5,896 and unknown for 15,780. Personnel categories include
2,131 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,208 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,657 unknown or
indeterminate.

Identity-status counts are 979 confirmed, 687 high confidence, 151 probable,
199 ambiguous, 93 conflicting and 21,831 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 138 |
| conflicting_sources | 92 |
| documented_prewar_employer_found | 97 |
| in_progress | 44 |
| needs_identity_review | 251 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,092 |
| occupation_only_found | 879 |
| requires_archival_review | 3,008 |
| verified_employer_found | 231 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed. The
  cohort index page was separately inspected for row order and spelling.
- The review ledger contains five rejected LoC candidates and replays
  idempotently. The evidence bundle validates under the strict Pydantic schema
  and imports idempotently as three sources, zero organizations, zero
  affiliations, ten claims, ten person updates and ten synthesized research
  outcomes.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 15/15 Batch 508 checks passed across desktop, phone and
  tablet. Two initial test-only capitalization or label mismatches were fixed;
  evidence and rendered behavior did not change.
- Bounded core browser QA: 54/54 selected search, officer-filter, direct-route,
  citation, organization, analysis and download checks passed across three
  viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.8 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 132 source files with zero errors, warnings or hints and built
  24,551 HTML pages / 24,623 artifacts.
- Link audit: all 24,551 internal HTML pages resolve; 49,881 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,100 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size matches across 24,623 artifacts. The evidence bundle and
  review ledger contain no raw strict private identifiers.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `4c3708e04241c054d397333f2644e9f8cd6da22599a37bf1426dcd934a1d5ab2`;
  the 24,623-file production-tree digest is
  `dbc38fcb21ae74a8c65c29ca909c06fd332d8fc496af0c02ded7ed5239a2a0bf`.
  The 67-file public manifest covers 91,024,032 bytes and has SHA-256
  `1b1be2d71bdfcd5967a7596729eb15fdb5a89af2cc2ef5fe847a577604bde860`.

## Resume commands

From the repository root, Batch 508 can be reproduced and checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch508.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-one-ramon-cunill-through-lou-cunningham-pathways_batch-508_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch508.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
```

Research resumes with page 101 rows 24-33, Mary Cunningham through Sanford C
Curcie, crossing from Box 159 to Box 160.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research
goal remains active because 19,092 person entities have not yet started the
research protocol. The generated entity-resolution report retains its
pre-existing warning that not every possible duplicate group is marked for
manual review; Batch 508 creates no new duplicate group, merge or silent
conflation.
