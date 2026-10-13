# Batch 764 release - Poehl-Pollack research

Research and local release verification date: 2026-10-13
America/New_York.

## Historical work

Batch 764 publishes reviewed outcomes for PDF page 372, rows 1-28, from
Theadfield L Poehl through Robert E Pollack. All 28 printed rows were visually
checked against a 300-dpi page render and remain separately preserved. The
page image confirms the indexed spelling Julian Pokrwyka; Pokrywka is retained
only as a search alias. Full protected identifiers remain private.

Fourteen exact or core-name official Army matches establish identity only for
Theadfield L Poehl, Danny A Poggioli, Stanley M Pogwist, George W Pohle,
Cornelius Poillon, Maurice C Poissant, John J Poklar, Andrew B Polansky,
Raymond F Polczak, Demetrios J Polemis, Leonid Polevoy, Mitchell A Polkowski,
David Pollack, and Robert E Pollack. Cornelius Poillon's unexplained trailing
Army token is excluded. The Army omission of Demetrios Polemis's index middle
initial and the Army-added S for Leonid Polevoy remain documented source
discrepancies. No Army occupation, grade code, raw record, or protected
identifier is published or converted into an employer.

An official CIA history establishes Thomas Polgar at high identity confidence
as a former OSS officer. A reputable obituary explicitly sequences his Army
service before OSS recruitment. The site therefore publishes the U.S. Army as
a qualified, medium-confidence immediate pre-OSS military assignment, never
as civilian employment. Exact transfer dates and Polgar's last civilian
employer remain unresolved.

The Jessie J Poesch art historian and the later Admiral John D Poindexter are
withheld as unbridged or age-incompatible namesakes. Searches for the other
unresolved people likewise produced no evidence strong enough to assign a
biography or employer. Every Batch 764 person remains routed to archival
review. The oil-company category remains evidence-scoped to nine people across
11 historically named companies.

The reviewed evidence bundle imports four source records, one organization,
one affiliation, 16 claims, 32 claim-source links, 28 person updates, and 28
completed manual staged research protocols. Fourteen candidate decisions were
reviewed and accepted for identity only. The CIA cohort adapter stopped
because its robots policy could not be retrieved, and the Library of Congress
cohort check stopped on a transport error. These are recorded as source-access
failures rather than negative evidence. No authenticated NARA Catalog API
request was made, and no API key or raw API response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,581 (44.1998%) |
| People with confirmed/high employer evidence | 347 (1.4495%) |
| People with confirmed/high affiliation evidence | 783 (3.2708%) |
| Archival-review dispositions assessed | 9,039 (37.7585%) |
| Not started | 13,353 |
| Possible duplicate groups | 536 |
| Conflicts | 359 |
| Claims by confidence | confirmed 1,402; high 3,235; medium 1,578; low 198; conflicting 312; unresolved 2 |
| Citation records / unique source documents | 5,887 / 3,022 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 198; conflicting_sources 303; documented_prewar_employer_found 175;
in_progress 1,902; needs_identity_review 535; needs_temporal_review 25;
no_reliable_result_after_protocol 1,156; not_started 13,353;
occupation_only_found 1,053; requires_archival_review 4,606; and
verified_employer_found 299.

The private database contains 2,581 affiliations, 916 organizations, 19,431
research attempts or plans, and 5,887 citation records. The public projection
contains 23,939 person entities, 2,558 published affiliations, 900
organizations, 4,663 public sources, and 6,520 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 tests plus 78 subtests passed.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 398 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,879 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 764, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,879 HTML files checked; every internal link resolved and
  50,876 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 108,506,766 bytes verified; manifest SHA-256
  `f3f81da1777a75e87cd9b08b4ab6067d84d24f494e9195689bfb9fd364babc17`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,951 public artifacts, and 1,249 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,951-file,
  312,078,673-byte output tree at SHA-256
  `d93cb894333548af7083d8eb5f92d3e857a454739d63f4432fb95b856e3e7f53`.

## Publication status

Publication is pending the GitHub Pages and Test workflows and immutable live
verification of the exact release commit.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-764-poehl-pollack --page 372 --first-row 1 --last-row 28
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-13_batch764.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page372-poehl-pollack-review_batch-764_2026-10-13.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next unresearched person boundary is PDF page 372, row 29, Rose S
Pollack. No API key, raw API response, full service or officer number,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or
published.
