# Batch 705 release - Nielsen-Nipper research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 705 covers PDF page 342, row 46, and page 343, rows 1-22, from Arthur H
Nielsen through Verne F Nipper. Fresh visual inspection confirmed all 23 printed
rows, representing 23 active person entities. The immutable extraction is
unchanged.

Julian M Niemczyk is confirmed by a Library of Congress oral history documenting
his progression from University of Oklahoma student through the 45th Division,
artillery leadership, and direct OSS recruitment from his battalion. The public
profile distinguishes his immediate military assignment from earlier student
status.

Henry R Nigrelli is a high-confidence identity match supported by contemporary
WPTF records, a 1940 Raleigh directory, and a separate OSS history. WPTF is
published as his last civilian employer before military service, not as an
explicitly immediate pre-OSS affiliation.

Boonyong Nikrodananda is a high-confidence identity match supported by Cornell,
a contemporary Harvard newspaper, and a scholarly cross-reference between name
variants. Cornell and Harvard are correctly modeled as student relationships;
his Free Thai activity is visibly qualified. Halver H Nipe is confirmed as
Halvor H Nipe and linked to the 99th Infantry Battalion (Separate), from which a
published Operation Rype account says the OSS recruited its Norwegian-speaking
volunteers.

Official Army bulk evidence supports five additional high-confidence
identity-only decisions. Lester C Nieman remains conflicting and unmerged from
a separate Lester C Neimann row sharing the same identifier. Unsupported name,
Red Cross, radio, and engineering leads were rejected. The CIA and LoC adapters
failed closed; the full staged protocol was nevertheless completed for all 23
people using accessible official, institutional, contemporary, military, and
archival sources.

The cohort records 18 `no_reliable_result_after_protocol`, three `completed`,
one `conflicting_sources`, and one `verified_employer_found` outcome. Identity
statuses are two `confirmed`, seven `high_confidence`, one `conflicting`, and 13
`unresolved`. The evidence bundle adds 12 sources, seven organizations, seven
affiliations, 16 claims, 34 claim-source links, 23 person updates, and 23
research attempts. Four claims are confirmed, 11 are high confidence, and one
medium-confidence claim is published only with visible qualification.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,254 (38.6566%) |
| People with confirmed/high employer evidence | 320 (1.3367%) |
| People with confirmed/high affiliation evidence | 711 (2.9700%) |
| Archival-review dispositions assessed | 7,712 (32.2152%) |
| Not started | 14,680 |
| Possible duplicate groups | 523 |
| Conflicts | 274 |
| Attempts or plans | 16,700 |
| Claims by confidence | confirmed 1,351; high 2,702; medium 1,479; low 196; conflicting 248; unresolved 2 |
| Citation records / unique source documents | 5,518 / 2,746 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 174; `conflicting_sources` 231;
`documented_prewar_employer_found` 155; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 885; `not_started` 14,680;
`occupation_only_found` 1,038; `requires_archival_review` 3,783; and
`verified_employer_found` 282.

The public projection contains **2,408** published affiliations, **823**
organizations, **4,301** public sources, and **5,773** published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all parser-warning rows visually
  resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing.
- Astro diagnostics: **339 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,799 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 705, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,799 HTML files** checked; every internal link resolved and
  50,610 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 104,124,446 bytes** verified; manifest SHA-256
  `84ca5b25445008146a624b239a3aaf7bccac8e0b30411a8af843705813d52725`.
- Private-identifier audit: **70 public data artifacts**, 12,926 normalized
  identifiers, 120 formatted variants, and 719 candidate substrings checked
  with **0 unexpected boundary matches**. Two numeric matches inside the public
  manifest were recognized as harmless file-size values.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,871 files /
  304,903,423 bytes**, SHA-256
  `0adf4d8557108e846549300d78998c9fd88fbbecb10893d433aaf1d4c6fd091c`.

The unbounded historical Playwright aggregate remains too large for one Node
process because 177 legacy specifications repeatedly retain the 56 MB people
dataset and exhaust an 8 GB heap. This is a runner-resource limitation, not a
known product failure. The bounded release suite exercises the core routes,
Batch 705 profiles, analytics, responsive layouts, and accessibility across all
three configured browser projects and passed 90 / 90.

## Released and verified live

Batch 705 was fast-forwarded to `main` as commit
[`4706a30724ea62677cb4b324b6bb8418ecbad4cf`](https://github.com/therealjameswilson/before-oss/commit/4706a30724ea62677cb4b324b6bb8418ecbad4cf).
The GitHub Pages build and deployment
[`37128752492`](https://github.com/therealjameswilson/before-oss/actions/runs/37128752492)
and independent test workflow
[`37128752449`](https://github.com/therealjameswilson/before-oss/actions/runs/37128752449)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 104,124,446 bytes matched, as did eight core
routes, all 29 source-register pages, and all 23 Batch 705 profiles changed by
the reviewed-evidence bundle. The live site reports 23,978 source rows, 23,939
person entities, 9,254 researched people, 711 verified affiliations, 320
verified employers, and 14,680 not-started people. Julian M Niemczyk's
immediate military pathway, Henry R Nigrelli's last civilian employer,
Boonyong Nikrodananda's student and qualified volunteer relationships, Halvor
H Nipe's immediate Army assignment, all five additional identity-only
decisions, the unmerged Lester C Nieman conflict, and the unresolved profiles
render from their public URLs. The oil-company directory remains visible with
nine cited people across eleven historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-705a --page 342 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-705b --page 343 --first-row 1 --last-row 22
python3 -m oss_research research --source cia --batch batch-705a --max-queries 1
python3 -m oss_research research --source loc --batch batch-705a --max-queries 1
python3 -m oss_research research --source loc --batch batch-705b --max-queries 6
python3 -m oss_research research --source web --batch batch-705a --resume --max-queries 1
python3 -m oss_research research --source web --batch batch-705b --resume --max-queries 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch705.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages342-343-nielsen-nipper-review_batch-705_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 343, row 23 (George H Nishi).
No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, street address, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
