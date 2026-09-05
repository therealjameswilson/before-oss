# Batch 423 release verification

2026-09-05 UTC. **Local release candidate; not yet merged or deployed.** This
report covers ten source records on PDF page 82 rows 38-46 and page 83 row 1,
Helen H Clark through Percy E Clark, spanning Boxes 126-127.

## Research

Pages 82 and 83 were rendered at 150 dpi. Every printed name, initial, rank or
blank, private number or blank, box and location in the cohort was visually
matched to the immutable database before research. The reviewed evidence
bundle adds four citations, one affiliation, two claims, six claim-source
links, ten person updates and ten saved research attempts. It adds no
organization or named employer.

John M Clark's exact private identifier and exact name select one official Army
record among thirty exact-name candidates. His 2 September 1943 Army entry,
private grade and source category `Policemen and detectives, public service`
support confirmed identity, enlisted Army classification and one qualified,
medium-confidence occupation observation with uncertain timing. The source
does not identify a public agency, jurisdiction, workplace or exact
police-versus-detective role, so no employer is inferred.

John N Clark retains the commissioned Army officer classification established
by the index's printed `Maj` rank. Thirteen exact-name Army records lack an
indexed identifier, unit, hometown or direct OSS bridge; none is selected and
no outside occupation or biography is transferred.

Hoyt B Clark has one name-only Army candidate, James E Clark has 111 and
Leonard F Clark has one whose identifier does not match the supplied index
number. They remain ambiguous and unmerged. Helen H Clark, Janie K Clark,
Julia A Clark and Percy E Clark have no exact-name Army row and remain
unresolved. Leslie A Clark's supplied identifier has no Army-file hit, while
four exact-name Army rows carry other identifiers; those candidates are
rejected rather than substituted.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional, obituary, newspaper or archival searches,
and the complete unrestricted 9,200,232-row Army merged-file comparison when
applicable were recorded for every person. All four distinct citation
destinations returned HTTP 200 in the bounded automated check. No access
control was bypassed and no authenticated NARA Catalog request was used.

See `research/batch-423-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved. All ten records remain on the Boxes 126-127 pull list.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,012 / 23,940 active people | 16.7586% |
| Verified-employer coverage | 215 / 23,940 active people | 0.8981% |
| Verified-affiliation coverage | 495 / 23,940 active people | 2.0677% |
| Archival disposition assessed | 3,965 / 23,940 active people | 16.5622% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,235 commissioned,
5,655 noncommissioned and 16,050 indeterminate. Identity: 754 confirmed, 608
high confidence, 128 probable, 84 ambiguous, 79 conflicting and 22,287
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,928 |
| in_progress | 46 |
| candidate_found | 7 |
| needs_identity_review | 122 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 682 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,577 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 934 | 35 |
| high | 1,240 | 276 |
| medium | 887 | 82 |
| low | 83 | 1 |
| conflicting | 90 | 2 |

There are 3,885 citation records, 1,813 legacy document keys that are not
certified unique historical documents, and 1,326 distinct stable URLs.
Inventory: 528 organizations, 1,579 affiliations, 3,234 claims, 7,377
claim-source links and 5,231 attempts/plans. Attempt outcomes: 1,785
`source_reviewed`, 183 `candidate_found`, 638 `candidate_rejected`, 2,038
`no_result` and 587 `planned`. There are 1,572 people with stored claims and
1,504 with public claims. Composite unresolved export: 22,853 data rows plus
header. Conflict union: 83. Pull list: 23,768 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 516 organizations, 1,568 affiliations, 3,148
published, qualified or conflict-visible claims, 2,735 public citations and 26
profile shards.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 423 counts. SQLite integrity and
foreign keys pass. All 90 Python tests pass in 4.374 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,464 HTML pages and 24,536
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,608 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,536 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,081 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. The tracked evidence bundle has
zero full private-identifier leaks. Twenty-one focused Batch 423 checks pass
across desktop, phone and tablet in 14.3 seconds. Their first completed run
exposed six test-only wording mismatches; only the assertions were corrected,
without changing evidence or site behavior. The dependency audit reports zero
vulnerabilities.

The complete 1,956-case local browser/accessibility matrix produced 1,954
passes and two browser-resource timeouts in 38.3 minutes with retries disabled.
One timed out during teardown; the other stalled while waiting for a previously
stable legacy profile. Both exact cases then passed 2/2 in isolation in 3.8
seconds, and all twenty-one Batch 423 scenarios passed across all three
viewports. Consecutive Pages-configuration builds reproduced byte-identical
public and production trees. Independent GitHub QA, merge, Pages deployment
and pinned live verification remain subsequent release gates.

Final manifest: 67 assets / 84,648,538 bytes; SHA-256
`880114ce786d173bba99f03d85b143b2c2b97b343d6b56a0b39e47d010c4bae3`.
Public tree: 70 files, SHA-256
`56aed88ade4ed5998b7b7d63fbeea6a8312894f1504c5b9baa245cd51b621379`.
Production tree: 24,536 files, SHA-256
`7190988b78f618e034b4fd99fd103579c6dde408ecfbb19dd44f0b9e4b88bf32`.
Tree digests use sorted relative paths and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-two-eighty-three-helen-clark-through-percy-clark-pathways_batch-423_2026-09-05.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npm run test:e2e
npm run check:links
```

Full replay: `bash scripts/rebuild-all.sh`. The goal remains active and
incomplete, with 19,928 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
