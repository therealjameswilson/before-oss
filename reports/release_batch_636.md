# Batch 636 release status - pages 431-440 and McDowell-McFadden research

Date: 2026-09-22 UTC. This report records the audited local release candidate.
Deployment fields will be completed only after the exact commit passes CI and
the public artifact is verified.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 431-440 were compared
against SQLite at 180 dpi. Every page matches the current extraction. The
durable visual ledger rises to **366/522 pages** and **16,802/23,978 rows**:
**16,770** match the extraction, **32** retain reviewed corrections, and
**7,176** remain for complete visual comparison.

The page-308 `Robert H. McDowell` through `Thomas J. McFadden` queue contained
23 source rows representing 21 people. Its Library of Congress pass saved one
live result for every person and returned four discovery candidates across
three people. Every candidate was inspected in official item-level context and
rejected as unrelated, different-initial, historical, or insufficiently
bridged.

Charles W. McFadden and Stuart P. McFadden received high-confidence Army
identity crosswalks from nonshared protected identifiers and exact normalized
names. Both Stuart index rows remain preserved and linked to one person entity.
The protected identifier printed for Edward C. McElroy instead resolves to a
wholly different Army entry. That identity was not assigned, and the conflict
remains visible pending Box 504 review. Full identifiers and the unrelated name
remain private; Army grade and occupation codes are not employer evidence.

The final queue state is 20 `in_progress` and one `conflicting_sources`. All
eight candidates have decisions; none remains unreviewed. This is
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
| Visually audited extraction | 16,802 / 23,978 rows; 366 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,742 (32.3405%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,303 (26.3294%) |
| Not started | 16,187 |
| Possible duplicate groups | 488 |
| Conflicts | 164 |
| Attempts or plans | 12,850 |
| Claims by confidence | confirmed 1,311; high 1,926; medium 1,375; low 187; conflicting 138 |
| Citation records / unique source documents | 5,064 / 2,384 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 125;
`documented_prewar_employer_found` 118; `in_progress` 1,619;
`needs_identity_review` 399; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,187;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,857
sources, and 4,746 claims. Full-index historical research remains unfinished.

## Local verification

The isolated tracked-only candidate passes all local release gates:

- **132/132** Python unit tests;
- **84/84** browser checks across desktop, phone, and tablet: 15 Batch 636,
  33 core-route, six analysis, and 30 accessibility/axe checks;
- Astro check with zero errors, warnings, or hints across **267** source files;
- **24,681** static HTML pages and **24,753** total artifacts;
- every internal link resolved, with **50,238** unique external URLs
  inventoried for the separate live check;
- all **67** manifest-listed assets matched, totaling **98,312,601** bytes at
  manifest SHA-256
  `8992bd9de02ec8d6cb5eff8b094b5b1e0dee787129cc6efe4c1e5e4869edb9fb`;
- the public-identifier audit compared **12,926** normalized identifiers and
  **120** formatted variants with zero unexpected full-number boundary matches;
- two clean builds reproduced production-tree SHA-256
  `387298800863b7f825b1d5883a1017cf3e5a842cc5d805b060c3aee345f9bf3f`.

Unrelated user-owned duplicate files remain preserved and excluded.

## Deployment

Pull request [#373](https://github.com/therealjameswilson/before-oss/pull/373)
merged as `52015b07826846c87f16f524ae961c7293ce9b76` after its required test
check passed in 4m29s. The exact merged commit then passed:

- [Test run 35727195675](https://github.com/therealjameswilson/before-oss/actions/runs/35727195675)
  in 4m15s; and
- [Deploy GitHub Pages run 35727195712](https://github.com/therealjameswilson/before-oss/actions/runs/35727195712),
  with a 1m16s build and 17s deploy job.

The post-deployment verifier fetched the exact merged ref, matched all **67**
manifest assets and **98,312,601** bytes at manifest SHA-256
`8992bd9de02ec8d6cb5eff8b094b5b1e0dee787129cc6efe4c1e5e4869edb9fb`,
checked eight core routes, all 26 source-register pages, and the three directly
affected profiles. Independent HTTP checks returned 200 for the home page, the
oil-company category, and a directly affected McFadden profile.

Public site: https://therealjameswilson.github.io/before-oss/

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages431-440_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch636.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch636.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page308-mcdowell-mcfadden-review_batch-636_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
