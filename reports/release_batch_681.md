# Batch 681 release - Morrissey-Morwood research

Research and local release date: 2026-09-25 America/New_York.

## Historical work

Batch 681 completes PDF page 331 rows 1-23, from Thomas T Morrison through two
adjacent William G Morwood records. Fresh page inspection confirmed all 23
source rows and kept the two Morwood rows separate.

Eleven protected-identifier-supported Army matches were accepted. Harlie P
Morse and Melvin S Morton instead retain visible spelling conflicts because
the Army file names Harlie B Morse and Melvin S Mooton under the corresponding
identifiers. The conflicts require Box 540 review and were not silently
corrected.

Richard Morse is a high-confidence match to Dartmouth's Richard Morse '44.
Institutional and official evidence support Dartmouth student status before
Army entry, not Dartmouth employment. A contemporaneous OSS review confirms
Don E Mort's Army-to-OSS chronology and his earlier salesman occupation but
does not name his civilian employer. A scholarly history supports the corporal
William Morwood's prewar radio-writer occupation and Army-to-OSS pathway. It
also makes the adjacent lieutenant row a probable later officer record, but
the two protected identifiers differ, so the rows remain unmerged.

Chandler Morse's previously verified Federal Reserve findings remain intact.
Sixteen people have terminal `no_reliable_result_after_protocol` outcomes, two
retain `conflicting_sources`, one is `completed`, two have
`occupation_only_found`, one has `requires_archival_review`, and Chandler
retains `verified_employer_found`. No negative online result is represented as
proof that prior employment did not exist.

The featured oil-company category remains at the top of the home page and
personnel directory, with a dedicated category page and shareable filter. It
remains evidence-scoped to **eight people across ten historically named
companies**; ownership-only and unsupported associations remain excluded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,714 (36.4009%) |
| People with confirmed/high employer evidence | 306 (1.2782%) |
| People with confirmed/high affiliation evidence | 678 (2.8322%) |
| Archival-review dispositions assessed | 7,170 (29.9511%) |
| Not started | 15,220 |
| Possible duplicate groups | 515 |
| Conflicts | 234 |
| Attempts or plans | 15,754 |
| Claims by confidence | confirmed 1,329; high 2,332; medium 1,451; low 196; conflicting 207 |
| Citation records / unique source documents | 5,351 / 2,612 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 151; `conflicting_sources` 191;
`documented_prewar_employer_found` 143; `in_progress` 1,905;
`needs_identity_review` 440; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 443; `not_started` 15,220;
`occupation_only_found` 1,034; `requires_archival_review` 3,783; and
`verified_employer_found` 272.

The public projection contains **2,339** published affiliations, **775**
organizations, **4,134** public sources, and **5,312** published claims.
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
- Astro diagnostics: **315 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,750 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 681, 33 core, 6 analytics, and 30 accessibility checks).
- Link check: **24,750 HTML files** checked; every internal link resolved and
  50,464 unique external URLs inventoried for the separate live check.
- Public manifest: **67 assets / 101,793,343 bytes** verified; manifest SHA-256
  `d6323ff75458e8c6e5e1541e48f0a6efa18aed2add54ec330fc78522bb64c673`.
- Private-identifier audit: **24,822 artifacts** scanned with **0 unexpected
  boundary matches**.
- Production dependency audit: **0 vulnerabilities**.
- Determinism: two consecutive build trees matched at **24,822 files /
  301,052,220 bytes**, SHA-256
  `63cc71207973b150ce7e27f9d84712df63fffee2cd9e4087a3b0ef1eaf8f824d`.

## Release status

Batch 681 is a local release candidate. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state and the already-live oil-company category.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-25_batch681.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page331-morrissey-morse-review_batch-681_2026-09-25.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, or private reviewer note is committed or
published.
