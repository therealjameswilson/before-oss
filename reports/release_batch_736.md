# Batch 736 release - Parry-Pascone research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 736 publishes reviewed outcomes for PDF page 358, rows 24-46, from
Arthur J Parry through John Pascone. All 23 printed rows were visually checked
against a 300-dpi page render. Original spellings, ranks, grades, boxes, notes,
and locations remain recoverable; protected identifiers remain private.

Seven exact official Army bulk matches establish high-confidence identities
without turning coded Army data into employer evidence. William E Parry's
indexed protected identifier points to a different Army name, and two Marvin F
Partain candidate rows also point to different Army names. Both conflicts
remain public, no mismatched metadata is transferred, and the relevant files
receive critical archival-review priority.

No defensible pre-OSS employer was found for the cohort. Discovery-only,
chronologically conflicting, and unbridged namesake leads remain unpublished.
The 23 people record 21 requires_archival_review outcomes and two
conflicting_sources outcomes. Identity statuses are seven high-confidence,
two conflicting, and 14 unresolved. The reviewed bundle imports two sources,
nine claims, 18 claim-source links, 23 person updates, and 23 research
attempts. Seven accepted and three conflicting identity decisions are
recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,962 (41.6141%) |
| People with confirmed/high employer evidence | 334 (1.3952%) |
| People with confirmed/high affiliation evidence | 745 (3.1121%) |
| Archival-review dispositions assessed | 8,420 (35.1727%) |
| Not started | 13,972 |
| Possible duplicate groups | 523 |
| Conflicts | 333 |
| Attempts or plans | 18,225 |
| Claims by confidence | confirmed 1,382; high 2,959; medium 1,537; low 198; conflicting 295; unresolved 2 |
| Citation records / unique source documents | 5,716 / 2,890 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 188; conflicting_sources 290;
documented_prewar_employer_found 168; in_progress 1,903;
needs_identity_review 459; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,972;
occupation_only_found 1,047; requires_archival_review 4,109; and
verified_employer_found 289.

The public projection contains 2,490 published affiliations, 863
organizations, 4,492 public sources, and 6,166 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Astro diagnostics: 370 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,840 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 736, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,840 HTML files checked; every internal link resolved and
  50,745 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,426,910 bytes verified; manifest SHA-256
  `8ecba51ab99db461454cb0812350680952b89d9e07acd7b2453885e32ece19e1`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,912 public artifacts, and 1,207 candidate substrings checked
  with zero unexpected boundary matches.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Two consecutive production builds reproduced the 24,912-file,
  308,630,039-byte output tree at SHA-256
  `b917c1677589c8779484a15a1a3141e7928ebf2d1f507901948f6447e57cc11c`.

## Publication verification

Publication verification is pending the immutable release commit and GitHub
Pages deployment.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-736-parry-pascone --page 358 --first-row 24 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch736.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page358-parry-pascone-review_batch-736_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 359, rows 1-23, from Angeline Pascuzzi
through Jane Paterson. No API key, raw API response, full service or officer
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
