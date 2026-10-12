# Batch 750 release - Peters-Peterson research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 750 publishes reviewed outcomes for PDF page 365, rows 24-46, from
Joseph C Peters through John R Peterson. All 23 printed rows were visually
checked against a 300-dpi page render. This corrects the prior Batch 749
handoff note: page 365 row 24 is Joseph C Peters, not Norma E Peters. No Norma
E Peters row appears in the index. Original spellings, ranks, boxes, notes,
locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The 23 source rows remain linked to 23 separate person entities. The John A
Petersen and John A Peterson rows share a protected identifier but preserve
their different printed surnames and remain unmerged pending personnel-file
review. The two Chester E Peterson rows have different protected identifiers
and likewise remain separate. Charlotta Peterson's `Also 120` note, Le Moyne
Peters's `CAF-4` grade, Virginia D Peters's `CAF-3` grade, and John R
Peterson's Major rank are preserved without silent reinterpretation.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Glenn R Petersen, Henry Petersen, John H Petersen, and Ross T
Petersen. Those matches establish identity only; no coded Army occupation is
converted into an employer or occupation claim. John A Petersen remains a
probable match because the protected identifier also appears on the separate
John A Peterson row. John A Peterson is conflicting. One Chester E Peterson
row conflicts with an official Army candidate named Andrew D Pedersen, while
the second same-name row remains ambiguous because it carries a different
identifier. These rows are exposed through neutral possible-duplicate review
groups rather than silently merged.

Exact-name OSS, employment/occupation, obituary, institutional, directory,
newspaper, military, and archival searches were reviewed for all 23 people.
The accessible sources did not establish a reliable pre-OSS employer for any
member of this cohort, so no employer claim was created. Each profile instead
publishes a dignified reviewed status and, where appropriate, explains that
the indexed personnel file may require archival examination.

The reviewed evidence bundle imports two sources, zero organizations, zero
affiliations, four high-confidence identity claims, eight claim-source links,
23 person updates, and 23 completed research attempts. Ten identity decisions
are recorded: four accepted, one probable, and five conflicting. The final
cohort identity statuses are four high-confidence, one probable, two
conflicting, one ambiguous, and 15 unresolved. Research statuses are four
`needs_identity_review` and 19 `requires_archival_review`.

The CIA cohort adapter failed before a person query because its robots policy
could not be retrieved, and the Library of Congress cohort run ended on a
source error. These are recorded as source-access limits rather than negative
evidence. No authenticated NARA Catalog API request was made, and no API key
or raw API response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,279 (42.9383%) |
| People with confirmed/high employer evidence | 340 (1.4203%) |
| People with confirmed/high affiliation evidence | 764 (3.1914%) |
| Archival-review dispositions assessed | 8,738 (36.5011%) |
| Not started | 13,655 |
| Possible duplicate groups | 531 |
| Conflicts | 344 |
| Claims by confidence | confirmed 1,392; high 3,092; medium 1,554; low 198; conflicting 299; unresolved 2 |
| Citation records / unique source documents | 5,795 / 2,948 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 294;
documented_prewar_employer_found 171; in_progress 1,902;
needs_identity_review 487; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,655;
occupation_only_found 1,050; requires_archival_review 4,378; and
verified_employer_found 294.

The public projection contains 23,939 person entities, 2,521 published
affiliations, 881 organizations, 4,571 public sources, and 6,330 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 384 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,859 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 750, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,859 HTML files checked; every internal link resolved and
  50,802 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,407,064 bytes verified; manifest SHA-256
  `201294866311b2e9859b1e7370e3b75933131c6d3d2bfc2ba6adc86c76aaf7c4`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,931 public artifacts, and 1,233 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,931-file,
  310,305,107-byte output tree at SHA-256
  `777acf40450a04c6e97a2f1351553b0933a308242250bd5ad4a3c0e975a1005a`.

## Publication verification

Publication verification is pending the release commit, GitHub Actions Test
and Pages workflows, and the immutable deployed-release comparison.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-750-peters-peterson --page 365 --first-row 24 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch750.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page365-peters-peterson-review_batch-750_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 366, row 1, Josephine S Peterson. No
API key, raw API response, full service or officer number, copyrighted page
image, unrelated Army coded occupation, street address, modern people-finder
record, or private reviewer note is committed or published.
