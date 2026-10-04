# Batch 732 release - Panzarella-Papoulias research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 732 publishes reviewed outcomes for PDF page 356, rows 24-46, from Neal
M Panzarella through Arthur D Papoulias. All 23 printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, grades,
boxes, notes, and locations remain recoverable; protected identifiers remain
private.

Five identities are confirmed by direct official roster evidence and seven
are linked at high confidence through official protected-identifier matches.
The review preserves every relevant anomaly instead of normalizing it away:
Papanu/Papapanu, Papayiannakis/Papayannakis, Papazoglou's first-lieutenant and
captain grades, Papoulias's D/J middle initial, and Silvia/Silvio Papini.

Six Greek Operational Group members receive a qualified 122nd Infantry
Battalion (Separate) pathway. Those relationships are medium-confidence,
probable-immediate military assignments based on a unit recruitment history
plus named roster entries. They are not civilian employers, are excluded from
confirmed/high analytics, and remain subject to individual transfer-order
review.

The shared protected identifier printed for Arthur A Pape and Arthur A Paper
also appears for Arthur A Pope on page 373. The release keeps all three source
rows and people separate, publishes the conflict on each direct profile, and
prioritizes Boxes 583 and 612 for archival comparison.

The 23 page-356 people record 20 `requires_archival_review` and three
`conflicting_sources` outcomes; the linked Pope profile adds a fourth conflict.
Across the 24 reviewed profiles, identity statuses are five confirmed, seven
high-confidence, four conflicting, and eight unresolved. The reviewed bundle
adds six sources, one reused organization, six affiliations, 22 claims, 52
claim-source links, 24 person updates, and 24 consolidated research attempts.
Ten accepted and four conflicting identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,872 (41.2381%) |
| People with confirmed/high employer evidence | 333 (1.3910%) |
| People with confirmed/high affiliation evidence | 743 (3.1037%) |
| Archival-review dispositions assessed | 8,330 (34.7968%) |
| Not started | 14,062 |
| Possible duplicate groups | 523 |
| Conflicts | 327 |
| Attempts or plans | 18,034 |
| Claims by confidence | confirmed 1,378; high 2,929; medium 1,535; low 198; conflicting 289; unresolved 2 |
| Citation records / unique source documents | 5,694 / 2,876 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 284;
`documented_prewar_employer_found` 167; `in_progress` 1,903;
`needs_identity_review` 459; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,156; `not_started` 14,062;
`occupation_only_found` 1,047; `requires_archival_review` 4,026; and
`verified_employer_found` 289.

The public projection contains 2,485 published affiliations, 861
organizations, 4,475 public sources, and 6,124 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Astro diagnostics: 366 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,838 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 732, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,838 HTML files checked; every internal link resolved and
  50,738 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 106,212,025 bytes verified; manifest SHA-256
  `b110062009be8748796e5021b673adc1a88ca0a6300f7b7e76b7f97bceac9354`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,910 public artifacts, and 1,209 candidate substrings checked
  with zero unexpected boundary matches.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Two consecutive production builds reproduced output-tree SHA-256
  `a2e2235d670cd6d18eb31c0f045a8daad74f5f07fc07d18022c5dcb5ca30b8e3`.
* The supported bounded release suite completed cleanly; all retained
  historical batch specifications remain available through the unbounded
  command.

## Publication verification

Pending commit, push, GitHub Actions completion, and immutable live-site
verification.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-732-panzarella-papa --page 356 --first-row 24 --last-row 27
python3 -m oss_research assign-page-batch --batch-name batch-732-papadopoulos-papoulias --page 356 --first-row 29 --last-row 46
python3 -m oss_research assign-page-batch --batch-name batch-732-duplicate-cluster --page 373 --first-row 27 --last-row 27
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch732.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page356-panzarella-papoulias-review_batch-732_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary is PDF page 357, rows 1-23, from Charles A
Papouschek through Jean P Parent. No API key, raw API response, full service
or officer number, copyrighted page image, unrelated Army coded occupation,
street address, modern people-finder record, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
