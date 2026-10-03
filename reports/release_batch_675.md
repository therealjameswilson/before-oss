# Batch 675 release - Moore-Moran research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 675 completes PDF page 328 rows 1-24, from Springs R Moore through
George B Moran. Fresh rendered-page inspection confirmed all 24 source rows,
including the truncated printed notes `file is ch` and `docume`.

Exact names plus nonshared protected identifiers support six high-confidence
Army identity resolutions. Those matches do not establish an employer, and
the official bulk file's coded occupations remain private. Walter A Moore's
Army record adds a `Jr.` suffix absent from the index; both source forms remain
recoverable, while the unfamiliar `PUT` grade stays uninterpreted.

NARA's official Record Group 226 Entry 210 guide provides a seventh
high-confidence identity and assignment bridge for Clarence Moran. Its Box
201, WN#08587 entry associates Clarence Moran, the Field Photo Branch, and the
same distinctive `C SP-P` grade printed in the index. This is not treated as
pre-OSS employment. Wayne E Moore's protected identifier instead retrieves a
different Army name. The unrelated name is excluded from publication, and
Wayne Moore remains an explicit identity conflict requiring critical-priority
Box 536 review.

Sixteen people have terminal `no_reliable_result_after_protocol` outcomes and
high-priority Box 535 or 536 next actions. No negative online result is
represented as proof that prior employment did not exist. A bounded Library
of Congress pass completed 24 live queries and returned 27 discovery
candidates; all were rejected as name-only or temporally unsuitable results
lacking the required identity and temporal bridges. Six official Army
identity candidates were accepted, one wrong-name Army result was rejected,
and all Library of Congress candidates were rejected, for 34 reviewed
decisions. The CIA adapter's single fail-closed event was preserved and did
not count as negative evidence.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**. Batch 675 adds no oil-company member.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,580 (35.8411%) |
| People with confirmed/high employer evidence | 302 (1.2615%) |
| People with confirmed/high affiliation evidence | 670 (2.7988%) |
| Archival-review dispositions assessed | 7,036 (29.3914%) |
| Not started | 15,354 |
| Possible duplicate groups | 512 |
| Conflicts | 224 |
| Attempts or plans | 15,496 |
| Claims by confidence | confirmed 1,326; high 2,272; medium 1,437; low 196; conflicting 197 |
| Citation records / unique source documents | 5,307 / 2,575 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 150; `conflicting_sources` 181;
`documented_prewar_employer_found` 139; `in_progress` 1,905;
`needs_identity_review` 438; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 358; `not_started` 15,354;
`occupation_only_found` 1,030; `requires_archival_review` 3,756; and
`verified_employer_found` 271.

The public projection contains **2,323** published affiliations, **767**
organizations, **4,090** public sources, and **5,225** published claims.
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
- Astro diagnostics: **309 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,742 pages**.
- Browser release suite: **93 / 93 passed** across desktop, phone, and tablet
  (24 Batch 675, 33 core, 6 analytics, and 30 accessibility checks).
- Link check: **24,742 HTML files** checked; every internal link resolved.
- Public manifest: **67 assets / 101,300,577 bytes** verified; manifest SHA-256
  `237f0ade6d642a4cae7df76bc3f4a7ab5b74c5d737697af6ead5e0103d0c3915`.
- Private-identifier audit: **24,814 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,814 files / 300,244,098
  bytes**, SHA-256
  `2cc50ad2a0109de93d4bddb703fb9a5e50d9e5c35d2de33ef203675794788ca7`.

## Release status

Batch 675 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch675.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page328-moore-moran-review_batch-675_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army name, or private reviewer note is committed or published.
