# Batch 720 release - Omeara-Oneill research

Research and local release verification date: 2026-10-04 America/New_York.

## Historical work

Batch 720 covers PDF page 350, rows 24-46, from Eugene F Omeara through the
second William F Oneill row. A 300-dpi visual inspection and embedded-text
comparison confirmed all 23 printed rows, representing 23 active person
entities. Original spellings, ranks, grades, boxes, notes, and archival
locations remain recoverable from the immutable source rows. Eugene Omeara and
Walter Omeara are in Box 573; the remaining 21 rows are in Box 574 at location
230/86/37/07. Unusual printed forms including `OnaHary`, `Onativia`, and the
separate `Oneal`, `Oneil`, and `Oneill` spellings are not silently corrected.

Walter A Omeara is linked with high confidence to advertising executive Walter
A. O'Meara. A Minnesota Historical Society finding aid supplies his detailed
employment chronology, and an independent Los Angeles Times obituary directly
connects the exact name to the OSS planning role. His 1942 return to J. Walter
Thompson is published only as a medium-confidence, probable-immediate
affiliation because the finding aid does not explicitly say that he left the
agency to join the OSS. His earlier work at Benton & Bowles and the Duluth News
Tribune is published separately as high-confidence documented prewar
employment. No single last civilian employer before service is invented.

The printed Charles K Oneil row is linked with high confidence to Charles
Kendall O'Neill through the nonshared protected identifier, transparent
apostrophe normalization, and a Dartmouth institutional biography. His 1930s
freelance writing is modeled as self-employment and documented prewar work, not
as a named employer or an immediate pre-OSS affiliation.

Cornelia Oneill is linked with high confidence to Cornelia Rockwell O'Neill
through a detailed obituary that documents her OSS service. Her attendance at
Smith College and the University of Minnesota is published as qualified
student status, never as employment. Thomas Oneal, Ray B Oneill, and Robert G
Oneill receive high-confidence identity matches from exact indexed names and
nonshared protected identifiers, but no Army code is converted into an
employer or occupation claim.

Dermot M Oneill is published only as a probable match to Dermot Michael "Pat"
O'Neill. The uncommon name and middle initial align with a Washington Post
obituary's Shanghai-Tokyo-Army chronology, but no protected identifier or
personnel-file bridge confirms the identity. The British Embassy in Tokyo is
therefore presented as a qualified, medium-confidence last civilian government
assignment before Army service, and the Shanghai Municipal Police as an
earlier qualified government assignment. The profile does not call him an OSS
operative and explains that Box 574 must establish why his record appears in
the OSS index.

Alan L Oneill remains conflicting because the printed protected identifier
reaches an Army bulk row for Bruce W Johnson. No Army name, occupation, rank,
or other metadata is transferred. The other 15 unresolved people remain
explicit archival-review cases rather than namesake matches.

The CIA and Library of Congress adapters each made one bounded attempt and
failed closed. The web adapter recorded 23 deterministic planned queries
without making live requests. Manual staged review completed the required
official, exact-name OSS, employment, occupation, obituary, institutional,
newspaper, military, punctuation-variant, spelling-variant, and archival
source families for every person. The official 1945 Army Register was searched
for applicable officer candidates. Discovery-only search snippets and
unsupported namesakes were rejected rather than converted into claims.

The cohort records 15 `requires_archival_review`, three
`no_reliable_result_after_protocol`, two
`documented_prewar_employer_found`, one `occupation_only_found`, one
`conflicting_sources`, and one `completed` outcome. Identity statuses are 15
`unresolved`, six `high_confidence`, one `probable`, and one `conflicting`.
The reviewed bundle imports seven sources, eight organizations, eight
affiliations, 16 claims, 27 claim-source links, 23 person updates, and 23
consolidated research attempts. Four accepted and one conflicting Army
identity-review decisions are recorded. Claim confidence within the batch is
nine high, six medium, and one conflicting.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 9,598 (40.0936%) |
| People with confirmed/high employer evidence | 328 (1.3701%) |
| People with confirmed/high affiliation evidence | 728 (3.0411%) |
| Archival-review dispositions assessed | 8,056 (33.6522%) |
| Not started | 14,336 |
| Possible duplicate groups | 523 |
| Conflicts | 305 |
| Attempts or plans | 17,454 |
| Claims by confidence | confirmed 1,355; high 2,832; medium 1,514; low 198; conflicting 264; unresolved 2 |
| Citation records / unique source documents | 5,609 / 2,819 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 187; `conflicting_sources` 262;
`documented_prewar_employer_found` 162; `in_progress` 1,903;
`needs_identity_review` 451; `needs_temporal_review` 24;
`no_reliable_result_after_protocol` 1,122; `not_started` 14,336;
`occupation_only_found` 1,041; `requires_archival_review` 3,832; and
`verified_employer_found` 285.

The public projection contains 2,451 published affiliations, 849
organizations, 4,390 public sources, and 5,958 published claims. Commissioned
status is 2,307 commissioned, 6,078 not commissioned, and 15,554 indeterminate.
The oil-company directory remains nine cited people across eleven historically
named companies. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

- Python unit suite: 139 / 139 passed, plus generated subtests.
- Ingest validation: 23,978 / 23,978 rows, 522 / 522 pages, SQLite quick
  check `ok`, no foreign-key errors, and all 32 parser-warning rows visually
  resolved.
- Astro diagnostics: 354 files, 0 errors, 0 warnings, 0 hints.
- Production build: 24,826 pages.
- Browser release suite: 90 / 90 passed across desktop, phone, and tablet (21
  Batch 720, 33 core, six analytics, and 30 accessibility checks).
- Link check: 24,826 HTML files checked; every internal link resolved and
  50,684 unique external URLs were inventoried for the separate live check.
- Public manifest: 67 assets / 105,209,508 bytes verified; manifest SHA-256
  `8296b62c3e61074a6f2a97510d8c969f01adcc7250f4de7e2471a10fa99bfaef`.
- Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,898 public artifacts, and 1,190 candidate substrings checked
  with zero unexpected boundary matches.
- Production dependency audit: zero vulnerabilities. The static deployment
  has no Node runtime.
- Determinism: consecutive build trees matched at 24,898 files / 306,691,856
  bytes, SHA-256
  `187e43ba5fe1eba667b300ea4827f2aefd91cf5d7f697112be5041a5da40ec5f`.

Publication to GitHub Pages and read-only verification against the immutable
pushed commit are pending at this checkpoint.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-720 --page 350 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-720 --max-queries 23
python3 -m oss_research research --source loc --batch batch-720 --max-queries 23
python3 -m oss_research research --source web --batch batch-720 --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch720.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page350-omeara-oneill-review_batch-720_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The next research boundary begins at PDF page 351, row 1. No API key, raw API
response, full service or officer number, copyrighted page image, unrelated
Army coded occupation, street address, modern people-finder record, or private
reviewer note is committed or published. No authenticated NARA Catalog API
request was made for this batch.
