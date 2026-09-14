# Batch 512 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 512 preserves and researches personnel-index PDF page 102 rows 8-17,
Joseph T Curtis through John S Curtiss, all in Box 161 at archival location
230/86/29/04. The complete index page and relevant Army occupation-code page
were visually inspected. No rank is printed in the cohort.

- Exact private-identifier evidence confirms Leslie S Curtis and Reid H
  Curtis as enlisted Army personnel. Leslie's Army record adds `Jr` and leaves
  occupation value 993 uninterpreted. Reid's code 992 is published only as
  qualified `Student` status at Army entry, not employment or a named school.
- An official Marine Corps history supports a probable Thomas L Curtis
  identity and explicitly sequences his Quantico Reconnaissance Section
  assignment before transfer into OSS paramilitary training. The military
  pathway is published at medium confidence and remains excluded from default
  analytics pending Box 161.
- A 1949 newspaper directly identifies Duke historian John S Curtiss with
  wartime OSS Russian analysis; an independent May 1942 report places John
  Shelton Curtiss on leave from an assistant-archivist post at the Franklin D.
  Roosevelt Library. The probable identity and last-civilian-employer claim
  are visibly qualified at medium confidence.
- Paul M Curtis and Richard R Curtis remain ambiguous. Four other identities
  remain unresolved. No name-only Army row, wrong-initial newspaper result or
  OCR collision is silently assigned.
- Ten CIA checks returned no candidates. Ten Library of Congress attempts
  created twelve candidates; all twelve were rejected after full-page review
  and replay idempotently. The complete 9,200,232-row Army file was scanned
  transiently; no-hit outcomes are not negative proof.

The batch adds seven sources, two organizations, three affiliations, seven
claims and eighteen claim-source links. Public profiles preserve the exact
index locator, masked private fields, identity uncertainty and archival next
actions.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,888 | 23,940 | 20.4177% |
| Verified affiliation found | 554 | 23,940 | 2.3141% |
| Verified employer found | 246 | 23,940 | 1.0276% |
| Archival disposition assessed | 4,843 | 23,940 | 20.2297% |
| Not started | 19,052 | 23,940 | 79.5823% |

Published data contains 1,929 affiliations, 605 organizations, 3,295 sources
and 3,839 claims. The private validated database contains 1,941 affiliations,
617 organizations, 4,469 citation records, 2,033 unique source documents,
4,005 claims, 7,431 research attempts and 9,457 claim-source links. Claim-
confidence totals are 1,152 confirmed, 1,424 high, 1,162 medium, 163 low and
104 conflicting. Ninety-eight conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,265 active people, documented as not
commissioned for 5,906 and unknown for 15,769. Personnel categories include
2,132 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,217 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,646 unknown or
indeterminate.

Active identity-status counts are 989 confirmed, 688 high confidence, 153
probable, 207 ambiguous, 93 conflicting and 21,810 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 138 |
| conflicting_sources | 92 |
| documented_prewar_employer_found | 97 |
| in_progress | 44 |
| needs_identity_review | 262 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,052 |
| occupation_only_found | 886 |
| requires_archival_review | 3,030 |
| verified_employer_found | 231 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed. The
  cohort page and occupation-code page were separately rendered and inspected.
- The review ledger contains twelve rejected LoC candidates and replays
  idempotently. The strict evidence bundle imports idempotently as seven
  sources, two organizations, three affiliations, seven claims, eighteen
  claim-source links, ten person updates and ten synthesized outcomes.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Focused browser QA passes 15/15 Batch 512 checks across desktop, phone and
  tablet.
- Python: 94/94 unit tests passed.
- Focused browser QA: 15/15 Batch 512 checks passed across desktop, phone and
  tablet.
- Bounded core browser QA: 18/18 search, filter, route, citation and downloads
  checks passed; analysis browser QA passed 6/6 across the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.9 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 137 source files with zero errors, warnings or hints and built
  24,553 HTML pages / 24,625 artifacts.
- Link audit: all 24,553 internal HTML pages resolve; 49,885 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,101 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size matches across 24,625 artifacts. The four complete private
  identifiers printed in this cohort appear neither in the evidence bundle nor
  in the review ledger.
- Credential audit found no local `.env` file and no populated `NARA_API_KEY`
  assignment outside excluded database, build and dependency trees.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `905527355ae25e94c3bf8a89f932577a8b805ce0ba6a5b3b68a117e329fb59bb`;
  the 24,625-file production-tree digest is
  `7734a116e74c9874a3a6194016d19ca1132190f19b127e2d6f0197b81941941c`.
  The 67-file public manifest covers 91,221,402 bytes and has SHA-256
  `8b794b4a1fb526fa5f1dd2f089cf3fc130103cb4187b689def44b4dffb65bc6d`.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch512.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-two-joseph-t-curtis-through-john-s-curtiss-pathways_batch-512_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch512.spec.ts
python3 -m oss_research audit-profiles --sample-size 200
```

Research resumes with page 102 rows 18-27, Joseph T Curtiss through James S
Cusick, all in Box 161.

## Release boundary

Batch 512 was merged in pull request #203 as commit
`df7ec8e690aaa680d7e67acc0adc4cb0efd43453`. PR test run 34808180867, main test
run 34808571853 and Pages run 34808571838 succeeded. The deployed verifier
matched all 67 manifest assets (91,221,402 bytes), seven core routes and ten
direct Batch 512 profiles to that commit. No authenticated NARA Catalog API
request was made. The research goal remains active because 19,052 person
entities have not yet started the research protocol. The generated entity-
resolution report retains its pre-existing warning that not every possible
duplicate group is marked for manual review; Batch 512 creates no new duplicate
group, merge or silent conflation.
