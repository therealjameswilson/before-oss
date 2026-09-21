# Batch 621 release status - pages 281-290 and variant review

Date: 2026-09-21 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 281-290 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match; no new correction
was needed. Because page 281 had already received parser-warning QA, the
complete-page ledger advances by nine pages and **414** rows to **242/522
pages** and **11,098/23,978 rows**, leaving **12,880** rows.

Twelve possible-duplicate, spelling-variant, or identifier-conflict groups
covering 27 people were reviewed without an unsupported merge. Twenty-four
people remain ambiguous with high archival priority. Patsy W Loconto, the PFC
Max Loeb entry, and Robert D Loeb remain separate conflicts with critical
priority because the index repeats one private identifier beside materially
different names. Public group labels are non-identifying.

A bounded Library of Congress pass completed 46 page-281 searches. All 13
discovery candidates were rejected after contextual review. Four affected
people remain `candidate_found` because other Army or duplicate-person leads
still require review; four whose only candidate was rejected returned to
`in_progress`. No employer claim was added, and no authenticated NARA request
was made.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 11,098 / 23,978 rows; 242 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,376 (30.8116%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,237 (26.0537%) |
| Not started | 16,563 |
| Possible duplicate groups | 476 |
| Conflicts | 146 |
| Attempts or plans | 12,434 |
| Claims by confidence | confirmed 1,311; high 1,898; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,045 / 2,372 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 117;
`documented_prewar_employer_found` 118; `in_progress` 1,291;
`needs_identity_review` 359; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,563;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,842
sources, and 4,711 claims. The oil-company category remains a supported,
incomplete evidence set of seven people across nine companies. Full-index
historical research remains unfinished.

## Local verification

Pending the tracked-only release validation suite.

## Deployment

Pending commit, pull request, required checks, merge, Pages deployment, and
unauthenticated verification of the exact public artifact.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages281-290_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch621.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages281-290-duplicate-review_batch-621_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The exact page-batch assignment commands are recorded in
`research/batch-621-progress.md`. No API key, raw API response, full service
number, or private reviewer note is committed or published.
