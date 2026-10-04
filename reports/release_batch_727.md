# Batch 727 release - Owens-Packer research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 727 publishes reviewed outcomes for PDF page 354, rows 1-23, from Emily
L Owens through Don S Packer. All 23 printed rows were visually checked against
a 300-dpi page render. Original spellings, grades, boxes, notes, and locations
remain recoverable. The asterisk-only `P` and `Pacchiotti` rows remain indexed
without invented first names, and the `also AS` notes for Richard C Owens Jr
and Axel H Oxholm remain distinct from identity evidence.

Three carefully qualified pre-OSS affiliations are published. A June 1942
architectural journal identifies Axel H Oxholm as managing director of Pacific
Forest Industries; this is a medium-confidence last civilian employer, not an
immediate pre-OSS affiliation. A 1942 directory supports high-confidence
identity resolution for Ned K Owyang as Ned Ke-Hung Owyang and records student
status at Tri-State College under radio engineering; the college is not
classified as his employer and no degree is inferred. Contemporary and later
historical accounts support a medium-confidence prewar Berlitz affiliation for
Andre Pacatte, while preserving uncertainty over the exact school branch and
role.

The batch also preserves three index or identifier conflicts instead of
silently merging them: Henry S Pachowicz shares a private Army identifier with
an adjacent Lewis Randall A row; Andre Pacatte and Harry A Pagatte collide in
the indexed Army evidence; and George J Packard Jr collides with Mary A
Hawkins. No mismatched metadata is transferred.

The cohort records 18 `requires_archival_review`, two
`documented_prewar_employer_found`, two `conflicting_sources`, and one
`occupation_only_found` outcome. Identity statuses are 14 unresolved, seven
high-confidence, and two conflicting. The reviewed bundle adds seven sources,
three organizations, three affiliations, 13 claims, 29 claim-source links, 23
person updates, and 23 consolidated research attempts. Six accepted and three
conflicting identity decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,758 (40.7619%) |
| People with confirmed/high employer evidence | 330 (1.3785%) |
| People with confirmed/high affiliation evidence | 738 (3.0828%) |
| Archival-review dispositions assessed | 8,216 (34.3206%) |
| Not started | 14,176 |
| Possible duplicate groups | 523 |
| Conflicts | 319 |
| Attempts or plans | 17,792 |
| Claims by confidence | confirmed 1,370; high 2,887; medium 1,524; low 198; conflicting 279; unresolved 2 |
| Citation records / unique source documents | 5,661 / 2,857 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 188; `conflicting_sources` 276;
`documented_prewar_employer_found` 166; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,156; `not_started` 14,176;
`occupation_only_found` 1,047; `requires_archival_review` 3,931; and
`verified_employer_found` 287.

The public projection contains 2,471 published affiliations, 858
organizations, 4,442 public sources, and 6,053 published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus generated subtests.
* Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick check
  `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
* Astro diagnostics: 361 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,835 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 727, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,835 HTML files checked; every internal link resolved and
  50,724 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 105,777,426 bytes verified; manifest SHA-256
  `cf33bd4f23646dc4c82bbcbdd8f9e5ca32baf472f9eb19941ddba5359c21f207`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,907 public artifacts, and 1,186 candidate substrings checked
  with zero unexpected boundary matches.
* Production dependency audit: zero vulnerabilities. The static deployment has
  no Node runtime.
* Determinism: consecutive build trees matched at 24,907 files /
  307,602,060 bytes, SHA-256
  `3b9db9f46e808ee2437b1bfc496846ee432f86fda0057b8320fc3badfba17119`.

## Publication verification

Release commit
[`2450e0aaf78f9e4fe444a62f31a099883b02b61f`](https://github.com/therealjameswilson/before-oss/commit/2450e0aaf78f9e4fe444a62f31a099883b02b61f)
was pushed to `main`. GitHub Actions completed successfully for both the
[`Test` run](https://github.com/therealjameswilson/before-oss/actions/runs/37212809550)
and the
[`Deploy GitHub Pages` run](https://github.com/therealjameswilson/before-oss/actions/runs/37212809530).

The immutable verifier then compared the public site with that exact commit.
It verified 67 assets / 105,777,426 bytes, manifest SHA-256
`cf33bd4f23646dc4c82bbcbdd8f9e5ca32baf472f9eb19941ddba5359c21f207`,
eight core routes, 30 source-register pages, and all 23 direct Batch 727
profile routes. The verified public base URL is
<https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-727 --page 354 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-727 --max-queries 23
python3 -m oss_research research --source loc --batch batch-727 --max-queries 23
python3 -m oss_research research --source web --batch batch-727 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch727.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page354-owens-packer-review_batch-727_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary is PDF page 354, rows 24-46, from Charles H Padden
through Wellman Page. No API key, raw API response, full service or
officer number, copyrighted page image, unrelated Army coded occupation,
street address, modern people-finder record, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
