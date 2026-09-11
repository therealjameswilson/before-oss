# Batch 462 release verification

2026-09-10 UTC. **Local release candidate; historical, data, build, privacy,
link, reproducibility, accessibility and complete three-viewport browser QA
passed. Independent release checks remain pending.** This release covers PDF
page 91 rows 14-23, John E Cook through Adelaide L Cooke, in Boxes 140-141 at
location 230/86/29/01.

## Research

Page 91 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. Richard C Cook's printed
rank is `Pvt`; the other nine rank cells are blank and remain blank. Seven
identifiers remain literal and private. All ten rows remain separate source
records and person entities.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066, then
scanned across all 9,200,232 fixed-width records.

Kenneth Cook's exact private identifier selects an Army private entry for
Kenneth W Cook dated 1 October 1942; the index omits the middle initial. The
selected entry's civilian-occupation value 992 maps to “Students.” The school,
field of study, employer and pre-OSS sequence are not named. The exact unique
identifier confirms identity and enlisted Army classification, while the
student category is published as a medium-confidence occupation observation,
not an employer or institutional affiliation.

Maurice W Cook's exact private identifier and exact name select an Army private
entry dated 15 September 1942. Civilian-occupation value 736 maps to
“Chauffeurs and drivers, bus, taxi, truck, and tractor.” The category does not
identify an employer, vehicle type, route, workplace or OSS sequence. It is
published as a medium-confidence occupation observation, not an employer.

Richard C Cook's exact private identifier and exact name select an Army private
entry dated 27 November 1942, corroborating the index's printed `Pvt` rank.
Civilian-occupation value 992 maps to “Students.” The school, field of study,
employer and pre-OSS sequence remain unknown. The category is not converted
into an employer or institutional affiliation.

Wilmer J Cook's exact private identifier and exact name select an Army private
entry dated 2 October 1943. Civilian-occupation value 316 maps to “Farm hands,
general farms.” The category names no farm, owner, employer, crop, location,
duties or OSS sequence. It is published as a medium-confidence occupation
observation, not an employer.

William R Cook presents a direct identifier conflict. His printed private
identifier selects an Army row for William B Cook, while exact-name William R
Cook rows have different identifiers. No candidate's rank, date, occupation or
other facts are transferred. The index remains literal and the conflict is
routed to critical Box 141 review.

Vernon J Cook's printed identifier has no Army-file row, but NARA's technical
documentation makes that non-hit inconclusive: the identifier falls inside the
documented missing range 36-488-000 through 37-103-673, covering missing rolls
1091-1166. The range condition is published as archival guidance; it is not an
identity, occupation or employer claim.

John E Cook's six-digit printed identifier was preserved literally and neither
silently padded nor corrected. It does not select an Army-file row, while
multiple exact-name John E Cook rows carry other identifiers. Thomas G Cook
also has multiple exact-name Army candidates but no index identifier with
which to distinguish them. Martha B Cook and Adelaide L Cooke have no exact
printed-name Army row. None is assigned. Army-file nonappearance is not
negative proof because the file is incomplete and is not an officer, Navy,
Marine Corps, women's-service, foreign-personnel or complete OSS roster.

NARA technical-documentation physical pages 13 and 44-46 and code-list pages
172 and 174 were rendered at 180 dpi and visually inspected. Page 13 supports
the missing-range explanation; pages 44-46 support the selected fixed-width
fields; pages 172 and 174 support only the two short occupation labels. The
student code was already visually verified on code-list page 304.

The CIA adapter completed one bounded public exact-name search per person and
returned no candidates. The Library of Congress adapter completed one bounded
exact-name employment search per person and returned twenty-one discovery
candidates. Every item was inspected against page-level OCR and rejected
through the decision ledger. The results were namesakes, missing-name OCR
collisions, or lacked an identifier or OSS/Box 140-141 bridge.

Exact-name OSS and meaningful variant searches, employment and occupation
queries, and applicable institutional, obituary, directory, military,
newspaper and archival searches found no public source that bridges another
namesake to these index rows. A Maurice W Cook aircraft-worker directory entry,
a Kenneth H Cook Navy Department obituary, Thomas George Cook legal notices
and a 1943 William R Cook faculty-adviser item were rejected because they did
not establish the indexed identity or relevant chronology. Modern people,
relatives, unsourced genealogy and generic keyword collisions were rejected.
No authenticated NARA Catalog API request was used.

Kenneth Cook, Maurice W Cook, Richard C Cook and Wilmer J Cook have
occupation-only outcomes. William R Cook has a conflict-visible outcome. John
E Cook and Thomas G Cook require identity review. Martha B Cook, Vernon J Cook
and Adelaide L Cooke require archival review. Every person still needs the
indexed Box 140 or 141 personnel file to identify or confirm an immediate
pre-OSS affiliation and last civilian employer.

The reviewed bundle adds four citation records, four affiliations, ten claims
with thirty-four source links, ten person updates and ten saved reviewed-public
research attempts. The CIA and Library of Congress adapters add thirty
sanitized attempts and twenty-one rejected candidates. Repeated imports
produced no duplicate decisions or evidence records. See
`research/batch-462-discovery-checkpoint.md` for the private identifiers,
rejected leads, adjudications and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,393 / 23,940 active people | 18.3500% |
| Verified-employer coverage | 229 / 23,940 active people | 0.9566% |
| Verified-affiliation coverage | 515 / 23,940 active people | 2.1512% |
| Archival disposition assessed | 4,348 / 23,940 active people | 18.1621% |

