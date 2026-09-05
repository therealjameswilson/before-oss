# Batch 419 release verification

2026-09-05 UTC. **Local release candidate; not yet merged or deployed.** This
report covers ten people on PDF page 81 rows 44-46 and page 82 rows 1-7,
Joseph C Ciras through Peter D Clainos, all in Box 125.

## Research

Pages 81 and 82 were rendered at 150 dpi. Every printed name, middle initial,
suffix, rank, number or blank, box, note and location in the cohort was
visually matched to the immutable database before research. The reviewed
evidence bundle adds thirteen citations, five organizations, nine
affiliations, sixteen claims, forty-four claim-source links, ten person updates
and ten saved research attempts.

Caesar J Civitella has the cohort's strongest pathway evidence. His exact
private identifier matches the official Army merged file's 17 February 1943
entry. An official U.S. Special Operations Command history independently says
that he worked for Ford in Chester, Pennsylvania, joined the Army in February
1943, completed basic and airborne training, reported to Camp Mackall and was
screened for OSS one week later. Ford Motor Company is therefore published as
his high-confidence last civilian employer before military service, while the
United States Army at Camp Mackall is separately published as the explicit
immediate pre-OSS military pathway. No Ford plant, role or exact employment
dates are invented.

The same official history identifies Civitella's earlier attendance at Girard
College and the Pennsylvania Maritime Academy. Both are modeled as student
relationships, never employers. The Army file's residual occupation category
for production of ferrous and nonferrous metals is a separate medium-
confidence observation with uncertain timing; it is not silently equated with
his Ford job.

Joseph C Ciras has a confirmed match through exact name and private identifier
in the official Army merged file, with a secondary Operational Groups roster
providing compatible Greek Group VII context. His broad Army-entry occupation
category, `Structural and ornamental metal workers`, is published with medium
confidence and uncertain timing. It names no employer.

George V Clainos has a confirmed private-identifier match across the index,
Army merged file and Denver Public Library 10th Mountain Division name index.
The Army-entry category `Waiters and waitresses, except private family` and
the institutional roster's Sergeant, Company A, `86TH INF` assignment are
published as qualified observations. Neither source dates the unit assignment
relative to OSS or names a civilian employer, so neither is promoted to an
immediate predecessor role.

Peter D Clainos is published as a high-confidence commissioned Army officer.
The uncommon exact name, compatible officer number, Manchester hometown, Army
appointment and 1943 Library of Congress catalog record converge on the same
person. The catalog's exact wording, `128 Infantry Greek battalion`, is
preserved for his Camp Carson command. Other histories use 122nd and suggest
that he may have left before OSS recruited volunteers from the unit. His
personnel file is therefore needed before characterizing his relationship to
OSS, and the military assignment remains temporally qualified.

The uncommon exact name Nicholas D Clainos appears in authoritative 86th
Infantry sources, but the institutional roster carries a different officer
identifier from the OSS index. The candidate is not merged: the conflict is
visible, excluded from default analytics and routed to critical archival
review. A name and unit cannot override the identifier conflict.

A same-name World War II Army sergeant for Paul F Cirillo lacks the indexed
identifier, hometown and OSS bridge. A rare-name spelling-variant candidate
for indexed `Iganazio Ciuppa` likewise lacks an identifier, Army or OSS bridge.
Both remain low-confidence private leads. The original `Iganazio` spelling is
preserved, and no candidate employer is published. John J Cizauskas Jr. and
Helen V Clabby remain unresolved after the completed protocol. Stephan M
Claessens is classified only as foreign or Allied military personnel from the
printed Sergeant rank and incomplete `Dutch Ar` note; the note remains
verbatim and unexpanded.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, obituary and institutional searches, the complete
unrestricted Army merged-file comparison when applicable, and current Library
of Congress discovery checks were recorded for every person. Twelve of
thirteen distinct citation destinations returned HTTP 200 or 206 in the
bounded automated check. The Library of Congress item was readable in the
browser but rejected the generic automated request with HTTP 403. No access
control was bypassed and no authenticated NARA Catalog request was used.

See `research/batch-419-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,972 / 23,940 active people | 16.5915% |
| Verified-employer coverage | 215 / 23,940 active people | 0.8981% |
| Verified-affiliation coverage | 495 / 23,940 active people | 2.0677% |
| Archival disposition assessed | 3,925 / 23,940 active people | 16.3952% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,235 commissioned,
5,649 noncommissioned and 16,056 indeterminate. Identity: 746 confirmed, 607
high confidence, 128 probable, 72 ambiguous, 76 conflicting and 22,311
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,968 |
| in_progress | 46 |
| candidate_found | 3 |
| needs_identity_review | 110 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 673 |
| conflicting_sources | 75 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,565 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 926 | 35 |
| high | 1,239 | 276 |
| medium | 878 | 82 |
| low | 80 | 1 |
| conflicting | 87 | 2 |

There are 3,860 citation records, 1,804 legacy document keys that are not
certified unique historical documents, and 1,317 distinct stable URLs.
Inventory: 528 organizations, 1,570 affiliations, 3,210 claims, 7,312
claim-source links and 5,191 attempts/plans. Attempt outcomes: 1,776
`source_reviewed`, 167 `candidate_found`, 634 `candidate_rejected`, 2,027
`no_result` and 587 `planned`. There are 1,557 people with stored claims and
1,492 with public claims. Composite unresolved export: 22,862 data rows plus
header. Conflict union: 80. Pull list: 23,768 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 516 organizations, 1,559 affiliations, 3,127
published/qualified/conflict-visible claims and 2,716 public citations.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 419 counts. SQLite integrity and
foreign keys pass. All 90 Python tests pass in 4.357 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,464 HTML pages and 24,536
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,605 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,536 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,081 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. A separate scan finds zero
eight-digit private-identifier sequences in the tracked evidence bundle. The
twenty-four final Batch 419 focused checks pass across desktop, phone and
tablet in 17.2 seconds. The first authoring run had two test-string mismatches;
only the assertions were corrected, without changing evidence or site
behavior. The dependency audit reports zero vulnerabilities.

The complete 1,866-case local browser/accessibility matrix passed 1,866/1,866
in 14.9 minutes across desktop, phone and tablet with retries disabled.
Consecutive Pages-configuration builds reproduced byte-identical public and
production trees. Independent GitHub QA, merge, Pages deployment and pinned
live verification remain subsequent release gates.

Final manifest: 67 assets / 84,475,132 bytes; SHA-256
`7425145d48c774398b5c0f7d4b51069a33f6dfd8d060bf8815fc2010008dfe79`.
Public tree: 70 files, SHA-256
`996cd1b7cebc830d9ab1a563f9f8484f71fa793ca6afd87e947c5d5b617c3dd3`.
Production tree: 24,536 files, SHA-256
`59b9655735287b3d1dff159d2069c542acf3c5bcaf9fa93a0d707db70839f79d`.
Tree digests use sorted file order and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-one-and-eighty-two-joseph-ciras-through-peter-clainos-pathways_batch-419_2026-09-05.json
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
incomplete, with 19,968 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
