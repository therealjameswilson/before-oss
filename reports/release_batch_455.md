# Batch 455 release verification

2026-09-10 UTC. **Local release candidate; complete local QA passed and
independent release checks pending.** This release covers PDF page 89 rows
36-45, Leroy G Conn through Emmett F Connelly, in Boxes 138-139 at location
230/86/29/01.

## Research

Page 89 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. Every rank cell is blank.
Numeric identifier forms remain literal and private; no short value was padded,
corrected or transferred to a convenient namesake.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Exact private identifiers and
names confirm George J Connell and Oswald C Connell as Army privates entering
on 20 May 1943 and 20 October 1942, respectively. Physical pages 227 and 170
of NARA's official compiled code list were rendered and visually checked.
George's value 878 is the historical category “Machine shop and related
occupations, n.e.c.”; Oswald's value 001 is “Accountants and auditors.” Neither
category identifies an employer, workplace, credential or immediate OSS
predecessor. Both observations are published only as medium-confidence,
strongly date-bounded statuses.

John G Connell has two exact-name Army rows, while Richard A Connell and Bernard
M Connelly each have one; every candidate has an identifier different from the
literal OSS-index value, so none is assigned. Leroy G Conn, Rebecca Connally,
Jacques M Connaughton, David L Connelly and Emmett F Connelly have no exact-name
enlisted-file row. Those non-hits are not negative proof because the file is
not a comprehensive officer, Navy, Marine Corps, women's-service,
foreign-personnel or OSS roster.

Three independent contemporary sources support a high-confidence identity
match between the indexed Emmett F Connelly and the Detroit figure consistently
printed as Emmett F. Connely. The 22 July 1942 Office of War Information
`Information Digest` identifies the Detroit civilian as nominated to the Army
Specialist Corps as chief of field service with colonel rank. The 1943
`Official Register of the United States` lists Col. Emmett F. Connely as chief
of the Field Office Branch in the Army Officer Procurement Service. The 1940
`Rand McNally Bankers Directory` lists Emmett F. Connely of Detroit as
president of First of Michigan Corporation.

The full name, middle initial, Detroit association and consistent chronology
support the identity, but no reviewed source directly crosswalks the private
OSS-index identifier. The spelling difference therefore remains visible and
identity is not promoted to `confirmed`. First of Michigan is the last
specifically documented civilian employer before the wartime-service evidence.
Because the sources do not explicitly exclude an intervening 1940-1942 role,
that employer claim is medium confidence with `probable_immediate` temporal
basis. It is not presented as the immediate pre-OSS affiliation. An undated
American Securities Corporation lead remains rejected and unpublished.

The current CIA adapter completed one bounded public exact-name search per
person and returned no candidate. The Library of Congress adapter completed
one bounded exact-name employment search per person. Eleven candidates were
inspected in page context and rejected idempotently: five for George J Connell,
five for John G Connell and one for Richard A Connell. They concern different
middle names or initials, McConnell spellings, different generations, postwar
activity, or common-name records without an OSS, private-identifier or Box 139
bridge.

Discovery searches also surfaced a Navy-veteran account for Leroy G Conn, a
1943 Artillery Officer Candidate School roster entry for Jacques M Connaughton,
and several unlinked John G Connell military or Cornell candidates. None has
the identity bridge required for publication. They remain archival leads, not
employment or personnel conclusions.

Leroy G Conn, Jacques M Connaughton, John G Connell, Richard A Connell and
Bernard M Connelly need identity review. Rebecca Connally and David L Connelly
require archival review. George J Connell and Oswald C Connell have
occupation-only outcomes. Emmett F Connelly has a documented-prewar-employer
outcome. All ten still need the applicable Box 138 or 139 file to establish or
confirm the requested immediate and last-civilian affiliations.

Every person received recorded NARA index context, complete Army comparison,
current official CIA and Library of Congress checks, exact-name OSS and
meaningful variant searches, employment and occupation queries, and applicable
institutional, obituary, directory, military, newspaper and archival
discovery. No authenticated NARA Catalog API request was used.

The reviewed bundle adds seven citation records, one organization, three
affiliations, six claims with eighteen source links, ten person updates and ten
saved reviewed-public research attempts. The CIA and Library of Congress
adapters add twenty sanitized project-side attempts. Eleven Library of
Congress candidate decisions remain separately auditable. Imports were
repeated idempotently. See `research/batch-455-discovery-checkpoint.md` for the
adjudication, rejected leads and next actions.

