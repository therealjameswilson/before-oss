# Batch 409 release verification

2026-09-04 UTC. **Released and pinned-live verified.** Batch 409 passed
independent GitHub Test `33925229525` with all 1,731 cases passing in 23.2
minutes, merged through PR 166 as
`e29e79e6aa23e11f686935015acd9a82dfa1e56a`, and deployed through Pages
`33927323898`. Pinned verification against source commit
`082e63594a087c7d84ecd1310f303043dae4edf1` matched all 67 assets /
83,758,733 bytes, seven core routes and all ten direct cohort profiles. The
verified public URL is <https://therealjameswilson.github.io/before-oss/>.

## Research

Ten individual outcomes from page 79 rows 36-45, Herbert G. Chissell through
DeForest D. Choha. The bundle adds seven citations, one organization, two
affiliations, six claims, thirteen claim-source links, ten person updates and
ten attempts.

Martin B. Chittick receives a high-confidence identity and a high-confidence,
documented-prewar **professional affiliation** with The Pure Oil Co. from the
official ASTM publisher record for his 1940 paper. It is not labeled employment,
immediate pre-OSS affiliation, or last civilian employer. A 1943 Official
Register entry places the colonel in the Chemical Warfare Service Technical
Division but does not establish the transition into OSS.

DeForest D. Choha receives a high-confidence exact private-identifier Army
bridge and a qualified aircraft-mechanics occupation-group observation dated
1944-02-08. It is not a named employer or an asserted immediate OSS pathway.
Ernest L. Chmieleski and Joseph F. Chochola receive probable identity evidence
from a contextual OSS Yugoslavia roster; no pre-OSS affiliation is inferred.
The other six identities remain unresolved and archive-routed after the saved
staged research protocol. No verified employer is added.

See `research/batch-409-discovery-checkpoint.md` for the discovery record,
adjudication summary, source limits, rejections and next actions.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,872 / 23,940 active people | 16.1738% |
| Verified-employer coverage | 213 / 23,940 active people | 0.8897% |
| Verified-affiliation coverage | 490 / 23,940 active people | 2.0468% |
| Archival disposition assessed | 3,825 / 23,940 active people | 15.9774% |

23,941 stored entities, one superseded; 233 possible duplicate groups. Officer
classification: 2,230 commissioned, 5,620 noncommissioned and 16,090
indeterminate. Identity: 742 confirmed, 573 high confidence, 126 probable, 70
ambiguous, 72 conflicting and 22,357 unresolved.

| Research status | Active people |
|---|---:|
| not_started | 20,068 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 208 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 650 |
| conflicting_sources | 71 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,509 |
| completed | 121 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 921 | 35 |
| high | 1,193 | 273 |
| medium | 845 | 82 |
| low | 72 | 1 |
| conflicting | 83 | 2 |

3,790 citations; 1,775 legacy document keys, not certified unique historical
documents; 1,295 distinct stable URLs. Inventory: 522 organizations, 1,528
affiliations, 3,114 claims, 7,077 claim-source links and 5,091 attempts/plans.
Attempt outcomes include 1,719 source_reviewed, 160 candidate_found, 619
candidate_rejected, 2,006 no_result and 587 planned. Composite unresolved
export: 22,892 data rows plus header. Conflict union: 76. Pull list: 23,770 data
rows plus header; review queue: 23,940 data rows plus header.

Public projection: 23,940 people, 510 organizations, 1,517 affiliations, 3,039
published/qualified/conflict-visible claims and 2,654 public citations.

## Local QA and resume

Evidence validation and repeated import pass idempotently. SQLite integrity
and foreign keys pass. All 90 Python tests pass in 4.186 seconds; existing
connection-cleanup ResourceWarnings remain visible. The generated 200-profile
structural audit passes; it is not independent historical re-review and the
women stratum remains unavailable without sourced classification.

The production build contains 24,458 HTML pages and 24,530 total artifacts with
zero Astro errors, warnings or hints. Repeated public export and production
build are byte-identical. All internal links resolve; 49,581 external
destinations are inventoried, not all visited. Privacy checks inspect all
24,530 artifacts, 12,926 normalized identifiers, 120 formatted variants and
1,080 substring coincidences with zero unexpected boundary matches or aggregate
exceptions. All twelve Batch 409 focused checks pass across desktop, phone and
tablet in 13.5 seconds. The first focused run used a stale built tree and one
incorrect test-only serial mask; after rebuilding and correcting the assertion
to the actual masked display, no evidence or site behavior changed.

Final manifest: 67 assets / 83,758,733 bytes; SHA-256
`7439600b57d4bdc5a6c74536edfa35f681ca6c62c09d2b1306dcca2f73a0c22a`.
Public tree: 70 files, SHA-256
`e9c15a0ea042b3beb82386085074aef7b1c851ad5cb3d4e16bf4b671f8715ea5`.
Production tree: 24,530 files, SHA-256
`04e8fec4ec3f742304dafbf80ae3789ec8606b5022d625a4f4df94b90974737f`.
Tree digests use sorted relative paths, NUL separators and binary file hashes.

The complete 1,731-case local matrix finished with 1,728 passes and three
browser-session timeouts in 45.5 minutes, with retries disabled. The three
unchanged affected scenarios then passed across all three viewports; the
grep-selected rerun covered nine cases and all passed in 16.7 seconds. Failure
artifacts from the first run were preserved outside the generated results
folder. This is not represented as a clean first-run local pass. Independent
GitHub Test `33925229525` then passed all 1,731 cases in 23.2 minutes. PR 166,
Pages and pinned production verification succeeded as recorded at the top of
this report. The redundant postmerge Test `33927323926` subsequently passed on
the merged commit. It is additional confirmation, not a substitute for the
completed independent premerge result.

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-seventy-nine-chissell-through-choha-pathways_batch-409_2026-09-04.json
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
work; public-source research is not blocked. Unresolved methodological issues
are unchanged from Batch 408: automated profile audit is structural rather than
independent historical validation, source-identity normalization remains
provisional, external links are inventoried rather than exhaustively visited,
and most personnel files still require archival examination.
