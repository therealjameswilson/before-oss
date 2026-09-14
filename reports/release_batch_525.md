# Batch 525 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 525 preserves and researches personnel-index PDF page 105 rows 2-11,
Geneva L Daniel through Edward L Daniels. All ten rows are in Box 166 at
archival location 230/86/29/05. The complete index page was rendered and
visually inspected.

- Exact private-identifier evidence confirms Arlan R Daniels as the person
  recorded entering the United States Army on 5 May 1942. The Army record adds
  a middle initial D and supports enlisted Army classification at entry but
  does not exclude later promotion.
- Arlan Daniels's civilian-occupation value 999 remains uninterpreted. No
  occupation, employer or Army-to-OSS chronology is inferred from it.
- The index records John F Daniel as a major and Edward J Danielewicz as a
  first lieutenant. Those source facts support commissioned Army
  classifications but do not resolve either external identity or establish a
  pre-OSS assignment.
- James B Daniel, John F Daniel, John W Daniel, Margaret Daniel, Robert J
  Daniel, Edward J Danielewicz and Edward L Daniels remain ambiguous after
  candidate review. Geneva L Daniel and Tatianna Daniell remain unresolved.
- Every profile has a terminal saved outcome, the required no-reliable-
  employer language and explicit Box 166 archival guidance. No employer or
  affiliation claim was created.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks produced 24 candidates: five each for
James B Daniel, John F Daniel, John W Daniel and Robert J Daniel, and four for
Margaret Daniel. All 24 official OCR contexts were reviewed and rejected as
token collisions, incompatible initials or surnames, or common-name records
without a private-identifier, OSS or Box 166 bridge. The complete 9,200,232-
row Army merged file was scanned transiently. One strict private-identifier
match selected Arlan Daniels's row. Thirty-seven exact-name Army rows for five
common-name people were not assigned. Army absence was not treated as
negative proof. Five printed private values were controlled during review and
withheld from the evidence bundle and public artifacts. No authenticated NARA
Catalog API request was made.

The reviewed bundle contains three sources, zero organizations or
affiliations, one identity claim, three claim-source links, ten person updates
and ten synthesized terminal research outcomes. The 24 Library of Congress
decisions and reviewed bundle each import idempotently.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 5,018 | 23,940 | 20.9607% |
| Verified affiliation found | 566 | 23,940 | 2.3642% |
| Verified employer found | 252 | 23,940 | 1.0526% |
| Archival disposition assessed | 4,973 | 23,940 | 20.7728% |
| Not started | 18,922 | 23,940 | 79.0393% |

Published data contains 1,984 affiliations, 613 organizations, 3,378 sources
and 3,947 claims. The private validated database contains 1,996 affiliations,
625 organizations, 4,552 citation records, 2,063 unique source documents,
4,113 claims, 7,828 research attempts and 9,762 claim-source links. Claim-
confidence totals are 1,188 confirmed, 1,452 high, 1,203 medium, 163 low and
107 conflicting. One hundred one conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,272 active people, documented as not
commissioned for 5,940 and unknown for 15,728. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,247 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,513 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,610 unknown or
indeterminate.

Active identity-status counts are 1,022 confirmed, 700 high confidence, 156
probable, 231 ambiguous, 96 conflicting and 21,735 unresolved.

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
| not_started | 18,922 |
| occupation_only_found | 913 |
| requires_archival_review | 3,103 |
| verified_employer_found | 237 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. Page 105 received a separate cohort visual check.
- The strict evidence bundle and 24 Library of Congress review decisions
  import idempotently. All 24 candidate rows are durably rejected.
- SQLite `integrity_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 45/45 Batch 525 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.7 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- The clean publish tree's Astro check covered 150 source files with zero
  errors, warnings or hints and built 24,561 HTML pages / 24,633 artifacts.
- Link audit: all 24,561 internal HTML pages resolve; 49,920 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,102 built-tree candidate substrings produced zero unexpected boundary,
  aggregate or manifest-size matches across 24,633 artifacts. All five cohort
  private values occur in neither the evidence bundle nor the public
  projection.
- Credential audit found no local `.env` file and no credential file beyond
  the blank `.env.example` template.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Three consecutive Pages builds from the same generated public assets were
  byte-identical. Under the documented relative-path/content digest, the
  70-file public tree covers 94,568,847 bytes at SHA-256
  `a967ad1b7c095dce4eb3e7b83e519749138750692da4b4b2e4e02d42eca58554`;
  the 24,633-file staging production tree covers 282,798,429 bytes at SHA-256
  `2a1ff56b2d856ec8352fa30dec4c4cb58db06f5db159c1f349dc1e81fd36aebe`.
  The 67-file public manifest covers 92,221,715 bytes and has SHA-256
  `fa58242565764511649adcd32372f9fbeb175fb2fbdf5971f95fab82c1ffaeba`.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch525.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-five-geneva-l-daniel-through-edward-l-daniels-pathways_batch-525_2026-09-14.json
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

Research resumes with page 105 row 12, Elmer Daniels, in Box 166, followed by
Eugene B Daniels, Jack Daniels, William H Daniels, Raymond Danielson, Richard E
Danielson, Serge Daniloff, Serge Daniluck, Albert P Dankwardt and Frank P Dann.
Do not assign common-name Army or newspaper records without corroborating
identifiers, and do not infer an employer from an uninterpreted occupation
code.

## Release boundary

Independent GitHub checks, merge, Pages deployment and deployed-artifact
verification remain pending. The research goal remains active because 18,922
person entities have not yet started the protocol.
