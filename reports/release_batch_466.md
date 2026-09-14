# Batch 466 release verification

2026-09-11 UTC. **Local release candidate; historical, data, build, privacy,
link, reproducibility, accessibility and complete three-viewport browser QA
passed. Independent release checks remain pending.** This release covers PDF
page 92 rows 8-17, Eli M Cooper through Leslie T Cooper, in Boxes 142-143 at
locations 230/86/29/02.

## Research

Page 92 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. All ten rank cells are blank
and remain blank. Seven private identifiers remain literal only in the private
database and checkpoint. All ten rows remain separate source records and person
entities.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Six printed identifiers select
exact-name rows: Eli M Cooper, Howard E Cooper, Irvin E Cooper, Irving Cooper,
John R Cooper and Leslie T Cooper. Herbert W Cooper's identifier selects a
damaged alternate-card row whose name field reads `COOPER HERBERT W LRD`; the
core name and identifier agree, but the damaged name, grade and branch fields
remain explicit warnings.

The official records date Army entry and preserve civilian-occupation codes.
The published, qualified results are: accountants and auditors for Eli at his
31 July 1942 entry; a broad metal-products-fabrication occupation for Herbert at
his 3 December 1942 entry; blaster or powderman for Howard at his 21 August 1941
entry; retail manager for Irving at his 20 August 1942 entry; student for John
at his 22 March 1943 entry; and a broad automobile-manufacturing occupation for
Leslie at his 8 May 1941 entry. These are occupations or student status, not
named employers or demonstrated immediate OSS predecessors. Irvin's 29 October
1942 row carries code 999, which the project cannot defensibly interpret and
therefore withholds.

Eli, Howard, Irvin, Irving and Leslie are classified as enlisted Army personnel
from the private-grade evidence. Herbert and John remain personnel-category
indeterminate because their grade fields are damaged and are not silently
repaired. Six identities are confirmed; Herbert's is high confidence because
of the damaged-card warning. Elizabeth J Cooper, Felix Cooper and Kenneth H
Cooper remain ambiguous.

The full exact-name search found one Elizabeth J Army/WAC candidate and one
Kenneth H Army candidate, but neither indexed row has a printed identifier or a
second bridge. The distinctive Felix Cooper rodeo candidate is supported by a
1940 *Tacoma Times* item and the National Cowboy & Western Heritage Museum, but
the index supplies no middle name, identifier, rank or public OSS bridge. All
three candidates remain low-confidence identity leads and none of their facts
is assigned to the indexed people pending archival review.

The CIA adapter completed one bounded public exact-name search per person and
returned no candidates. The Library of Congress adapter completed one bounded
exact-name employment search per person and returned seventeen candidates.
Every page-level result was inspected and rejected for publication with a
person-specific reason. The strongest withheld lead is a 25 February 1943
*Miami Citizen* item naming a John R. Cooper discharged by Miami Shipbuilding
Corporation twenty-five days before the identifier-matched Army entry. The
common name has no identifier, OSS reference, Box 143 link or second
corroborating fact, so Miami Shipbuilding is not published as his employer.

The reviewed bundle adds seven citation records, six affiliations, seventeen
claims with forty-nine source links, ten person updates and ten saved reviewed
research attempts. The decision ledger records all seventeen newspaper
adjudications. Repeated decision, evidence and adapter-checkpoint imports were
idempotent. No authenticated NARA Catalog API request was made. See
`research/batch-466-discovery-checkpoint.md` for private identifiers, complete
candidate adjudications and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,432 / 23,940 active people | 18.5129% |
| Verified-employer coverage | 230 / 23,940 active people | 0.9607% |
| Verified-affiliation coverage | 519 / 23,940 active people | 2.1679% |
| Archival disposition assessed | 4,387 / 23,940 active people | 18.3250% |

There are 23,941 stored entities and one superseded entity; 236 possible
duplicate groups remain visible. Officer classification: 2,244 commissioned,
5,773 not commissioned and 15,923 indeterminate. Identity: 867 confirmed, 643
high confidence, 143 probable, 146 ambiguous, 87 conflicting and 22,054
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,508 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 199 |
| needs_temporal_review | 14 |
| verified_employer_found | 217 |
| documented_prewar_employer_found | 86 |
| occupation_only_found | 791 |
| conflicting_sources | 86 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,775 |
| completed | 131 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,050 | 35 |
| high | 1,320 | 301 |
| medium | 1,036 | 99 |
| low | 101 | 1 |
| conflicting | 98 | 2 |

