# Batch 444 release verification

2026-09-09 UTC. **Local release candidate; independent release checks
pending.** This report covers PDF page 87 rows 18-27, Lawrence A Coleman
through Norman T Collett, spanning Boxes 134-135 at location 230/86/29/01.

## Research

Page 87 was rendered at 150 dpi. Every printed name, initial, blank or printed
rank, private identifier or blank, box, note and location in the cohort was
visually matched to the immutable database before research. Five printed
identifiers remain research-only and are masked in every public artifact.
Lawrence A Coleman's six-digit, Robert C Coleman's seven-digit and Joseph
Collart's five-digit values were preserved literally; none was padded or
corrected to force an Army match.

A complete transient scan of 9,200,232 official Army merged-file records found
two exact private-identifier matches. Thomas J Coleman's identifier selects one
of twenty exact-name Army rows and dates Army entry to 31 March 1941 as a
private, with civilian-occupation value 125. The other identifier links the
index's printed `Loannis N Collaros` to the Army form `Ioannis N Collaros` and
dates Army entry to 3 April 1942 as a private, with value 061. Both name forms
remain visible; `Ioannis` is documented as a variant rather than silently
substituted for the indexed spelling.

Official NARA technical documentation and visually checked code-list pages
define values 125 and 061 as office machine operators and radio operators.
They are published as medium-confidence historical occupational categories,
strongly date-bounded to Army entry. Neither observation names an employer,
machine, station, workplace, military specialty, immediate pre-OSS affiliation
or Army-to-OSS sequence.

The Army scan found one exact-name row each for Lawrence A Coleman, Marion E
Coleman and Orrin K Coligan; eighteen for Robert C Coleman, twenty for Thomas J
Coleman and seven for William S Coleman. It found no exact-name row for Aline J
Colgate, the printed Loannis form, Joseph Collart or Norman T Collett. Only the
exact identifiers selected the Thomas and Ioannis records. Name-only rows were
not assigned to index people. The Army file is incomplete and is neither an
officer, Navy, Marine Corps nor comprehensive OSS roster, so a non-hit is not
negative proof.

Existing official evidence continues to support Joseph H Collart at high
confidence as the indexed commissioned Army officer and Area B instructor.
His Washington State connection remains a student affiliation, not an
employer. The short printed identifier is consistent with an official officer-
register presentation but remains literal and private. Box 135 is still
required to establish his immediate pre-OSS assignment and any last civilian
employer.

Lawrence A Coleman, Marion E Coleman, Robert C Coleman, William S Coleman,
Aline J Colgate, Orrin K Coligan and Norman T Collett remain unresolved. The
index's printed `Sgt` continues to classify Coligan as enlisted Army personnel,
but a lone name-only Army row and a postwar former-GI caption do not establish
his identity or employment. Every unresolved profile carries a specific Box
134 or 135 question rather than claiming that no prior employment existed.

Every person received recorded official NARA and CIA context checks, exact-
name OSS and meaningful variant searches, employment and occupation queries,
institutional, obituary, directory, newspaper, current Library of Congress and
other archival discovery. Modern namesakes and unbridged common-name results
were rejected. No authenticated NARA Catalog request was used.

The reviewed bundle adds four citation records, two affiliations, four claims,
twelve claim-source links, ten person updates and ten saved research attempts.
Because Joseph Collart already had a nonplanned attempt, the cohort advances
distinct research-attempt coverage by nine people. See
`research/batch-444-discovery-checkpoint.md` for the complete adjudication,
rejected leads, source cautions and next actions. All ten records have terminal
outcomes. Research completion means a saved reviewable result, not that a
prior employer has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,215 / 23,940 active people | 17.6065% |
| Verified-employer coverage | 223 / 23,940 active people | 0.9315% |
| Verified-affiliation coverage | 506 / 23,940 active people | 2.1136% |
| Archival disposition assessed | 4,170 / 23,940 active people | 17.4185% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,239 commissioned,
5,716 noncommissioned and 15,985 indeterminate. Identity: 815 confirmed, 620
high confidence, 139 probable, 106 ambiguous, 79 conflicting and 22,181
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,725 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 141 |
| needs_temporal_review | 13 |
| verified_employer_found | 212 |
| documented_prewar_employer_found | 80 |
| occupation_only_found | 740 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,691 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 995 | 35 |
| high | 1,272 | 289 |
| medium | 968 | 92 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

There are 4,022 citation records, 1,864 provisional document keys that are not
certified unique historical documents, and 1,369 distinct stable URLs.
Inventory: 541 organizations, 1,664 affiliations, 3,422 claims, 7,902 claim-
source links and 5,441 attempts/plans. Attempt outcomes: 1,869
`source_reviewed`, 201 `candidate_found`, 675 `candidate_rejected`, 2,109
`no_result` and 587 `planned`. Composite unresolved export: 22,781 data rows
plus header. Conflict count: 83. Pull list: 23,766 data rows plus header;
review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 529 organizations, 1,653 affiliations, 3,322
published, qualified or conflict-visible claims, 2,865 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 529
organization rows, 1,653 affiliation rows and 2,865 citation rows.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full fresh replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduces the Batch 444 counts and both output-tree digests
byte-for-byte. SQLite `quick_check` returns `ok`, foreign keys pass, and all 93
Python tests pass in 4.258 seconds. The deterministic 200-profile structural
audit passes; it is not independent historical re-review, and the women
stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,477 HTML pages and 24,549
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,659 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,549 built artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,095 candidate substring coincidences with zero
unexpected boundary, aggregate or manifest-size matches. The same audit over
all 70 public-tree files finds 665 candidate coincidences and zero unexpected
matches. The focused Batch 444 browser suite passes all nine checks across
desktop, phone and tablet in 5.2 seconds after the fresh replay. An initial
focused run exposed two test-only case/wording expectations; those expectations
were aligned with the already correct public pages, and all subsequent checks
pass. The dependency audit reports zero vulnerabilities across 277 installed
package paths.

The public manifest contains 67 assets / 86,235,238 bytes at SHA-256
`7353914d300772d58dac1713adbdecfd2c8bf668952cb10a89c83da7cd99c0c2`.
The deterministic public-tree digest covers 70 files / 88,582,373 bytes at
SHA-256
`bce73eb07f30a625a780556a36cc9383a7db7689b00ff96e4b2b45e799d54670`;
the 24,549-file / 273,378,857-byte production tree is
`e46dd60f89fc39a46fec0d60c6b5c32bdd5e292478cf0fdcc0276ea2e1f83f50`.
The clean replay and second exact Pages build reproduce both tree digests and
file counts.

Batch 440 is the latest pinned-live verified release at the time of this local
report. Batch 441 is in independent pull-request Test `34338589582`; Batches
442-444 remain queued for their own independent gates.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-seven-lawrence-a-coleman-through-norman-t-collett-pathways_batch-444_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch444.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,725 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-
source research is not blocked. Unresolved methodological issues remain:
automated profile audit is structural rather than independent historical
validation, source-document identity normalization is provisional, external
links are inventoried rather than exhaustively visited, and most personnel
files still require archival examination.
