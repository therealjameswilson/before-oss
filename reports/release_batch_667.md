# Batch 667 release - Mitschke-Moefred research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 667 completes the next contiguous 22-person queue on PDF page 324 rows
28-46 and page 325 rows 1-3. Rendered-page inspection confirmed all printed
rows, ranks, blank fields, boxes, archival locations, and private identifiers.

Henry H. Miwa receives a high-confidence identity match and a documented last
civilian employer at the Fresno Buddhist Church or Fresno Betsuin. The adjacent
Hideo Miwa row remains a separate ambiguous entity and is not merged. Tetsuo
Scott Miyakawa's South Manchurian Railway Office work is published as earlier
documented prewar employment, not as immediate employment, because a later
unnamed private employer intervened. Eric Edward Mockler-Ferryman's documented
British and Allied assignments are classified as military affiliations. Rudolf
Modley's civilian enterprises and Coordinator of Information consulting are
kept distinct.

Three exact protected Army matches receive high-confidence identities without
employer inferences. The Kazyu C. Miyadira versus `MIYABARA KAZUO C` conflict
remains visible. Low-confidence namesake and authorship leads are withheld from
public employment claims. All 22 people have saved terminal outcomes.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It is
still evidence-scoped to **eight people across ten historically named
companies**. Batch 667 adds no oil-company member.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,424 (35.1894%) |
| People with confirmed/high employer evidence | 300 (1.2532%) |
| People with confirmed/high affiliation evidence | 664 (2.7737%) |
| Archival-review dispositions assessed | 6,880 (28.7397%) |
| Not started | 15,510 |
| Possible duplicate groups | 512 |
| Conflicts | 216 |
| Attempts or plans | 14,971 |
| Claims by confidence | confirmed 1,325; high 2,206; medium 1,429; low 196; conflicting 191 |
| Citation records / unique source documents | 5,261 / 2,539 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 149; `conflicting_sources` 175;
`documented_prewar_employer_found` 136; `in_progress` 1,906;
`needs_identity_review` 431; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 275; `not_started` 15,510;
`occupation_only_found` 1,030; `requires_archival_review` 3,700; and
`verified_employer_found` 270.

The public projection contains **2,313** published affiliations, **766**
organizations, **4,045** public sources, and **5,147** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass except for the precisely documented Astro
type-check loader issue below:

- all **136** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- a static production build of **24,740** HTML pages;
- **93/93** bounded Playwright checks across desktop, phone, and tablet,
  including **24/24** Batch 667 checks, **33/33** core route and interaction
  checks, **6/6** analytics checks, and **30/30** accessibility checks with no
  serious or critical axe violations;
- all internal links across **24,740** HTML files, with **50,404** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,821,648** bytes verified
  at manifest SHA-256
  `854a3e1d7778e2233f63245e0a149633166823f9896af9834e7f76b33822b220`;
- zero unexpected private-identifier boundary matches across **24,812** built
  artifacts and all **70** tracked public assets;
- a production dependency audit with **zero known vulnerabilities**; and
- identical consecutive static-build tree digests:
  `abdba10bf30b29d2f8a876d070dc882b77938418c0e7062ca86cef98708030f8`,
  with tracked-public-data digest
  `080bc2d867f59b998cb3ede93dda7a232388d86cfb15dc0bc974fb9418f9b3a4`.

The clean static build completed successfully using Node 24.19.0 and Astro
7.1.5. `astro check` does not currently run to diagnostics: importing the
installed `@astrojs/check` dependency fails inside `vscode-languageserver` with
`TypeError: Class extends value undefined is not a constructor or null`, after
which Astro incorrectly offers to reinstall the already-present package. This
is a local dependency-resolution defect, not a reported source diagnostic. The
production build, browser suites, link audit, data integrity, manifest, and
privacy checks above are unaffected. The QA server and link checker now accept
`BEFORE_OSS_DIST_DIR`, so clean build artifacts can be verified without
copying them into the checkout.

No authenticated NARA Catalog request was made. The previously exposed API key
must be rotated before authenticated work resumes.

## Release status

Batch 667 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-24_batch667.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page324-mitschke-moe-page325-moefred-review_batch-667_2026-09-24.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
