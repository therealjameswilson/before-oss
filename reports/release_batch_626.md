# Batch 626 release status - pages 331-340 and Mayes-Mazzarini research

Date: 2026-09-21 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 331-340 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match. Pages 336, 337,
and 339 already had correction-complete review, so this replay adds seven
pages and **322** rows to the complete-page ledger. Visual review now covers
**278/522 pages** and **12,754/23,978 rows**. Of those rows, **12,722** match
the extraction and **32** retain reviewed corrections.

The complete page-302 `Mayes` through `Mazzarini` queue contained **23**
people. Its Library of Congress pass completed **23** live exact-name searches
and returned **11** discovery candidates. Every candidate was inspected in
official item-level OCR context and the bounded full-text fallback. Nine
candidates supplied no usable exact-name context; three of those were postwar.
The remaining contextual hits concerned newborn William James Mayhew rather
than indexed Major William A. Mayhew and Thomas G. Mays rather than indexed
Thomas J. Mays. All 11 candidates were rejected. No employer claim was added
and no raw Library of Congress response was retained.

Five pre-existing official Army bulk candidates were accepted as
identity-only crosswalks. John T. Mayher, Alex Mazel, Dana G. Mazerolle,
Chester John Mazur, and Gesualdo J. Mazza agree with the index in full name
and a nonshared protected identifier, so their identity status is now
`high_confidence`. Army grades and occupation codes were not translated into
employers, occupations, or immediate affiliations. All 23 people remain
`in_progress` with saved next actions; this is research-attempt progress, not
completion of the minimum research protocol.

An exhausted Library of Congress read timeout exposed a batch-control defect:
the adapter correctly retried and audited the request, but the scheduler
propagated the exception as a traceback. The scheduler now writes a durable
`error` attempt containing only the exception class, leaves the person
resumable, stops the bounded run without probing every remaining person, and
never treats the failure as a negative source finding. The original request
subsequently succeeded through the ordinary `--resume` path. A scheduler-level
regression test confirms the returned summary, redaction, and resume state.

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
| Visually audited extraction | 12,754 / 23,978 rows; 278 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,511 (31.3756%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,298 (26.3085%) |
| Not started | 16,392 |
| Possible duplicate groups | 488 |
| Conflicts | 157 |
| Attempts or plans | 12,569 |
| Claims by confidence | confirmed 1,311; high 1,898; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,045 / 2,372 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 120;
`documented_prewar_employer_found` 118; `in_progress` 1,423;
`needs_identity_review` 395; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,392;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,842
sources, and 4,711 claims. Full-index historical research remains unfinished.

## Local verification

The working-tree verification completed before publication:

- **132** Python unit, parser, schema, normalization, privacy, adapter,
  review-import, and export tests passed; the final clean release run is
  recorded below when available.
- `validate-ingest` passed every extraction invariant; SQLite `quick_check`
  returned `ok` and there were **0** foreign-key errors.
- The deterministic **200-profile** stratified audit passed all **7/7**
  structural and evidence checks.
- Astro completed with **0 errors, 0 warnings, and 0 hints**.
- The bounded Playwright release suite passed **81/81** tests: **12** Batch
  626 checks, **33** core-route checks, **6** analysis checks, and **30**
  accessibility checks. Axe reported no serious or critical violations.
- The checked-in public manifest covers **67 assets** and **98,093,188 bytes**
  with SHA-256
  `cd9f63fac6cc4750b43821377935897cef4b63eeb9e4ae5468f5b7650382e0c3`.

Tracked-only build, link, public-identifier, deterministic-tree, CI, and live
deployment evidence will replace this paragraph after the release commit is
tested and published.

## Deployment

Pending exact-commit CI, merge, Pages deployment, and unauthenticated live
verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages331-340_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch626.csv
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-21_batch626.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page302-mayes-mayo-identity-review_batch-626_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch626b.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch626c.csv
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

Continue with:

```sh
python3 -m oss_research research --source loc --batch page-303-mazzone-mcbride-john-b623 --max-queries 10 --resume
```

No API key, raw API response, full service number, or private reviewer note is
committed or published.
