# Batch 707 release - Noel-Norberg research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 707 covers PDF page 343, row 46, and page 344, rows 1-22, from Joseph L
Noel through Charles R Norberg. Fresh 300-dpi visual inspection confirmed all
23 printed rows, representing 23 active person entities. The immutable
extraction is unchanged. The PDF visual reading, not an NARA web-extraction
transposition, remains authoritative for Paul F Nolan's protected identifier.

Official Army evidence supports six high-confidence identity-only decisions:
Joe P Nogay, Joseph Noia, Loren A Nolan, Richard G Nolan, Thomas A Nolan, and
Orestes M Nomico. An OSS Operational Groups roster independently documents T/5
Joseph Noia on the Chicago II and Ginny I rosters. Coded Army occupations are
not converted into employer claims.

Isamu Noguchi remains only a probable match to the famous sculptor because the
index row is rankless and identifier-free. Institutional evidence supports a
qualified prewar self-employment affiliation while explicitly distinguishing
Noguchi from artists documented as working for OSS. The site does not state
that the famous sculptor served in OSS. Louis A Nonni is also a probable match
to a Ritchie Boys roster entry. Charles R Norberg is a probable match to the
attorney whose last documented civilian employer before wartime service was
Hepburn and Norris; that affiliation is published at medium confidence and is
excluded from default verified-employer analytics.

Oscar D Nohowel versus Nohowell and John N Norback versus Morback remain
visible spelling conflicts pending personnel-file review. The CIA and LoC
adapters failed closed; the full staged protocol was nevertheless completed for
all 23 people using accessible official, institutional, contemporary,
military, newspaper, obituary, and archival sources.

The cohort records 19 `no_reliable_result_after_protocol`, two
`conflicting_sources`, one `occupation_only_found`, and one
`documented_prewar_employer_found` outcome. Identity statuses are six
`high_confidence`, three `probable`, two `conflicting`, and 12 `unresolved`.
The evidence bundle adds eight sources, two organizations, two affiliations,
13 claims, 29 claim-source links, 23 person updates, and 23 research attempts.
Claims comprise six high-confidence, five medium-confidence, and two
conflicting decisions.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,300 (38.8487%) |
| People with confirmed/high employer evidence | 320 (1.3367%) |
| People with confirmed/high affiliation evidence | 711 (2.9700%) |
| Archival-review dispositions assessed | 7,758 (32.4074%) |
| Not started | 14,634 |
| Possible duplicate groups | 523 |
| Conflicts | 278 |
| Attempts or plans | 16,821 |
| Claims by confidence | confirmed 1,352; high 2,717; medium 1,486; low 196; conflicting 252; unresolved 2 |
| Citation records / unique source documents | 5,532 / 2,757 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 176; `conflicting_sources` 235;
`documented_prewar_employer_found` 156; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 923; `not_started` 14,634;
`occupation_only_found` 1,039; `requires_archival_review` 3,783; and
`verified_employer_found` 282.

The public projection contains **2,412** published affiliations, **824**
organizations, **4,315** public sources, and **5,800** published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**, plus **78 / 78** parametrized
  subtests.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all parser-warning rows visually
  resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing.
- Astro diagnostics: **341 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,800 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 707, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,800 HTML files** checked; every internal link resolved and
  50,618 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 104,280,306 bytes** verified; manifest SHA-256
  `8191d3295837ac8c16607eac93def7638d38d4a5f9e2f2f0d04230e3dc09aaf0`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,872 artifacts, and 1,165 candidate substrings checked with **0
  unexpected boundary matches**. Two numeric matches inside the public manifest
  were recognized as harmless file-size values.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,872 files /
  305,147,477 bytes**, SHA-256
  `60c3c6c3510d70c60e1e146283ca46bc0cb6e5e7915e8350cc2d986e3cbed320`.

The unbounded historical Playwright aggregate remains too large for one Node
process because the legacy specifications repeatedly retain the large people
dataset and exhaust an 8 GB heap. This is a runner-resource limitation, not a
known product failure. The bounded release suite exercises the core routes,
Batch 707 profiles, analytics, responsive layouts, and accessibility across all
three configured browser projects.

## Released and verified live

Batch 707 was fast-forwarded to `main` as commit
[`d0b44259fb4825ac32976d03f4251afcbaeb7129`](https://github.com/therealjameswilson/before-oss/commit/d0b44259fb4825ac32976d03f4251afcbaeb7129).
The GitHub Pages build and deployment
[`37161208401`](https://github.com/therealjameswilson/before-oss/actions/runs/37161208401)
and independent test workflow
[`37161208439`](https://github.com/therealjameswilson/before-oss/actions/runs/37161208439)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 104,280,306 bytes matched, as did eight core
routes, all 29 source-register pages, and all 23 Batch 707 profiles changed by
the reviewed-evidence bundle. The live site reports 23,978 source rows, 23,939
person entities, 9,300 researched people, 711 verified affiliations, 320
verified employers, and 14,634 not-started people. Isamu Noguchi's conditional
identity and occupation, Joseph Noia's identity-only OSS roster evidence,
Charles R Norberg's qualified last civilian employer, all five additional
Army-supported identity decisions, both unmerged spelling conflicts, and the
unresolved profiles render from their public URLs. The oil-company directory
remains visible with nine cited people across eleven historically named
companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-707a --page 343 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-707b --page 344 --first-row 1 --last-row 22
python3 -m oss_research research --source cia --batch batch-707a --max-queries 1
python3 -m oss_research research --source cia --batch batch-707b --max-queries 22
python3 -m oss_research research --source loc --batch batch-707a --max-queries 1
python3 -m oss_research research --source loc --batch batch-707b --max-queries 22
python3 -m oss_research research --source web --batch batch-707a --resume --max-queries 1
python3 -m oss_research research --source web --batch batch-707b --resume --max-queries 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch707.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page343-344-noel-norberg-review_batch-707_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 344, row 23 (Willard P Norberg).
No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, street address, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
