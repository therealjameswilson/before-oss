# Batch 470 release verification

2026-09-11 UTC. **Local release candidate; historical, data, build, privacy,
link, reproducibility, accessibility and complete three-viewport browser QA
passed. Independent release checks remain pending.** This release covers PDF
page 93 rows 2-11, Pauline Corbitt through Sidney A Corderman, in Box 144 at
location 230/86/29/02.

## Research

PDF page 93 was rendered at 150 dpi and every printed field in the ten-row
cohort was visually compared with the immutable database. The first row is
Pauline Corbitt; the earlier Batch 469 handoff's reference to a nonexistent
Dorothy H Corbin was corrected in that private checkpoint and release report.
Five rows contain eight- or nine-digit identifiers, one contains an
`RA`-prefixed identifier, and one contains a seven-digit identifier. They remain
literal only in private research data. Short and prefixed forms were compared
without padding or assigning them to an undocumented identifier system. All ten
rows remain separate source records and person entities.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Exact name-and-identifier
matches establish three Army entries: Herman L Corcoran on 11 January 1941,
Nicholas Cordas on 9 December 1942, and Sidney A Corderman on 11 January 1944.
Each entered as a private. Herman's occupation value is the withheld `999`
category and is not interpreted.

The official occupation list was rendered and visually inspected. Physical
page 173 defines Nicholas Cordas's `4-12` value as the skilled level of
`Occupations in manufacture of tobacco products`; physical page 304 defines
Sidney A Corderman's `9-92` value as `Students`. The former is published as a
medium-confidence, date-bounded occupation observation. Neither code names an
employer, workplace, school or OSS-entry date.

The Army file has one exact-name Roy E Corbitt row dated 25 October 1945, after
OSS was dissolved, with no matching literal identifier. Its facts are not
transferred. Two Charles R Corcoran rows carry different identifiers, residence
codes, birth years, branches and entry dates. The file supplies no exact-name
row for Pauline Corbitt, Georges Cordeau, Janet E Cordell, Robert W Cordell or
the no-middle-initial Sidney Corderman. Nonappearance is not negative proof:
the merged file is incomplete and is not a comprehensive OSS, officer, Navy,
Marine Corps, women's-service or foreign-personnel roster.

McIntosh Laboratory's institutional memorial states that Sidney Corderman
joined OSS in 1942 at age sixteen, remained in high school while continuing OSS
work, was drafted at eighteen, and continued in an OSS communications
laboratory as an Army technician. The independently matching Army row dates his
Army entry to 11 January 1944, records a 1925 birth-year code, and classifies
him as a student. Together these sources confirm the indexed Sidney A
Corderman and support high-school student status as his immediate pre-OSS
affiliation. The school is unnamed, and student status is not employment.

The adjacent no-middle-initial Sidney Corderman row remains a separate person.
The exact base name, adjacent placement and shared Box 144 make duplication
plausible, but they do not authorize a merge. Both profiles expose the same new
possible-duplicate group; the unnumbered row requires critical archival review,
and none of Sidney A Corderman's Army or student facts is transferred to it.

The OSS index prints Georges Cordeau as `S/Lt` with the note `French`. The
project preserves that abbreviation without expanding it and classifies him as
foreign or Allied military personnel while leaving commissioned status
indeterminate. The French Service historique de la Defense finding aid was
verified at 3,181,430 bytes and SHA-256
`042f2062b0deec40860d9c183f10069dff27e5e01620e733814da4796adaebfe`.
Physical page 237 lists his individual file `GR 28 P 4 175 / 187`, dated
1943-1982, and related resistance file `GR 16 P 142178`. A source-referenced but
explicitly tentative secondary register connects the same files to the
Proust/OSS/Midiron `Conge` wireless mission and the aliases George Courtois and
Cottard. This supports a high-confidence identity, not a confirmed one, and no
pre-OSS employer or predecessor affiliation is claimed.

The CIA adapter completed one bounded exact-name search for each person and
returned no candidates. The Library of Congress adapter completed one bounded
employment-focused search per person. Nine returned no candidates. Charles R
Corcoran returned two *Evening Star* pages, but page-level OCR identifies
Charles E. Corcoran in 1939 and Father Charles J. Corcoran in 1946. Both lack
the middle-initial and Box 144 bridge; the second is also postwar. Both are
rejected with item-specific reasons in the review ledger.

The reviewed bundle contributes seven citation records, two affiliations, six
claims with eighteen source links, ten person updates and ten saved reviewed
research attempts. No organization definition was needed. CIA and Library of
Congress work contributes twenty adapter attempts, so the batch adds thirty
attempts overall: nineteen no-result checks, eight source reviews, two
candidate-finding events and one candidate rejection. Repeated decision,
evidence and adapter-checkpoint imports are idempotent. No authenticated NARA
Catalog API request was made. See
`research/batch-470-discovery-checkpoint.md` for identifier-class notes, full
candidate adjudications and person-specific archival next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,470 / 23,940 active people | 18.6717% |
| Verified-employer coverage | 231 / 23,940 active people | 0.9649% |
| Verified-affiliation coverage | 522 / 23,940 active people | 2.1805% |
| Archival disposition assessed | 4,425 / 23,940 active people | 18.4837% |