The website now exposes the identity-match and temporal assessment attached to
every public claim in a restrained disclosure panel. Rejected candidate notes
remain private, so transparency about published evidence does not disclose
unaccepted namesakes.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,324 / 23,940 active people | 18.0618% |
| Verified-employer coverage | 227 / 23,940 active people | 0.9482% |
| Verified-affiliation coverage | 512 / 23,940 active people | 2.1387% |
| Archival disposition assessed | 4,279 / 23,940 active people | 17.8739% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,243 commissioned,
5,745 noncommissioned and 15,952 indeterminate. Identity: 838 confirmed, 634
high confidence, 143 probable, 113 ambiguous, 81 conflicting and 22,131
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,616 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 166 |
| needs_temporal_review | 14 |
| verified_employer_found | 214 |
| documented_prewar_employer_found | 85 |
| occupation_only_found | 762 |
| conflicting_sources | 80 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,742 |
| completed | 128 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,018 | 35 |
| high | 1,294 | 295 |
| medium | 1,004 | 97 |
| low | 97 | 1 |
| conflicting | 92 | 2 |

Personnel categories: 1,504 civilian professional or administrative; 2,115
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
87 commissioned naval; 4,066 enlisted Army; 5 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,826 unknown or indeterminate.

Inventory: 554 organizations, 1,703 affiliations, 3,505 claims, 8,138 claim-
source links, 4,095 citation records and 5,681 attempts/plans. Attempt outcomes
are 1,908 `source_reviewed`, 224 `candidate_found`, 696
`candidate_rejected`, 2,266 `no_result` and 587 `planned`. There are 1,893
provisional source-document keys, 1,394 distinct stable URLs and 85 conflicts.
The unresolved export has 22,751 data rows; the pull list 23,764; and the review
queue 23,940.

Public projection: 23,940 people, 542 organizations, 1,692 affiliations, 3,405
published, qualified or conflict-visible claims, 2,936 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 542
organization rows, 1,692 affiliation rows and 2,936 citation rows.

## Local QA and resume

SQLite `quick_check` returns `ok`, foreign keys pass, all 93 Python unit tests
pass in 4.333 seconds, and `npm audit --audit-level=high` reports zero
vulnerabilities. The deterministic 200-profile structural audit passes; it is
not independent historical rereview, and the women stratum remains unavailable
without sourced classification.

The Pages-configuration build reports 79 Astro files with zero errors,
warnings or hints and generates 24,490 HTML pages. All internal links resolve;
49,697 external destinations are inventoried, not all visited. All seven
distinct Batch 455 citation destinations returned HTTP 200 in bounded checks.
The focused Batch 455 plus privacy-regression browser suite passes all eighteen
checks across desktop, phone and tablet. The complete retries-disabled
browser/accessibility matrix passes 2,346/2,346 in one uninterrupted,
keep-awake-guarded run across those three layouts (17.6 minutes).

Identifier audits cover all 24,562 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers and 120 formatted variants. There are
1,094 / 665 candidate substring coincidences, with zero unexpected boundary,
aggregate or manifest-size matches in either tree. `.env` and `.env.*` remain
ignored, only `.env.example` is tracked, and a repository scan finds zero
populated `NARA_API_KEY` assignments.

The public manifest contains 67 assets / 87,058,543 bytes and has SHA-256
`6de80c758f9be62a9677724f34308043dc473cc5cd2ce733871625e1bd26bae9`.
The deterministic public-tree digest covers 70 files / 89,405,685 bytes at
SHA-256
`8e0a4e0e96d7d48185f5f20903d997d02f2948e93bde3249f2cfdc2be436621e`;
the Pages-configured 24,562-file / 276,141,454-byte production tree is
`82ebb7c40326eed2dc8936404e2895281003f6e7bb180c997b36ca348905fa73`.
Two consecutive fresh Pages-configured builds and the complete frozen-input
replay reproduce both tree digests and file counts exactly.

Batches 443-445 remain in open, mergeable PR 198 with successful Test run
`34354744527`. Batch 446 remains in open, mergeable PR 199 with successful Test
run `34361660741`. Batch 447 remains in open, mergeable PR 200 with successful
Test run `34368546155`. Their required merge order is PR 198, PR 199, then PR
200. Batches 448-455 are complete local release candidates layered after PR
200. The live site was checked on 2026-09-09 and still serves Batch 442 data:
4,196 researched people, 505 verified affiliations and 222 verified employers.
External publication requires explicit authorization for that PR chain; the
prior Batch 448 push was stopped by the privacy safety gate because the branch
contains private research material. Each later release must pass independent
Test, Pages deployment and pinned-live verification before being called
deployed.

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-09_batch455.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-nine-leroy-g-conn-through-emmett-f-connelly-pathways_batch-455_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m oss_research audit-profiles --sample-size 200
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
caffeinate -dimsu npx playwright test tests/site.spec.ts -g 'Batch 033' tests/batch455.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/public
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. Continue research at
PDF page 89 row 46. The goal remains active and incomplete, with 19,616 active
people still `not_started`. Rotate the previously exposed credential before
authenticated NARA work; public-source research is not blocked. Unresolved
methodological issues remain: the automated profile audit is structural rather
than independent historical validation, source-document identity normalization
is provisional, and external links are inventoried rather than exhaustively
visited.
