# Batch 401 release verification

Checkpoint: 2026-09-04 UTC. Public URL:
https://therealjameswilson.github.io/before-oss/

PR 158 merged at 05:28:43 UTC:
https://github.com/therealjameswilson/before-oss/pull/158

- Reviewed head: `dd3d2cbc9e6493ccde68e156db091085beae6946`
- Merge: `2f8531e7165bf67fc29bf7649ecc4660901cf32c`
- Premerge Test 33839016615: **success**, including 82 Python tests,
  **1,629 / 1,629 browser cases** in 22.8 minutes, and identifier redaction.
- Local full matrix: 1,628 pass, one phone timeout in an older Batch 329
  scenario, 31.5 minutes. The error records a closed Chromium protocol
  session. That case passed unchanged on isolated rerun in 1.9 seconds.
  The original full run is not described as clean.
- Pages 33840631003: **success**; deployed Batch 401 was verified.
- Postmerge Test 33840631008: in progress at this checkpoint.
- Live asset verification: all 67 assets match the reviewed manifest byte
  lengths and SHA-256 hashes (83,204,891 bytes); all seven core routes and
  ten Batch 401 direct profiles return HTTP 200 and expected content. Live
  statistics exactly match the local reviewed projection.

## Public content and exact coverage

Ten reviewed people on index page 78, rows 2-11: Margaret I Chase through
Arthur A Chattillion. Rene Chatellier gains a high-confidence identity link
and one visibly qualified, temporally uncertain Army-entry occupation.
Nine identities remain unresolved with individual archival questions. No
employer is newly verified, and no earlier rank is used to infer a later
commissioned status. The methodology explains these distinctions.

| Measure | Numerator / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 rows, 522 / 522 pages | 100.0000% |
| Research-attempt coverage | 3,793 / 23,940 active people | 15.8438% |
| Verified-employer coverage | 211 / 23,940 active people | 0.8814% |
| Verified-affiliation coverage | 485 / 23,940 active people | 2.0259% |
| Archival disposition assessed | 3,746 / 23,940 active people | 15.6475% |

Stored entities: 23,941, one superseded. Duplicate groups: 233. Commissioned:
2,228 yes; 5,617 no; 16,095 unknown. Archival disposition does not mean the
physical personnel file was examined; six legacy file-reviewed flags remain.

### All research statuses

| Status | People |
|---|---:|
| not_started | 20,147 |
| in_progress | 46 |
| candidate_found | 1 |
| needs_identity_review | 106 |
| needs_temporal_review | 9 |
| verified_employer_found | 207 |
| documented_prewar_employer_found | 68 |
| occupation_only_found | 627 |
| conflicting_sources | 69 |
| no_reliable_result_after_protocol | 82 |
| requires_archival_review | 2,458 |
| completed | 120 |

### Claim and citation inventory

| Claim confidence | All claim rows | Employment/self-employment claim rows |
|---|---:|---:|
| confirmed | 917 | 35 |
| high | 1,154 | 270 |
| medium | 821 | 83 |
| low | 57 | 0 |
| conflicting | 81 | 2 |
| unresolved | 0 | 0 |

3,717 citation records; 1,736 legacy document keys; 1,260 distinct non-null
source URLs. The document keys are not a certified unique-document count.
There are 5,011 durable attempts/plans; a planned query is not an attempt.
Public output has 502 organizations, 1,486 affiliations, 2,970 claims,
2,597 source citations, and 26 profile shards. Composite unresolved export:
22,918 people. Archival pull list: 23,771 source rows.

## Reproducibility and checks

- SQLite integrity and foreign keys pass; deterministic 200-profile
  structural/stratified audit passes. No gender category is guessed.
- Production build: 24,450 pages; zero Astro errors, warnings, or hints.
- Every internal target resolves. 49,551 external URLs are inventoried,
  **not** all visited; six new source targets returned HEAD 200.
- Final identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,522 artifacts, 1,081 classified substring coincidences,
  **zero unexpected boundary matches**.
- Two consecutive final builds match the 24,522-file tree digest:
  `aa045cb0e7bafacc43cf4ffe2e906dd73215acaaa5000e50889f6c3230e0d1c8`.
- Repeated public export matches the 70-file tree digest:
  `ca234e925b94b1f1f309bbe947eafe8d32d51c6ee840aaf6c1473d405e2238a4`.
- Public manifest: 67 assets, 83,204,891 bytes; SHA-256:
  `504b084ac9f7a14a712dd8711e18bc06750beab3e3d8ab22017a5d3d648f491f`.
- Dependencies and lockfile unchanged. No authenticated NARA API calls.

## Continuation and limits

The goal remains incomplete: 20,147 people are not started, 468 older
occupation-timing claims require individual review, and source-document
normalization is unresolved. A rotated, privately provisioned key is needed
for authenticated NARA API work, not for all public-source research.

Batch 402's ten-person discovery checkpoint is committed separately. Its
three exact Army links and institutional leads are **not imported outcomes**
and do not increase the counts above. Some institutional retrievals were
blocked; no restrictions were bypassed. Continue from
`research/batch-402-discovery-checkpoint.md` and adjudicate each person before
creating the reviewed bundle. Do not rerun already-completed release jobs.

Batch 401 replay commands are recorded in `reports/batch_401_release.md`;
`scripts/rebuild-all.sh` remains the complete database replay. The local
preview is http://127.0.0.1:4321/before-oss/ while its preview process runs.
