# Batch 452 release verification

2026-09-09 UTC. **Local release candidate; complete local QA passed and
independent release checks pending.** This release covers PDF page 89 rows
6-15, Edward A Condon through William J Coneys, in Boxes 137-138 at location
230/86/29/01.

## Research

Page 89 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. All ten rows have blank
printed rank and notes fields. Jack G Condon's six-digit value and Richard S
Condon's seven-digit value remain literal and private; neither was padded or
replaced. The source row and normalized identity remain separate throughout
the projection.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Four eligible eight-digit
index identifiers produced exact identifier-and-name matches:

- Edward A Condon entered 5 March 1943 as a private with civilian-occupation
  value 992, which NARA's official code list defines as Students.
- William A Condon entered the Enlisted Reserve Corps 24 July 1942 as a
  private with civilian-occupation value 524, Operators, construction
  machinery. A plainly impossible birth-year field in the converted Army row
  is withheld, documented as damage and not used for identity.
- Charles W Cone entered 27 May 1943 as a private with civilian-occupation
  value 992, Students.
- Edward T Cone entered 14 October 1942 as a private with civilian-occupation
  value 024, Musicians and teachers of music, and a 1917 birth-year value.

These matches establish confirmed index-to-Army identities and enlisted Army
classification. The occupations are published as strongly date-bounded
historical categories, not employers and not proof of an immediate OSS
predecessor.

Jack G Condon's literal six-digit value and Richard S Condon's literal
seven-digit value produced no Army identifier hit. Seven broad Jack Condon
rows and seventeen broad Richard Condon rows have different middle initials.
Alma P Coneby, Lucien E Conein and Leonard R Coneley have no exact-name Army
row. William J Coneys has one exact full-name Army candidate, but no private
identifier joins it to the index, the converted birth-year field is impossible
for its 1942 entry, and namesake ambiguity remains. It stays a rejected
candidate. Army-file non-hits are not negative proof.

The current project CIA adapter completed one bounded public OSS Collection
search per person and found no new candidate. The Library of Congress adapter
completed one bounded exact-name employment search per person. Seven newspaper
pages were inspected in OCR context and rejected through an idempotent review
file: five Edward A Condon results concern physicist Edward U. Condon or
retired Major Edward S. Condon, one Charles W Cone result concerns painter
Charles R. Conely, and one William J Coneys page does not contain the name in
its OCR. None is published as identity or employment evidence.

Princeton University's detailed institutional biography identifies Edward T.
Cone as born in 1917, Princeton class of 1939, recipient of an MFA in music in
1942, and a wartime member of the Army's Office of Strategic Services. The
private-identifier match, birth year, music field and explicit OSS bridge
confirm that the indexed person is Edward Toner Cone. Princeton is modeled as
high-confidence student status ending in 1942, not employment. His faculty
appointment began in 1946. The Army occupation group remains separate and
qualified because it does not establish paid work or a named employer.

Lucien E Conein already had reviewed high-confidence evidence. The contiguous
cohort review found no contradiction and preserves, without duplication, five
existing claims: an unnamed Kansas City printer as last civilian employer, an
Army officer-candidate pathway as the immediate pre-OSS affiliation, and
earlier Kansas National Guard and French Army service. The employer is not
given a name the sources do not supply.

Edward A Condon, William A Condon, Charles W Cone and Edward T Cone now have
qualified occupation or student findings. Jack G Condon, Richard S Condon and
William J Coneys need critical identity review. Alma P Coneby and Leonard R
Coneley remain unresolved with high-priority Box 138 questions. No status,
occupation or employer is transferred from an initial mismatch, famous
namesake, painter, damaged converted value or broken OCR.

Every person received recorded NARA index context, complete Army comparison,
current official CIA and Library of Congress checks, exact-name OSS and
meaningful variant searches, employment and occupation queries, and applicable
institutional, obituary, directory, military, newspaper and archival
discovery. No authenticated NARA Catalog API request was used.

The reviewed bundle adds five citation records, one organization, five
affiliations, nine claims, twenty-eight claim-source links, ten person updates
and ten saved reviewed-public research attempts. The CIA and Library of
Congress adapters add twenty sanitized project-side attempts. Seven Library of
Congress candidate decisions remain separately auditable. Imports were
repeated idempotently and the complete reconstruction from the frozen PDF
reproduced all table counts and generated public data. See
`research/batch-452-discovery-checkpoint.md` for the full adjudication,
rejected leads and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,294 / 23,940 active people | 17.9365% |
| Verified-employer coverage | 226 / 23,940 active people | 0.9440% |
| Verified-affiliation coverage | 511 / 23,940 active people | 2.1345% |
| Archival disposition assessed | 4,249 / 23,940 active people | 17.7485% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,241 commissioned,
5,741 noncommissioned and 15,958 indeterminate. Identity: 834 confirmed, 632
high confidence, 143 probable, 106 ambiguous, 79 conflicting and 22,146
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,646 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 151 |
| needs_temporal_review | 14 |
| verified_employer_found | 214 |
| documented_prewar_employer_found | 83 |
| occupation_only_found | 758 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,735 |
| completed | 128 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,014 | 35 |
| high | 1,291 | 294 |
| medium | 999 | 96 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

