# Batch 716 release - Ohara-Olafsen research

Research and release date: 2026-10-04 America/New_York.

## Historical work

Batch 716 covers PDF page 348, rows 24-46, from John H Ohara through Aase
Olafsen. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Original spellings, ranks, grades,
box numbers, notes, and archival locations remain recoverable from the
immutable source rows.

Three people receive high-confidence identity matches from the official Army
bulk file: Ole P Oines, Leif Oistad, and Tito U Okamoto. Each match uses the
exact printed name and a nonshared protected identifier. Those identifiers
remain private. No coded Army occupation was converted into occupation or
employer evidence.

Louis A Ojibway reaches high-confidence identity as Louis Austin O'Jibway. A
CIA Center for the Study of Intelligence article cites his OSS requisition in
Entry 224, Box 570 and identifies his immediate pre-OSS assignment as athletic
director at the Cavalry Replacement Training Center, Fort Riley. The public
profile separately records his earlier 1st Cavalry Division physical-training
assignment and student status in petroleum engineering at the University of
New Mexico. The source mentions summer work as a roughneck but names no
employer, so this remains occupation-only evidence and does not place Ojibway
in the oil-company directory.

Leif Oistad reaches high-confidence identity through the exact protected Army
identifier plus independently matching rank, unit, NORSO assignment, and
chronology. His immediate pre-OSS affiliation is the 99th Infantry Battalion
(Separate) at Camp Hale, where he was a sergeant and ski instructor. A
reputable obituary explicitly says the OSS recruited him from that
assignment. It also documents deckhand work on commercial ships, including
the tanker *Brasil*, but does not name an employer. The ship's owner or
operator is not inferred as Oistad's employer, and he is not placed in the
oil-company directory.

Takashi Ohta reaches high-confidence identity through the rare exact name and
a visually inspected April 1945 OSS travel order. A separate art-history
source documents his 1928 employment as a set designer for the Provincetown
Players and as set designer and scenic director at the Maverick Theatre. Both
roles appear at medium confidence as `documented_prewar`; neither is labeled
immediate or last civilian employment because the intervening chronology is
unknown.

Prince Olaf remains unresolved. The index entry does not justify equating him
with Crown Prince Olav of Norway, and Box 571 requires archival examination.
The printed note `recomm` remains recoverable without expansion. Fred K
Okamoto and Mary N Okamoto likewise require their personnel files before any
identity or relationship can be established. Common-name and incomplete-name
cases remain unresolved rather than being attached to convenient biographies.

The CIA and Library of Congress adapters each made one bounded attempt for
Daniel G Okeeffe and failed closed. The web adapter recorded 23 deterministic
planned queries without making live requests. Manual staged review completed
the required official, exact-name OSS, employment, occupation, obituary,
institutional, newspaper, directory, military, and archival source families
for every person.

The cohort records 19 `no_reliable_result_after_protocol`, two `completed`,
one `documented_prewar_employer_found`, and one `requires_archival_review`
outcome. Identity statuses are five `high_confidence` and 18 `unresolved`.
The reviewed bundle imports six sources, six organizations, six affiliations,
11 claims, 17 claim-source links, 23 person updates, and 23 consolidated
research attempts. Three accepted identity-review decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,506 (39.7093%) |
| People with confirmed/high employer evidence | 326 (1.3618%) |
| People with confirmed/high affiliation evidence | 724 (3.0244%) |
| Archival-review dispositions assessed | 7,964 (33.2679%) |
| Not started | 14,428 |
| Possible duplicate groups | 523 |
| Conflicts | 296 |
| Attempts or plans | 17,262 |
| Claims by confidence | confirmed 1,352; high 2,802; medium 1,506; low 198; conflicting 257; unresolved 2 |
| Citation records / unique source documents | 5,590 / 2,805 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 184; `conflicting_sources` 253;
`documented_prewar_employer_found` 159; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,080; `not_started` 14,428;
`occupation_only_found` 1,040; `requires_archival_review` 3,798; and
`verified_employer_found` 285.

The public projection contains 2,437 published affiliations, 842
organizations, 4,371 public sources, and 5,910 published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Verification and publication

The exact rebuilt tree passed these local release gates:

- Python unit suite: 139 / 139 passed, plus generated subtests.
- Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick
  check `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
- Stratified profile audit: 200 profiles, with every identity, queue,
  commissioned-category, duplicate-review, source-row, and public-projection
  invariant passing. The women stratum was unavailable because the project
  does not infer gender.
- Astro diagnostics: 350 files, 0 errors, 0 warnings, 0 hints.
- Production build: 24,819 pages.
- Browser release suite: 90 / 90 passed across desktop, phone, and tablet (21
  Batch 716, 33 core, six analytics, and 30 accessibility checks).
- Link check: 24,819 HTML files checked; every internal link resolved and
  50,668 unique external URLs were inventoried for the separate live check.
- Public manifest: 67 assets / 104,943,407 bytes verified; manifest SHA-256
  `8503094c33fe7e3ac65c492d2ac24354305cf1e0256ecee5700088c422f4b17a`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,891 public artifacts, and 1,159 candidate substrings checked
  with zero unexpected boundary matches.
- Production dependency audit: zero vulnerabilities. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at 24,891 files / 306,248,877
  bytes, SHA-256
  `0af2c10d94fc39e53cb3ded37210d769c87b5137c3657024ce135ae8183ff7de`.

Release commit
[`9f6b7d495c0d2d57394beb441eac44b68c39da06`](https://github.com/therealjameswilson/before-oss/commit/9f6b7d495c0d2d57394beb441eac44b68c39da06)
was published to `main`. Its
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37179975575)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37179975570)
both completed successfully. GitHub reported only prospective runner/action
deprecation notices: selected actions are being forced from Node.js 20 to 24,
and `ubuntu-latest` is scheduled to migrate to Ubuntu 26. Neither notice
affected this release.

The read-only live verifier compared the deployed site with that immutable
commit and verified 67 assets / 104,943,407 bytes, the same manifest SHA-256,
eight core routes, 30 source-register pages, and all 23 Batch 716 direct
profile URLs at <https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-716 --page 348 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-716 --person-id dd626e1f-4269-5679-88e5-40722c9f1213 --max-queries 1
python3 -m oss_research research --source loc --batch batch-716 --person-id dd626e1f-4269-5679-88e5-40722c9f1213 --max-queries 1
python3 -m oss_research research --source web --batch batch-716 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch716.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page348-ohara-olafsen-review_batch-716_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 349, row 1 (Paul N Olafsen) and
runs through row 23 (Louise L Oliver). No API key, raw API response, full
service number, copyrighted page image, unrelated Army coded occupation,
street address, modern people-finder record, or private reviewer note is
committed or published. No authenticated NARA Catalog API request was made for
this batch.
