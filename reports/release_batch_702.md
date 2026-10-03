# Batch 702 release - Newman-Nicholas research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 702 covers PDF page 341, rows 23-45, from Martin D Newman through Blake
H Nicholas. Fresh visual inspection confirmed all 23 printed rows,
representing 22 active person entities. The two William L Newman rows remain
separately preserved and linked to one entity; the immutable extraction is
unchanged.

Lester J Newquist receives a qualified, medium-confidence Brown Brothers
Harriman & Co. affiliation beginning in 1936. It is published as documented
prewar employment, not as an immediate pre-OSS affiliation or last civilian
employer. Martin D Newman, Morton Newman, Howard T Newsom, Grover R Newton,
Vidma Newton, and Blake H Nicholas receive high-confidence identity-only
decisions from official Army bulk evidence. Coded occupations are not treated
as employers, and Howard T Newsom's postwar oil-tool employer lead is excluded.

Earl J Nichelson and Earl J Nicholson share a protected identifier but differ
in spelling, rank, box, and page. Their possible-duplicate relationship is
published while both records remain unmerged pending direct file evidence.

The CIA adapter failed closed at robots policy without sending a request. The
Library of Congress adapter completed four no-result checks and recorded one
timeout before the live run was stopped. The staged web protocol was completed
for all 22 people. No raw API response is retained.

The cohort records one `documented_prewar_employer_found`, one
`needs_identity_review`, and 20 `no_reliable_result_after_protocol` outcomes.
Identity statuses are seven `high_confidence`, one `probable`, one
`ambiguous`, and 13 `unresolved`. The evidence bundle adds four sources, one
organization, one affiliation, ten claims, 19 claim-source links, 22 person
updates, and 22 consolidated research attempts. Six Army identity candidates
are accepted; one possible duplicate remains probable and unmerged.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,187 (38.3767%) |
| People with confirmed/high employer evidence | 319 (1.3326%) |
| People with confirmed/high affiliation evidence | 706 (2.9492%) |
| Archival-review dispositions assessed | 7,644 (31.9312%) |
| Not started | 14,747 |
| Possible duplicate groups | 521 |
| Conflicts | 272 |
| Attempts or plans | 16,571 |
| Claims by confidence | confirmed 1,345; high 2,678; medium 1,471; low 196; conflicting 246; unresolved 2 |
| Citation records / unique source documents | 5,493 / 2,725 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 169; `conflicting_sources` 229;
`documented_prewar_employer_found` 154; `in_progress` 1,904;
`needs_identity_review` 446; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 832; `not_started` 14,747;
`occupation_only_found` 1,037; `requires_archival_review` 3,783; and
`verified_employer_found` 281.

The public projection contains **2,395** published affiliations, **815**
organizations, **4,276** public sources, and **5,733** published claims. The
top oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all parser-warning rows visually
  resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing.
- Astro diagnostics: **336 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,791 pages**.
- Browser release suite: **84 / 84 passed** across desktop, phone, and tablet
  (15 Batch 702, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,791 HTML files** checked; every internal link resolved and
  50,585 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 103,855,029 bytes** verified; manifest SHA-256
  `b9affa789ac31f756a853d0b736a42de5d0c97b8ce756ef51b4da11229378486`.
- Private-identifier audit: **24,863 artifacts**, 12,926 normalized identifiers,
  120 formatted variants, and 1,161 candidate substrings checked with **0
  unexpected boundary matches** and **0 false positives**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,863 files /
  304,461,095 bytes**, SHA-256
  `d3dc5c13e46fa35b95b10d615e973d3e18526e78e63a42c0bb594c0bf5bd281e`.

## Released and verified live

Batch 702 was fast-forwarded to `main` as commit
[`030daa2c2e09240eedf1907d2507108fd3f8cdaa`](https://github.com/therealjameswilson/before-oss/commit/030daa2c2e09240eedf1907d2507108fd3f8cdaa).
The GitHub Pages build and deployment
[`37120430565`](https://github.com/therealjameswilson/before-oss/actions/runs/37120430565)
and independent test workflow
[`37120430488`](https://github.com/therealjameswilson/before-oss/actions/runs/37120430488)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 103,855,029 bytes matched, as did eight core
routes, all 29 source-register pages, and all 22 Batch 702 profile routes. The
live site reports 23,978 source rows, 23,939 person entities, 9,187 researched
people, 706 verified affiliations, 319 verified employers, and 14,747
not-started people. Lester J Newquist's qualified Brown Brothers Harriman
affiliation, the Nichelson/Nicholson unmerged duplicate review, all six
identity-only decisions, and the unresolved profiles render from their public
URLs. The oil-company directory remains visible with nine cited people across
eleven historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-702 --page 341 --first-row 23 --last-row 45
python3 -m oss_research research --source cia --batch batch-702 --max-queries 22
python3 -m oss_research research --source loc --batch batch-702 --max-queries 22
python3 -m oss_research research --source web --batch batch-702 --max-queries 22
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch702.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page341-newman-nicholas-review_batch-702_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 341, row 46 (Christo Nicholas).
No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, postwar employer lead, street address, or
private reviewer note is committed or published. No authenticated NARA
Catalog API request was made for this batch.
