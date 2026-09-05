# Batch 417 release verification

2026-09-05 UTC. **Local release candidate; not yet merged or deployed.** This
report covers ten people on PDF page 81 rows 24-33, George Ciampa through
Charles Ciccone, all in Box 125.

## Research

The complete page was rendered at 150 dpi. Every printed name, middle initial,
blank rank, number or blank, box and location was visually matched to the
immutable database before research. The reviewed evidence bundle adds eight
citations, six affiliations, seventeen claims, forty-five claim-source links,
ten person updates and ten saved research attempts.

Eight supplied private identifiers produced exact-name, exact-identifier
matches in NARA's unrestricted Army merged file. Six support qualified
occupation observations: Cafiero Cicala, accountants and auditors; Anthony L
Cicatelli, furnacemen, smelters and pourers; Peter J Cicchini, chauffeurs and
drivers; Salvatore Cicciari, fabrication of textile products not elsewhere
classified; Angelo R Ciccolella, semiprofessional occupations not elsewhere
classified; and Charles Ciccone, metal filers, grinders, buffers and polishers.
Each observation retains its dated Army-entry context and medium confidence.
None names an employer, proves actual work dates or establishes that the work
immediately preceded OSS service.

George Ciampa's exact identifier match carries occupation value 999, which the
inspected NARA code pages do not define. It is deliberately left uninterpreted.
The well-documented veteran George W Ciampa has a different middle initial,
identifier and 1943 entry chronology and was rejected as a namesake. Guy A
Ciaraldi's exact match is dated 1 July 1946, after NARA's documented 20
September 1945 termination of OSS. It supports identity and enlisted Army
status only; occupation value 177 is also left uninterpreted. Guy is routed to
critical temporal review.

A reputable obituary identifies the distinctive Clement Cianfichi as an Army
OSS veteran who served in Europe as a demolition specialist. That supports a
high-confidence identity and enlisted status, not a pre-service employer. Its
post-1959 master-carpenter chronology is not projected backward. A 1952
federal court decision documents Sergeant Arthur Ciarmicoli with the U.S. Army
Chrysler Mission in northern Italy in October 1944. It likewise supports
identity and status only.

A National Park Service history names an OSS Tacoma Mission Sergeant Charles
Ciccone, but supplies no identifier, middle name, hometown or personnel-file
bridge. That candidate remains low confidence and private. A 1941 Rochester
directory employer lead for Angelo Ciccolella lacks the indexed middle initial
and identifier and conflicts with the Army file's New Jersey residence; it was
rejected. No candidate employer is promoted into the public data.

The public Catalog page for NAID 1263923 supplied the unrestricted
185,043,578-byte Army enlistment ZIP. Its SHA-256 was
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`.
All 9,200,232 fixed-width records were scanned once without an API key. No raw
record, response body, archive or full private identifier was retained.
Absence from the merged file is not treated as negative proof. The technical
documentation and code-list pages needed to interpret the six published
occupation values were also visually inspected.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, obituary and institutional searches, and Library of
Congress discovery checks were completed for every person. Six of eight
distinct citation destinations returned HTTP 200 or 206 in the bounded
automated check. The Legacy obituary and Justia court-decision pages were
readable in the browser but rejected the generic automated request with HTTP
403; external link availability is therefore not fully automated. No
authenticated NARA Catalog request, exposed credential or access-control
bypass was used.

See `research/batch-417-discovery-checkpoint.md` for the search chronology,
bulk-file adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,952 / 23,940 active people | 16.5079% |
| Verified-employer coverage | 214 / 23,940 active people | 0.8939% |
| Verified-affiliation coverage | 493 / 23,940 active people | 2.0593% |
| Archival disposition assessed | 3,905 / 23,940 active people | 16.3116% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,234 commissioned,
5,641 noncommissioned and 16,065 indeterminate. Identity: 743 confirmed, 600
high confidence, 128 probable, 71 ambiguous, 75 conflicting and 22,323
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,988 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 108 |
| needs_temporal_review | 11 |
| verified_employer_found | 209 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 668 |
| conflicting_sources | 74 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,559 |
| completed | 125 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 923 | 35 |
| high | 1,226 | 275 |
| medium | 870 | 82 |
| low | 76 | 1 |
| conflicting | 86 | 2 |

There are 3,839 citation records, 1,794 legacy document keys that are not
certified unique historical documents, and 1,308 distinct stable URLs.
Inventory: 525 organizations, 1,556 affiliations, 3,181 claims, 7,236
claim-source links and 5,171 attempts/plans. Attempt outcomes: 1,766
`source_reviewed`, 163 `candidate_found`, 633 `candidate_rejected`, 2,022
`no_result` and 587 `planned`. There are 1,542 people with stored claims and
1,481 with public claims. Composite unresolved export: 22,869 data rows plus
header. Conflict union: 79. Pull list: 23,769 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 513 organizations, 1,545 affiliations, 3,102
published/qualified/conflict-visible claims and 2,697 public citations.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 417 counts. SQLite integrity and
foreign keys pass. All 90 Python tests pass in 4.324 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,461 HTML pages and 24,533
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,595 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,533 artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,083 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. A separate scan of the tracked
Batch 417 evidence bundle also finds zero private-identifier boundary matches.
The fifteen Batch 417 focused checks pass across desktop, phone and tablet on
the final build. The dependency audit reports zero vulnerabilities.

The complete 1,821-case local browser/accessibility matrix passed 1,821/1,821
in 15.0 minutes across desktop, phone and tablet with retries disabled.
Consecutive Pages-configuration builds reproduced byte-identical public and
production trees. Independent GitHub QA, merge, Pages deployment and pinned
live verification remain subsequent release gates.

Final manifest: 67 assets / 84,251,572 bytes; SHA-256
`b9bda45c293b345f6878eb3b3fc5d4ff5c6c64aec085ad77caaef26533ade734`.
Public tree: 70 files, SHA-256
`818fc52a3a681de5480d721abadc9e02180c37a3a0e9213d2966b82b9ab017de`.
Production tree: 24,533 files, SHA-256
`2cf44a7da3157e06b58bc7aa36d7f811e13d40136e4af647cee1ecf3bd6050ae`.
Tree digests use sorted relative paths, NUL separators and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-one-george-ciampa-through-charles-ciccone-pathways_batch-417_2026-09-05.json
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
incomplete, with 19,988 active people still `not_started`. Rotate the previously
exposed credential before authenticated NARA work; public-source research is
not blocked. Unresolved methodological issues remain: automated profile audit
is structural rather than independent historical validation, source-document
identity normalization is provisional, external links are inventoried rather
than exhaustively visited, and most personnel files still require archival
examination.
