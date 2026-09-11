# Batch 467 release verification

2026-09-11 UTC. **Local release candidate; historical, data, build, privacy,
link, reproducibility, accessibility and complete three-viewport browser QA
passed. Independent release checks remain pending.** This release covers PDF
page 92 rows 18-27, Nolan R Cooper through Elizabeth Copeland, all in Box 143
at location 230/86/29/02.

## Research

Page 92 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. All ten rank cells are blank
and remain blank. Six private identifiers remain literal only in the private
database and checkpoint. All ten rows remain separate source records and person
entities.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Three printed identifiers
select exact-name rows: Nolan R Cooper, Sidney H Cooper and William H Cooper
Jr. The official records date Army entry and preserve civilian-occupation
codes. The published, qualified results are a general-farm-hand category for
Nolan at his 3 February 1941 entry, a photographic-process category for Sidney
at his 17 August 1942 entry, and a broad chauffeur/driver category for William
at his 4 April 1941 entry. These are occupations, not named employers or
demonstrated immediate OSS predecessors.

An official NARA-hosted OSS order dated 2 May 1945 independently identifies
Technician Third Grade William H. Cooper, Jr., with the exact private identifier
printed in the index. This confirms William's indexed identity and enlisted
Army status but is during-service evidence; it does not establish his pre-OSS
employer or prove that the Army-entry occupation was immediately pre-OSS.

Arthur S Copeland's printed identifier instead selects an Army row named Paul
Wagner. The complete file contains two exact-name Arthur S Copeland rows, one
whose identifier differs by one digit and one with a substantially different
identifier. Neither is attached. Arthur remains a conflicting identity and a
critical Box 143 review case. The seven-digit values printed for Steven V Cope
and Charles H Copeland produced no literal file match; no prefix or padding
guess was used. Pauline F Cooper, Rollo W Cooper, Steven V Cope, A C Copeland,
Charles H Copeland and Elizabeth Copeland remain unresolved. Nonappearance in
the Army file is not negative proof and is not presented that way.

The CIA adapter completed one bounded public exact-name search per person and
returned no candidates. The Library of Congress adapter completed one bounded
employment-focused search per person and returned twelve candidates. Every
page-level result was inspected and rejected for publication with a
person-specific reason. The results concern conflicting middle initials or
first names, a product name, a forename collision, unrelated professors, or
exact-name social notices without an identifier, OSS, occupation, or Box 143
bridge. Exact-name web searches found no additional publishable identity or
employer bridge.

The reviewed bundle adds five citation records, three affiliations, seven
claims with twenty-two source links, ten person updates and ten saved reviewed
research attempts. The decision ledger records all twelve newspaper
adjudications. Repeated decision, evidence and adapter-checkpoint imports were
idempotent. No authenticated NARA Catalog API request was made. All five
official Batch 467 citation destinations returned HTTP 200 during the release
probe. See `research/batch-467-discovery-checkpoint.md` for private identifiers,
complete candidate adjudications and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,442 / 23,940 active people | 18.5547% |
| Verified-employer coverage | 230 / 23,940 active people | 0.9607% |
| Verified-affiliation coverage | 519 / 23,940 active people | 2.1679% |
| Archival disposition assessed | 4,397 / 23,940 active people | 18.3668% |

There are 23,941 stored entities and one superseded entity; 236 possible
duplicate groups remain visible. Officer classification: 2,244 commissioned,
5,776 not commissioned and 15,920 indeterminate. Identity: 870 confirmed, 643
high confidence, 143 probable, 146 ambiguous, 88 conflicting and 22,050
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,498 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 199 |
| needs_temporal_review | 14 |
| verified_employer_found | 217 |
| documented_prewar_employer_found | 86 |
| occupation_only_found | 794 |
| conflicting_sources | 87 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,781 |
| completed | 131 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,053 | 35 |
| high | 1,320 | 301 |
| medium | 1,039 | 99 |
| low | 101 | 1 |
| conflicting | 99 | 2 |

Personnel categories: 1,505 civilian professional or administrative; 2,116
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
87 commissioned naval; 4,096 enlisted Army; 6 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,793 unknown or indeterminate.

