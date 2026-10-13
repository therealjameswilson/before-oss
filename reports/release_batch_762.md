# Batch 762 release - Pizutto-Platt research

Research and local release verification date: 2026-10-13
America/New_York.

## Historical work

Batch 762 publishes reviewed outcomes for PDF page 371, rows 1-18, from
Vincent Pizutto through Robert S Platt. All 18 printed rows were visually
checked against a 300-dpi page render. This review corrected the inherited
Batch 761 boundary note: printed page 371 begins with Vincent Pizutto, not
Olga Pizzorno. Original spellings, ranks, boxes, notes, locations, and
protected identifiers remain recoverable in the private database. Full
protected identifiers remain private.

The 18 source rows remain linked to 18 separate person entities. Seven
row-specific official Army candidates were reviewed. Exact or core-name,
nonshared-identifier matches for Alexander J Pizzi, John Pizzoferrato, Alfred
D Plamondon, Gerard A Plante, and Frank P Platnick were accepted as identity
evidence only. Alfred Plamondon's trailing bulk-name anomaly remains visible
and is not silently adopted as a suffix. William G Plaetti retains two
explicitly conflicting candidate decisions because his protected identifier
is shared by a separate William G Paletti index row and the Army record uses
the Paletti spelling. No Army occupation, employer, or other metadata is
transferred into the conflicting profile.

Historian Katharine Gerbner's report of direct OSS personnel-file inspection
supports a probable identification of Rade Plan with the alias Robert Perry.
It also supports one qualified, medium-confidence documented-prewar military
affiliation with the Yugoslav Battalion at Haifa. The article separately
calls Plan a Yugoslav civilian, so the site does not infer commissioned or
enlisted status, ethnicity, an exact battalion role, or a civilian employer.
The underlying personnel file remains a high-priority archival review.

A 31 May 1944 official OSS memorandum from Gardiner S. Platt was downloaded,
text-searched, and visually inspected at 300 dpi. The exact rare name and OSS
context establish Gardiner at high identity confidence. The memorandum is
used for identity only and is not converted into a pre-OSS employer,
affiliation, or operational-role claim.

Robert S Platt remains unresolved. University of Chicago, Library of Congress,
and Yale sources document the wartime career and University of Chicago
employment of geographer Robert Swanton Platt, but no direct OSS or personnel
file bridge connects that biography to this index row. The tempting
same-name match is therefore withheld rather than published as fact.

Seventeen people have requires_archival_review, while William Plaetti has
conflicting_sources. No named employer was added. The oil-company category
remains evidence-scoped to nine people across 11 historically named
companies.

The reviewed evidence bundle imports four source records, one organization,
one affiliation, nine claims, 17 evidence links, 18 person updates, and 18
completed manual staged research protocols. The CIA cohort adapter stopped
because its robots policy could not be retrieved, and the Library of Congress
cohort check stopped on a transport error. These are recorded as
source-access failures rather than negative evidence. No authenticated NARA
Catalog API request was made, and no API key or raw API response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,526 (43.9701%) |
| People with confirmed/high employer evidence | 345 (1.4412%) |
| People with confirmed/high affiliation evidence | 781 (3.2625%) |
| Archival-review dispositions assessed | 8,984 (37.5287%) |
| Not started | 13,408 |
| Possible duplicate groups | 536 |
| Conflicts | 355 |
| Claims by confidence | confirmed 1,400; high 3,209; medium 1,577; low 198; conflicting 308; unresolved 2 |
| Citation records / unique source documents | 5,877 / 3,014 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 198; conflicting_sources 299; documented_prewar_employer_found 175;
in_progress 1,902; needs_identity_review 535; needs_temporal_review 25;
no_reliable_result_after_protocol 1,156; not_started 13,408;
occupation_only_found 1,053; requires_archival_review 4,557; and
verified_employer_found 297.

The private database contains 2,577 affiliations, 912 organizations, 19,372
research attempts or plans, and 5,877 citation records. The public projection
contains 23,939 person entities, 2,554 published affiliations, 896
organizations, 4,653 public sources, and 6,487 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 tests plus 78 subtests passed.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 396 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,875 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 762, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,875 HTML files checked; every internal link resolved and
  50,867 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 108,352,030 bytes verified; manifest SHA-256
  93279fcc42b0d29a38cdd630c038ba58c7262b33908e587ef4f6d545807213b4.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,947 public artifacts, and 1,245 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,947-file,
  311,814,113-byte output tree at SHA-256
  a1b9c1ffeb57e7fb99756710a86c43f35ed93a0dbd9af9c2fedc6fdf2b1a2a23.

## Publication verification

Publication status: pending commit, push, GitHub Pages deployment, and
unauthenticated live verification.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-762-pizutto-platt --page 371 --first-row 1 --last-row 18
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch762.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page371-pizutto-platt-review_batch-762_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next unresearched person boundary is PDF page 371, row 19, Karl J Platz.
No API key, raw API response, full service or officer number, copyrighted page
image, unrelated Army coded occupation, street address, modern people-finder
record, or private reviewer note is committed or published.
