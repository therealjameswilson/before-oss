# Batch 412 release verification

2026-09-05 UTC. **Released and pinned-live verified.** This
report covers the ten people on PDF page 80 rows 20-29, Geoffrey Christensen
through Mary W. Christian, all in Box 123.

## Research

The full page was rendered at 150 dpi and all ten printed rows were visually
matched to the database before research. The reviewed evidence bundle adds
four official citations, no organization, one affiliation, two claims, five
claim-source links, ten person updates and ten saved research attempts.

Chester Christian receives a high-confidence identity and a visibly qualified,
medium-confidence occupation observation. His exact indexed name and exact
private identifier match an official Army entry dated 18 August 1942 whose
grade field reads private and whose occupation value is 781. The NARA code
list, physical page 175 / printed XVIII, labels 7-81 “Mechanics and repairmen,
motor vehicle.” That broad group is not converted into a named employer,
specific workplace, employment date, immediate pre-OSS affiliation or last
civilian employer. The private identifier is masked publicly, and the profile
marks the temporal relationship to OSS service as uncertain.

The other nine people have no accepted external identity or affiliation claim
and are routed to Box 123. Mary Walker Christian's American Red Cross obituary
remains a rejected, unpublished lead for Mary W. Christian because it provides
no OSS, box or second-identifier bridge. A Rochester directory namesake for
Louise E. Christian and unbridged Army namesakes for Hal S. Christensen,
Robert J. Christensen and Christian R. Christenson likewise remain unassigned.

The public Catalog page for NAID 1263923 supplied an unrestricted 176 MB Army
enlistment bulk file. All 9,200,232 fixed-width rows were scanned once without
an API key. No raw record, response body, archive or full identifier was
retained. Eligible exact-identifier checks found Chester's bridge; the printed
identifiers for Norris A. Christensen and Robert J. Christensen were absent.
That absence is not treated as negative proof. Six- and seven-digit values were
not padded, and names alone were not used to select among namesakes.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, obituary and institutional searches, and targeted
newspaper/Library of Congress discovery checks were completed for every
person. All four cited destinations returned HTTP 200 in the final availability
check. No authenticated NARA Catalog request or exposed credential was used.

See `research/batch-412-discovery-checkpoint.md` for the search chronology,
bulk-file adjudication, rejected leads and next archival actions. The structured
bundle retains each person's queries, reviewed-source count, rejection reasons
and bounded outcome. Research completion here means a saved, reviewable
outcome, not that a prior employer has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,902 / 23,940 active people | 16.2991% |
| Verified-employer coverage | 214 / 23,940 active people | 0.8939% |
| Verified-affiliation coverage | 491 / 23,940 active people | 2.0510% |
| Archival disposition assessed | 3,855 / 23,940 active people | 16.1028% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,232 commissioned,
5,622 noncommissioned and 16,086 indeterminate. Identity: 742 confirmed, 577
high confidence, 128 probable, 70 ambiguous, 72 conflicting and 22,351
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 20,038 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 209 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 651 |
| conflicting_sources | 71 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,535 |
| completed | 123 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 921 | 35 |
| high | 1,199 | 275 |
| medium | 852 | 82 |
| low | 73 | 1 |
| conflicting | 83 | 2 |

There are 3,808 citation records, 1,786 legacy document keys that are not
certified unique historical documents, and 1,302 distinct stable URLs.
Inventory: 523 organizations, 1,533 affiliations, 3,128 claims, 7,105
claim-source links and 5,121 attempts/plans. Attempt outcomes: 1,740
`source_reviewed`, 160 `candidate_found`, 624 `candidate_rejected`, 2,010
`no_result` and 587 `planned`. There are 1,513 people with stored claims and
1,454 with public claims. Composite unresolved export: 22,888 data rows plus
header. Conflict union: 76. Pull list: 23,769 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 511 organizations, 1,522 affiliations, 3,052
published/qualified/conflict-visible claims and 2,668 public citations.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 412 counts and byte-identical public
tree. SQLite integrity and foreign keys pass. All 90 Python tests pass in 4.285
seconds; existing connection-cleanup ResourceWarnings remain visible. The
generated 200-profile structural audit passes; it is not independent historical
re-review, and the women stratum remains unavailable without sourced
classification.

The exact Pages-configuration build contains 24,459 HTML pages and 24,531
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,587 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,531 artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,085 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. The six Batch 412 focused checks
pass across desktop, phone and tablet on the final build.

The complete 1,761-case local browser/accessibility matrix passed 1,761/1,761
in 19.2 minutes across desktop, phone and tablet with retries disabled.
Consecutive final production builds match byte-for-byte.

Independent GitHub Test `33939013769` passed in 34 minutes 41 seconds. PR 169
merged as `c9d7906660ecd7d08f7dd20ad9f6d612ea6c24ea`; Pages run
`33940662130` succeeded. Pinned verification against source commit
`4bf9e80b6a258c6658c8d03b0c8a483960f260e5` matched all 67 assets /
83,888,460 bytes, seven core routes and all ten direct cohort profiles at
`https://therealjameswilson.github.io/before-oss/`.

Final manifest: 67 assets / 83,888,460 bytes; SHA-256
`cac12dd0e57bb8f21d75ff38b7ce1bb5a1d95609f8c0aae80bd9f8fc158ff7ab`.
Public tree: 70 files, SHA-256
`1aa842c778e49847d69699fcff9b9e6ec9e8e993b37e61a5936e6f9b5a8148e4`.
Production tree: 24,531 files, SHA-256
`d83739b9d25e627c2ef844a039064303b44fa9f9da3278c7c14944ec0fd19db9`.
Tree digests use sorted relative paths, NUL separators and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-geoffrey-christensen-through-mary-w-christian-pathways_batch-412_2026-09-05.json
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
incomplete, with 20,038 active people still `not_started`. Rotate the previously
exposed credential before authenticated NARA work; public-source research is
not blocked. Unresolved methodological issues remain: automated profile audit
is structural rather than independent historical validation, source-document
identity normalization is provisional, external links are inventoried rather
than exhaustively visited, and most personnel files still require archival
examination.
