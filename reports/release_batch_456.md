# Batch 456 release verification

2026-09-10 UTC. **Local release candidate; complete local QA passed and
independent release checks pending.** This release covers PDF page 89 row 46
and page 90 rows 1-9, Marguerite Connelly through Thomas Conniff, in Box 139 at
location 230/86/29/01.

## Research

Pages 89-90 were rendered at 150 dpi and every printed field in the ten-row
cohort was visually compared with the immutable database. Every rank cell is
blank. Identifier forms remain literal and private; none was padded, silently
corrected or transferred to a convenient namesake.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066, then
scanned across all 9,200,232 fixed-width records.

Five private identifiers select exact-name or explicitly preserved
name-variant Army records:

- Ralph H Connelly entered as a private on 18 May 1943; historical occupation
  code 473 is Engravers.
- Richard D Connelly entered as a private on 14 February 1944 in an Army row
  printed Richard D Connely; code 992 is Students. A separate exact-spelling
  namesake has another identifier and is not assigned.
- Annie G Conner entered on 13 January 1943 with Auxiliary grade and WAC branch
  coding; code 137 is Stenographers and typists. The Army file's hyphenated
  identifier form is preserved privately.
- Fred N Conner entered as a private on 11 March 1943; code 794 is Machinists'
  apprentices.
- John J Conner entered as a private on 8 May 1943; code 513 is Miscellaneous
  products manufacturing occupations, n.e.c. The private identifier
  disambiguates one of five exact-name Army rows.

Physical pages 171, 173, 175, 177 and 304 of NARA's official compiled code
list were rendered and visually checked. All five observations are published
only as medium-confidence, strongly date-bounded occupation or student-status
findings. They supply no named employer, institution, product, specialty,
workplace or immediate Army-to-OSS sequence. Student status is not classified
as employment.

An exact-name Army row for Melvin E Conner is not assigned because the index
has no identifier or rank. No exact full-name Army row was found for Marguerite
Connelly, Margaret L Conner, Willie M Connick or Thomas Conniff. These non-hits
are not negative proof because the file is incomplete and is not a
comprehensive officer, Navy, Marine Corps, women's-service, foreign-personnel
or OSS roster.

The current CIA adapter completed one bounded public exact-name search per
person and returned no candidates. The Library of Congress adapter completed
one bounded exact-name employment search per person. Nine candidates were
inspected in OCR context and rejected idempotently: five for John J Conner,
two for Margaret L Conner and two for Thomas Conniff. The 1940 Labor Department
conciliator named John J. Conner lacks the private identifier, military, OSS
and Box 139 bridge required for assignment. The Margaret results are postwar
family notices; the Thomas results are early auctioneer notices without an
identity bridge.

Every person also received exact-name OSS and meaningful variant searches,
employment and occupation queries, and applicable institutional, obituary,
directory, military, newspaper and archival discovery. No authenticated NARA
Catalog API request was used.

Marguerite Connelly, Margaret L Conner, Willie M Connick and Thomas Conniff
require archival review. Melvin E Conner needs identity review. Ralph H
Connelly, Richard D Connelly, Annie G Conner, Fred N Conner and John J Conner
have occupation-only outcomes. All ten still need Box 139 to establish or
confirm the requested immediate and last-civilian affiliations.

The reviewed bundle adds four citation records, five affiliations, ten claims
with thirty source links, ten person updates and ten saved reviewed-public
research attempts. The CIA and Library of Congress adapters add twenty
sanitized project-side attempts. Nine Library of Congress candidate decisions
remain separately auditable. Imports were repeated idempotently. See
research/batch-456-discovery-checkpoint.md for printed identifiers, rejected
leads, adjudications and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,334 / 23,940 active people | 18.1036% |
| Verified-employer coverage | 227 / 23,940 active people | 0.9482% |
| Verified-affiliation coverage | 512 / 23,940 active people | 2.1387% |
| Archival disposition assessed | 4,289 / 23,940 active people | 17.9156% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,243 commissioned,
5,750 noncommissioned and 15,947 indeterminate. Identity: 843 confirmed, 634
high confidence, 143 probable, 114 ambiguous, 81 conflicting and 22,125
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,606 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 167 |
| needs_temporal_review | 14 |
| verified_employer_found | 214 |
| documented_prewar_employer_found | 85 |
| occupation_only_found | 767 |
| conflicting_sources | 80 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,746 |
| completed | 128 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,023 | 35 |
| high | 1,294 | 295 |
| medium | 1,009 | 97 |
| low | 97 | 1 |
| conflicting | 92 | 2 |

