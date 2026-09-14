# Batch 517 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 517 preserves and researches personnel-index PDF page 103 rows 12-21,
William C Dabney through Clarence Dahl, all in Box 163 at archival location
230/86/29/05. The complete index page and the relevant Army occupation-code
pages were rendered and visually inspected.

- Institutional and official military sources support a high-confidence match
  between the index row and the Kentucky aviator William C. Dabney. Colorado
  College is published as a documented prewar student affiliation, not an
  employer or necessarily the immediate predecessor to OSS.
- A contemporary OSS report and official House history confirm Captain Emilio
  Q. Daddario. The House biography and Wesleyan finding aid establish his
  individual Middletown law practice as his strongly date-bounded last civilian
  work. Because no firm is named, it is modeled as self-employment.
- Daddario's Army-to-OSS pathway is explicit, but official and institutional
  sources give February 1943 while a compatible distinctive Army row encodes
  29 April 1943. The conflict is published as such and excluded from default
  analytics pending review of Box 163 and the original enlistment card.
- Exact private-identifier evidence confirms Joseph Dagan and Ralph C Dahdah.
  Exact identifier plus transparent apostrophe normalization confirms Arthur T
  D'Agostino. Their Army-entry records support only qualified occupation
  categories: salesman to consumers, cook except private family, and
  stenographer or typist. No employer or workplace is inferred.
- Marcelino H DaCosta, Theodore A Dada, Malcolm D Daggett, Stuart Daggett and
  Clarence Dahl remain unresolved after the recorded protocol. Famous or
  prominent namesakes without an OSS or Box 163 bridge were rejected.

Ten bounded CIA Reading Room checks returned no candidates or errors. Ten
current Library of Congress checks produced two candidates for William C
Dabney; both were rejected after full-page image review because they name
different people. The complete 9,200,232-row Army merged file was scanned
transiently. No authenticated NARA Catalog API request was made.

The reviewed bundle contains nine source records, three canonical organization
upserts, six affiliations, eleven claims, thirty-four claim-source links, ten
person updates and ten synthesized terminal research outcomes. A repeat import
produced no duplicate evidence rows; the two newspaper decisions also replay
without duplicate decisions.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,937 | 23,940 | 20.6224% |
| Verified affiliation found | 564 | 23,940 | 2.3559% |
| Verified employer found | 251 | 23,940 | 1.0485% |
| Archival disposition assessed | 4,892 | 23,940 | 20.4344% |
| Not started | 19,003 | 23,940 | 79.3776% |

Published data contains 1,961 affiliations, 610 organizations, 3,341 sources
and 3,898 claims. The private validated database contains 1,973 affiliations,
622 organizations, 4,515 citation records, 2,054 unique source documents,
4,064 claims, 7,581 research attempts and 9,614 claim-source links. Claim-
confidence totals are 1,164 confirmed, 1,448 high, 1,182 medium, 163 low and
107 conflicting. Ninety-nine conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,270 active people, documented as not
commissioned for 5,919 and unknown for 15,751. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,227 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,631 unknown or
indeterminate.

Active identity-status counts are 1,000 confirmed, 699 high confidence, 155
probable, 214 ambiguous, 94 conflicting and 21,778 unresolved.

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
| not_started | 19,003 |
| occupation_only_found | 896 |
| requires_archival_review | 3,049 |
| verified_employer_found | 236 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. The cohort page and supporting Army code pages received
  separate visual checks.
- The strict evidence bundle and the two Library of Congress rejection
  decisions import idempotently.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 48/48 Batch 517 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.6 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 142 source files with zero errors, warnings or hints and built
  24,558 HTML pages / 24,630 artifacts.
- Link audit: all 24,558 internal HTML pages resolve; 49,909 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,103 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size boundary matches across 24,630 artifacts. The five complete
  private values printed in this cohort appear neither in the evidence bundle
  nor in the public projection.
- Credential audit found no local `.env` file and no populated literal
  `NARA_API_KEY` assignment outside excluded database, build and dependency
  trees.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  94,115,015 bytes at SHA-256
  `40471f1be6b358201e9782849beb1a666d80a8a7438291e2fcf728b79d54cfec`;
  the 24,630-file production tree covers 282,099,265 bytes at SHA-256
  `a47f6038a06b7bbf250a96e141ee9cfd35dca0696bc1b83ae6dcbaceebfdbf4c`.
  The 67-file public manifest covers 91,767,883 bytes and has SHA-256
  `1539477854d9ead37c4811635ece7dbc0ad96d8740ec408f68589c7f50df99aa`.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-three-william-c-dabney-through-clarence-dahl-pathways_batch-517_2026-09-14.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch517.csv
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

Research resumes with page 103 rows 22-31, Dorothy J Dahl through Richard J
Daigle Jr., crossing from Box 163 to Box 164.

## Release boundary

This local release candidate is validated but not yet pushed or deployed. The
current live release is Batch 516 at immutable content commit
`a013b9372469b8029c75256c4434342413915202`, followed by release-proof commit
`b18dee2a8d50546c6c2251fef3e6a811caeeca1b`. Main Test and Pages runs
34829078975 and 34829078981 succeeded, and the verifier matched all 67 manifest
assets, seven core routes and ten direct profiles. The research goal remains
active because 19,003 person entities have not yet started the protocol. The
generated entity-resolution report retains its pre-existing warning that not
every possible duplicate group is marked for manual review; Batch 517 creates
no new merge or silent conflation.
