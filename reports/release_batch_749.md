# Batch 749 release - Persons-Peters research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 749 publishes reviewed outcomes for PDF page 365, rows 1-23, from
Edmund Persons through John Peters. All 23 printed rows were visually checked
against a 300-dpi page render. Original spellings, ranks, boxes, notes,
locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The 23 source rows represent 22 person entities because the two printed Fred W
Peters rows share the same protected identifier. Both rows remain separately
visible, including their different Boxes 598 and 599 and the printed `CSP(X)`
rank. The unusual `H` / `Frede` name-field split, Claude Perthius's `S/Lt` and
`French` annotations, Lillian Perugia's `Also 013` note, and Herman Perveslin's
truncated `Extract fr` note are preserved without silent expansion.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Edmund Persons, Sam Perusso, Victor C Petchul, George
Petemezas, David L Peters, Emerson E Peters, and Harry L Peters. Those matches
establish identity only; no coded Army occupation is converted into an
employer or occupation claim. Cyril J Perusek remains a probable identity
match because the official Army name reads Cyril J Penusek. The spelling is
retained as a variant, not a correction.

The Albert Perz row is the second side of the Albert Perez / Albert Perz
shared-identifier conflict first identified in Batch 746. The separate Box 595
and Box 598 people remain unmerged and now share the same neutral duplicate
review group. The Army candidate is not accepted for either spelling without
personnel-file comparison.

Two qualified affiliation outcomes are published. Contemporary newspaper and
school-yearbook evidence identifies Victor Petchul as a 1941 senior at Tilden
Technical High School. This is published as student status, never as
employment and not as the immediate pre-OSS affiliation. Official Army data
and a contemporary TIME account support the U.S. Army as George Petemezas's
probable immediate military pathway to OSS service in Yugoslavia. The account
does not supply a unit-level transfer date, so the claim remains medium
confidence and outside confirmed/high default analytics.

A 1943 306th Bomb Group officer roster agrees with the distinctive name,
officer context, and protected identifier for Captain Carl S Perutz and lists
an Ordnance assignment. It is published only as qualified identity context;
the assignment is not labeled pre-OSS because the transition chronology is
unknown. Postwar references for Herman Perveslin and Horace W Peters are
recorded as rejected or insufficient identity leads and do not become pre-OSS
claims.

Exact-name OSS, employment/occupation, obituary, institutional, directory,
newspaper, military, and archival searches were reviewed for all 22 people.
The reviewed evidence bundle imports six sources, two organizations, two
affiliations, ten claims, 21 claim-source links, 22 person updates, and 22
completed research attempts. Ten identity decisions are recorded: seven
accepted, one probable, and two conflicting. The CIA cohort adapter failed
before a person query and the Library of Congress cohort run ended on a source
error; these are recorded as source-access limits rather than negative
evidence. No authenticated NARA Catalog API request was made.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,256 (42.8422%) |
| People with confirmed/high employer evidence | 340 (1.4203%) |
| People with confirmed/high affiliation evidence | 764 (3.1914%) |
| Archival-review dispositions assessed | 8,715 (36.4050%) |
| Not started | 13,678 |
| Possible duplicate groups | 530 |
| Conflicts | 342 |
| Claims by confidence | confirmed 1,392; high 3,088; medium 1,554; low 198; conflicting 299; unresolved 2 |
| Citation records / unique source documents | 5,793 / 2,948 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 294;
documented_prewar_employer_found 171; in_progress 1,902;
needs_identity_review 483; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,678;
occupation_only_found 1,050; requires_archival_review 4,359; and
verified_employer_found 294.

The public projection contains 23,939 person entities, 2,521 published
affiliations, 881 organizations, 4,569 public sources, and 6,326 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 383 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,859 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 749, 33 core, six analytics, and 30 accessibility
  checks. One earlier run was interrupted by a roughly 15-minute machine pause;
  the clean rerun passed in full.
* Link check: 24,859 HTML files checked; every internal link resolved and
  50,802 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,383,422 bytes verified; manifest SHA-256
  `d47e8ea92933a0294c4a2e538825a5d566d7cfa9d958116b3f8cecb51571f6c2`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,931 public artifacts, and 1,233 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,931-file,
  310,267,342-byte output tree at SHA-256
  `f6a6e5b185083c4ad58fe46f8c0f9a3467cc67741a61bd769eaa64047af55e12`.

## Publication verification

Release commit
[`dee663fdc82b42f65e4508697a84fae35da374e3`](https://github.com/therealjameswilson/before-oss/commit/dee663fdc82b42f65e4508697a84fae35da374e3)
was pushed to `main` on 2026-10-12. The independent
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38252634502)
and
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38252634055)
both completed successfully.

The immutable deployed-release verifier checked the public site against that
commit: 67 assets and 107,383,422 bytes matched manifest SHA-256
`d47e8ea92933a0294c4a2e538825a5d566d7cfa9d958116b3f8cecb51571f6c2`.
It also verified eight core routes, 31 source-register pages, and all 22 direct
profiles referenced by the evidence bundle. Cache-busted live checks confirmed
23,978 source rows, 23,939 people, 10,256 people with research attempts, 764
verified-affiliation people, 340 verified-employer people, 8,715 archival-review
dispositions, and 13,678 not-started people.

The live Victor C Petchul profile displays the qualified Tilden Technical High
School student affiliation. The live George Petemezas profile displays the
qualified Army-to-OSS pathway, while the Albert Perz profile preserves the
Perez/Perz conflict and the Fred W Peters profile preserves both source rows.
The published site is <https://therealjameswilson.github.io/before-oss/>.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-749-persons-peters --page 365 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-11_batch749.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page365-persons-peters-review_batch-749_2026-10-11.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 365, beginning with row 24, Norma E
Peters. No API key, raw API response, full service or officer number,
copyrighted page image, unrelated Army coded occupation, street address,
modern people-finder record, or private reviewer note is committed or
published.
