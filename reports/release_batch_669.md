# Batch 669 release - Molster-Monroe research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 669 completes the next contiguous 22-person queue on PDF page 325 rows
26-46 and page 326 row 1. Rendered-page inspection confirmed all printed rows,
ranks, blank fields, boxes, archival locations, and private identifiers,
including the original `Robert P Monlvx` spelling.

Negley C. Monett receives a probable identity match and a qualified,
medium-confidence, documented prewar role at the *San Francisco News* based on
the 1938 and 1941 Polk directories. The project does not represent that role as
his immediate pre-OSS affiliation or last civilian employer. Major John J.
Monigan Jr. receives a high-confidence identity bridge from Harvard's
Nuremberg Trials Project, without a speculative employer assignment.

Eight exact or defensible protected Army matches receive high-confidence
identities without employer inferences. Wrong-name, middle-initial, impossible
chronology, and OCR candidates were rejected. The Natalene Mongello/Natelene
Mengello and Avary C. Monroe/Avary C. Munroe pairs remain separate possible
duplicates. All 22 people have saved terminal outcomes and explicit archival
next actions where online evidence did not resolve the question.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**. Batch 669 adds no oil-company member.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,467 (35.3691%) |
| People with confirmed/high employer evidence | 300 (1.2532%) |
| People with confirmed/high affiliation evidence | 664 (2.7737%) |
| Archival-review dispositions assessed | 6,924 (28.9235%) |
| Not started | 15,467 |
| Possible duplicate groups | 512 |
| Conflicts | 218 |
| Attempts or plans | 15,104 |
| Claims by confidence | confirmed 1,325; high 2,224; medium 1,433; low 196; conflicting 191 |
| Citation records / unique source documents | 5,269 / 2,545 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 149; `conflicting_sources` 175;
`documented_prewar_employer_found` 138; `in_progress` 1,905;
`needs_identity_review` 435; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 295; `not_started` 15,467;
`occupation_only_found` 1,030; `requires_archival_review` 3,718; and
`verified_employer_found` 270.

The public projection contains **2,315** published affiliations, **767**
organizations, **4,053** public sources, and **5,169** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass except for the precisely documented Astro
type-check loader issue below:

- all **136** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- a static production build of **24,742** HTML pages;
- **87/87** bounded Playwright checks across desktop, phone, and tablet,
  including **18/18** Batch 669 checks, **33/33** core route and interaction
  checks, **6/6** analytics checks, and **30/30** accessibility checks with no
  serious axe violations;
- all internal links across **24,742** HTML files, with **50,410** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,933,628** bytes verified
  at manifest SHA-256
  `1a3cead0a15883c6d11fb6bb63454dc7e4ec72be00729b4c8cbc0b725a9c685c`;
- zero unexpected private-identifier boundary matches across **24,814** built
  artifacts and all **70** tracked public assets;
- a production dependency audit with **zero known vulnerabilities**; and
- identical consecutive static-build tree digests:
  `b0f95bd048d2094df4967257a48b3f19644158772e2b43f6a596a66be7d66722`,
  with tracked-public-data digest
  `8210199772a416a52eb73c98594d46e6443b939dc5c86a4cde2dc5a40bb29855`.

The static build completed successfully using Node 26.0.0 and Astro 7.3.2.
`astro check` still does not reach diagnostics: in CI mode it reports that
`@astrojs/check` and TypeScript are required even though installed versions
0.9.10 and 5.9.3 are present. This is a local dependency-discovery defect, not
a reported source diagnostic. The production build, browser suites, link
audit, data integrity, manifest, and privacy checks above are unaffected.

No authenticated NARA Catalog request was made. The previously exposed API key
must be rotated before authenticated work resumes.

## Release status

Batch 669 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch669.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page325-326-molster-monroe-review_batch-669_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
