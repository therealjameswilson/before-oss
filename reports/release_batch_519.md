# Batch 519 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 519 preserves and researches personnel-index PDF page 103 rows 32-41,
Rose Daigle through Edward J Dajewski, all in Box 164 at archival location
230/86/29/05. The complete index page, the relevant Army code page and the
pertinent OSS Assessment Staff page were rendered and visually inspected.

- Exact private-identifier evidence confirms Alfred P Daignault and Pat H
  Dailey as enlisted Army personnel. Their Army-entry values support only
  qualified automobile-manufacturing and machinist occupations; no employer,
  plant or later Army-to-OSS chronology is inferred.
- A direct OSS staff publication independently corroborates Alfred P
  Daignault's name and corporal grade. It prints no predecessor institution
  for him, which is preserved as an absence of evidence rather than evidence
  that no employer existed.
- A scholarly history based on OSS records places Lieutenant George Dail in
  the Morale Operations unit in China. Name, grade and direct OSS context make
  the match to indexed 2nd Lt. George E. Dail Jr. high confidence, not
  confirmed, because the source omits his middle initial and suffix. The
  within-OSS assignment is not misrepresented as a pre-OSS affiliation.
- Harvey J Dain retains the commissioned classification printed in the index,
  but a psychiatrist namesake remains unassigned without an OSS or Box 164
  bridge. Six other identities remain unresolved.
- Three Library of Congress newspaper candidates were rejected after
  full-page review: one common-name incident, one impossibly early item and
  one OCR artifact.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks produced the three rejected candidates.
The complete 9,200,232-row Army merged file was scanned transiently. No
authenticated NARA Catalog API request was made.

The reviewed bundle contains six sources, no organization upserts, two
affiliations, five claims, fifteen claim-source links, ten person updates and
ten synthesized terminal research outcomes. A repeat import leaves all durable
counts unchanged.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,957 | 23,940 | 20.7059% |
| Verified affiliation found | 565 | 23,940 | 2.3601% |
| Verified employer found | 252 | 23,940 | 1.0526% |
| Archival disposition assessed | 4,912 | 23,940 | 20.5180% |
| Not started | 18,983 | 23,940 | 79.2941% |

Published data contains 1,967 affiliations, 611 organizations, 3,355 sources
and 3,912 claims. The private validated database contains 1,979 affiliations,
623 organizations, 4,529 citation records, 2,059 unique source documents,
4,078 claims, 7,645 research attempts and 9,657 claim-source links. Claim-
confidence totals are 1,172 confirmed, 1,450 high, 1,186 medium, 163 low and
107 conflicting. Ninety-nine conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,270 active people, documented as not
commissioned for 5,925 and unknown for 15,745. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,232 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,513 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,625 unknown or
indeterminate.

Active identity-status counts are 1,006 confirmed, 700 high confidence, 155
probable, 214 ambiguous, 94 conflicting and 21,771 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 142 |
| conflicting_sources | 93 |
| documented_prewar_employer_found | 99 |
| in_progress | 44 |
| needs_identity_review | 270 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 18,983 |
| occupation_only_found | 900 |
| requires_archival_review | 3,064 |
| verified_employer_found | 237 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. The cohort page, two fixed-width documentation pages,
  one code-list page and one OSS staff-list page received separate visual
  checks.
- The strict evidence bundle imports idempotently. The three Library of
  Congress review decisions also import idempotently.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 51/51 Batch 519 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.6 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 142 source files with zero errors, warnings or hints and built
  24,559 HTML pages / 24,631 artifacts.
- Link audit: all 24,559 internal HTML pages resolve; 49,914 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,100 built-tree candidate substrings produced zero unexpected or aggregate
  boundary matches across 24,631 artifacts. Two exact numeric coincidences in
  manifest `size_bytes` fields were recognized and excluded as expected false
  positives. The four complete private values printed in this cohort occur in
  neither the evidence bundle nor the public projection.
- Credential audit found no local `.env` file and no populated literal
  `NARA_API_KEY` assignment outside excluded database, build and dependency
  trees.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  94,262,650 bytes at SHA-256
  `255de8d5bda709c5d2741c8ba8d815acd8ae0af88c4cc7dd1aa1ba3400a3b13e`;
  the 24,631-file production tree covers 282,321,950 bytes at SHA-256
  `1c5d4b4ab99146b09bf36722876b3124f383f476df8f44b4a5b50f41b7a59c3a`.
  The 67-file public manifest covers 91,915,517 bytes and has SHA-256
  `663b532797dcea1a18f6dde4e7b6c27013c26456e00d9e6ea54adb5e443100f7`.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-three-rose-daigle-through-edward-j-dajewski-pathways_batch-519_2026-09-14.json
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

Research resumes with page 103 row 42, John P Dalberg, in Box 164.

## Release boundary

Pull request #215 was merged as immutable content commit
`424e796932071b601ea03c921c184fea5c02de9b`. Main Test run 34838701167 and
Pages run 34838701188 succeeded. The deployed verifier matched all 67 manifest
assets, 91,915,517 manifest bytes, seven core routes and ten direct Batch 519
profiles at <https://therealjameswilson.github.io/before-oss/>. The research
goal remains active because 18,983 person entities had not yet started the
protocol at this release. The generated entity-resolution report retains its
pre-existing warning that not every possible duplicate group is marked for
manual review; Batch 519 creates no new merge or silent conflation.
