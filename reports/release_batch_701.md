# Batch 701 release - Nevada-Newman research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 701 covers PDF page 340, row 46, and page 341, rows 1-22, from Arpad J
Nevada through John R Newman. Fresh visual inspection confirmed all 23 printed
rows. The immutable extraction remains unchanged.

Ilhan New is confirmed through the index, protected identifier, official Army
evidence, and Yuhan's institutional chronology. His immediate Overseas Korean
Congress affiliation, Yuhan presidency, La Choy self-employment, and USC
student status remain distinct. Theodore M Newcomb receives a high-confidence
University of Michigan pathway from an explicit National Academy chronology.

Norman N Newhouse's Long Island Press role and Raymond F Newkirk's FBI
assignment are published with visible medium-confidence temporal
qualifications. John W Newett's Naval Air Corps and OSS service is documented,
but its sequence remains uncertain. Louis W Neve, Charles H New, Victor M
Newberg, Truman H Newberry II, Edwin S Newman, and John R Newman receive
identity-only decisions from official Army evidence. Winton H Newkirk and
Howard L Newman retain visible identifier conflicts.

The Library of Congress API produced 12 candidates. Official OCR context for
each was inspected, and all were rejected as unrelated namesakes or contexts
that did not establish identity or pre-OSS work. The CIA adapter failed closed
at robots policy without sending a request. No raw API response is retained.

The cohort records two `verified_employer_found`, one
`documented_prewar_employer_found`, two `completed`, two
`conflicting_sources`, and 16 `no_reliable_result_after_protocol` outcomes.
Identity statuses are one `confirmed`, ten `high_confidence`, two
`conflicting`, and ten `unresolved`. The evidence bundle adds ten sources,
eight organizations, eight affiliations, 22 claims, 42 claim-source links, 23
person updates, and 23 consolidated research attempts. Seven Army identity
candidates are accepted, two conflicts are preserved, and 12 LoC candidates
are rejected.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,165 (38.2848%) |
| People with confirmed/high employer evidence | 319 (1.3326%) |
| People with confirmed/high affiliation evidence | 706 (2.9492%) |
| Archival-review dispositions assessed | 7,622 (31.8393%) |
| Not started | 14,769 |
| Possible duplicate groups | 521 |
| Conflicts | 272 |
| Attempts or plans | 16,521 |
| Claims by confidence | confirmed 1,345; high 2,671; medium 1,469; low 196; conflicting 245; unresolved 2 |
| Citation records / unique source documents | 5,489 / 2,722 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 169; `conflicting_sources` 229;
`documented_prewar_employer_found` 153; `in_progress` 1,904;
`needs_identity_review` 445; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 812; `not_started` 14,769;
`occupation_only_found` 1,037; `requires_archival_review` 3,783; and
`verified_employer_found` 281.

The public projection contains **2,394** published affiliations, **814**
organizations, **4,272** public sources, and **5,723** published claims.
Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all parser-warning rows visually
  resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing.
- Astro diagnostics: **335 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,790 pages**.
- Browser release suite: **84 / 84 passed** across desktop, phone, and tablet
  (15 Batch 701, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,790 HTML files** checked; every internal link resolved and
  50,582 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 103,801,592 bytes** verified; manifest SHA-256
  `86bc7926238abd88e0daf68a36133bc03f62736b3ce8cd8753772d43860040c5`.
- Private-identifier audit: **24,862 artifacts**, 12,926 normalized identifiers,
  120 formatted variants, and 1,163 candidate substrings checked with **0
  unexpected boundary matches** and **0 false positives**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,862 files /
  304,371,693 bytes**, SHA-256
  `c29f73f861cebcfc542d5705d28d691b9fe51edda066b5358dc20601c628850d`.

## Deployment status

Publication details will be appended after the exact commit is deployed and
verified against GitHub Pages.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-701 --page 340 --first-row 46 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-701-main --page 341 --first-row 1 --last-row 22
python3 -m oss_research research --source cia --batch batch-701 --max-queries 1
python3 -m oss_research research --source cia --batch batch-701-main --max-queries 22
python3 -m oss_research research --source loc --batch batch-701 --max-queries 1
python3 -m oss_research research --source loc --batch batch-701-main --max-queries 22
python3 scripts/inspect_loc_candidates.py --batch batch-701-main --max-candidates 12 --delay 3.2
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch701.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages340-341-nevada-newman-review_batch-701_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 341, row 23. No API key, raw API
response, full service number, copyrighted page image, unrelated Army coded
occupation, street address, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
