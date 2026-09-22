# Batch 643 release status - pages 501-510 and McNamara-McNutt research

Date: 2026-09-22 UTC. This report records the audited tracked-only local
release candidate. Deployment fields will be finalized from the exact merged
revision after release.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 501-510 were compared
against SQLite at 180 dpi. Page 506 was already in the deterministic-random
visual-review ledger. Every row matches the current extraction. Complete-page
visual review now covers **424/522 pages** and **19,470/23,978 rows**:
**19,438** match the extraction, **32** retain reviewed corrections, and
**4,508** remain unaudited.

The page-313 `James J. McNamara` through `Mack McNutt` queue contains 23 source
rows and 23 cautious people. A live Library of Congress attempt is saved for
every person. All 17 newspaper candidates were inspected and rejected because
they identify a different name or initial, are postwar, or lack an OSS, rank,
protected-identifier, or Box 511-512 bridge. No namesake occupation was
transferred.

Thirteen official Army or duplicate-boundary candidates received decisions.
Exact normalized names and nonshared protected identifiers support
high-confidence crosswalks for Thomas J. McNamara, William D. McNeely, Edward
F. McNeil, Volney G. McNeill, Harry P. McNickle, John J. McNulty, Joseph G.
McNulty, and Joseph S. McNulty. Joseph S. McNulty's official `Jr.` suffix is a
documented variant without changing the indexed display name.

Coy I. McNeil remains conflicting because the printed identifier points to an
Army entry rendered `MC VIEL/COY`. James E. McNearnry and James E. McNerney
remain separate probable entities: their adjacent Box 512 rows share a
protected identifier but differ in surname and rank. Both jackets remain on
the archival-review path.

The final queue state is 20 `in_progress`, two `needs_identity_review`, and one
`conflicting_sources`. All 30 candidates have decisions: eight accepted, four
probable, one conflicting, and 17 rejected. No employer or affiliation claim
was added. Army grades, entry dates, and occupation codes remain identity
context rather than employer evidence.

The oil-company category remains prominently available in the site navigation,
home page, and personnel directory. It lists the current evidence-scoped set of
**seven people** across **nine historically named companies** and excludes
mere text matches and unsupported candidates.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 19,470 / 23,978 rows; 424 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,899 (32.9964%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,357 (26.5550%) |
| Not started | 16,035 |
| Possible duplicate groups | 489 |
| Conflicts | 170 |
| Attempts or plans | 13,099 |
| Claims by confidence | confirmed 1,311; high 1,969; medium 1,380; low 187; conflicting 145 |
| Citation records / unique source documents | 5,078 / 2,390 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 131;
`documented_prewar_employer_found` 118; `in_progress` 1,760;
`needs_identity_review` 404; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,035;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,871
sources, and 4,801 claims. Full-index historical research remains unfinished.

## Privacy hardening

The release adds an export-layer guard that recursively redacts any complete
private identifier accidentally embedded in public prose, including formatted
legacy variants. This removed two identity-note exposures in the
McNearnry-McNerney review while retaining the private evidence in SQLite. The
guard is covered by a unit test and the independent artifact scanner.

## Local verification

The isolated tracked-only candidate passes all local release gates:

- **133/133** Python unit tests;
- **84/84** browser checks across desktop, phone, and tablet: 15 Batch 643,
  33 core-route, six analysis, and 30 accessibility/axe checks;
- Astro check with zero errors, warnings, or hints across **274** source files;
- **24,681** static HTML pages and **24,753** total artifacts;
- every internal link resolved, with **50,238** unique external URLs
  inventoried for the separate live check;
- all **67** manifest-listed assets matched, totaling **98,575,813** bytes at
  manifest SHA-256
  `6ad2073211405a0415a44567ed5cb0e418fbe8753ef2eb489907190a58e317d9`;
- the public-identifier audit compared **12,926** normalized identifiers and
  **120** formatted variants across 24,753 artifacts with zero aggregate false
  positives, manifest-size false positives, or unexpected full-number boundary
  matches;
- two clean builds reproduced production-tree SHA-256
  `7eaa37d80aa9772777d1810b84d9680ebc02b533c4e22faa74f4f712ab3832c2`
  across 24,753 files and 295,078,274 bytes.

The complete historical browser archive contains 244 batch specifications and
remains available through `npm run test:e2e`; the bounded release suite is the
documented release gate. Unrelated user-owned duplicate files remain preserved
and excluded from tracked-only verification.

## Deployment

Deployment is pending merge of the Batch 643 release candidate. The final
merged commit, GitHub Actions runs, GitHub Pages workflow, and exact-ref live
verification will be recorded here after release.

- Public release: <https://therealjameswilson.github.io/before-oss/>
- Oil-company category: <https://therealjameswilson.github.io/before-oss/oil-companies/>

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages501-510_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch643.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch643.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page313-mcnamara-mcnutt-review_batch-643_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
