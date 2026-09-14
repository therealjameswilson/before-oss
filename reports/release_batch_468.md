# Batch 468 release verification

2026-09-11 UTC. **Local release candidate; historical, data, build, privacy,
link, reproducibility, accessibility and complete three-viewport browser QA
passed. Independent release checks remain pending.** This release covers PDF
page 92 rows 28-37, James W Copeland through John O Coppock, all in Box 143 at
location 230/86/29/02.

## Research

Page 92 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. James W Copeland's rank is
printed as `1st Lt`; the other nine rank cells are blank. Three private
identifiers remain literal only in the private database and checkpoint. The
printed spelling `Mortimemr Copeland` is preserved. `Mortimer` was tested only
as a search alias and is not presented as a correction. All ten rows remain
separate source records and person entities.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Millard A Copeland's exact
private identifier and name select one Army row, dated 16 July 1942 as a
private. The alternate-card civilian-occupation value `310` is not interpreted:
the inspected official code-list pages contain no corresponding `3-10` entry.
Millard is confirmed as enlisted Army personnel, but no Army-to-OSS chronology
or pre-OSS employer is inferred.

John O Coppock's exact private identifier and name select the sole exact-name
Army row, dated 10 August 1943 as a private. The official code list defines its
civilian-occupation entry `0-39` as `Professional occupations, n. e. c.`. That
broad, date-bounded occupation is published at medium claim confidence without
an employer. An official Truman Library finding aid independently documents
John O. Coppock as a War Production Board official in 1942 and lists his 1942
WPB report. The role is published as documented earlier government service,
not as an immediate pre-OSS affiliation or last civilian employer. Box 143 is
still required to establish the WPB-to-Army-to-OSS sequence.

Joe M Copeland's printed private identifier selects a different full name in
the Army file, which has no exact-name Joe M Copeland row. The unrelated name
and full identifier are withheld. Joe remains a visible identity conflict and
a critical Box 143 review case. Seven exact-name James W Copeland Army rows and
seven exact-name William Copeland rows cannot identify either index person by
name alone. Mortimemr Copeland, Oliver C Copeland, Virginia Copeland, William
Copeland and Ida L Coppa remain unresolved. James W Copeland retains the
commissioned Army classification established by the printed `1st Lt` rank.
Nonappearance in the Army file is not negative proof and is not presented that
way.

Miles A Copeland's existing high-confidence result was rechecked, not
duplicated: the official CIA biography supports his immediate U.S. Army
divisional Finance Office assignment before Donovan recruited him and an
earlier professional-jazz-musician occupation. No single bandleader or venue
is converted into an employer.

For the eight people who had not already received the current source checks,
the CIA adapter completed one bounded exact-name search per person and returned
no candidates. The Library of Congress adapter completed one bounded
employment-focused search per person and returned eight candidates: one for
James W Copeland, two for Virginia Copeland and five for William Copeland.
Every page-level OCR result was inspected and rejected with a person-specific
reason. The items concern a conflicting middle initial, an unrelated surviving
daughter, a punctuation collision, unrelated legal reports, a common-name
list, and a 1962 postwar union notice. None supplies an identifier, OSS, Box
143, occupation or employer bridge.

The reviewed bundle contributes five citation records, two affiliations, five
claims with sixteen source links, ten person updates and ten saved reviewed
research attempts. The decision ledger records all eight newspaper
adjudications. Together with the CIA and Library of Congress adapter work, the
batch adds twenty-six attempts. Repeated decision, evidence and adapter-
checkpoint imports were idempotent. No authenticated NARA Catalog API request
was made. All five official Batch 468 citation destinations returned HTTP 200
during the release probe. See `research/batch-468-discovery-checkpoint.md` for
private identifiers, complete candidate adjudications and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,450 / 23,940 active people | 18.5881% |
| Verified-employer coverage | 230 / 23,940 active people | 0.9607% |
| Verified-affiliation coverage | 520 / 23,940 active people | 2.1721% |
| Archival disposition assessed | 4,405 / 23,940 active people | 18.4002% |

