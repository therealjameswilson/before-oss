# Batch 657 release - Mierzejewski-Milbauer research

Research and release date: 2026-09-23 America/New_York.

## Historical work

The PDF-page 319-320 queue from `William S. Mierzejewski` through `Eugene
Milbauer` contains 22 source rows and 22 cautious people. Every person now has
a saved reviewed outcome. No reliable predecessor employer was found online
for anyone in the cohort; each profile preserves that evidentiary limit and
routes the open question to the indexed Box 522 or 523 personnel file.

William S. Mierzejewski has high-confidence identity evidence in an IPN study
of OSS operations in Yugoslavia. John L. Mihelich is confirmed by the NARA
index, official Army bulk data, and a contemporary Detachment 101 order.
Casimir J. Migon is also supported by an exact Army match and the Detachment
101 order. Those sources establish identities or wartime assignments, not
pre-OSS employers.

Rafael P. Miettunen remains separate from Rafael P. Mettuhen despite a
duplicated protected identifier, and Wallace J. Mihelich remains separate from
John L. Mihelich for the same reason. A 1939 newspaper candidate for a John L.
Mihelich was rejected because it provided no bridge to the indexed OSS
technician. All 19 generated candidates received decisions: 14 accepted as
identity evidence, four marked conflicting, and one rejected. Zero remain
unreviewed.

The cohort ends with 20 `requires_archival_review` and two
`conflicting_sources` statuses. Identity statuses are one `confirmed`, 14
`high_confidence`, two `conflicting`, and five `unresolved`. The bundle adds 17
identity claims: one confirmed, 14 high, and two conflicting. It adds zero
employer or affiliation claims and four cited source documents.

A normalization repair maps printed `T-Sgt`, `S-Sgt`, and `Tec-4` variants
into the existing enlisted-Army taxonomy. Six source rows now classify
correctly; the database refresh changed five person entities because one had
already been corrected in the reviewed bundle.

The top oil-company category remains evidence-scoped to **eight people across
ten historically named companies**. No identity-only Army record in this
batch is counted as oil-company employment.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,206 (34.2788%) |
| People with confirmed/high employer evidence | 293 (1.2239%) |
| People with confirmed/high affiliation evidence | 650 (2.7152%) |
| Archival-review dispositions assessed | 6,662 (27.8291%) |
| Not started | 15,728 |
| Possible duplicate groups | 497 |
| Conflicts | 199 |
| Attempts or plans | 14,286 |
| Claims by confidence | confirmed 1,316; high 2,122; medium 1,416; low 189; conflicting 174 |
| Citation records / unique source documents | 5,188 / 2,481 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 158;
`documented_prewar_employer_found` 128; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,728;
`occupation_only_found` 1,024; `requires_archival_review` 3,588; and
`verified_employer_found` 266.

The public projection contains **2,282** published affiliations, **750**
organizations, **3,978** public sources, and **5,024** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **135** Python unit tests;
- Astro check with zero errors, warnings, or hints across **288** source files;
- a static build of **24,724** HTML pages;
- **87/87** bounded Playwright checks across desktop, phone, and tablet,
  including **18/18** Batch 657 checks and **30/30** accessibility checks with
  no serious or critical axe violations;
- all internal links across **24,724** HTML files, with **50,348** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,015,104** bytes verified
  at manifest SHA-256
  `cf2e81b2c6db9ace25da2404b56d6e2c23417a627f05e816e97f9fbd521d1b29`;
- zero unexpected private-identifier boundary matches across **24,796** public
  artifacts; and
- identical consecutive tree digests:
  `5c1eff9349a11360a8bd09aa5daea81a6cf18e4dc406926398e8513819903567`
  for `site/public` and
  `996765b4c3ecc25c1353e89b5d336f2eb5dc86f1e958b1cd9d7897f7823deb4e`
  for `site/dist`.

External URLs were inventoried, not all requested. The CIA Reading Room check
was blocked by its robots restriction, and the second LoC batch repeatedly
returned transient 503 responses; neither access failure was treated as a
negative research result. No authenticated NARA Catalog request was made. The
previously exposed API key must be rotated before authenticated work resumes.

## Released and verified live

Release identifiers will be recorded here after the reviewed commit is merged
and the exact GitHub Pages artifact passes deployed verification.

## Resume

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch657.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page319-320-mierzejewski-milbauer-review_batch-657_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research refresh-classifications
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
