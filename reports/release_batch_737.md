# Batch 737 release - Pascuzzi-Paterson research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 737 publishes reviewed outcomes for PDF page 359, rows 1-23, from
Angeline Pascuzzi through Jane Paterson. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, grades,
boxes, notes, and locations remain recoverable; protected identifiers remain
private.

Eleven people now have high-confidence identity assessments. Seven come from
compatible exact official Army bulk matches; Felix Pasqualino is corroborated
by an exact-name, exact-rank NARA OSS record; Sebastian J Passanesi by a state
historic-context report and official Marine Corps biography-file index; Lloyd
Edwin Patch by name, rank, and identifier agreement; and Paul J Paterni by a
wartime OSS report and independent institutional sources. These identity-only
records do not become employer claims.

Passanesi's 1935 Catholic University of America degree is published as a
student affiliation, never employment. Paterni's evidence supports three
separate relationships: U.S. Army as the immediate pre-OSS military
assignment; U.S. Secret Service as the last civilian affiliation before Army
service; and U.S. Veterans Administration as earlier prewar government
employment. The second indexed Paterni row remains a separate probable entity
pending comparison of the two Box 588 files. John Pastilock's official Army
name conflict remains visible and receives critical archival priority.

The 23 people record 20 requires_archival_review outcomes, one completed
outcome, one conflicting_sources outcome, and one verified_employer_found
outcome. Identity statuses are 11 high-confidence, one probable, one
conflicting, and ten unresolved. The reviewed bundle imports nine sources,
four organizations, four affiliations, 16 claims, 33 claim-source links, 23
person updates, and 23 research attempts. Seven accepted and one conflicting
identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,985 (41.7102%) |
| People with confirmed/high employer evidence | 334 (1.3952%) |
| People with confirmed/high affiliation evidence | 747 (3.1204%) |
| Archival-review dispositions assessed | 8,443 (35.2688%) |
| Not started | 13,949 |
| Possible duplicate groups | 524 |
| Conflicts | 334 |
| Attempts or plans | 18,273 |
| Claims by confidence | confirmed 1,383; high 2,973; medium 1,537; low 198; conflicting 296; unresolved 2 |
| Citation records / unique source documents | 5,725 / 2,898 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 189; conflicting_sources 291;
documented_prewar_employer_found 168; in_progress 1,903;
needs_identity_review 459; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,949;
occupation_only_found 1,047; requires_archival_review 4,129; and
verified_employer_found 290.

The public projection contains 2,494 published affiliations, 865
organizations, 4,501 public sources, and 6,182 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 generated subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 371 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,843 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 737, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,843 HTML files checked; every internal link resolved and
  50,754 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,522,368 bytes verified; manifest SHA-256
  `cb2628ceea98dcb48877ed9ba1a1350102c600e119383c7678a65586f7ec4627`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,915 public artifacts, and 1,209 candidate substrings checked
  with zero unexpected boundary matches.
* Two consecutive production builds reproduced the 24,915-file,
  308,788,468-byte output tree at SHA-256
  `d7f404bd7f8af4668275a379e04ce0e8f296997167c0f8ff87be7f12081220a4`.

## Publication verification

Release commit
[258badc555e34a73894f7a64e84979904476e6b9](https://github.com/therealjameswilson/before-oss/commit/258badc555e34a73894f7a64e84979904476e6b9)
was pushed to main. The
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37238196451)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37238196469)
both completed successfully.

The immutable live verifier confirmed the deployment at
<https://therealjameswilson.github.io/before-oss/> against that exact commit:

* 67 public assets / 106,522,368 bytes matched the checked-in release
  manifest;
* the verified manifest SHA-256 was
  `cb2628ceea98dcb48877ed9ba1a1350102c600e119383c7678a65586f7ec4627`;
* eight core routes, 31 source-register pages, and all 23 directly affected
  profiles resolved successfully.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-737-pascuzzi-paterson --page 359 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch737.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page359-pascuzzi-paterson-review_batch-737_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 359, rows 24-46, from Lewis C Paterson
through Jere W Patterson. No API key, raw API response, full service or officer
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
