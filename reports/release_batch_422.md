# Batch 422 release verification

2026-09-05 UTC. **Released and pinned-live verified.** This
report covers ten source records on PDF page 82 rows 28-37, Elizabeth W Clark
through George O Clark Jr., all in Box 126.

## Research

Page 82 was rendered at 150 dpi. Every printed name, initial, rank or blank,
private number or blank, box and location in the cohort was visually matched
to the immutable database before research. The reviewed evidence bundle adds
five citations, three affiliations, ten claims, twenty-six claim-source links,
ten person updates and ten saved research attempts. It adds no organization or
named employer.

The first Ernest D Clark source record has an exact private-identifier and name
match in the official Army Serial Number Merged File. His 10 July 1942 Army
entry and the source category `Engineers, stationary` support confirmed
identity and one qualified, medium-confidence occupation observation with
uncertain timing. The Army grade field is malformed, so it is neither expanded
nor used to classify his personnel category.

The second Ernest D Clark source record remains a separate entity. Its exact
private identifier points to Ernest K Clark in the Army file, while no exact-
name bridge resolves that discrepancy. This is a public identity conflict: no
occupation, assignment, grade or other candidate Army fact is transferred.

Frederick W Clark's exact private identifier and name support a high-confidence
identity and a qualified, medium-confidence `Furniture manufacturing
occupations, n.e.c.` observation at Army entry on 11 May 1939. The unusually
early entry date, internally anomalous birth-year value, and blank grade and
branch fields are exposed as source cautions. No unsupported rank or personnel
category is inferred.

George H Clark's exact private identifier and name support confirmed identity,
an Army-entry date of 9 March 1942, the occupation category `Designers`, and
enlisted Army classification. The occupation remains qualified and temporally
uncertain: it names neither an employer nor an exact design role and is not
promoted to immediate pre-OSS affiliation or last civilian employer.

Ellery D Clark's sole Navy candidate has middle initial H and is withheld.
Francis J Clark has one exact-name Army candidate, and George O Clark Jr. has
two exact-name-and-suffix Army candidates; the index lacks corroborating
identifiers needed to select any of them. Those candidates remain private and
the indexed identities remain ambiguous. Elizabeth W Clark, Frank M Clark and
George E Clark remain unresolved after the completed protocol.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional, obituary, newspaper or archival searches,
and the complete unrestricted 9,200,232-row Army merged-file comparison when
applicable were recorded for every person. All five distinct citation
destinations returned HTTP 200 in the bounded automated check. No access
control was bypassed and no authenticated NARA Catalog request was used.

See `research/batch-422-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved. All ten records remain on the Box 126 pull list.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,002 / 23,940 active people | 16.7168% |
| Verified-employer coverage | 215 / 23,940 active people | 0.8981% |
| Verified-affiliation coverage | 495 / 23,940 active people | 2.0677% |
| Archival disposition assessed | 3,955 / 23,940 active people | 16.5205% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,235 commissioned,
5,654 noncommissioned and 16,051 indeterminate. Identity: 753 confirmed, 608
high confidence, 128 probable, 80 ambiguous, 79 conflicting and 22,292
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,938 |
| in_progress | 46 |
| candidate_found | 7 |
| needs_identity_review | 118 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 681 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,572 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 933 | 35 |
| high | 1,240 | 276 |
| medium | 886 | 82 |
| low | 83 | 1 |
| conflicting | 90 | 2 |

There are 3,881 citation records, 1,813 legacy document keys that are not
certified unique historical documents, and 1,326 distinct stable URLs.
Inventory: 528 organizations, 1,578 affiliations, 3,232 claims, 7,371
claim-source links and 5,221 attempts/plans. Attempt outcomes: 1,784
`source_reviewed`, 179 `candidate_found`, 637 `candidate_rejected`, 2,034
`no_result` and 587 `planned`. There are 1,571 people with stored claims and
1,503 with public claims. Composite unresolved export: 22,854 data rows plus
header. Conflict union: 83. Pull list: 23,768 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 516 organizations, 1,567 affiliations, 3,146
published, qualified or conflict-visible claims, 2,731 public citations and 26
profile shards.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 422 counts. SQLite integrity and
foreign keys pass. All 90 Python tests pass in 4.399 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,464 HTML pages and 24,536
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,608 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,536 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,080 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. The tracked evidence bundle has
zero full private-identifier leaks. Twenty-one focused Batch 422 checks pass
across desktop, phone and tablet in 13.8 seconds. Their first run exposed six
test-only wording mismatches; only the assertions were corrected, without
changing evidence or site behavior. The dependency audit reports zero
vulnerabilities.

The complete 1,935-case local browser/accessibility matrix passed 1,935/1,935
in 17.0 minutes across desktop, phone and tablet with retries disabled.
Consecutive Pages-configuration builds reproduced byte-identical public and
production trees. Independent GitHub Test `33959080520` passed in 41 minutes
17 seconds. PR 179 merged as
`45e2ec15e0f9e6181e1550e6019d64e4776613ad`; Pages run `33961405702`
succeeded; and pinned verification against source commit
`be35bff667187beedf14e4904835280230079e46` matched all 67 assets, seven core
routes and ten direct cohort profiles.

Final manifest: 67 assets / 84,624,267 bytes; SHA-256
`3d166ca2523670adeb3db193d618d328cdf566f0bf6560346fab255fd7fd04b3`.
Public tree: 70 files, SHA-256
`586b24390d9abb46e4720cfa79fe890d764d4b01b347f028a5aa0ecbbfa44e96`.
Production tree: 24,536 files, SHA-256
`3b215e099d6ebd0f4f8495b23d3c43218a6e86012303123ab968df99a87b2d02`.
Tree digests use sorted file order and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-two-elizabeth-clark-through-george-o-clark-pathways_batch-422_2026-09-05.json
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
incomplete, with 19,938 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
