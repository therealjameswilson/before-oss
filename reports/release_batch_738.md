# Batch 738 release - Paterson-Patterson research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 738 publishes reviewed outcomes for PDF page 359, rows 24-46, from
Lewis C Paterson through Jere W Patterson. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, grades,
boxes, notes, and locations remain recoverable; protected identifiers remain
private.

Eleven people now have high-confidence identity assessments. Ten are based on
compatible official Army bulk matches. Pises Pattaborgse is resolved through
official Cornell records, a contemporary Cornell alumni article, and a
scholarly Free Thai/OSS index as Pises Pattabongse, also rendered Phiset
Pattaphong. His 1938-40 mechanical-engineering study and 1940 BME are
published as a student affiliation, never employment.

Larissa Patrekeyeva's postwar Library of Congress identity evidence remains
probable and is not projected backward into a pre-OSS job. The two Lewis C
Paterson rows remain separate probable/high-confidence entities pending Box
588 file comparison. Gardner Patterson's famous economist and Navy namesake
is explicitly rejected, and Jere W Patterson's postwar Parker Pen and
advertising leads are not published as pre-OSS work.

The 23 people record 22 requires_archival_review outcomes and one completed
outcome. Identity statuses are 11 high-confidence, two probable, and ten
unresolved. The reviewed bundle imports eight sources, one organization, one
affiliation, 14 claims, 30 claim-source links, 23 person updates, and 23
research attempts. Eleven accepted identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,008 (41.8063%) |
| People with confirmed/high employer evidence | 334 (1.3952%) |
| People with confirmed/high affiliation evidence | 748 (3.1246%) |
| Archival-review dispositions assessed | 8,466 (35.3649%) |
| Not started | 13,926 |
| Possible duplicate groups | 525 |
| Conflicts | 334 |
| Attempts or plans | 18,321 |
| Claims by confidence | confirmed 1,383; high 2,985; medium 1,539; low 198; conflicting 296; unresolved 2 |
| Citation records / unique source documents | 5,733 / 2,902 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 190; conflicting_sources 291;
documented_prewar_employer_found 168; in_progress 1,903;
needs_identity_review 459; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,926;
occupation_only_found 1,047; requires_archival_review 4,151; and
verified_employer_found 290.

The public projection contains 2,495 published affiliations, 866
organizations, 4,509 public sources, and 6,196 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 generated subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 372 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,844 pages.
* Browser release suite: 90 / 90 checks passed across desktop, phone, and
  tablet, including 21 Batch 738, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,844 HTML files checked; every internal link resolved and
  50,758 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,592,655 bytes verified; manifest SHA-256
  `29237f4eafa6c478ecadf2d83b82bf20ef46c8c8de282f98bb0d5bfa85a8e62b`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,916 public artifacts, and 1,210 candidate substrings checked
  with zero unexpected boundary matches.
* Two consecutive production builds reproduced the 24,916-file,
  308,902,502-byte output tree at SHA-256
  `999f81ea469cd16a32dc5029972be0743fcea90ce50d999f2a102b236bdb5790`.

## Publication verification

Publication verification is pending the release commit, GitHub Actions test,
GitHub Pages deployment, and immutable live-manifest comparison.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-738-paterson-patterson --page 359 --first-row 24 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch738.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page359-paterson-patterson-review_batch-738_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 360, rows 1-23, from John B Patterson
through Robert W Paul. No API key, raw API response, full service or officer
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
