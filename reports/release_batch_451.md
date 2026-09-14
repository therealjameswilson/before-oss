# Batch 451 release verification

2026-09-09 UTC. **Local release candidate; complete local QA passed and
independent release checks pending.** This release covers PDF page 88 rows
42-46 and page 89 rows 1-5, Charles L Conaughty through Jean O Condit, all in
Box 137 at location 230/86/29/01.

## Research

Pages 88 and 89 were rendered at 150 dpi and every printed field in the
ten-row cohort was visually compared with the immutable database. The index
prints `Josephthine M Conde`; that spelling remains recoverable and is not
silently changed to Josephine. Robert S Condie's six-digit value and Trimble C
Condict's seven-digit officer-style value remain literal and private. Neither
was padded or replaced with a value from another record.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Anthony E Concordia and
Vahram H Condayan were the only cohort members with eligible eight-digit index
identifiers. Anthony's identifier produced no hit. Vahram's identifier and
exact name produced one row dated 25 October 1944 with grade PVT. George P
Condakes produced one exact-name row dated 1 December 1942 with 1922 birth-year
and Massachusetts-residence values. Trimble C Condict produced one exact-name
row dated 16 July 1941 with 1917 birth-year and Vermont-residence values, but
its enlisted identifier differs from the number printed for the indexed first
lieutenant and is not silently substituted. Robert V and Robert E Condie are
initial mismatches for Robert S. Army-file non-hits are not negative proof.

The current project CIA adapter completed one bounded public OSS Collection
search for each person and returned no candidates. The current Library of
Congress adapter completed bounded exact-name employment searches. Twelve
newspaper-page candidates were checked at OCR-context level and rejected
through an idempotent review-decision file. Two Anthony Concordia results use
Anthony and Concordia as separate Kansas weather-station names. Ten E C Condit
results name other people or contain broken OCR for words such as condition or
air-conditioned. None is published as evidence.

George P Condakes' 1922 Army birth-year and Massachusetts-residence values
align with a detailed obituary for George Peter Condakes, born in 1922 and
associated with the Boston area. The obituary says he attended Northeastern
University before the Army draft and started in the 100th Infantry Division
before joining OSS. This unusual name and explicit chronology support a
high-confidence identity. The 100th Infantry Division is published as a
medium-confidence immediate military affiliation because the sequence
currently rests on one obituary; the Army record corroborates service but not
the unit. Northeastern is separately modeled as student status, never as an
employer. The postwar family business is outside scope.

Vahram H Condayan's exact private identifier confirms the index-to-Army match.
NARA's direct Entry 219 description independently identifies approximately
100 pages concerning Vahram H. Condayan's intelligence reporting from the
French Somali Coast, circa July 1944-October 1946, in Box 3, WN#27076. This
confirms identity and supplies a second archival target, but does not name a
pre-OSS employer. The Army row is dated after the approximate beginning of
that reporting period, so its civilian-occupation code is not presented as
pre-OSS evidence.

The University of Vermont's 1941-1942 catalogue title page and physical page
293, printed page 292, were rendered and visually inspected. The register
lists Trimble Chubb Condict, B.S. from Bucknell, as a graduate student in
education from Richmond, Vermont. The distinctive full name, state, matching
middle initial and indexed rank support high-confidence identity. University
of Vermont is published as documented prewar student status, not employment
or an immediate affiliation. The July 1941 Army entry overlaps the catalogue
period. A cached Detachment 101 transcription aligned the name and rank, but
its current public URL redirects to an unrelated domain; it is excluded from
public evidence.

Charles L Conaughty, Anthony E Concordia, Marie L Concordia, Josephthine M
Conde, Robert S Condie, E C Condit and Jean O Condit remain unresolved with
specific Box 137 questions. Four receive critical identity-review priority.
No status, occupation or employer is transferred from a cemetery namesake,
postwar item, initial mismatch, weather table or broken OCR.

Every person received recorded NARA index context, current official CIA and
Library of Congress checks, exact-name OSS and meaningful variant searches,
employment and occupation queries, and applicable institutional, obituary,
directory, military, newspaper and archival discovery. No authenticated NARA
Catalog API request was used.

