# Batch 426 release verification

2026-09-05 UTC. **Released.** This report covers ten source
records on PDF page 83 rows 22-31, Kathleen M Clarke through Frederick Claudy,
spanning Boxes 125, 127 and 128 at locations 230/86/28/06 and 230/86/28/07.

## Research

Page 83 was rendered at 150 dpi. Every printed name, initial, rank or blank,
private identifier or blank, box and location in the cohort was visually
matched to the immutable database before research. The reviewed evidence
bundle adds five citations, two affiliations, seven claims, eighteen
claim-source links, ten person updates and ten saved research attempts. It
adds no organization or named employer.

Exact private-identifier and name matches support confirmed identities for
Norman F Clarke and William W Clarke. Norman's official Army record reports
entry on 3 June 1942 as a Private and carries Enlisted Reserve Corps occupation
value 017. The rendered official code page defines that value as Engineers,
electrical. William's official record reports entry on 29 June 1944 as a
Private and standard-card occupation value 992, Students. Both are qualified,
medium-confidence observations with uncertain pre-OSS timing. Norman's category
does not name an employer; William's student status is not employment and does
not name a school.

Paul W Clarke retains enlisted naval classification from the index's printed
`S 2/c` grade. The sole exact-name Army row has an incompatible identifier and
is rejected. Marianne Clarke, Harold W Classen, Henri L Claudel and Frederick
Claudy retain unmerged or archival identity leads and remain ambiguous.
Kathleen M Clarke, Mildred A Clarke and Ruby M Clarke remain unresolved. A CIA
Reading Room search discovery names a Marianne Clarke as a 1944 OSS Special
Funds secretary, but the direct document redirected during review and neither
that lead nor a Nebraska teaching namesake can be linked to Box 127. The CIA
lead remains low-confidence and withheld. No employer, immediate predecessor
affiliation or last civilian employer was established for any person in the
cohort.

Exact-name OSS and CIA searches, meaningful variants, employment and
occupation searches, institutional, obituary, newspaper or archival searches,
the current Library of Congress API and the complete unrestricted
9,200,232-row Army merged-file comparison when applicable were recorded for
every person. The four archival and index citation destinations returned HTTP
200. The CIA discovery-only URL redirected to the Reading Room home page and
is not treated as inspected evidence. No access control was bypassed and no
authenticated NARA Catalog request was used.

See `research/batch-426-discovery-checkpoint.md` for the search chronology,
candidate adjudication, rejected leads and next archival actions. Research
completion here means a saved, reviewable outcome, not that a prior employer
has been disproved. All ten records remain on the archival pull list.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 4,040 / 23,940 active people | 16.8755% |
| Verified-employer coverage | 215 / 23,940 active people | 0.8981% |
| Verified-affiliation coverage | 495 / 23,940 active people | 2.0677% |
| Archival disposition assessed | 3,995 / 23,940 active people | 16.6876% |

There are 23,941 stored entities and one superseded entity; 233 possible
duplicate groups remain visible. Officer classification: 2,235 commissioned,
5,662 noncommissioned and 16,043 indeterminate. Identity: 761 confirmed, 609
high confidence, 128 probable, 96 ambiguous, 79 conflicting and 22,267
unresolved.

| Research status | Active people |
|---|---:|
| not_started | 19,900 |
| in_progress | 44 |
| candidate_found | 7 |
| needs_identity_review | 134 |
| needs_temporal_review | 13 |
| verified_employer_found | 210 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 689 |
| conflicting_sources | 78 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,588 |
| completed | 126 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 941 | 35 |
| high | 1,241 | 276 |
| medium | 894 | 82 |
| low | 86 | 1 |
| conflicting | 90 | 2 |

There are 3,898 citation records, 1,814 legacy document keys that are not
certified unique historical documents, and 1,326 distinct stable URLs.
Inventory: 528 organizations, 1,586 affiliations, 3,252 claims, 7,428
claim-source links and 5,261 attempts/plans. Attempt outcomes: 1,793
`source_reviewed`, 195 `candidate_found`, 641 `candidate_rejected`, 2,045
`no_result` and 587 `planned`. There are 1,583 people with stored claims and
1,512 with public or conflict-visible claims. Composite unresolved export:
22,846 data rows plus header. Conflict union: 83. Pull list: 23,768 data rows
plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 516 organizations, 1,575 affiliations, 3,163
published, qualified or conflict-visible claims, 2,747 public citations and 26
profile shards.

