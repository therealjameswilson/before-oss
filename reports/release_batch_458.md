# Batch 458 release verification

2026-09-10 UTC. **Local release candidate; historical, data, build, privacy,
link, reproducibility, accessibility and complete three-viewport browser QA
passed. Independent release checks remain pending.** This release covers PDF
page 90 rows 20-29, Irving Connors through Marion C Conroy, in Boxes 139-140
at location 230/86/29/01.

## Research

Page 90 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. Every rank cell is blank.
Identifier forms remain literal and private; none was padded, silently
corrected or transferred to a convenient namesake. All ten rows remain
separate source records and person entities.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066, then
scanned across all 9,200,232 fixed-width records.

Robert J Conrad's exact private identifier and exact full name select an Army
private entry dated 16 February 1943. Historical occupation code 543 is
“Motormen, street, subway, and elevated railway.” This is a
medium-confidence, strongly date-bounded occupation observation, not a named
employer or a demonstrated immediate OSS predecessor.

Louise W Conrad's exact private identifier selects an Army private entry named
Louis W Conrad. The surname and middle initial agree, but the first name
conflicts. No grade, date, occupation or identity is transferred from that
record. The public profile instead carries a conflict claim that withholds the
unrelated name and identifier.

Doda Conrad has one exact rare-name Army row dated 13 July 1942 as a private.
Its birth-year value and American Army chronology agree with independent New
York Public Library and Musée d'art et d'histoire du Judaïsme descriptions.
Together they support a high-confidence identity and a baritone/bass musical
career. Army occupation code 024 is “Musicians and teachers of music.” No
employer, ensemble or venue is inferred.

Owen M Conrad has one exact full-name Army row dated 30 October 1942 as a
private. Code 175 is “Salespersons.” An independent WCVB / Patriot Ledger
report identifies an Owen Conrad as a career soldier and OSS communications
officer but omits his middle initial. The rare exact Army name, wartime Army
context and independent OSS context support high confidence rather than
confirmation. A later lieutenant-colonel reference does not establish
commissioned status during OSS service, so that classification remains
indeterminate.

Physical pages 171 and 174 of NARA's official compiled code list were rendered
at 150 dpi and visually checked. The three occupational labels identify no
named employer or immediate OSS predecessor.

Henry Conrad has two exact-name Army candidates with different dates,
birth-year values and occupations; neither is assigned. Denzil L Conrad's
private identifier and exact full name have no Army-file match. Irving
Connors, Allen J Conover, Margaret E Conroy and Marion C Conroy have no exact
full-name Army row. These non-hits are not negative proof because the file is
incomplete and is not a comprehensive officer, Navy, Marine Corps,
women's-service, foreign-personnel or OSS roster.

The CIA adapter completed one bounded public exact-name search for each person
and returned no candidates. The Library of Congress adapter completed one
bounded exact-name employment search per person. Three Evening Star candidates
for Robert J Conrad were inspected in OCR context and rejected idempotently:
they contain adjacent or unrelated name terms and supply no exact Robert J
Conrad context, private identifier, OSS service or Box 140 bridge.

Every person also received exact-name OSS and meaningful variant searches,
employment and occupation queries, and applicable institutional, obituary,
directory, military, newspaper and archival discovery. No authenticated NARA
Catalog API request was used.

Irving Connors, Allen J Conover, Margaret E Conroy and Marion C Conroy require
archival review. Denzil L Conrad and Henry Conrad require identity review.
Louise W Conrad has a conflict-visible outcome. Doda Conrad, Owen M Conrad and
Robert J Conrad have occupation-only outcomes. All ten people still need Box
139 or 140 to establish or confirm the requested immediate and last-civilian
affiliations.

The reviewed bundle adds seven citation records, three affiliations, seven
claims with twenty-four source links, ten person updates and ten saved
reviewed-public research attempts. The CIA and Library of Congress adapters
add twenty sanitized project-side attempts. Three Library of Congress
candidate decisions remain separately auditable. Imports were repeated
idempotently. See `research/batch-458-discovery-checkpoint.md` for printed
identifiers, rejected leads, adjudications and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,353 / 23,940 active people | 18.1830% |
| Verified-employer coverage | 227 / 23,940 active people | 0.9482% |
| Verified-affiliation coverage | 513 / 23,940 active people | 2.1429% |
| Archival disposition assessed | 4,308 / 23,940 active people | 17.9950% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,243 commissioned,
5,755 noncommissioned and 15,942 indeterminate. Identity: 847 confirmed, 635
high confidence, 143 probable, 119 ambiguous, 83 conflicting and 22,113
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,587 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 172 |
| needs_temporal_review | 14 |
| verified_employer_found | 214 |
| documented_prewar_employer_found | 85 |
| occupation_only_found | 773 |
| conflicting_sources | 82 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,752 |
| completed | 128 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,027 | 35 |
| high | 1,297 | 295 |
| medium | 1,014 | 97 |
| low | 97 | 1 |
| conflicting | 94 | 2 |

