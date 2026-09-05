# Batch 424 release verification

2026-09-05 UTC. **Local release candidate; independent CI and live release
pending.** This report covers ten source records on PDF page 83 rows 2-11,
Phillip H Clark through Sidney E Clark, all in Box 127 at location 230/86/28/07.

## Research

Page 83 was rendered at 150 dpi. Every printed name, initial, rank or blank,
private number or blank, box and location in the cohort was visually matched to
the immutable database before research. The reviewed evidence bundle adds four
citations, three affiliations, seven claims, twenty-one claim-source links, ten
person updates and ten saved research attempts. It adds no organization or
named employer.

Exact private-identifier and name matches support confirmed identities for
Richard E Clark, Roger A Clark Jr. and Samuel E Clark. Richard's 7 May 1942
Army entry, private grade and official source category support a qualified,
medium-confidence occupation observation: chauffeurs and drivers, bus, taxi,
truck, and tractor. The category does not identify an employer, vehicle, route,
location or exact job.

Roger's record uses the Enlisted Reserve Corps statistical-card layout. The
official technical documentation places civilian occupation in columns 71-73,
one column later than the standard layout. The correct value is 992, students,
not the misleading apparent value 699. Student status is published separately
from employment; the source names no school and does not establish immediate
pre-OSS chronology.

Samuel's 13 December 1941 Army entry supports confirmed identity and enlisted
classification, but value 999 remains uninterpreted because the inspected
official summary pages do not define it reliably for this context. Russell W
Clark's exact identifier and name select one of eight exact-name Army rows and
support a high-confidence identity plus a qualified photographers occupation
observation. His grade field is malformed as `750`, so it is exposed as a
source anomaly and is not used for personnel classification.

Phillip H Clark and Richard N Clark Jr. have neither an identifier match nor an
exact-name Army row and remain unresolved. Robert G Clark has no identifier
match while thirty exact-name rows carry other identifiers; those candidates
are rejected. Randall E Clark, Sherman W Clark and Sidney E Clark have one,
one and two name-only Army candidates respectively; all remain ambiguous and
unmerged. No named employer, immediate predecessor affiliation or last
civilian employer was established for the cohort.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional, obituary, newspaper or archival searches,
and the complete unrestricted 9,200,232-row Army merged-file comparison when
applicable were recorded for every person. All four distinct citation
destinations returned HTTP 200 in the bounded automated check. No access
control was bypassed and no authenticated NARA Catalog request was used.

See `research/batch-424-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved. All ten records remain on the Box 127 pull list.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,021 / 23,940 active people | 16.7962% |
| Verified-employer coverage | 215 / 23,940 active people | 0.8981% |
| Verified-affiliation coverage | 495 / 23,940 active people | 2.0677% |
| Archival disposition assessed | 3,975 / 23,940 active people | 16.6040% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,235 commissioned,
5,658 noncommissioned and 16,047 indeterminate. Identity: 757 confirmed, 609
high confidence, 128 probable, 87 ambiguous, 79 conflicting and 22,280
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,919 |
| in_progress | 45 |
| candidate_found | 7 |
| needs_identity_review | 125 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 685 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,581 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 937 | 35 |
| high | 1,241 | 276 |
| medium | 890 | 82 |
| low | 83 | 1 |
| conflicting | 90 | 2 |

There are 3,889 citation records, 1,813 legacy document keys that are not
certified unique historical documents, and 1,326 distinct stable URLs.
Inventory: 528 organizations, 1,582 affiliations, 3,241 claims, 7,398
claim-source links and 5,241 attempts/plans. Attempt outcomes: 1,789
`source_reviewed`, 186 `candidate_found`, 639 `candidate_rejected`, 2,040
`no_result` and 587 `planned`. There are 1,576 people with stored claims and
1,508 with public claims. Composite unresolved export: 22,850 data rows plus
header. Conflict union: 83. Pull list: 23,768 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 516 organizations, 1,571 affiliations, 3,155
published, qualified or conflict-visible claims, 2,739 public citations and 26
profile shards.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 424 counts. SQLite integrity and
foreign keys pass. All 90 Python tests pass in 4.261 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,464 HTML pages and 24,536
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,608 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,536 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,083 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. The tracked evidence bundle has
zero full private-identifier leaks. Fifteen focused Batch 424 checks pass
across desktop, phone and tablet in 14.1 seconds. The first fresh-page run
exposed six test-only wording mismatches across three viewports; only the
assertions were corrected, without changing evidence or site behavior. The
dependency audit reports zero vulnerabilities.

The complete 1,971-case local browser/accessibility matrix produced 1,964
passes and seven browser-resource failures in 1.1 hours with retries disabled:
six action, navigation or teardown timeouts and one suspended local-network
navigation. No Batch 424 test failed. All seven affected legacy scenarios then
passed across desktop, phone and tablet, 21/21 in 22.7 seconds. Consecutive
Pages-configuration builds reproduced byte-identical public and production
trees. Independent GitHub QA, merge, Pages deployment and pinned live
verification remain subsequent release gates.

Final manifest: 67 assets / 84,701,215 bytes; SHA-256
`89a690ef1879074a49079921e90e363b1007aae8b58312ff26de6b2a7432b522`.
Public tree: 70 files, SHA-256
`bbb003592ecafdcbe8576f2c4e7dcebf9c7d4617a358459990fc19a185bacdcd`.
Consecutive Pages-configuration production trees: 24,536 files, SHA-256
`7a2bcd95b5042941a5c7c289650438e1b3dd028596a50c709eca8245412dade1`.
Tree digests use sorted relative paths and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-three-phillip-clark-through-sidney-clark-pathways_batch-424_2026-09-05.json
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
incomplete, with 19,919 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
