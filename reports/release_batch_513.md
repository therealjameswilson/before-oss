# Batch 513 release report

Run: 2026-09-14 UTC

## Scope and outcomes

Batch 513 preserves and researches personnel-index PDF page 102 rows 18-27,
Joseph T Curtiss through James S Cusick, all in Box 161 at archival location
230/86/29/04. The complete index page and relevant Army occupation-code page
were visually inspected. No rank is printed in the cohort.

- Yale institutional evidence supports Joseph Toy Curtiss at high confidence
  and explicitly identifies his assistant professorship as the role from which
  OSS recruited him.
- An official OSS review report supports Congdon Curts at high confidence and
  establishes his Staff Sergeant Army assignment as the immediate military
  path into OSS; no civilian employer is claimed.
- Bowdoin evidence supports Benjamin H. Cushing Jr. and two prewar librarian
  employers, but does not settle their order. Both remain documented-prewar
  rather than being promoted to immediate or last-civilian status.
- Two institutional sources support Edward Thomas Francis Cushing and preserve
  his Columbia Gramophone work and concurrent bookshop as separate, qualified
  probable-immediate civilian roles.
- Exact private-identifier evidence confirms Ralph H Cushing as enlisted Army
  personnel and supports only the occupation `Foremen, n. e. c.` at Army entry.
- Virginia Cushing remains a probable identity with a qualified wartime mail-
  censorship assignment. James R Cushing Jr. and James S Cusick remain
  ambiguous; Allen I and Lillian E Cushing remain unresolved.
- Ten CIA checks returned no candidates. Ten Library of Congress attempts
  created one wrong-middle-initial candidate, rejected after full-page review
  and replayed idempotently. The complete 9,200,232-row Army file was scanned
  transiently; no-hit outcomes are not negative proof.

The batch adds eleven sources, one net-new organization, eight affiliations,
fifteen claims and thirty claim-source links. Public profiles preserve the
exact index locator, masked private fields, identity uncertainty and archival
next actions.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,898 | 23,940 | 20.4595% |
| Verified affiliation found | 557 | 23,940 | 2.3266% |
| Verified employer found | 248 | 23,940 | 1.0359% |
| Archival disposition assessed | 4,853 | 23,940 | 20.2715% |
| Not started | 19,042 | 23,940 | 79.5405% |

Published data contains 1,937 affiliations, 606 organizations, 3,306 sources
and 3,854 claims. The private validated database contains 1,949 affiliations,
618 organizations, 4,480 citation records, 2,038 unique source documents,
4,020 claims, 7,461 research attempts and 9,487 claim-source links. Claim-
confidence totals are 1,153 confirmed, 1,433 high, 1,167 medium, 163 low and
104 conflicting. Ninety-eight conflicts and 241 possible-duplicate groups
remain visible.

Commissioned status is documented for 2,266 active people, documented as not
commissioned for 5,908 and unknown for 15,766. Personnel categories include
2,133 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,219 enlisted Army personnel, 65 enlisted naval personnel,
seven enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,643 unknown or
indeterminate.

Active identity-status counts are 990 confirmed, 692 high confidence, 154
probable, 209 ambiguous, 93 conflicting and 21,802 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 138 |
| conflicting_sources | 92 |
| documented_prewar_employer_found | 98 |
| in_progress | 44 |
| needs_identity_review | 265 |
| needs_temporal_review | 18 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,042 |
| occupation_only_found | 887 |
| requires_archival_review | 3,033 |
| verified_employer_found | 233 |

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed. The
  cohort page and occupation-code page were separately rendered and inspected.
- The review ledger contains one rejected LoC candidate and replays
  idempotently. The strict evidence bundle imports idempotently as eleven
  sources, five referenced organizations, eight affiliations, fifteen claims,
  thirty claim-source links, ten person updates and ten synthesized outcomes.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed.
- Focused browser QA: 24/24 Batch 513 checks passed across desktop, phone and
  tablet after correcting three test-only ordering or wording assumptions.
- Bounded core browser QA passed 18/18; analysis browser QA passed 6/6 across
  the same viewports.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.6 minutes.
- Stratified profile audit: all seven structural checks passed across 200
  profiles. This is not an independent historical rereview.
- Astro checked 138 source files with zero errors, warnings or hints and built
  24,554 HTML pages / 24,626 artifacts.
- Link audit: all 24,554 internal HTML pages resolve; 49,891 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,112 built-tree candidate substrings produced zero unexpected, aggregate or
  manifest-size matches across 24,626 artifacts. The five complete private
  identifiers printed in this cohort appear neither in the evidence bundle nor
  in the review ledger.
- Credential audit found no local `.env` file and no populated `NARA_API_KEY`
  assignment outside excluded database, build and dependency trees.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `28025070b4f9997ea92e086e4be00d3714dcd27c6ba21cf9d2b92416eb22eab7`;
  the 24,626-file production-tree digest is
  `201922b008fa77fb23e0f76dbaaa097451efcd9cc3f69e0c60677b64d18abd94`.
  The 67-file public manifest covers 91,340,900 bytes and has SHA-256
  `b0234ce9df72691252a79e6327747ed00815d11661f72c365b493456b813fb26`.

## Resume commands

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-14_batch513.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-and-two-joseph-t-curtiss-through-james-s-cusick-pathways_batch-513_2026-09-14.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:release
python3 -m oss_research audit-profiles --sample-size 200
```

Research resumes with page 102 rows 28-37, Arline Custer through Levern W
Cutler, all in Box 161.

## Release boundary

Batch 513 was merged in pull request #205 as commit
`d16ee5c46fbd1cd51725a41ed25b10e3205f3b08`. PR test run 34811500345, main
test run 34811913382 and Pages run 34811913366 succeeded. The deployed verifier
matched all 67 manifest assets (91,340,900 bytes), seven core routes and ten
direct Batch 513 profiles to that commit. No authenticated NARA Catalog API
request was made. The research goal remains active because 19,042 person
entities have not yet started the research protocol. The generated entity-
resolution report retains its pre-existing warning that not every possible
duplicate group is marked for manual review; Batch 513 creates no new duplicate
group, merge or silent conflation.