Personnel categories: 1,504 civilian professional or administrative; 2,114
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
86 commissioned naval; 4,062 enlisted Army; 5 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,832 unknown or indeterminate.

Inventory: 552 organizations, 1,697 affiliations, 3,491 claims, 8,100 claim-
source links, 4,079 citation records and 5,591 attempts/plans. Attempt outcomes
are 1,900 `source_reviewed`, 217 `candidate_found`, 681
`candidate_rejected`, 2,206 `no_result` and 587 `planned`. There are 1,889
provisional source-document keys, 1,390 distinct stable URLs and 83 conflicts.
The unresolved export has 22,757 data rows; the pull list 23,764; and the
review queue 23,940.

Public projection: 23,940 people, 540 organizations, 1,686 affiliations, 3,391
published, qualified or conflict-visible claims, 2,922 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 540
organization rows, 1,686 affiliation rows and 2,922 citation rows.

## Local QA and resume

SQLite `quick_check` returns `ok`, foreign keys pass, all 93 Python unit tests
pass in 4.172 seconds, and `npm audit --audit-level=high` reports zero
vulnerabilities. The deterministic 200-profile structural audit passes; it is
not independent historical rereview, and the women stratum remains unavailable
without sourced classification.

The Pages-configuration build reports 76 Astro files with zero errors,
warnings or hints and generates 24,488 HTML pages. All internal links resolve;
49,691 external destinations are inventoried, not all visited. All five
distinct Batch 452 citation destinations returned HTTP 200 in bounded checks.
The focused Batch 452 browser suite passes all fifteen checks across desktop,
phone and tablet. The complete retries-disabled browser/accessibility matrix
passes 2,301/2,301 in one uninterrupted 17.0-minute run across those three
layouts.

Identifier audits cover all 24,560 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers, 120 formatted variants and 1,092
candidate substring coincidences with zero unexpected boundary, aggregate or
manifest-size matches.

The public manifest contains 67 assets / 86,916,674 bytes at SHA-256
`e747a5b030b76656c659985d00d397199c3fa8d97ef4e767191db025219c0679`.
The deterministic public-tree digest covers 70 files / 89,263,803 bytes at
SHA-256
`a5fd36305095fe560ec9eab758e795546893a1cfd1f93f4fead99f3168f58056`;
the clean Pages-configured 24,560-file / 273,113,549-byte production tree is
`d7b46f236eb1985cab1eeda353d9a9902e0e276204840647cc76eff3d1162b0e`.
Two consecutive fresh Pages-configured builds reproduce both tree digests and
file counts exactly. The first comparison included stale output from an
earlier dependency-install interruption and is not counted as a determinism
result. The clean full replay completed every data stage; its sandboxed
dependency refresh initially hit a transient registry DNS failure, after
which an exact-lock install restored 276 packages and reported zero
vulnerabilities.

Batches 443-445 remain in open, clean PR 198 with successful Test run
`34354744527`. Batch 446 remains in open, clean PR 199 with successful Test run
`34361660741`. Batch 447 remains in open, clean PR 200 with successful Test run
`34368546155`. Their required merge order is PR 198, PR 199, then PR 200.
Batches 448-452 are complete local release candidates layered after PR 200.
The live site was checked on 2026-09-09 and still serves Batch 442 data:
4,196 researched people, 505 verified affiliations and 222 verified employers.
External publication requires explicit authorization for that PR chain; the
prior Batch 448 push was stopped by the privacy safety gate because the branch
contains private research material. Each later release must pass independent
Test, Pages deployment and pinned-live verification before being called
deployed.

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-09_batch452.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-nine-edward-a-condon-through-william-j-coneys-pathways_batch-452_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m oss_research audit-profiles --sample-size 200
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch452.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. Continue research at
PDF page 89 row 16. The goal remains active and incomplete, with 19,646 active
people still `not_started`. Rotate the previously exposed credential before
authenticated NARA work; public-source research is not blocked. Unresolved
methodological issues remain: the automated profile audit is structural rather
than independent historical validation, source-document identity normalization
is provisional, external links are inventoried rather than exhaustively
visited, and most personnel files still require archival examination.
