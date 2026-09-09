# Batch 434 release verification

2026-09-09 UTC. **Released and pinned-live verified.** This report covers PDF
page 85 rows 10-19, Philip B Coan through
Anne M Coblean, spanning Boxes 130-131 at location 230/86/28/07.

## Research

Page 85 was rendered at 150 dpi. Every printed name, initial, blank rank,
private identifier or blank, box, note and location in the cohort was visually
matched to the immutable database before research. The index prints no rank
for anyone in the batch. Four private identifiers remain research-only and are
masked in every public artifact.

A complete transient scan of 9,200,232 fixed-width Army merged-file records
tested every eligible printed identifier literally. The two seven-digit values
were also checked with a single leading zero as an explicitly recorded search
variant, not as a correction to the index. Two exact identifier-and-name
matches resulted. William A Coates entered the Army on 8 March 1945 as a
private; Howard L Cobb entered on 21 May 1943 as a private. Those fields support
confirmed identities and enlisted Army classification.

Official NARA record-layout and code-list documentation was visually checked
before interpreting the selected Army fields. William's code is published as
`Teachers (secondary school) and principals`; Howard's is published as
`Wholesale managers`. Both are medium-confidence, temporally uncertain
occupation observations. Neither code names a school, district, business,
employer, immediate predecessor or last civilian employer. The recorded Army
entry dates do not establish the occupations' actual dates or their relation to
OSS service.

Philip B Coan's printed identifier produced no Army match. John G Coates's
printed identifier likewise produced no match, while the file contains one
exact-name row with a different identifier. That conflict is recorded as a
rejected candidate and the row remains unresolved; a name match cannot
override incompatible identifier evidence. George H Coates has three exact-
name Army rows and Robert B Coates has three, but neither index row supplies an
identifier and no independent source bridges any candidate to the relevant OSS
file. Howard has two exact-name rows and William four, but their exact private
identifiers select one row apiece. Jane E Coates, Lucille A Coates, Eleanor
Cobb and Anne M Coblean have no exact-name Army row. These non-hits are not
negative proof because the file is incomplete and is neither an officer, Navy
nor comprehensive OSS register.

Outside candidates were kept separate. The journalist and editor Philip
Munson Coan conflicts with the indexed middle initial B and lacks an OSS or Box
130 bridge. A Texas petroleum geologist named George H Coates, a spouse
reference for Eleanor Ruggles Cobb, and an RCA inventor named Howard L Cobb
likewise lack record-level bridges. No employment or identity claim was copied
from those people. Modern people-finder material was rejected without
retaining sensitive details.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional archives, obituaries, directories,
newspapers, current Library of Congress discovery, official NARA context and
the complete Army comparison when applicable were recorded for every person.
CIA Reading Room site searches produced no exact-name result. Search snippets,
commercial people finders, unsourced genealogy and generated summaries were
not used as evidence. No authenticated NARA Catalog request was used.

The reviewed evidence bundle adds four citations, no organization, two
affiliations, four claims, twelve claim-source links, ten person updates and ten
saved research attempts. It is idempotent on repeated import. See
`research/batch-434-discovery-checkpoint.md` for rejected leads, cautions and
next actions. All ten records remain on the archival pull list; eight remain
unresolved and two have qualified occupation-only outcomes. Research completion
means a saved reviewable outcome, not that a prior employer has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,118 / 23,940 active people | 17.2013% |
| Verified-employer coverage | 219 / 23,940 active people | 0.9148% |
| Verified-affiliation coverage | 501 / 23,940 active people | 2.0927% |
| Archival disposition assessed | 4,073 / 23,940 active people | 17.0134% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,238 commissioned,
5,680 noncommissioned and 16,022 indeterminate. Identity: 783 confirmed, 613
high confidence, 132 probable, 106 ambiguous, 79 conflicting and 22,227
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,822 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 142 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 73 |
| occupation_only_found | 707 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,635 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 963 | 35 |
| high | 1,257 | 283 |
| medium | 919 | 83 |
| low | 96 | 1 |
| conflicting | 90 | 2 |

There are 3,953 citation records, 1,837 provisional document keys that are not
certified unique historical documents, and 1,344 distinct stable URLs.
Inventory: 535 organizations, 1,618 affiliations, 3,325 claims, 7,628
claim-source links and 5,341 attempts/plans. Attempt outcomes: 1,822
`source_reviewed`, 200 `candidate_found`, 660 `candidate_rejected`, 2,072
`no_result` and 587 `planned`. There are 1,622 people with stored claims and
1,542 with public or conflict-visible claims. Composite unresolved export:
22,823 data rows plus header. Conflict union: 83. Pull list: 23,768 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 523 organizations, 1,607 affiliations, 3,226
published, qualified or conflict-visible claims, 2,797 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 523
organization rows, 1,607 affiliation rows and 2,797 citation rows.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduces the exact Batch 434 counts. SQLite `quick_check`
returns `ok`, foreign keys pass, and all 93 Python tests pass in 4.558 seconds.
The deterministic 200-profile structural audit passes; it is not independent
historical re-review, and the women stratum remains unavailable without sourced
classification.

The exact Pages-configuration build contains 24,471 HTML pages and 24,543
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,629 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,543 built artifacts, 12,926 normalized
identifiers, 120 formatted variants and 1,086 candidate substring coincidences
with zero unexpected boundary, aggregate or manifest-size matches. The same
audit over all 70 public-tree files finds zero unexpected matches. The focused
Batch 434 browser suite passes all twelve checks across desktop, phone and
tablet in 9.0 seconds. The dependency audit reports zero vulnerabilities.

The public manifest contains 67 assets / 85,337,347 bytes at SHA-256
`d503683e418193890b645dc444cfe73d0980e0b1cd512602843e6b116bd15ef9`.
The deterministic public-tree digest covers 70 files / 87,684,477 bytes at
SHA-256
`1ce16813ed2d2fce1ed15233808fe564ef8c2acc0832bf813d0cea5212345566`;
the 24,543-file / 272,069,851-byte production tree is
`70add608edb55a6688402a3138a907d285cff4c007ba6e84dafb899feda71bf9`.
Two consecutive projections and exact Pages-configuration builds, including
the full replay, reproduce both tree digests and file counts.

Independent pull-request Test `34306691024` passed every stage in 39 minutes
8 seconds. Pull request 190 merged to `main` as
`dbf7c9bc981fee5698bbaf7e4295cf26f09fbb9e` on 2026-09-09 at 04:06 UTC,
and Pages run `34309668867` completed successfully. The pinned read-only check
against immutable release commit
`ceb84b956be87abfd0b7623b306cf8430e2b4d30` matched all 67 manifest assets /
85,402,321 bytes at SHA-256
`4d666a735bf5dbd8bab0750918b20eef1788717be902711840185b2ba6891587`, seven
core routes and all ten Batch 434 profiles at
`https://therealjameswilson.github.io/before-oss/`. The merge-triggered main-
branch Test remains separately recorded in GitHub Actions and does not alter
the pinned release result.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-five-philip-b-coan-through-anne-m-coblean-pathways_batch-434_2026-09-08.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch434.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,822 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
