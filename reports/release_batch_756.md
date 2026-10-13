# Batch 756 release - Piazza-Pickus research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 756 publishes reviewed outcomes for PDF page 368, rows 24-46, from
Austin T Piazza through Sidney R Pickus. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes,
notes, locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The 23 source rows remain linked to 23 person entities. Sidney R Pickus is
printed again on page 369, row 1; both immutable source rows remain visible and
are linked to one high-confidence person entity. Nine row-specific exact-name,
nonshared protected-identifier matches in official Army bulk data are accepted
for eight people: Austin T Piazza, Joel J Picard, George Piccardi, Edward
Pichette, Germain V Pichon, Steve Picinich, Arthur A Pickett, and Sidney R
Pickus. The two Pickus decisions correspond to the two preserved source rows.
Those matches establish identity only; no coded Army occupation is converted
into an employer or role.

Germain V Pichon's separate identifier-collision candidate points to a
differently named Army record and is explicitly rejected. The exact-name
candidate is accepted. This disagreement remains in the private review trail
rather than being silently discarded.

A visually inspected contemporary trade-journal item identifies Lawrence
Pickard as an 82d Airborne Division officer and says that, before entering the
Army, he was with the Yonkers Herald-Statesman. A separate obituary agrees on
Yonkers and 82nd Airborne details. Together with the indexed officer rank,
these provide the two corroborating identifiers required for the common-name
case. The Herald-Statesman is therefore published at high confidence as
Pickard's last documented civilian employer before Army service. It is not
presented as his immediate pre-OSS affiliation, which remains unresolved.

Search leads for Steve Picinich, Lydia I Pickup, and Germain V Pichon did not
meet the publication threshold for new employment claims. The Picinich roster
has a rank discrepancy and no employment evidence; the Pickup scholarship
does not bridge the namesake to the index row; and the Pichon genealogy lead
is not adequate final evidence. No sensitive people-finder data were retained.

The remaining common-name, incomplete-name, foreign-note, cross-reference, and
civilian-grade cases remain unresolved or ambiguous. Santo Piazza's printed
"French" note, Edward Pichette's "Also Fra," Adrian Pickering's "Also 313,"
and India Pickett's "Also 601" remain literal pending archival review.

The reviewed evidence bundle imports four sources, one organization, one
affiliation, ten claims, 21 evidence links, 23 person updates, and 23 completed
research attempts. Nine row-specific Army identity decisions are accepted and
one conflicting-name candidate is rejected. The final cohort identity statuses
are nine high-confidence, 11 ambiguous, and three unresolved. Research
statuses are 11 `needs_identity_review`, 11 `requires_archival_review`, and one
`verified_employer_found`.

The CIA cohort adapter stopped because the requested path was disallowed by
the retrieved robots policy, and the Library of Congress cohort check stopped
on HTTP 503. These are recorded as source-access limits rather than negative
evidence. No authenticated NARA Catalog API request was made, and no API key
or raw API response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,417 (43.5148%) |
| People with confirmed/high employer evidence | 345 (1.4412%) |
| People with confirmed/high affiliation evidence | 775 (3.2374%) |
| Archival-review dispositions assessed | 8,876 (37.0776%) |
| Not started | 13,517 |
| Possible duplicate groups | 533 |
| Conflicts | 350 |
| Claims by confidence | confirmed 1,397; high 3,161; medium 1,561; low 198; conflicting 305; unresolved 2 |
| Citation records / unique source documents | 5,838 / 2,982 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 294; documented_prewar_employer_found 175;
in_progress 1,902; needs_identity_review 516; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,517;
occupation_only_found 1,050; requires_archival_review 4,480; and
verified_employer_found 297.

The public projection contains 23,939 person entities, 2,538 published
affiliations, 890 organizations, 4,614 public sources, and 6,417 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 390 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,868 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 756, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,868 HTML files checked; every internal link resolved and
  50,838 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,927,675 bytes verified; manifest SHA-256
  `6b16afae11bc9db8505d18af81bebef60e7ac52df137b55b2126372199f9b352`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,940 public artifacts, and 1,235 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,940-file,
  311,135,365-byte output tree at SHA-256
  `3152c7ef52000837c9331758f4cef2d7502d3d2b6f1cae5de7756065f43b0c35`.

## Publication verification

Publication receipt pending commit, GitHub Actions, and immutable live-site
verification.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-756-piazza-pickus --page 368 --first-row 24 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch756.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page368-piazza-pickus-review_batch-756_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

Page 369, row 1 is the repeated Sidney R Pickus row already researched in this
batch. The next unresearched person boundary is PDF page 369, row 2, George L
Piday. No API key, raw API response, full service or officer number,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or
published.
