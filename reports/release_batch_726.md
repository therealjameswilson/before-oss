# Batch 726 release - Otwell-Owens research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 726 publishes reviewed outcomes for PDF page 353, rows 24-46, from Betty
N Otwell through David A Owens. All 23 printed rows were visually checked
against a 300-dpi page render. Original spellings, grades, boxes, notes, and
locations remain recoverable. In particular, `Oaul Ouer` and `Adrien
Outellett` remain the indexed forms rather than being silently corrected.

Jose R Oural is confirmed as José Ramón Oural López by the exact indexed and
Army names, a nonshared private identifier, University of South Florida
records, and an independent historical account of his May 1944 OSS mission.
The site publishes his June 17, 1943 entry into the Army of the United States
as documented pre-OSS military service. It does not claim an immediate Army
assignment, infer a unit or civilian employer, convert an Army occupation
code, or misuse his postwar employment as prewar evidence.

Six other exact or documented-variant Army matches are accepted for identity
only: Paul L Otwell, Stephen Ovary, Alvin M Overall, Sven I Overbo, Auburn E
Owen Jr, and Charles W Owen. The official Army coded occupations are not
converted into named work. Carla R Overly remains a visible conflict because
the identifier-matched Army row says Carl R Overly. No mismatched metadata is
transferred.

The cohort records 15 `requires_archival_review`, six
`no_reliable_result_after_protocol`, one `conflicting_sources`, and one
`occupation_only_found` outcome. Identity statuses are 15 unresolved, six
high-confidence, one confirmed, and one conflicting. The reviewed bundle adds
five sources, one affiliation, nine claims, 22 claim-source links, 23 person
updates, and 23 consolidated research attempts. Seven accepted and one
conflicting identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,735 (40.6659%) |
| People with confirmed/high employer evidence | 330 (1.3785%) |
| People with confirmed/high affiliation evidence | 738 (3.0828%) |
| Archival-review dispositions assessed | 8,193 (34.2245%) |
| Not started | 14,199 |
| Possible duplicate groups | 523 |
| Conflicts | 317 |
| Attempts or plans | 17,744 |
| Claims by confidence | confirmed 1,370; high 2,880; medium 1,521; low 198; conflicting 276; unresolved 2 |
| Citation records / unique source documents | 5,654 / 2,851 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 274;
`documented_prewar_employer_found` 164; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,156; `not_started` 14,199;
`occupation_only_found` 1,046; `requires_archival_review` 3,913; and
`verified_employer_found` 287.

The public projection contains 2,468 published affiliations, 855
organizations, 4,435 public sources, and 6,040 published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick check
  `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
* Astro diagnostics: 360 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,832 pages.
* Browser release suite: 84 / 84 checks passed across desktop, phone, and
  tablet, including 15 Batch 726, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,832 HTML files checked; every internal link resolved and
  50,716 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 105,688,902 bytes verified; manifest SHA-256
  `1be1afbcee90e353a6bc8e5904a06b104dbd5b5e60c569ba7747a96573a10a48`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,904 public artifacts, and 1,186 candidate substrings checked
  with zero unexpected boundary matches.
* Production dependency audit: zero vulnerabilities. The static deployment has
  no Node runtime.
* Determinism: consecutive build trees matched at 24,904 files /
  307,454,770 bytes, SHA-256
  `21d47a6300f6b510d705e37fc2f528c32ef82e830837874d8c8129c81f78389b`.

## Publication verification

Release commit
[`226f1395f952e5b9436d22d426473a8eb1ed40ff`](https://github.com/therealjameswilson/before-oss/commit/226f1395f952e5b9436d22d426473a8eb1ed40ff)
was pushed to `main`. GitHub Actions completed successfully for both the
[`Test` run](https://github.com/therealjameswilson/before-oss/actions/runs/37210634559)
and the
[`Deploy GitHub Pages` run](https://github.com/therealjameswilson/before-oss/actions/runs/37210634560).

The immutable verifier then compared the public site with that exact commit.
It verified 67 assets / 105,688,902 bytes, manifest SHA-256
`1be1afbcee90e353a6bc8e5904a06b104dbd5b5e60c569ba7747a96573a10a48`,
eight core routes, 30 source-register pages, and all 23 direct Batch 726
profile routes. The verified public base URL is
<https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-726 --page 353 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-726 --max-queries 23
python3 -m oss_research research --source loc --batch batch-726 --max-queries 23
python3 -m oss_research research --source web --batch batch-726 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch726.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page353-otwell-owens-review_batch-726_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary is PDF page 354, rows 1-23, from Emily L Owens
through Don S Packer. No API key, raw API response, full service or officer
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
