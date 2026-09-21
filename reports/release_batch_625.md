# Batch 625 release status - pages 321-330 and Mayer research

Date: 2026-09-21 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 321-330 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match. Pages 326 and 330
already had complete review, so this replay adds eight pages and **368** rows
to the complete-page ledger. Visual review now covers **271/522 pages** and
**12,432/23,978 rows**. Of those rows, **12,400** match the extraction and
**32** retain reviewed corrections.

The next unsearched page-302 queue contained **10** people. Its Library of
Congress pass completed **10** live exact-name searches and returned **12**
discovery candidates. Every candidate was inspected in official item-level
OCR context. Eleven had no matching exact-name context in the complete OCR;
the remaining item was a classified advertisement for Hofmayer's Bureau,
not Rene A. Mayer. All 12 were rejected as context-free hits, postwar or
temporally remote material, or an unrelated OCR substring. No employer claim
was added and no raw Library of Congress response was retained.

One pre-existing official Army bulk candidate was accepted as an identity-only
crosswalk. Lawrence J. Mayer agrees with the index in full name and a
nonshared protected identifier, so the identity is now `high_confidence`.
The Army grade and occupation code were not translated into an employer,
occupation, or immediate affiliation. All ten people remain `in_progress`
with saved next actions; this is research-attempt progress, not completion of
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
| Visually audited extraction | 12,432 / 23,978 rows; 271 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,488 (31.2795%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,298 (26.3085%) |
| Not started | 16,415 |
| Possible duplicate groups | 488 |
| Conflicts | 157 |
| Attempts or plans | 12,546 |
| Claims by confidence | confirmed 1,311; high 1,898; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,045 / 2,372 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 120;
`documented_prewar_employer_found` 118; `in_progress` 1,400;
`needs_identity_review` 395; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,415;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,842
sources, and 4,711 claims. Full-index historical research remains unfinished.

## Local verification

A clean tracked-only worktree passed the complete local release suite:

- **130/130** Python unit, parser, schema, normalization, privacy, adapter,
  review-import, and export tests passed, together with **75** parameterized
  subtests.
- `validate-ingest` passed every extraction invariant; SQLite `quick_check`
  returned `ok` and there were **0** foreign-key errors.
- The deterministic **200-profile** stratified audit passed all **7/7**
  structural and evidence checks.
- Astro completed with **0 errors, 0 warnings, and 0 hints**, generating
  **24,681 HTML pages** and **24,753 total artifacts**.
- The bounded Playwright release suite passed **78/78** tests: **9** Batch 625
  checks, **33** core-route checks, **6** analysis checks, and **30**
  accessibility checks. Axe reported no serious or critical violations.
- All internal links resolved across **24,681** HTML files; **50,236** unique
  external URLs were inventoried for the separate live-source process.
- The public-identifier audit examined **12,926** normalized identifiers,
  **120** formatted variants, and **24,753** artifacts, finding **0** aggregate
  false positives, **0** manifest-size false positives, and **0** unexpected
  boundary matches.
- The checked-in public manifest covers **67 assets** and **98,085,125 bytes**
  with SHA-256
  `25f433da14b511b864843d0064a8c96589ba52bc8ee9040e874a470aee60040e`.
- Two independent clean production builds were byte-identical: **24,753**
  files, **294,304,984** bytes, tree SHA-256
  `ce439160e442f69b2061aad34c516535c660e5d6e36ba401b5fb1cc51680b86a`.

## Deployment

Pull request [#351](https://github.com/therealjameswilson/before-oss/pull/351)
passed its required test workflow in 4m22s and was merged to `main` as commit
`9e0bbcee29099ae0227d4f69cae510e5dc04e593`.

The post-merge
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35642026688)
passed in 3m32s, including the checked-in manifest and public-identifier audit.
The corresponding
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35642026752)
also passed and deployed the site.

An unauthenticated verifier then resolved the live release to the exact merge
commit and checked **8** required core routes, all **26** paginated source
register routes, the identity-evidence profile, and all **67** manifest-listed
assets. It verified **98,085,125 bytes** with manifest SHA-256
`25f433da14b511b864843d0064a8c96589ba52bc8ee9040e874a470aee60040e`.
A separate bounded live check loaded all **10** directly affected profile URLs
and confirmed their rendered main content and exact public person identifiers.
The public release is available at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages321-330_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch625.csv
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-21_batch625.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page302-mayer-identity-review_batch-625_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The exact next queue is recorded in `research/batch-625-progress.md`. No API
key, raw API response, full service number, or private reviewer note is
committed or published.
