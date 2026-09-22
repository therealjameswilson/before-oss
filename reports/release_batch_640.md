# Batch 640 release status - pages 471-480 and McGuire-McIntosh research

Date: 2026-09-22 UTC. This report records the audited tracked-only local
release candidate. Exact-ref public verification will be added after merge.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 471-480 were compared
against SQLite; page 472 received an additional 300-dpi check. Every page
matches the current extraction. The durable visual ledger rises to **398/522
pages** and **18,274/23,978 rows**: **18,242** match the extraction, **32**
retain reviewed corrections, and **5,704** remain unaudited.

The page-310 `James A. McGuire` through `Henry D. McIntosh` queue contains 23
source rows and 23 people. A Library of Congress attempt is saved for every
person. Sixteen discovery candidates across six people were inspected and
rejected; none reliably bridge the candidate to the indexed person or establish
a pre-OSS affiliation. Erie McIlhenny's LoC attempt records an explicit timeout
and access blockage, not a negative result.

Four Army candidates received review decisions. Nonshared protected identifiers
support high-confidence identity crosswalks for Donald E. McInnis and William
T. McGuire. Loughlin G. McHugh remains conflicting because the Army source has
a different middle initial. Thomas F. McGuire remains conflicting because the
protected identifier instead points to Robert N. Durbin. Full identifiers stay
private, and no Army grade or occupation code was treated as employer evidence.

The two adjacent Carolyn McIntosh index rows remain separate: Box 508 lists
Carolyn S. McIntosh, while Box 507 lists Carolyn McIntosh as CAF-2. The final
queue state is 21 `in_progress` and two `conflicting_sources`. All 20 candidates
have decisions: two accepted, two conflicting, and 16 rejected. This is
research-attempt progress, not completion of the minimum research protocol. No
new employer or affiliation claim was made.

The oil-company category remains prominently available in the site navigation,
home page, and personnel directory. It lists the current evidence-scoped set of
**seven people** across **nine historically named companies** and excludes
mere text matches and unsupported candidates.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 18,274 / 23,978 rows; 398 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,832 (32.7165%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,331 (26.4464%) |
| Not started | 16,102 |
| Possible duplicate groups | 488 |
| Conflicts | 167 |
| Attempts or plans | 12,993 |
| Claims by confidence | confirmed 1,311; high 1,951; medium 1,375; low 187; conflicting 142 |
| Citation records / unique source documents | 5,072 / 2,388 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 128;
`documented_prewar_employer_found` 118; `in_progress` 1,701;
`needs_identity_review` 399; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,102;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,865
sources, and 4,775 claims. Full-index historical research remains unfinished.

## Local verification

The isolated tracked-only candidate passes all local release gates:

- **132/132** Python unit tests;
- **87/87** browser checks across desktop, phone, and tablet: 18 Batch 640,
  33 core-route, six analysis, and 30 accessibility/axe checks;
- Astro check with zero errors, warnings, or hints across **271** source files;
- **24,681** static HTML pages and **24,753** total artifacts;
- every internal link resolved, with **50,238** unique external URLs
  inventoried for the separate live check;
- all **67** manifest-listed assets matched, totaling **98,456,942** bytes at
  manifest SHA-256
  `b22f0f79a1f391f962bd71bc6888d90aeb60f26e63ac45559aa5df2b41ce59f2`;
- the public-identifier audit compared **12,926** normalized identifiers and
  **120** formatted variants with zero aggregate false positives, manifest-size
  false positives, or unexpected full-number boundary matches;
- two clean builds reproduced production-tree SHA-256
  `1cdac5b14a7932dd5252e7c284ed06c464fb8e88ed0c64bb1927d512d20f807d`
  across 24,753 files and 294,888,755 bytes.

Unrelated user-owned duplicate files remain preserved and excluded from the
tracked-only verification.

## Deployment

Pending pull-request review, merge, GitHub Actions, Pages deployment, and
exact-ref public verification.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages471-480_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch640.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch640.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page310-mcguire-mcintosh-review_batch-640_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
