# Batch 706 release - Nishi-Noel research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 706 covers PDF page 343, rows 23-45, from George H Nishi through James A
Noel. Fresh 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. The immutable extraction is unchanged.

Katsuma Nishimoto is a high-confidence identity match supported by a Japanese
American Veterans Association article documenting his Military Intelligence
Service Language School training at Camp Savage and later Southeast Asia
translator and intercept work. The school is published only as a qualified
military assignment with uncertain temporal relation to OSS service.

Marshall H Noble is confirmed through exact name and protected-identifier
evidence across the OSS index, official Army data, and a direct Detachment 101
promotion report. Andre Noel is a high-confidence match to Second Lieutenant
Andre Noel, alias Andre Ferriere, radio operator on OSSEX Team FILAN. His Free
French Forces affiliation is visibly qualified because the recruitment
evidence applies to the SUSSEX program rather than documenting his individual
transfer.

Official Army bulk evidence supports seven additional high-confidence
identity-only decisions. Malcolm N Nishioa and Yincenzo L Nocella remain as
visible conflicts rather than being merged with similar Army records. The CIA
and LoC adapters failed closed; the full staged protocol was nevertheless
completed for all 23 people using accessible official, institutional,
contemporary, military, and archival sources.

The cohort records 19 `no_reliable_result_after_protocol`, two `completed`, and
two `conflicting_sources` outcomes. Identity statuses are one `confirmed`, nine
`high_confidence`, two `conflicting`, and 11 `unresolved`. The evidence bundle
adds six sources, two organizations, two affiliations, 14 claims, 29
claim-source links, 23 person updates, and 23 research attempts. Claims comprise
one confirmed, nine high-confidence, two medium-confidence, and two conflicting
decisions.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,277 (38.7527%) |
| People with confirmed/high employer evidence | 320 (1.3367%) |
| People with confirmed/high affiliation evidence | 711 (2.9700%) |
| Archival-review dispositions assessed | 7,735 (32.3113%) |
| Not started | 14,657 |
| Possible duplicate groups | 523 |
| Conflicts | 276 |
| Attempts or plans | 16,748 |
| Claims by confidence | confirmed 1,352; high 2,711; medium 1,481; low 196; conflicting 250; unresolved 2 |
| Citation records / unique source documents | 5,524 / 2,751 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 176; `conflicting_sources` 233;
`documented_prewar_employer_found` 155; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 904; `not_started` 14,657;
`occupation_only_found` 1,038; `requires_archival_review` 3,783; and
`verified_employer_found` 282.

The public projection contains **2,410** published affiliations, **823**
organizations, **4,307** public sources, and **5,787** published claims. The
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
- Astro diagnostics: **340 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,799 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 706, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,799 HTML files** checked; every internal link resolved and
  50,613 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 104,200,556 bytes** verified; manifest SHA-256
  `307c97cf5b486eabb92a4e7b54c7457ccf4efe18da390beba0c818931aafef7c`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,871 artifacts, and 1,163 candidate substrings checked with **0
  unexpected boundary matches**. Two numeric matches inside the public manifest
  were recognized as harmless file-size values.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,871 files /
  305,021,240 bytes**, SHA-256
  `19b144989ac7d1f8ab545186ef1f8fb78c88f5b3894c7d0d4fae148ae845c0f6`.

The unbounded historical Playwright aggregate remains too large for one Node
process because the legacy specifications repeatedly retain the large people
dataset and exhaust an 8 GB heap. This is a runner-resource limitation, not a
known product failure. The bounded release suite exercises the core routes,
Batch 706 profiles, analytics, responsive layouts, and accessibility across all
three configured browser projects.

## Deployment status

Commit, GitHub Actions, and live-site verification details will be appended
after the audited release is pushed and the public deployment passes.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-706 --page 343 --first-row 23 --last-row 45
python3 -m oss_research research --source cia --batch batch-706 --max-queries 23
python3 -m oss_research research --source loc --batch batch-706 --max-queries 23
python3 -m oss_research research --source web --batch batch-706 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch706.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page343-nishi-noel-review_batch-706_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 343, row 46 (Joseph L Noel).
No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, street address, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