Personnel categories: 1,505 civilian professional or administrative; 2,116
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
87 commissioned naval; 4,093 enlisted Army; 6 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,796 unknown or indeterminate.

Inventory: 560 organizations, 1,749 affiliations, 3,605 claims, 8,424
claim-source links, 4,162 citation records and 6,009 attempts/plans. Attempt
outcomes are 1,954 source reviewed, 268 candidate found, 746 candidate rejected,
2,453 no result and 588 planned. There are 1,915 provisional source-document
keys, 1,416 distinct stable URLs, 91 person-level conflicts and 4,162 citations.
The unresolved export has 22,715 data rows; the pull list 23,761; and the review
queue 23,940.

Public projection: 23,940 people, 548 organizations, 1,738 affiliations, 3,501
published, qualified or conflict-visible claims, 2,999 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 548
organization rows, 1,738 affiliation rows and 2,999 citation rows.

## Local QA and resume

SQLite `quick_check` returns `ok`, foreign keys pass, all 93 Python unit tests
pass, and `npm audit` reports zero vulnerabilities. The deterministic
200-profile structural audit passes; it is not independent historical rereview,
and the women stratum remains unavailable without sourced classification.

The Pages-configuration build reports 90 Astro files with zero errors, warnings
or hints and generates 24,496 HTML pages / 24,568 artifacts. All internal links
resolve; 49,722 external destinations are inventoried, not all visited. Five of
the seven Batch 466 citation destinations returned HTTP 200 during the release
probe. The two Library of Congress resource pages returned HTTP 403 to the
command-line probe even with a descriptive User-Agent; both had been retrieved
and inspected during research. This is recorded as an access-control exception,
not a claim that either item is missing.

The focused Batch 466 browser suite passes all twelve checks across desktop,
phone and tablet. The complete browser/accessibility matrix passes 836 / 836
checks in each project, for 2,508 / 2,508 passing checks in 18.3 minutes. No
assertion, content, responsive-layout, accessibility or data-product failure
remains. The focused suite also passes 12 / 12 after the clean replay. Its first
sandboxed attempt could not bind the local preview port (`EPERM`); the permitted
local-only retry passed and this was not a product failure.

Identifier audits cover all 24,568 built artifacts and all 70 public-tree files,
12,926 normalized identifiers and 120 formatted variants. There are 1,095
built-tree and 665 public-tree candidate substring coincidences, with zero
unexpected boundary, aggregate or manifest-size matches. Only `.env.example`
is tracked, and generated public assets contain no full service identifiers.

The public manifest contains 67 assets / 87,920,413 bytes and has SHA-256
`a31358acd773dc90b5585d367f51868b17edeec693f39f74a4342b17895dca39`.
The deterministic public-tree digest covers 70 files / 90,267,543 bytes at
SHA-256
`18846abd4ce9da2691b4fc1e924cc969321d1137e5ded8cf8765a4db3611f836`;
the Pages-configured 24,568-file / 277,424,195-byte production tree is
`960c521d73550a750f01089bf5f70dee9bccfecd5d2a3dff1f014b7cea7ac7fc`.
A complete fresh-database frozen-input replay reproduced both tree digests, the
manifest digest, every byte total and every file count exactly. The replay
database independently produced 23,978 source rows, 23,941 stored entities,
1,749 affiliations, 3,605 claims, 8,424 claim-source links, 4,162 citations and
6,009 attempts with clean integrity and foreign keys.

Batches 443-445 remain in open, mergeable PR 198 with successful Test run
34354744527. Batch 446 remains in open, mergeable PR 199 with successful Test
run 34361660741. Batch 447 remains in open, mergeable PR 200 with successful
Test run 34368546155. Their required merge order is PR 198, PR 199, then PR 200.
Batches 448-466 are complete local release candidates layered after PR 200.
An unauthenticated live-data request on 2026-09-11 confirms that the public site
still serves Batch 442 data: 4,196 research-attempted people, 222 verified
employers and 505 verified affiliations.
External publication requires explicit authorization for the PR chain; the
prior push was stopped by the privacy safety gate because this branch contains
private research material. Each later release must pass independent Test,
Pages deployment and pinned-live verification before being called deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-10_batch466.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-two-eli-m-cooper-through-leslie-t-cooper-pathways_batch-466_2026-09-11.json
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
bounded cohort begins at PDF page 92 row 18.
