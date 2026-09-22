# Batch 632 release status - pages 391-400 and McConaughy-McCormick research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 391-400 were compared
against SQLite at 180 dpi. Pages 396, 397, and 398 retain earlier authoritative
corrected decisions; the other seven pages match the current extraction. This
adds seven pages and 322 rows to the complete-page ledger. Visual review now
covers **328/522 pages** and **15,054/23,978 rows**. Of those rows, **15,022**
match the extraction and **32** retain reviewed corrections.

The complete page-305 `James L. Dr. McConaughy` through `Charles H.
McCormick` queue contained 23 people. Its Library of Congress pass saved one
live attempt per person and returned 11 discovery candidates. Every candidate
was inspected in official item-level OCR context and rejected as a conflicting
initial, unrelated OCR collision, non-person vessel reference, insufficient
common-name match, or postwar namesake. No newspaper identity, occupation,
affiliation, or employer claim was retained.

Four official Army identity candidates were accepted at high confidence on
nonshared protected identifiers and strong name agreement. The resulting
profiles qualify the McConnaughe/McConnaughey, Wallack/Hallack, and omitted-
middle-initial discrepancies; William M. McCormack agrees after fixed-width
surname-spacing normalization. The indexed display names remain unchanged.
Army grade and occupation codes were not converted into employers or
predecessor affiliations. The three Alice M. McCool rows remain separate
ambiguous entities pending Box 500 review.

The final queue state is 20 `in_progress` and three
`needs_identity_review`. This is research-attempt progress, not completion of
the minimum research protocol.

The featured oil-company category remains prominently available in the top
navigation, near the top of the home page, and above the personnel-directory
filters. It lists the current evidence-scoped set of **seven people** across
**nine historically named companies**. It includes only cited employment or
self-employment relationships; qualified findings are labeled and mere text
matches or professional representation are excluded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 15,054 / 23,978 rows; 328 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,652 (31.9646%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,300 (26.3169%) |
| Not started | 16,271 |
| Possible duplicate groups | 488 |
| Conflicts | 159 |
| Attempts or plans | 12,722 |
| Claims by confidence | confirmed 1,311; high 1,912; medium 1,374; low 187; conflicting 133 |
| Citation records / unique source documents | 5,054 / 2,378 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 120;
`documented_prewar_employer_found` 118; `in_progress` 1,541;
`needs_identity_review` 398; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,271;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,847
sources, and 4,726 claims. Full-index historical research remains unfinished.

## Local verification

The isolated tracked-only candidate passed all local release gates:

- 132/132 Python unit tests;
- all seven checks in the 200-profile stratified structural audit (not a
  substitute for the required independent manual historical audit);
- Astro diagnostics across 263 source files with zero errors, warnings, or
  hints, followed by a successful 24,681-page static build;
- 12/12 focused Batch 632 browser checks and the complete bounded **81/81**
  desktop, phone, tablet, analysis, and axe accessibility suite;
- 24,681 internal HTML pages checked with every internal link resolving;
- 12,926 normalized identifiers and 120 formatted variants scanned across
  24,753 public artifacts with zero unexpected full-number boundary matches;
- all 67 public-manifest assets verified, totaling 98,197,781 bytes, at
  manifest SHA-256
  `d3e019f8766a29b091b41914b76244ef71f608f6661f0fb6816587261b196701`;
- two consecutive clean builds reproduced the same output-tree SHA-256
  `f7b4db300268a0d4f962d60719333e7773cc7706bfac83d24c2225d3d9a6d010`.

## Deployment

Pending pull request, main-branch CI, GitHub Pages deployment, and exact live-
artifact verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages391-400_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch632.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch632.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page305-mcconaughy-mccormick-review_batch-632_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published.
