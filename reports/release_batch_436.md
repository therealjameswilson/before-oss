# Batch 436 release verification

2026-09-09 UTC. **Local release candidate; independent release checks
pending.** This report covers PDF page 85 rows 30-39, Nick J Cocoris through
Chester Cody, spanning Boxes 131-132 at location 230/86/28/07.

## Research

Page 85 was rendered at 150 dpi. Every printed name, initial, rank or blank,
private identifier or blank, box, note and location in the cohort was visually
matched to the immutable database before research. The page prints `Sgt` for
Chester Cody and no rank for the other nine people. Five private identifiers
remain research-only and are masked in every public artifact. Two identical
William S Codd rows and two Ernest J Codekas rows remain separate source rows
and separate person entities.

A complete transient scan of 9,200,232 fixed-width Army merged-file records
tested all five printed identifiers literally. Four exact identifier-and-name
matches resulted. Nick J Cocoris, Avery L Coddens, the identifier-bearing
Ernest J Codekas entity and George N Codino entered the Army as privates. Their
officially decoded categories are `General industry clerks`, `Students`,
`Foremen, manufacturing`, and `Chauffeurs and drivers, bus, taxi, truck, and
tractor`. Each is published as a medium-confidence, temporally uncertain
observation rather than a named employer or immediate predecessor. Student
status remains separate from employment.

Chester Cody's printed seven-digit identifier has no literal Army match. A
zero-prefixed exact-name row remains rejected because the project does not
silently pad or repair private identifiers. Two National Army Museum
descriptions independently place the exact name with Kachin Rangers and
American OSS operations in 1945. The uncommon name, indexed Sergeant rank and
wartime context support a high-confidence enlisted Army identity, but no
pre-OSS employer, occupation or Army-to-OSS chronology.

A scholarly review explicitly links John Insley Coddington to Harvard History
Department teaching from 1930 to 1936 and later service as an OSS Research
Specialist. A Georgia Historical Society finding aid independently identifies
him as a Harvard professor and later State Department worker. The rare full
name, middle initial, profession and explicit OSS title support a high-
confidence identity. Harvard is published at medium confidence as earlier
documented pre-OSS employment, not as the immediate affiliation or last
civilian employer, because later academic and government chronology remains
insufficiently dated.

The two William Codd rows remain separate unresolved entities in a visible
duplicate group. The Box 132 Ernest Codekas row receives the identifier-backed
Army facts; those facts are not copied to the adjacent no-identifier Box 131
entity. Eliot Codman remains unresolved after staged official, institutional,
newspaper, directory and archival discovery. All unresolved entities retain
public research-status pages and specific physical-file questions.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional archives, obituaries, directories,
newspapers, current Library of Congress discovery, official NARA context and
the complete Army comparison when applicable were recorded for every person.
Commercial people finders, sensitive living-person data, unsourced genealogy,
search snippets and name-only biographies were rejected as final evidence. No
authenticated NARA Catalog request was used.

The reviewed evidence bundle adds seven citations, one canonical organization,
five affiliations, eleven claims, thirty-one claim-source links, ten person
updates and ten saved research attempts. See
`research/batch-436-discovery-checkpoint.md` for the adjudication, rejected
leads, source cautions and next actions. All ten records remain on the archival
pull list. Research completion means a saved reviewable outcome, not that a
prior employer has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,138 / 23,940 active people | 17.2849% |
| Verified-employer coverage | 220 / 23,940 active people | 0.9190% |
| Verified-affiliation coverage | 502 / 23,940 active people | 2.0969% |
| Archival disposition assessed | 4,093 / 23,940 active people | 17.0969% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,238 commissioned,
5,686 noncommissioned and 16,016 indeterminate. Identity: 788 confirmed, 616
high confidence, 132 probable, 106 ambiguous, 79 conflicting and 22,219
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,802 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 142 |
| needs_temporal_review | 13 |
| verified_employer_found | 211 |
| documented_prewar_employer_found | 74 |
| occupation_only_found | 712 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,648 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 968 | 35 |
| high | 1,261 | 284 |
| medium | 925 | 84 |
| low | 96 | 1 |
| conflicting | 90 | 2 |

There are 3,970 citation records, 1,846 provisional document keys that are not
certified unique historical documents, and 1,352 distinct stable URLs.
Inventory: 535 organizations, 1,625 affiliations, 3,340 claims, 7,674 claim-
source links and 5,361 attempts/plans. Attempt outcomes: 1,830
`source_reviewed`, 200 `candidate_found`, 667 `candidate_rejected`, 2,077
`no_result` and 587 `planned`. There are 1,630 people with stored claims and
1,550 with public or conflict-visible claims. Composite unresolved export:
22,816 data rows plus header. Conflict union: 83. Pull list: 23,767 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 523 organizations, 1,614 affiliations, 3,241
published, qualified or conflict-visible claims, 2,814 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 523
organization rows, 1,614 affiliation rows and 2,814 citation rows.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduces the Batch 436 counts. SQLite `quick_check` returns
`ok`, foreign keys pass, and all 93 Python tests pass in 4.151 seconds. The
deterministic 200-profile structural audit passes; it is not independent
historical re-review, and the women stratum remains unavailable without
sourced classification.

The exact Pages-configuration build contains 24,471 HTML pages and 24,543
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,637 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,543 built artifacts, 12,926 normalized
identifiers, 120 formatted variants and 1,086 candidate substring coincidences
with zero unexpected boundary, aggregate or manifest-size matches. The same
audit over all 70 public-tree files finds 652 candidate coincidences and zero
unexpected matches. The focused Batch 436 browser suite passes all twelve
checks across desktop, phone and tablet in 7.1 seconds after the full replay.
The dependency audit reports zero vulnerabilities across 379 installed
dependency relationships.

The public manifest contains 67 assets / 85,502,384 bytes at SHA-256
`a533bd4da2f296e9e4844ac7c980245b3590fb5ba0d555ae290a7086e724d0fa`.
The deterministic public-tree digest covers 70 files / 87,849,513 bytes at
SHA-256
`0d3a8ac883f6cb0ec6e7a7ebbc0d914ed6bc6333416375c383a6158dc0805de2`;
the 24,543-file / 272,305,260-byte production tree is
`cea9eee061dba10a9a6e661abe85c936b4bbc804e94e859be9c02f650fb259e6`.
Two consecutive exact Pages-configuration builds reproduce both tree digests
and file counts.

Batches 433-435 passed their independent pull-request Test and merged as
`dbf7c9bc981fee5698bbaf7e4295cf26f09fbb9e`; their merge-triggered Test,
Pages deployment and pinned-live verification are still pending. Batch 436
requires its own independent pull-request Test, merge, deployment and pinned-
live verification before it is described as released.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-five-nick-j-cocoris-through-chester-cody-pathways_batch-436_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch436.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,802 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
