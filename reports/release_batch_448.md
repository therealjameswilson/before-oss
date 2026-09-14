# Batch 448 release verification

2026-09-09 UTC. **Local release candidate; complete local QA passed and
independent release checks pending.** This release covers PDF
page 88 rows 12-21, Lola Colonel through Don P Combe, spanning Boxes 136 and
141 at location 230/86/29/01.

## Research

Page 88 was rendered at 150 dpi and every printed field in the ten-row cohort
was visually compared with the immutable database. Joseph S Comastra's
eight-digit private identifier and the seven-digit printed values for Robert C
Colson and Don P Combe remain private and masked. The seven-digit values are
preserved literally; neither was padded or forced into an Army identifier.

The complete official Army merged file was verified at 185,043,578 compressed
bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`, then
scanned across all 9,200,232 fixed-width records. Joseph S Comastra's exact
private identifier selects the Army row named COMASTRA JOSEPH despite its
omission of the indexed middle initial. The record confirms Infantry service
and private grade at Army entry on 16 January 1941. Its civilian-occupation
value 736 is decoded from the visually inspected official NARA code list as
Chauffeurs and drivers, bus, taxi, truck, and tractor. The broad category is
published as a medium-confidence, strongly date-bounded observation, not an
employer, vehicle, route, industry, workplace or precise Army-to-OSS sequence.

One official Army row names Edward A Colson and four rows name Robert C Colson,
but none can be assigned without a second identifier or personnel-file bridge.
The other seven non-Joseph names have no exact-name row. No non-hit is treated
as negative proof because the merged file is not a comprehensive OSS, officer,
women's-service, Navy or Marine Corps roster.

A Washington Post obituary expands Frances R Colosimo to Frances Richey
Colosimo, explicitly documents World War II service as an OSS documents analyst,
and names her 1930s Washington employer and role: research technician with the
American Bottlers of Carbonated Beverages. The exact name and OSS bridge support
a high-confidence identity and high-confidence employer claim. The source does
not prove that this was her immediate or last civilian role, so the site
publishes it only as other documented pre-OSS employment. Her husband's Navy
rank is not assigned to Frances.

An obituary for Constance Colt Bassett explicitly says that she was working in
New York for the Free French at the beginning of World War II and then moved to
Washington because her language skills were needed at OSS. This supports a
high-confidence identity, an explicit immediate affiliation and the best-
supported last civilian affiliation before OSS. The source says the Free French
operated radio stations but does not say what Colt personally did, so no radio
occupation or title is inferred. The broad Free French movement is also kept
distinct from the narrower Free French Forces organization.

Norwich University identifies Harold Lee Colvocoresses (1913-1979), a 1945 Pan
American Union article carries his byline, and a scholarly archival citation
points to his 16 March 1944 correspondence in RG 229, Entry 1, Box 326. These
sources make him a probable rare-name candidate for Harold L Colvocoresses but
do not bridge him to the OSS index or state a formal employer. His identity
remains qualified and the apparent OCIAA connection remains an archival lead,
excluded from employer analytics.

Lola Colonel, Edward A Colson, Robert C Colson, Elizabeth V Colt, Gertrude L
Colvin and Don P Combe remain unresolved with specific physical-file questions.
An Elizabeth Colt in Library of Congress National Woman's Party records lacks
the middle initial and OSS bridge and remains unassigned. Every person received
recorded NARA and CIA context checks, meaningful exact-name and variant searches,
employment and occupation queries, and applicable institutional, obituary,
directory, newspaper, current Library of Congress and other archival discovery.
No authenticated NARA Catalog request was used.

The reviewed bundle adds nine citation records, two organizations, three
affiliations, eight claims, seventeen claim-source links, ten person updates and
ten saved research attempts. See `research/batch-448-discovery-checkpoint.md`
for the complete adjudication, rejected leads and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,255 / 23,940 active people | 17.7736% |
| Verified-employer coverage | 226 / 23,940 active people | 0.9440% |
| Verified-affiliation coverage | 509 / 23,940 active people | 2.1261% |
| Archival disposition assessed | 4,210 / 23,940 active people | 17.5856% |

There are 23,941 stored entities and one superseded entity; 235 possible
duplicate groups remain visible. Officer classification: 2,239 commissioned,
5,729 noncommissioned and 15,972 indeterminate. Identity: 827 confirmed, 624
high confidence, 143 probable, 106 ambiguous, 79 conflicting and 22,161
unresolved active people.

| Research status | Active people |
|---|---:|
| not_started | 19,685 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 141 |
| needs_temporal_review | 13 |
| verified_employer_found | 214 |
| documented_prewar_employer_found | 81 |
| occupation_only_found | 752 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,716 |
| completed | 127 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 1,007 | 35 |
| high | 1,281 | 294 |
| medium | 987 | 94 |
| low | 97 | 1 |
| conflicting | 90 | 2 |

Personnel categories: 1,504 civilian professional or administrative; 2,112
commissioned Army; 1 commissioned Coast Guard; 9 commissioned Marine Corps; 86
commissioned naval; 4,051 enlisted Army; 5 enlisted Marine Corps; 64 enlisted
naval; 253 foreign or Allied military; 3 temporary/contract/special; 6 warrant;
and 15,846 unknown or indeterminate.

Inventory: 545 organizations, 1,683 affiliations, 3,462 claims, 8,010 claim-
source links, 4,049 citation records and 5,481 attempts/plans. Attempt outcomes
are 1,885 `source_reviewed`, 205 `candidate_found`, 675 `candidate_rejected`,
2,129 `no_result` and 587 `planned`. There are 1,875 provisional document keys,
1,380 distinct stable URLs and 83 conflicts. The unresolved export has 22,766
data rows; the pull list 23,764; and the review queue 23,940.

Public projection: 23,940 people, 533 organizations, 1,672 affiliations, 3,362
published, qualified or conflict-visible claims, 2,892 public citations and 26
profile shards. Public downloads contain 23,940 personnel rows, 533
organization rows, 1,672 affiliation rows and 2,892 citation rows.

## Local QA and resume

SQLite `quick_check` returns `ok`, foreign keys pass, and all 93 Python tests
pass in 4.133 seconds. The deterministic 200-profile structural audit passes;
it is not independent historical rereview, and the women stratum remains
unavailable without sourced classification.

The Pages-configuration build reports 72 Astro files with zero errors, warnings
or hints and generates 24,481 HTML pages. All internal links resolve; 49,674
external destinations are inventoried, not all visited. The focused Batch 448
browser suite passes all nine checks across desktop, phone and tablet. The
complete browser and accessibility matrix passes 2,247 / 2,247 checks across
desktop, phone and tablet in 16.8 minutes. Identifier audits cover all 24,553
built artifacts and all 70 public-tree files, with zero unexpected boundary,
aggregate or manifest-size matches.

The public manifest contains 67 assets / 86,589,328 bytes at SHA-256
`389d7b7f48ae475b53be55c05cb9b2aa7beb654aa4926b59602bda4d307f18d3`.
The deterministic public-tree digest covers 70 files / 88,936,473 bytes at
SHA-256 `bde34aa092222ada7f4ba110d57f186acb778987bb2f79dd29f8975da79ab40f`;
the Pages-configured 24,553-file / 273,893,503-byte production tree is
`27a87ca00005d19d8e6c7866a918544e8245ed5d41e089f991980b2f679c2dbf`.
A second Pages-configured build after the complete browser matrix reproduced
all three counts, byte totals and SHA-256 digests exactly.

Batches 443-445 are preserved in PR 198 and passed independent Test run
`34354744527`. Batch 446 is preserved in PR 199 and passed independent Test run
`34361660741`. Batch 447 is preserved in PR 200 and passed independent Test run
`34368546155`. All three PRs are open and clean, and their merge order remains
PR 198, PR 199, then PR 200. Merging and deployment require explicit user
approval; Batch 448 must follow them and pass its own independent Test, Pages
deployment and pinned-live verification.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-eight-lola-colonel-through-don-p-combe-pathways_batch-448_2026-09-09.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch448.spec.ts
npm run check:links
cd ..
python3 scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `PUBLIC_SITE_URL=https://therealjameswilson.github.io
PUBLIC_BASE_PATH=/before-oss bash scripts/rebuild-all.sh`. The goal remains
active and incomplete, with 19,685 active people still `not_started`. Rotate
the previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: the automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
