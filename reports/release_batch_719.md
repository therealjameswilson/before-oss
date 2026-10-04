# Batch 719 release - Olson-Omeara research

Research and release date: 2026-10-04 America/New_York.

## Historical work

Batch 719 covers PDF page 350, rows 1-23, from Curtis Olson through Donn M
Omeara. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Original spellings, ranks, grades,
box numbers, notes, and archival locations remain recoverable from the
immutable source rows. The first six rows are in Box 572; the remaining 17
rows are in Box 573 at location 230/86/37/07.

Six people receive high-confidence identity matches from the official Army
bulk file: Curtis Olson, John P Olson, Robert A Olson, Harry A Olwell, John M
Omalley, and Robert C Omalley. Each match uses the exact printed name plus a
nonshared protected identifier. Those identifiers remain private. No coded
Army occupation was converted into occupation or employer evidence.

John E Olson remains separate from source-derived John E Olsen on the previous
page. The same protected identifier is printed on both index rows, while the
Army bulk row uses Olsen. The profiles remain linked in the
`serial-conflict:13175112` possible-duplicate group. Boxes 572 and 573 must be
compared before any merge or correction.

Carla A Oman remains conflicting. Her protected identifier reaches an Army
bulk row for Carl A Oman, but the given-name and sex-marker difference cannot
be silently corrected. Donn M Omeara also remains conflicting: his printed
identifier reaches an Army bulk row for Albert L Monett, an incompatible
name. No Army name, occupation, or other metadata is transferred in either
case; Box 573 review is required.

Joseph H Omalley is confirmed as career Army officer Joseph Henry O'Malley
through the exact officer-number bridge, compatible colonel rank, and name in
the War Department's 1945 *Official Army Register*. The register documents
cadet status at the United States Military Academy from July 1929 through
June 1933 and a career Army Cavalry path beginning as a second lieutenant on
June 13, 1933. West Point is modeled as student status, not employment; the
Army is modeled as a military assignment, not a civilian employer. The
register does not establish O'Malley's immediate pre-OSS assignment, so Box
573 remains necessary and no immediate affiliation is invented.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed. The web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed the required
official, exact-name OSS, employment, occupation, obituary, institutional,
newspaper, directory, military, punctuation-variant, spelling-variant, and
archival source families for every person. Discovery-only namesakes were
rejected rather than converted into claims.

The cohort records 12 `requires_archival_review`, seven
`no_reliable_result_after_protocol`, three `conflicting_sources`, and one
`completed` outcome. Identity statuses are 13 `unresolved`, six
`high_confidence`, two `conflicting`, one `ambiguous`, and one `confirmed`.
The reviewed bundle imports three sources, two organizations, two
affiliations, 12 claims, 22 claim-source links, 23 person updates, and 23
consolidated research attempts. Six accepted and four conflicting
identity-review decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,575 (39.9975%) |
| People with confirmed/high employer evidence | 326 (1.3618%) |
| People with confirmed/high affiliation evidence | 726 (3.0327%) |
| Archival-review dispositions assessed | 8,033 (33.5561%) |
| Not started | 14,359 |
| Possible duplicate groups | 523 |
| Conflicts | 304 |
| Attempts or plans | 17,406 |
| Claims by confidence | confirmed 1,355; high 2,823; medium 1,508; low 198; conflicting 263; unresolved 2 |
| Citation records / unique source documents | 5,602 / 2,813 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 186; `conflicting_sources` 261;
`documented_prewar_employer_found` 160; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,119; `not_started` 14,359;
`occupation_only_found` 1,040; `requires_archival_review` 3,817; and
`verified_employer_found` 285.

The public projection contains 2,443 published affiliations, 846
organizations, 4,383 public sources, and 5,942 published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Verification and publication

The exact rebuilt tree passed these local release gates:

- Python unit suite: 139 / 139 passed, plus generated subtests.
- Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick
  check `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
- Astro diagnostics: 353 files, 0 errors, 0 warnings, 0 hints.
- Production build: 24,823 pages.
- Browser release suite: 87 / 87 passed across desktop, phone, and tablet (18
  Batch 719, 33 core, six analytics, and 30 accessibility checks).
- Link check: 24,823 HTML files checked; every internal link resolved and
  50,676 unique external URLs were inventoried for the separate live check.
- Public manifest: 67 assets / 105,109,619 bytes verified; manifest SHA-256
  `207144057294e637a22b0cc62d5c665bd007a7a6dfd024b07407500cc526c526`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,895 public artifacts, and 1,188 candidate substrings checked
  with zero unexpected boundary matches.
- Production dependency audit: zero vulnerabilities. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at 24,895 files / 306,526,944
  bytes, SHA-256
  `1f1a1da828ff38fce9c18868f480607090bdc22518cff2576b7ee959f2bcb70f`.

Release commit
[`06ae96c7ceec02cce8ff252c0ec80a4f5c186cbc`](https://github.com/therealjameswilson/before-oss/commit/06ae96c7ceec02cce8ff252c0ec80a4f5c186cbc)
was published to `main`. Its
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37184292961)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37184292861)
both completed successfully. GitHub reported only prospective runner/action
deprecation notices: selected actions are being forced from Node.js 20 to 24,
and `ubuntu-latest` is scheduled to migrate to Ubuntu 26. Neither notice
affected this release.

The read-only live verifier compared the deployed site with that immutable
commit and verified 67 assets / 105,109,619 bytes, the same manifest SHA-256,
eight core routes, 30 source-register pages, and all 23 Batch 719 direct
profile URLs at <https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-719 --page 350 --first-row 1 --last-row 23
python3 -m oss_research research --source cia --batch batch-719 --max-queries 23
python3 -m oss_research research --source loc --batch batch-719 --max-queries 23
python3 -m oss_research research --source web --batch batch-719 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch719.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page350-olson-omeara-review_batch-719_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 350, row 24. No API key, raw
API response, full service or officer number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published. No authenticated NARA
Catalog API request was made for this batch.
