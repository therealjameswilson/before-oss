# Batch 745 release - Pendleton-Peratino research

Research and local release verification date: 2026-10-05 America/New_York.

## Historical work

Batch 745 publishes reviewed outcomes for PDF page 363, rows 1-23, from
Kathryn M Pendleton through the two separately indexed William Peratino rows.
All 23 printed rows were visually checked against a 300-dpi page render.
Original spellings, ranks, boxes, notes, locations, and protected identifiers
remain recoverable in the private database. Full protected identifiers remain
private, and the two William Peratino source records remain separate people.

The strongest new institutional finding is Stephen B. L. Penrose Jr. A Whitman
College archival finding aid documents his chronology, including employment
as assistant director of the Near East College Association before he entered
OSS service on 1942-05-10. A direct OSS Cairo interview transcript confirms
the indexed person's identity. The association is therefore published as a
strongly date-bounded immediate pre-OSS affiliation and last civilian
employer, not as explicit recruitment evidence. Earlier, separately labeled
prewar teaching at the American University of Beirut, Whitman College, and
Rockford College is also published.

Michael P. Penetar is linked at high confidence to a contemporary University
of Scranton record identifying him as a student in the class of 1942. The
university is published as student status, not as an employer. Elias John
Pepper is linked at high confidence to a contemporary Pacific Electric
biography, which documents initial employment in the Panama Railroad's New
York offices after high school and evening study at Hunter College. The
Panama Railroad relationship is classified as documented prewar employment,
not as an immediate or last civilian employer. The source's name variants are
preserved, and the conflicting Army bulk spelling remains visibly qualified.

The corporal William Peratino is confirmed by an exact name, rank, and
protected-identifier match in a direct OSS interview transcript. That source
documents a civilian occupation in accounting and auditing before Army
service, but names no employer; the profile therefore reports occupation only.
It separately reports Benjamin Franklin University student status. The first
lieutenant indexed under the same name remains unresolved and in identity
review rather than inheriting the corporal's evidence.

Exact-name, nonshared protected-identifier matches in official Army bulk data
are accepted for Anial Pennell, Anthony Pepe, Herbert Penny, Louis Pepin,
Michael Penetar, Morris Penn, Nelson Pepin, Rylie Penn, Stanley Pepera, William
Pennington, and the corporal William Peratino. Those matches establish identity
only; no coded Army occupation is converted into an employer or occupation
claim. Clement B Penrose's source/Army suffix disagreement and John P
Pennsovecchi's surname disagreement remain probable and visibly qualified.
Other unresolved records are routed to archival review rather than assigned
speculative affiliations.

CIA Reading Room access failed under the site's access policy and the Library
of Congress adapter timed out. Both are recorded as source-access failures,
not negative evidence. Exact-name OSS, employment/occupation, obituary,
institutional, directory/newspaper, military, and archival searches were
reviewed for all 23 people. The reviewed evidence bundle imports seven
sources, eight organizations, nine affiliations, 25 claims, 49 claim-source
links, 23 person updates, and 23 completed research attempts. Fourteen identity
decisions are recorded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,165 (42.4621%) |
| People with confirmed/high employer evidence | 339 (1.4161%) |
| People with confirmed/high affiliation evidence | 760 (3.1747%) |
| Archival-review dispositions assessed | 8,624 (36.0249%) |
| Not started | 13,769 |
| Possible duplicate groups | 526 |
| Conflicts | 338 |
| Claims by confidence | confirmed 1,392; high 3,050; medium 1,545; low 198; conflicting 297; unresolved 2 |
| Citation records / unique source documents | 5,769 / 2,929 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 194; conflicting_sources 292;
documented_prewar_employer_found 171; in_progress 1,902;
needs_identity_review 474; needs_temporal_review 24;
no_reliable_result_after_protocol 1,156; not_started 13,769;
occupation_only_found 1,049; requires_archival_review 4,281; and
verified_employer_found 293.

The public projection contains 23,939 person entities, 2,515 published
affiliations, 877 organizations, 4,545 public sources, and 6,277 published
claims. Full-index historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed, plus 78 generated subtests.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 379 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,855 pages.
* Browser release suite: 90 / 90 checks passed across desktop, phone, and
  tablet, including 21 Batch 745, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,855 HTML files checked; every internal link resolved and
  50,783 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 107,110,184 bytes verified; manifest SHA-256
  `e4645777fe6aa42708b4e554a9d000a4a43cc2f6e3724268083c4ccdeed126f4`.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,927 public artifacts, and 1,209 candidate substrings checked;
  zero unexpected boundary matches.
* Two consecutive production builds reproduced the 24,927-file,
  309,828,510-byte output tree at SHA-256
  `220fcb34a8e0a887cf3d39a180692c81da688dded2a88c9a4dc89926cbf2abb9`.

## Publication verification

Batch 745 was published from commit
[`3068490`](https://github.com/therealjameswilson/before-oss/commit/3068490de2b0694d3b34a2b8fa7710fea28b011b).
The [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37264975848)
and [GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/37264975841)
both completed successfully. Immutable live verification against that commit
confirmed 67 assets totaling 107,110,184 bytes at manifest SHA-256
`e4645777fe6aa42708b4e554a9d000a4a43cc2f6e3724268083c4ccdeed126f4`,
eight core routes, 31 source-register pages, and all 23 directly updated
profiles at <https://therealjameswilson.github.io/before-oss/>.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-745-pendleton-peratino --page 363 --first-row 1 --last-row 23
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-05_batch745.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page363-pendleton-peratino-review_batch-745_2026-10-05.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next research boundary is PDF page 363, beginning with row 24. No API key,
raw API response, full service or officer number, copyrighted page image,
unrelated Army coded occupation, street address, modern people-finder record,
or private reviewer note is committed or published. No authenticated NARA
Catalog API request was made for this batch.