Inventory: 560 organizations, 1,752 affiliations, 3,612 claims, 8,446
claim-source links, 4,167 citation records and 6,039 attempts/plans. Attempt
outcomes are 1,957 source reviewed, 272 candidate found, 751 candidate rejected,
2,471 no result and 588 planned. There are 1,916 unique source-document keys,
1,416 distinct stable URLs, 92 person-level conflicts and 4,167 citations. The
unresolved export has 22,712 data rows; the pull list 23,761; and the review
queue 23,940.

Public projection: 23,940 people, 548 organizations, 1,741 affiliations, 3,508
published, qualified or conflict-visible claims, 3,004 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 548
organization rows, 1,741 affiliation rows and 3,004 citation rows.

## Local QA and resume

SQLite `quick_check` returns `ok`, foreign keys pass, all 93 Python unit tests
pass, and `npm audit` reports zero vulnerabilities. Ingest validation confirms
23,978 rows, all 522 pages and all 32 parser-warning rows resolved. The
deterministic 200-profile structural audit passes; it is not independent
historical rereview, and the women stratum remains unavailable without sourced
classification.

The Pages-configuration build reports 91 Astro source files with zero errors,
warnings or hints and generates 24,496 HTML pages / 24,568 artifacts. All
internal links resolve; 49,722 external destinations are inventoried, not all
visited. The focused Batch 467 browser suite passes all twelve checks across
desktop, phone and tablet. The complete browser/accessibility matrix passes 840
/ 840 checks in each project, for 2,520 / 2,520 passing checks in 20.4 minutes.
No assertion, content, responsive-layout, accessibility or data-product failure
remains. The focused suite also passes 12 / 12 after the clean replay. Its first
sandboxed attempt could not bind the local preview port (`EPERM`); the permitted
local-only retry passed and this was not a product failure.

Identifier audits cover all 24,568 built artifacts and all 70 public-tree files,
12,926 normalized identifiers and 120 formatted variants. There are 1,095
built-tree and 665 public-tree candidate substring coincidences, with zero
unexpected boundary, aggregate or manifest-size matches. Only `.env.example`
is tracked, and generated public assets contain no full service identifiers.

The public manifest contains 67 assets / 87,979,819 bytes and has SHA-256
`1f12920bf248b53855c391f263254914a62cf7eff85252903357c91a9044b1c1`.
The deterministic public-tree digest covers 70 files / 90,326,948 bytes at
SHA-256
`7e60bf8e606d8fe7576ea944935703b1939fb106381d7b41f6a7cd6c17dc1347`;
the Pages-configured 24,568-file / 277,512,482-byte production tree is
`2aabaf76212090e1893acf61b0779d6c8379a337859660a5ac965cb83f1d4737`.
A complete fresh-database frozen-input replay reproduced both tree digests, the
manifest digest, every byte total and every file count exactly. The replay
database independently produced 23,978 source rows, 23,941 stored entities,
1,752 affiliations, 3,612 claims, 8,446 claim-source links, 4,167 citations and
6,039 attempts with clean integrity and foreign keys.

Batches 448-467 are complete local release candidates layered after the
previously reviewed PR chain. An unauthenticated live-data request on
2026-09-11 confirms that the public site still serves Batch 442 data: 4,196
research-attempted people, 222 verified employers and 505 verified
affiliations. External publication requires explicit authorization and
independent Test, Pages deployment and pinned-live verification before any
later batch is called deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-11_batch467.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-two-nolan-r-cooper-through-elizabeth-copeland-pathways_batch-467_2026-09-11.json
    python3 -m oss_research export-derived
    python3 -m oss_research export-review-queue
    python3 -m oss_research coverage-report
    python3 -m oss_research build-public-data
    python3 -m oss_research audit-profiles --sample-size 200
    cd site
    PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
    caffeinate -dimsu npx playwright test --project=desktop --project=phone --project=tablet
    npm run check:links

Authenticated NARA Catalog work remains fail-closed until the exposed key is
rotated and supplied outside chat. No key, raw NARA API payload, full service
identifier or private discovery note is present in public assets. The next
bounded cohort begins at PDF page 92 row 28, James W Copeland, and continues
through row 37, John O Coppock.
