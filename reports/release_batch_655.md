# Batch 655 release candidate - Meyer-Meysereav research

Research date: 2026-09-23 America/New_York. Deployment verification is pending.

## Historical work

The page-318/319 `Jack L. Meyer` through `C. P. Meysereav` queue contains 22
source rows and 22 cautious people. Every person now has a saved reviewed
outcome. Hans Meyerhoff's Army-assigned immediate OSS pathway, UCLA
teaching-assistant employment, and student status are modeled separately.
Emile Meyran's archive-cited Compagnie Française de Raffinage employment is a
qualified medium-confidence finding, distinct from his French Army service
and earlier Compagnie des Eaux de Paris work.

The adjacent Hans Meyerhoff rows remain separate. The Norman H. Meyers/Norman
M. Myers and C. P. Meysereav/Charles P. Mersereau/Charles P. Meserau conflicts
also remain separate and visible. Six other official Army crosswalks are
identity evidence only, not inferred employers.

The cohort ends with 17 `requires_archival_review`, three
`conflicting_sources`, one `verified_employer_found`, and one
`documented_prewar_employer_found` statuses. Identity statuses are seven
`high_confidence`, three `conflicting`, and 12 `unresolved`. The bundle adds
18 claims: ten high, five medium, and three conflicting.

The top oil-company category now contains **eight people across ten
historically named companies**. Emile Meyran is visibly labeled as a qualified
medium-confidence entry; mere professional affiliations and oil-related
occupations without a named employer remain excluded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,162 (34.0950%) |
| People with confirmed/high employer evidence | 291 (1.2156%) |
| People with confirmed/high affiliation evidence | 646 (2.6985%) |
| Archival-review dispositions assessed | 6,618 (27.6453%) |
| Not started | 15,772 |
| Possible duplicate groups | 497 |
| Conflicts | 195 |
| Attempts or plans | 14,166 |
| Claims by confidence | confirmed 1,312; high 2,092; medium 1,415; low 189; conflicting 170 |
| Citation records / unique source documents | 5,169 / 2,465 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 154;
`documented_prewar_employer_found` 126; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,772;
`occupation_only_found` 1,021; `requires_archival_review` 3,553; and
`verified_employer_found` 266.

The public projection contains **2,275** published affiliations, **747**
organizations, **3,959** public sources, and **4,985** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **134** Python unit tests, including canonical-organization reuse and
  safe cleanup of an unreferenced bundle-generated duplicate;
- Astro check with zero errors, warnings, or hints across **286** source files;
- a static build of **24,721** HTML pages;
- **84/84** bounded Playwright checks across desktop, phone, and tablet,
  including **15/15** Batch 655 checks and **30/30** accessibility checks with
  no serious or critical axe violations;
- all internal links across **24,721** HTML files, with **50,332** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **99,787,721** bytes verified at
  manifest SHA-256
  `81d84169dbe31018b23b2a93b07c25115e978cefdee813b7e666355dbad3f2a8`;
- zero unexpected private-identifier boundary matches across **24,793** public
  artifacts; and
- identical consecutive tree digests:
  `0dfde72d5bd009b0a077d49c69a77ec78f3eca8d1ab85b6b0bb35305b13717e0`
  for `site/public` and
  `b73f53319e69e211074fd4e99d79e061f98a1029fda7a3616ad9c14cba6ede81`
  for `site/dist`.

External URLs were inventoried, not all requested. Deployment verification is
still pending. No authenticated NARA Catalog request was made. The previously
exposed API key must be rotated before authenticated work resumes.

## Resume

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch655.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages318-319-meyer-meysereav-review_batch-655_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
