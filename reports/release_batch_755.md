# Batch 755 release - Phillips-Piantadosi research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 755 publishes reviewed outcomes for PDF page 368, rows 1-23, from
Kenneth H Phillips through Louis Piantadosi. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes,
notes, locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The 23 source rows remain linked to 23 separate person entities. Nine
exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Kenneth H Phillips, Paul A Phillips, Perecles P Phillips,
William R Phillips, Robert L Philpot, Charles H Phipps, Edward A Phipps, Peter
C Photis, and Arthur R Piantadosi. Those matches establish identity only; no
coded Army occupation is converted into an employer or role.

Perecles P Phillips is additionally corroborated by the Greek Operational
Group soldier-monument roster, which documents the expanded name Perecles
Peter "Perry" Phillips. Peter C Photis is corroborated by the same roster and
a detailed funeral-home obituary that directly links him to OSS commando
service and Company C, 2671st Special Reconnaissance Battalion. The obituary's
1953-1995 nightclub ownership is postwar and is not projected backward as a
pre-OSS employer.

An official CIA Reading Room search lead names a Captain Robert S. Phillips in
an OSS Middle East parachute unit. Because the underlying document could not be
directly inspected during this session, the lead remains qualified and is not
published as a claim. Arthur R Piantadosi's later film-industry biography is
similarly retained only as a research lead: accessible discovery sources did
not establish his immediate pre-OSS employer to the project's publication
standard.

The remaining common-name, incomplete-name, foreign-note, and civilian-grade
cases remain unresolved or ambiguous. Wallace B Phillips's printed "Polish
Ar" note and Wayman F Phillips's "Also 348" cross-reference remain literal
and require Box 603 examination. No new pre-OSS employer is published for this
cohort.

The reviewed evidence bundle imports four sources, 11 claims, 28 evidence
links, 23 person updates, and 23 completed research attempts. Nine identity
decisions are accepted. The final cohort identity statuses are nine
high-confidence, one probable, eight ambiguous, and five unresolved. Research
statuses are eight `needs_identity_review` and 15
`requires_archival_review`.

The CIA cohort adapter could not proceed because its robots policy was
unavailable, and the Library of Congress cohort check was blocked. These are
recorded as source-access limits rather than negative evidence. No
authenticated NARA Catalog API request was made, and no API key or raw API
response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,394 (43.4187%) |
| People with confirmed/high employer evidence | 344 (1.4370%) |
| People with confirmed/high affiliation evidence | 774 (3.2332%) |
| Archival-review dispositions assessed | 8,853 (36.9815%) |
| Not started | 13,540 |
| Possible duplicate groups | 533 |
| Conflicts | 350 |
| Claims by confidence | confirmed 1,397; high 3,151; medium 1,561; low 198; conflicting 305; unresolved 2 |
| Citation records / unique source documents | 5,834 / 2,979 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 294; documented_prewar_employer_found 175;
in_progress 1,902; needs_identity_review 505; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,540;
occupation_only_found 1,050; requires_archival_review 4,469; and
verified_employer_found 296.

The public projection contains 23,939 person entities, 2,537 published
affiliations, 889 organizations, 4,610 public sources, and 6,407 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 389 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,867 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 755, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,867 HTML files checked; every internal link resolved and
  50,835 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,868,753 bytes verified; manifest SHA-256
  `4e23602a27cc9ad7b0b567a3ca77da774484d266e5eff991fadc7803c2c69445`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,939 public artifacts, and 1,230 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,939-file,
  311,040,683-byte output tree at SHA-256
  `b05f25e8eccc5b96e83da5b7c1194a9cde0e52f0179f44c1c063a3a02594102d`.

## Publication verification

Release commit `f0ec9da9388342affbdb3227562c07baad86fd12` was pushed to
`main`. The exact commit passed the [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38323492444)
and [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38323492423).

At `2026-10-12T23:47:28Z`, the immutable release verifier compared the
[public site](https://therealjameswilson.github.io/before-oss/) with that
commit and verified all 67 manifest assets / 107,868,753 bytes, the eight core
routes, all 31 source-register pages, and all 23 Batch 755 profiles. The
deployed manifest SHA-256 was
`4e23602a27cc9ad7b0b567a3ca77da774484d266e5eff991fadc7803c2c69445`.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-755-phillips-piantadosi --page 368 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch755.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page368-phillips-piantadosi-review_batch-755_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 368, row 24, Austin T Piazza. No API
key, raw API response, full service or officer number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published.
