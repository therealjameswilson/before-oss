# Batch 713 release - Obuckley-Odeneal research

Research and release-candidate date: 2026-10-03 America/New_York.

## Historical work

Batch 713 covers PDF page 347, rows 1-23, from Joseph P Obuckley through
John F Odeneal. Fresh 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Original index spellings, punctuation,
rank fields, box numbers, and archival location remain recoverable from the
immutable source rows. The `also AS` note for Edward V Oconnor is preserved
without expansion.

Five nonshared identifiers from the official Army bulk file support
high-confidence identities for Joseph S Ochranek, Daniel J Oconnell, John A
Oconnor, Joseph J Oddo, and William K Odell. Ochranek's `Jr.` suffix is retained
as a documented variant. Odell's 1946 Army entry date is identity evidence
only, not a pre-OSS pathway. Army occupation codes were not converted into
occupations or affiliations.

One protected identifier creates a material conflict rather than a match: the
index prints Joseph F Ochnat, while the Army file gives OCHWAT JOSEPH F. The
candidate is formally rejected, the person remains visibly `conflicting`, and
Box 567 is required before any merge.

Miyoji Oda reaches high-confidence identity through the exact index name, a
wartime War Relocation Authority roster, and a Los Angeles Times obituary;
the latter two independently name siblings Frank, Kazume, and Lillian. Gabriel
Odalovich is published only as a probable identity because the unusual exact
name and Army lieutenant status agree with a Veterans Affairs-derived cemetery
transcription, but no protected identifier or direct OSS bridge is accessible.
Neither identity establishes a named pre-OSS employer.

A 1941 Gloucester directory entry for a rare-name John F Odeneal student and a
later library authority record remain unpublished leads because neither links
that person directly to the OSS index row. Evelyn F Oconnor and Raymond R
Oconnor leads were rejected as unbridged namesakes. Common-name results and
postwar-only material were excluded.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed; the web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed the required
official, OSS, employment, occupation, obituary, institutional, newspaper,
directory, military, and archival checks for every person. The current
official Army bulk object was downloaded to a temporary directory, verified,
and scanned transiently across 9,200,232 records. No raw bulk file or raw row
is retained in the repository.

The cohort records 21 `no_reliable_result_after_protocol`, one
`requires_archival_review`, and one `conflicting_sources` outcome. Identity
statuses are six `high_confidence`, one `probable`, one `conflicting`, and 15
`unresolved`. The reviewed bundle adds five sources, seven identity claims
(six high and one medium), 15 claim-source links, 23 person updates, and 23
consolidated research attempts. Six identity-review decisions are recorded:
five accepted Army matches and one rejected conflict. No organization or
affiliation claim was added.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,437 (39.4210%) |
| People with confirmed/high employer evidence | 325 (1.3576%) |
| People with confirmed/high affiliation evidence | 720 (3.0076%) |
| Archival-review dispositions assessed | 7,895 (32.9797%) |
| Not started | 14,497 |
| Possible duplicate groups | 523 |
| Conflicts | 294 |
| Attempts or plans | 17,117 |
| Claims by confidence | confirmed 1,352; high 2,779; medium 1,498; low 198; conflicting 256; unresolved 2 |
| Citation records / unique source documents | 5,572 / 2,790 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 180; `conflicting_sources` 251;
`documented_prewar_employer_found` 158; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 1,024; `not_started` 14,497;
`occupation_only_found` 1,039; `requires_archival_review` 3,794; and
`verified_employer_found` 285.

The public projection contains **2,425** published affiliations, **832**
organizations, **4,353** public sources, and **5,878** published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Verification and publication

The exact rebuilt tree passed these local release gates:

- Python unit suite: **139 / 139 passed**, plus 78 generated subtests.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all 32 parser-warning rows
  visually resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, public-projection, and
  terminal-status invariant passing.
- Astro diagnostics: **347 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,809 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 713, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,809 HTML files** checked; every internal link resolved and
  50,650 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 104,724,189 bytes** verified; manifest SHA-256
  `33477fae28e85cb1fa9372e704985247490f6e5c986375cadd12b9669771c624`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 70 public artifacts, and 717 candidate substrings checked with **0
  unexpected boundary matches**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,881 files /
  305,872,390 bytes**, SHA-256
  `512b42af4f12dc684c94fc4e88b7445c7cc54f9623899b99ee2198cf8e09bc80`.

Publication verification will be appended after the immutable content commit
has passed the independent GitHub Actions test and Pages workflows and the
deployed manifest, routes, source register, and direct profile URLs have been
checked against that commit.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-713 --page 347 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-713 --max-queries 23
python3 -m oss_research research --source loc --batch batch-713 --max-queries 23
python3 -m oss_research research --source web --batch batch-713 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch713.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page347-obuckley-odeneal-review_batch-713_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 347, row 24 (Mary J Odgers). No
API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published. No authenticated NARA
Catalog API request was made for this batch.