## Local QA and resume

The evidence validates against the Pydantic schema and repeated import is
idempotent. A full 17 minute 53 second replay from the frozen 522-page PDF and
every reviewed evidence bundle reproduced the exact Batch 426 counts. SQLite
integrity and foreign keys pass. All 90 Python tests pass in 4.313 seconds;
existing connection-cleanup ResourceWarnings remain visible. The generated
200-profile structural audit passes; it is not independent historical
re-review, and the women stratum remains unavailable without sourced
classification.

The exact Pages-configuration build contains 24,464 HTML pages and 24,536
artifacts with zero Astro errors, warnings or hints. All internal links
resolve; 49,608 external destinations are inventoried, not all visited.
Identifier checks inspect all 24,536 artifacts, 12,926 normalized identifiers,
120 formatted variants and 1,081 substring coincidences with zero unexpected
boundary, aggregate or manifest-size matches. The tracked evidence bundle has
zero full private-identifier leaks. Fifteen focused Batch 426 checks pass
across desktop, phone and tablet in 14.9 seconds. The dependency audit reports
zero vulnerabilities.

The complete 2,001-case local browser/accessibility matrix produced 1,992
passes and nine browser-resource timeouts in 1.7 hours with retries disabled.
Seven legacy scenarios, the Sources audit on phone and one Batch 426 scenario
on tablet timed out; no evidence assertion failed. In the first exact rerun,
the eight non-Sources scenarios passed across all layouts, 24/24, while the
Sources audit passed on desktop and tablet but again timed out on phone. Trace
inspection found a fully loaded page with no network or console errors: axe
stalled while returning every passing and inapplicable node from the 2,747-
entry citation list. The accessibility test now requests only violations while
retaining the same WCAG tags and serious/critical assertion. The full 27-check
accessibility route set and all fifteen Batch 426 checks subsequently passed
across desktop, phone and tablet, 42/42 in 90 seconds. Consecutive production
builds are byte-identical. A clean independent GitHub Test, merge, Pages
deployment and pinned live verification completed successfully. Independent
Test run `34003906550` passed against exact source commit
`3bc9934a56269d3e42abe91ef66d1f70b489dc00` in 41 minutes 46 seconds. Pull
request 183 merged at 2026-09-06 02:41:10 UTC as merge commit
`8258962ba55aed8d5400f0f02945abcf4031142a`. Pages run `34007115591` passed
(build 1 minute 16 seconds; deploy 16 seconds). Pinned live verification
recovered 67 manifest assets totaling 84,773,353 bytes, matched manifest
SHA-256 `7858022f2c5a9d255272c7cd502a9d9d77d6da81cd6fd2fca3794e3d677d68a4`,
confirmed exact source commit `3bc9934a56269d3e42abe91ef66d1f70b489dc00`, and passed seven core routes plus
all ten direct cohort profiles at
`https://therealjameswilson.github.io/before-oss/`.
The supplementary merge-triggered Test `34007115532` passed against merge
commit `8258962ba55aed8d5400f0f02945abcf4031142a` in 42 minutes 39 seconds.

Current manifest: 67 assets / 84,773,353 bytes; SHA-256
`7858022f2c5a9d255272c7cd502a9d9d77d6da81cd6fd2fca3794e3d677d68a4`.
Public tree: 70 files, SHA-256
`fbdeeada54447ad00b2476f914072cd95268f008aaac8d5f113af818b037b96a`.
Consecutive Pages-configuration production trees: 24,536 files, SHA-256
`ec8d738a46b0c59254109c57c45a7c76ef2db7845bb462015e53a96806066273`.
Tree digests use sorted relative paths, NUL separators and binary file hashes.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-eighty-three-kathleen-clarke-through-frederick-claudy-pathways_batch-426_2026-09-05.json
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
incomplete, with 19,900 active people still `not_started`. Rotate the
previously exposed credential before authenticated NARA work; public-source
research is not blocked. Unresolved methodological issues remain: automated
profile audit is structural rather than independent historical validation,
source-document identity normalization is provisional, external links are
inventoried rather than exhaustively visited, and most personnel files still
require archival examination.
