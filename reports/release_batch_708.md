# Batch 708 release - Norberg-Norris research

Research and release date: 2026-10-03 America/New_York.

## Historical work

Batch 708 covers PDF page 344, rows 23-46, from Willard P Norberg through Karl
H Norris. Fresh 300-dpi visual inspection confirmed all 24 printed rows,
representing 24 active person entities. The immutable extraction is unchanged.
Jackson E Nordin's already-terminal pilot disposition was rechecked and
retained.

Official Army evidence supports six high-confidence identity-only decisions:
Willard P Norberg, John B Nordmann, Frederick C Nordsiek, Kenneth R Nordwall,
Maurice O Normandin, and Ira E Norrell. An OSS Operational Groups roster
supports Albert Nordang's NORSO II identity. A 1944 OSS Cairo report identifies
Harold E Nordblom at the OSS Cyprus base; that wartime duty is not converted
into pre-OSS employer evidence.

The site publishes three affiliations. Christopher Sverre Norborg was an
Assistant Professor of Philosophy at the University of Minnesota in 1940-1941;
this is a dated last civilian employer, not an immediate-pre-OSS claim. Johan
Nordentoft was chief of staff of the Danish Army's Zealand Division from 1942
to 29 August 1943; the site labels this only as a military assignment with an
uncertain temporal relation to OSS, and his overall workflow status is
`completed`. Jens Henrik Throne Nordlie was office manager at Narvesens
Kioskkompani from 1941 into early 1943; the site publishes that as a strongly
date-bounded last civilian employer without asserting immediate succession.

Guy E Norbert versus Norbert C Guy and Carl W Nordsiek versus Carl W Nordsieck
remain visible name conflicts. Brunnon C Normand and Karl H Noris/Karl H Norris
remain unmerged possible-duplicate cases. Both Karl rows preserve their own
profiles and show only a masked serial suffix. The CIA and LoC adapters failed
closed; the staged protocol was nevertheless completed for all 24 people using
accessible official, institutional, contemporary, military, newspaper,
obituary, and archival sources.

The cohort records 15 `no_reliable_result_after_protocol`, five
`conflicting_sources`, one `completed`, one `requires_archival_review`, one
`documented_prewar_employer_found`, and one `verified_employer_found` outcome.
Identity statuses are 11 `high_confidence`, three `probable`, two
`conflicting`, and eight `unresolved`. The evidence bundle adds nine sources,
three organizations, three affiliations, 19 claims, 39 claim-source links, 24
person updates, and 24 research attempts. Claims comprise 14 high-confidence,
three medium-confidence, and two conflicting decisions.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,323 (38.9448%) |
| People with confirmed/high employer evidence | 322 (1.3451%) |
| People with confirmed/high affiliation evidence | 713 (2.9784%) |
| Archival-review dispositions assessed | 7,781 (32.5034%) |
| Not started | 14,611 |
| Possible duplicate groups | 523 |
| Conflicts | 283 |
| Attempts or plans | 16,872 |
| Claims by confidence | confirmed 1,352; high 2,731; medium 1,489; low 196; conflicting 254; unresolved 2 |
| Citation records / unique source documents | 5,541 / 2,764 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 177; `conflicting_sources` 240;
`documented_prewar_employer_found` 157; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 938; `not_started` 14,611;
`occupation_only_found` 1,039; `requires_archival_review` 3,783; and
`verified_employer_found` 283.

The public projection contains **2,415** published affiliations, **827**
organizations, **4,324** public sources, and **5,819** published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these release gates:

- Python unit suite: **139 / 139 passed**, plus **78 / 78** parametrized
  subtests. Python 3.14 emitted existing unclosed-connection resource warnings;
  the suite exited successfully.
- Ingest validation: **23,978 / 23,978 rows**, **522 / 522 pages**, SQLite
  quick check `ok`, no foreign-key errors, and all parser-warning rows visually
  resolved.
- Stratified profile audit: **200 profiles**, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing.
- Astro diagnostics: **342 files**, **0 errors, 0 warnings, 0 hints**.
- Production build: **24,803 pages**.
- Browser release suite: **90 / 90 passed** across desktop, phone, and tablet
  (21 Batch 708, 33 core, six analytics, and 30 accessibility checks).
- Link check: **24,803 HTML files** checked; every internal link resolved and
  50,627 unique external URLs were inventoried for the separate live check.
- Public manifest: **67 assets / 104,388,435 bytes** verified; manifest SHA-256
  `e853566a43f3f7daee30080d755f80938c412545f7dcf43536888b88f5f008ca`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,875 artifacts, and 1,159 candidate substrings checked with **0
  unexpected boundary matches**. Two numeric matches inside the public manifest
  were recognized as harmless file-size values.
- Production dependency audit: **0 vulnerabilities**. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at **24,875 files /
  305,326,420 bytes**, SHA-256
  `161fb50aec87d9781e36e3c4c8031029cc639b1afa713f23ba756498409e9fa8`.

The unbounded historical Playwright aggregate remains too large for one Node
process because the legacy specifications repeatedly retain the large people
dataset and exhaust an 8 GB heap. This is a runner-resource limitation, not a
known product failure. The bounded release suite exercises the core routes,
Batch 708 profiles, analytics, responsive layouts, and accessibility across
all three configured browser projects.

## Release status

The reviewed Batch 708 release is locally verified and ready to fast-forward
to `main`. GitHub Pages deployment and byte-for-byte live verification will be
recorded here after the workflows complete.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-708a --page 344 --first-row 23 --last-row 31
python3 -m oss_research assign-page-batch --batch-name batch-708b --page 344 --first-row 33 --last-row 46
python3 -m oss_research research --source cia --batch batch-708a --max-queries 9
python3 -m oss_research research --source cia --batch batch-708b --max-queries 14
python3 -m oss_research research --source loc --batch batch-708a --max-queries 9
python3 -m oss_research research --source loc --batch batch-708b --max-queries 14
python3 -m oss_research research --source web --batch batch-708a --resume --max-queries 9
python3 -m oss_research research --source web --batch batch-708b --resume --max-queries 14
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-03_batch708.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page344-norberg-norris-review_batch-708_2026-10-03.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 345, row 1 (Laura M Norris). No
API key, raw API response, full service number, copyrighted page image,
unrelated Army coded occupation, street address, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
