# Batch 453 release verification

2026-09-09 UTC. **Local release candidate; complete local QA passed and
independent release checks pending.** This release covers PDF page 89 rows
16-25, Agent Confidential through Groff Conklin, in Box 138 at location
230/86/29/01.

## Research

Page 89 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. The first row is printed
as `Confidential | Agent` with the note `no real n`; neither the name nor note
is expanded. Eugene A Confrey's rank remains `T-5`. Six- and seven-digit
identifier forms remain literal and private; they were not padded or replaced.
The source row and normalized identity remain separate throughout the public
projection.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Garret E Conklin is the only
cohort member with an eligible eight-digit indexed identifier; it produced no
Army identifier hit. Eugene A Confrey and Melvin R Conger's shorter literal
values likewise produced no identifier hit. The full-name scan found Eugene A
and Eugene F Confrey rows, four Melvin Conger rows including one Melvin R row,
and a Charles R rather than Charles E Conkey row. No private identifier links
those candidates to the OSS index, so none is assigned. Army-file non-hits are
not negative proof.

The current project CIA adapter completed one bounded public exact-name search
per person and found no new candidate. The Library of Congress adapter
completed one bounded exact-name employment search per person. Nine returned
no candidate. The remaining result was a 25 March 1946 *Evening Star*
classified advertisement containing the words “no agent; confidential.” It
identifies no person and was rejected in OCR context through an idempotent
review decision.

An official NIH search lead for Eugene Confrey could not be inspected and has
no OSS, private-identifier or Box 138 bridge; it is not evidence. A 1942 Army
candidate and secondary athlete biography for Melvin R Conger also lack an
OSS or Box 138 bridge. A 1943 newspaper page concerns Charles A Conkey, not
Charles E Conkey. These leads remain documented as rejected or unresolved and
do not populate public claims.

The CIA's official history “Edna Andrade: From the OSS to Op Art” explicitly
names science-fiction author Groff Conklin among artists working together in
OSS. The distinctive exact name and direct OSS bridge support a high-confidence
identity, not a confirmed identity, because no unique private identifier or
personnel-file linkage is available.

Princeton University Library finding aid C1656 identifies Groff Conklin
(1904-1968) as the same science-fiction author and states that he began his
career as a fiction editor and assistant manager at New York's Doubleday
Bookstore. It separately dates the anthology records from 1929. The bookstore
role is therefore published as high-confidence, documented-prewar employment.
It is not marked as immediate pre-OSS affiliation or last civilian employer,
and no employment dates are invented.

Agent Confidential, Louise E Congdon and Dolores S Conger require archival
review. Eugene A Confrey, Gerard M Congdon, Eleanor F Congleton, Charles E
Conkey and Garret E Conklin need identity review. Melvin R Conger remains
ambiguous and needs identity review. Groff Conklin has a documented-prewar-
employer result but still requires the Box 138 file to establish the immediate
and last-civilian affiliations.

Every person received recorded NARA index context, complete Army comparison,
current official CIA and Library of Congress checks, exact-name OSS and
meaningful variant searches, employment and occupation queries, and applicable
institutional, obituary, directory, military, newspaper and archival
discovery. No authenticated NARA Catalog API request was used.

The reviewed bundle adds five citation records, one organization, one
affiliation, two claims with four source links, ten person updates and ten
saved reviewed-public research attempts. The CIA and Library of Congress
adapters add twenty sanitized project-side attempts. One Library of Congress
candidate decision remains separately auditable. Imports were repeated
idempotently, and the complete reconstruction from the frozen PDF reproduced
all table counts and generated public data. See
`research/batch-453-discovery-checkpoint.md` for the full adjudication,
rejected leads and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,304 / 23,940 active people | 17.9783% |
| Verified-employer coverage | 227 / 23,940 active people | 0.9482% |
| Verified-affiliation coverage | 512 / 23,940 active people | 2.1387% |
| Archival disposition assessed | 4,259 / 23,940 active people | 17.7903% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,241 commissioned,
5,741 noncommissioned and 15,958 indeterminate. Identity: 834 confirmed, 633
high confidence, 143 probable, 107 ambiguous, 79 conflicting and 22,144
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,636 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 157 |
| needs_temporal_review | 14 |
| verified_employer_found | 214 |
| documented_prewar_employer_found | 84 |
| occupation_only_found | 758 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,738 |
| completed | 128 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,014 | 35 |
| high | 1,293 | 295 |
| medium | 999 | 96 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

