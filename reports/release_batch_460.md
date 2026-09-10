# Batch 460 release verification

2026-09-10 UTC. **Local release candidate; historical, data, build, privacy,
link, reproducibility, accessibility and complete three-viewport browser QA
passed. Independent release checks remain pending.** This release covers PDF
page 90 rows 40-46 and page 91 rows 1-3, Edmund C Converse through Charles W
Cook, in Box 140 at location 230/86/29/01.

## Research

Pages 90-91 were rendered at 150 dpi and every printed field in the ten-row
cohort was visually compared with the immutable database. All ten printed rank
cells are blank and remain blank. Five identifiers remain literal and private;
the six- and seven-digit forms were not padded, silently corrected or
transferred to a convenient namesake. All ten rows remain separate source
records and person entities.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066, then
scanned across all 9,200,232 fixed-width records.

William E Conway's exact private identifier and exact full name select an Army
private entry dated 30 July 1945. Its civilian-occupation value 992 maps to
“Students.” This identifies neither a school nor an employer. The entry is
late in the war and the OSS accession date is unknown, so the student status is
published with `temporal_relation_uncertain`, not as the immediate pre-OSS
affiliation or last civilian employer.

Harry G Coogias's exact private identifier selects an Army private entry with
the same rare first and surname but a conflicting middle initial. No grade,
entry date, occupation or identity is transferred. The public profile carries
only the conflict notice and withholds the alternative name, identifier and raw
row.

Alan C Conway's literal seven-digit identifier has no Army-file match. One
exact-name Army row has another identifier and is not assigned. Charles W Cook's
exact eight-digit identifier and William H Conway's literal six-digit identifier
have no file match; numerous exact-name candidates cannot be distinguished.
William F Conway also has numerous name candidates but no index identifier.
George M Converse has one name candidate but no index identifier or public
identity bridge. Edmund C Converse, Alice E Conway and Cecilia M Cook have no
exact full-name row. These non-hits are not negative proof because the file is
incomplete and is not a comprehensive officer, Navy, Marine Corps, women's
service, foreign-personnel or OSS roster.

Physical page 304 of NARA's official compiled code list was rendered at 150 dpi
and visually checked for 9-92, “Students.” The label names no institution,
course, degree, employer or immediate OSS predecessor.

The University of Wyoming American Heritage Center's *Guide to Politics and
Public Affairs Resources* contains an institutional biography for the Edmund
Converse Papers, 1943-1970, Accession 10826. PDF physical page 22, printed page
21, was rendered at 150 dpi and inspected. The collection heading misspells the
given name “Edumnd”; the citation notes that source wording rather than silently
correcting it.

The guide says Converse was born in New York City in 1906, grew up in
California, and had earned economics and law degrees from Stanford University
by 1934. It dates his service on U.S. Senator Styles Bridges's staff to
1937-1941, then says he entered the Navy in 1941 and served in the Office of
Naval Intelligence, the Pacific Fleet and OSS. Its later 1945 airline material
is identity context only and is not used to answer the pre-OSS question.

The rare exact name, indexed middle initial, explicit OSS service and detailed
institutional chronology support a high-confidence identity match. The United
States Navy is the best-supported probable immediate institutional pathway into
OSS, but the source does not establish whether ONI or the Pacific Fleet was the
last specific command, an exact transfer date, or Converse's rank. The office
of Senator Styles Bridges is the high-confidence last civilian employer before
1941 Navy entry. Stanford is an earlier student affiliation, not an employer.

The CIA adapter completed one bounded public exact-name search per person and
returned no candidates. The Library of Congress adapter completed one bounded
exact-name employment search per person and returned twenty discovery
candidates across ten newspaper pages. Every item was inspected in page context
and rejected through the auditable decision import: the hits were different
middle initials, historical people from 1896-1905, a spouse or auxiliary rather
than Charles W Cook, a postwar town official, and OCR word collisions. No
candidate supplies the private identifier, OSS context or Box 140 bridge.

Every person also received exact-name OSS and meaningful variant searches,
employment and occupation queries, and applicable institutional, obituary,
directory, military, newspaper and archival discovery. No authenticated NARA
Catalog API request was used.

Edmund C Converse has a verified-employer outcome. William E Conway has an
occupation-only outcome. Harry G Coogias has a conflict-visible outcome. Alice
E Conway and Cecilia M Cook require archival review; George M Converse, Alan C
Conway, William F Conway, William H Conway and Charles W Cook require identity
review. All ten still need Box 140 to answer or independently confirm the
requested immediate and last-civilian affiliations. Edmund also needs American
Heritage Center Accession 10826 to confirm his middle name, rank, command
sequence and OSS accession.

The reviewed bundle adds five citation records, four affiliations, seven claims
with thirteen source links, ten person updates and ten saved reviewed-public
research attempts. Three organizations are included and the existing United
States Navy organization is reused idempotently. The CIA and Library of
Congress adapters add twenty sanitized attempts and twenty rejected candidate
records. Repeated imports produced no duplicate decisions or evidence records.
See `research/batch-460-discovery-checkpoint.md` for printed identifiers,
rejected leads, adjudications and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,373 / 23,940 active people | 18.2665% |
| Verified-employer coverage | 229 / 23,940 active people | 0.9566% |
| Verified-affiliation coverage | 515 / 23,940 active people | 2.1512% |
| Archival disposition assessed | 4,328 / 23,940 active people | 18.0785% |