There are 23,941 stored entities and one superseded entity; 236 possible
duplicate groups remain visible. Officer classification: 2,243 commissioned,
5,766 not commissioned and 15,931 indeterminate. Identity: 858 confirmed, 638
high confidence, 143 probable, 132 ambiguous, 87 conflicting and 22,082
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,547 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 185 |
| needs_temporal_review | 14 |
| verified_employer_found | 216 |
| documented_prewar_employer_found | 85 |
| occupation_only_found | 783 |
| conflicting_sources | 86 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,763 |
| completed | 128 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,040 | 35 |
| high | 1,306 | 299 |
| medium | 1,024 | 97 |
| low | 97 | 1 |
| conflicting | 98 | 2 |

Personnel categories: 1,505 civilian professional or administrative; 2,115
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
87 commissioned naval; 4,087 enlisted Army; 5 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,804 unknown or indeterminate.

Inventory: 556 organizations, 1,729 affiliations, 3,565 claims, 8,316
claim-source links, 4,132 citation records and 5,889 attempts/plans. Attempt
outcomes are 1,939 source reviewed, 251 candidate found, 727 candidate rejected,
2,384 no result and 588 planned. There are 1,902 provisional source-document
keys, 1,403 distinct stable URLs, 91 conflicts and 4,132 citations. The
unresolved export has 22,728 data rows; the pull list 23,762; and the review
queue 23,940.

Public projection: 23,940 people, 544 organizations, 1,718 affiliations, 3,465
published, qualified or conflict-visible claims, 2,973 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 544
organization rows, 1,718 affiliation rows and 2,973 citation rows.

## Local QA and resume

SQLite quick_check returns ok, foreign keys pass, all 93 Python unit tests pass,
and npm audit at high severity reports zero vulnerabilities. The deterministic
200-profile structural audit passes; it is not independent historical rereview,
and the women stratum remains unavailable without sourced classification.

The Pages-configuration build reports 86 Astro files with zero errors, warnings
or hints and generates 24,492 HTML pages / 24,564 artifacts. All internal links
resolve; 49,708 external destinations are inventoried, not all visited. The
four official Batch 462 citation destinations—the NARA index, Catalog series
record, Army layout documentation and code list—returned HTTP 200 on the
release date.

The focused Batch 462 browser suite passes all fifteen checks across desktop,
phone and tablet. The complete browser/accessibility matrix passes
818 / 818 checks in each project, for 2,454 / 2,454 passing checks in 18.1
minutes. No assertion, content, responsive-layout, accessibility or data-product
failure remains.

Identifier audits cover all 24,564 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers and 120 formatted variants. There are
1,094 / 665 candidate substring coincidences, with zero unexpected boundary,
aggregate or manifest-size matches in either tree. Only `.env.example` is
tracked, and the generated public assets contain no full service identifiers.

The public manifest contains 67 assets / 87,578,667 bytes and has SHA-256
30a3ac9875f58eaefd809747669ea14e6564f04a7ce139f1f270ac251e59eb74.
The deterministic public-tree digest covers 70 files / 89,925,808 bytes at
SHA-256
25f81e0519d61b55206d92a2450244edf6fd1a1d21068305809f4a88e44316ba;
the Pages-configured 24,564-file / 276,912,303-byte production tree is
c74f5ce1bf09d958a06d70de4e489a04e6687c79a0f77195f2cbf16aac45b0a5.
A complete fresh-database frozen-input replay reproduced both tree digests, the
manifest digest, every byte total and every file count exactly. The replay
database independently produced 23,978 source rows, 23,941 stored entities,
1,729 affiliations, 3,565 claims, 8,316 claim-source links, 4,132 citations and
5,889 attempts with clean integrity and foreign keys.

Batches 443-445 remain in open, mergeable PR 198 with successful Test run
34354744527. Batch 446 remains in open, mergeable PR 199 with successful Test
run 34361660741. Batch 447 remains in open, mergeable PR 200 with successful
Test run 34368546155. Their required merge order is PR 198, PR 199, then PR 200.
Batches 448-462 are complete local release candidates layered after PR 200. A
fresh live-data request confirms that the public site still serves Batch 442
data: 4,196 research-attempted people, 222 verified employers and 505 verified
affiliations. External publication requires explicit authorization for the PR
chain; the prior push was stopped by the privacy safety gate because this branch
contains private research material. Each later release must pass independent
Test, Pages deployment and pinned-live verification before being called
deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-10_batch462.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-one-john-e-cook-through-adelaide-l-cooke-pathways_batch-462_2026-09-10.json
    python3 -m oss_research export-derived
    python3 -m oss_research export-review-queue
    python3 -m oss_research coverage-report
    python3 -m oss_research build-public-data
    python3 -m oss_research audit-profiles --sample-size 200
    cd site
    PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
    caffeinate -dimsu npx playwright test --project=desktop --project=phone --project=tablet
    npm run check:links

Batch 463 resumes with PDF page 91 rows 24-33: Elizabeth M Cooke, Margauerite
Cooke, Mary Cooke, Raymond F Cooke, Frederick Cookson, Nick R Cooky, Francis J
Cooley, James Cooley, Margaret A Cooley and Marion L Cooley.
