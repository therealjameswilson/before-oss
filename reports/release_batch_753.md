# Batch 753 release - Petty-Phaneuf research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 753 publishes reviewed outcomes for PDF page 367, rows 1-23, from
Virgil O Petty through Joseph A Phaneuf. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes,
notes, locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The 23 source rows remain linked to 23 separate person entities. Lon Peyton
shares a protected identifier with a separate indexed person under a different
name; both entities remain visibly conflicting and unmerged. Harold M or
Pfeifer's protected identifier agrees with the official Army dataset, but the
Army middle initial conflicts with the index's literal `M or` field. The index
wording is preserved without silent correction. Ralph A Pezzulo remains
ambiguous because accessible sources support two same-name veteran candidates.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Benjamin K Pfeiffer, Jacob Pfanz, James F Pfister, John B
Pfaifer, John M Pfenninger, Robert R Pfeiffer, and Walter C Pfleeger. Those
matches establish identity only; no coded Army occupation is converted into
an employer or role.

Eveline Peyronel is linked at high confidence through French Defense Historical
Service file GR 16 P 473346 and an institutional local-history biography. Home
Catalan is published as a medium-confidence, documented prewar employer, with
her English-teacher role and 1941-1943 date range. It is not labeled the
immediate pre-OSS affiliation.

Otto Pfister is linked at high confidence through the German Resistance
Memorial Center. His active support for the Internationaler Sozialistischer
Kampfbund is published as a volunteer or professional affiliation, not as
employment. Irving P Pflaum is linked only at probable confidence: a 1939
first-person article documents his United Press correspondent role in Spain
through summer 1938, but no accessible source directly bridges that writer to
the personnel file. The employment is therefore published as qualified,
documented prewar work rather than the immediate or last civilian employer.

Robert P Pflieger is confirmed through an exact distinctive name and
lieutenant-colonel rank in a visually verified 1944 official memorandum. A
1934 reported court opinion separately identifies him as a partner trading as
Paul Pflieger and Company. That role is published as high-confidence earlier
self-employment, not as the final civilian employer or immediate affiliation.

Joseph A Phaneuf remains probable because an operational-group roster supports
the name and wartime context but supplies no second independent identifier.
Roger A Pfaff's institutional PDF returned an empty response, so neither the
search snippet nor an inaccessible document is used as final evidence.

The reviewed evidence bundle imports eight sources, four organizations, four
affiliations, 17 claims, 33 claim-source links, 23 person updates, and 23
completed research attempts. Nine identity decisions are recorded: seven
accepted and two conflicting. The final cohort identity statuses are one
confirmed, nine high-confidence, two probable, one ambiguous, two conflicting,
and eight unresolved. Research statuses are three
`documented_prewar_employer_found`, three `needs_identity_review`, and 17
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
| People with nonplanned research attempts | 10,348 (43.2265%) |
| People with confirmed/high employer evidence | 343 (1.4328%) |
| People with confirmed/high affiliation evidence | 773 (3.2290%) |
| Archival-review dispositions assessed | 8,807 (36.7893%) |
| Not started | 13,586 |
| Possible duplicate groups | 533 |
| Conflicts | 349 |
| Claims by confidence | confirmed 1,397; high 3,130; medium 1,559; low 198; conflicting 304; unresolved 2 |
| Citation records / unique source documents | 5,823 / 2,972 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 294; documented_prewar_employer_found 175;
in_progress 1,902; needs_identity_review 495; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,586;
occupation_only_found 1,050; requires_archival_review 4,434; and
verified_employer_found 295.

The public projection contains 23,939 person entities, 2,535 published
affiliations, 889 organizations, 4,599 public sources, and 6,383 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 387 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,867 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 753, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,867 HTML files checked; every internal link resolved and
  50,830 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,737,558 bytes verified; manifest SHA-256
  `735be5ee947862215c7493b4f5f0bfa5ab0067fc23a7107d9af3c244d7f5ce9c`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,939 public artifacts, and 1,232 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,939-file,
  310,838,185-byte output tree at SHA-256
  `7f921fc68f6689583599d9e2aa80f470beb022049fb4b46d7474620f070a8a02`.

## Publication verification

Publication is pending the release commit, GitHub Actions checks, GitHub Pages
deployment, and immutable live-site verification. This section will be updated
with exact commit and workflow links after those checks complete.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-753-petty-phaneuf --page 367 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch753.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page367-petty-phaneuf-review_batch-753_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 367, row 24, Agnes G Phelan. No API
key, raw API response, full service or officer number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published.
