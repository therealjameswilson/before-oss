# Batch 521 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 521 preserves and researches personnel-index PDF page 104 rows 6-16,
Amando Dalisay through Edward F Daly, spanning Boxes 164-165 at archival
location 230/86/29/05. The complete index page and the pertinent Army
technical-documentation pages were rendered and visually inspected.

- Exact private-identifier evidence confirms John E Dally, Ronald E
  Dalrymple, Robert A Dalton, Dennis D Daly and Edward F Daly as enlisted Army
  personnel. Their Army-entry values support only qualified student, driver,
  residual-construction, lawyers-and-judges and actor findings; no employer or
  later Army-to-OSS chronology is inferred.
- Edward F Daly's T-4 row in Box 165 and corporal row in Box 164 share the
  private identifier and remain separate immutable source records linked to
  one person entity.
- Contemporary Harvard evidence and an official Philippine institutional
  biography support a probable Amando Dalisay identity and documented student
  affiliations at the University of the Philippines and Harvard University.
  Both affiliations remain medium confidence, and neither university is
  represented as an employer or immediate OSS predecessor.
- James W Dallas and Donald D Daly remain ambiguous. Miguel S Dalmau and Earle
  J Daly remain unresolved. All four profiles expose Box 164 archival next
  actions.
- Seven Library of Congress newspaper candidates were rejected after full-
  page and OCR-context review. An exact-name James W Dallas Army row remains
  unassigned because the index supplies no private identifier or other bridge.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks produced the seven rejected candidates.
The complete 9,200,232-row Army merged file was scanned transiently. Seven
printed private values were controlled during review; six unique people have
masked values in the public projection, and five received exact Army-file
matches. No authenticated NARA Catalog API request was made.

The reviewed bundle contains six sources, two organization upserts, seven
affiliations, thirteen claims, thirty-six claim-source links, ten person
updates and ten synthesized terminal research outcomes. A repeat import leaves
all durable counts unchanged.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,977 | 23,940 | 20.7895% |
| Verified affiliation found | 566 | 23,940 | 2.3642% |
| Verified employer found | 252 | 23,940 | 1.0526% |
| Archival disposition assessed | 4,932 | 23,940 | 20.6015% |
| Not started | 18,963 | 23,940 | 79.2105% |

Published data contains 1,980 affiliations, 613 organizations, 3,367 sources
and 3,936 claims. The private validated database contains 1,992 affiliations,
625 organizations, 4,541 citation records, 2,063 unique source documents,
4,102 claims, 7,705 research attempts and 9,729 claim-source links. Claim-
confidence totals are 1,181 confirmed, 1,452 high, 1,199 medium, 163 low and
107 conflicting. Ninety-nine conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,270 active people, documented as not
commissioned for 5,933 and unknown for 15,737. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,240 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,513 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,617 unknown or
indeterminate.

Active identity-status counts are 1,015 confirmed, 700 high confidence, 156
probable, 219 ambiguous, 94 conflicting and 21,756 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 143 |
| conflicting_sources | 93 |
| documented_prewar_employer_found | 99 |
| in_progress | 44 |
| needs_identity_review | 276 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 18,963 |
| occupation_only_found | 909 |
| requires_archival_review | 3,068 |
| verified_employer_found | 237 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. The cohort page and four pertinent Army documentation
  pages received separate visual checks.
- The strict evidence bundle imports idempotently. The seven Library of
  Congress review decisions also import idempotently.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 48/48 Batch 521 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 146 source files with zero errors, warnings or hints and built
  24,561 HTML pages / 24,633 artifacts in the clean publish tree.
- Link audit: all 24,561 internal HTML pages resolve; 49,920 unique external
  URLs were inventoried for separate live checking. All six Batch 521 source
  URLs returned successful HTTP 200 responses.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,102 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size boundary matches across 24,633 artifacts. The seven complete
  private values printed in this cohort occur in neither the evidence bundle
  nor the public projection.
- Credential audit found no local `.env` file and no populated literal
  `NARA_API_KEY` assignment outside excluded database, build and dependency
  trees.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Three consecutive Pages builds from the same generated public assets were
  byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  94,458,264 bytes at SHA-256
  `8860057860afcfbf13d71ec97342c4306d8a1c358f124dd70e78d8345a1dd170`;
  the 24,633-file staging production tree covers 282,626,842 bytes at SHA-256
  `c3b4ffa81a075f81ee811a2c2940cc7303b8eaffd70568d324f8ebddf979c3eb`.
  The 67-file public manifest covers 92,111,132 bytes and has SHA-256
  `7360701f728c9b723657fe5dd5d7989a1fcdfc779eedc4b91e736a85d03ba1ed`.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-four-amando-dalisay-through-edward-f-daly-pathways_batch-521_2026-09-14.json
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

Research resumes with page 104 row 17, George R Daly, in Box 165.

## Release boundary

Pull request #217 was merged as immutable main commit
`53c071bac9afab2d8d4ae081e5253388fed1e2bf`. PR Test run 34847423079, main
Test run 34848185791 and Pages run 34848185806 succeeded. The deployed verifier
matched all 67 manifest assets, 92,111,132 manifest bytes, seven core routes
and ten direct Batch 521 profiles at
<https://therealjameswilson.github.io/before-oss/>. The research goal remains
active because 18,963 person entities had not yet started the protocol at this
release. The generated entity-resolution report retains its pre-existing
warning that not every possible duplicate group is marked for manual review;
Batch 521 creates no new merge or silent conflation.
