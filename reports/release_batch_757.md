# Batch 757 release - Piday-Pikanski research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 757 publishes reviewed outcomes for PDF page 369, rows 2-28, from
George L Piday through Edward J Pikanski. All 27 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes,
notes, locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The 27 source rows remain linked to 27 separate person entities. Edward J
Piekanski and Edward J Pikanski have the same printed protected identifier and
rank but different spellings and boxes. They remain separate, conflicting
profiles pending archival review rather than being silently merged. The two
adjacent William H Pietsch rows also remain separate probable duplicate
profiles because one row has a blank identifier and the other has an officer
identifier. George W Pierce's damaged scientific-notation identifier and Guy R
Pierce's truncated `Folder al` note are preserved literally rather than
reconstructed.

Eight exact-name or independently corroborated, nonshared protected-identifier
matches in official Army bulk data establish high-confidence identity for
Donald S Pierce, Hubert B Pierce, Roger L Pierre, Spiros D Pieratos, Glen
Pierson, Robert C Pierson, Emmanuel Pietromartire, and Bernard M Pietrowiak.
Those matches establish identity only; no coded Army occupation is converted
into an employer or role.

A visually inspected institutional military history identifies Kenneth M Pier
as a U.S. Naval Reserve officer assigned to the Navy's Field Photographic
Office before he became commander of the OSS Maritime Unit on the Arakan coast
in July 1944. The Field Photographic Office is therefore published at high
confidence as his strongly date-bounded immediate pre-OSS military assignment,
not as a civilian employer.

A separate obituary says Robert C Pierson Jr attended West Virginia University
until called to Army active duty and that the Army assigned him to the OSS. The
Army is published at high confidence as his explicit immediate pre-OSS military
assignment. West Virginia University is published as an earlier student
affiliation, never as an employer. No named civilian employer was established
for either Pier or Pierson.

The CIA Museum's William H Pietsch Jr artifact is retained only as a qualified,
medium-confidence identity lead on both Pietsch profiles. The duplicate rows
and lack of a row-specific identifier bridge prevent a settled identity or an
affiliation claim. Search leads that did not bridge the remaining common or
incomplete names to the indexed people are not published as facts.

The reviewed evidence bundle imports five sources, three organizations, three
affiliations, 14 claims, 26 evidence links, 27 person updates, and 27 completed
research attempts. Twelve row-specific identity decisions were imported. The
final cohort identity statuses are nine high-confidence, three probable, one
conflicting, eight ambiguous, and six unresolved. Research statuses are two
`completed`, 13 `requires_archival_review`, ten `needs_identity_review`, and
two `conflicting_sources`.

The CIA cohort adapter stopped because the requested path was disallowed by
the retrieved robots policy, and the Library of Congress cohort check stopped
on HTTP 503 after bounded retries. These are recorded as source-access limits
rather than negative evidence. No authenticated NARA Catalog API request was
made, and no API key or raw API response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,444 (43.6276%) |
| People with confirmed/high employer evidence | 345 (1.4412%) |
| People with confirmed/high affiliation evidence | 777 (3.2457%) |
| Archival-review dispositions assessed | 8,903 (37.1904%) |
| Not started | 13,490 |
| Possible duplicate groups | 534 |
| Conflicts | 352 |
| Claims by confidence | confirmed 1,397; high 3,173; medium 1,563; low 198; conflicting 305; unresolved 2 |
| Citation records / unique source documents | 5,843 / 2,986 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 196; conflicting_sources 296; documented_prewar_employer_found 175;
in_progress 1,902; needs_identity_review 526; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,490;
occupation_only_found 1,050; requires_archival_review 4,493; and
verified_employer_found 297.

The public projection contains 23,939 person entities, 2,541 published
affiliations, 891 organizations, 4,619 public sources, and 6,431 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 391 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,869 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 757, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,869 HTML files checked; every internal link resolved and
  50,842 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 108,007,641 bytes verified; manifest SHA-256
  `c49bfce8218ee0d45ba5996e6b98b729a885193d567e261434155afb165966cc`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,941 public artifacts, and 1,237 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,941-file,
  311,263,397-byte output tree at SHA-256
  `335852a262855c76b00e98eb6dcabc9be3b6a711b8dc78649e4c222748d27ceb`.

## Publication verification

Release commit `a93851ac0fbd0bea6681d4a47bf83304b9a73dd5` was pushed to
`main`. The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38329838104)
completed successfully at `2026-10-13T01:01:30Z`, and the
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38329838108)
completed successfully at `2026-10-13T01:00:06Z`.

An unauthenticated immutable verification at `2026-10-13T01:01:53Z` confirmed
the deployed commit and 67 public assets totaling 108,007,641 bytes, with
manifest SHA-256
`c49bfce8218ee0d45ba5996e6b98b729a885193d567e261434155afb165966cc`.
The verifier also checked eight core routes, all 31 source-register pages, and
all 27 direct Batch 757 profile routes at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-757-piday-pikanski --page 369 --first-row 2 --last-row 28
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch757.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page369-piday-pikanski-review_batch-757_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next unresearched person boundary is PDF page 369, row 29, Bertrand F
Pike. No API key, raw API response, full service or officer number,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or
published.
