# Batch 401: reviewed outcomes and pending release

The live-verified site currently contains Batch 400. This next local update
covers PDF page 78, rows 2-11, from Margaret I Chase through Arthur A
Chattillion. It preserves the Box 119/120 boundary and every printed spelling.

## Historical adjudication

One exact private-identifier match links Rene Chatellier to an Army entry
under Rene A. Chatellier. The dated occupation is qualified as Bartenders,
recorded March 21, 1944, with uncertain relation to OSS service. There is no
named employer, immediate predecessor, or last civilian employer. The index's
blank rank and indeterminate officer flag remain intact; a PVT grade at Army
entry does not rule out a later commission.

Nine identities remain unresolved, with individual Box 119 or 120 research
questions. The same-name calendar publisher, obituary index, postwar signature
lead, and family-only references were not converted into pre-OSS biographies.
Six source citations, one affiliation, two claims, five claim-source links,
ten person updates, and ten durable attempts are retained. Reimporting the
bundle does not grow these tables. New claims: one high identity claim and
one medium qualified occupation; zero new employer claims.

## Exact local coverage

| Measure | Count / denominator | Percent |
|---|---:|---:|
| Index coverage | 23,978 / 23,978 source rows | 100.0000% |
| Research attempted | 3,793 / 23,940 active people | 15.8438% |
| Verified affiliation | 485 / 23,940 active people | 2.0259% |
| Verified employer | 211 / 23,940 active people | 0.8814% |
| Archival disposition assessed | 3,746 / 23,940 active people | 15.6475% |

Stored entities: 23,941, including one superseded record. Possible duplicate
groups: 233. Commissioned classification: 2,228 yes, 5,617 no, 16,095 unknown.
Archival disposition is not physical-file examination; six entities have a
saved file-reviewed flag in the legacy database, and this batch adds none.

Status counts: not_started 20,147; in_progress 46; candidate_found 1;
needs_identity_review 106; needs_temporal_review 9; verified_employer_found
207; documented_prewar_employer_found 68; occupation_only_found 627;
conflicting_sources 69; no_reliable_result_after_protocol 82;
requires_archival_review 2,458; completed 120.

Claim confidence: confirmed 917, high 1,154, medium 821, low 57, conflicting
81. Employment/self-employment claim rows remain confirmed 35, high 270,
medium 83, low 0, conflicting 2, unresolved 0. These are claim counts, not
unique-person coverage. The database has 3,717 citation records, 1,736 legacy
document keys and 1,260 distinct non-null source URLs. The legacy-key count
is not a certified count of unique historical documents.

Public projection: 23,940 people; 502 organizations; 1,486 affiliation rows;
2,970 public-visible claims; 2,597 public source citations; 26 profile shards.
Private derived outputs include 23,771 archival pull-list rows, 22,918 rows
in the composite unresolved export, and 5,011 attempts/plans.

## Checks and release gates

- 82 Python unittest cases pass. SQLite integrity and foreign keys pass.
- The deterministic 200-profile structural/stratified audit passes. Its
  unsourced-gender stratum is explicitly unavailable, not inferred from names.
- All nine new browser cases pass (4.6 seconds). The first run had three
  test-only wording failures; the corrected assertion checks the public
  employer disclaimer rather than a private note that should not be rendered.
- The production build has 24,450 pages and zero Astro errors, warnings or
  hints. The public methodology now distinguishes occupation, rank date, and
  bounded archival-review outcomes.
- All internal targets resolve; 49,551 external URLs were inventoried, not all
  visited. All six citation targets returned HEAD 200. The full 1,629-case
  matrix is running and must pass before publication.
- All 67 manifest assets match their sizes/hashes: 83,204,891 bytes. Manifest:
  `504b084ac9f7a14a712dd8711e18bc06750beab3e3d8ab22017a5d3d648f491f`.
- Repeated public export matches the 70-file tree digest:
  `ca234e925b94b1f1f309bbe947eafe8d32d51c6ee840aaf6c1473d405e2238a4`.
- Consecutive final-methodology builds match the 24,522-file tree digest:
  `aa045cb0e7bafacc43cf4ffe2e906dd73215acaaa5000e50889f6c3230e0d1c8`.
- The final-methodology identifier audit covered 24,522 artifacts against
  12,926 normalized and 120 formatted private identifiers, with zero unexpected
  matches. The 1,081 substring coincidences were classified by the audit.
- No authenticated NARA API request was made. Dependencies and lockfile are
  unchanged; no fresh vulnerability count is asserted.

## Remaining work and resumption

The overall goal is incomplete. There are 20,147 unstarted people, 468 older
occupation-only temporal labels requiring individual review, and unresolved
source-document normalization. Live NARA API use needs a rotated key outside
source control; public-source research can continue without it. Do not use the
key previously pasted in chat.

Resume the existing full-matrix and GitHub jobs rather than starting duplicate
runs. From the repository, a one-batch replay is:

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-seventy-eight-margaret-chase-through-chattillion-pathways_batch-401_2026-09-04.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

A clean whole-database replay remains `scripts/rebuild-all.sh`. Do not run a
rebuild while another check uses the current generated site. Publish only
after the required checks, then verify the deployed manifest and direct routes.
