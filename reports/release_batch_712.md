# Batch 712 release - Obenshain-Obucina research

Research and release-candidate date: 2026-10-03 America/New_York.

## Historical work

Batch 712 covers PDF page 346, rows 24-46, from Donald W Obenshain through
Joseph D Obucina. Fresh 300-dpi visual inspection confirmed all 23 printed
rows, representing 23 active person entities. Original index spellings,
punctuation, rank fields, box numbers, and archival location remain
recoverable from the immutable source rows.

Nine new identity claims meet publication standards. Eight are grounded in
nonshared identifiers from NARA's official Army bulk file; the Micheal/Michael
spelling difference is retained as a variant. A contemporary Detachment 101
promotion record corroborates John M Obereiner's OSS identity. These records
do not establish named pre-OSS employers, and Army occupation codes were not
converted into occupations or affiliations. Serge Obolensky's previously
reviewed National Guard, St. Regis Hotel, banking, and real-estate chronology
remains intact without creating duplicate claims.

Ten LoC newspaper candidates are formally rejected as common-name discovery
noise. Plausible John R O'Brien and Walter E O'Brien namesake leads are also
withheld because they lack sufficient corroborating identifiers or conflict
with the indexed identifier. The cohort records 21
`no_reliable_result_after_protocol`, one `requires_archival_review`, and one
`documented_prewar_employer_found` outcome. Identity statuses are one
`confirmed`, nine `high_confidence`, and 13 `unresolved`. The reviewed bundle
adds three sources, nine claims, 18 claim-source links, 23 person updates, and
23 consolidated research attempts. Eighteen identity-review decisions are
recorded: eight accepted Army matches and ten rejected newspaper candidates.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,414 (39.3250%) |
| People with confirmed/high employer evidence | 325 (1.3576%) |
| People with confirmed/high affiliation evidence | 720 (3.0076%) |
| Archival-review dispositions assessed | 7,872 (32.8836%) |
| Not started | 14,520 |
| Possible duplicate groups | 523 |
| Conflicts | 293 |
| Attempts or plans | 17,069 |
| Claims by confidence | confirmed 1,352; high 2,773; medium 1,497; low 198; conflicting 256; unresolved 2 |
| Citation records / unique source documents | 5,567 / 2,786 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 180; `conflicting_sources` 250;
`documented_prewar_employer_found` 158; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 1,003; `not_started` 14,520;
`occupation_only_found` 1,039; `requires_archival_review` 3,793; and
`verified_employer_found` 285.

The public projection contains **2,425** published affiliations, **832**
organizations, **4,348** public sources, and **5,871** published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Verification and publication

The exact rebuilt tree passed these local release gates:

- Python unit suite: **139 / 139 passed**, plus 78 generated subtests.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all 32 parser-warning rows
  visually resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, public-projection, and
  terminal-status invariant passing.
- Astro diagnostics: **346 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,808 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 712, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,808 HTML files** checked; every internal link resolved and
  50,646 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 104,683,101 bytes** verified; manifest SHA-256
  `7736918610acd7d176c6fd60e61a78aa9d4c30341a1b436d0bf0f4dcfd038569`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,880 artifacts, and 1,163 candidate substrings checked with **0
  unexpected boundary matches**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,880 files /
  305,804,002 bytes**, SHA-256
  `da959d1c14e9e80170c7759d37de5ecf1dad82836a2ec0d2aa3a95490c1a1f37`.

Exact commit metadata, GitHub Actions runs, and live deployment verification
will be recorded after the release is pushed.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-712 --page 346 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-712 --max-queries 23
python3 -m oss_research research --source loc --batch batch-712 --max-queries 23
python3 -m oss_research research --source web --batch batch-712 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch712.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page346-obenshain-obucina-review_batch-712_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 346, row 47 (Bernard F
O'Connell). No API key, raw API response, full service number, copyrighted
page image, unrelated Army coded occupation, street address, modern
people-finder record, or private reviewer note is committed or published. No
authenticated NARA Catalog API request was made for this batch.
