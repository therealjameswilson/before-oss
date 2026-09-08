# Batch 430 release verification

2026-09-08 UTC. **Local release candidate; independent release checks pending.**
This report covers ten source records on PDF page 84 rows 16-25, Joseph E
Clements through David H Clift, all in Box 129 at location 230/86/28/07.

## Research

Page 84 was rendered at 150 dpi. Every printed name, initial, blank rank,
private identifier or blank, box, blank note and location in the cohort was
visually matched to the immutable database before research. Only three
eligible private-identifier shapes were compared directly with the official
Army file. Edmund C Cleveland's five-digit value was preserved unchanged and
was not padded, truncated or interpreted as an officer number. The reviewed
evidence bundle adds seven citations, three organization references including
one existing Army organization, six affiliations, twelve claims, thirty-four
claim-source links, ten person updates and ten saved research attempts.

Exact private-identifier matches support confirmed identities and enlisted
Army classification for Harold V Cleveland, Elizabeth A Clifford and David H
Clift. The Elizabeth match uses a punctuation-normalized identifier to select
a fixed-width Women's Army Corps row whose first name is compressed in the
source. Their official Army-entry records carry occupation values 081, 104 and
023. Rendered official code pages define those as `Advertising agents`,
`Clerks, general` and `Librarians`. Each is published as a qualified,
medium-confidence observation with uncertain timing. These categories name no
employer and do not establish immediate pre-OSS chronology.

The American Library Association Archives record for David H Clift states that
he began reference work at the New York Public Library after receiving his
library degree in 1931, became assistant to the Columbia University Library
director in 1937 and was drafted after five years. It then explicitly places
an Army hospital-orderly assignment before his OSS work. The project therefore
publishes three distinct high-confidence pathway claims: New York Public
Library as earlier documented prewar employment, Columbia University Library
as the strongly date-bounded last civilian employer, and the Army hospital-
orderly assignment as the immediate pre-OSS military affiliation. His
education remains separate from employment, and no postwar role is projected
backward.

An official 1 November 1945 War Department Strategic Services Unit dispatch
lists Margaret Cleveland and Elizabeth Clifford among vouchered civilians
being transferred to Nuremberg war-crimes work. Exact first and surname plus
the official SSU context support only a probable match for Margaret because
the record supplies neither her middle initial nor a private identifier. The
claim is visibly qualified. For Elizabeth, the dispatch provides later context
after her identifier-confirmed Army record. Neither person's late-1945 status
is treated as a prewar employer or as proof of the index-time personnel
category.

None of four exact-name Joseph E Clements Army rows can be selected without a
source identifier or a second identity bridge, so all four remain rejected
rather than merged. Ysobel Clements, Edmund C Cleveland, Eleanor E Cleveland,
Zito Cleveland and Acice C Clifford remain unresolved. The unusual printed
spelling `Acice` was visually confirmed and preserved; a search-engine
substitution of `Alice` was rejected as an unsupported correction. The 1946
Official Army Register contains no Edmund C Cleveland entry, but this bounded
negative check is not treated as proof that the person did not serve or as an
interpretation of the five-digit value.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional archives, obituaries, directories,
newspapers, the current Library of Congress API, the 1946 Official Army
Register and a complete 9,200,232-row Army merged-file comparison when
applicable were recorded for every person. Library of Congress result counts
were used for discovery only and supplied no identity or employer bridge. All
seven citation destinations returned HTTP 200 in bounded automated HEAD
checks. No authenticated NARA Catalog request was used and no access
restriction or CAPTCHA was bypassed.

See `research/batch-430-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved. All ten records remain on the Box 129 pull list.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,080 / 23,940 active people | 17.0426% |
| Verified-employer coverage | 218 / 23,940 active people | 0.9106% |
| Verified-affiliation coverage | 499 / 23,940 active people | 2.0844% |
| Archival disposition assessed | 4,035 / 23,940 active people | 16.8546% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,238 commissioned,
5,672 noncommissioned and 16,030 indeterminate. Identity: 773 confirmed, 611
high confidence, 130 probable, 104 ambiguous, 79 conflicting and 22,243
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,860 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 142 |
| needs_temporal_review | 13 |
| verified_employer_found | 211 |
| documented_prewar_employer_found | 72 |
| occupation_only_found | 698 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,607 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 953 | 35 |
| high | 1,249 | 280 |
| medium | 908 | 83 |
| low | 96 | 1 |
| conflicting | 90 | 2 |

There are 3,930 citation records, 1,830 legacy document keys that are not
certified unique historical documents, and 1,340 distinct stable URLs.
Inventory: 532 organizations, 1,604 affiliations, 3,296 claims, 7,551
claim-source links and 5,301 attempts/plans. Attempt outcomes: 1,808
`source_reviewed`, 198 `candidate_found`, 650 `candidate_rejected`, 2,058
`no_result` and 587 `planned`. There are 1,608 people with stored claims and
1,528 with public or conflict-visible claims. Composite unresolved export:
22,833 data rows plus header. Conflict union: 83. Pull list: 23,767 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 520 organizations, 1,593 affiliations, 3,197
published, qualified or conflict-visible claims, 2,774 public citations and 26
profile shards.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduces the exact Batch 430 counts. SQLite integrity and
foreign keys pass. All 93 Python tests pass in 4.185 seconds; test output is
clean. The generated 200-profile structural audit passes; it is not independent
historical re-review, and the women stratum remains unavailable without
sourced classification.

The exact Pages-configuration build contains 24,468 HTML pages and 24,540
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,622 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,540 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,082 candidate substring coincidences with zero
unexpected boundary, aggregate or manifest-size matches. The focused Batch
430 browser suite passes all twelve checks across desktop, phone and tablet in
21.2 seconds. An earlier run produced eleven passes and one local Chromium-
control stall; its trace showed the final desktop multi-search action stalled
before any network request or console error, and the exact unchanged scenario
passed alone. No evidence or interface assertion failed. The dependency audit
reports zero vulnerabilities.

The public manifest contains 67 assets / 85,087,639 bytes at SHA-256
`6f74b988cf3de63eb80921772be7ac784cc22ae5f79acc4a1d85a0c54ab7973c`.
The deterministic public-tree digest covers 70 files / 87,434,770 bytes at
SHA-256
`31f6d600db57e490f0f264ff6646916308ee39138a85ed6973fbbf6e56af8bbf`;
the 24,540-file / 271,692,627-byte production tree is
`480e4ff313d04f22f858c7d7938758aaa41cb7d2d0fe3f710a75d55291d14ac6`.
A clean replay regenerated the database and public projection before the
restricted npm install process ended with npm's internal `Exit handler never
called!` error. Repeating only the dependency install with network access
succeeded with zero vulnerabilities; the exact Pages build then reproduced
both tree digests and file counts above.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-four-joseph-e-clements-through-david-h-clift-pathways_batch-430_2026-09-08.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research audit-profiles
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npx playwright test tests/batch430.spec.ts
npm run check:links
cd ..
python3 scripts/hash_tree.py site/public site/dist
```

Full replay: `bash scripts/rebuild-all.sh`. The goal remains active and
incomplete, with 19,860 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