There are 23,941 stored entities and one superseded entity; 237 possible
duplicate groups remain visible. Officer classification: 2,245 commissioned,
5,783 not commissioned and 15,912 indeterminate. Identity: 878 confirmed, 644
high confidence, 143 probable, 147 ambiguous, 89 conflicting and 22,039
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,470 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 199 |
| needs_temporal_review | 14 |
| verified_employer_found | 217 |
| documented_prewar_employer_found | 87 |
| occupation_only_found | 797 |
| conflicting_sources | 88 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,803 |
| completed | 132 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,062 | 35 |
| high | 1,328 | 303 |
| medium | 1,043 | 99 |
| low | 101 | 1 |
| conflicting | 100 | 2 |

Personnel categories: 1,505 civilian professional or administrative; 2,116
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
88 commissioned naval; 4,103 enlisted Army; 6 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,785 unknown or indeterminate.

Inventory: 562 organizations, 1,764 affiliations, 3,634 claims, 8,506
claim-source links, 4,186 citation records and 6,125 attempts/plans. Attempt
outcomes are 1,972 source reviewed, 278 candidate found, 757 candidate rejected,
2,530 no result and 588 planned. There are 1,922 unique source-document keys,
1,421 distinct stable URLs, 93 person-level conflicts and 4,186 citations. The
unresolved export has 22,707 data rows; the pull list 23,761; and the review
queue 23,940.

Public projection: 23,940 people, 550 organizations, 1,753 affiliations, 3,530
published, qualified or conflict-visible claims, 3,023 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 550 organization
rows, 1,753 affiliation rows and 3,023 citation rows.

## Local QA and resume

SQLite `integrity_check` returns `ok`, foreign keys pass, all 93 Python unit
tests pass, and the locked npm dependency audit reports zero vulnerabilities.
Ingest validation confirms 23,978 rows, all 522 pages and all 32 parser-warning
rows resolved. The deterministic 200-profile structural audit passes; it is not
an independent historical rereview, and the women stratum remains unavailable
without sourced classification.

The Pages-configuration build reports 94 Astro source files with zero errors,
warnings or hints and generates 24,498 HTML pages / 24,570 artifacts. All
internal links resolve; 49,729 external destinations are inventoried, not all
visited. The focused Batch 470 browser suite passes all twelve checks across
desktop, phone and tablet. The complete browser/accessibility matrix passes 852
/ 852 checks in each project, for 2,556 / 2,556 passing checks in 26.0 minutes.
No assertion, content, responsive-layout, accessibility or data-product failure
remains. The focused suite also passes 12 / 12 after the clean replay.

One earlier non-authoritative full-suite attempt executed all 2,556 assertions
without a test failure, then the Node process exited with status 134 while a
concurrent public-data regeneration caused the preview server to rebuild during
cleanup. The authoritative run above was isolated from all writes, used an
8 GiB Node heap limit, and exited zero. The resource incident is not counted as
a passing run and did not alter the clean result.

Identifier audits cover all 24,570 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers and 120 formatted variants. There are
1,093 built-tree and 663 public-tree candidate substring coincidences, with
zero unexpected boundary, aggregate or manifest-size matches. Only
`.env.example` is tracked, and generated public assets contain no full service
identifiers.

The separate public-repository audit finds no new literal identifier in the
Batch 470 checkpoint after redaction. It also finds 95 pre-existing boundary
matches across older tracked research checkpoints and parser/review fixtures.
Those materials are not shipped in the site or downloads, and many reproduce
fields from the official public index, but the repository is public; describing
them as private would be inaccurate. Moving sensitive literal values into an
ignored or access-controlled research package remains a methodological privacy
cleanup item for a later compatibility-preserving migration.

The public manifest contains 67 assets / 88,203,066 bytes and has SHA-256
`63fd7f2be9729b1f45be815e32b5de6779971d48bd20876cbc7d9148de0e32b3`.
The deterministic public-tree digest covers 70 files / 90,550,191 bytes at
SHA-256
`95a9b11791462a03b5890fd87bc0e4f20d7ae87ba8ede6eaecdbd53f12f704ba`;
the Pages-configured 24,570-file / 276,591,990-byte production tree is
`1f1e310aed40b0b2bcabc9e3f7fa1dd8fd06f20c34bb71545a5b68dc22522d91`.
A complete fresh-database frozen-input replay reproduced both tree digests, the
manifest digest, every byte total and every file count exactly. The replay
database independently produced 23,978 source rows, 23,941 stored entities,
562 organizations, 1,764 affiliations, 3,634 claims, 8,506 claim-source links,
4,186 citations and 6,125 attempts with clean integrity and foreign keys.

Batches 448-470 are complete local release candidates layered after the
previously reviewed PR chain. The public site was last verified on 2026-09-11
as serving the earlier dataset: 4,196 research-attempted people, 222 verified
employers and 505 verified affiliations, generated 2026-09-09. External
publication requires explicit authorization and independent Test, Pages
deployment and pinned-live verification before any later batch is called
deployed.

Resume commands:

    python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
    python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-11_batch470.csv
    python3 -m oss_research import-reviewed-evidence research/evidence-page-ninety-three-pauline-corbitt-through-sidney-a-corderman-pathways_batch-470_2026-09-11.json
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
bounded cohort begins at PDF page 93 row 12, Ismael Cordero.
