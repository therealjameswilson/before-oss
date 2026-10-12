# Batch 751 release - Peterson-Petroff research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 751 publishes reviewed outcomes for PDF page 366, rows 1-23, from
Josephine S Peterson through Boris B Petroff. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes, notes,
locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The 23 source rows remain linked to 23 separate person entities. Melvin
Petievich shares a protected identifier with the separate Melvin Corvin row on
page 94, and Robert L Petitt shares an identifier with the separate Robert L
Pettit row on page 366. Both pairs remain visibly conflicting and unmerged.
The printed `Extract fr` note for Ross L Pethtel and the CAF-5 and CAF-6 grades
for Vivian A Peterson and Ross T Peterson are preserved without silent
expansion or reinterpretation.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Kenneth N Peterson, Marvin K Peterson, Norman E Peterson,
William G Peterson, Ross L Pethtel, Joseph E Petitpas, Angelo S Petraglia, and
Edward A Petro. Those matches establish identity only; no coded Army
occupation is converted into an employer or role.

Nicholas C Petris is linked at high confidence to Nicholas Christos Petris
through the distinctive full name, matching wartime chronology, a California
State Archives finding aid, and an obituary explicitly documenting OSS
service. His 1943 UC Berkeley journalism degree is published as student status,
not employment, and is not labeled the immediate pre-OSS affiliation.

Peter P Petkoff is linked at high confidence to Peter Pavloff Petkoff through
the distinctive name, a 1942 University of Michigan engineering degree,
documented Army enlistment, a professional obituary describing OSS service,
and an official CMS transcript introducing him as an original OSS member. The
University of Michigan is likewise published only as student status. His
postwar engineering firm is excluded from the pre-OSS chronology.

A 1948 Theta Tau alumni publication describes Boris B. Petroff's five years as
assistant manager of Traffic Survey for the North Carolina State Highway
Commission before Army service in 1942-1943. The distinctive name and wartime
chronology support a probable identity, but the publication does not directly
bridge the biography to OSS. The commission is therefore published only as a
medium-confidence, qualified last civilian employer and remains excluded from
default high-confidence analytics pending Box 600 review.

The reviewed evidence bundle imports eight sources, three organizations, three
affiliations, 16 claims, 33 claim-source links, 25 person updates, and 23
completed research attempts. Twelve identity decisions are recorded: eight
accepted and four conflicting. The final cohort identity statuses are ten
high-confidence, one probable, one ambiguous, two conflicting, and nine
unresolved. Research statuses are four `needs_identity_review` and 19
`requires_archival_review`.

The CIA cohort adapter failed before a person query because its robots policy
could not be retrieved, and the Library of Congress cohort run ended on a
source error. These are recorded as source-access limits rather than negative
evidence. The UC Berkeley oral-history PDF returned an access challenge and
was not bypassed. No authenticated NARA Catalog API request was made, and no
API key or raw API response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,302 (43.0344%) |
| People with confirmed/high employer evidence | 340 (1.4203%) |
| People with confirmed/high affiliation evidence | 766 (3.1998%) |
| Archival-review dispositions assessed | 8,761 (36.5972%) |
| Not started | 13,632 |
| Possible duplicate groups | 531 |
| Conflicts | 346 |
| Claims by confidence | confirmed 1,392; high 3,104; medium 1,556; low 198; conflicting 301; unresolved 2 |
| Citation records / unique source documents | 5,803 / 2,955 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 294; documented_prewar_employer_found 171;
in_progress 1,902; needs_identity_review 491; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,632;
occupation_only_found 1,050; requires_archival_review 4,397; and
verified_employer_found 294.

The public projection contains 23,939 person entities, 2,524 published
affiliations, 882 organizations, 4,579 public sources, and 6,346 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 385 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,860 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 751, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,860 HTML files checked; every internal link resolved and
  50,809 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,500,357 bytes verified; manifest SHA-256
  `8c999fe9224ce70645f0f9bf826fc926862405a8595f485c0bfbedf2fda5c19b`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,932 public artifacts, and 1,239 candidate substrings checked;
  zero aggregate false positives or unexpected boundary matches. Two numeric
  manifest-size coincidences were recognized and excluded by the audit.
* Two consecutive production builds reproduced the 24,932-file,
  310,450,942-byte output tree at SHA-256
  `8657d5c9422f3209313e2640c610d7767697be7a00f28bc2da1b14baf660b179`.

## Publication verification

Publication is pending the release commit, GitHub Actions checks, GitHub Pages
deployment, and immutable live-site verification. This section will be updated
with exact commit and workflow links after those checks complete.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-751-peterson-petroff --page 366 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch751.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page366-peterson-petroff-review_batch-751_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 366, row 24, Gerard Petron. No API key,
raw API response, full service or officer number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published.
