# Batch 413 release verification

2026-09-05 UTC. **Released and pinned-live verified.** This report covers the
ten people on PDF page 80 rows 30-39, Roy P. Christian through Peter A.
Christoff, all in Box 123.

## Research

The full page was rendered at 150 dpi and all ten printed rows were visually
matched to the database before research. The reviewed evidence bundle adds
four official citations, no organization, two affiliations, six claims,
fourteen claim-source links, ten person updates and ten saved research
attempts.

Gustave M. Christianson and Richard A. Christman receive high-confidence
identity matches and visibly qualified, medium-confidence occupation
observations. Gustave's exact private identifier, surname and middle initial
match an official Army entry dated 8 September 1943; the record spells his
given name `Gustav`. Richard's exact indexed name and exact private identifier
match an Army entry dated 12 May 1943. Both entry-grade fields read private.
The NARA code list, physical page 173 / printed XIV-XV, labels their codes
“Occupations in printing and publishing, n.e.c.” and “Occupations in
production of bakery products, n.e.c.” These broad groups are not converted
into named employers, workplaces, specific titles, employment dates,
immediate pre-OSS affiliations or last civilian employers. Their private
identifiers are masked publicly, and both profiles mark the temporal
relationship to OSS service as uncertain.

Two identifier/name conflicts remain visible. Christian C. Christis's exact
private identifier returns an Army entry naming Christ G. Christis, with both
the given-name form and middle initial different. Peter A. Christoff's exact
private identifier returns Peter K. Christoff. Neither Army occupation is
assigned to the indexed person, and both profiles route to critical-priority
Box 123 review.

Roy P. Christian, Waldemar C. Christian, William B. Christian, William F.
Christians, Herbert P. Christiansen and William D. Christman remain unresolved
and route to Box 123. Modern professionals, burial-index entries, unrelated
prewar people and generic newspaper hits remain rejected namesakes without an
OSS, Box 123 or second-identifier bridge.

The public Catalog page for NAID 1263923 supplied an unrestricted 185,043,578-
byte Army enlistment ZIP. Its SHA-256 was
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`.
All 9,200,232 fixed-width records were scanned once without an API key. No raw
record, response body, archive or full identifier was retained. Six- and
seven-digit index values were not padded, and a name alone was never used to
choose among candidates. Absence from the merged Army file is not treated as
negative proof. Richard's indexed T-5 rank is preserved; the earlier Army
entry grade is contextual evidence, not a replacement rank.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, obituary and institutional searches, and targeted
newspaper/Library of Congress discovery checks were completed for every
person. All four cited destinations returned HTTP 200 in the final
availability check. No authenticated NARA Catalog request or exposed
credential was used.

See `research/batch-413-discovery-checkpoint.md` for the search chronology,
bulk-file adjudication, rejected leads and next archival actions. The
structured bundle retains each person's queries, reviewed-source count,
rejection reasons and bounded outcome. Research completion here means a saved,
reviewable outcome, not that a prior employer has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,912 / 23,940 active people | 16.3409% |
| Verified-employer coverage | 214 / 23,940 active people | 0.8939% |
| Verified-affiliation coverage | 491 / 23,940 active people | 2.0510% |
| Archival disposition assessed | 3,865 / 23,940 active people | 16.1445% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,232 commissioned,
5,623 noncommissioned and 16,085 indeterminate. Identity: 742 confirmed, 579
high confidence, 128 probable, 70 ambiguous, 74 conflicting and 22,347
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 20,028 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 209 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 653 |
| conflicting_sources | 73 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,541 |
| completed | 123 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 921 | 35 |
| high | 1,201 | 275 |
| medium | 854 | 82 |
| low | 73 | 1 |
| conflicting | 85 | 2 |

There are 3,812 citation records, 1,786 legacy document keys that are not
certified unique historical documents, and 1,302 distinct stable URLs.
Inventory: 523 organizations, 1,535 affiliations, 3,134 claims, 7,119
claim-source links and 5,131 attempts/plans. Attempt outcomes: 1,744
`source_reviewed`, 160 `candidate_found`, 629 `candidate_rejected`, 2,011
`no_result` and 587 `planned`. There are 1,517 people with stored claims and
1,458 with public claims. Composite unresolved export: 22,886 data rows plus
header. Conflict union: 78. Pull list: 23,769 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 511 organizations, 1,524 affiliations, 3,058
published/qualified/conflict-visible claims and 2,672 public citations.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 413 counts and byte-identical public
tree. SQLite integrity and foreign keys pass. All 90 Python tests pass in 4.291
seconds; existing connection-cleanup ResourceWarnings remain visible. The
generated 200-profile structural audit passes; it is not independent
historical re-review, and the women stratum remains unavailable without
sourced classification.

The exact Pages-configuration build contains 24,459 HTML pages and 24,531
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,587 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,531 artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,087 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. The nine Batch 413 focused
checks pass across desktop, phone and tablet on the final build.

The complete 1,770-case local browser/accessibility matrix passed 1,770/1,770
in 18.8 minutes across desktop, phone and tablet with retries disabled.
Independent GitHub Test run `33941088586` passed in 33 minutes 31 seconds. PR
170 merged source commit `7db51afc990c5b880453f2d3c76fa0ece11ab4d8`
as `b8cc29a74d7930873e884dfe6554ca9da956b7b5`; Pages run `33942667032`
succeeded. Pinned verification against the source commit matched all 67 assets
/ 83,929,419 bytes, seven core routes and all ten direct cohort profiles at
`https://therealjameswilson.github.io/before-oss/`.

Final manifest: 67 assets / 83,929,419 bytes; SHA-256
`cfbfbd3b82c4d46d784dfb6a7d5b4bf86fb8902030d832825ccb944097842232`.
Public tree: 70 files, SHA-256
`76d8bb8434e1826bcb4d1e6fa959316ae3dd3e04180af7bee70575f5220884df`.
Production tree: 24,531 files, SHA-256
`c519cefc808c1ca1419f2238fd5582aacccb01373f0c61ae042331ff8a6b2b56`.
Tree digests use sorted relative paths, NUL separators and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-roy-p-christian-through-peter-a-christoff-pathways_batch-413_2026-09-05.json
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
incomplete, with 20,028 active people still `not_started`. Rotate the previously
exposed credential before authenticated NARA work; public-source research is
not blocked. Unresolved methodological issues remain: automated profile audit
is structural rather than independent historical validation, source-document
identity normalization is provisional, external links are inventoried rather
than exhaustively visited, and most personnel files still require archival
examination.
