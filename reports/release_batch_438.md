# Batch 438 release verification

2026-09-09 UTC. **Local release candidate; independent release checks
pending.** This report covers PDF page 86 rows 4-13, Mary M Coghlan through
Leonard Cohen, spanning Boxes 132-133 at location 230/86/28/07.

## Research

Page 86 was rendered at 150 dpi. Every printed name, initial, blank rank,
private identifier or blank, box, note and location in the cohort was visually
matched to the immutable database before research. Nine people print Box 132;
Leonard Cohen prints Box 133. All ten rows print no rank. Seven private
identifiers remain research-only and are masked in every public artifact.
Shared Cohen surnames are not treated as evidence of kinship, duplication or a
shared biography.

A complete transient scan of 9,200,232 fixed-width Army merged-file records
tested all seven printed identifiers literally. Thomas B Cogley, Colby A
Cogswell, Albert Cohen, Arthur A Cohen and Harry Cohen each have one exact
identifier-and-name match and entered the Army as privates. Their officially
decoded categories are, respectively, `Electrical machinery and accessories
manufacturing occupations, n.e.c.`, `Salesmen, stock and bond`, `Warehousing,
storekeeping, handling, loading, unloading, and related occupations, n.e.c.`,
`Foremen, n.e.c.`, and `Managers and officials, n.e.c.` Each is published as a
medium-confidence, temporally uncertain occupation observation rather than a
named employer or immediate predecessor.

Harold Cohen's and Leonard Cohen's printed identifiers have no literal Army
match. Dozens of exact-name Army candidates remain rejected because no printed
identifier, OSS file, branch or other corroborating bridge selects one. The
project does not silently pad, truncate or repair either printed identifier.

Dartmouth institutional sources establish the only documented employer pathway
in the cohort. An obituary supplies Colby Adams Cogswell's rare full name,
Dartmouth class and wartime OSS service in Paris. A contemporary March 1944 war
directory lists Colby A. Cogswell in the Army of the United States. A 1954
class notice, based on information from Northern Trust, says that he joined the
bank in 1949 after ten years with the First Boston Corporation. Read with his
official June 1943 Army-entry date, this supports First Boston as the best-
supported last civilian employer before wartime service. The retrospective
ten-year wording necessarily spans the wartime interruption and does not state
the precise leave or separation date. First Boston is therefore published at
medium confidence with `probable_immediate` temporal basis, not as an explicit
immediate pre-OSS affiliation and not in default high-confidence employer
analytics.

Cogswell's Dartmouth attendance remains a student relationship, not
employment. His Army record remains a military assignment, not a civilian
employer. His stock-and-bond category remains a separate occupation and is not
silently attached to First Boston. The official entry record establishes
private grade only at Army entry; the obituary's generic word `officer` is not
treated as proof of a military commission.

Mary M Coghlan, David C Cohen, Harold Cohen, Jean Cohen and Leonard Cohen remain
unresolved after staged official, institutional, newspaper, directory and
archival discovery. The younger writer Arthur Allen Cohen, the later Canadian
singer Leonard Cohen, an unbridged British military-intelligence Leonard Cohen
and a Harold Cohen associated with the 4th Armored Division remain rejected
namesakes. A Dartmouth registrar page presented an access challenge; it was not
used as evidence, and no access restriction was bypassed. All five unresolved
people retain public research-status pages and specific physical-file
questions.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional archives, obituaries, directories,
newspapers, current Library of Congress discovery, official NARA context and
the complete Army comparison when applicable were recorded for every person.
Commercial people finders, sensitive living-person data, unsourced genealogy,
search snippets and name-only biographies were rejected as final evidence. No
authenticated NARA Catalog request was used.

