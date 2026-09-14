# Batch 518 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 518 preserves and researches personnel-index PDF page 103 rows 22-31,
Dorothy J Dahl through Richard J Daigle Jr., crossing from Box 163 to Box 164
at archival location 230/86/29/05. The complete index page, relevant Army
occupation-code pages and the pertinent OSS Assessment Staff page were rendered
and visually inspected.

- A 1948 OSS Assessment Staff publication explicitly identifies Duke
  University as Bingham Dai's institution immediately before government
  service. Institutional and scholarly sources establish his Duke teaching
  work and preserve Peking Union Medical College as separate earlier prewar
  employment.
- Exact private-identifier evidence confirms Bruce T Dahlberg and Larry A
  Dahlquist as enlisted Army personnel. Their Army-entry values support only
  qualified student and construction-occupation findings; no school or employer
  is inferred.
- Exact identifier evidence confirms Richard J Daigle Jr. A specialist
  NARA-derived roster corroborates his OSS Greek Group VI context, but his Army
  row is dated February 1946 and is deliberately excluded from pre-OSS
  employment fields.
- Dorothy J Dahl, George N Dahl, Nils Dahl, Alma A Dahlgren, Robert N Dahlgren
  and Marion H Daigle remain unresolved after the recorded protocol and are
  directed to their indexed boxes.

Ten bounded CIA Reading Room checks and ten current Library of Congress checks
returned no candidates or errors. The complete 9,200,232-row Army merged file
was scanned transiently. No authenticated NARA Catalog API request was made.

The reviewed bundle contains eight sources, two canonical organization
upserts, four affiliations, nine claims, twenty-eight claim-source links, ten
person updates and ten synthesized terminal research outcomes. A repeat import
produced no duplicate evidence rows.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,947 | 23,940 | 20.6642% |
| Verified affiliation found | 565 | 23,940 | 2.3601% |
| Verified employer found | 252 | 23,940 | 1.0526% |
| Archival disposition assessed | 4,902 | 23,940 | 20.4762% |
| Not started | 18,993 | 23,940 | 79.3358% |

Published data contains 1,965 affiliations, 611 organizations, 3,349 sources
and 3,907 claims. The private validated database contains 1,977 affiliations,
623 organizations, 4,523 citation records, 2,058 unique source documents,
4,073 claims, 7,611 research attempts and 9,642 claim-source links. Claim-
confidence totals are 1,170 confirmed, 1,449 high, 1,184 medium, 163 low and
107 conflicting. Ninety-nine conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,270 active people, documented as not
commissioned for 5,923 and unknown for 15,747. Personnel categories include
2,137 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,230 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,513 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,627 unknown or
indeterminate.

Active identity-status counts are 1,004 confirmed, 699 high confidence, 155
probable, 214 ambiguous, 94 conflicting and 21,774 unresolved.

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
| not_started | 18,993 |
| occupation_only_found | 898 |
| requires_archival_review | 3,056 |
| verified_employer_found | 237 |

## Validation

- PDF ingest audit remains 522/522 pages processed and 23,978/23,978 rows
  linked. All 32 parser-warning rows are visually resolved, and all 92 selected
  pages are reviewed. The cohort page and three supporting source pages received
  separate visual checks.
- The strict evidence bundle imports idempotently.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 48/48 Batch 518 checks passed across desktop, phone and
  tablet. Bounded core browser QA passed 18/18; analysis browser QA passed 6/6
  across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.6 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 141 source files with zero errors, warnings or hints and built
  24,559 HTML pages / 24,631 artifacts.
- Link audit: all 24,559 internal HTML pages resolve; 49,914 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,098 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size boundary matches across 24,631 artifacts. The five complete
  private values printed in this cohort occur in neither the evidence bundle
  nor the public projection.
- Credential audit found no local `.env` file and no populated literal
  `NARA_API_KEY` assignment outside excluded database, build and dependency
  trees.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. Under the
  documented relative-path/content digest, the 70-file public tree covers
  94,213,970 bytes at SHA-256
  `a9a9b667861636714bd6407d182bb405e51f51ebadd5a95bb0e9d47609f64776`;
  the 24,631-file production tree covers 282,249,202 bytes at SHA-256
  `eee19fd41e46c911b7d58e6da27fd300bc7e1337da5cd558379b22babfc23de2`.
  The 67-file public manifest covers 91,866,826 bytes and has SHA-256
  `f526df6a1a79b926e685da91d470e793ff84327a2a97f080f28907d755f745fb`.

## Resume commands

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-three-dorothy-j-dahl-through-richard-j-daigle-jr-pathways_batch-518_2026-09-14.json
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

Research resumes with page 103 rows 32-41, Rose Daigle through Edward J
Dajewski, in Box 164.

## Release boundary

This local release candidate is validated but not yet pushed or deployed. The
current live release is Batch 517 at immutable content commit
`c268ed2b4c943d1d5e01f4951d97cb425fcb64d0`. Main Test run 34832799936 and
Pages run 34832799986 succeeded, and the verifier matched all 67 manifest
assets, 91,767,883 manifest bytes, seven core routes and ten direct profiles.
The research goal remains active because 18,993 person entities have not yet
started the protocol. The generated entity-resolution report retains its
pre-existing warning that not every possible duplicate group is marked for
manual review; Batch 518 creates no new merge or silent conflation.
