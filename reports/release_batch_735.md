# Batch 735 release - Parker-Parrott research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 735 publishes reviewed outcomes for PDF page 358, rows 1-23, from
James C Parker through Marian A Parrott. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, grades,
boxes, notes, and locations remain recoverable; protected identifiers remain
private.

Six exact official Army bulk matches establish high-confidence identities
without turning coded Army data into employer evidence. The printed Lester
Parkes identifier is shared with a separate Robert L Miller row, while two
exact-name Lester N Parkes Army records also exist. The conflict remains
public, no Army metadata is transferred, and the relevant files receive
critical archival-review priority.

Charles M Parkin Jr. and Robert R Parrish reuse stronger prior reviewed
evidence instead of receiving duplicate claims. Parkin retains his confirmed
immediate Army Corps of Engineers School assignment at Fort Belvoir and a
separately labeled Penn State student affiliation. Parrish retains a
high-confidence prewar film-editing occupation; no studio is inferred as his
employer. Fourteen other people remain unresolved after the staged protocol.

The 23 people record 20 requires_archival_review outcomes, one completed
outcome, one occupation_only_found outcome, and one conflicting_sources
outcome. Identity statuses are eight high-confidence, one conflicting, and 14
unresolved. The reviewed bundle imports two sources, seven claims, 14
claim-source links, 23 person updates, and 21 new consolidated research
attempts while reusing the two earlier complete research outcomes. Six
accepted and three conflicting identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,939 (41.5180%) |
| People with confirmed/high employer evidence | 334 (1.3952%) |
| People with confirmed/high affiliation evidence | 745 (3.1121%) |
| Archival-review dispositions assessed | 8,397 (35.0767%) |
| Not started | 13,995 |
| Possible duplicate groups | 523 |
| Conflicts | 331 |
| Attempts or plans | 18,177 |
| Claims by confidence | confirmed 1,382; high 2,952; medium 1,537; low 198; conflicting 293; unresolved 2 |
| Citation records / unique source documents | 5,714 / 2,889 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 188; conflicting_sources 288;
documented_prewar_employer_found 168; in_progress 1,903;
needs_identity_review 459; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,995;
occupation_only_found 1,047; requires_archival_review 4,088; and
verified_employer_found 289.

The public projection contains 2,490 published affiliations, 863
organizations, 4,490 public sources, and 6,157 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Astro diagnostics: 369 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,840 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 735, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,840 HTML files checked; every internal link resolved and
  50,745 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,389,722 bytes verified; manifest SHA-256
  d588b93f0f674b56aaa129d7cc5cde4f2dd6da8b1c31c97c3ceda0648d97081f.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,912 public artifacts, and 1,205 candidate substrings checked
  with zero unexpected boundary matches.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Two consecutive production builds reproduced output-tree SHA-256
  6eaab88f0604ead9f4897d663dd0cd7a06cc7c9c7b69a0dde5d16d2f72fcfef8.
* The supported bounded release suite completed cleanly; all retained
  historical batch specifications remain available through the unbounded
  command.

## Publication verification

Release commit
[d60cd360d1365d9bded6a4089a6b18fdc789897d](https://github.com/therealjameswilson/before-oss/commit/d60cd360d1365d9bded6a4089a6b18fdc789897d)
was pushed to main. The
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37233592099)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37233592128)
both completed successfully.

The immutable live verifier confirmed the deployment at
<https://therealjameswilson.github.io/before-oss/> against that exact commit:

* 67 public assets / 106,389,722 bytes matched the checked-in release
  manifest;
* the verified manifest SHA-256 was
  d588b93f0f674b56aaa129d7cc5cde4f2dd6da8b1c31c97c3ceda0648d97081f;
* eight core routes, 30 source-register pages, and all 23 directly affected
  profiles resolved successfully.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-735-parker-parrott --page 358 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch735.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page358-parker-parrott-review_batch-735_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 358, rows 24-46, from Arthur J Parry
through John Pascone. No API key, raw API response, full service or officer
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
