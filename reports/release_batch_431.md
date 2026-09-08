# Batch 431 release verification

2026-09-08 UTC. **Local release candidate; independent release checks pending.**
This report covers ten source records on PDF page 84 rows 26-35, Howard J
Clifton through DeWitt Clinton, spanning Boxes 129-130 at location
230/86/28/07.

## Research

Page 84 was rendered at 150 dpi. Every printed name, initial, blank or stated
rank, private identifier or blank, box, note and location in the cohort was
visually matched to the immutable database before research. The page directly
prints `Sp 2/C` and `Navy` for Dean A Cline; no specialty or unit is inferred.
Only three eligible private-identifier shapes were compared with the official
Army file. The reviewed evidence bundle adds five citations, no new
organizations, three affiliations, seven claims, twenty claim-source links,
ten person updates and ten saved research attempts.

A complete transient scan of 9,200,232 fixed-width Army merged-file records
found three exact-name Howard J Clifton rows, one William R Clifton row and one
Sheldon R Cline row. Their private identifiers select exactly one row apiece.
The selected records support confirmed identities and enlisted Army
classification. Official code documentation labels their Army-entry
occupations `Sales clerks`, `Attendants, recreation and amusement, n.e.c.` and
`Salesmen, to consumers`. Each observation is published at medium confidence
with uncertain timing. None names an employer, identifies a workplace or
establishes an immediate pre-OSS sequence. The full identifiers and raw Army
rows remain private and are absent from public artifacts.

The Army comparison produced no exact-name row for Mary F Clifton, A C Cline,
Dean A Cline, Jeraldine E Cline, Ray S Cline, Walter B Cline or DeWitt
Clinton. Those non-hits are not negative proof because the file is incomplete
and is neither a Navy register nor a comprehensive OSS roster. Initials were
not expanded, and the indexed spelling `Jeraldine` remains unchanged.

Ray S Cline's existing Library of Congress chronology was re-audited. It
continues to support a Harvard junior fellowship in 1941-1942, Department of
the Navy cryptanalysis in 1942-1943 and OSS service beginning in 1943. Harvard
remains a professional affiliation, not an employer; the Navy role remains a
government assignment, not a civilian employer. Ray's prior
`verified_employer_found` workflow status was therefore corrected to
`requires_archival_review`, while the valid high-confidence affiliation claims
remain unchanged. The status count and evidence-derived verified-employer
count are different measures; this correction reduces the former without
changing the latter.

An official NARA Director's Office microfilm roll list was downloaded and PDF
physical page 137, internal page 134, was rendered at 150 dpi and visually
inspected. Roll 87, frame 3, names `DeWitt Clinton` among people mentioned for
photographs dated 22 August 1944 near Besancon, France. The distinctive exact
name and explicit OSS archival context support a probable identity lead, but
the entry gives no middle name, identifier, role, occupation, unit or pre-OSS
chronology. It is published only as a qualified identity claim. DeWitt Clinton
Poole and other search collisions remain rejected rather than merged.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional archives, obituaries, directories,
newspapers, the current Library of Congress API, official NARA context and a
complete Army merged-file comparison when applicable were recorded for every
person. Library of Congress result counts were retained for discovery only and
supplied no identity or employer bridge. Commercial people finders, sensitive
living-person data, unsourced genealogy, cemetery namesakes, search snippets
and unrelated name combinations were rejected as final evidence. All five
citation destinations returned HTTP 200 in bounded automated HEAD checks. No
authenticated NARA Catalog request was used and no access restriction or
CAPTCHA was bypassed.

See `research/batch-431-discovery-checkpoint.md` for the exact cohort, search
chronology, candidate adjudication, rejected leads and next archival actions.
Research completion here means a saved, reviewable outcome, not that a prior
employer has been disproved. All ten records remain on the archival pull list.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,089 / 23,940 active people | 17.0802% |
| Verified-employer coverage | 218 / 23,940 active people | 0.9106% |
| Verified-affiliation coverage | 499 / 23,940 active people | 2.0844% |
| Archival disposition assessed | 4,044 / 23,940 active people | 16.8922% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,238 commissioned,
5,675 noncommissioned and 16,028 indeterminate. Identity: 776 confirmed, 611
high confidence, 131 probable, 104 ambiguous, 79 conflicting and 22,240
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,851 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 142 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 72 |
| occupation_only_found | 701 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,614 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 956 | 35 |
| high | 1,249 | 280 |
| medium | 912 | 83 |
| low | 96 | 1 |
| conflicting | 90 | 2 |

There are 3,935 citation records, 1,831 legacy document keys that are not
certified unique historical documents, and 1,341 distinct stable URLs.
Inventory: 532 organizations, 1,607 affiliations, 3,303 claims, 7,571
claim-source links and 5,311 attempts/plans. Attempt outcomes: 1,812
`source_reviewed`, 199 `candidate_found`, 650 `candidate_rejected`, 2,063
`no_result` and 587 `planned`. There are 1,612 people with stored claims and
1,532 with public or conflict-visible claims. Composite unresolved export:
22,831 data rows plus header. Conflict union: 83. Pull list: 23,768 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 520 organizations, 1,596 affiliations, 3,204
published, qualified or conflict-visible claims, 2,779 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 1,596
affiliation rows and 2,779 citation rows.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduces the exact Batch 431 counts. SQLite integrity and
foreign keys pass. All 93 Python tests pass in 4.134 seconds; test output is
clean. The generated 200-profile structural audit passes; it is not
independent historical re-review, and the women stratum remains unavailable
without sourced classification.

The exact Pages-configuration build contains 24,468 HTML pages and 24,540
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,623 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,540 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,085 candidate substring coincidences with zero
unexpected boundary, aggregate or manifest-size matches. The corrected
focused Batch 431 browser suite passes all twelve checks across desktop, phone
and tablet twice, most recently in 6.9 seconds after the deterministic rebuild.
The first corrected run completed in 8.1 seconds. An earlier run produced eight
passes and four
test-harness failures: three expected a private identity note that is
intentionally absent from the rendered interface, and one long tablet search
loop stalled during teardown. The test was corrected without changing data or
application behavior; it still validates the note in generated private-safe
public data, every one of the ten source rows, identifier masking and a
representative rendered search. The dependency audit reports zero
vulnerabilities.

The public manifest contains 67 assets / 85,140,258 bytes at SHA-256
`45bd15e95b9ff6b1cf44e9587a94bfc4d43e4759f962fc20d973e1deb5c6cdb7`.
The deterministic public-tree digest covers 70 files / 87,487,391 bytes at
SHA-256
`a13e86640345d36ba22474848e968282f4c19a2477a17c8c1d02992c0e7971bf`;
the 24,540-file / 271,771,224-byte production tree is
`719691e2a53b064bf2f6375c899ffa1b3cd4c5d9cc1ff3b052a9d2a51fdac9f5`.
Two consecutive exact Pages-configuration builds reproduce both tree digests
and file counts.
A clean replay regenerated the database, reports and public projection before
the restricted npm install process ended with npm's internal `Exit handler
never called!` error. Repeating only dependency installation with permitted
network access succeeded for 288 packages with zero vulnerabilities; the
exact Pages build then produced the counts and digests above. A second
projection and build must reproduce them before the branch is released.

Independent Test, pull-request merge, Pages deployment and pinned-live
verification remain pending at this release-candidate stage.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-four-howard-j-clifton-through-dewitt-clinton-pathways_batch-431_2026-09-08.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch431.spec.ts
npm run check:links
cd ..
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `bash scripts/rebuild-all.sh`. The goal remains active and
incomplete, with 19,851 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
