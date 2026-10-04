# Batch 710 release - Novak-Nupen research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 710 covers PDF page 345, rows 24-46, from Francis J Novak through Edly D
Nupen. Fresh 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. The immutable extraction is unchanged.

Official Army evidence supports seven high-confidence identities: John J
Novak, Michael J Novosel, Chester S Nowik, Robert P Noyes, Benjamin B Null,
Jose R Nunez, and Guy T Nunn Jr. A Little Norway roster and Department of
Justice report support Edly Daniel Nupen while leaving his chronology relative
to OSS unresolved. Army occupation codes were not converted into employer or
occupation claims.

The site publishes one Batch 710 affiliation. Official Army history and the
Michael J. Novosel Foundation biography establish Novosel's Army air-service
path into four months of OSS special duty in 1943. It is classified as a
strongly date-bounded military assignment, with “Army Air Corps” preserved as
the source wording, and never presented as a civilian employer.

Joseph A Novatnik and Joseph A Novotnik remain separate, as do Robert S Nowell
and Robin S Nowell; each pair shares an index identifier but lacks evidence
that justifies a merge. A 1947 *Interiors* article about a designer named
Dorothy Q. Noyes remains a low-confidence private lead because it does not
establish identity with the OSS index row. The public profile directs readers
to Box 564 instead of publishing that lead as fact. Public identifiers remain
masked.

The CIA and LoC adapters failed closed without usable adapter results. The
staged protocol was nevertheless completed for all 23 people using accessible
exact-name OSS, employment, occupation, institutional, newspaper, obituary,
military, directory, and archival sources. The cohort records 15
`no_reliable_result_after_protocol`, four `conflicting_sources`, three
`requires_archival_review`, and one `completed` outcome. Identity statuses are
eight `high_confidence`, four `probable`, and 11 `unresolved`. The reviewed
bundle adds seven sources, one organization, one affiliation, 14 claims, 25
claim-source links, 23 person updates, and 23 consolidated research attempts.
Claims comprise nine high-confidence published decisions, four medium-
confidence qualified decisions, and one low-confidence withheld lead. Ten
manual review decisions are recorded and imported.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,369 (39.1370%) |
| People with confirmed/high employer evidence | 323 (1.3493%) |
| People with confirmed/high affiliation evidence | 716 (2.9909%) |
| Archival-review dispositions assessed | 7,827 (32.6956%) |
| Not started | 14,565 |
| Possible duplicate groups | 523 |
| Conflicts | 291 |
| Attempts or plans | 16,969 |
| Claims by confidence | confirmed 1,352; high 2,750; medium 1,495; low 197; conflicting 256; unresolved 2 |
| Citation records / unique source documents | 5,554 / 2,775 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 179; `conflicting_sources` 248;
`documented_prewar_employer_found` 157; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 967; `not_started` 14,565;
`occupation_only_found` 1,039; `requires_archival_review` 3,789; and
`verified_employer_found` 284.

The public projection contains **2,419** published affiliations, **830**
organizations, **4,336** public sources, and **5,846** published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**. Python 3.14 emitted existing
  unclosed-connection resource warnings; the suite exited successfully.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all 32 parser-warning rows
  visually resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, public-projection, and
  terminal-status invariant passing.
- Astro diagnostics: **344 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,806 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 710, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,806 HTML files** checked; every internal link resolved and
  50,637 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 104,533,107 bytes** verified; manifest SHA-256
  `f346d48268854605a4ae0b269584b90fe711a6c92c37dbad1996f6f72469477b`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,878 artifacts, and 1,158 candidate substrings checked with **0
  unexpected boundary matches**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,878 files /
  305,563,615 bytes**, SHA-256
  `7af635b5f77e8c8ac38dad374a22176965521e5125a8f19829ab03f56ad6dadc`.

The unbounded historical Playwright aggregate remains too large for one Node
process because the legacy specifications repeatedly retain the large people
dataset and exhaust an 8 GB heap. This is a runner-resource limitation, not a
known product failure. The bounded release suite exercises the core routes,
Batch 710 profiles, analytics, responsive layouts, and accessibility across
all three configured browser projects.

## Released and verified live

Batch 710 was fast-forwarded to `main` as commit
[`fe052d6e2f83c192823e196f49efe490220e068f`](https://github.com/therealjameswilson/before-oss/commit/fe052d6e2f83c192823e196f49efe490220e068f).
The GitHub Pages build and deployment
[`37168336849`](https://github.com/therealjameswilson/before-oss/actions/runs/37168336849)
and independent test workflow
[`37168336759`](https://github.com/therealjameswilson/before-oss/actions/runs/37168336759)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 104,533,107 bytes matched, as did eight core
routes, all 29 source-register pages, and all 23 Batch 710 profiles changed by
the reviewed-evidence bundle. The live site reports 23,978 source rows, 23,939
person entities, 9,369 researched people, 716 verified affiliations, 323
verified employers, and 14,565 not-started people. Novosel's military pathway,
Nupen's qualified identity, all six additional identifier-backed identities,
the withheld Dorothy Noyes lead, the four distinct shared-identifier profiles,
and the unresolved and archival-review dispositions render from their public
URLs. The oil-company directory remains visible with nine cited people across
eleven historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-710 --page 345 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-710 --max-queries 23
python3 -m oss_research research --source loc --batch batch-710 --max-queries 23
python3 -m oss_research research --source web --batch batch-710 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch710.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page345-novak-nupen-review_batch-710_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 346, row 1 (Robert C Nusbaum).
No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published. No authenticated NARA
Catalog API request was made for this batch.
