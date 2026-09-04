# Batch 403 release verification

2026-09-04 UTC. **Local reviewed dataset; full testing/publication pending.**
The last live-verified release is Batch 401. Batch 402 PR 159 is awaiting the
corrected full Test run `33856421009`; its first run's stale-label failures
and passing targeted rerun are documented in `release_batch_402.md`.

## What changed

PDF page 78 rows 22–31, Cheffins through Chenowith: ten individual research
outcomes, six high-confidence identity claims and six medium-confidence
occupation observations. Four people require archival resolution. Three
low-confidence identity candidates are retained in the research evidence bundle,
not exported as public claims. No organization or employer is invented.

The idempotent bundle contains seven sources, six affiliations, fifteen claims,
thirty-six claim-source links, ten updates and ten durable research attempts.
All 9,200,232 official Army bulk records were compared transiently twice; the
second pass tested the Vung name candidate. No raw rows, full identifiers or
authenticated Catalog API content were retained. The complete index page and
relevant technical/code-list page images were inspected.

| Person | Outcome and limits |
|---|---|
| Elmer T Cheffins | Army observation 1943-07-15: Routemen; no company or route inferred |
| George L Chekani | 1942-09-16: Cooks, except private family; no restaurant inferred |
| C A Chekrezi | Probable biographical candidate, not an accepted employer or OSS employment claim |
| Michael C Chemsak | 1942-09-05: Meatcutters, except in slaughtering and packing houses; no shop inferred |
| Tung-Yu Chen | Unresolved; modern namesakes excluded |
| Vung T Chen | Ambiguous; different-number Army candidate is postwar, not accepted |
| Wilson P Chenevert | 1943-10-07: Attendants, filling stations and parking lots; category not narrowed |
| Clarence L Cheney | 1944-01-17: Clerks, general; no office/employer inferred |
| Jane P Chennault | Unresolved; inaccessible newspaper lead and adjacent names not adopted |
| George N Chenowith | 1942-05-09: Painters, construction and maintenance; Maryland Chenoweth lead remains unlinked |

Observation dates are in explicit date-precision notes; actual employment
start/end dates and work locations are unknown and remain null. None of these
observations is marked immediate pre-OSS or last civilian employer. Earlier
Army private grades do not determine later OSS officer classification.

Hamit Kaba's chapter (not the uploader's name) supplies the Chekrezi candidate
context; cooperation with OSS is not employment. Its text was reviewed but
page-image retrieval failed, so no public biography is asserted. The McKeesport
banner is only corroborative context; the adjacent Vietnam-era Michael A.
Chemsak is not assigned to Michael C. Maryland's indexed archival pointer is
not a reviewed service file. Restricted/failed source opens were not bypassed.

## Exact counts from SQLite

| Measure | Numerator / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,813 / 23,940 active people | 15.9273% |
| Verified-employer coverage | 212 / 23,940 active people | 0.8855% |
| Verified-affiliation coverage | 486 / 23,940 active people | 2.0301% |
| Archival disposition assessed | 3,766 / 23,940 active people | 15.7310% |

Stored entities: 23,941, including one superseded record. Possible duplicate
groups: 233. Commissioned: 2,229 yes, 5,617 no, 16,094 unknown. Identity statuses:
739 confirmed, 552 high confidence, 123 probable, 65 ambiguous, 70 conflicting,
22,391 unresolved. The six legacy file-reviewed flags are not the denominator
for archival disposition coverage and do not certify physical-file review.

| Active research status | People |
|---|---:|
| not_started | 20,127 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 208 |
| documented_prewar_employer_found | 68 |
| occupation_only_found | 633 |
| conflicting_sources | 69 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,471 |
| completed | 120 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 917 | 35 |
| high | 1,168 | 272 |
| medium | 828 | 83 |
| low | 60 | 0 |
| conflicting | 81 | 2 |
| unresolved | 0 | 0 |

3,731 citation records; 1,742 legacy document keys; 1,266 distinct non-null
source URLs. Keys are not certified unique historical documents. Research
inventory: 518 organizations, 1,507 affiliations, 3,054 claims, 6,917 links,
5,031 attempts/plans (1,659 source-reviewed outcomes). 1,470 people have a
stored claim; 1,420 have a public-visible claim. Broad conflict union: 74.
Composite unresolved export: 22,911 people. Pull list: 23,770 source rows.

Public projection: 23,940 people, 506 organizations, 1,496 affiliations, 2,991
claims, 2,608 source citations and 26 profile shards. All six new occupation
claims are excluded from default verified-employer/affiliation analytics.

## Checks completed

- 84 Python tests initially passed in 4.138 seconds; strict evidence-schema validation,
  repeated import, SQLite integrity and foreign keys passed.
- Adding a reusable commit-pinned live-release verifier brings the final Python
  suite to **90 passing tests in 4.338 seconds**. Its six mock tests make no
  network request. Four existing SQLite connection-cleanup ResourceWarnings
  appeared on this run; they were not suppressed and did not fail tests.
- Twelve focused Batch 403 browser tests passed in 6.2 seconds, across desktop,
  phone and tablet. They cover all ten profiles, search, citations, unknown
  work dates/locations, raw index retention and exclusion of speculative claims.
- A 200-profile deterministic structural/stratified audit passed. This does
  not replace independent historical re-review; gender is not inferred and the
  women stratum remains unavailable without sourced classification.
- Production build: 24,454 HTML pages, zero Astro errors/warnings/hints. All
  internal targets resolve; 49,559 external URLs inventoried, not all visited.
- Identifier audit: 12,926 normalized identifiers, 120 formatted variants,
  24,526 artifacts, 1,081 classified substring coincidences, zero unexpected
  boundary matches. Full serial numbers are not public fields.
- Chenevert's rendered local profile was visually checked; complete accessible
  text confirms grouped occupation, date caveat, masked serial and claim links.
- Consecutive exports/builds match. Public tree: 70 files, digest
  `988797fbd14e8be6ae74828ff38f21aee652a63cc2d9345369b982a561c420b4`.
  Production tree: 24,526 files, digest
  `ac382b806f4164f40085163cfb5182f465ed8f499fc3b4f5458e572de3311608`.
  Digests hash sorted relative paths, a NUL separator and binary file SHA-256s.
- Manifest: 67 assets, 83,362,842 bytes, SHA-256
  `43e7ab5002f3687871d688d1c447b5cd472c526015191e18b4f606b7e4d995e4`;
  generated checkpoint 2026-09-04T09:19:41Z.
- A full profile-shard comparison against Batch 402 changes exactly the ten
  intended people; no unrelated person or source row changed.

The complete 1,653-test local browser/accessibility matrix is running. No
Batch 403 deployment is claimed. Dependencies/lockfile remain unchanged.

## Resume and limits

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-seventy-eight-cheffins-through-chenowith-pathways_batch-403_2026-09-04.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npm run test:e2e
npm run check:links
```

Full replay: `bash scripts/rebuild-all.sh`. Next cohort starts at PDF page 78
row 32. Do not restart a live test process just because observation times out.
The overall goal is incomplete: 20,127 people not started; 468 older occupation
timing labels and some rank classifications need individual review. Distinct
rejected-document counts were not reliably retained in this research protocol;
zero placeholders must not be read as proof that no candidates were rejected.
Qualitative rejection reasons and access failures remain saved. Source-document
normalization is unresolved. A rotated, privately provisioned key is required
only for authenticated NARA work; public-source research remains available.