There are 23,941 stored entities and one superseded entity; 236 possible
duplicate groups remain visible. Officer classification: 2,243 commissioned,
5,760 not commissioned and 15,937 indeterminate. Identity: 851 confirmed, 638
high confidence, 143 probable, 127 ambiguous, 85 conflicting and 22,096
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,567 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 180 |
| needs_temporal_review | 14 |
| verified_employer_found | 216 |
| documented_prewar_employer_found | 85 |
| occupation_only_found | 777 |
| conflicting_sources | 84 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,756 |
| completed | 128 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,031 | 35 |
| high | 1,306 | 299 |
| medium | 1,018 | 97 |
| low | 97 | 1 |
| conflicting | 96 | 2 |

Personnel categories: 1,505 civilian professional or administrative; 2,115
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
87 commissioned naval; 4,081 enlisted Army; 5 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,810 unknown or indeterminate.

Inventory: 556 organizations, 1,723 affiliations, 3,548 claims, 8,261
claim-source links, 4,124 citation records and 5,829 attempts/plans. Attempt
outcomes are 1,930 source reviewed, 239 candidate found, 721 candidate rejected,
2,351 no result and 588 planned. There are 1,902 provisional source-document
keys, 1,403 distinct stable URLs, 89 conflicts and 4,124 citations. The
unresolved export has 22,734 data rows; the pull list 23,762; and the review
queue 23,940.

Public projection: 23,940 people, 544 organizations, 1,712 affiliations, 3,448
published, qualified or conflict-visible claims, 2,965 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 544
organization rows, 1,712 affiliation rows and 2,965 citation rows.

## Local QA and resume

SQLite quick_check returns ok, foreign keys pass, all 93 Python unit tests pass,
and npm audit at high severity reports zero vulnerabilities. The deterministic
200-profile structural audit passes; it is not independent historical rereview,
and the women stratum remains unavailable without sourced classification.

The Pages-configuration build reports 84 Astro files with zero errors, warnings
or hints and generates 24,492 HTML pages / 24,564 artifacts. All internal links
resolve; 49,708 external destinations are inventoried, not all visited. The five
official Batch 460 citation destinations—the NARA index, Catalog series record,
Army layout documentation, code list and University of Wyoming guide—returned
HTTP 200 on the release date.

The focused Batch 460 browser suite passes all fifteen checks across desktop,
phone and tablet. The complete browser/accessibility matrix passes 808 / 808
checks in each project, for 2,424 / 2,424 passing checks in 18.1 minutes. No
assertion, content, responsive-layout, accessibility or data-product failure
remains.

Identifier audits cover all 24,564 built artifacts and all 70 public-tree files,
12,926 normalized identifiers and 120 formatted variants. There are 1,095 / 663
candidate substring coincidences, with zero unexpected boundary, aggregate or
manifest-size matches in either tree. Only `.env.example` is tracked, and the
generated public assets contain no full service identifiers.

The public manifest contains 67 assets / 87,438,143 bytes and has SHA-256
dea85fe3eebec622f2b48569aa9043adeaba7626d7d30a3e7363227e0a1b1032.
The deterministic public-tree digest covers 70 files / 89,785,290 bytes at
SHA-256
7c3fb612e0158f1d98d3a947fe074106a1e855c8826f64392cd63545a323d44f;
the Pages-configured 24,564-file / 276,706,325-byte production tree is
3863a91b9536f4d3fbe242c4504ae4fc36d82bc1fb8fcb4487db20000e00eb15.
A complete fresh-database frozen-input replay reproduced both tree digests, the
manifest digest, every byte total and every file count exactly. The replay
database independently produced 23,978 source rows, 23,941 stored entities and
5,829 attempts with clean integrity and foreign keys.

Batches 443-445 remain in open, mergeable PR 198 with successful Test run
34354744527. Batch 446 remains in open, mergeable PR 199 with successful Test
run 34361660741. Batch 447 remains in open, mergeable PR 200 with successful
Test run 34368546155. Their required merge order is PR 198, PR 199, then PR 200.
Batches 448-460 are complete local release candidates layered after PR 200. A
fresh live-data request confirms that the public site still serves Batch 442
data: 4,196 research-attempted people, 222 verified employers and 505 verified
affiliations. External publication requires explicit authorization for the PR
chain; the prior push was stopped by the privacy safety gate because this branch
contains private research material. Each later release must pass independent
Test, Pages deployment and pinned-live verification before being called
deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-10_batch460.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-edmund-c-converse-through-charles-w-cook-pathways_batch-460_2026-09-10.json
    python3 -m oss_research export-derived
    python3 -m oss_research export-review-queue
    python3 -m oss_research coverage-report
    python3 -m oss_research build-public-data
    python3 -m oss_research audit-profiles --sample-size 200
    cd site
    PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
    caffeinate -dimsu npx playwright test --project=desktop --project=phone --project=tablet
    npm run check:links

Batch 461 resumes with PDF page 91 rows 4-13: Charles O Cook, Dale F Cook,
Davis L Cook, Elizabeth H Cook, Eva C Cook, Francis Cook, Fred H Cook, Harl
Cook, Harry E Cook and Hughes M Cook.
