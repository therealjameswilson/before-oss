# Batch 647 release status - pages 18-34 and Meegan-Meigs research

Research date: 2026-09-23 America/New_York. This report records the reviewed
research and extraction state before release verification and deployment.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 18, 19, 22, 23, 26, 27,
29, 30, 31, and 34 were compared against the extraction at 180 dpi. Every row
matches the extraction. Complete-page visual review now covers **458/522
pages** and **21,034/23,978 rows**: **21,002** match the extraction, **32**
retain reviewed corrections, and **2,944** remain unaudited. All PDF pages
remain represented, every parser warning is resolved, and SQLite integrity
and foreign-key checks pass.

The page-315 `Jospeh Meegan` through `Richard L. Meigs` queue contains **22
source rows and 22 cautious people**. Every person received four staged
source-specific plans and a saved reviewed outcome. Seven exact or carefully
bounded official-Army identity bridges were accepted; two protected-identifier
spelling conflicts remain visible.

The principal evidence outcomes are:

- **Leonard C. Meeker:** high-confidence identity. Treasury and Solicitor
  General government-law assignments are separated from the Army, which is
  the best-supported immediate institutional route into OSS.
- **Gaudens Megaro:** high-confidence identity. A contemporary Queens College
  affiliation is the last documented civilian employment before his December
  1941 work for the Coordinator of Information, itself recorded separately as
  the immediate pre-OSS affiliation.
- **Lincoln Mei:** probable, medium-confidence identity. A 1949 Senate report
  corroborates an Army first lieutenant and wartime service, but does not
  establish an employer or directly identify an OSS file.
- **William G. Mehillos / Army `MEHILOS`** and **Eugene W. Mehner / Army
  `MOHNER`:** explicit conflicts pending archival review; neither spelling is
  silently substituted.

The cohort ends with 17 `in_progress`, two `verified_employer_found`, two
`conflicting_sources`, and one `needs_identity_review` status. The oil-company
category remains limited to the supported set of **seven people across nine
historically named companies**.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 21,034 / 23,978 rows; 458 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,989 (33.3723%) |
| People with confirmed/high employer evidence | 282 (1.1780%) |
| People with confirmed/high affiliation evidence | 634 (2.6484%) |
| Archival-review dispositions assessed | 6,447 (26.9309%) |
| Not started | 15,945 |
| Possible duplicate groups | 492 |
| Conflicts | 175 |
| Attempts or plans | 13,349 |
| Claims by confidence | confirmed 1,311; high 2,007; medium 1,392; low 187; conflicting 150 |
| Citation records / unique source documents | 5,101 / 2,409 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 134;
`documented_prewar_employer_found` 118; `in_progress` 1,831;
`needs_identity_review` 416; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,945;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 260.

The public projection contains **2,237** published affiliations, **714**
organizations, **3,894** public sources, and **4,856** published claims.
Full-index historical research remains unfinished.

## Verification and deployment

Release-test, reproducibility, and deployment results will be appended after
the tracked-only candidate passes local validation and the GitHub Pages
artifact is verified.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages18-34_sparse_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch647.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page315-meegan-meigs-review_batch-647_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published. No authenticated NARA Catalog request was made.
