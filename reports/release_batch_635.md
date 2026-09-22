# Batch 635 release status - pages 421-430 and McDonald-McDowell research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 421-430 were compared
against SQLite at 180 dpi. Every page matches the current extraction. Because
page 424 was already part of the deterministic random audit, the durable ledger
rises by nine pages and 414 rows to **356/522 pages** and **16,342/23,978
rows**. Of those rows, **16,310** match the extraction and **32** retain
reviewed corrections; **7,636** rows remain for complete visual comparison.

The complete page-307 `Mary B. McDonald` through `Michael V. McDowell` queue
contained 23 people. Its Library of Congress pass saved at least one live
attempt per person and returned 28 discovery candidates across ten people.
Every candidate was inspected in official item-level context and rejected as a
conflicting-initial, unrelated, contextless, postwar, or insufficiently bridged
name.

Four official Army identity candidates were accepted at high confidence on
nonshared protected identifiers and exact or carefully qualified name
agreement: Michael V. McDowell, Paul J. McDougall, Thomas F. McDonnell, and
William P. McDonough. The indexed display names remain unchanged. The
protected identifiers printed for Raymond W. McDonald and Roy W. McDonald
instead resolve to conflicting Army entries. Neither Army identity nor an
unbridged same-name institutional lead was assigned. Both profiles are marked
`conflicting_sources` pending Box 503 review, while full protected identifiers
and the other Army names remain private.

The two Robert L. McDougal rows remain separate ambiguous entities: one has a
grade without an identifier and the other an identifier without a grade. The
final queue state is 19 `in_progress`, two `needs_identity_review`, and two
`conflicting_sources`. All 34 candidates have review decisions; none remains
unreviewed. This is research-attempt progress, not completion of the minimum
research protocol. No new employer or affiliation claim was made.

The featured oil-company category remains prominently available in the top
navigation, near the top of the home page, and above the personnel-directory
filters. It lists the current evidence-scoped set of **seven people** across
**nine historically named companies**. It includes only cited employment or
self-employment relationships; qualified findings are labeled and mere text
matches are excluded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 16,342 / 23,978 rows; 356 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,721 (32.2528%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,300 (26.3169%) |
| Not started | 16,208 |
| Possible duplicate groups | 488 |
| Conflicts | 163 |
| Attempts or plans | 12,823 |
| Claims by confidence | confirmed 1,311; high 1,924; medium 1,375; low 187; conflicting 137 |
| Citation records / unique source documents | 5,062 / 2,383 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 124;
`documented_prewar_employer_found` 118; `in_progress` 1,599;
`needs_identity_review` 399; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,208;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,855
sources, and 4,743 claims. Full-index historical research remains unfinished.

## Local verification

The exact tracked-only release candidate passed all **132** Python tests and
all **84** bounded browser checks: 15 Batch 635 assertions, 33 core-route
checks, six analysis checks, and 30 axe checks across desktop, phone, and
tablet layouts. The 200-profile stratified structural audit passed all seven
checks; it is not the required independent manual historical audit.

Astro reported zero errors, warnings, or hints across **266** source files and
built **24,681** pages. All internal links resolve across **24,753** artifacts;
**50,238** unique external URLs were inventoried for the separate live check.
The public-identifier audit found zero unexpected full-number boundary matches.
The local verifier matched all **67** manifest assets and **98,292,743** bytes
at manifest SHA-256
`09b86baf7b19ad898317b0a929172baa09e4d66fa9349defe39f998a94881eaa`.
Two consecutive clean builds reproduced production-tree SHA-256
`9ca7eea4a5699d050c71fbf15b4e1dc939b6699577b4ca46c0491745efd68f2a`.
Unrelated user-owned duplicate files were preserved and excluded.

## Deployment

Pull request [#371](https://github.com/therealjameswilson/before-oss/pull/371)
merged to `main` as
`32de0af8be2820f82bc264fff305e84433ea0112` at 2026-09-22 11:30:31 UTC.
The PR test passed in 4m27s. The merged-commit Test workflow
[35721837207](https://github.com/therealjameswilson/before-oss/actions/runs/35721837207)
passed in 4m09s, and Deploy GitHub Pages workflow
[35721837178](https://github.com/therealjameswilson/before-oss/actions/runs/35721837178)
completed successfully (1m24s build and 52s deploy). GitHub emitted
informational Node.js 20 action-runtime deprecation and future Ubuntu runner
migration annotations; no release check failed.

The exact-ref live verifier matched all **67** manifest assets and
**98,292,743** bytes at the local manifest digest, then verified eight core
routes, all 26 source-register pages, and the eight profiles directly affected
by the evidence bundle. Independent public checks returned HTTP 200 for the
home page, the oil-company category, and the affected conflict profile. The
live home page reports **7,721 of 23,939** entities researched (**32.25%**);
the live oil-company page renders exactly **seven** person cards. The Roy W.
McDonald profile publishes the documented conflict while withholding the
unrelated Army name and unbridged institutional lead.

Public site: https://therealjameswilson.github.io/before-oss/

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages421-430_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch635.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch635.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page307-mcdonald-mcdowell-review_batch-635_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
