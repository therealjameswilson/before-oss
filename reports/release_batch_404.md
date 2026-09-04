# Batch 404 release verification

2026-09-04 UTC. **Reviewed local dataset; complete local matrix passed.**
Batch 404 PR 161 targets main and is awaiting independent GitHub Test
`33861391925`. Batch 403 PR 160 has merged after successful Test `33859076065`;
its Pages `33862231457` succeeded. Pinned live verification passed all 67
assets, seven core routes and ten new profiles. Batch 403 remains the public
release until Batch 404's independent workflow and publication succeed.

## Research added

Ten individual dispositions for PDF page 78 rows 32–41, Saraadi Cheo-Sakul
through Irma M Cherry. Eleven citation records, three affiliations, eleven
claims, twenty-nine claim-source links and ten durable research attempts.
Six exact-name/private-identifier Army matches support high-confidence
identity. Three medium-confidence occupation observations name no employer.
Two low-confidence identity candidates are retained only for review. No
organization, immediate affiliation or last civilian employer is invented.

| Person | Outcome |
|---|---|
| Saraadi Cheo-Sakul | Ambiguous: Savasdi/Sawat candidate remains unlinked; Cornell student lead is not employer evidence |
| Lefty J Cheramie | 1942-11-18 Army observation: Occupations in production of petroleum; postwar boat-company lead excluded |
| Leo E Chergoski | High Army identity only; 999 uninterpreted; secondary discharge-index dates require reconciliation |
| Alfred Cherman | 1943-02-24: Linemen and servicemen, telegraph, telephone, and power; no utility inferred |
| George Chernek | 1942-06-01: Upholsterers; no employer or self-employment inferred; obituary index remains unlinked |
| Irving Cherner | High Army identity only; 992 uninterpreted; guestbook business not an employer |
| Robert H Cherney | Unresolved: inaccessible alumni/fraternity candidates not assigned |
| Peter Cherowitz | High Army identity only; 999 uninterpreted |
| Cecilia Cherry | Unresolved; source spelling retained, unrelated OCR excluded |
| Irma M Cherry | Unresolved; no common-name biography assigned |

One complete transient scan of 9,200,232 official Army bulk records, seven
eligible private identifiers, six exact matches. No raw records, full service
numbers or authenticated API payloads retained. Complete PDF page 78 and the
relevant technical/code-list images were inspected. Each row retains its
blank rank: earlier private grades and later discharge ranks do not determine
OSS commissioned classification. The three dated occupation observations have
null employment start/end and work location; all retain uncertain OSS timing.

Underlying personnel files are not reviewed. All ten have specific high-priority
Box 120/121 follow-ups. Cornell student status is not silently promoted from a
different spelling; no clipped military unit is expanded. The seven nonoccupation
outcomes use requires_archival_review, not an exhaustive no-result status.
Item-level sources, failed opens and candidate exclusions are recorded in the
bundle and discovery checkpoint. No access control was bypassed or outreach sent.

## Website correction

New tests exposed that “Lefty Cheramie” failed to find indexed “Lefty J Cheramie”.
Search now accepts complete query tokens within a single documented name,
including omitted initials and surname-first order. Exact full-name matches
still rank first. Tokens cannot be mixed across aliases or reused to match
duplicated query words. This changes discovery behavior, not names or identities.
The source-type checker excludes generated Playwright report/trace artifacts;
application code and tests remain checked. Dependencies/lockfile unchanged.

## Exact local counts

| Measure | Numerator / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,823 / 23,940 active people | 15.9691% |
| Verified-employer coverage | 212 / 23,940 active people | 0.8855% |
| Verified-affiliation coverage | 486 / 23,940 active people | 2.0301% |
| Archival disposition assessed | 3,776 / 23,940 active people | 15.7728% |

23,941 stored entities, one superseded; 233 possible duplicate groups.
Commissioned classification: 2,229 yes, 5,617 no, 16,094 unknown. Identity:
739 confirmed, 558 high confidence, 123 probable, 66 ambiguous, 70 conflicting,
22,384 unresolved. Archival assessment is not physical-file review: six legacy
file-reviewed flags do not certify that this session reviewed any physical file.