The reviewed evidence bundle adds seven citations, one new canonical
organization plus two references to existing organizations, eight
affiliations, thirteen claims, thirty-nine claim-source links, ten person
updates and ten saved research attempts. See
`research/batch-438-discovery-checkpoint.md` for the adjudication, rejected
leads, source cautions and next actions. All ten records remain on the archival
pull list. Research completion means a saved reviewable outcome, not that a
prior employer has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,158 / 23,940 active people | 17.3684% |
| Verified-employer coverage | 221 / 23,940 active people | 0.9231% |
| Verified-affiliation coverage | 504 / 23,940 active people | 2.1053% |
| Archival disposition assessed | 4,113 / 23,940 active people | 17.1805% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,238 commissioned,
5,695 noncommissioned and 16,007 indeterminate. Identity: 795 confirmed, 618
high confidence, 133 probable, 106 ambiguous, 79 conflicting and 22,209
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,782 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 142 |
| needs_temporal_review | 13 |
| verified_employer_found | 212 |
| documented_prewar_employer_found | 76 |
| occupation_only_found | 718 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,659 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 975 | 35 |
| high | 1,267 | 286 |
| medium | 934 | 86 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

There are 3,984 citation records, 1,852 provisional document keys that are not
certified unique historical documents, and 1,358 distinct stable URLs.
Inventory: 536 organizations, 1,637 affiliations, 3,363 claims, 7,736 claim-
source links and 5,381 attempts/plans. Attempt outcomes: 1,839
`source_reviewed`, 201 `candidate_found`, 675 `candidate_rejected`, 2,079
`no_result` and 587 `planned`. There are 1,640 people with stored claims and
1,559 with public or conflict-visible claims. Composite unresolved export:
22,807 data rows plus header. Conflict count: 83. Pull list: 23,766 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 524 organizations, 1,626 affiliations, 3,263
published, qualified or conflict-visible claims, 2,827 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 524
organization rows, 1,626 affiliation rows and 2,827 citation rows.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A fresh replay into a new SQLite database from the frozen 522-page
PDF and every reviewed evidence bundle reproduces the Batch 438 counts. SQLite
`quick_check` returns `ok`, foreign keys pass, and all 93 Python tests pass in
4.498 seconds. The deterministic 200-profile structural audit passes; it is not
independent historical re-review, and the women stratum remains unavailable
without sourced classification.

The exact Pages-configuration build contains 24,472 HTML pages and 24,544
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,643 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,544 built artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,084 candidate substring coincidences with zero
unexpected boundary, aggregate or manifest-size matches. The same audit over
all 70 public-tree files finds 654 candidate coincidences and zero unexpected
matches. The focused Batch 438 browser suite passes all twelve checks across
desktop, phone and tablet in 7.3 seconds after the fresh replay. The dependency
audit reports zero vulnerabilities across 379 installed dependency
relationships.

The public manifest contains 67 assets / 85,718,020 bytes at SHA-256
`096e2a33a52936c64868cb9fe38a8526e6bad7cf08021ea35a23cdd5c7ffa1b0`.
The deterministic public-tree digest covers 70 files / 88,065,148 bytes at
SHA-256
`8c8bcea433184345a01e6c98380ff12a647dcb42b17b740786e97d9ae730fae9`;
the 24,544-file / 272,617,455-byte production tree is
`c9540372467327125f00424395366e5878c527a616731b12067f488f08d5f38d`.
Two consecutive exact Pages-configuration builds reproduce both tree digests
and file counts.

Batch 437 passed independent pull-request Test `34314054523`, merged to
`main` as `74a437e0826b3a95ee677a9c82d61afe2c574d83`, deployed through Pages run
`34317209870`, and passed pinned-live verification against immutable commit
`7bc35220f9104b9b964ac1f5614aae2a24674d81`: all 67 manifest assets /
85,587,446 bytes at SHA-256
`399fa4f21f6ee89ffabf0516c1ec34d61d45600d745dffe28b5191c7f8f668b2`, seven
core routes and ten direct profiles matched at
`https://therealjameswilson.github.io/before-oss/`. Batch 438 requires its own
independent pull-request Test, merge, deployment and pinned-live verification
before it is described as released.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-six-mary-m-coghlan-through-leonard-cohen-pathways_batch-438_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch438.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,782 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
