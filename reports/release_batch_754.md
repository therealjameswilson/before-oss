# Batch 754 release - Phelan-Phillips research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 754 publishes reviewed outcomes for PDF page 367, rows 24-46, from
Agnes G Phelan through John S Phillips. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes,
notes, locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The 23 source rows remain linked to 23 separate person entities. Jacques L
Philippot's protected identifier agrees with an official Army bulk record that
names a different person. The entities remain separate, the discrepancy is
published as an identity conflict, and Box 602 review remains the next action.
The common-name cases remain unresolved or ambiguous unless the accessible
evidence provides corroborating identifiers.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Alexander P Phillips, Earl L Phillips, Frederick L Phillips,
John M Phillips, Karl Philippi, and Stephanos J Philippides. Those matches
establish identity only; no coded Army occupation is converted into an
employer or role.

Reginald H Phelps is linked at high confidence through a Harvard Gazette
institutional biography. Harvard is published as his strongly date-bounded
immediate pre-OSS affiliation and last civilian employer: the source documents
his German teaching there from 1931 through 1944 and states that he and Julia
joined the OSS in September 1944. Julia G Phelps is separately linked at high
confidence as Julia Gray Sears Phelps. Her Radcliffe undergraduate status is
published as a medium-confidence, documented-prewar student affiliation, not
as employment and not as her immediate pre-OSS affiliation.

Elizabeth Q Phenix remains a probable match to memoirist Elizabeth Phenix
Wiesner. An institutional bibliography and scholarly thesis establish the
wartime Red Cross and OSS context but do not independently confirm the middle
initial or a qualifying pre-OSS employer. Albert J Phiebig is linked at high
confidence through a scholarly article that identifies him as Franz L.
Neumann's OSS colleague in the same division; discovery-only prewar-employment
leads are excluded. Operational-group roster entries for Alexander P Phillips
and Stephanos J Philippides are retained only as secondary corroboration, not
as employer evidence.

The reviewed evidence bundle imports seven sources, two organizations, two
affiliations, 13 claims, 27 evidence links, 23 person updates, and 23 completed
research attempts. Seven identity decisions are recorded: six accepted and
one conflicting. The final cohort identity statuses are nine high-confidence,
one probable, one ambiguous, one conflicting, and 11 unresolved. Research
statuses are one `verified_employer_found`, two `needs_identity_review`, and
20 `requires_archival_review`.

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
| People with nonplanned research attempts | 10,371 (43.3226%) |
| People with confirmed/high employer evidence | 344 (1.4370%) |
| People with confirmed/high affiliation evidence | 774 (3.2332%) |
| Archival-review dispositions assessed | 8,830 (36.8854%) |
| Not started | 13,563 |
| Possible duplicate groups | 533 |
| Conflicts | 350 |
| Claims by confidence | confirmed 1,397; high 3,140; medium 1,561; low 198; conflicting 305; unresolved 2 |
| Citation records / unique source documents | 5,830 / 2,977 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 294; documented_prewar_employer_found 175;
in_progress 1,902; needs_identity_review 497; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,563;
occupation_only_found 1,050; requires_archival_review 4,454; and
verified_employer_found 296.

The public projection contains 23,939 person entities, 2,537 published
affiliations, 889 organizations, 4,606 public sources, and 6,396 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 388 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,867 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 754, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,867 HTML files checked; every internal link resolved and
  50,834 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,814,612 bytes verified; manifest SHA-256
  `aed9cf64ae0d96ae46364b3a4a28e1e7011995bdf2a08ac37b36eda7f1f4822d`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,939 public artifacts, and 1,230 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,939-file,
  310,955,684-byte output tree at SHA-256
  `1de63d125240b59926a2599550a7b702b6037210e94d9524e6ae08bbda0cc41a`.

## Publication verification

Release commit
`841573f5028d317e645ed51d96eb9144ffafa3f7` was pushed to `main`. The exact
commit passed the [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38321215852)
and the [Deploy GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38321215892).

At `2026-10-12T23:20:58Z`, the immutable release verifier compared the live
site with that commit and verified all 67 manifest assets / 107,814,612 bytes,
the eight core routes, all 31 source-register pages, and all 23 Batch 754
profiles. The deployed manifest SHA-256 was
`aed9cf64ae0d96ae46364b3a4a28e1e7011995bdf2a08ac37b36eda7f1f4822d`.
The published site is <https://therealjameswilson.github.io/before-oss/>.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-754-phelan-phillips --page 367 --first-row 24 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch754.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page367-phelan-phillips-review_batch-754_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 368, row 1, Kenneth H Phillips. No API
key, raw API response, full service or officer number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published.
