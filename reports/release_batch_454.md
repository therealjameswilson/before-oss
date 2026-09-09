# Batch 454 release verification

2026-09-09 UTC. **Local release candidate; complete local QA passed and
independent release checks pending.** This release covers PDF page 89 rows
26-35, Hugh R Conklin through Charles J Conlon, in Box 138 at location
230/86/29/01.

## Research

Page 89 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. Phillip J Conley is printed
with two l's and rank `Lt Comd`; both are preserved. Numeric identifier forms
remain literal and private. Short values were not padded, corrected or
transferred to a convenient namesake.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Exact private identifiers
confirm Lloyd B Conley and Robert M Conley as Army privates entering on 14
January and 6 July 1943, respectively. Physical pages 247 and 304 of NARA's
official compiled code list were rendered and visually checked. Lloyd's value
187 is the historical category “Salesmen and sales agents, except to
consumers”; Robert's value 992 is “Students.” The first category names no
employer, product or workplace. Student status is not employment and names no
institution. Both are published only as medium-confidence, strongly
date-bounded statuses, not immediate affiliations or last civilian employers.

The identifiers printed for Leonard R Conley and Charles J Conlon each resolve
to an official Army row for a differently named person. Separate exact-name
Army rows exist but carry other identifiers. No candidate is assigned. The
public profiles expose the conflict while withholding the unrelated subjects
and all full identifiers; both cases are excluded from default analytics and
routed to critical Box 138 review.

Edward J Conley has nine and John H Conley twelve exact full-initial Army rows,
none linked by their literal seven-digit index values. Hugh R Conklin and
Arthur P Conkling have no exact full-initial Army row or identifier match. Mary
P Conklin and Phillip J Conley have no indexed identifier. Army-file non-hits
are not negative proof, and no common-name candidate receives an occupation or
employer.

The current CIA adapter completed one bounded public exact-name search per
person and found no candidate. The Library of Congress adapter completed one
bounded exact-name employment search per person; Lloyd's request succeeded on
one bounded retry after an upstream timeout. Ten candidates for Mary P
Conklin, Edward J Conley and John H Conley were inspected in OCR context and
rejected idempotently. They concern different middle names or initials,
different generations, or common-name records without an OSS,
private-identifier or Box 138 bridge.

Discovery-only genealogy, burial, postwar and modern namesake results were also
rejected. They are not used as identity, occupation or employer evidence.
Phillip J Conley's printed lieutenant-commander rank establishes commissioned
naval classification, while his personal identity and pre-OSS chronology
remain unresolved.

Hugh R Conklin, Arthur P Conkling, Edward J Conley and John H Conley need
identity review. Mary P Conklin and Phillip J Conley require archival review.
Leonard R Conley and Charles J Conlon have conflicting-source outcomes. Lloyd
B Conley and Robert M Conley have occupation-only outcomes. All ten still need
their Box 138 files to establish the requested immediate and last-civilian
affiliations.

Every person received recorded NARA index context, complete Army comparison,
current official CIA and Library of Congress checks, exact-name OSS and
meaningful variant searches, employment and occupation queries, and applicable
institutional, obituary, directory, military, newspaper and archival
discovery. No authenticated NARA Catalog API request was used.

The reviewed bundle adds four citation records, two affiliations, six claims
with sixteen source links, ten person updates and ten saved reviewed-public
research attempts. The CIA and Library of Congress adapters add twenty
sanitized project-side attempts. Ten Library of Congress candidate decisions
remain separately auditable. Imports were repeated idempotently. See
`research/batch-454-discovery-checkpoint.md` for the adjudication, rejected
leads and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,314 / 23,940 active people | 18.0201% |
| Verified-employer coverage | 227 / 23,940 active people | 0.9482% |
| Verified-affiliation coverage | 512 / 23,940 active people | 2.1387% |
| Archival disposition assessed | 4,269 / 23,940 active people | 17.8321% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,242 commissioned,
5,743 noncommissioned and 15,955 indeterminate. Identity: 836 confirmed, 633
high confidence, 143 probable, 109 ambiguous, 81 conflicting and 22,138
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,626 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 161 |
| needs_temporal_review | 14 |
| verified_employer_found | 214 |
| documented_prewar_employer_found | 84 |
| occupation_only_found | 760 |
| conflicting_sources | 80 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,740 |
| completed | 128 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,016 | 35 |
| high | 1,293 | 295 |
| medium | 1,001 | 96 |
| low | 97 | 1 |
| conflicting | 92 | 2 |

