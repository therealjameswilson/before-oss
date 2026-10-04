# Batch 724 release - Ortiz-Ossman research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 724 publishes reviewed outcomes for PDF page 352, rows 24-46, from
Gilbert Ortiz through Harold Ossman. All 23 printed rows were visually checked
against a 300-dpi page render. Original spellings, grades, boxes, notes, and
locations remain recoverable, including `Birginia Osborn` and the incomplete
notes `Polish Ar`, `possibly`, `folder se`, and `aka Atna`.

Lithgow Osborne receives the cohort's new confirmed predecessor evidence. His
signed 1942 New York State report and the Congressional Record document his
transition from Conservation Commissioner to OSS. The site publishes the New
York State Conservation Department as an explicit immediate affiliation and
last civilian government employer, classified as a government assignment
rather than private employment.

Helen Osmun is linked at high confidence to Helen Edith Osmun Parker. A
contemporary Swarthmore yearbook and a reputable obituary support a documented
prewar student affiliation and subsequent wartime OSS work. The site does not
turn Swarthmore attendance into employment or claim it was the immediate
predecessor. Peter J Ortiz retains his previously reviewed Marine Corps and
French Foreign Legion evidence without duplicated claims.

Four exact, nonshared protected-identifier results are accepted for identity
only: Robert G Osborne, Stanley Oscar, Leonard Oshrain, and Francis J Osinskie.
Two conflicting protected-identifier results for Frederic C Osgood and Harold
Ossman remain visible without transferring mismatched Army metadata. A
first-name-free Captain Orwin discovery lead is rejected because it cannot
distinguish the two adjacent Robert Orwin rows.

The cohort records 15 `requires_archival_review`, four
`no_reliable_result_after_protocol`, two `conflicting_sources`, and two
`verified_employer_found` outcomes. Identity statuses are 14 unresolved, six
high-confidence, two conflicting, and one confirmed. The reviewed bundle adds
six sources, two organizations, two affiliations, 11 claims, 24 claim-source
links, 23 person updates, and 23 consolidated research attempts. Four accepted
and two conflicting identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,689 (40.4737%) |
| People with confirmed/high employer evidence | 329 (1.3743%) |
| People with confirmed/high affiliation evidence | 736 (3.0745%) |
| Archival-review dispositions assessed | 8,147 (34.0323%) |
| Not started | 14,245 |
| Possible duplicate groups | 523 |
| Conflicts | 314 |
| Attempts or plans | 17,648 |
| Claims by confidence | confirmed 1,365; high 2,870; medium 1,519; low 198; conflicting 273; unresolved 2 |
| Citation records / unique source documents | 5,643 / 2,844 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 271;
`documented_prewar_employer_found` 164; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,146; `not_started` 14,245;
`occupation_only_found` 1,043; `requires_archival_review` 3,883; and
`verified_employer_found` 287.

The public projection contains 2,464 published affiliations, 855
organizations, 4,424 public sources, and 6,020 published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick check
  `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
* Astro diagnostics: 358 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,832 pages.
* Browser release suite: 87 / 87 passed across desktop, phone, and tablet (18
  Batch 724, 33 core, six analytics, and 30 accessibility checks).
* Link check: 24,832 HTML files checked; every internal link resolved and
  50,712 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 105,573,359 bytes verified; manifest SHA-256
  `888602aabdf19400b1c81c26fb2cd4cc985e8802d2b70e8adc1b12b5d0f6bf44`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,904 public artifacts, and 1,188 candidate substrings checked
  with zero unexpected boundary matches.
* Production dependency audit: zero vulnerabilities. The static deployment has
  no Node runtime.
* Determinism: consecutive build trees matched at 24,904 files /
  307,274,758 bytes, SHA-256
  `ba5feb053f7a89e0cf1497e0d32bcc48c760e3085245daad8c536000aed761c0`.

Release commit
[`9aabd20da17714123c3f88dd3f98bfb42f1b4e3e`](https://github.com/therealjameswilson/before-oss/commit/9aabd20da17714123c3f88dd3f98bfb42f1b4e3e)
was published to `main`. Its
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37195294160)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37195294183)
both completed successfully. GitHub reported only prospective runner/action
deprecation notices: selected actions are being forced from Node.js 20 to 24,
and `ubuntu-latest` is scheduled to migrate to Ubuntu 26. Neither notice
affected this release.

The read-only live verifier compared the deployed site with that immutable
commit and verified 67 assets / 105,573,359 bytes, the same manifest SHA-256,
eight core routes, 30 source-register pages, and all 23 Batch 724 direct profile
URLs at <https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-724 --page 352 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-724 --max-queries 23
python3 -m oss_research research --source loc --batch batch-724 --max-queries 23
python3 -m oss_research research --source web --batch batch-724 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch724.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page352-ortiz-ossman-review_batch-724_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 353, row 1; a later full-page
visual recount confirmed that page 352 contains exactly 46 printed rows. No API key, raw API
response, full service or officer number, copyrighted page image, unrelated
Army coded occupation, street address, modern people-finder record, or private
reviewer note is committed or published. No authenticated NARA Catalog API
request was made for this batch.
