# Batch 652 release status - pages 75-84 and Merrick-Meslin research

Research date: 2026-09-23 America/New_York. This report records the reviewed
research, extraction, and local release-verification state. Production
deployment evidence is added after the reviewed release merges.

## Historical and extraction work

All **470** printed rows on original NARA PDF pages 75-84 were compared against
the extraction at 180 dpi. Page 77 was already covered; the other nine pages
and **414** rows received their first complete visual comparison. Every row
matches. Complete-page visual review now covers **500/522 pages** and
**22,966/23,978 rows**: **22,934** match the extraction, **32** retain reviewed
corrections, and **1,012** remain unaudited. All PDF pages remain represented,
every parser warning is resolved, and SQLite integrity and foreign-key checks
pass.

The page-317 `Ray D. Merrick` through `Jerome Meslin` queue contains 22 source
rows and 22 cautious people. Every person received staged source-specific work
and a saved reviewed outcome. The bounded LoC run produced seven candidates;
all were rejected after page-context review. No authenticated NARA Catalog
request was made.

Frank C. Mesle now has a high-confidence identity bridge and a separated,
qualified chronology: University of Iowa as prewar student status, professional
Scouting in Camden as his strongly date-bounded last civilian work, and the
Corps of Engineers as his probable immediate military predecessor to OSS
training. The local Scout council and exact military transfer sequence remain
unknown, so neither medium-confidence claim is overstated.

Seven other people have high-confidence Army identity bridges without inferred
employers. Lawrencee N. Merritt, the two Charles Mersereau/Meserau rows, and
William L. Merritts remain conflicting. F Nevill Merritt's unusual printed
field order remains intact pending direct file evidence.

The cohort ends with 17 `in_progress`, four `conflicting_sources`, and one
`documented_prewar_employer_found` status. Identity statuses are eight
`high_confidence`, ten `unresolved`, and four `conflicting`. The evidence bundle
adds 15 claims: nine high, two medium, and four conflicting. The oil-company
category remains prominently available at the top of the personnel directory
and remains limited to the supported set of **seven people across nine
historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 22,966 / 23,978 rows; 500 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,097 (33.8235%) |
| People with confirmed/high employer evidence | 288 (1.2031%) |
| People with confirmed/high affiliation evidence | 643 (2.6860%) |
| Archival-review dispositions assessed | 6,553 (27.3737%) |
| Not started | 15,837 |
| Possible duplicate groups | 492 |
| Conflicts | 189 |
| Attempts or plans | 13,895 |
| Claims by confidence | confirmed 1,311; high 2,065; medium 1,406; low 189; conflicting 164 |
| Citation records / unique source documents | 5,145 / 2,445 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 148;
`documented_prewar_employer_found` 122; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,837;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 264.

The public projection contains **2,263** published affiliations, **740**
organizations, **3,935** public sources, and **4,942** published claims.
Full-index historical research remains unfinished.

## Local verification

The clean pull-request release candidate passes:

- **133/133** Python unit tests;
- **90/90** Playwright checks: 21 Batch 652, 33 core release, six analysis,
  and 30 accessibility checks across desktop, phone, and tablet;
- Astro diagnostics across **283** source files with zero errors, warnings, or
  hints;
- all internal links across **24,714 HTML files**, with **50,313** unique
  external URLs inventoried for the separate live check;
- public-identifier redaction across **24,786** build artifacts with zero
  aggregate false positives, manifest-size false positives, or unexpected
  boundary matches; and
- manifest verification of **67** projected assets totaling **99,489,263
  bytes**, manifest SHA-256
  `433fa188f7df74b8165fe8a013fd16af8bde969132a29d823134746c0fa91da4`.

The first clean workflow exposed only a capitalization mismatch in the new
temporal-badge assertion: the page correctly rendered `probable immediate`
while the test expected an initial capital. The assertion was corrected, and
the complete release suite then passed. Two isolated local Node runs had
stalled before Astro emitted a page or diagnostic and were stopped without
modifying the release tree; the independent clean build supplies the completed
site and browser verification.

User-owned Finder-style ` 2` files and local SQLite sidecars remain untouched
and are excluded from the release.

## Deployment

The reviewed research release merged through
[PR #405](https://github.com/therealjameswilson/before-oss/pull/405) as commit
`2af4aeb94100eb0d172f65bcb718a975fc882e1b`. The corrected pull-request test
passed in 4m27s. The post-merge
[main test](https://github.com/therealjameswilson/before-oss/actions/runs/35870513529)
passed in 4m12s, including the full release suite, source-PDF rebuild, and
public-identifier audit. The
[Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35870513766)
built successfully in 1m27s and deployed successfully in 22s.

Read-only verification of the live Pages site confirmed the updated exact
coverage totals, the oil-company category before the directory filters, all
seven supported names on both the personnel and dedicated category pages, and
Frank C. Mesle's qualified Corps of Engineers, professional Scouting, and
University of Iowa chronology with its claim-level citations.

The workflows emitted non-blocking platform notices about Actions' Node 20
transition and the future `ubuntu-latest` image migration; no project test or
deployment step failed in the final runs.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages75-84_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch652.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-23_batch652.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page317-merrick-meslin-review_batch-652_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published. No authenticated NARA Catalog
request was made.
