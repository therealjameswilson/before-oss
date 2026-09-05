# Batch 425 release verification

2026-09-05 UTC. **Local release candidate.** This report covers ten source
records on PDF page 83 rows 12-21, Thomas B Clark through Josephine Clarke,
all in Box 127 at location 230/86/28/07.

## Research

Page 83 was rendered at 150 dpi. Every printed name, initial, rank or blank,
private number or blank, box and location in the cohort was visually matched to
the immutable database before research. The reviewed evidence bundle adds four
citations, two affiliations, four claims, twelve claim-source links, ten person
updates and ten saved research attempts. It adds no organization or named
employer.

Exact private-identifier and name matches support confirmed identities for
Thomas B Clark and William F Clark. Thomas's official record reports Army entry
on 25 October 1943, an enlisted grade and civilian-occupation value 031. The
rendered official code page defines that value as teachers (secondary school)
and principals. The result is a qualified, medium-confidence occupation
observation: it names no school or employer and does not establish that the
work immediately preceded OSS service.

William's official record reports Army entry on 12 October 1943, an enlisted
grade and standard-card occupation value 992, students. Student status is
published separately from employment; the record identifies no school and
does not establish immediate OSS chronology. Walter R Clark remains a
commissioned Army officer because the index prints `Capt`. The incomplete Army
bulk file supplies no matching identifier, but that non-hit is not used to
weaken the index classification.

Vernon S Clark, Edward Clarke, Frederick C Clarke and James F Clarke retain
unmerged name-only candidates and remain ambiguous. William R Clark, Grace M
Clarke and Josephine Clarke remain unresolved. Incompatible or unbridged
school, obituary, engineering, military-roster and genealogy candidates were
rejected or kept private. No employer, immediate predecessor affiliation or
last civilian employer was established for any person in the cohort.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional, obituary, newspaper or archival searches,
the current Library of Congress API and the complete unrestricted
9,200,232-row Army merged-file comparison when applicable were recorded for
every person. All four distinct citation destinations returned HTTP 200 in the
bounded automated check. No access control was bypassed and no authenticated
NARA Catalog request was used.

See `research/batch-425-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved. All ten records remain on the Box 127 pull list.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,030 / 23,940 active people | 16.8338% |
| Verified-employer coverage | 215 / 23,940 active people | 0.8981% |
| Verified-affiliation coverage | 495 / 23,940 active people | 2.0677% |
| Archival disposition assessed | 3,985 / 23,940 active people | 16.6458% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,235 commissioned,
5,660 noncommissioned and 16,045 indeterminate. Identity: 759 confirmed, 609
high confidence, 128 probable, 91 ambiguous, 79 conflicting and 22,274
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,910 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 129 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 687 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,585 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 939 | 35 |
| high | 1,241 | 276 |
| medium | 892 | 82 |
| low | 83 | 1 |
| conflicting | 90 | 2 |

There are 3,893 citation records, 1,813 legacy document keys that are not
certified unique historical documents, and 1,326 distinct stable URLs.
Inventory: 528 organizations, 1,584 affiliations, 3,245 claims, 7,410
claim-source links and 5,251 attempts/plans. Attempt outcomes: 1,791
`source_reviewed`, 190 `candidate_found`, 641 `candidate_rejected`, 2,042
`no_result` and 587 `planned`. There are 1,578 people with stored claims and
1,510 with public claims. Composite unresolved export: 22,848 data rows plus
header. Conflict union: 83. Pull list: 23,768 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 516 organizations, 1,573 affiliations, 3,159
published, qualified or conflict-visible claims, 2,743 public citations and 26
profile shards.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 425 counts. SQLite integrity and
foreign keys pass. All 90 Python tests pass in 4.272 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,464 HTML pages and 24,536
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,608 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,536 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,081 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. The tracked evidence bundle has
zero full private-identifier leaks. Fifteen focused Batch 425 checks pass
across desktop, phone and tablet in 14.4 seconds. Authoring runs exposed only
test-wording assumptions about a private note and a public field label; the
assertions were corrected without changing evidence or site behavior. The
dependency audit reports zero vulnerabilities.

The complete 1,986-case local browser/accessibility matrix produced 1,983
passes and three legacy browser-resource failures in 58.4 minutes with retries
disabled. Batches 022, 175 and 331 each stalled while waiting for a profile;
all passed in another viewport during the matrix, and all three exact scenarios
then passed across desktop, phone and tablet, 9/9 in 10.3 seconds. No Batch 425
test failed. Consecutive Pages-configuration builds reproduced byte-identical
public and production trees. The clean independent GitHub Test, merge, Pages
deployment and pinned live verification remain required before this candidate
is a release.

Final manifest: 67 assets / 84,736,826 bytes; SHA-256
`44f14caa66a23a4484e73fea079b5fdb2237c366cba9f2896ed1baaed4942cce`.
Public tree: 70 files, SHA-256
`0854de0558d23a9115f1f992f16a9833c61de6429107a9b4dac37aa3f0c0583a`.
Consecutive Pages-configuration production trees: 24,536 files, SHA-256
`afa6cae72a765ab312e23442db8b28466b62a8afe90a165d65a46360b68d82e1`.
Tree digests use sorted relative paths and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-three-thomas-clark-through-josephine-clarke-pathways_batch-425_2026-09-05.json
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
incomplete, with 19,910 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