The reviewed bundle adds seven citation records, three organizations, three
affiliations, six claims, eighteen claim-source links, ten person updates and
ten saved reviewed-public research attempts. The CIA and Library of Congress
adapter checks contribute twenty-nine sanitized project-side attempts. Twelve
Library of Congress candidate decisions remain separately auditable. Imports
were repeated idempotently and the complete reconstruction from the frozen
PDF reproduced all table counts and generated public data. See
`research/batch-451-discovery-checkpoint.md` for the full adjudication,
rejected leads and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,285 / 23,940 active people | 17.8989% |
| Verified-employer coverage | 226 / 23,940 active people | 0.9440% |
| Verified-affiliation coverage | 510 / 23,940 active people | 2.1303% |
| Archival disposition assessed | 4,240 / 23,940 active people | 17.7109% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,241 commissioned,
5,737 noncommissioned and 15,962 indeterminate. Identity: 830 confirmed, 632
high confidence, 143 probable, 106 ambiguous, 79 conflicting and 22,150
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,655 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 148 |
| needs_temporal_review | 14 |
| verified_employer_found | 214 |
| documented_prewar_employer_found | 83 |
| occupation_only_found | 754 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,733 |
| completed | 128 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,010 | 35 |
| high | 1,290 | 294 |
| medium | 995 | 96 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

Personnel categories: 1,504 civilian professional or administrative; 2,114
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
86 commissioned naval; 4,058 enlisted Army; 5 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,836 unknown or indeterminate.

Inventory: 551 organizations, 1,692 affiliations, 3,482 claims, 8,072 claim-
source links, 4,074 citation records and 5,561 attempts/plans. Attempt outcomes
are 1,895 `source_reviewed`, 214 `candidate_found`, 678
`candidate_rejected`, 2,187 `no_result` and 587 `planned`. There are 1,888
provisional source-document keys, 1,389 distinct stable URLs and 83 conflicts.
The unresolved export has 22,761 data rows; the pull list 23,764; and the
review queue 23,940.

Public projection: 23,940 people, 539 organizations, 1,681 affiliations, 3,382
published, qualified or conflict-visible claims, 2,917 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 539
organization rows, 1,681 affiliation rows and 2,917 citation rows.

## Local QA and resume

SQLite `quick_check` returns `ok`, foreign keys pass, all 93 Python tests pass
in 4.123 seconds, and `npm audit --audit-level=high` reports zero
vulnerabilities. The deterministic 200-profile structural audit passes; it is
not independent historical rereview, and the women stratum remains unavailable
without sourced classification.

The Pages-configuration build reports 75 Astro files with zero errors,
warnings or hints and generates 24,487 HTML pages. All internal links resolve;
49,689 external destinations are inventoried, not all visited. The focused
Batch 451 browser suite passes all fifteen checks across desktop, phone and
tablet. During the retries-disabled full 2,286-case browser/accessibility
matrix, 2,108 checks passed before the shared preview server exited, producing
85 `ERR_CONNECTION_REFUSED` infrastructure errors, one interruption and 92
unrun cases. A fresh isolated rerun of the affected tablet segment from Batches
355-451 passed 406/406 in 3.0 minutes. Combined, the two runs execute every
case in the 2,286-case matrix without a product assertion failure; this is
reported as a segmented pass, not an uninterrupted full run.

Identifier audits cover all 24,559 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers, 120 formatted variants and 1,095
candidate substring coincidences with zero unexpected boundary, aggregate or
manifest-size matches.

The public manifest contains 67 assets / 86,826,149 bytes at SHA-256
`871a5412db5dbca5fe3ac9200670520e242386d6eac92394b3ed0569e2d1b574`.
The deterministic public-tree digest covers 70 files / 89,173,290 bytes at
SHA-256
`8692f7e4b19f4253b45f84c0102288797479f7f84e8739d381a95237644094fa`;
the Pages-configured 24,559-file / 274,247,667-byte production tree is
`835c753af982c59cabcf97cb44fea448357b4a0f763d5feb92728bfe74dab360`.
Two consecutive Pages-configured builds and the subsequent complete replay
reproduced all three counts, byte totals and SHA-256 digests exactly.

Batches 443-445 are preserved in PR 198 and passed independent Test run
`34354744527`. Batch 446 is preserved in PR 199 and passed independent Test run
`34361660741`. Batch 447 is preserved in PR 200 and passed independent Test run
`34368546155`. All three PRs are open and clean, and their merge order remains
PR 198, PR 199, then PR 200. Batches 448-451 are complete local release
candidates layered after PR 200. External publication requires explicit user
authorization; the prior Batch 448 push was stopped by the safety gate because
the branch contains private research material. Each release must pass its own
independent Test, Pages deployment and pinned-live verification before being
called deployed.

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-09_batch451.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages-eighty-eight-eighty-nine-charles-l-conaughty-through-jean-o-condit-pathways_batch-451_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m oss_research audit-profiles --sample-size 200
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch451.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. Continue research at
PDF page 89 row 6. The goal remains active and incomplete, with 19,655 active
people still `not_started`. Rotate the previously exposed credential before
authenticated NARA work; public-source research is not blocked. Unresolved
methodological issues remain: the automated profile audit is structural rather
than independent historical validation, source-document identity normalization
is provisional, external links are inventoried rather than exhaustively
visited, and most personnel files still require archival examination.
