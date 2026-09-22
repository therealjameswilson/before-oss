# Batch 629 release status - pages 361-370 and McCann-McCarthy research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 361-370 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match. This adds ten
pages and 460 rows to the complete-page ledger. Visual review now covers
**305/522 pages** and **13,996/23,978 rows**. Of those rows, **13,964** match
the extraction and **32** retain reviewed corrections.

The complete page-304 `Thomas A. McCann` through `John A. McCarthy` queue
contained **23** people. Its Library of Congress pass completed **23** live
exact-name searches and returned **36** discovery candidates. Every candidate
was inspected in official item-level OCR context and rejected because it was
a different name or initial, was postwar, was only an OCR-adjacent fragment,
or lacked corroborating identity and employment evidence. No employer claim
was added and no raw Library of Congress response was retained.

Seven official Army identity candidates were accepted at high confidence on
matching full or normalized names and nonshared protected identifiers. The
staff-sergeant John F. McCarthy row was distinguished from the adjacent
same-name row by its different identifier. Jack L. McCarary on page 304 and
Jack L. McCrary on page 306 remain separate ambiguous people and probable
duplicates: the index prints the same protected identifier and Box 501 for
both, while the Army fixed-width name supports the McCrary spelling. Original-
jacket examination is still required. Army occupation codes were not converted
into employers.

The final queue state is 19 `in_progress` and four
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
| Visually audited extraction | 13,996 / 23,978 rows; 305 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,580 (31.6638%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,298 (26.3085%) |
| Not started | 16,331 |
| Possible duplicate groups | 488 |
| Conflicts | 158 |
| Attempts or plans | 12,638 |
| Claims by confidence | confirmed 1,311; high 1,898; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,045 / 2,372 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 120;
`documented_prewar_employer_found` 118; `in_progress` 1,485;
`needs_identity_review` 394; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,331;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,842
sources, and 4,711 claims. Full-index historical research remains unfinished.

## Local verification

The clean tracked-only release candidate passed all local gates:

- Python: **132/132** tests passed.
- Playwright: **81/81** release tests passed - 12 Batch 629 profile and
  checkpoint tests, 33 core route/interaction tests, six analysis tests, and
  30 accessibility tests across desktop, phone, and tablet projects.
- Astro: zero errors, warnings, or hints.
- Deterministic build: two successive builds each produced **24,681 HTML
  files**, **24,753 total artifacts**, and **294,353,270 bytes**, with tree
  SHA-256 `532e5b8e3b48487bbfbab4c11b516dff896e47cfa1e8afe4ef58627eea16a108`.
- Link check: all internal links in 24,681 HTML files resolved; **50,236**
  unique external URLs were inventoried for the separate live check.
- Public-identifier audit: 12,926 normalized private identifiers, 120
  formatted variants, and 24,753 artifacts produced zero aggregate false
  positives, zero manifest-size false positives, and zero unexpected boundary
  matches.
- Public-data manifest: **67 assets**, **98,116,180 bytes**, SHA-256
  `7fab817e96b818559a57d3ffedefac163d3aa634a3fb3ac1bce9dfaec44c2034`.
- Ingest validation remained complete, SQLite `quick_check` returned `ok`,
  foreign-key errors remained zero, and the 200-profile stratified audit
  retained all seven checks.

## Deployment

Pending pull-request CI, merge, GitHub Pages deployment, and unauthenticated
exact-commit verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages361-370_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch629.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch629b.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch629c.csv
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-22_batch629.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page304-mccann-mccarthy-identity-review_batch-629_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

Continue with:

```sh
python3 -m oss_research research --source loc --batch page-304-mccarthy-joseph-mcclelian-b623 --max-queries 10 --resume
```

No API key, raw API response, full service number, or private reviewer note is
committed or published.
