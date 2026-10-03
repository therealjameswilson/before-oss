# Batch 704 release - Nicholson-Niedner research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 704 covers PDF page 342, rows 23-45, from Donald Nicholson through Jack B
Niedner. Fresh visual inspection confirmed all 23 printed rows, representing 23
active person entities. The immutable extraction is unchanged.

Emrich Nicholson is a probable identity match to the industrial designer whom
the Museum of Modern Art's 1941 catalogue identifies as Otto Kuhler's chief
designer from 1936 through 1938 and a freelance designer from 1938 onward. Both
are qualified medium-confidence documented-prewar affiliations; neither is
presented as his immediate pre-OSS affiliation or last civilian employer.

Harry G Nickles is confirmed by a direct OSS mission report naming “Lt. Harry
G. Nickles, USNR” as security officer for Istanbul. His personnel category is
corrected to commissioned naval officer. The assignment is documented as OSS
service and is not converted into a pre-OSS affiliation.

Gaspare Nicotri is a high-confidence identity match to the Sicilian lawyer,
educator, sociologist, and political exile documented by Queens College and to
the man linked in a source-attributed historical account to 1942 discussions
about assisting the OSS. A University of Turin archival record documents his
1940 authorship in *La Parola*. The public profile distinguishes occupation,
professional affiliation, and OSS-related chronology instead of inventing an
employer.

Official Army bulk evidence supports five high-confidence identity-only
decisions. Four spelling or duplicate conflicts remain visible and unmerged.
Three unrelated Library of Congress candidates were rejected. The CIA adapter
failed closed, and the full staged protocol was completed for all 23 people.

The cohort records 17 `no_reliable_result_after_protocol`, four
`needs_identity_review`, one `documented_prewar_employer_found`, and one
`occupation_only_found` outcome. Identity statuses are one `confirmed`, six
`high_confidence`, three `probable`, two `ambiguous`, and 11 `unresolved`. The
evidence bundle adds seven sources, three organizations, three affiliations,
12 claims, 23 claim-source links, 23 person updates, and 23 research attempts.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,231 (38.5605%) |
| People with confirmed/high employer evidence | 319 (1.3326%) |
| People with confirmed/high affiliation evidence | 707 (2.9533%) |
| Archival-review dispositions assessed | 7,689 (32.1191%) |
| Not started | 14,703 |
| Possible duplicate groups | 522 |
| Conflicts | 273 |
| Attempts or plans | 16,651 |
| Claims by confidence | confirmed 1,347; high 2,691; medium 1,478; low 196; conflicting 248; unresolved 2 |
| Citation records / unique source documents | 5,506 / 2,736 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 171; `conflicting_sources` 230;
`documented_prewar_employer_found` 155; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 867; `not_started` 14,703;
`occupation_only_found` 1,038; `requires_archival_review` 3,783; and
`verified_employer_found` 281.

The public projection contains **2,401** published affiliations, **821**
organizations, **4,289** public sources, and **5,757** published claims. The
oil-company directory remains nine cited people across eleven historically
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
- Astro diagnostics: **338 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,797 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 704, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,797 HTML files** checked; every internal link resolved and
  50,599 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 104,002,900 bytes** verified; manifest SHA-256
  `8ce60af9e4b89ba3fbf98cc76e55af245f6e7235176e316c1d73c6e536b34c68`.
- Private-identifier audit: **70 public data artifacts**, 12,926 normalized
  identifiers, 120 formatted variants, and 713 candidate substrings checked
  with **0 unexpected boundary matches** and **0 false positives**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,869 files /
  304,715,301 bytes**, SHA-256
  `78565f63b3e1ea9073e6b756f46ef5cf92f25014ac622b4e0b569b9202ea8676`.

The unbounded historical Playwright aggregate remains too large for one Node
process because 176 legacy specifications repeatedly retain the 56 MB people
dataset and exhaust an 8 GB heap. This is a runner-resource limitation, not a
known product failure. The bounded release suite exercises the core routes,
Batch 704 profiles, analytics, responsive layouts, and accessibility across all
three configured browser projects and passed 87 / 87.

## Released and verified live

Batch 704 was fast-forwarded to `main` as commit
[`53067ebaba2036a26931b57d5bde66c5cc8ea729`](https://github.com/therealjameswilson/before-oss/commit/53067ebaba2036a26931b57d5bde66c5cc8ea729).
The GitHub Pages build and deployment
[`37125324401`](https://github.com/therealjameswilson/before-oss/actions/runs/37125324401)
and independent test workflow
[`37125324407`](https://github.com/therealjameswilson/before-oss/actions/runs/37125324407)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 104,002,900 bytes matched, as did eight core
routes, all 29 source-register pages, and all 23 Batch 704 profiles changed by
the reviewed-evidence bundle. The live site reports 23,978 source rows, 23,939
person entities, 9,231 researched people, 707 verified affiliations, 319
verified employers, and 14,703 not-started people. Emrich Nicholson's two
qualified design affiliations, Harry G Nickles's documented OSS assignment,
Gaspare Nicotri's occupation and professional affiliation, all five accepted
identity-only decisions, all four unmerged identity conflicts, and the
unresolved profiles render from their public URLs. The oil-company directory
remains visible with nine cited people across eleven historically named
companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-704 --page 342 --first-row 23 --last-row 45
python3 -m oss_research research --source cia --batch batch-704 --max-queries 1
python3 -m oss_research research --source loc --batch batch-704 --resume --max-queries 6
python3 -m oss_research research --source web --batch batch-704 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch704.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page342-nicholson-niedner-review_batch-704_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 342, row 46 (Arthur H Nielsen).
No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, street address, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