Personnel categories: 1,504 civilian professional or administrative; 2,114
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps;
86 commissioned naval; 4,062 enlisted Army; 5 enlisted Marine Corps; 64
enlisted naval; 253 foreign or Allied military; 4 temporary/contract/special;
6 warrant; and 15,832 unknown or indeterminate.

Inventory: 553 organizations, 1,698 affiliations, 3,493 claims, 8,104 claim-
source links, 4,084 citation records and 5,621 attempts/plans. Attempt outcomes
are 1,901 `source_reviewed`, 218 `candidate_found`, 685
`candidate_rejected`, 2,230 `no_result` and 587 `planned`. There are 1,890
provisional source-document keys, 1,391 distinct stable URLs and 83 conflicts.
The unresolved export has 22,756 data rows; the pull list 23,764; and the
review queue 23,940.

Public projection: 23,940 people, 541 organizations, 1,687 affiliations, 3,393
published, qualified or conflict-visible claims, 2,925 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 541
organization rows, 1,687 affiliation rows and 2,925 citation rows.

## Local QA and resume

SQLite `quick_check` returns `ok`, foreign keys pass, all 93 Python unit tests
pass in 4.139 seconds, and `npm audit --audit-level=high` reports zero
vulnerabilities. The deterministic 200-profile structural audit passes; it is
not independent historical rereview, and the women stratum remains unavailable
without sourced classification.

The Pages-configuration build reports 77 Astro files with zero errors,
warnings or hints and generates 24,489 HTML pages. All internal links resolve;
49,693 external destinations are inventoried, not all visited. All five
distinct Batch 453 citation destinations returned HTTP 200 in bounded checks.
The focused Batch 453 browser suite passes all fifteen checks across desktop,
phone and tablet. A post-replay sandbox run could not bind its local test
server (`EPERM`); the immediate permitted rerun passed all fifteen checks. The
complete retries-disabled browser/accessibility matrix
passes 2,316/2,316 in one uninterrupted 17.4-minute run across those three
layouts.

Identifier audits cover all 24,561 built artifacts and all 70 public-tree
files, 12,926 normalized identifiers, 120 formatted variants and 1,092
candidate substring coincidences with zero unexpected boundary, aggregate or
manifest-size matches. `.env` and `.env.*` remain ignored, only
`.env.example` is tracked, and a repository scan finds zero populated
`NARA_API_KEY` assignments.

The public manifest contains 67 assets / 86,948,639 bytes at SHA-256
`1770ef2bfe77072cc0cf510d6f37ceea43473b875ede008f770fcefabf568d89`.
The deterministic public-tree digest covers 70 files / 89,295,772 bytes at
SHA-256
`0f074f2f974f2885a8b6673dd742c2a1a8e93e482db863305563ef40406cae2c`;
the Pages-configured 24,561-file / 274,429,819-byte production tree is
`bc55006a6f8829143f30ae55a89892d85cc291064644ff1ecf5d21e497bec7bc`.
Two consecutive fresh Pages-configured builds and the complete frozen-input
replay reproduce both tree digests and file counts exactly. The replay
completed every data stage, refreshed 276 exact-lock dependencies, and rebuilt
the complete static site.

Batches 443-445 remain in open, mergeable PR 198 with successful Test run
`34354744527`. Batch 446 remains in open, mergeable PR 199 with successful Test
run `34361660741`. Batch 447 remains in open, mergeable PR 200 with successful
Test run `34368546155`. Their required merge order is PR 198, PR 199, then PR
200. Batches 448-453 are complete local release candidates layered after PR
200. The live site was checked on 2026-09-09 and still serves Batch 442 data:
4,196 researched people, 505 verified affiliations and 222 verified employers.
External publication requires explicit authorization for that PR chain; the
prior Batch 448 push was stopped by the privacy safety gate because the branch
contains private research material. Each later release must pass independent
Test, Pages deployment and pinned-live verification before being called
deployed.

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-09_batch453.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-nine-agent-confidential-through-groff-conklin-pathways_batch-453_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m oss_research audit-profiles --sample-size 200
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch453.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. Continue research at
PDF page 89 row 26. The goal remains active and incomplete, with 19,636 active
people still `not_started`. Rotate the previously exposed credential before
authenticated NARA work; public-source research is not blocked. Unresolved
methodological issues remain: the automated profile audit is structural rather
than independent historical validation, source-document identity normalization
is provisional, external links are inventoried rather than exhaustively
visited, and most personnel files still require archival examination.
