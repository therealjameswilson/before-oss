# Batch 656 release - Mezoff-Mielziner research

Research and release date: 2026-09-23 America/New_York.

## Historical work

The page-319 `Eleanor E. Mezoff` through `Jo Mielziner` queue contains 22
source rows and 22 cautious people. Every person now has a saved reviewed
outcome. Jerry G. Mican's Army-to-OSS pathway, Roman Michalowski's
Interallied Information Center and Army chronology, Charles A. Micaud's
Bowdoin employment, Alfredo Michelagnoli's qualified Allied pathway, and Jo
Mielziner's Army Air Forces camouflage work are modeled without conflating
military assignment, employer, occupation, and student or professional status.

Gimino Michelangelo's official Army-name conflict remains unresolved. I.
Michel and Michel M. Ivy remain separate people despite a duplicated protected
identifier. Six other Army crosswalks are identity evidence only, not inferred
employers. All 13 generated candidates received explicit decisions.

The cohort ends with 15 `requires_archival_review`, three
`occupation_only_found`, two `documented_prewar_employer_found`, and two
`conflicting_sources` statuses. Identity statuses are two `confirmed`, eight
`high_confidence`, two `conflicting`, and ten `unresolved`. The bundle adds 22
claims: three confirmed, 16 high, one medium, and two conflicting.

The top oil-company category remains evidence-scoped to **eight people across
ten historically named companies**. No occupation-only or military-assignment
finding from this batch is counted as oil-company employment.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,184 (34.1869%) |
| People with confirmed/high employer evidence | 293 (1.2239%) |
| People with confirmed/high affiliation evidence | 650 (2.7152%) |
| Archival-review dispositions assessed | 6,640 (27.7372%) |
| Not started | 15,750 |
| Possible duplicate groups | 498 |
| Conflicts | 197 |
| Attempts or plans | 14,230 |
| Claims by confidence | confirmed 1,315; high 2,108; medium 1,416; low 189; conflicting 172 |
| Citation records / unique source documents | 5,184 / 2,478 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 156;
`documented_prewar_employer_found` 128; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,750;
`occupation_only_found` 1,024; `requires_archival_review` 3,568; and
`verified_employer_found` 266.

The public projection contains **2,282** published affiliations, **750**
organizations, **3,974** public sources, and **5,007** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **134** Python unit tests;
- Astro check with zero errors, warnings, or hints across **287** source files;
- a static build of **24,724** HTML pages;
- **87/87** bounded Playwright checks across desktop, phone, and tablet,
  including **18/18** Batch 656 checks and **30/30** accessibility checks with
  no serious or critical axe violations;
- all internal links across **24,724** HTML files, with **50,347** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **99,935,605** bytes verified at
  manifest SHA-256
  `7f2414a19046012d3e98be1e89a1194670fd46991f49f8b2daa771c062f564f4`;
- zero unexpected private-identifier boundary matches across **24,796** public
  artifacts; and
- identical consecutive tree digests:
  `c873a1adb17496cce42229dcbf4b19235cc20fd5d4f1de4520d8f51668a12451`
  for `site/public` and
  `cead6c4c2e7d191040271f888327754de7e0cc9d4f473faa79723f50a55bc721`
  for `site/dist`.

External URLs were inventoried, not all requested. No authenticated NARA
Catalog request was made. The previously exposed API key must be rotated before
authenticated work resumes. CI, Pages deployment, and exact live-release
verification remain pending until the branch is pushed and merged.

## Resume

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch656.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page319-mezoff-mielziner-review_batch-656_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
