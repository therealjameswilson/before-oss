# Batch 450 release verification

2026-09-09 UTC. **Local release candidate; complete local QA passed and
independent release checks pending.** This release covers PDF page 88 rows
32-41, Simone J Companardi through Alfred F Conard, all in Box 137 at location
230/86/29/01.

## Research

Page 88 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. Charles R Compton's
six-digit printed value remains literal and private; it was neither padded nor
silently converted into a complete Army identifier. James M Compton's
eight-digit identifier remains research-only and masked publicly.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. James M Compton was the only
cohort member with an eligible eight-digit index identifier; it produced no
match. Charles R, James M, James R and William D Compton produced three, three,
five and six exact-name Army rows respectively, but none can be selected by
name alone. No occupation or grade from those rows is assigned to an indexed
person.

The current project CIA adapter completed one bounded public OSS Collection
search for each cohort member and returned no candidate matches. The current
Library of Congress adapter also ran bounded searches. Seven newspaper-page
candidates were checked at OCR-context level and rejected through an
idempotent review-decision file. A 1960 *Kodiak Mirror* page names James Alfred
Compton, not indexed James M or James R. The five William Compton pages name
different middle initials or lack a William D identity and OSS bridge. None is
published as evidence.

The official April 30, 1917 *Congressional Record* places Cadet Coalter Bates
Compton under the Cavalry Arm and appoints him a second lieutenant with rank
from April 20. The 2010 West Point graduate register independently records
Coalter B. Compton, Cullum number 5701, in the April 1917 class. Both pages were
rendered at 150 dpi and visually inspected. The unusual full name and two
consistent military sources support high-confidence identity and commissioned
Army classification. The cavalry appointment is deliberately labeled other
documented prewar history, not the assignment immediately before OSS; Box 137
must bridge the quarter-century gap.

Alfred F Conard has a single exact-name Army row dated 24 September 1943. Its
1911 birth-year value aligns with Grinnell College's institutional history of
Alfred Fletcher Conard, and its civilian-occupation value `022` maps through
NARA's official code list to `Lawyers and judges`. A 1940 *Washington
University Law Quarterly* byline identifies Alfred F. Conard as Assistant
Professor of Law at the University of Kansas City. Columbia University's 1942
annual report independently records the same name, title and law school. Both
PDF pages were rendered at 150 dpi and visually inspected.

The name, birth year, legal occupation and two institutional sources support a
high-confidence identity, not confirmation: no private index identifier or
direct personnel-file linkage selects the Army row. The University of Kansas
City School of Law is published as a medium-confidence, qualified candidate for
Conard's last civilian employer before Army service. The 1940-1942 evidence
precedes his September 1943 Army entry but does not exclude an intervening role
or establish his later Army-to-OSS chronology. The historical institution name
is preserved without silently substituting a modern successor. The Army coding
is separately published as an occupation and is not converted into a law-firm,
private-practice or judicial-employment claim.

Simone J Companardi, Charles R Compton, James M Compton, James R Compton,
William D Compton, Isabel L Comstedt, Anne E Comstock and Dorothy D Comstock
remain unresolved with specific Box 137 questions. An indirect Isabel
Comstedt surname lead lacks identity, OSS and employment bridges and remains
rejected. A Dorothy G Comstock Army row has the wrong middle initial and is not
assigned. Every person received recorded NARA index context, current CIA and
Library of Congress checks, meaningful exact-name and variant searches,
employment and occupation queries, and applicable institutional, obituary,
directory, newspaper and archival discovery. No authenticated NARA Catalog API
request was used.

The reviewed bundle adds nine citation records, two organizations, three
affiliations, five claims, twenty claim-source links, ten person updates and ten
saved reviewed-public research attempts. The live CIA and Library of Congress
adapter checks add twenty-one sanitized project-side attempts; raw payloads
were discarded. The regenerated durable adapter checkpoint grows by twenty-two
attempts because it also recovers one previously reviewed Batch 406 attempt
that was absent from the prior exported checkpoint. Seven Library of Congress
candidate decisions are separately auditable. See
`research/batch-450-discovery-checkpoint.md` for the complete adjudication,
rejected leads and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,275 / 23,940 active people | 17.8571% |
| Verified-employer coverage | 226 / 23,940 active people | 0.9440% |
| Verified-affiliation coverage | 510 / 23,940 active people | 2.1303% |
| Archival disposition assessed | 4,230 / 23,940 active people | 17.6692% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,241 commissioned,
5,735 noncommissioned and 15,964 indeterminate. Identity: 829 confirmed, 630
high confidence, 143 probable, 106 ambiguous, 79 conflicting and 22,153
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,665 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 144 |
| needs_temporal_review | 14 |
| verified_employer_found | 214 |
| documented_prewar_employer_found | 83 |
| occupation_only_found | 754 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,728 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,009 | 35 |
| high | 1,288 | 294 |
| medium | 992 | 96 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

