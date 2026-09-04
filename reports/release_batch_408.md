# Batch 408 local release checkpoint

2026-09-04 UTC. **Reviewed local data; full browser matrix pending.** No Batch
408 deployment is claimed. Batch 407 passed independent GitHub QA with all
1,707 cases, merged through PR 164, deployed through Pages 33907253488 and
passed pinned verification of every asset and all nine cohort profiles. It is
the current live release.

## Research

Ten individual outcomes from page 79 rows 26-35, Durwood W Chiles through
Corning Chisolm. The bundle adds six citations, five affiliations, eleven
claims, twenty-seven claim-source links, ten person updates and ten attempts.
Its one organization record reuses the existing Columbia University key and
does not create a new organization.

Durwood Chiles receives a confirmed identity bridge from a private-identifier
Army match and a contemporary OSS roster; Robert Chin receives a confirmed
bridge from the Army match, matching birth year and scholarly OSS chronology.
Robert's Columbia pathway is student status, strongly date-bounded within 1943,
not employment. Durwood, Walter Chinn, Charles Chiriako and Joseph Chirichillo
receive qualified historical occupation-group observations. William Chilton's
1946 record supplies identity evidence only. Four other people remain
unresolved and archive-routed. No named employer is added.

See `research/batch-408-discovery-checkpoint.md` for source inspection,
rejections, failed-access details and individual next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,862 / 23,940 active people | 16.1320% |
| Verified-employer coverage | 213 / 23,940 active people | 0.8897% |
| Verified-affiliation coverage | 489 / 23,940 active people | 2.0426% |
| Archival disposition assessed | 3,815 / 23,940 active people | 15.9357% |

23,941 stored entities, one superseded; 233 possible duplicate groups. Officer
classification: 2,230 commissioned, 5,619 noncommissioned and 16,091
indeterminate. Identity: 742 confirmed, 571 high confidence, 124 probable, 70
ambiguous, 72 conflicting and 22,361 unresolved.

| Research status | Active people |
|---|---:|
| not_started | 20,078 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 208 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 649 |
| conflicting_sources | 71 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,500 |
| completed | 121 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 921 | 35 |
| high | 1,190 | 273 |
| medium | 842 | 82 |
| low | 72 | 1 |
| conflicting | 83 | 2 |

3,783 citations; 1,772 legacy document keys, not certified unique historical
documents; 1,293 distinct stable URLs. Inventory: 521 organizations, 1,526
affiliations, 3,108 claims, 7,064 claim-source links and 5,081 attempts/plans.
Attempt outcomes include 1,709 source_reviewed, 160 candidate_found, 619
candidate_rejected, 2,006 no_result and 587 planned. Composite unresolved
export: 22,893 data rows plus header. Conflict union: 76. Pull list: 23,770 data
rows plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 509 organizations, 1,515 affiliations, 3,033
published/qualified/conflict-visible claims and 2,647 public citations.

## QA and resume

Evidence validation and repeated import pass idempotently. SQLite integrity
and foreign keys pass. All 90 Python tests pass in 4.147 seconds. The generated
200-profile structural audit passes; it is not independent historical re-review
and the women stratum remains unavailable without sourced classification.

The production build contains 24,457 HTML pages with zero Astro errors,
warnings or hints; its first reported elapsed time was 16m 58s after a long
machine pause. Repeated public export and production build are byte-identical.
All internal links resolve; 49,578 external destinations are inventoried, not
all visited. Privacy checks inspect all 24,529 artifacts, 12,926 normalized
identifiers, 120 formatted variants and 1,082 substring coincidences with zero
unexpected boundary matches or aggregate exceptions. All twelve final focused
browser checks pass across desktop, phone and tablet in 12.3 seconds. The first
focused authoring run had three identical assertion failures because the test
used a non-existent display-field name; the assertion was corrected to the
actual canonical-organization field. Data and application behavior did not
change to make it pass.

Final manifest: 67 assets / 83,715,111 bytes; SHA-256
`59017dd704f8e0c3212709b175025a55917a9226aa4a84d223c7ce7b86c79400`.
Public tree: 70 files, SHA-256
`077389097e4f97f26c19fee3d369b3a4c8fc7c8a32f9d99222f5dee3b4f8c5c1`.
Production tree: 24,529 files, SHA-256
`5137fa23d0686d5a6972729a91775f5226797f3f46a311389951ccd483478370`.
Tree digests use sorted relative paths, NUL separators and binary file hashes.
The complete 1,719-case local matrix, independent GitHub QA, Pages deployment
and pinned live verification remain required. No release is claimed.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-seventy-nine-chiles-through-chisolm-pathways_batch-408_2026-09-04.json
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
incomplete. Rotate the previously exposed credential before authenticated NARA
work; public-source research is not blocked. Legacy methodological issues remain
the same as Batch 407 and are not hidden by the new coverage totals.
