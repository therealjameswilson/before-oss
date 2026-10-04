# Batch 714 release - Odgers-Offut research

Research and release-candidate date: 2026-10-04 America/New_York.

## Historical work

Batch 714 covers PDF page 347, rows 24-46, from Mary J Odgers through
Wilma B Offut. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Original index spellings, rank fields,
box numbers, and archival location remain recoverable from the immutable
source rows.

One nonshared identifier from the official Army bulk file supports a
high-confidence identity for William H Odonnell. Another protected identifier
creates a material conflict: the index prints John L Ofax, while the Army file
gives OFAK JOHN L. That candidate is formally rejected, both spellings remain
visible, and Box 569 is required before any merge. No Army occupation code was
converted into occupation or employer evidence.

Bjarne Oen reaches high-confidence identity through the documented Bjarne Øen
spelling, compatible Norwegian air-service leadership, and Norwegian
institutional sources. Store norske leksikon places Øen at the head of the
Norwegian Armed Forces High Command's Fourth Office (FO IV) from 1942. FO IV
is published as his best-supported immediate pre-OSS military assignment with
a strongly date-bounded temporal basis; it is not presented as a civilian
employer or silently merged into OSS.

Charles Z Offin is published only as a probable identity. A City College
institutional biography documents the rare exact name and a role as editor
and publisher of *Pictures on Exhibit* beginning in 1937. That is presented as
a medium-confidence documented prewar professional affiliation, not as a
proven immediate predecessor or last civilian employer. Edward W Oexner is
also published only as a probable identity because an unusual exact name and
matching master-sergeant status align with a Veterans Affairs-derived
cemetery transcription, but no protected identifier or OSS transition is
available online.

A postwar CIA memorandum signed Justin E. O'Donnell remains an unpublished
lead because it does not bridge its signer to the indexed first lieutenant.
Fred or Frederick Oechsner results were rejected because the index prints
Francis and no direct source establishes equivalence. Modern people-search,
address, postwar-only, and other namesake results were excluded.

The CIA adapter made one bounded attempt and failed closed; the Library of
Congress adapter searched one query across two people and failed closed. The
web adapter recorded 23 deterministic planned queries without making live
requests. Manual staged review completed the required official, exact-name
OSS, employment, occupation, obituary, institutional, newspaper, directory,
military, and archival search families for every person. The official Army
bulk object was verified and scanned transiently across 9,200,232 records. No
raw bulk file or raw row is retained in the repository.

The cohort records 19 `no_reliable_result_after_protocol`, one `completed`,
one `occupation_only_found`, one `requires_archival_review`, and one
`conflicting_sources` outcome. Identity statuses are two `high_confidence`,
two `probable`, one `conflicting`, and 18 `unresolved`. The reviewed bundle
adds six sources, two organizations, two affiliations, six claims (three high
and three medium), 13 claim-source links, 23 person updates, and 23
consolidated research attempts. Two identity-review decisions are recorded:
one accepted Army match and one rejected conflict.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,460 (39.5171%) |
| People with confirmed/high employer evidence | 325 (1.3576%) |
| People with confirmed/high affiliation evidence | 721 (3.0118%) |
| Archival-review dispositions assessed | 7,918 (33.0757%) |
| Not started | 14,474 |
| Possible duplicate groups | 523 |
| Conflicts | 295 |
| Attempts or plans | 17,166 |
| Claims by confidence | confirmed 1,352; high 2,782; medium 1,501; low 198; conflicting 256; unresolved 2 |
| Citation records / unique source documents | 5,578 / 2,795 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 181; `conflicting_sources` 252;
`documented_prewar_employer_found` 158; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 1,043; `not_started` 14,474;
`occupation_only_found` 1,040; `requires_archival_review` 3,795; and
`verified_employer_found` 285.

The public projection contains **2,427** published affiliations, **834**
organizations, **4,359** public sources, and **5,884** published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Verification and publication

The exact rebuilt tree passed these local release gates:

- Python unit suite: **139 / 139 passed**, plus generated subtests.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all 32 parser-warning rows
  visually resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing.
- Astro diagnostics: **348 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,811 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 714, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,811 HTML files** checked; every internal link resolved and
  50,655 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 104,776,941 bytes** verified; manifest SHA-256
  `c390e1956b8b8cf3178bc78e26396af5584563f85f3ecb1427cea879c0c55bea`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 70 public artifacts, and 715 candidate substrings checked with **0
  unexpected boundary matches**.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,883 files /
  305,960,557 bytes**, SHA-256
  `d9ea533f8ac53276ebde01593ba38a50526369ff56f8ae862a518091b579a4ca`.

Release commit
[`19cb1f521b15c5ddc34060aa597e618d0e1207e0`](https://github.com/therealjameswilson/before-oss/commit/19cb1f521b15c5ddc34060aa597e618d0e1207e0)
was published to `main`. The independent
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37176306283)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37176306284)
both completed successfully. GitHub reported only prospective runner/action
deprecation notices: selected actions are being forced from Node.js 20 to 24,
and `ubuntu-latest` is scheduled to migrate to Ubuntu 26. Neither notice
affected this release.

The read-only live verifier compared the deployed site with that immutable
commit and verified **67 assets / 104,776,941 bytes**, the same manifest
SHA-256 shown above, **eight core routes**, **30 source-register pages**, and
all **23 Batch 714 direct profile URLs** at
<https://therealjameswilson.github.io/before-oss/>. Targeted live checks also
confirmed the exact home-page coverage figures; Bjarne Oen's high-confidence
FO IV military pathway; Charles Z Offin's qualified documented-prewar
publishing affiliation; Edward W Oexner's probable identity and
archival-review status; and John L Ofax's visible OFAK conflict and explicit
instruction not to merge the records.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-714 --page 347 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-714 --max-queries 23
python3 -m oss_research research --source loc --batch batch-714 --max-queries 23
python3 -m oss_research research --source web --batch batch-714 --resume --max-queries 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch714.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page347-odgers-offut-review_batch-714_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 348, row 1 (Julian A
Oflaherty). No API key, raw API response, full service number, copyrighted
page image, unrelated Army coded occupation, street address, modern
people-finder record, or private reviewer note is committed or published. No
authenticated NARA Catalog API request was made for this batch.
