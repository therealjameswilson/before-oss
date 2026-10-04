# Batch 711 release - Nusbaum-Obata research

Research and release-candidate date: 2026-10-03 America/New_York.

## Historical work

Batch 711 covers PDF page 346, rows 1-23, from Robert C Nusbaum through Chiura
Z Obata. Fresh 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. The immutable extraction is unchanged,
including two unusual index spellings and the abbreviated or truncated notes.

The site adds six carefully typed affiliations. Robert C Nusbaum's explicit
Army-to-OSS sequence is published as an immediate military assignment, while
his Harvard undergraduate status remains a separate educational affiliation.
John Bertram Oakes's last identifiable civilian employer is The Washington
Post, with the Trenton Times preserved as earlier work; the chronology is
strongly date-bounded rather than overstated as an explicit OSS transfer. Hans
A Nyholm's Royal Danish Navy service and Chiura Z Obata's 1932-1942 UC
Berkeley faculty employment are documented pre-OSS roles whose precise OSS
sequence still requires archival review.

Official Army evidence supports four additional or corroborating identities,
and direct institutional or official evidence supports Nydorf, Nyholm, Oakes,
and Obata. Nydorf's documented OSS graphic-design work is used for identity
resolution only, not reclassified as pre-OSS employment. Conflicting protected
identifiers for Philip J Nyquist and Dale W Oakley remain visible and rejected
as identity evidence. A possible Willem A Nyland chemist lead is withheld from
the public claims because the accessible sources do not adequately link that
person to the index row. No Army occupation code was converted into an
employer or occupation claim.

The CIA and LoC adapters failed closed without usable adapter results. The
staged protocol was nevertheless completed for all 23 people using accessible
exact-name OSS, employment, occupation, institutional, newspaper, obituary,
military, directory, and archival sources. The cohort records 15
`no_reliable_result_after_protocol`, three `requires_archival_review`, two
`conflicting_sources`, one `completed`, one
`documented_prewar_employer_found`, and one `verified_employer_found` outcome.
Identity statuses are eight `high_confidence`, two `conflicting`, one
`probable`, and 12 `unresolved`. The reviewed bundle adds ten sources, six
organizations, six affiliations, 17 claims, 33 claim-source links, 23 person
updates, and 23 consolidated research attempts. Claims comprise 14
high-confidence published decisions, two medium-confidence qualified
conflicts, and one low-confidence withheld lead. Six identity-review decisions
are recorded and imported.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,392 (39.2331%) |
| People with confirmed/high employer evidence | 325 (1.3576%) |
| People with confirmed/high affiliation evidence | 720 (3.0076%) |
| Archival-review dispositions assessed | 7,850 (32.7917%) |
| Not started | 14,542 |
| Possible duplicate groups | 523 |
| Conflicts | 293 |
| Attempts or plans | 17,017 |
| Claims by confidence | confirmed 1,352; high 2,764; medium 1,497; low 198; conflicting 256; unresolved 2 |
| Citation records / unique source documents | 5,564 / 2,784 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 180; `conflicting_sources` 250;
`documented_prewar_employer_found` 158; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 982; `not_started` 14,542;
`occupation_only_found` 1,039; `requires_archival_review` 3,792; and
`verified_employer_found` 285.

The public projection contains **2,425** published affiliations, **832**
organizations, **4,345** public sources, and **5,862** published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**, plus 78 subtests.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all 32 parser-warning rows
  visually resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, public-projection, and
  terminal-status invariant passing.
- Astro diagnostics: **345 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,808 pages**.
- Browser release suite: **87 / 87 passed** across desktop, phone, and tablet
  (18 Batch 711, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,808 HTML files** checked; every internal link resolved and
  50,646 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 104,641,947 bytes** verified; manifest SHA-256
  `3c1046dd90ec26f7290f3e2c3850dfa302adca418888b8d299136c9a94dc50c5`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,880 artifacts, and 1,157 candidate substrings checked with **0
  unexpected boundary matches**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,880 files /
  305,737,018 bytes**, SHA-256
  `c766abb615a08b233e5c64cdeb246d74582af5cda9f8460d19adb791d416242f`.

The unbounded historical Playwright aggregate remains too large for one Node
process because the legacy specifications repeatedly retain the large people
dataset and exhaust an 8 GB heap. This is a runner-resource limitation, not a
known product failure. The bounded release suite exercises the core routes,
Batch 711 profiles, analytics, responsive layouts, and accessibility across
all three configured browser projects.

## Release status

This release candidate passed every local gate. GitHub Pages deployment and
post-deployment byte and route verification are still pending.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-711 --page 346 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-711 --max-queries 23
python3 -m oss_research research --source loc --batch batch-711 --max-queries 23
python3 -m oss_research research --source web --batch batch-711 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch711.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page346-nusbaum-obata-review_batch-711_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 346, row 24 (Donald W
Obenshain). No API key, raw API response, full service number, copyrighted
page image, unrelated Army coded occupation, street address, modern
people-finder record, or private reviewer note is committed or published. No
authenticated NARA Catalog API request was made for this batch.
