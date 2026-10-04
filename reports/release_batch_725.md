# Batch 725 release - Osterbur-Ottwell research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 725 publishes reviewed outcomes for PDF page 353, rows 1-23, from Robert
J Osterbur through Paul O Ottwell. All 23 printed rows were visually checked
against a 300-dpi page render. Original spellings, grades, boxes, notes, and
locations remain recoverable, including `Walter S Oswalo` and the incomplete
notes `fodler co`, `charge s`, and `folder se`.

Julius Ostroff receives confirmed, direct evidence from his 1944 OSS Board
interview. It matches his exact name, Navy grade, and protected identifier and
records his pre-Navy civilian occupation as salesman. Because the interview
does not name an employer or establish that this was his immediate pre-OSS
role, the site publishes only the occupation and does not invent an employer.

Gjerulf "Gerald" Ottersland receives high-confidence identity evidence and
two qualified medium-confidence pathway claims. The site identifies the 99th
Infantry Battalion (Separate) as his immediate military assignment before OSS
and an unnamed Brooklyn shipyard as his last civilian work before 1942 Army
enlistment. It preserves the missing shipyard name rather than normalizing the
lead to a guessed company. Official OSS records confirm Fred R Ostheimer and
Roy N Osthus at high identity confidence but provide no employer evidence.

Two exact, nonshared protected-identifier results are accepted for identity
only: Robert J Osterbur and Gustav F Osterman. Two protected-identifier
conflicts remain visible: Raymond R Otake versus an Army Raymond K Otake, and
a number printed in the index for both Paul O Ottwell and William H Thomas. No
mismatched Army metadata is transferred and no rows are silently merged.

The cohort records 15 `requires_archival_review`, four
`no_reliable_result_after_protocol`, two `conflicting_sources`, and two
`occupation_only_found` outcomes. Identity statuses are 15 unresolved, four
high-confidence, two confirmed, and two conflicting. The reviewed bundle adds
seven sources, one organization, three affiliations, 11 claims, 20
claim-source links, 23 person updates, and 23 consolidated research attempts.
Two accepted and two conflicting identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,712 (40.5698%) |
| People with confirmed/high employer evidence | 330 (1.3785%) |
| People with confirmed/high affiliation evidence | 737 (3.0787%) |
| Archival-review dispositions assessed | 8,170 (34.1284%) |
| Not started | 14,222 |
| Possible duplicate groups | 523 |
| Conflicts | 316 |
| Attempts or plans | 17,696 |
| Claims by confidence | confirmed 1,368; high 2,874; medium 1,521; low 198; conflicting 275; unresolved 2 |
| Citation records / unique source documents | 5,649 / 2,847 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 273;
`documented_prewar_employer_found` 164; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,150; `not_started` 14,222;
`occupation_only_found` 1,045; `requires_archival_review` 3,898; and
`verified_employer_found` 287.

The public projection contains 2,467 published affiliations, 855
organizations, 4,430 public sources, and 6,031 published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick check
  `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
* Astro diagnostics: 359 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,832 pages.
* Browser release suite: 86 checks passed across desktop, phone, and tablet;
  one tablet accessibility run for the organization directory stalled at its
  timeout after the same test passed on desktop and phone, then passed in 4.2
  seconds on an isolated rerun. All 87 release checks therefore have passing
  results, including 18 Batch 725, 33 core, six analytics, and 30
  accessibility checks.
* Link check: 24,832 HTML files checked; every internal link resolved and
  50,713 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 105,631,993 bytes verified; manifest SHA-256
  `44ba5477733843a9008023ef2f8bbe6dd7e283ce82a3e4c1f5e359758e4e13ae`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,904 public artifacts, and 1,186 candidate substrings checked
  with zero unexpected boundary matches.
* Production dependency audit: zero vulnerabilities. The static deployment has
  no Node runtime.
* Determinism: consecutive build trees matched at 24,904 files /
  307,366,564 bytes, SHA-256
  `8a84af4886cd6720ff09dbb85d836af339822b6e48bac5d531f1d782b9a17f65`.

Deployment verification will be appended after the immutable release commit is
published and its GitHub Actions runs complete.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-725 --page 353 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-725 --max-queries 23
python3 -m oss_research research --source loc --batch batch-725 --max-queries 23
python3 -m oss_research research --source web --batch batch-725 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch725.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page353-osterbur-ottwell-review_batch-725_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary is PDF page 353, rows 24-46. No API key, raw API
response, full service or officer number, copyrighted page image, unrelated
Army coded occupation, street address, modern people-finder record, or private
reviewer note is committed or published. No authenticated NARA Catalog API
request was made for this batch.
