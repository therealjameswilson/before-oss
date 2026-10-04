# Batch 722 release - Orban-Ormiston research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 722 publishes reviewed outcomes for PDF page 351, rows 24-46, from John
Orban through David Ormiston. All 23 printed rows were visually checked against
a 300-dpi page render. Original spellings, grades, boxes, notes, and locations
remain recoverable. The unusual printed forms `also AS`, `Pampeil`,
`Orlowsci`, and rank `Pc` are preserved without silent correction.

Joseph J Orlan receives the cohort's only new pre-OSS occupation evidence: a
1936 signed contribution says amateur radio had become his vocation. A 1946
contemporary memorial separately documents his 1940 Signal Corps assignment at
Pearl Harbor and later OSS communications role. The site publishes these as a
qualified occupation and an earlier military assignment, not as a named
civilian employer or an explicit immediate predecessor.

Alekos X Orkoulas and John Orisek receive confirmed identities from official
wartime records matching exact name, grade, and protected identifier. Peter C
Orlich receives a high-confidence identity from a direct-witness mission
history. Their sources document OSS roles but do not establish pre-OSS
employers. Eight official Army bulk matches are accepted for identity only,
including the supported fuller form David K Ormiston. Liberio Orlando/Liborio
and John Orlowsci/Orlowski remain visible conflicts pending Box 576 review.

The cohort records 12 `requires_archival_review`, eight
`no_reliable_result_after_protocol`, two `conflicting_sources`, and one
`occupation_only_found` outcomes. Identity statuses are nine unresolved, ten
high-confidence, two confirmed, and two conflicting. The reviewed bundle adds
seven sources, two affiliations, 16 claims, 30 claim-source links, 23 person
updates, 23 consolidated research attempts, eight accepted identity decisions,
and two conflicting decisions.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,644 (40.2857%) |
| People with confirmed/high employer evidence | 328 (1.3701%) |
| People with confirmed/high affiliation evidence | 732 (3.0578%) |
| Archival-review dispositions assessed | 8,102 (33.8444%) |
| Not started | 14,290 |
| Possible duplicate groups | 523 |
| Conflicts | 308 |
| Attempts or plans | 17,550 |
| Claims by confidence | confirmed 1,359; high 2,858; medium 1,517; low 198; conflicting 267; unresolved 2 |
| Citation records / unique source documents | 5,631 / 2,834 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 265;
`documented_prewar_employer_found` 164; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,138; `not_started` 14,290;
`occupation_only_found` 1,042; `requires_archival_review` 3,855; and
`verified_employer_found` 285.

The public projection contains 2,459 published affiliations, 851
organizations, 4,412 public sources, and 5,994 published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

- Python unit suite: 139 / 139 passed, plus generated subtests.
- Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick check
  `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
- Astro diagnostics: 356 files, 0 errors, 0 warnings, 0 hints.
- Production build: 24,828 pages.
- Browser release suite: 87 / 87 passed across desktop, phone, and tablet (18
  Batch 722, 33 core, six analytics, and 30 accessibility checks).
- Link check: 24,828 HTML files checked; every internal link resolved and
  50,701 unique external URLs were inventoried for the separate live check.
- Public manifest: 67 assets / 105,420,188 bytes verified; manifest SHA-256
  `9c103f58545f5e3d5a72b6372dd8d423e0e4b279fa2c9cf86cfcc41370ea26d3`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,900 public artifacts, and 1,192 candidate substrings checked
  with zero unexpected boundary matches.
- Production dependency audit: zero vulnerabilities. The static deployment has
  no Node runtime.
- Determinism: consecutive build trees matched at 24,900 files /
  307,020,362 bytes, SHA-256
  `abe6df9f6369edd83d9d810a97de0941eb0a413f32a5a2032c31443cade5a00a`.

Publication verification will be appended after the immutable release commit is
pushed and GitHub Pages completes.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-722 --page 351 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-722 --max-queries 23
python3 -m oss_research research --source loc --batch batch-722 --max-queries 23
python3 -m oss_research research --source web --batch batch-722 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch722.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page351-orban-ormiston-review_batch-722_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 352, row 1. No API key, raw API
response, full service or officer number, copyrighted page image, unrelated
Army coded occupation, street address, modern people-finder record, or private
reviewer note is committed or published. No authenticated NARA Catalog API
request was made for this batch.