Personnel categories: 1,504 civilian professional or administrative; 2,115
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
87 commissioned naval; 4,071 enlisted Army; 5 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,821 unknown or indeterminate.

Inventory: 554 organizations, 1,708 affiliations, 3,515 claims, 8,168
claim-source links, 4,099 citation records and 5,711 attempts/plans. Attempt
outcomes are 1,913 source_reviewed, 227 candidate_found, 701
candidate_rejected, 2,283 no_result and 587 planned. There are 1,893
provisional source-document keys, 1,394 distinct stable URLs and 85 conflicts.
The unresolved export has 22,746 data rows; the pull list 23,764; and the review
queue 23,940.

Public projection: 23,940 people, 542 organizations, 1,697 affiliations, 3,415
published, qualified or conflict-visible claims, 2,940 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 542
organization rows, 1,697 affiliation rows and 2,940 citation rows.

## Local QA and resume

SQLite quick_check returns ok, foreign keys pass, all 93 Python unit tests pass
in 4.250 seconds, and npm audit at high severity reports zero vulnerabilities.
The deterministic 200-profile structural audit passes; it is not independent
historical rereview, and the women stratum remains unavailable without sourced
classification.

The Pages-configuration build reports 80 Astro files with zero errors, warnings
or hints and generates 24,490 HTML pages. All internal links resolve; 49,697
external destinations are inventoried, not all visited. All four distinct
Batch 456 citation destinations returned HTTP 200 in bounded checks. The
focused Batch 456 plus privacy-regression browser suite passes all eighteen
checks across desktop, phone and tablet. The complete retries-disabled
browser/accessibility matrix passes all 2,361 checks across desktop, phone and
tablet in 18.0 minutes.

Identifier audits cover all 24,562 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers and 120 formatted variants. There are
1,094 / 665 candidate substring coincidences, with zero unexpected boundary,
aggregate or manifest-size matches in either tree. Only .env.example is
tracked, and the generated public assets contain no full service identifiers.

The public manifest contains 67 assets / 87,135,509 bytes and has SHA-256
e9bdc2bc0b3a28f48f8b0c1a54a832c46c766db75cc798d125392520ce180d0c.
The deterministic public-tree digest covers 70 files / 89,482,644 bytes at
SHA-256
b9d180f1ab8a7068a4e46a6d2e37c618a7126753094eed37cc201445b065853f;
the Pages-configured 24,562-file / 276,256,218-byte production tree is
b01805c91411640308b345c798b4acf0d64064e495dee0053e8f31d756a14e8e.
A complete frozen-input replay reproduced both tree digests and file counts
exactly.

Batches 443-445 remain in open, mergeable PR 198 with successful Test run
34354744527. Batch 446 remains in open, mergeable PR 199 with successful Test
run 34361660741. Batch 447 remains in open, mergeable PR 200 with successful
Test run 34368546155. Their required merge order is PR 198, PR 199, then PR
200. Batches 448-456 are complete local release candidates layered after PR
200. The live site still serves Batch 442 data. External publication requires
explicit authorization for that PR chain; the prior push was stopped by the
privacy safety gate because the branch contains private research material.
Each later release must pass independent Test, Pages deployment and pinned-live
verification before being called deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-10_batch456.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-pages-eighty-nine-ninety-marguerite-connelly-through-thomas-conniff-pathways_batch-456_2026-09-10.json
    python3 -m oss_research export-derived
    python3 -m oss_research export-review-queue
    python3 -m oss_research coverage-report
    python3 -m oss_research build-public-data
    python3 -m oss_research audit-profiles --sample-size 200
    cd site
    PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
    caffeinate -dimsu npx playwright test tests/site.spec.ts -g 'Batch 033' tests/batch456.spec.ts
    npm run check:links
