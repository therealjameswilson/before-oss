# Batch 411 release verification

2026-09-05 UTC. **Local release candidate; not yet merged or deployed.** This
report covers the ten people on PDF page 80 rows 10-19, Jean Chretien through
Emil E. Christensen, in Boxes 122-123.

## Research

The full page was rendered at 150 dpi and all ten printed rows were visually
matched to the database before research. The reviewed evidence bundle adds
seven citations, one new canonical organization plus one reused organization,
two affiliations, five claims, ten claim-source links, ten person updates and
ten saved research attempts.

Jean Chretien receives a high-confidence identity and a visibly qualified,
medium-confidence military pathway through the French Service de
Renseignement (SR) in Algiers. Arthur L. Funk's chapter in the NARA-published
*The Secrets War* names Colonel Jean Chretien among the French intelligence
officers with whom OSS cooperated. Exact name, colonel rank, the index's
`French` note and direct OSS context align. The chapter documents cooperation,
not an OSS employment transfer, so the profile does not invent a transfer date
or call SR a civilian employer.

John L. Chrislow receives a high-confidence identity as John Laurence Chrislow
and a qualified, medium-confidence U.S. Naval Reserve pathway. NARA expands his
name in its OSS Naval Officers Personnel Cards list. Notre Dame's contemporary
May 1943 *Capstan* volume independently lists John L. Chrislow of Lodi,
Wisconsin, a University of Wisconsin 1941 graduate, in the class commissioned
as USNR ensigns on 27 May 1943. Education is used only for identity and is not
classified as employment. The exact OSS assignment date remains unknown.

An official 1946 Shanghai cable provides a low-confidence exact-name lead for
Anthony M. Chrisler. It lacks a wartime identifier or Box 122 bridge, so the
lead is withheld from public facts and analytics. The other seven people have
no accepted external identity or affiliation claim. All eight unresolved
profiles retain dignified research-status pages and direct researchers to
Boxes 122-123. Unsuccessful searches are not described as evidence that no
prior employer existed.

All seven cited destinations returned HTTP 200 in a normal final availability
check. A secondary magazine lead for John Chrislow returned an access
restriction and was excluded from the evidence bundle; no restriction was
bypassed. The public Army bulk-data route remained unavailable for eligible
checks, and no identifier outcome was inferred. No authenticated NARA Catalog
request or exposed credential was used.

See `research/batch-411-discovery-checkpoint.md` for the search chronology,
adjudication, rejected leads and next archival actions. The structured bundle
retains each person's queries, reviewed-source count, rejection reasons and
bounded outcome.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,892 / 23,940 active people | 16.2573% |
| Verified-employer coverage | 214 / 23,940 active people | 0.8939% |
| Verified-affiliation coverage | 491 / 23,940 active people | 2.0510% |
| Archival disposition assessed | 3,845 / 23,940 active people | 16.0610% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,232 commissioned,
5,621 noncommissioned and 16,087 indeterminate. Identity: 742 confirmed, 576
high confidence, 128 probable, 70 ambiguous, 72 conflicting and 22,352
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 20,048 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 209 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 650 |
| conflicting_sources | 71 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,526 |
| completed | 123 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 921 | 35 |
| high | 1,198 | 275 |
| medium | 851 | 82 |
| low | 73 | 1 |
| conflicting | 83 | 2 |

There are 3,804 citation records, 1,785 legacy document keys that are not
certified unique historical documents, and 1,302 distinct stable URLs.
Inventory: 523 organizations, 1,532 affiliations, 3,126 claims, 7,100
claim-source links and 5,111 attempts/plans. Attempt outcomes: 1,739
`source_reviewed`, 160 `candidate_found`, 619 `candidate_rejected`, 2,006
`no_result` and 587 `planned`. There are 1,512 people with stored claims and
1,453 with public claims. Composite unresolved export: 22,889 data rows plus
header. Conflict union: 76. Pull list: 23,769 data rows plus header; review
queue: 23,940 data rows plus header.

Public projection: 23,940 people, 511 organizations, 1,521 affiliations, 3,050
published/qualified/conflict-visible claims and 2,664 public citations.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full replay from the frozen 522-page PDF and every reviewed
evidence bundle reproduced the exact database and byte-identical public tree.
SQLite integrity and foreign keys pass. All 90 Python tests pass in 4.160
seconds; existing connection-cleanup ResourceWarnings remain visible. The
generated 200-profile structural audit passes; it is not independent
historical re-review, and the women stratum remains unavailable without sourced
classification.

The exact Pages-configuration build contains 24,459 HTML pages and 24,531
artifacts with zero Astro errors, warnings or hints. All internal links resolve;
49,587 external destinations are inventoried, not all visited. Identifier
checks inspect all 24,531 artifacts, 12,926 normalized identifiers, 120
formatted variants and 1,083 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. All twelve Batch 411 focused
checks pass across desktop, phone and tablet on the final build.

The complete 1,755-case local browser/accessibility matrix produced 1,754
passes and one metadata equality failure in 16.0 minutes. During that run, the
reviewed-evidence completion timestamp was corrected and the source data was
regenerated while the already-built test server still held the earlier
timestamp. The sole failure was therefore the tablet analysis assertion
comparing those two generations, not a page, evidence or accessibility defect.
After the final deterministic rebuild, both analysis scenarios passed across
all three viewports, 6/6, and all twelve Batch 411 scenarios passed across the
same viewports, 12/12; the combined final rerun passed 18/18 in 15.7 seconds.

Final manifest: 67 assets / 83,867,088 bytes; SHA-256
`9b151c18c4d3d20c6297fb093147db229ec7dbd95639a74ff09b0ecd4ad97690`.
Public tree: 70 files, SHA-256
`7e86f9c0560cc0cc5ef15d5199a4eb3306390aa377a777c7025b80249dc5591b`.
Production tree: 24,531 files, SHA-256
`68c8369ffdbe44ca178de091a279bdd8717987074a892743eeb09d44e2af6804`.
Tree digests use sorted relative paths, NUL separators and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-jean-chretien-through-emil-e-christensen-pathways_batch-411_2026-09-05.json
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
incomplete, with 20,048 active people still `not_started`. Rotate the previously
exposed credential before authenticated NARA work; public-source research is
not blocked. Unresolved methodological issues remain: automated profile audit
is structural rather than independent historical validation, source-document
identity normalization is provisional, external links are inventoried rather
than exhaustively visited, and most personnel files still require archival
examination.
