# Batch 733 release - Papouschek-Parent research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 733 publishes reviewed outcomes for PDF page 357, rows 1-23, from
Charles A Papouschek through Jean P Parent. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, grades,
boxes, notes, and locations remain recoverable; protected identifiers remain
private.

Three identities are confirmed by direct official OSS evidence and seven are
linked at high confidence through exact official Army bulk matches. George J
Pappas and Nicholas G Pappas each receive a qualified 122nd Infantry Battalion
(Separate) pathway. Those relationships are medium-confidence,
probable-immediate military assignments based on a unit recruitment history
plus named roster entries. They are not civilian employers and are excluded
from confirmed/high analytics.

A contemporary 26 December 1941 newspaper documents Maxwell J Papurt as
executive director of the Pride of Judea Children's Home and as the former
chief psychologist of the New York State Department of Correction. Both jobs
are high-confidence, documented prewar employment. Neither is mislabeled as
his immediate pre-OSS affiliation or last civilian employer because the
accessible chronology does not prove that sequence.

Charles S Pappageorge and George L Pappageorge remain separate people and
source rows in a visible shared-identifier conflict. Jean Lucien Pardimene and
the Italian naval officer Gastone Pardo remain probable identity leads without
published affiliations. A same-name Greek Operational Group record for Angelo
Pappas is preserved as a rejected candidate rather than silently assigned.

The 23 reviewed people record 20 `requires_archival_review`, two
`conflicting_sources`, and one `documented_prewar_employer_found` outcome.
Identity statuses are three confirmed, seven high-confidence, two probable,
two conflicting, and nine unresolved. The reviewed bundle imports 13 sources,
reuses one organization, adds two organizations and four affiliations, 16
claims, 33 claim-source links, 23 person updates, and 23 consolidated research
attempts. Seven accepted and two conflicting identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,895 (41.3342%) |
| People with confirmed/high employer evidence | 334 (1.3952%) |
| People with confirmed/high affiliation evidence | 744 (3.1079%) |
| Archival-review dispositions assessed | 8,353 (34.8929%) |
| Not started | 14,039 |
| Possible duplicate groups | 523 |
| Conflicts | 329 |
| Attempts or plans | 18,083 |
| Claims by confidence | confirmed 1,381; high 2,938; medium 1,537; low 198; conflicting 291; unresolved 2 |
| Citation records / unique source documents | 5,707 / 2,885 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 286;
`documented_prewar_employer_found` 168; `in_progress` 1,903;
`needs_identity_review` 459; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,156; `not_started` 14,039;
`occupation_only_found` 1,047; `requires_archival_review` 4,046; and
`verified_employer_found` 289.

The public projection contains 2,489 published affiliations, 863
organizations, 4,483 public sources, and 6,140 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Astro diagnostics: 367 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,840 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 733, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,840 HTML files checked; every internal link resolved and
  50,743 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,310,225 bytes verified; manifest SHA-256
  `4aff88481c831544124ed67f072f1b0f5c53093fa29f0ffde1a6ca8102ff4efc`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,912 public artifacts, and 1,209 candidate substrings checked
  with zero unexpected boundary matches.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Two consecutive production builds reproduced output-tree SHA-256
  `d7097caea1524d8ea910c5093e9ecadaabf0bbe43f6ecd4b2e5084f25fde3165`.
* The supported bounded release suite completed cleanly; all retained
  historical batch specifications remain available through the unbounded
  command.

## Publication verification

Release commit
[`c2285f9679919e9a528c192fef7d1df699d12836`](https://github.com/therealjameswilson/before-oss/commit/c2285f9679919e9a528c192fef7d1df699d12836)
was pushed to `main`. The
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37228003637)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37228003693)
both completed successfully.

The immutable live verifier confirmed the deployment at
<https://therealjameswilson.github.io/before-oss/> against that exact commit:

* 67 public assets / 106,310,225 bytes matched the checked-in release
  manifest;
* the verified manifest SHA-256 was
  `4aff88481c831544124ed67f072f1b0f5c53093fa29f0ffde1a6ca8102ff4efc`;
* eight core routes, 30 source-register pages, and all 23 directly affected
  profiles resolved successfully.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-733-papouschek-parent --page 357 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch733.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page357-papouschek-parent-review_batch-733_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary is PDF page 357, rows 24-46, from Robert E Parent
through Hilda B Parker. No API key, raw API response, full service or officer
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
