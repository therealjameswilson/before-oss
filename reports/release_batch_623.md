# Batch 623 release status - pages 301-310 and identity review

Date: 2026-09-21 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 301-310 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match. Five pages and
**230** rows were new to the complete-page ledger; visual review now covers
**255/522 pages** and **11,696/23,978 rows**. Of those rows, **11,664** match
the extraction and **32** retain reviewed corrections.

Twenty-two bounded queues were assigned for **454** newly owned people. The
page-301 Library of Congress passes completed **45** live searches and returned
**48** discovery candidates. Item-level OCR review rejected every candidate as
a surname-only occurrence, inaccessible page, distinct namesake, minimally
identified occurrence, postwar material, or text without usable exact-name
context. No employer claim was added and no raw response was retained.

Eighteen pre-existing official Army bulk candidates were reviewed. Sixteen
were accepted as identity-only crosswalks where the full indexed name and a
nonshared protected identifier agree. Charles Maxwell remains `probable`
because the official bulk surname is printed `MAXWELC`; Erwin Mauss remains
`conflicting` because the same protected identifier points to the materially
different bulk name Stephen Z Krzyzaniak. Army occupation codes were not
translated into employers or immediate affiliations.

Eighteen same-name, spelling-variant, or protected-identifier groups covering
**38 people** were reviewed without an unsupported merge. Existing Frederick
Mayer and Robert Mackay / McCay decisions remain authoritative, and already
linked exact duplicate rows remain linked. Public duplicate-group labels are
non-identifying.

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
| Visually audited extraction | 11,696 / 23,978 rows; 255 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,467 (31.1918%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,298 (26.3085%) |
| Not started | 16,436 |
| Possible duplicate groups | 488 |
| Conflicts | 157 |
| Attempts or plans | 12,525 |
| Claims by confidence | confirmed 1,311; high 1,898; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,045 / 2,372 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 120;
`documented_prewar_employer_found` 118; `in_progress` 1,379;
`needs_identity_review` 395; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,436;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,842
sources, and 4,711 claims. Full-index historical research remains unfinished.

## Local verification

A clean tracked-only worktree passed the complete local release suite:

- **128/128** Python unit, parser, schema, normalization, privacy, adapter,
  review-import, and export tests passed, together with **75** parameterized
  subtests.
- `validate-ingest` passed every extraction invariant; SQLite `quick_check`
  returned `ok` and there were **0** foreign-key errors.
- The deterministic **200-profile** stratified audit passed all **7/7**
  structural and evidence checks.
- Astro completed with **0 errors, 0 warnings, and 0 hints**, generating
  **24,681 HTML pages** and **24,753 total artifacts**.
- The bounded Playwright release suite passed **93/93** tests: **24** Batch
  623 checks, **33** core-route checks, **6** analysis checks, and **30**
  accessibility checks. The oil-company category passed its dedicated tests
  in all three viewports, and axe reported no serious or critical violations.
- All internal links resolved across **24,681** HTML files; **50,236** unique
  external URLs were inventoried for the separate live-source process.
- The public-identifier audit examined **12,926** normalized identifiers,
  **120** formatted variants, and **24,753** artifacts, finding **0** aggregate
  false positives, **0** manifest-size false positives, and **0** unexpected
  boundary matches.
- The checked-in public manifest covers **67 assets** and **98,078,272 bytes**
  with SHA-256
  `6324284958d9f3d3063bdb6071a7c2885ad72e023314e50bf40a174dee4f5d95`.
- Two independent clean production builds were byte-identical: **24,753**
  files, **294,294,255** bytes, tree SHA-256
  `7a432fb1b954e002c70cd2fe9ed11660e7127c5faad8a92cc662ebc89dedc301`.

## Deployment

Pull request [#347](https://github.com/therealjameswilson/before-oss/pull/347)
passed its required test workflow and was merged to `main` as commit
`28f05bc5fba14177e94b0989d6b7ef1535361ba6`.

The post-merge
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35629550689)
passed in 4m16s, including the checked-in manifest and public-identifier audits.
The corresponding
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35629550612)
also passed and deployed the site.

An unauthenticated verifier then resolved the live release to the exact merge
commit and checked **8** required core routes, all **26** paginated source
register routes, **54** directly affected profiles, and all **67**
manifest-listed assets. It verified **98,078,272 bytes** with manifest SHA-256
`6324284958d9f3d3063bdb6071a7c2885ad72e023314e50bf40a174dee4f5d95`.
The public release is available at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages301-310_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch623.csv
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-21_batch623.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages301-310-identity-review_batch-623_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The exact page-batch assignment commands and first unsearched queue are in
`research/batch-623-progress.md`. No API key, raw API response, full service
number, or private reviewer note is committed or published.
