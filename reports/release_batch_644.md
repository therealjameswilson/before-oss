# Batch 644 release status - pages 511-520 and McPadden-McVannel research

Date: 2026-09-22 UTC. This report records the audited tracked-only local
release candidate. Deployment fields will be finalized from the exact merged
revision after release.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 511-520 were compared
against SQLite at 180 dpi. Pages 517-520 were already present in the
complete-page ledger. Every row matches the current extraction. Complete-page
visual review now covers **430/522 pages** and **19,746/23,978 rows**:
**19,714** match the extraction, **32** retain reviewed corrections, and
**4,232** remain unaudited.

The page-313 `John F. McPadden` through `Donald S. McVannel` queue contains 23
source rows and 23 cautious people. All 23 received exact-name OSS/employment
discovery review. The bounded LoC request timed out and CIA correctly stopped
at robots policy; both access outcomes remain explicit. Targeted discovery
returned no defensible employer evidence, and search snippets or unrelated
namesakes were not promoted into claims.

Six official Army or duplicate-boundary candidates received decisions. Exact
normalized names and nonshared protected identifiers support high-confidence
crosswalks for Robert E. McPeek, James F. McPoil, Robert C. McQueen, and
Donald S. McVannel. Thomas E. McParland and Thomas E. McPharland remain a
probable duplicate pair because adjacent Box 512 rows share a protected
identifier but differ in spelling and rank occupancy. Joann W. McQuiston and
Joanne W. Mcquiston remain separate probable entities because close spelling
and Box 513 adjacency are not enough to merge their jackets.

The final queue state is 19 `in_progress` and four
`needs_identity_review`. All six stored candidates have decisions: four
accepted and two probable. Four high-confidence and four qualified
medium-confidence identity claims were added. No employer or affiliation
claim was added. Army grades, entry dates, and occupation codes remain
identity context rather than employer evidence.

The clean rebuild audit also closed two pre-existing resumability gaps. The
rebuild now imports every tracked page-review bundle instead of only the
original random-audit file, and its sanitized adapter checkpoint now restores
all **7,364** Army bulk identity candidates plus current queue dispositions
without exporting full protected identifiers. A staged-files-only rebuild
reconstructed all **10,310** candidate records and reproduced every public
JSON asset byte-for-byte. Guarded display and organization-normalization
decisions make the few previously order-dependent fields deterministic.

The oil-company category remains prominently available in the site navigation,
home page, and personnel directory. It lists the current evidence-scoped set of
**seven people** across **nine historically named companies** and excludes
mere text matches and unsupported candidates.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 19,746 / 23,978 rows; 430 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,922 (33.0924%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,380 (26.6511%) |
| Not started | 16,012 |
| Possible duplicate groups | 490 |
| Conflicts | 170 |
| Attempts or plans | 13,147 |
| Claims by confidence | confirmed 1,311; high 1,973; medium 1,384; low 187; conflicting 145 |
| Citation records / unique source documents | 5,080 / 2,391 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 131;
`documented_prewar_employer_found` 118; `in_progress` 1,779;
`needs_identity_review` 408; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,012;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,873
sources, and 4,809 claims. Full-index historical research remains unfinished.

## Local verification

The tracked-only release candidate passed:

- **133/133** Python unit tests;
- Astro diagnostics across **275** source files with zero errors, warnings, or
  hints;
- **84/84** bounded Playwright release checks: 15 Batch 644, 33 core-route and
  interaction, six analysis, and 30 accessibility checks across desktop,
  phone, and tablet;
- internal-link validation across **24,681** generated HTML pages;
- public-identifier redaction across **24,753** artifacts, with zero aggregate,
  manifest-size, or unexpected-boundary false positives;
- local manifest verification of **67** projected assets totaling
  **98,609,376 bytes**, manifest SHA-256
  `bcec49ce657102dd9cc45143fa2d0a9f336d76b5d4699d07c2e557a652d9a9ea`;
- two byte-identical production builds: **24,753 files**, **295,131,974 bytes**,
  tree SHA-256
  `fe91db760f6fb8b937e19b22515c352279d0830265ac9ddc0cce99d8ac9e2efb`;
  and
- a staged-files-only reconstruction with **430** visually reviewed pages,
  **19,714** matching rows, **32** corrected rows, **4,232** remaining rows,
  **10,310** candidate records, and public JSON identical to the release
  projection.

The locked dependency install reported one moderate npm advisory. No package
was upgraded outside the lockfile in this historical-data release.

## Deployment

Pending exact merged revision, CI, GitHub Pages workflow, and live artifact
verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages511-520_2026-09-22.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch644.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page313-mcpadden-mcvannel-review_batch-644_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
