# Batch 429 release verification

2026-09-06 UTC. **Local release candidate; independent release checks pending.**
This report covers ten source records on PDF page 84 rows 6-15, Alice B Clem
through Ira L Clements, spanning Boxes 128-129 at location 230/86/28/07.

## Research

Page 84 was rendered at 150 dpi. Every printed name, initial, rank or blank
rank, private identifier or blank, box, note and location in the cohort was
visually matched to the immutable database before research. Only the two
eligible eight-digit identifier shapes were compared directly with the
official Army file. Robert E Clemens's nine-digit, Geraldine Clement's six-
digit and Ira L Clements's nine-character alphanumeric values were preserved
unchanged and tested separately; none was silently truncated, padded or
converted. The reviewed evidence bundle adds nine citations, one organization,
four affiliations, ten claims, twenty-nine claim-source links, ten person
updates and ten saved research attempts.

Exact private-identifier matches support confirmed identities and enlisted
Army classification for Kent L Clemans and Egidio Clemente. Their official
Army-entry records carry occupation values 681 and 649. Rendered official code
pages define those as `Molders` and `Occupations in printing and publishing,
n.e.c.` Each is published as a qualified, medium-confidence observation. The
categories name no employer and do not establish immediate pre-OSS chronology.
The Army row for Egidio uses the source variant `Clement Egidio`; rare-name,
birth-year and occupation evidence plus a University of Minnesota finding aid
independently corroborate the identifier-confirmed identity.

The University of Minnesota's IHRC460 finding aid documents Egidio Clemente as
editor and publisher of *La Parola del Popolo* before describing his World War
II U.S. intelligence service in Algeria, Sicily and Rome. The employment claim
is high confidence and documented prewar. It is neither marked immediate nor
last civilian because the finding aid supplies no employment end date or
complete Army-to-OSS sequence.

CIA FOIA document 00309756, an official 24 May 1945 OSS regimental list, names
Captain Marcel J. Clemente. A 5 May 1945 *Nassau Daily Review-Star* article
independently gives the rare exact name, promotion to major, Army entry in June
1943 and service with OSS in Italy. The article says he had been employed by a
guarantee and trust company in New York. This is published as high-confidence,
strongly date-bounded last civilian employment before Army service, not as the
immediate pre-OSS affiliation. The company remains explicitly unnamed and no
role is invented. The terminal status remains documented prewar employer found
so the unresolved legal organization name and chronology stay on the archival
pull list.

Military Times Hall of Valor identifies Georges Clement as a French sous-
lieutenant attached to OSS for 1944 action near Le Mans and cites a 1945
European Theater general order. The exact name, equivalent rank, French index
note and OSS context support high-confidence identity and French Allied
commissioned-officer classification. The accessible source is a secondary
index to the order, so identity is not called confirmed and no prior French
assignment or civilian employer is inferred.

None of three exact-name Robert E Clemens Army rows matches the indexed nine-
digit value, and the sole exact-name Ira L Clements Army row carries a
different identifier. A later same-name veteran obituary for Ira lacks a
branch, identifier or OSS link. All candidates remain rejected rather than
merged. Alice B Clem, Catherine A Clement, Geraldine Clement and Claras B
Clements remain unresolved. Search-engine correction of `Claras` to `Clara`
was rejected as a spelling correction.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional finding aids, obituaries, directories,
newspapers, the current Library of Congress API and a complete 9,200,232-row
Army merged-file comparison when applicable were recorded for every person.
Seven of nine citation destinations returned HTTP 200 in a bounded automated
HEAD check. The University of Minnesota finding-aid endpoint returned HTTP 202
and the NYS Historic Newspapers viewer returned HTTP 403 to the generic
automated request after both pages had been visually inspected in an ordinary
browser. No authenticated NARA Catalog request was used and no access
restriction or CAPTCHA was bypassed.

See `research/batch-429-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved. All ten records remain on the Boxes 128-129 pull list.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,070 / 23,940 active people | 17.0008% |
| Verified-employer coverage | 217 / 23,940 active people | 0.9064% |
| Verified-affiliation coverage | 498 / 23,940 active people | 2.0802% |
| Archival disposition assessed | 4,025 / 23,940 active people | 16.8129% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,238 commissioned,
5,669 noncommissioned and 16,033 indeterminate. Identity: 770 confirmed, 611
high confidence, 129 probable, 103 ambiguous, 79 conflicting and 22,248
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,870 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 141 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 72 |
| occupation_only_found | 696 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,601 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 950 | 35 |
| high | 1,246 | 278 |
| medium | 904 | 83 |
| low | 94 | 1 |
| conflicting | 90 | 2 |

There are 3,923 citation records, 1,827 legacy document keys that are not
certified unique historical documents, and 1,338 distinct stable URLs.
Inventory: 530 organizations, 1,598 affiliations, 3,284 claims, 7,517
claim-source links and 5,291 attempts/plans. Attempt outcomes: 1,805
`source_reviewed`, 197 `candidate_found`, 646 `candidate_rejected`, 2,056
`no_result` and 587 `planned`. There are 1,602 people with stored claims and
1,524 with public or conflict-visible claims. Composite unresolved export:
22,836 data rows plus header. Conflict union: 83. Pull list: 23,768 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 518 organizations, 1,587 affiliations, 3,187
published, qualified or conflict-visible claims, 2,768 public citations and 26
profile shards.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduces the exact Batch 429 counts. SQLite integrity and
foreign keys pass. All 93 Python tests pass in 4.678 seconds; test output is
clean. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,466 HTML pages and 24,538
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,618 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,538 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,080 candidate substring coincidences with zero
unexpected boundary, aggregate or manifest-size matches. Twelve focused Batch
429 checks pass across desktop, phone and tablet in 25.1 seconds after two
test-only wording assumptions were corrected; no evidence or application
behavior changed. The dependency audit reports zero vulnerabilities.

The public manifest contains 67 assets / 84,991,645 bytes at SHA-256
`f7e9c1fbda2f5af50a4829fdcd2a09a0393752a569aaf29ef94ee06f4e56f711`.
The deterministic public-tree digest covers 70 files / 87,338,782 bytes at
SHA-256
`368aa0aa3249afb7f0fe23e7835c45b579c30a342dda593437a3d2a058facc4b`;
the 24,538-file / 271,542,874-byte production tree is
`3669f831cb2e6027eb7df6505286d8082cf1a0250086d9952b29846924a99215`.
A clean replay reproduces both tree digests exactly. A separate scan of the
five private identifiers in this cohort finds zero exact matches in either
public tree.

An initial retries-disabled full matrix reached 520 passes before three
Chromium-control stalls; trace inspection found a delayed navigation whose
HTTP response completed in 69 milliseconds while the expected page content
was present. All three unchanged scenarios passed together in 12.2 seconds.
A subsequent CI-policy run completed the desktop and phone projects with six
isolated control stalls recovered on retry, but its process handle disappeared
after tablet testing began, so it is not treated as a terminal full-matrix
result. The clean replacement tablet run passed 680/680 in 8.0 minutes with no
retries. No historical-evidence assertion failed in these runs. The
independent GitHub Test, pull request, Pages deployment and pinned-live checks
remain pending and will provide the authoritative complete 2,040-case gate.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-four-alice-b-clem-through-ira-l-clements-pathways_batch-429_2026-09-06.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npm run test:e2e
npm run check:links
cd ..
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `bash scripts/rebuild-all.sh`. The goal remains active and
incomplete, with 19,870 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