Personnel categories: 1,504 civilian professional or administrative; 2,115
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
87 commissioned naval; 4,077 enlisted Army; 5 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,815 unknown or indeterminate.

Inventory: 554 organizations, 1,714 affiliations, 3,529 claims, 8,212
claim-source links, 4,110 citation records and 5,769 attempts/plans. Attempt
outcomes are 1,921 source_reviewed, 233 candidate_found, 712
candidate_rejected, 2,315 no_result and 588 planned. There are 1,896
provisional source-document keys, 87 conflicts and 4,110 citations. The
unresolved export has 22,740 data rows; the pull list 23,764; and the review
queue 23,940.

Public projection: 23,940 people, 542 organizations, 1,703 affiliations, 3,429
published, qualified or conflict-visible claims, 2,951 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 542
organization rows, 1,703 affiliation rows and 2,951 citation rows.

## Local QA and resume

SQLite quick_check returns ok, foreign keys pass, all 93 Python unit tests
pass, and npm audit at high severity reports zero vulnerabilities. The
deterministic 200-profile structural audit passes; it is not independent
historical rereview, and the women stratum remains unavailable without sourced
classification.

The Pages-configuration build reports 82 Astro files with zero errors,
warnings or hints and generates 24,490 HTML pages / 24,562 artifacts. All
internal links resolve; 49,700 external destinations are inventoried, not all
visited. All seven distinct Batch 458 citation destinations returned HTTP 200
in bounded checks. The focused Batch 458 plus privacy-regression browser suite
passes all eighteen checks across desktop, phone and tablet.

The complete browser/accessibility matrix covers 797 tests in each of the
desktop, phone and tablet projects, for 2,391 passing checks. Desktop and phone
each completed in the original sleep-prevented run. That process was
interrupted at the turn boundary after 495 tablet checks; the complete tablet
project was therefore rerun and passed 797 / 797 in 7.4 minutes. No assertion,
content or data-product failure remains.

Identifier audits cover all 24,562 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers and 120 formatted variants. There are
1,092 / 663 candidate substring coincidences, with zero unexpected boundary,
aggregate or manifest-size matches in either tree. Only `.env.example` is
tracked, and the generated public assets contain no full service identifiers.

The public manifest contains 67 assets / 87,254,989 bytes and has SHA-256
04d115d7a69b9bba0691cc000f76ac1efc53860abec842965326cd5fc5b80f87.
The deterministic public-tree digest covers 70 files / 89,602,131 bytes at
SHA-256
2f6d6f156ded33e62a2792127aa38329823bfcd34cb1525c598c678d84f79e19;
the Pages-configured 24,562-file / 276,432,190-byte production tree is
ab0a7c0c5bb861f77271f5442def010288fbfd77fe2f2a83460942d2b17c2005.
A complete frozen-input replay reproduced both tree digests and file counts
exactly.

Batches 443-445 remain in open, mergeable PR 198 with successful Test run
34354744527. Batch 446 remains in open, mergeable PR 199 with successful Test
run 34361660741. Batch 447 remains in open, mergeable PR 200 with successful
Test run 34368546155. Their required merge order is PR 198, PR 199, then PR
200. Batches 448-458 are complete local release candidates layered after PR
200. The live site still serves Batch 442 data. External publication requires
explicit authorization for that PR chain; the prior push was stopped by the
privacy safety gate because the branch contains private research material.
Each later release must pass independent Test, Pages deployment and
pinned-live verification before being called deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-10_batch458.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-irving-connors-through-marion-conroy-pathways_batch-458_2026-09-10.json
    python3 -m oss_research export-derived
    python3 -m oss_research export-review-queue
    python3 -m oss_research coverage-report
    python3 -m oss_research build-public-data
    python3 -m oss_research audit-profiles --sample-size 200
    cd site
    PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
    caffeinate -dimsu npx playwright test --project=tablet
    npm run check:links

Batch 459 resumes with PDF page 90 rows 30-39.
