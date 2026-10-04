# Batch 709 release - Norris-Novak research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 709 covers PDF page 345, rows 1-23, from Laura M Norris through Charles
J Novak. Fresh 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. The immutable extraction is unchanged.
The visual audit also confirmed Leonard E Norris's printed four-digit value
`5633`, Mary T Norris's `folders s` note, Genevieve M Noto's `possible` note,
and the identical identifier printed in the adjacent Wilson K Norton and
William A Norwood rows. Those anomalies are preserved rather than silently
repaired.

Official Army evidence supports six high-confidence identity-only decisions:
Steve F Norsic Jr., Irving M Norton, William A Norton, William A Notbohm,
Theodore Notides, and Charles J Novak. Cornell's 1941 commencement record and a
contemporary Troy newspaper support Robert P Northup through exact name, Round
Lake locality, captain rank, Army Air Forces context, and mechanical-engineering
education.

The site publishes three affiliations. Robert Northup's June 1941 Mechanical
Engineering degree is classified strictly as a Cornell University student
affiliation, never as employment. A contemporary banking journal digitized by
the Federal Reserve Bank of St. Louis documents Theodore Notides at
Manufacturers Trust Company beginning in 1941; official Army evidence dates
his entry to 26 August 1942, making this a strongly date-bounded last civilian
employer without claiming immediate succession to OSS. The same journal
documents three earlier years at Corn Exchange Bank & Trust Company, published
as earlier prewar employment. A Library of Congress finding aid independently
corroborates the Notides-Manufacturers Trust association.

The Army file associated with David T Northault prints David T Northcutt, and
the one associated with Rudolf S Nothmann prints Nothman. Both spelling
conflicts remain visible and neither is treated as a correction. Wilson K
Norton and William A Norwood remain separate people in one possible-duplicate
group pending comparison of their Box 564 files. Public pages expose only
masked serial suffixes. Leonard Norris, Mary Norris, and Genevieve Noto receive
explicit archival-review outcomes because their index anomalies require
file-level context.

The CIA and LoC adapters failed closed without usable adapter results. The
staged protocol was nevertheless completed for all 23 people using accessible
exact-name OSS, employment, occupation, institutional, newspaper, obituary,
military, directory, and archival sources. The cohort records 14
`no_reliable_result_after_protocol`, four `conflicting_sources`, three
`requires_archival_review`, one `completed`, and one `verified_employer_found`
outcome. Identity statuses are seven `high_confidence`, two `probable`, two
`conflicting`, and 12 `unresolved`. The reviewed bundle adds six sources, three
organizations, three affiliations, 14 claims, 28 claim-source links, 23 person
updates, and 23 consolidated research attempts. Claims comprise ten
high-confidence, two medium-confidence, and two conflicting decisions. Ten
manual review decisions are recorded and imported.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,346 (39.0409%) |
| People with confirmed/high employer evidence | 323 (1.3493%) |
| People with confirmed/high affiliation evidence | 715 (2.9868%) |
| Archival-review dispositions assessed | 7,804 (32.5995%) |
| Not started | 14,588 |
| Possible duplicate groups | 523 |
| Conflicts | 287 |
| Attempts or plans | 16,920 |
| Claims by confidence | confirmed 1,352; high 2,741; medium 1,491; low 196; conflicting 256; unresolved 2 |
| Citation records / unique source documents | 5,547 / 2,769 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 178; `conflicting_sources` 244;
`documented_prewar_employer_found` 157; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 952; `not_started` 14,588;
`occupation_only_found` 1,039; `requires_archival_review` 3,786; and
`verified_employer_found` 284.

The public projection contains **2,418** published affiliations, **830**
organizations, **4,330** public sources, and **5,833** published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**, plus **78 / 78** parametrized
  subtests. Python 3.14 emitted existing unclosed-connection resource warnings;
  the suite exited successfully.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all 32 parser-warning rows
  visually resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, public-projection, and
  terminal-status invariant passing.
- Astro diagnostics: **343 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,806 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 709, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,806 HTML files** checked; every internal link resolved and
  50,633 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 104,470,466 bytes** verified; manifest SHA-256
  `189dc082dc6c0b083cb2d2a21608985d355c26b018186bd030e47e92e7a5c69b`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,878 artifacts, and 1,158 candidate substrings checked with **0
  unexpected boundary matches**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,878 files /
  305,465,577 bytes**, SHA-256
  `80b629003d5c6453d92c824a96a8b35fa8c0cf7941985f2c0d1dce8232fa8a4a`.

The unbounded historical Playwright aggregate remains too large for one Node
process because the legacy specifications repeatedly retain the large people
dataset and exhaust an 8 GB heap. This is a runner-resource limitation, not a
known product failure. The bounded release suite exercises the core routes,
Batch 709 profiles, analytics, responsive layouts, and accessibility across
all three configured browser projects.

## Released and verified live

Batch 709 was fast-forwarded to `main` as commit
[`63bbaccb898279b0a0472da52c35a17850e292cd`](https://github.com/therealjameswilson/before-oss/commit/63bbaccb898279b0a0472da52c35a17850e292cd).
The GitHub Pages build and deployment
[`37165843532`](https://github.com/therealjameswilson/before-oss/actions/runs/37165843532)
and independent test workflow
[`37165843561`](https://github.com/therealjameswilson/before-oss/actions/runs/37165843561)
passed on 2026-10-03 America/New_York. GitHub emitted advisory warnings that
several official actions still target Node.js 20 while runners force Node.js
24, and that `ubuntu-latest` is scheduled to migrate to Ubuntu 26; the
workflows nevertheless completed successfully.

Post-deployment verification compared the public site with that exact commit.
All 67 manifest assets totaling 104,470,466 bytes matched, as did eight core
routes, all 29 source-register pages, and all 23 Batch 709 profiles changed by
the reviewed-evidence bundle. The live site reports 23,978 source rows, 23,939
person entities, 9,346 researched people, 715 verified affiliations, 323
verified employers, and 14,588 not-started people. Theodore Notides's two
banking roles, Robert Northup's student-only affiliation, all additional
high-confidence identities, the unresolved profiles, the archival anomalies,
and the preserved spelling and duplicate conflicts render from their public
URLs. The oil-company directory remains visible with nine cited people across
eleven historically named companies.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-709 --page 345 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-709 --max-queries 23
python3 -m oss_research research --source loc --batch batch-709 --max-queries 23
python3 -m oss_research research --source web --batch batch-709 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch709.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page345-norris-novak-review_batch-709_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 345, row 24 (Francis J Novak).
No API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published. No authenticated NARA
Catalog API request was made for this batch.
