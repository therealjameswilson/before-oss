# Batch 523 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 523 preserves and researches personnel-index PDF page 104 rows 27-28
and 30-37, James F D'Amico through Joseph C Dance. All ten printed rows are in
Box 165 at archival location 230/86/29/05. Row 29 was completed in Batch 522
and was not counted again. The complete index page was rendered and visually
inspected.

- Exact private-identifier evidence confirms James F D'Amico, Jerry M
  D'Amico, Donald M Dana and Joseph C Dance as the people recorded entering
  the United States Army. The two D'Amico rows document the Army file's omitted
  apostrophe rather than silently treating the punctuation as identical.
- The Army records support a qualified semiskilled metal-products-fabrication
  occupation group for James F D'Amico and a qualified stenographer-or-typist
  group for Joseph C Dance at Army entry. Neither is a named employer, an exact
  role, or a demonstrated immediate predecessor to OSS service.
- Jerry M D'Amico's occupation value 999 and Donald M Dana's value 253 remain
  deliberately uninterpreted. Identity and Army entry are published; no
  affiliation is manufactured from the residual values.
- Henri C Damon remains externally unresolved. The index's French
  lieutenant-colonel notation supports foreign or Allied commissioned-
  personnel classification but no unit, biography, or pre-OSS assignment.
- Jean Damming, Gerald V D'Amore, Norma Damuth, John J Danahay and Alice M
  Danaher remain unresolved. John J Danahay's seven-digit printed private
  value is preserved privately and was neither padded nor submitted as a
  standard eight-digit Army identifier.
- Every profile has a terminal saved outcome, the required no-reliable-
  employer language and explicit Box 165 archival guidance. No employer or
  immediate-affiliation claim was created.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks produced six candidates for Donald M Dana
and Joseph C Dance. All six official OCR contexts were reviewed and rejected
for a middle-initial mismatch, token collision, other-person context, or an
event phrase rather than a person. The complete 9,200,232-row Army merged file
was scanned transiently. Four strict private-identifier matches selected one
row each; Donald M Dana and Joseph C Dance also each had one exact-name row.
Army absence was not treated as negative proof. Five private values were
controlled during review and withheld from the evidence bundle and public
artifacts. No authenticated NARA Catalog API request was made.

The reviewed bundle contains four sources, zero organizations, two qualified
occupation affiliations, six claims, eighteen claim-source links, ten person
updates and ten synthesized terminal research outcomes. The six Library of
Congress decisions and reviewed bundle each import idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,998 | 23,940 | 20.8772% |
| Verified affiliation found | 566 | 23,940 | 2.3642% |
| Verified employer found | 252 | 23,940 | 1.0526% |
| Archival disposition assessed | 4,953 | 23,940 | 20.6892% |
| Not started | 18,942 | 23,940 | 79.1228% |

Published data contains 1,982 affiliations, 613 organizations, 3,371 sources
and 3,942 claims. The private validated database contains 1,994 affiliations,
625 organizations, 4,545 citation records, 2,063 unique source documents,
4,108 claims, 7,768 research attempts and 9,747 claim-source links. Claim-
confidence totals are 1,185 confirmed, 1,452 high, 1,201 medium, 163 low and
107 conflicting. One hundred one conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,271 active people, documented as not
commissioned for 5,937 and unknown for 15,732. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,244 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,513 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,613 unknown or
indeterminate.

Active identity-status counts are 1,019 confirmed, 700 high confidence, 156
probable, 224 ambiguous, 96 conflicting and 21,745 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 95 |
| documented_prewar_employer_found | 99 |
| in_progress | 44 |
| needs_identity_review | 276 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 18,942 |
| occupation_only_found | 911 |
| requires_archival_review | 3,085 |
| verified_employer_found | 237 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. The cohort page received a separate visual check.
- The strict evidence bundle and six Library of Congress review decisions
  import idempotently. All six candidate rows are durably rejected.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 45/45 Batch 523 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The clean publish tree's Astro check covered 148 source files with zero
  errors, warnings or hints and built
  24,561 HTML pages / 24,633 artifacts.
- Link audit: all 24,561 internal HTML pages resolve; 49,920 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,105 built-tree candidate substrings produced zero unexpected boundary or
  manifest-size matches across 24,633 artifacts. Two aggregate-size numeric
  coincidences are reported separately and are not person-level identifiers.
  All five cohort private values occur in neither the evidence bundle nor the
  public projection.
- Credential audit found no local `.env` file and no credential file beyond
  the blank `.env.example` template.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Three consecutive Pages builds from the same generated public assets were
  byte-identical. Under the documented relative-path/content digest, the
  70-file public tree covers 94,515,012 bytes at SHA-256
  `8f6ec23ca4a4464946743a9b8b116e1c583765acffa5aa8f2931eda599d5b2a1`;
  the 24,633-file staging production tree covers 282,716,302 bytes at SHA-256
  `9494e5da0bf65d2dbf43f808206a71bf7e277947ddfe38da9acae33b457855f0`.
  The 67-file public manifest covers 92,167,881 bytes and has SHA-256
  `4624f9d97e2dfc8fe681174623629a506871c31d787b1317716db02c8ea02e5c`.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch523.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-four-james-f-damico-through-joseph-c-dance-pathways_batch-523_2026-09-14.json
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

Research resumes with page 104 row 38, Beatrice Dancy, in Box 165. Do not
infer an employer from an Army occupation code, residual value, student
affiliation, namesake, or a source describing service after the person had
already joined OSS.

## Release boundary

Pull request #219 was merged as immutable main commit
`3405cbe7b4e64b2422e5f36c57aa6c9cf5db8928`. PR Test run 34858254253,
main Test run 34859041025 and Pages run 34859041152 succeeded. The deployed
verifier matched all 67 manifest assets, 92,167,881 manifest bytes, seven core
routes and ten direct Batch 523 profiles at
<https://therealjameswilson.github.io/before-oss/>. The research goal remains
active because 18,942 person entities have not yet started the protocol.
