# Batch 759 release - Pilone-Pipinias research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 759 publishes reviewed outcomes for PDF page 370, rows 1-18, from
Albert V Pilone through Eleftherios Pipinias. All 18 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes,
locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The 18 source rows remain linked to 18 separate person entities. Eight
row-specific candidate matches were reviewed: seven were accepted and the
Gero K Piper candidate remains probable because the official Army record spells
the given name `GERE`. Official Army bulk data is used as identity evidence
only; no coded Army occupation is converted into an employer or role.

A National Archives-published OSS conference volume identifies Irwin N. Pincus
as one of the Enemy Objectives Unit professionals who came from the Board of
Economic Warfare and records an April 1943 arrival. The Board of Economic
Warfare is therefore published at high confidence as his explicit immediate
pre-OSS government assignment, not as a civilian employer. No job title is
inferred.

Two independent institutional sources place David H. Pinkney in OSS Research
and Analysis and describe his Harvard doctoral study before wartime service.
Because the index row gives only `David Pinkney` and no row-specific identifier,
the identity remains probable. Harvard is published as a visibly qualified,
medium-confidence student affiliation, never as employment or as an immediate
pre-OSS affiliation.

An institutional roster assigns Eleftherios J. Pipinias to Company C, 87th
Infantry Regiment. A declassified OSS mission record independently names
Technician Fifth Grade Eleftherios J. Pipinias in Greek Operational Group VI.
Together with the protected-identifier match in the official Army bulk file,
these records support a high-confidence identity and Army assignment. They do
not establish the sequence between the 87th Infantry and OSS, so the assignment
is published with `temporal_relation_uncertain` and excluded from immediate-
affiliation analytics.

An obituary for Albert V. Pilone corroborates wartime Army service in England.
Its named garment, automobile-sales, and union roles are undated or postwar and
are deliberately excluded from the pre-OSS affiliation fields. The remaining
unsupported or common-name candidates are retained as unresolved archival
tasks rather than converted into public facts.

The reviewed evidence bundle imports eight sources, three organizations, three
affiliations, 13 claims, 28 evidence links, 18 person updates, and 18 completed
manual staged research protocols. The final cohort identity statuses are eight
high-confidence, two probable, two ambiguous, and six unresolved. Research
statuses are one `completed`, 12 `requires_archival_review`, four
`needs_identity_review`, and one `needs_temporal_review`.

The CIA cohort adapter stopped because the requested path was disallowed by the
retrieved robots policy, and the Library of Congress cohort check stopped on
HTTP 503 after bounded retries. These are recorded as source-access limits
rather than negative evidence. No authenticated NARA Catalog API request was
made, and no API key or raw API response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,480 (43.7779%) |
| People with confirmed/high employer evidence | 345 (1.4412%) |
| People with confirmed/high affiliation evidence | 779 (3.2541%) |
| Archival-review dispositions assessed | 8,939 (37.3407%) |
| Not started | 13,454 |
| Possible duplicate groups | 535 |
| Conflicts | 352 |
| Claims by confidence | confirmed 1,397; high 3,192; medium 1,569; low 198; conflicting 305; unresolved 2 |
| Citation records / unique source documents | 5,858 / 2,999 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 198; conflicting_sources 296; documented_prewar_employer_found 175;
in_progress 1,902; needs_identity_review 534; needs_temporal_review 25;
no_reliable_result_after_protocol 1,156; not_started 13,454;
occupation_only_found 1,052; requires_archival_review 4,516; and
verified_employer_found 297.

The public projection contains 23,939 person entities, 2,547 published
affiliations, 892 organizations, 4,634 public sources, and 6,456 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 393 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,870 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 759, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,870 HTML files checked; every internal link resolved and
  50,852 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 108,156,622 bytes verified; manifest SHA-256
  `0245f6cb450916dd1ff80a6168cd27bbd029235ab4262676630114951073c57c`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,942 public artifacts, and 1,238 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,942-file,
  311,495,180-byte output tree at SHA-256
  `6202d9214594df4ba4a7544e17b80e5fe08507c65c7d70910b045b08f6110fa5`.

## Publication verification

Publication is pending the release commit, GitHub Actions, and unauthenticated
live verification. This section will be updated with immutable workflow and
deployment receipts after the release reaches GitHub Pages.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-759-pilone-pipinias --page 370 --first-row 1 --last-row 18
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch759.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page370-pilone-pipinias-review_batch-759_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next unresearched person boundary is PDF page 370, row 19, Paul P Pipp.
No API key, raw API response, full service or officer number, copyrighted page
image, unrelated Army coded occupation, street address, modern people-finder
record, or private reviewer note is committed or published.