Personnel categories: 1,504 civilian professional or administrative; 2,114
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
87 commissioned naval; 4,064 enlisted Army; 5 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,829 unknown or indeterminate.

Inventory: 553 organizations, 1,700 affiliations, 3,499 claims, 8,120 claim-
source links, 4,088 citation records and 5,651 attempts/plans. Attempt outcomes
are 1,905 `source_reviewed`, 221 `candidate_found`, 691
`candidate_rejected`, 2,247 `no_result` and 587 `planned`. There are 1,890
provisional source-document keys, 1,391 distinct stable URLs and 85 conflicts.
The unresolved export has 22,754 data rows; the pull list 23,764; and the
review queue 23,940.

Public projection: 23,940 people, 541 organizations, 1,689 affiliations, 3,399
published, qualified or conflict-visible claims, 2,929 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 541
organization rows, 1,689 affiliation rows and 2,929 citation rows.

## Local QA and resume

SQLite `quick_check` returns `ok`, foreign keys pass, all 93 Python unit tests
pass in 4.155 seconds, and `npm audit --audit-level=high` reports zero
vulnerabilities. The deterministic 200-profile structural audit passes; it is
not independent historical rereview, and the women stratum remains unavailable
without sourced classification.

The Pages-configuration build reports 78 Astro files with zero errors,
warnings or hints and generates 24,489 HTML pages. All internal links resolve;
49,693 external destinations are inventoried, not all visited. All four
distinct Batch 454 citation destinations returned HTTP 200 in bounded checks.
The focused Batch 454 browser suite passes all fifteen checks across desktop,
phone and tablet after the sandboxed local server received `EPERM` and the
permitted rerun was used. The complete retries-disabled browser/accessibility
matrix passes 2,331/2,331 in one uninterrupted run across those three layouts.

Identifier audits cover all 24,561 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers, 120 formatted variants and 1,096 / 665
candidate substring coincidences. Two coincidences in each tree are benign,
explicit `size_bytes` values in the public manifest; there are zero unexpected
boundary or aggregate matches. `.env` and `.env.*` remain ignored, only
`.env.example` is tracked, and a repository scan finds zero populated
`NARA_API_KEY` assignments.

The public manifest contains 67 assets / 86,994,470 bytes at SHA-256
`1fc9b77376c5913aaadb5749427d4f585bd6a19010fea0fe08f13df727dcc1e9`.
The deterministic public-tree digest covers 70 files / 89,341,603 bytes at
SHA-256
`a93a9ea888d2cf9c1063e905ed0eee8a9b4a2eb308e97e5dd9890182be0c619a`;
the Pages-configured 24,561-file / 274,496,069-byte production tree is
`c58b55aa2e5cbac2dd1ee54898077a270d9d50109aac67e62e16e0b6354c9dc0`.
Two consecutive fresh Pages-configured builds and the complete frozen-input
replay reproduce both tree digests and file counts exactly.

Batches 443-445 remain in open, mergeable PR 198 with successful Test run
`34354744527`. Batch 446 remains in open, mergeable PR 199 with successful Test
run `34361660741`. Batch 447 remains in open, mergeable PR 200 with successful
Test run `34368546155`. Their required merge order is PR 198, PR 199, then PR
200. Batches 448-454 are complete local release candidates layered after PR
200. The live site was checked on 2026-09-09 and still serves Batch 442 data:
4,196 researched people, 505 verified affiliations and 222 verified employers.
External publication requires explicit authorization for that PR chain; the
prior Batch 448 push was stopped by the privacy safety gate because the branch
contains private research material. Each later release must pass independent
Test, Pages deployment and pinned-live verification before being called
deployed.

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-09_batch454.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-nine-hugh-r-conklin-through-charles-j-conlon-pathways_batch-454_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m oss_research audit-profiles --sample-size 200
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch454.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. Continue research at
PDF page 89 row 36. The goal remains active and incomplete, with 19,626 active
people still `not_started`. Rotate the previously exposed credential before
authenticated NARA work; public-source research is not blocked. Unresolved
methodological issues remain: the automated profile audit is structural rather
than independent historical validation, source-document identity normalization
is provisional, external links are inventoried rather than exhaustively
visited, and most personnel files still require archival examination.