Personnel categories: 1,504 civilian professional or administrative; 2,114
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps; 86
commissioned naval; 4,056 enlisted Army; 5 enlisted Marine Corps; 64 enlisted
naval; 253 foreign or Allied military; 4 temporary/contract/special; 6 warrant;
and 15,838 unknown or indeterminate.

Inventory: 548 organizations, 1,689 affiliations, 3,476 claims, 8,054 claim-
source links, 4,067 citation records and 5,522 attempts/plans. Attempt outcomes
are 1,892 `source_reviewed`, 211 `candidate_found`, 675 `candidate_rejected`,
2,157 `no_result` and 587 `planned`. There are 1,884 provisional document keys,
1,387 distinct stable URLs and 83 conflicts. The unresolved export has 22,762
data rows; the pull list 23,764; and the review queue 23,940.

Public projection: 23,940 people, 536 organizations, 1,678 affiliations, 3,376
published, qualified or conflict-visible claims, 2,910 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 536
organization rows, 1,678 affiliation rows and 2,910 citation rows.

## Local QA and resume

SQLite `quick_check` returns `ok`, foreign keys pass, all 93 Python tests pass
in 4.163 seconds, and `npm audit --audit-level=high` reports zero
vulnerabilities. The deterministic 200-profile structural audit passes; it is
not independent historical rereview, and the women stratum remains unavailable
without sourced classification.

The Pages-configuration build reports 74 Astro files with zero errors, warnings
or hints and generates 24,484 HTML pages. All internal links resolve; 49,684
external destinations are inventoried, not all visited. The focused Batch 450
browser suite passes all twelve checks across desktop, phone and tablet. The
complete browser and accessibility matrix passes 2,271 / 2,271 checks across
desktop, phone and tablet in 16.8 minutes. Identifier audits cover all 24,556
built artifacts and all 70 public-tree files, with zero unexpected boundary,
aggregate or manifest-size matches.

The public manifest contains 67 assets / 86,747,167 bytes at SHA-256
`21842871f8c77abce3ad641df9728d78427d7dea5a613a5327a26d1f7b253eff`.
The deterministic public-tree digest covers 70 files / 89,094,302 bytes at
SHA-256 `3f3d8bfbeac723b3676bea56d6371c419e1328398b2453a8cd72ee25d6d6fa43`;
the Pages-configured 24,556-file / 274,125,483-byte production tree is
`8d41a2be188ea22288b9275970f21ecfc78491e81eeeb06f327cde69910db31d`.
A second Pages-configured build reproduced all three counts, byte totals and
SHA-256 digests exactly.

Batches 443-445 are preserved in PR 198 and passed independent Test run
`34354744527`. Batch 446 is preserved in PR 199 and passed independent Test run
`34361660741`. Batch 447 is preserved in PR 200 and passed independent Test run
`34368546155`. All three PRs are open and clean, and their merge order remains
PR 198, PR 199, then PR 200. Batches 448-450 are complete local release
candidates layered after PR 200. External publication requires explicit user
authorization; the prior Batch 448 push was stopped by the safety gate because
the branch contains private research material. Each release must pass its own
independent Test, Pages deployment and pinned-live verification before being
called deployed.

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-09_batch450.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-eight-simone-j-companardi-through-alfred-f-conard-pathways_batch-450_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m oss_research audit-profiles --sample-size 200
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch450.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. Continue research at
PDF page 88 row 42. The goal remains active and incomplete, with 19,665 active
people still `not_started`. Rotate the previously exposed credential before
authenticated NARA work; public-source research is not blocked. Unresolved
methodological issues remain: the automated profile audit is structural rather
than independent historical validation, source-document identity normalization
is provisional, external links are inventoried rather than exhaustively
visited, and most personnel files still require archival examination.
