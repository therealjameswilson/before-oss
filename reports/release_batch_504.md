# Batch 504 release report

Run: 2026-09-13 UTC

## Scope

Batch 504 preserves and researches personnel-index PDF page 100 rows 20-29,
Walter M Cuddy Jr. through Jane Culbertson, crossing from Box 157 to Box 158 at
archival location 230/86/29/04. The source page and the two newly needed Army
occupation-code passages were rendered and visually inspected.

The next unprocessed sequence is page 100 rows 30-39, Ruth B Culbertson through
Carson W Culp, all in Box 158.

## Research outcomes

- Exact private-identifier evidence confirms Walter M Cuddy Jr. and Mario J
  Cugia as enlisted Army personnel. Their official codes support qualified
  printing occupations only; neither source names an employer.
- Frank Cuellar and Rodolfo E Cueva remain ambiguous because their Army
  candidates lack a compatible direct identifier/OSS bridge. John H Cudmore,
  Domingo Cuevas, Saburo Cujow, Frederick C Culbert and Jane Culbertson remain
  unresolved with archival guidance.
- Direct wartime and institutional sources support a high-confidence Frederick
  P Culbert pathway from a U.S. Department of State / Foreign Service vice-
  consul and control-officer assignment into GYMNAST/Western Task Force work.
  Casablanca and Dakar source claims conflict and remain explicit. Earlier
  Navy service and an unnamed business-executive history are separately
  modeled; the latter is not counted as an employer.
- Ten CIA checks returned no candidates. Ten Library of Congress checks
  produced two false candidates; official page context established an
  unrelated probate notice and an OCR token collision. Both rejections are in
  the durable review ledger.

No employer was inferred from an occupation, military assignment, namesake,
snippet or unnamed business history. Immediate pre-OSS affiliation, last
civilian employer and earlier documented affiliation remain separate.

## Exact coverage after import

| Measure | Count | Denominator | Coverage |
| --- | ---: | ---: | ---: |
| Index rows preserved and linked | 23,978 | 23,978 | 100.0000% |
| Active person entities | 23,940 | - | - |
| Research attempted | 4,808 | 23,940 | 20.0835% |
| Verified affiliation found | 548 | 23,940 | 2.2891% |
| Verified employer found | 243 | 23,940 | 1.0150% |
| Archival disposition assessed | 4,763 | 23,940 | 19.8956% |
| Not started | 19,132 | 23,940 | 79.9165% |

Published data contains 1,901 affiliations, 595 organizations, 3,255 sources
and 3,792 claims. The private validated database contains 1,913 affiliations,
607 organizations, 4,425 citation rows, 2,022 unique source documents, 3,919
claims and 7,170 research attempts. Claim-confidence totals are 1,137
confirmed, 1,413 high, 1,142 medium, 124 low and 103 conflicting. Ninety-seven
conflicts and 241 possible-duplicate groups remain visible.

Commissioned status is documented for 2,263 active people, documented as not
commissioned for 5,891 and unknown for 15,786. Personnel categories include
2,130 commissioned Army officers, 88 commissioned naval officers, nine
commissioned Marine Corps officers, one commissioned Coast Guard officer, six
warrant officers, 4,203 enlisted Army personnel, 65 enlisted naval personnel,
six enlisted Marine Corps personnel, 1,512 civilians, 253 foreign or Allied
military personnel, four temporary or special personnel and 15,663 unknown or
indeterminate.

Identity-status counts are 972 confirmed, 686 high confidence, 150 probable,
189 ambiguous, 92 conflicting and 21,851 unresolved.

Research-status counts:

| Status | Count |
| --- | ---: |
| blocked_by_source_access | 1 |
| candidate_found | 7 |
| completed | 137 |
| conflicting_sources | 91 |
| documented_prewar_employer_found | 95 |
| in_progress | 44 |
| needs_identity_review | 241 |
| needs_temporal_review | 17 |
| no_reliable_result_after_protocol | 82 |
| not_started | 19,132 |
| occupation_only_found | 876 |
| requires_archival_review | 2,988 |
| verified_employer_found | 229 |

## Employer-metric correction

The analytics and export logic now count an employment relationship as a
verified employer only when a historical organization is actually named;
self-employment remains countable. Unnamed employment histories stay visible
as public affiliations but no longer inflate employer or sector analytics.
This excludes Culbert's unnamed business history and corrects an older unnamed
Betty A Lussier record. The verified-employer total therefore changes from 244
to 243.

## Validation

- PDF ingest audit remains 522/522 pages processed, 23,978/23,978 rows linked,
  all 32 parser warnings visually resolved and 92 selected pages reviewed.
  Page 100 rows 20-29 and official code-list passages 448 and 849 were
  separately rendered and visually checked.
- SQLite `quick_check` returns `ok`; the foreign-key check returns no rows.
- Python: 94/94 unit tests passed, including the named-employer regression.
- Focused browser QA: 18/18 Batch 504 checks passed across desktop, phone and
  tablet.
- Bounded core browser QA: 42/42 selected search, filter, direct-route,
  citation, organization, analysis and download checks passed across three
  viewports. An accidental full matrix was deliberately stopped after 112
  passes; its interrupted case is not reported as a failure or pass.
- Accessibility: all 27 route-and-viewport axe cases passed in 1.5 minutes.
- Stratified profile audit: all seven checks passed across 200 profiles.
- Astro checked 128 source files with zero errors, warnings or hints and built
  24,543 HTML pages / 24,615 artifacts.
- Link audit: all 24,543 internal HTML pages resolve; 49,863 unique external
  URLs were inventoried for separate live checking.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants and
  1,098 built-tree candidate substrings produced zero unexpected matches
  across 24,615 artifacts. The evidence bundle and review ledger likewise
  contain no raw strict private identifiers.
- Dependencies: `npm audit --omit=dev` reports zero vulnerabilities.
- Two consecutive public-data and Pages builds were byte-identical. The
  70-file public-tree digest is
  `7b6b6f6ddfe665d7fd0ea71ca6f77259955364464cfbacd98270305e94504cc8`;
  the 24,615-file production-tree digest is
  `c1a61393f796c9f5e340c8fb216ad4cac5def02dfd096fe088f1912bfcb47ee2`.
  The 67-file public manifest covers 90,748,730 bytes and has SHA-256
  `8bf27ef5a0707c27439e5330d9da3a73242912c794f72981c9cd6d84dffaddf0`.

## Resume commands

From the repository root, Batch 504 can be reproduced and checked with:

```bash
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-13_batch504.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-one-hundred-walter-cuddy-through-jane-culbertson-pathways_batch-504_2026-09-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m unittest discover -s tests -q
npm --prefix site run build
npm --prefix site run test:e2e -- tests/batch504.spec.ts
```

Research resumes with page 100 rows 30-39, Ruth B Culbertson through Carson W
Culp.

## Release boundary

This batch is a validated local release candidate. It has not been pushed or
deployed. No authenticated NARA Catalog API request was made. The research goal
remains active because 19,132 person entities have not yet started the research
protocol.
