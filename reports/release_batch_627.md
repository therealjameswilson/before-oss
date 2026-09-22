# Batch 627 release status - pages 341-350 and Mazzone-McBride research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 341-350 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match. Pages 345 and 349
already had complete review, so this replay adds eight pages and **368** rows
to the complete-page ledger. Visual review now covers **286/522 pages** and
**13,122/23,978 rows**. Of those rows, **13,090** match the extraction and
**32** retain reviewed corrections.

The complete page-303 `Mazzone` through `John J. McBride` queue contained
**23** people. Its Library of Congress pass completed **23** live exact-name
searches and returned **7** discovery candidates. Every candidate was
inspected in official item-level OCR context and the bounded full-text
fallback. The items concerned George A. McAdams rather than indexed George F.;
George Warren and George W. McBride rather than indexed George J.; and John
P., John S., or John E. McBride rather than indexed John J. All seven were
rejected because the initials conflict and no corroborating identifier
supports a match. No employer claim was added and no raw Library of Congress
response was retained.

No pre-existing official Army bulk crosswalk was available for this queue.
All 23 people remain `in_progress` with saved next actions; this is
research-attempt progress, not completion of the minimum research protocol.

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
| Visually audited extraction | 13,122 / 23,978 rows; 286 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,534 (31.4717%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,298 (26.3085%) |
| Not started | 16,370 |
| Possible duplicate groups | 488 |
| Conflicts | 157 |
| Attempts or plans | 12,592 |
| Claims by confidence | confirmed 1,311; high 1,898; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,045 / 2,372 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 120;
`documented_prewar_employer_found` 118; `in_progress` 1,446;
`needs_identity_review` 394; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,370;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,842
sources, and 4,711 claims. Full-index historical research remains unfinished.

## Local verification

A clean tracked-only worktree passed the complete local release suite:

- **132/132** Python unit, parser, schema, normalization, privacy, adapter,
  review-import, and export tests passed, together with **75** parameterized
  subtests.
- `validate-ingest` passed every extraction invariant; SQLite `quick_check`
  returned `ok` and there were **0** foreign-key errors.
- The deterministic **200-profile** stratified audit passed all **7/7**
  structural and evidence checks.
- Astro completed with **0 errors, 0 warnings, and 0 hints**.
- The bounded Playwright release suite passed **81/81** tests: **12** Batch
  627 checks, **33** core-route checks, **6** analysis checks, and **30**
  accessibility checks. Axe reported no serious or critical violations.
- All internal links resolved across **24,681** HTML files; **50,236** unique
  external URLs were inventoried for the separate live-source process.
- The public-identifier audit examined **12,926** normalized identifiers,
  **120** formatted variants, and **24,753** artifacts, finding **0** aggregate
  false positives, **0** manifest-size false positives, and **0** unexpected
  boundary matches.
- The checked-in public manifest covers **67 assets** and **98,099,730 bytes**
  with SHA-256
  `88a11b44322810c8a5c1f44f97314ac831a715286ab485e253107fda1ae7a8d6`.
- Two independent clean production builds were byte-identical: **24,753**
  files, **294,327,659** bytes, tree SHA-256
  `48f2cb51838ca5de3e8f9102300b8b6ab73ab542eea8a4b1f5b08defdb42facd`.

## Deployment

Pending exact-commit CI, merge, Pages deployment, and unauthenticated live
verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages341-350_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch627.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch627b.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch627c.csv
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

Continue with:

```sh
python3 -m oss_research research --source loc --batch page-303-mcbride-william-mccann-richard-b623 --max-queries 10 --resume
```

No API key, raw API response, full service number, or private reviewer note is
committed or published.
