# Batch 416 release verification

2026-09-05 UTC. **Released and pinned-live verified.** This
report covers ten people across PDF page 81 rows 14-23, Woon S Chung through
Michael A Ciaccio, spanning Boxes 124-125.

## Research

The complete page was rendered at 150 dpi. Every printed name, middle initial,
number or blank, rank or blank, box and location was visually matched to the
immutable database before research. The reviewed evidence bundle adds six
citations, two organizations, seven affiliations, thirteen claims, thirty
claim-source links, ten person updates and ten saved research attempts.

Archie Chun-Ming has the cohort's strongest documented pathway. A CIA
institutional biography and a *Studies in Intelligence* article identify the
distinctive exact name as a Hawaii-born physician and Army Medical Corps
captain recruited from a reserve unit in Hawaii in spring 1942 for the first
planned field team, later OSS Detachment 101. The unnamed reserve unit is his
explicit immediate pre-OSS/COI military affiliation. His physician occupation
and June 1941 presidency of the Hawaii Chinese Civic Association are stored as
separate earlier affiliations. Neither is presented as employment or as his
last civilian employer because the sources name no clinic, hospital, practice
ownership arrangement or other employer.

Four official Army records support qualified occupation observations. Oral L
Chupp's exact private identifier and name match a 10 March 1942 record for
repairmen and mechanics, not elsewhere classified. Raymond Chynoweth's exact
identifier and name match a 23 April 1942 record for shipping and receiving
clerks. Phillip E Churchill's identifier, surname and middle initial match a
29 October 1942 record under the given-name spelling `Philip` for chauffeurs
and drivers. Edward J Church's identifier selects one 18 April 1941 entry from
five same-name records; its occupation group is general office clerks, but its
grade and branch fields are malformed. That defect is disclosed, and those
fields are not used for classification. All four observations are medium
confidence with uncertain temporal relationships. None names an employer or
establishes the immediately prior affiliation.

Woon S Chung remains an identity-review case. The index prints 1st Lt. and no
identifier; the Army file contains one exact-name private entry dated 9 June
1943. With no matching identifier, hometown, birth datum, unit or promotion
chronology, the Army candidate remains low confidence and unpublished. The
index-derived commissioned-officer classification is preserved, while the
candidate's occupation and enlisted classification are withheld.

Mallory D Church, Rosa M Church, Mary B Chynoweth and Michael A Ciaccio remain
unresolved. A 1990 litigant named Mary B Chynoweth is chronologically
impossible. Modern corporate, property, licensing, family-history and
similarly spelled results were rejected rather than promoted into public
claims.

The public Catalog page for NAID 1263923 supplied the unrestricted
185,043,578-byte Army enlistment ZIP. Its SHA-256 was
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`.
All 9,200,232 fixed-width records were scanned once without an API key. No raw
record, response body, archive or full identifier was retained. Absence from
the merged file is not treated as negative proof. The technical-documentation
and code-list pages needed to interpret the four occupation values were also
visually inspected.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, obituary and institutional searches, and current Library
of Congress discovery checks were completed for every person. All six distinct
citation destinations returned HTTP 200 or HTTP 206 in the final bounded
availability check. No authenticated NARA Catalog request, exposed credential
or access-control bypass was used.

See `research/batch-416-discovery-checkpoint.md` for the search chronology,
bulk-file adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,942 / 23,940 active people | 16.4662% |
| Verified-employer coverage | 214 / 23,940 active people | 0.8939% |
| Verified-affiliation coverage | 493 / 23,940 active people | 2.0593% |
| Archival disposition assessed | 3,895 / 23,940 active people | 16.2698% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,234 commissioned,
5,631 noncommissioned and 16,075 indeterminate. Identity: 743 confirmed, 590
high confidence, 128 probable, 71 ambiguous, 75 conflicting and 22,333
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,998 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 108 |
| needs_temporal_review | 10 |
| verified_employer_found | 209 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 662 |
| conflicting_sources | 74 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,556 |
| completed | 125 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 923 | 35 |
| high | 1,216 | 275 |
| medium | 864 | 82 |
| low | 75 | 1 |
| conflicting | 86 | 2 |

There are 3,831 citation records, 1,791 legacy document keys that are not
certified unique historical documents, and 1,306 distinct stable URLs.
Inventory: 525 organizations, 1,550 affiliations, 3,164 claims, 7,191
claim-source links and 5,161 attempts/plans. Attempt outcomes: 1,757
`source_reviewed`, 162 `candidate_found`, 633 `candidate_rejected`, 2,022
`no_result` and 587 `planned`. There are 1,532 people with stored claims and
1,471 with public claims. Composite unresolved export: 22,875 data rows plus
header. Conflict union: 79. Pull list: 23,769 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 513 organizations, 1,539 affiliations, 3,086
published/qualified/conflict-visible claims and 2,690 public citations.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 416 counts. SQLite integrity and
foreign keys pass. All 90 Python tests pass in 4.176 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,461 HTML pages and 24,533
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,593 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,533 artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,081 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. A separate scan of the tracked
Batch 416 evidence bundle also finds zero private-identifier boundary matches.
The twelve Batch 416 focused checks pass across desktop, phone and tablet on
the final build. The dependency audit reports zero vulnerabilities.

The complete 1,806-case local browser/accessibility matrix passed 1,806/1,806
in 16.3 minutes across desktop, phone and tablet with retries disabled.
Consecutive Pages-configuration builds reproduced byte-identical public and
production trees. Independent GitHub Test `33946810994` passed in 32 minutes
55 seconds; PR 173 merged as
`e31a53147f837f3446fd753f0347414ac48769ff`; Pages `33948257696` succeeded;
and pinned verification of source commit
`f3114cafc2246018d90bbb60724e9edb93b29ad1` matched all 67 assets, seven core
routes and ten direct cohort profiles.

Final manifest: 67 assets / 84,148,970 bytes; SHA-256
`76418ac28f27542ffc7040b961e93cf0e3308d3db2b745049b9e271e383d2a07`.
Public tree: 70 files, SHA-256
`e530cf1325a78d29bdf68020e56989a071b5997c16897b87172d893886f23516`.
Production tree: 24,533 files, SHA-256
`47d4ac9d4f74337217c23457d82c24176b5f2282a3a704ca303da7cdf56ed5a0`.
Tree digests use sorted relative paths, NUL separators and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-one-woon-s-chung-through-michael-a-ciaccio-pathways_batch-416_2026-09-05.json
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
incomplete, with 19,998 active people still `not_started`. Rotate the previously
exposed credential before authenticated NARA work; public-source research is
not blocked. Unresolved methodological issues remain: automated profile audit
is structural rather than independent historical validation, source-document
identity normalization is provisional, external links are inventoried rather
than exhaustively visited, and most personnel files still require archival
examination.
