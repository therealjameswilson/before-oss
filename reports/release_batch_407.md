# Batch 407 release checkpoint

2026-09-04 UTC. **Reviewed local data; independent GitHub QA pending.**
No Batch 407 deployment is claimed. Batch 406 passed independent GitHub Test
33894971764, merged through PR 163, deployed through Pages 33900368779 and
passed pinned live verification.

## Research

Nine new individuals from page 79 rows 16-25, omitting already-researched Paul
C Child. His correction was included in Batch 406 and gets no new-person
credit here. The complete page was re-inspected; raw names, ranks, numbers,
boxes and location remain unchanged. Two full transient 9,200,232-row Army
scans support the comparisons. No authenticated Catalog calls were made.

- William Chidekel: high-confidence exact name/identifier Army match and a
  medium-confidence apprenticeship observation. The NYU list is from 1948,
  independently unlinked and not a pre-OSS employer.
- Dawson W Chiles: high-confidence exact name/identifier match and a qualified
  Student observation, supported by the inspected official corrected code
  list. No institution is named or inferred. Study is not employment.
- Frank R Chiella and Harold A Childs: explicit identifier/name conflicts.
  Neither candidate occupation is published. Harold's other name candidate
  differs from the printed number in six positions; no number is corrected.
- Shirley A Chidsey: probable identity candidate, withheld pending a direct
  index bridge. CIA review and postwar journal references do not settle her
  pre-OSS employer. A commercial editorial-work account remains discovery only.
- Howard Child, Lois O Child, Alton Q Childs and Francis V Childs remain
  unresolved, each with a saved individual outcome and Box 121 next action.

Two occupation/status observations, five archival-review dispositions and two
conflicts are not nine verified employers. Temporal relations to OSS remain
uncertain for both occupational observations; start/end dates and workplace
locations remain null, and immediate/last-civilian flags are false. Only
published/qualified evidence or explicit conflicts enter the public projection.

Sources: 10 citation entries; no new organizations; 2 affiliations; 8 claims;
24 claim-source links; 9 person updates and 9 attempts. Import is idempotent.
The two low-confidence candidate claims remain private. Source-access failures,
text-only versus visual inspection, discovery-only leads and the staged search
record are retained in `research/batch-407-discovery-checkpoint.md`.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows; 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,852 / 23,940 active people | 16.0902% |
| Verified-employer coverage | 213 / 23,940 active people | 0.8897% |
| Verified-affiliation coverage | 488 / 23,940 active people | 2.0384% |
| Archival disposition assessed | 3,805 / 23,940 active people | 15.8939% |

23,941 stored entities, one superseded; 233 possible duplicate groups. Officer
classification: 2,229 commissioned, 5,618 noncommissioned, 16,093 indeterminate.
Identity: 740 confirmed, 567 high confidence, 124 probable, 70 ambiguous,
72 conflicting and 22,367 unresolved. Personnel categories are unchanged.

| Research status | Active people |
|---|---:|
| not_started | 20,088 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 208 |
| documented_prewar_employer_found | 69 |
| occupation_only_found | 644 |
| conflicting_sources | 71 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,495 |
| completed | 121 |

| Claim confidence | All claims | Employment/self-employment claims |
|---|---:|---:|
| confirmed | 919 | 35 |
| high | 1,185 | 273 |
| medium | 838 | 82 |
| low | 72 | 1 |
| conflicting | 83 | 2 |
| unresolved | 0 | 0 |

3,777 citations; 1,769 legacy document keys, not certified unique historical
documents; 1,290 distinct stable URLs. 521 organizations, 1,521 affiliations,
3,097 claims, 7,037 claim-source links. 5,071 attempts/plans: 1,699 source_reviewed,
160 candidate_found, 619 candidate_rejected, 2,006 no_result and 587 planned.
1,496 people have stored claims; 1,438 have public claims. Composite unresolved
export: 22,898. Conflict union: 76. Pull list: 23,770 source rows; review queue:
23,940 people. No physical personnel file examined; six legacy reviewed flags
are not certified physical-file examinations in this session.

Public: 23,940 people, 509 organizations, 1,510 affiliations, 3,022 claims,
2,641 citations and 26 profile shards. No verified-employer increase is claimed.

## Software and data checks

- All 90 Python tests pass in 4.143 seconds; existing SQLite cleanup
  ResourceWarnings remain visible. Integrity and foreign keys pass. A
  diagnostic query initially used an incorrect table name, then was corrected
  to the actual entity_supersessions table; no data was mutated by that check.
- The deterministic 200-profile structural audit passes, not an independent
  historical re-review. The women stratum is unavailable without sourced
  classification; no gender inference is made.
- All twelve focused checks pass in 8.5 seconds after the repeated build
  completed. An earlier 8.7-second pass overlapped the determinism command's
  startup and is not the final check used here. No assertion repair was needed.
- Final production build: 24,457 HTML pages, zero Astro errors/warnings/hints;
  first reported elapsed 2m 43s. Repeated export and build are byte-identical.
- All internal links resolve; 49,575 external destinations inventoried, not
  all visited. Privacy: 12,926 normalized identifiers, 120 formatted variants,
  24,529 artifacts, 1,079 substring coincidences, zero unexpected boundary
  matches, zero aggregate or manifest-size exceptions.
- All 26 public profile shards compared with Batch 406: exactly the nine
  intended new profiles changed. The Paul Child correction was not altered.
- Manifest: 67 assets / 83,651,737 bytes; SHA-256
  `159e135485d99f2e565fa6dc9e4f0156acb6f2836bed89c456d1cb6291cd2d79`.
- Public tree: 70 files; SHA-256
  `3f03d4f7e1a2dd9b0301b3e4e8e3e1261bf7d7240ea20a2780001f1b1cb1f91a`.
- Production tree: 24,529 files; SHA-256
  `71053a3f10579be0d8d0abf0ce3d0fc610691928a920df48582377bcb27e0f77`.
  Tree digests use sorted relative paths, NUL separators and binary file hashes.

The full 1,707-case local suite finished with 1,701 passes and six timeouts in
56.0 minutes, with retries disabled. Five timeouts reported closed browser
sessions and one was an accessibility timeout; no assertion contradicted the
Batch 407 data. The six unchanged affected scenarios then passed across all
three viewports, 18/18 in 1.5 minutes, again without retries. Failure artifacts
from the initial run are preserved outside the generated test-results folder.
This is not represented as a clean first-run full-matrix pass. Independent
GitHub Test, Pages deployment and pinned live verification remain required
before publication.

## Resume and limitations

```sh
python3 -m oss_research import-reviewed-evidence research/evidence-page-seventy-nine-chidekel-through-chiles-pathways_batch-407_2026-09-04.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
cd site
PUBLIC_SITE_URL=https://therealjameswilson.github.io PUBLIC_BASE_PATH=/before-oss npm run build
npm run test:e2e
npm run check:links
```

Next cohort: page 79 rows 26-35, Durwood W Chiles through Corning Chisolm.
Full replay: `bash scripts/rebuild-all.sh`. The research goal remains active and
incomplete. No access blocker prevents further public-source work. Rotate the
previously exposed credential before authenticated NARA work; do not use it.
Legacy methodological issues remain: 468 occupation timing labels, older rank
classification, rejected-document counting, source-document identity and
independent historical profile review. Do not relabel pending people as complete.
