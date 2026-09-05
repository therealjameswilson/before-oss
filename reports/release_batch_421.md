# Batch 421 release verification

2026-09-05 UTC. **Local release candidate; not yet merged or deployed.** This
report covers ten people on PDF page 82 rows 18-27, Andrew H Clark through
Eleanor Clark, all in Box 126.

## Research

Page 82 was rendered at 150 dpi. Every printed name, initial, rank or blank,
private number or blank, box and location in the cohort was visually matched
to the immutable database before research. The reviewed evidence bundle adds
six citations, one affiliation, three claims, eight claim-source links, ten
person updates and ten saved research attempts. It adds no organization or
named employer.

Creston P Clark's exact private identifier and distinctive name match the
official Army Serial Number Merged File. The corresponding Army-entry
occupation category, accountants and auditors, is therefore published as a
qualified, medium-confidence observation with uncertain timing. It does not
name an employer, workplace or exact accounting role and is not promoted to
an immediate pre-OSS affiliation or last civilian employer. Creston is
classified as enlisted Army personnel; the other nine classifications remain
unknown or indeterminate.

Calvin L Clark is a documented conflict, not a merged military biography. The
sole exact-name Army row carries a different private identifier, while the
identifier printed in the OSS index has no Army-file hit. No candidate
occupation, assignment or other Army fact is transferred. The conflict is
public, excluded from default analytics and routed to critical Box 126
archival review.

Andrew H Clark, Clayton E Clark and Douglas M Clark each have a sole exact-name
Army candidate; Dorothy P Clark has a sole exact-name Women's Army Corps
candidate; and Clyde Clark has six exact-name Army candidates. The index lacks
the corroborating identifiers needed to select any of them. They remain
separate private leads, and the five indexed identities remain ambiguous.
Anna H Clark and Cecelia Clark remain unresolved after the completed protocol.
The printed spelling `Cecelia` is preserved; `Cecilia` was used only as a
search variant.

Authoritative Vassar material and a contemporary 1943 magazine report strongly
document writer Eleanor Clark as an OSS employee. The unqualified common-name
index row supplies no second identifier, however, so that biography is not
assigned to the indexed person. Her writing, translation, political and
educational history remain private candidate evidence rather than public
affiliation claims.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional, obituary, newspaper or archival searches,
and the complete unrestricted 9,200,232-row Army merged-file comparison when
applicable were recorded for every person. All six distinct citation
destinations returned HTTP 200 in the bounded automated check. No access
control was bypassed and no authenticated NARA Catalog request was used.

See `research/batch-421-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved. All ten records remain on the Box 126 pull list.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,992 / 23,940 active people | 16.6750% |
| Verified-employer coverage | 215 / 23,940 active people | 0.8981% |
| Verified-affiliation coverage | 495 / 23,940 active people | 2.0677% |
| Archival disposition assessed | 3,945 / 23,940 active people | 16.4787% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,235 commissioned,
5,653 noncommissioned and 16,052 indeterminate. Identity: 751 confirmed, 607
high confidence, 128 probable, 78 ambiguous, 78 conflicting and 22,298
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,948 |
| in_progress | 46 |
| candidate_found | 6 |
| needs_identity_review | 116 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 678 |
| conflicting_sources | 77 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,569 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 931 | 35 |
| high | 1,239 | 276 |
| medium | 883 | 82 |
| low | 80 | 1 |
| conflicting | 89 | 2 |

There are 3,876 citation records, 1,812 legacy document keys that are not
certified unique historical documents, and 1,325 distinct stable URLs.
Inventory: 528 organizations, 1,575 affiliations, 3,222 claims, 7,345
claim-source links and 5,211 attempts/plans. Attempt outcomes: 1,781
`source_reviewed`, 176 `candidate_found`, 636 `candidate_rejected`, 2,031
`no_result` and 587 `planned`. There are 1,564 people with stored claims and
1,499 with public claims. Composite unresolved export: 22,857 data rows plus
header. Conflict union: 82. Pull list: 23,768 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 516 organizations, 1,564 affiliations, 3,139
published, qualified or conflict-visible claims, 2,727 public citations and 26
profile shards.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 421 counts. SQLite integrity and
foreign keys pass. All 90 Python tests pass in 4.293 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,464 HTML pages and 24,536
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,608 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,536 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,080 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. The tracked evidence bundle has
zero full private-identifier leaks. Twenty-four focused Batch 421 checks pass
across desktop, phone and tablet in 15.4 seconds. The dependency audit reports
zero vulnerabilities.

The complete 1,914-case local browser/accessibility matrix passed 1,914/1,914
in 15.6 minutes across desktop, phone and tablet with retries disabled.
Consecutive Pages-configuration builds reproduced byte-identical public and
production trees. Independent GitHub QA, merge, Pages deployment and pinned
live verification remain subsequent release gates.

Final manifest: 67 assets / 84,572,017 bytes; SHA-256
`b1939d162d61a76c3a1c5140bddaefddfd83aebe640583156374c6f9e8630c6c`.
Public tree: 70 files, SHA-256
`5f9c1014e6a5080857985e6e1eabf3681786ecda4fad61cd602050ec399841cb`.
Production tree: 24,536 files, SHA-256
`a6153be1a28c30ecf3e733983dbad9887302b8a7b6a5b56d8272939ccbd130a7`.
Tree digests use sorted file order and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-two-andrew-clark-through-eleanor-clark-pathways_batch-421_2026-09-05.json
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
incomplete, with 19,948 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
