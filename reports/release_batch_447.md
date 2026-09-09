# Batch 447 release verification

2026-09-09 UTC. **Local release candidate; independent release checks
pending.** This release covers PDF page 88 rows 2-11, Rose L Collins through
Peter J Colombo, spanning Boxes 135-136 at location 230/86/29/01.

## Research

Page 88 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. Five eight-digit private
identifiers and William L Collins's anomalous six-digit printed value remain
private and masked. William's value is preserved literally; it was not padded
or forced into an Army identifier.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Exact private-identifier and
name matches confirm Thomas M Collins, John E Colnon, Willard D Cologna and
Peter J Colombo as enlisted Army personnel. Thomas's broad miscellaneous food-
products-producing category, John and Willard's student statuses, and Peter's
historical checkers category are published as medium-confidence, strongly date-
bounded observations at Army entry. They are not employers and do not supply a
school, product, industry, workplace or precise OSS sequence.

Rare-name public evidence makes Yolande de Mauduit Collins a probable candidate
for Yolande D Collins and Clarence Vernon Colmorgen a probable candidate for
Clarence V Colmorgen. Neither source bridges the candidate to the indexed
personnel file, so both identities remain visibly qualified, no personnel
category is promoted, and no employer claim is published. Rose L Collins, Sara
R Collins, William L Collins and Patsy Collitti remain unresolved. William has
twenty-four exact-name Army rows but no safely assignable one; all identifier
and name non-hits are treated as non-probative because the Army file is not a
comprehensive OSS roster.

Every person received recorded NARA and CIA context checks, meaningful exact-
name and variant searches, employment and occupation queries, and applicable
institutional, obituary, directory, newspaper, current Library of Congress and
other archival discovery. The current LoC API returned a 403 access challenge;
that bounded source-access failure was recorded and not bypassed. No
authenticated NARA Catalog request was used.

The reviewed bundle adds six citation records, four affiliations, ten claims,
twenty-nine claim-source links, ten person updates and ten saved research
attempts. It adds no named employer or organization. See
`research/batch-447-discovery-checkpoint.md` for the complete adjudication,
rejected leads and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,245 / 23,940 active people | 17.7318% |
| Verified-employer coverage | 224 / 23,940 active people | 0.9357% |
| Verified-affiliation coverage | 507 / 23,940 active people | 2.1178% |
| Archival disposition assessed | 4,200 / 23,940 active people | 17.5439% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,239 commissioned,
5,726 noncommissioned and 15,975 indeterminate. Identity: 826 confirmed, 622
high confidence, 142 probable, 106 ambiguous, 79 conflicting and 22,165
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,695 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 141 |
| needs_temporal_review | 13 |
| verified_employer_found | 213 |
| documented_prewar_employer_found | 80 |
| occupation_only_found | 751 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,709 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,006 | 35 |
| high | 1,276 | 291 |
| medium | 985 | 94 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

Inventory: 543 organizations, 1,680 affiliations, 3,454 claims, 7,993 claim-
source links, 4,040 citation records and 5,471 attempts/plans. Attempt outcomes
are 1,882 `source_reviewed`, 204 `candidate_found`, 675 `candidate_rejected`,
2,123 `no_result` and 587 `planned`. There are 1,870 provisional document keys,
1,375 distinct stable URLs and 83 conflicts. The unresolved export has 22,769
data rows; the pull list 23,765; and the review queue 23,940.

Public projection: 23,940 people, 531 organizations, 1,669 affiliations, 3,354
published, qualified or conflict-visible claims, 2,883 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 531
organization rows, 1,669 affiliation rows and 2,883 citation rows.

## Local QA and resume

The complete data replay from the frozen PDF and every reviewed evidence bundle
reproduces the Batch 447 counts. SQLite `quick_check` returns `ok`, foreign keys
pass, and all 93 Python tests pass in 4.152 seconds. The deterministic 200-
profile structural audit passes; it is not independent historical rereview,
and the women stratum remains unavailable without sourced classification.

The Pages-configuration build reports 71 Astro files with zero errors, warnings
or hints and generates 24,479 HTML pages. All internal links resolve; 49,667
external destinations are inventoried, not all visited. The focused Batch 447
browser suite passes all nine checks across desktop, phone and tablet. The
complete browser and accessibility matrix passes all 2,238 checks across the
same three viewports in one uninterrupted 16.8-minute run. Identifier audits
cover all 24,551 built artifacts and all 70 public-tree files, with zero
unexpected boundary, aggregate or manifest-size matches. The lockfile install
and dependency audit report zero known vulnerabilities.

The public manifest contains 67 assets / 86,512,227 bytes at SHA-256
`a99a7c07ec51311487ea16e04b10fea0e4d448abc56edb70af40b35866dbf312`.
The deterministic public-tree digest covers 70 files / 88,859,361 bytes at
SHA-256 `52c4888236075f5be4308d40ae84c019341d2978c4fd56055f279a24dbbd2879`;
the Pages-configured 24,551-file / 273,777,474-byte production tree is
`e320b81185fccaa29baa9377c07ab3a62afef2355e9256a84cfc1820d71757ab`.
Two consecutive Pages-configured builds reproduce both tree digests and file
counts byte for byte.

Batches 443-445 are preserved in PR 198 and passed independent Test run
`34354744527`. Batch 446 is preserved in PR 199 and passed independent Test run
`34361660741`. Both PRs are open and clean, but merge still requires explicit
user approval. Batch 447 must follow them, then pass its own independent Test,
Pages deployment and pinned-live verification.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-eight-rose-l-collins-through-peter-j-colombo-pathways_batch-447_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch447.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,695 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-
source research is not blocked. Unresolved methodological issues remain: the
automated profile audit is structural rather than independent historical
validation, source-document identity normalization is provisional, external
links are inventoried rather than exhaustively visited, and most personnel
files still require archival examination.
