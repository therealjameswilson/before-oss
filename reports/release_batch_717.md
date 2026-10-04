# Batch 717 release - Olafsen-Oliver research

Research and release date: 2026-10-04 America/New_York.

## Historical work

Batch 717 covers PDF page 349, rows 1-23, from Paul N Olafsen through Louise
L Oliver. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Original spellings, ranks, grades,
box numbers, notes, and archival locations remain recoverable from the
immutable source rows. Every row is in Box 571 at location 230/86/37/07.

Seven people receive high-confidence identity matches from the official Army
bulk file: Paul N Olafsen, Karl L Olberg, David Oldashi, Ross C Oldford, John G
Oldiges, Arthur R Oldrey, and Darwin G Oliver. Each match uses the exact
printed name plus a nonshared protected identifier. Those identifiers remain
private. No coded Army occupation was converted into occupation or employer
evidence.

James H Oliver is probably the classicist James Henry Oliver. The exact name
and middle initial, indexed major rank, Barnard College career ending in 1942,
wartime gap, and 1946 return to academic employment form a coherent
chronology. Columbia's 1936 annual report announces his appointment as an
assistant professor responsible for ancient history, while the Rutgers
Database of Classical Scholars dates the Barnard employment from 1936 through
1942. Because no direct personnel-file or unique-identifier bridge was found,
the identity and Barnard claim remain `probable` / `medium` and visibly
qualified. Barnard is modeled as the likely last civilian employer before
wartime service, not as the immediate pre-OSS affiliation. It is excluded from
default high-confidence employer analytics.

George T Olden is not silently merged with the famous OSS graphic designer
Georg Olden. The index row visibly prints middle initial `T`, while the
biographical candidate was George Elliott Olden. The CIA source establishes
that Georg Olden served as an OSS graphic designer, but supplies no bridge to
the indexed Box 571 row. The profile therefore publishes the identity conflict
and withholds the designer's student and career history from this entity.

Roy A Oleary and Roy A Olerud remain separate source-derived entities. Fresh
visual inspection confirms that the adjacent rows share a protected identifier
despite materially different surnames. Contemporary trade sources give Olerud
a coherent postwar broadcast-engineering career, but do not establish prewar
employment or resolve the duplicate. The two profiles share a deterministic
public possible-duplicate group and require comparison of both Box 571 files
before any merge or spelling correction.

The printed `one fold` note for Courtenay Olden and `also AS` note for David A
Olds remain recoverable without expansion. Both require archival examination.
Common-name and incomplete-identifier cases remain unresolved rather than
being attached to convenient biographies.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed. The web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed the required
official, exact-name OSS, employment, occupation, obituary, institutional,
newspaper, directory, military, and archival source families for every person.

The cohort records 17 `no_reliable_result_after_protocol`, three
`conflicting_sources`, two `requires_archival_review`, and one
`documented_prewar_employer_found` outcome. Identity statuses are seven
`high_confidence`, 12 `unresolved`, two `probable`, one `ambiguous`, and one
`conflicting`. The reviewed bundle imports six sources, one organization, one
affiliation, 10 claims, 22 claim-source links, 23 person updates, and 23
consolidated research attempts. Seven accepted identity-review decisions are
recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,529 (39.8053%) |
| People with confirmed/high employer evidence | 326 (1.3618%) |
| People with confirmed/high affiliation evidence | 724 (3.0244%) |
| Archival-review dispositions assessed | 7,987 (33.3640%) |
| Not started | 14,405 |
| Possible duplicate groups | 523 |
| Conflicts | 299 |
| Attempts or plans | 17,310 |
| Claims by confidence | confirmed 1,352; high 2,809; medium 1,508; low 198; conflicting 258; unresolved 2 |
| Citation records / unique source documents | 5,596 / 2,809 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 184; `conflicting_sources` 256;
`documented_prewar_employer_found` 160; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,097; `not_started` 14,405;
`occupation_only_found` 1,040; `requires_archival_review` 3,800; and
`verified_employer_found` 285.

The public projection contains 2,438 published affiliations, 843
organizations, 4,377 public sources, and 5,920 published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Verification and publication

The exact rebuilt tree passed these local release gates:

- Python unit suite: 139 / 139 passed, plus generated subtests.
- Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick
  check `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
- Stratified profile audit: 200 profiles, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing. The women stratum was unavailable because the project
  does not infer gender.
- Astro diagnostics: 351 files, 0 errors, 0 warnings, 0 hints.
- Production build: 24,820 pages.
- Browser release suite: 90 / 90 passed across desktop, phone, and tablet (21
  Batch 717, 33 core, six analytics, and 30 accessibility checks).
- Link check: 24,820 HTML files checked; every internal link resolved and
  50,672 unique external URLs were inventoried for the separate live check.
- Public manifest: 67 assets / 104,998,384 bytes verified; manifest SHA-256
  `0cc25b2c13450cec64e363b2b5b2a2f463915b0f3e8717cbf4fe6c27d19a21b8`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,892 public artifacts, and 1,159 candidate substrings checked
  with zero unexpected boundary matches.
- Production dependency audit: zero vulnerabilities. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at 24,892 files / 306,337,892
  bytes, SHA-256
  `3e14329e3d83486cc4eeeb96949b28ed3b31796f38172177956062cf74f4503a`.

Release commit
[`44fd4adf7607b73b9774d9bf452a47c8392d3323`](https://github.com/therealjameswilson/before-oss/commit/44fd4adf7607b73b9774d9bf452a47c8392d3323)
was published to `main`. Its
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37181188947)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37181188975)
both completed successfully. GitHub reported only prospective runner/action
deprecation notices: selected actions are being forced from Node.js 20 to 24,
and `ubuntu-latest` is scheduled to migrate to Ubuntu 26. Neither notice
affected this release.

The read-only live verifier compared the deployed site with that immutable
commit and verified 67 assets / 104,998,384 bytes, the same manifest SHA-256,
eight core routes, 30 source-register pages, and all 23 Batch 717 direct
profile URLs at <https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-717 --page 349 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-717 --max-queries 23
python3 -m oss_research research --source loc --batch batch-717 --max-queries 23
python3 -m oss_research research --source web --batch batch-717 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch717.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page349-olafsen-oliver-review_batch-717_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 349, row 24 (Maida O Oliver) and
runs through row 46 (Clinton L Olson). No API key, raw API response, full
service number, copyrighted page image, unrelated Army coded occupation,
street address, modern people-finder record, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
