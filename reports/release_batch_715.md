# Batch 715 release - Oflaherty-Ohara research

Research and release-candidate date: 2026-10-04 America/New_York.

## Historical work

Batch 715 covers PDF page 348, rows 1-23, from Julian A Oflaherty through
James W Ohara. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Original spellings, ranks, grades,
box numbers, archival location, and the index note `possibly` attached to
Marbury B Ogle remain recoverable from the immutable source rows.

Six people receive high-confidence identity matches from the official Army
bulk file: Thomas A Ogden, Ezra G Ogletree, Warren A Ogren, Louis Oguss,
Edward C Ohara, and James F Ohara. Louis Oguss appears in two duplicate Army
rows with the same exact name and protected identifier, producing seven
accepted candidate decisions across six people. Both rows remain in the
private audit trail and are not treated as separate people. Ezra's documented
`Jr.` suffix is preserved as a variant. No Army occupation code was converted
into occupation or employer evidence.

The eighth Army candidate is a material conflict. The visually verified index
prints Edward Ogden, while the protected identifier points to `OGDEE EDWARD`.
The candidate is formally rejected, neither spelling overwrites the other,
and Box 569 is required before any merge.

Marbury B Ogle reaches high-confidence identity as Marbury Bladen Ogle Jr.
A Purdue-authored obituary explicitly states that he served as senior
organizational analyst in a Department of Justice special war policy unit in
1943-44 and then joined the OSS Analysis Branch. The public profile therefore
distinguishes that immediate pre-OSS government assignment from his last
civilian employer, Western Reserve University (1937-42), and his earlier Ohio
State political-science employment through 1937. Western Reserve's historical
name is preserved rather than silently replaced by its modern successor.

John F Oglevee remains a probable identity. Official Ohio State Board of
Trustees minutes document a John F. Oglevee as a Reader in History effective
January 1, 1944. The affiliation is published at medium confidence with
`temporal_relation_uncertain`; it is not labeled immediate pre-OSS or last
civilian employment until Box 569 establishes the sequence. Dorothy T Ogata
also remains a probable identity: a scholarly study names a Dorothy Ogata as
an OSS colleague but omits the middle initial and supplies no pre-OSS
employer.

Patrick Ohanlon reaches high-confidence identity as British Intelligence
Corps lieutenant-colonel Patrick Hudson O'Hanlon through the uncommon name,
matching rank, and an official London Gazette notice of a U.S. Medal of
Freedom with Bronze Palm. The profile does not label the Intelligence Corps
role an immediate predecessor because the notice does not document the OSS
transition chronology.

Postwar-only records, namesakes, modern people-search results, genealogy
pages, and sources that did not establish a pre-OSS sequence were rejected or
retained only as private discovery leads. The CIA and Library of Congress
adapters each made one bounded attempt and failed closed. The web adapter
recorded 23 deterministic planned queries without making live requests.
Manual staged review completed the required source families for all 23
people.

The cohort records 18 `no_reliable_result_after_protocol`, two
`requires_archival_review`, one `completed`, one `needs_temporal_review`, and
one `conflicting_sources` outcome. Identity statuses are eight
`high_confidence`, two `probable`, one `conflicting`, and 12 `unresolved`.
The reviewed bundle imports six sources, three organizations, four
affiliations, 15 claims, 26 claim-source links, 23 person updates, and 23
consolidated research attempts. Eight identity-review decisions are recorded:
seven accepted candidate rows representing six people and one rejected
conflict.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,483 (39.6132%) |
| People with confirmed/high employer evidence | 326 (1.3618%) |
| People with confirmed/high affiliation evidence | 722 (3.0160%) |
| Archival-review dispositions assessed | 7,941 (33.1718%) |
| Not started | 14,451 |
| Possible duplicate groups | 523 |
| Conflicts | 296 |
| Attempts or plans | 17,214 |
| Claims by confidence | confirmed 1,352; high 2,793; medium 1,504; low 198; conflicting 257; unresolved 2 |
| Citation records / unique source documents | 5,584 / 2,800 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 182; `conflicting_sources` 253;
`documented_prewar_employer_found` 158; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,061; `not_started` 14,451;
`occupation_only_found` 1,040; `requires_archival_review` 3,797; and
`verified_employer_found` 285.

The public projection contains 2,431 published affiliations, 837
organizations, 4,365 public sources, and 5,899 published claims. The
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
  invariant passing.
- Astro diagnostics: 349 files, 0 errors, 0 warnings, 0 hints.
- Production build: 24,814 pages.
- Browser release suite: 93 / 93 passed across desktop, phone, and tablet (24
  Batch 715, 33 core, six analytics, and 30 accessibility checks).
- Link check: 24,814 HTML files checked; every internal link resolved and
  50,661 unique external URLs were inventoried for the separate live check.
- Public manifest: 67 assets / 104,859,557 bytes verified; manifest SHA-256
  `cd9e1f891bb0cdb0e8635853f44209d0206c0b2231478ba5e6271499d209781d`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 70 public artifacts, and 717 candidate substrings checked with
  zero unexpected boundary matches.
- Production dependency audit: zero vulnerabilities. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at 24,886 files / 306,102,619
  bytes, SHA-256
  `409abb8643655a8119a3619a28a0e18f27320b3ad6d49c7b3bc7093ac50205e5`.

Release commit
[`787887b098fe641441d92ff941b4a08cf462b95b`](https://github.com/therealjameswilson/before-oss/commit/787887b098fe641441d92ff941b4a08cf462b95b)
was published to `main`. The independent
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37178340145)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37178340159)
both completed successfully. GitHub reported only prospective runner/action
deprecation notices: selected actions are being forced from Node.js 20 to 24,
and `ubuntu-latest` is scheduled to migrate to Ubuntu 26. Neither notice
affected this release.

The read-only live verifier compared the deployed site with that immutable
commit and verified 67 assets / 104,859,557 bytes, the same manifest SHA-256,
eight core routes, 30 source-register pages, and all 23 Batch 715 direct
profile URLs at <https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-715 --page 348 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-715 --max-queries 23
python3 -m oss_research research --source loc --batch batch-715 --max-queries 23
python3 -m oss_research research --source web --batch batch-715 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch715.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page348-oflaherty-ohara-review_batch-715_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 348, row 24 (John H Ohara) and
runs through row 46 (Aase Olafsen). No API key, raw API response, full service
number, copyrighted page image, unrelated Army coded occupation, street
address, modern people-finder record, or private reviewer note is committed or
published. No authenticated NARA Catalog API request was made for this batch.
