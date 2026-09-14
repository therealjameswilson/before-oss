# Batch 524 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 524 preserves and researches personnel-index PDF page 104 rows 38-46
and page 105 row 1, Beatrice Dancy through Ernest Daniel. The cohort crosses
from Box 165 to Box 166 at archival location 230/86/29/05. Both complete index
pages were rendered and visually inspected.

- Exact private-identifier evidence confirms John Dancy and Dennis V
  Dangerfield as the people recorded entering the United States Army. Both
  records support enlisted Army classification at entry but do not exclude a
  later promotion.
- John Dancy's Army record supports only student status at Army entry. It
  identifies no school, course, degree or employer and does not establish the
  later Army-to-OSS chronology.
- Dennis V Dangerfield's Army record supports only the grouped category
  miners and mining-machine operators at Army entry. It identifies no
  employer, mine, machine, workplace or exact duties and does not establish
  the later Army-to-OSS chronology.
- Gerard N D'Anglure remains externally unresolved. The index's French-captain
  notation supports foreign or Allied commissioned-personnel classification
  but no unit, biography or pre-OSS assignment.
- Beatrice Dancy, Mary E D'Andelet, Clifton Dandridge, Joseph P Dangel,
  Winifred A Dangerfield, Deborah Daniel and Ernest Daniel remain unresolved
  after the completed protocol and require Box 165 or Box 166 review.
- Every profile has a terminal saved outcome, the required no-reliable-
  employer language and explicit archival guidance. No named employer or
  immediate-affiliation claim was created.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks produced seven candidates: three for John
Dancy, one for Deborah Daniel and three for Ernest Daniel. All seven official
OCR contexts and full newspaper pages were reviewed and rejected. The John
Dancy items concerned an older Detroit Urban League namesake or read John
Dance; the Deborah Daniel item supplied a different middle name and no
archival bridge; and the Ernest Daniel items were adjacent-token or column-
break collisions or an uncorroborated common name. The complete 9,200,232-row
Army merged file was scanned transiently. Two strict private-identifier
matches selected one row each. Ernest Daniel's private identifier did not
select a row, so a same-name Army row was not assigned. Army absence was not
treated as negative proof. Three private values were controlled during review
and withheld from the evidence bundle and public artifacts. No authenticated
NARA Catalog API request was made.

The reviewed bundle contains four sources, zero organizations, two qualified
affiliations, four claims, twelve claim-source links, ten person updates and
ten synthesized terminal research outcomes. The seven Library of Congress
decisions and reviewed bundle each import idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,008 | 23,940 | 20.9190% |
| Verified affiliation found | 566 | 23,940 | 2.3642% |
| Verified employer found | 252 | 23,940 | 1.0526% |
| Archival disposition assessed | 4,963 | 23,940 | 20.7310% |
| Not started | 18,932 | 23,940 | 79.0810% |

Published data contains 1,984 affiliations, 613 organizations, 3,375 sources
and 3,946 claims. The private validated database contains 1,996 affiliations,
625 organizations, 4,549 citation records, 2,063 unique source documents,
4,112 claims, 7,798 research attempts and 9,759 claim-source links. Claim-
confidence totals are 1,187 confirmed, 1,452 high, 1,203 medium, 163 low and
107 conflicting. One hundred one conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,272 active people, documented as not
commissioned for 5,939 and unknown for 15,729. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,246 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,513 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,611 unknown or
indeterminate.

Active identity-status counts are 1,021 confirmed, 700 high confidence, 156
probable, 224 ambiguous, 96 conflicting and 21,743 unresolved.

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
| not_started | 18,932 |
| occupation_only_found | 913 |
| requires_archival_review | 3,093 |
| verified_employer_found | 237 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Both cohort pages received separate visual checks.
- The strict evidence bundle and seven Library of Congress review decisions
  import idempotently. All seven candidate rows are durably rejected.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 45/45 Batch 524 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The clean publish tree's Astro check covered 149 source files with zero
  errors, warnings or hints and built 24,561 HTML pages / 24,633 artifacts.
- Link audit: all 24,561 internal HTML pages resolve; 49,920 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,102 built-tree candidate substrings produced zero unexpected boundary,
  aggregate or manifest-size matches across 24,633 artifacts. All three cohort
  private values occur in neither the evidence bundle nor the public
  projection.
- Credential audit found no local `.env` file and no credential file beyond
  the blank `.env.example` template.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Three consecutive Pages builds from the same generated public assets were
  byte-identical. Under the documented relative-path/content digest, the
  70-file public tree covers 94,550,612 bytes at SHA-256
  `f4b4d9cbd221daca596c83b2c2e69c29e111b1cd04d30f1a56ed747a7045256b`;
  the 24,633-file staging production tree covers 282,770,904 bytes at SHA-256
  `a56bedc0915a377677f97ad9cdc293077c3eb7f8bb93f21b4a8b268e2db7e12a`.
  The 67-file public manifest covers 92,203,485 bytes and has SHA-256
  `ec5422224c6a43c81e2121658f0fb8fe32d26d2604dba940927c46782e612f05`.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch524.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-four-beatrice-dancy-through-page-one-hundred-and-five-ernest-daniel-pathways_batch-524_2026-09-14.json
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

Research resumes with page 105 row 2, Geneva L Daniel, in Box 166. Do not
infer an employer from an Army occupation code, student status, namesake,
family relationship or a source describing service after the person had
already joined OSS.

## Release boundary

Batch 524 remains a local release candidate until its exact commit passes the
independent GitHub Test and Pages workflows and the deployed verifier matches
the manifest assets, core routes and direct cohort profiles. The research goal
remains active because 18,932 person entities have not yet started the
protocol.
