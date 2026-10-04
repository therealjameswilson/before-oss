# Batch 718 release - Oliver-Olson research

Research and release date: 2026-10-04 America/New_York.

## Historical work

Batch 718 covers PDF page 349, rows 24-46, from Maida O Oliver through
Clinton L Olson. A 300-dpi visual inspection confirmed all 23 printed rows,
representing 23 active person entities. Original spellings, ranks, grades,
box numbers, and archival locations remain recoverable from the immutable
source rows. Nicholas V Olos is in Box 571; the other 22 rows are in Box 572
at location 230/86/37/07.

Four people receive high-confidence identity matches from the official Army
bulk file: Victor M Oliveria, Richard P Ollenburg, Erling M Olsen, and Rodney
E Olsen. Each match uses the exact printed name plus a nonshared protected
identifier. Those identifiers remain private. No coded Army occupation was
converted into occupation or employer evidence.

Nicholas V Olos remains conflicting. His protected identifier reaches an Army
bulk record for Nicholas V Olds, but the surname difference cannot be silently
corrected. Both spellings remain visible and the Box 571 file is required
before any merge or correction.

John E Olsen remains separate from source-derived John E Olson on PDF page
350. The Army bulk name agrees with Olsen, but the same protected identifier
is printed on both index rows. The profiles remain linked in the
`serial-conflict:13175112` possible-duplicate group, while the complete
identifier is excluded from the public site. Boxes 572 and 573 must be
compared before any merge.

Clinton L Olson receives a high-confidence identity match from his
first-person Association for Diplomatic Studies and Training oral history.
The distinctive exact name, indexed major rank, Army chronology, and explicit
account of 1944-45 OSS Secret Intelligence service align. His last documented
assignment before OSS was as an Army ordnance officer and deputy in the U.S.
Military Supply Mission to the Soviet Union, beginning in September 1941. It
is published as `probable_immediate`: the chronology is strong, but the
transcript does not explicitly say that he transferred directly from the
mission to OSS. His 1941 Production Control Officer assignment in the Office
of the Chief of Ordnance is published as earlier pre-OSS military service.
His Stanford Graduate School of Business attendance is separately modeled as
student status, never as employment. The transcript mentions unnamed work in
Los Angeles after high school, so no civilian employer is invented.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed. The web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed the required
official, exact-name OSS, employment, occupation, obituary, institutional,
newspaper, directory, military, spelling-variant, and archival source families
for every person.

The cohort records 15 `no_reliable_result_after_protocol`, five
`requires_archival_review`, two `conflicting_sources`, and one `completed`
outcome. Identity statuses are five `high_confidence`, 16 `unresolved`, one
`ambiguous`, and one `conflicting`. The reviewed bundle imports three sources,
three organizations, three affiliations, 10 claims, 18 claim-source links, 23
person updates, and 23 consolidated research attempts. Four accepted and
three conflicting identity-review decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,552 (39.9014%) |
| People with confirmed/high employer evidence | 326 (1.3618%) |
| People with confirmed/high affiliation evidence | 725 (3.0285%) |
| Archival-review dispositions assessed | 8,010 (33.4600%) |
| Not started | 14,382 |
| Possible duplicate groups | 523 |
| Conflicts | 301 |
| Attempts or plans | 17,358 |
| Claims by confidence | confirmed 1,352; high 2,817; medium 1,508; low 198; conflicting 260; unresolved 2 |
| Citation records / unique source documents | 5,599 / 2,811 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 185; `conflicting_sources` 258;
`documented_prewar_employer_found` 160; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,112; `not_started` 14,382;
`occupation_only_found` 1,040; `requires_archival_review` 3,805; and
`verified_employer_found` 285.

The public projection contains 2,441 published affiliations, 846
organizations, 4,380 public sources, and 5,930 published claims. The
oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Verification and publication

The exact rebuilt tree passed these local release gates:

- Python unit suite: 139 / 139 passed, plus generated subtests.
- Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick
  check `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
- Astro diagnostics: 352 files, 0 errors, 0 warnings, 0 hints.
- Production build: 24,823 pages.
- Browser release suite: 87 / 87 passed across desktop, phone, and tablet (18
  Batch 718, 33 core, six analytics, and 30 accessibility checks).
- Link check: 24,823 HTML files checked; every internal link resolved and
  50,676 unique external URLs were inventoried for the separate live check.
- Public manifest: 67 assets / 105,056,998 bytes verified; manifest SHA-256
  `f2fe58f41953c6c2b02c3d44cb943807bbd20800d9e3f914448da1c32792669f`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,895 public artifacts, and 1,159 candidate substrings checked
  with zero unexpected boundary matches.
- Production dependency audit: zero vulnerabilities. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at 24,895 files / 306,441,871
  bytes, SHA-256
  `84e1ad3f0d94df69c098749f089d17cc2eee72b0165f97bcab06106a69fd4ae8`.

Release commit
[`d820d2f434c018bd7c28e351f4671b6cd2f45997`](https://github.com/therealjameswilson/before-oss/commit/d820d2f434c018bd7c28e351f4671b6cd2f45997)
was published to `main`. Its
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37182300068)
and
[GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/37182300101)
both completed successfully. GitHub reported only prospective runner/action
deprecation notices: selected actions are being forced from Node.js 20 to 24,
and `ubuntu-latest` is scheduled to migrate to Ubuntu 26. Neither notice
affected this release.

The read-only live verifier compared the deployed site with that immutable
commit and verified 67 assets / 105,056,998 bytes, the same manifest SHA-256,
eight core routes, 30 source-register pages, and all 23 Batch 718 direct
profile URLs at <https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-718 --page 349 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-718 --max-queries 23
python3 -m oss_research research --source loc --batch batch-718 --max-queries 23
python3 -m oss_research research --source web --batch batch-718 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch718.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page349-oliver-olson-review_batch-718_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 350, row 1. No API key, raw API
response, full service number, copyrighted page image, unrelated Army coded
occupation, street address, modern people-finder record, or private reviewer
note is committed or published. No authenticated NARA Catalog API request was
made for this batch.
