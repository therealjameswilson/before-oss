# Batch 674 release - Moore research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 674 completes PDF page 327 rows 23-46, from George R. Moore through
Russell C. Moore. Fresh rendered-page inspection confirmed all 24 source rows,
including the printed `Margeret` spelling and Robert D. Moore's `possible`
note.

Exact names plus nonshared protected identifiers support ten high-confidence
Army identity resolutions. Those matches do not establish an employer, and
the official bulk file's coded occupations remain private. Richard H. Moore's
Army entry grade of private conflicts sharply with the index's `Col`; the
identity bridge is strong, but the rank disagreement remains public and the
case is excluded from settled analytics pending Box 535 review. Robert D.
Moore's Army record includes a `Jr.` suffix absent from the index; both source
forms remain recoverable.

Fourteen people have terminal `no_reliable_result_after_protocol` outcomes
and high-priority Box 534 or 535 next actions. No negative online result is
represented as proof that prior employment did not exist. A bounded Library
of Congress retry completed 24 live queries and returned 87 discovery
candidates; all were rejected as name-only or postwar results lacking the
required identity and temporal bridges. Ten official Army identity candidates
were accepted, for 97 reviewed decisions. The CIA adapter's single fail-closed
event was preserved and did not count as negative evidence.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**. Batch 674 adds no oil-company member.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,556 (35.7408%) |
| People with confirmed/high employer evidence | 302 (1.2615%) |
| People with confirmed/high affiliation evidence | 670 (2.7988%) |
| Archival-review dispositions assessed | 7,012 (29.2911%) |
| Not started | 15,378 |
| Possible duplicate groups | 512 |
| Conflicts | 223 |
| Attempts or plans | 15,447 |
| Claims by confidence | confirmed 1,326; high 2,265; medium 1,437; low 196; conflicting 196 |
| Citation records / unique source documents | 5,304 / 2,573 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 150; `conflicting_sources` 180;
`documented_prewar_employer_found` 139; `in_progress` 1,905;
`needs_identity_review` 438; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 342; `not_started` 15,378;
`occupation_only_found` 1,030; `requires_archival_review` 3,749; and
`verified_employer_found` 271.

The public projection contains **2,323** published affiliations, **767**
organizations, **4,087** public sources, and **5,217** published claims.
Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all parser-warning rows visually
  resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing.
- Astro diagnostics: **308 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,742 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 674, 33 core, 6 analytics, and 30 accessibility checks).
- Link check: **24,742 HTML files** checked; every internal link resolved.
- Public manifest: **67 assets / 101,260,405 bytes** verified; manifest SHA-256
  `9a4e0be2dfaf09674f31c0187f14ee3b70c38710d00db4209c2e43ae8c7e1b20`.
- Private-identifier audit: **24,814 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,814 files / 300,178,464
  bytes**, SHA-256
  `47f3d618fcc063b401c87b91b98d4bd63887ba5faee510cbb47edc44eab9f2f6`.

## Release status

Batch 674 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch674.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page327-moore-review_batch-674_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
