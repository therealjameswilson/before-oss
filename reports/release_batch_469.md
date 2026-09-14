# Batch 469 release verification

2026-09-11 UTC. **Local release candidate; historical, data, build, privacy,
link, reproducibility, accessibility and complete three-viewport browser QA
passed. Independent release checks remain pending.** This release covers PDF
page 92 rows 38-46, Joseph D Coppock through Dolly O Corbin, and page 93 row 1,
Robert C Corbin. The cohort crosses the Box 143-to-144 boundary at location
230/86/29/02.

## Research

Pages 92 and 93 were rendered at 150 dpi and every printed field in the ten-row
cohort was visually compared with the immutable database. All ten rank cells are
blank. Two eight-digit identifiers, one seven-digit identifier and one six-digit
identifier remain literal only in private research data. The shorter values are
not padded or assigned to a service-number system. All ten rows remain separate
source records and person entities.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Stephen J Coraleski's exact
identifier and name select one Army row, dated 3 September 1942 as a private.
Robert C Corbin's exact identifier and name select one Army row, dated 19
February 1943 as a private. Four other Robert C Corbin rows carry different
identifiers and remain unassigned.

The official code list was downloaded at 29,870,215 bytes and SHA-256
`5197b7d45d609012ee489f3d8fb8447b0f7a112f36cc2c5b020a64c9a10222a2`.
Physical page 175 defines Coraleski's value `6-67` as `Buffers, polishers,
filers, and grinders (metal)`; physical page 186 defines Corbin's value `0-18`
as `Engineers, industrial`. Both categories are published as medium-confidence,
date-bounded occupation observations without an employer, workplace, exact job
title or Army-to-OSS sequence.

The six- and seven-digit values printed for George C Corbett Jr. and John M
Corbett are not padded. The Army file supplies no exact-name match for either.
One exact-name Dorothy L Corbett row is a name-only women's-service candidate,
and two exact-name John M Corbett rows are distinct name-only candidates. None
receives Army facts without a unique identifier or second corroborating bridge.
The file contains no exact-name row for Joseph D Coppock, Eugene P Corbets,
Chesley S Corbett, Emory T Corbett or Dolly O Corbin. Nonappearance is not
negative proof and is not presented that way.

The Harry S. Truman Presidential Library's first-person Joseph D. Coppock oral
history provides a direct identity and chronology bridge. Coppock says that he
headed the Office of Price Administration's Chemicals and Drugs Branch in 1943,
remained through the fall, and went to OSS in late 1943, initially as a
civilian. He says OSS arranged an early-1944 naval commission as lieutenant
junior grade. The OPA role is therefore the confirmed explicit immediate
pre-OSS government assignment. The naval classification is later documented
status; it is not inferred from the index's blank rank cell.

The Truman Library finding aid independently documents Coppock's 1941 U.S.
Department of Agriculture work, 1942 War Production Board special-assistant
role, and 1943 OPA work. His signed 1940 NBER acknowledgment was downloaded at
216,745 bytes and SHA-256
`128052745df1d427fca184a94c676c6a2f378f8f9f7d52a5c96f7a437e76ea92` and
visually inspected at physical page 15, printed page xii. It documents leave
from Swarthmore College, work on the National Bureau of Economic Research's
Financial Research Staff, and a University of California affiliation.
Swarthmore and NBER are published as earlier employment; the University of
California remains a professional affiliation because the source states no
role. The concurrent relationships do not support choosing a single last
civilian employer before government service.

The person-profile fallback now states this distinction directly when a
profile has documented earlier employment but no supportable single last
civilian employer. It no longer suggests that no employer evidence exists.
Legacy regression coverage was retained with explicitly scoped wording.

The CIA adapter completed one bounded exact-name search for each person and
returned no candidates. The Library of Congress adapter completed one bounded
employment-focused search per person. Nine returned no candidates. John M
Corbett returned five Union Times pages; page-level OCR shows that every item
concerns `JOHN J. CORBETT PRESS`, not John M Corbett. None supplies the printed
identifier, OSS, occupation or Box 143 bridge, and the 1947 item is postwar.
All five are rejected with item-specific reasons in the decision ledger.

The reviewed bundle contributes seven citation records, eight affiliations,
eleven claims with twenty-six source links, ten person updates and ten saved
reviewed research attempts. Six organization definitions appear in the bundle;
two are new to the cumulative database. The CIA and Library of Congress work
adds twenty adapter attempts, so the batch adds thirty attempts overall:
twenty-four no-result checks, three source reviews, two candidate rejections and
one candidate-finding event. Repeated decision, evidence and adapter-checkpoint
imports are idempotent. No authenticated NARA Catalog API request was made. All
seven official Batch 469 citation destinations returned HTTP 200 during the
release probe. See `research/batch-469-discovery-checkpoint.md` for private
identifiers, complete candidate adjudications and person-specific next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,460 / 23,940 active people | 18.6299% |
| Verified-employer coverage | 231 / 23,940 active people | 0.9649% |
| Verified-affiliation coverage | 521 / 23,940 active people | 2.1763% |
| Archival disposition assessed | 4,415 / 23,940 active people | 18.4419% |

There are 23,941 stored entities and one superseded entity; 236 possible
duplicate groups remain visible. Officer classification: 2,245 commissioned,
5,780 not commissioned and 15,915 indeterminate. Identity: 875 confirmed, 643
high confidence, 143 probable, 146 ambiguous, 89 conflicting and 22,044
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,480 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 199 |
| needs_temporal_review | 14 |
| verified_employer_found | 217 |
| documented_prewar_employer_found | 87 |
| occupation_only_found | 796 |
| conflicting_sources | 88 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,795 |
| completed | 131 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,059 | 35 |
| high | 1,326 | 303 |
| medium | 1,042 | 99 |
| low | 101 | 1 |
| conflicting | 100 | 2 |

Personnel categories: 1,505 civilian professional or administrative; 2,116
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
88 commissioned naval; 4,100 enlisted Army; 6 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,788 unknown or indeterminate.

Inventory: 562 organizations, 1,762 affiliations, 3,628 claims, 8,488
claim-source links, 4,179 citation records and 6,095 attempts/plans. Attempt
outcomes are 1,964 source reviewed, 276 candidate found, 756 candidate rejected,
2,511 no result and 588 planned. There are 1,920 unique source-document keys,
1,420 distinct stable URLs, 93 person-level conflicts and 4,179 citations. The
unresolved export has 22,709 data rows; the pull list 23,761; and the review
queue 23,940.

Public projection: 23,940 people, 550 organizations, 1,751 affiliations, 3,524
published, qualified or conflict-visible claims, 3,016 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 550 organization
rows, 1,751 affiliation rows and 3,016 citation rows.

## Local QA and resume

SQLite `quick_check` returns `ok`, foreign keys pass, all 93 Python unit tests
pass, and the locked npm dependency audit reports zero vulnerabilities. Ingest
validation confirms 23,978 rows, all 522 pages and all 32 parser-warning rows
resolved. The deterministic 200-profile structural audit passes; it is not an
independent historical rereview, and the women stratum remains unavailable
without sourced classification.

The Pages-configuration build reports 93 Astro source files with zero errors,
warnings or hints and generates 24,498 HTML pages / 24,570 artifacts. All
internal links resolve; 49,728 external destinations are inventoried, not all
visited. The focused Batch 469 browser suite passes all twelve checks across
desktop, phone and tablet. The complete browser/accessibility matrix passes
848 / 848 checks in each project, for 2,544 / 2,544 passing checks in 25.9
minutes. No assertion, content, responsive-layout, accessibility or data-product
failure remains. The focused suite also passes 12 / 12 after the clean replay.

Identifier audits cover all 24,570 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers and 120 formatted variants. There are
1,095 built-tree and 665 public-tree candidate substring coincidences, with
zero unexpected boundary, aggregate or manifest-size matches. Only
`.env.example` is tracked, and generated public assets contain no full service
identifiers.

The public manifest contains 67 assets / 88,145,374 bytes and has SHA-256
`35b5bb19b1b3c98c3f6b3a1c68caf9781c21786c36607d65bc8da2002b36f9ab`.
The deterministic public-tree digest covers 70 files / 90,492,503 bytes at
SHA-256
`2ef0db5800f979b787fc4b6a90e4226e879be68a6815df9131d581766dad8536`;
the Pages-configured 24,570-file / 276,507,553-byte production tree is
`aeb3fd64d81e309dcbcca77e85d867763259a06b4e5980dd4255290dcb73f54a`.
A complete fresh-database frozen-input replay reproduced both tree digests, the
manifest digest, every byte total and every file count exactly. The replay
database independently produced 23,978 source rows, 23,941 stored entities,
562 organizations, 1,762 affiliations, 3,628 claims, 8,488 claim-source links,
4,179 citations and 6,095 attempts with clean integrity and foreign keys.

Batches 448-469 are complete local release candidates layered after the
previously reviewed PR chain. An unauthenticated live-data request on 2026-09-11
confirms that the public site still serves the earlier dataset: 4,196
research-attempted people, 222 verified employers and 505 verified affiliations,
generated 2026-09-09. External publication requires explicit authorization and
independent Test, Pages deployment and pinned-live verification before any
later batch is called deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-11_batch469.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-two-joseph-d-coppock-through-page-ninety-three-robert-c-corbin-pathways_batch-469_2026-09-11.json
    python3 -m oss_research export-derived
    python3 -m oss_research export-review-queue
    python3 -m oss_research coverage-report
    python3 -m oss_research build-public-data
    python3 -m oss_research audit-profiles --sample-size 200
    cd site
    PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
    npx playwright test --project=desktop --project=phone --project=tablet
    npm run check:links

Authenticated NARA Catalog work remains fail-closed until the exposed key is
rotated and supplied outside chat. No key, raw NARA API payload, full service
identifier or private discovery note is present in public assets. The next
bounded cohort begins at PDF page 93 row 2, Pauline Corbitt.
