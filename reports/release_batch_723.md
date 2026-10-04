# Batch 723 release - Ormond-Orth research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 723 publishes reviewed outcomes for PDF page 352, rows 1-23, from Rudolph
P Ormond through Theodore P Orth. All 23 printed rows were visually checked
against a 300-dpi page render. Original spellings, grades, boxes, notes, and
locations remain recoverable. Initials-only and truncated note forms remain
unexpanded.

Jacob Ornstein receives the cohort's new verified civilian-employer evidence.
A 1942 professional listing places him at Washington University in St. Louis
as an instructor in Spanish and Portuguese; an official federal record begins
his civilian OSS linguist employment in September 1942. The site publishes the
university as a high-confidence, strongly date-bounded immediate affiliation
and last civilian employer, not as an explicit `recruited from` fact.

Clifford Orourke is confirmed as Second Lieutenant Clifford H. O'Rourke by an
exact private officer-identifier match. A declassified OSS report explicitly
documents his January 15, 1944 assignment to OSS from a Replacement Center in
Cairo. The site correctly treats that predecessor as a military assignment;
his civilian-employer question remains unresolved. Laszlo Ormos receives a
qualified medium-confidence 1937 documentary-film-director occupation, with no
employer or immediate-predecessor inference.

Four official Army bulk matches are accepted for identity only, including the
supported fuller form Harold R Orr Jr. Four identifier conflicts remain
visible: Paul E Orr, Leo J Ortego, and the separate Theresa Orocchi and Theresa
A Orroch entities. The two Theresa rows are not merged despite a shared private
identifier.

The cohort records 13 `requires_archival_review`, four
`no_reliable_result_after_protocol`, four `conflicting_sources`, one
`occupation_only_found`, and one `verified_employer_found` outcome. Identity
statuses are 12 unresolved, four high-confidence, four conflicting, two
confirmed, and one probable. The reviewed bundle adds six sources, two
organizations, three affiliations, 15 claims, 27 claim-source links, 23 person
updates, 23 consolidated research attempts, four accepted identity decisions,
and four conflicting decisions.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,667 (40.3818%) |
| People with confirmed/high employer evidence | 329 (1.3743%) |
| People with confirmed/high affiliation evidence | 734 (3.0661%) |
| Archival-review dispositions assessed | 8,125 (33.9404%) |
| Not started | 14,267 |
| Possible duplicate groups | 523 |
| Conflicts | 312 |
| Attempts or plans | 17,600 |
| Claims by confidence | confirmed 1,362; high 2,864; medium 1,519; low 198; conflicting 271; unresolved 2 |
| Citation records / unique source documents | 5,637 / 2,839 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 269;
`documented_prewar_employer_found` 164; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,142; `not_started` 14,267;
`occupation_only_found` 1,043; `requires_archival_review` 3,868; and
`verified_employer_found` 286.

The public projection contains 2,462 published affiliations, 853
organizations, 4,418 public sources, and 6,009 published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick check
  `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
* Astro diagnostics: 357 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,830 pages.
* Browser release suite: 87 / 87 passed across desktop, phone, and tablet (18
  Batch 723, 33 core, six analytics, and 30 accessibility checks).
* Link check: 24,830 HTML files checked; every internal link resolved and
  50,706 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 105,501,531 bytes verified; manifest SHA-256
  `f62a9d3b8cd8f5c0ca0e62952617d6da932d89f9d3fcdfc3f5542cebe04a6c52`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,902 public artifacts, and 1,188 candidate substrings checked
  with zero unexpected boundary matches.
* Production dependency audit: zero vulnerabilities. The static deployment has
  no Node runtime.
* Determinism: consecutive build trees matched at 24,902 files /
  307,156,538 bytes, SHA-256
  `565e29531252b23d1ce8e6d13b5b43bfc2bafb113672808f7f19924135db9fc9`.

Release commit
[`8d32961804b53587304608be56f9f1db5d11f4ee`](https://github.com/therealjameswilson/before-oss/commit/8d32961804b53587304608be56f9f1db5d11f4ee)
was published to `main`. Its
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37193485357)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37193485387)
both completed successfully. GitHub reported only prospective runner/action
deprecation notices: selected actions are being forced from Node.js 20 to 24,
and `ubuntu-latest` is scheduled to migrate to Ubuntu 26. Neither notice
affected this release.

The read-only live verifier compared the deployed site with that immutable
commit and verified 67 assets / 105,501,531 bytes, the same manifest SHA-256,
eight core routes, 30 source-register pages, and all 23 Batch 723 direct profile
URLs at <https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-723 --page 352 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-723 --max-queries 23
python3 -m oss_research research --source loc --batch batch-723 --max-queries 23
python3 -m oss_research research --source web --batch batch-723 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch723.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page352-ormond-orth-review_batch-723_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 352, row 24. No API key, raw API
response, full service or officer number, copyrighted page image, unrelated
Army coded occupation, street address, modern people-finder record, or private
reviewer note is committed or published. No authenticated NARA Catalog API
request was made for this batch.