| Active research status | People |
|---|---:|
| not_started | 20,117 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 208 |
| documented_prewar_employer_found | 68 |
| occupation_only_found | 636 |
| conflicting_sources | 69 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,478 |
| completed | 120 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 917 | 35 |
| high | 1,174 | 272 |
| medium | 831 | 83 |
| low | 62 | 0 |
| conflicting | 81 | 2 |
| unresolved | 0 | 0 |

3,742 citation records, 1,748 legacy document keys, 1,272 distinct source URLs.
These keys are not certified unique historical documents. Research inventory:
518 organizations, 1,510 affiliations, 3,065 claims, 6,946 links, 5,041 attempts
or plans (1,669 source_reviewed, 160 candidate_found, 619 candidate_rejected,
2,006 no_result, 587 planned). People with a stored claim: 1,477; with a public
claim: 1,426. Broad conflict union: 74. Composite unresolved export: 22,908.
Pull list: 23,770 source rows.

Public projection: 23,940 people, 506 organizations, 1,499 affiliations, 3,000
claims, 2,617 citations and 26 profile shards. The three new occupation findings
are excluded from default verified-employer/affiliation analytics.

## Checks

- Strict evidence schema, repeat import, SQLite integrity and foreign keys pass.
- 90 Python tests pass in 4.077 seconds. Four existing SQLite connection-cleanup
  ResourceWarnings remain visible, not suppressed or represented as failures.
- 200-profile deterministic structural/stratified audit passes; this does not
  replace independent historical re-review. The women stratum still requires
  sourced classification, not gender inferred from names.
- Initial focused browser run: nine passed, three failed on omitted-middle-initial
  search. Repaired run: **15/15 pass in 10.1 seconds** across three viewports,
  including new exact-first, surname-first and alias-isolation regressions.
- Production builds 24,454 HTML pages. The first rebuild following failed tests
  scanned generated trace scripts and reported 193 hints, zero errors/warnings;
  generated-artifact exclusion fixes that source-check scope, without silencing
  application diagnostics. Final repeated build reports zero errors, warnings
  or hints across 28 source files; 24,454 pages built in 9.66 seconds.
- Initial identifier audit: 12,926 normalized numbers, 120 formatted variants,
  24,526 artifacts, 1,079 classified substring coincidences, zero unexpected
  boundary matches. No full service numbers in public fields.
- All internal links resolve; 49,564 external URLs inventoried, not all visited.
- Full profile-shard comparison against Batch 403 changes exactly the ten
  intended people, no unrelated profile or source-row change.
- Public manifest: 67 assets, 83,435,423 bytes, SHA-256
  `2d06a2a1e4329f908a46511769f475a3fa81a904b6ff7b80652c48a47852dc3c`.
  Public tree: 70 files, digest
  `6650094f84db0531c6fe1fe8b74ac6fe8bb571e62ee198675fd42dc1bedb1dff`.
  Consecutive exports/builds match exactly. Production tree: 24,526 files,
  digest `00c783c377f978ef8dd1e2b342d4931454f54c8368c060b12f351292322024e7`.
  Digests hash sorted relative paths, NUL separators and binary file SHA-256s.
- Lefty's local profile was visually inspected; readable layout and complete
  accessible text retain the occupation/date caveat, masked serial, separate
  employer question and item-level citations with explicit context-only support.

The complete **1,668-test local browser/accessibility matrix passed in 19.1
minutes**, exit zero. All three viewports passed, without retries or changed
data/build inputs during the run. No Batch 404 deployment claimed yet.

## Resume and remaining work

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-seventy-eight-cheo-sakul-through-cherry-pathways_batch-404_2026-09-04.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npm run test:e2e
npm run check:links
```

Full replay: `bash scripts/rebuild-all.sh`. Next cohort starts PDF page 78 row 42.
Do not modify generated assets during a full browser matrix. The overall goal
is not complete: 20,117 people remain not started. Legacy occupation timing
(468 labels), some rank classifications, source-document identity normalization
and numeric rejected-document counts need further review. Zero rejection-count
placeholders do not mean that no candidates were rejected; qualitative reasons
are preserved. A rotated privately provisioned key is needed only for authenticated
NARA work; ordinary public-source research can continue without it.
