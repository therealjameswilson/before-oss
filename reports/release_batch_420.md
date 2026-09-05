# Batch 420 release verification

2026-09-05 UTC. **Local release candidate; not yet merged or deployed.** This
report covers ten people on PDF page 82 rows 8-17, Richard R Clair through
Alvin Clark, in Boxes 125 and 126.

## Research

Page 82 was rendered at 150 dpi. Every printed name, initial, rank, number or
blank, box and location in the cohort was visually matched to the immutable
database before research. The reviewed evidence bundle adds ten citations,
four affiliations, nine claims, twenty-five claim-source links, ten person
updates and ten saved research attempts. It does not add an organization or a
named employer.

Exact private-identifier matches in the official Army merged file establish
Eugene H Clapp, Aldo Clara, Alfred C Clark and Alvin Clark as the indexed
people. Their Army-entry occupation categories are published as qualified,
medium-confidence observations with uncertain timing: accountants and
auditors; cement and concrete finishers; actors and actresses; and waiters and
waitresses except private family. These classifications do not identify an
employer and are not promoted to immediate pre-OSS affiliations or last
civilian employers.

The Army name field for Eugene ends with the unexplained text `SND`. It is
preserved in the evidence note and is not expanded or used to alter his
indexed name. Alvin's matched Army row says `ALVIN C CLARK`; that is recorded
as a documented variant while the printed index name remains Alvin Clark.
The Army-entry grade `PVT` and the index grade `T-5` remain separate source
facts rather than being silently reconciled.

James W Clance is a documented conflict, not a merged military biography. An
official Florida National Guard roster places a Corporal James W Clance in
Battery D at Daytona Beach, and official Army histories describe a rare-name
James W Clance as a wartime paratrooper and 82nd Airborne veteran. The exact-
name Army row, however, carries a different identifier from the OSS index.
The conflict is public, excluded from default analytics and routed to critical
archival review; no candidate assignment or occupation is transferred to the
indexed person.

Sixteen exact-name Army candidates exist for Albert L Clark, but the index
does not supply enough corroboration to select one. They remain separate and
the profile is marked ambiguous. A same-name Richard R Clair Army candidate
entered service on 31 January 1946, after OSS ended, and lacks an indexed
identifier or other bridge. A distinctive Frederick Gardner Clapp petroleum-
geologist candidate appears in authoritative institutional sources, but no
OSS linkage or second identifier supports assigning that biography to the
index row. Both candidates remain private leads. Beulah O Clapp and Cloyd
Clare remain unresolved after the completed protocol.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional, obituary, newspaper or archival searches,
and the complete unrestricted Army merged-file comparison when applicable
were recorded for every person. Nine of ten distinct citation destinations
returned HTTP 200 in the bounded automated check. The official Army history
PDF timed out in that check but was readable and reviewed in the browser. No
access control was bypassed and no authenticated NARA Catalog request was
used.

See `research/batch-420-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,982 / 23,940 active people | 16.6332% |
| Verified-employer coverage | 215 / 23,940 active people | 0.8981% |
| Verified-affiliation coverage | 495 / 23,940 active people | 2.0677% |
| Archival disposition assessed | 3,935 / 23,940 active people | 16.4369% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,235 commissioned,
5,652 noncommissioned and 16,053 indeterminate. Identity: 750 confirmed, 607
high confidence, 128 probable, 73 ambiguous, 77 conflicting and 22,305
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,958 |
| in_progress | 46 |
| candidate_found | 5 |
| needs_identity_review | 111 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 677 |
| conflicting_sources | 76 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,567 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 930 | 35 |
| high | 1,239 | 276 |
| medium | 882 | 82 |
| low | 80 | 1 |
| conflicting | 88 | 2 |

There are 3,870 citation records, 1,810 legacy document keys that are not
certified unique historical documents, and 1,323 distinct stable URLs.
Inventory: 528 organizations, 1,574 affiliations, 3,219 claims, 7,337
claim-source links and 5,201 attempts/plans. Attempt outcomes: 1,780
`source_reviewed`, 170 `candidate_found`, 635 `candidate_rejected`, 2,029
`no_result` and 587 `planned`. There are 1,562 people with stored claims and
1,497 with public claims. Composite unresolved export: 22,858 data rows plus
header. Conflict union: 81. Pull list: 23,768 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 516 organizations, 1,563 affiliations, 3,136
published, qualified or conflict-visible claims, 2,723 public citations and 26
profile shards.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact Batch 420 counts. SQLite integrity and
foreign keys pass. All 90 Python tests pass in 4.219 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review, and the
women stratum remains unavailable without sourced classification.

The exact Pages-configuration build contains 24,464 HTML pages and 24,536
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,608 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,536 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,081 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. The tracked evidence bundle has
zero full private-identifier leaks. Twenty-four final Batch 420 focused checks
pass across desktop, phone and tablet in 15.3 seconds. The first authoring run
had twelve assertion failures caused by test-string and absent-section
assumptions; only the assertions were corrected, without changing evidence or
site behavior. The dependency audit reports zero vulnerabilities.

The complete 1,890-case local browser/accessibility matrix passed 1,890/1,890
in 15.7 minutes across desktop, phone and tablet with retries disabled.
Consecutive Pages-configuration builds reproduced byte-identical public and
production trees. Independent GitHub QA, merge, Pages deployment and pinned
live verification remain subsequent release gates.

Final manifest: 67 assets / 84,543,559 bytes; SHA-256
`14720a5fe3d997c9754895d4bed24b8b095a9eef908b114ef166af4ed28fe381`.
Public tree: 70 files, SHA-256
`e542b471c8ee8de08c3bc71eb8030e3fed5ff3f846871fe1321592d06b2575b9`.
Production tree: 24,536 files, SHA-256
`5b366638cb8bfc9c5a72f823d82bfd5f5b83b828ed208deb76a80d1667adcaca`.
Tree digests use sorted file order and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-two-richard-clair-through-alvin-clark-pathways_batch-420_2026-09-05.json
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
incomplete, with 19,958 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