There are 23,941 stored entities and one superseded entity; 236 possible
duplicate groups remain visible. Officer classification: 2,244 commissioned,
5,778 not commissioned and 15,918 indeterminate. Identity: 872 confirmed, 643
high confidence, 143 probable, 146 ambiguous, 89 conflicting and 22,047
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,490 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 199 |
| needs_temporal_review | 14 |
| verified_employer_found | 217 |
| documented_prewar_employer_found | 86 |
| occupation_only_found | 794 |
| conflicting_sources | 88 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,788 |
| completed | 131 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,055 | 35 |
| high | 1,321 | 301 |
| medium | 1,040 | 99 |
| low | 101 | 1 |
| conflicting | 100 | 2 |

Personnel categories: 1,505 civilian professional or administrative; 2,116
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
87 commissioned naval; 4,098 enlisted Army; 6 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,791 unknown or indeterminate.

Inventory: 560 organizations, 1,754 affiliations, 3,617 claims, 8,462
claim-source links, 4,172 citation records and 6,065 attempts/plans. Attempt
outcomes are 1,961 source reviewed, 275 candidate found, 754 candidate rejected,
2,487 no result and 588 planned. There are 1,917 unique source-document keys,
1,417 distinct stable URLs, 93 person-level conflicts and 4,172 citations. The
unresolved export has 22,712 data rows; the pull list 23,761; and the review
queue 23,940.

Public projection: 23,940 people, 548 organizations, 1,743 affiliations, 3,513
published, qualified or conflict-visible claims, 3,009 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 548
organization rows, 1,743 affiliation rows and 3,009 citation rows.

## Local QA and resume

SQLite `quick_check` returns `ok`, foreign keys pass, all 93 Python unit tests
pass, and `npm audit` reports zero vulnerabilities. Ingest validation confirms
23,978 rows, all 522 pages and all 32 parser-warning rows resolved. The
deterministic 200-profile structural audit passes; it is not independent
historical rereview, and the women stratum remains unavailable without sourced
classification.

The Pages-configuration build reports 92 Astro source files with zero errors,
warnings or hints and generates 24,496 HTML pages / 24,568 artifacts. All
internal links resolve; 49,723 external destinations are inventoried, not all
visited. The focused Batch 468 browser suite passes all twelve checks across
desktop, phone and tablet. The complete browser/accessibility matrix passes
844 / 844 checks in each project, for 2,532 / 2,532 passing checks in 20.7
minutes. No assertion, content, responsive-layout, accessibility or data-
product failure remains. The focused suite also passes 12 / 12 after the clean
replay.

Identifier audits cover all 24,568 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers and 120 formatted variants. There are
1,093 built-tree and 663 public-tree candidate substring coincidences, with
zero unexpected boundary, aggregate or manifest-size matches. Only
`.env.example` is tracked, and generated public assets contain no full service
identifiers.

The public manifest contains 67 assets / 88,034,364 bytes and has SHA-256
`9bda7672bae8b45af263b80e100f65e7bcd2725c97b546087dd093b6196ff8dd`.
The deterministic public-tree digest covers 70 files / 90,381,493 bytes at
SHA-256
`9297a2256641caca5167d43be742bd3f532fb9fafe1a677f4d4d5228ee0661cd`;
the Pages-configured 24,568-file / 277,590,634-byte production tree is
`8be93ff1c7bb5960cd46760a627c31e0186270df870b1854122829c1f526021d`.
A complete fresh-database frozen-input replay reproduced both tree digests,
the manifest digest, every byte total and every file count exactly. The replay
database independently produced 23,978 source rows, 23,941 stored entities,
1,754 affiliations, 3,617 claims, 8,462 claim-source links, 4,172 citations and
6,065 attempts with clean integrity and foreign keys.

Batches 448-468 are complete local release candidates layered after the
previously reviewed PR chain. An unauthenticated live-data request on
2026-09-11 confirms that the public site still serves the earlier dataset:
4,196 research-attempted people, 222 verified employers and 505 verified
affiliations. External publication requires explicit authorization and
independent Test, Pages deployment and pinned-live verification before any
later batch is called deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-11_batch468.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-two-james-w-copeland-through-john-o-coppock-pathways_batch-468_2026-09-11.json
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
bounded cohort begins at PDF page 92 row 38, Joseph D Coppock, continues
through row 46, and then crosses to page 93.
