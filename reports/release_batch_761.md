# Batch 761 release - Pittard-Pizor research

Research and local release verification date: 2026-10-12 America/New_York.

## Historical work

Batch 761 publishes reviewed outcomes for PDF page 370, rows 37-46, from
Murcil M Pittard through James P Pizor. All ten printed rows were visually
checked against a 300-dpi page render. Original spellings, ranks, boxes, notes,
locations, and protected identifiers remain recoverable in the private
database. Full protected identifiers remain private.

The ten source rows remain linked to ten separate person entities. Three
row-specific official Army candidates were reviewed. Exact-name,
nonshared-identifier matches for Frank S Pittillo and Lawrence R Pitts were
accepted as identity evidence only. Robert F Pitts retains an explicit
conflict because the official Army record at his indexed identifier names
Dovidio Alfonso; the mismatched record was not linked and none of its metadata
was transferred to Robert.

Three institutional sources support qualified, medium-confidence student
affiliations. A Wake Forest College bulletin names Murcil Monroe Pittard as a
student in the 1923-1924 session. Hunter College's official 14 June 1933
commencement program lists Felicetta Pittaro as a Bachelor of Arts candidate.
Grove City College's institutional honor roll identifies James Pizor with the
class of 1940, while the Field Artillery Officer Candidate School alumni roster
lists James P Pizor in class 8-42, which began 22 January and graduated 16
April 1942. These affiliations are published as documented-prewar student
relationships. None is labeled employment, an immediate pre-OSS affiliation,
or a last civilian employer.

An official Congressional Record entry establishes Colonel Otto G Pitz's full
name and Coast Artillery context at high identity confidence. Because that
record is dated 16 July 1942, it is used for identity only and is not presented
as proof that the assignment preceded OSS service. A separate official 1938
Army assignment lead could not be retrieved from its access-restricted source
and is not published as evidence.

Murcil Pittard, Felicetta Pittaro, and James Pizor remain probable identities;
Frank Pittillo, Lawrence Pitts, and Otto Pitz are high-confidence identities;
Robert Pitts is conflicting; and Ernest Pittaro, Lillian Pitts, and Donald
Pixley remain unresolved. Nine people have `requires_archival_review`, while
Robert has `conflicting_sources`. No named employer was added. The oil-company
category remains evidence-scoped to nine people across 11 historically named
companies.

The reviewed evidence bundle imports seven source records, three
organizations, three affiliations, ten claims, 19 evidence links, ten person
updates, and ten completed manual staged research protocols. The CIA cohort
adapter stopped because its robots policy could not be retrieved, and the
Library of Congress cohort check stopped on a transport error. These are
recorded as source-access failures rather than negative evidence. No
authenticated NARA Catalog API request was made, and no API key or raw API
response was stored.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 10,508 (43.8949%) |
| People with confirmed/high employer evidence | 345 (1.4412%) |
| People with confirmed/high affiliation evidence | 781 (3.2625%) |
| Archival-review dispositions assessed | 8,966 (37.4535%) |
| Not started | 13,426 |
| Possible duplicate groups | 536 |
| Conflicts | 354 |
| Claims by confidence | confirmed 1,400; high 3,203; medium 1,575; low 198; conflicting 307; unresolved 2 |
| Citation records / unique source documents | 5,873 / 3,011 |

Research statuses are: blocked_by_source_access 1; candidate_found 333;
completed 198; conflicting_sources 298; documented_prewar_employer_found 175;
in_progress 1,902; needs_identity_review 535; needs_temporal_review 25;
no_reliable_result_after_protocol 1,156; not_started 13,426;
occupation_only_found 1,053; requires_archival_review 4,540; and
verified_employer_found 297.

The private database contains 2,576 affiliations, 911 organizations, 19,352
research attempts or plans, and 5,873 citation records. The public projection
contains 23,939 person entities, 2,553 published affiliations, 895
organizations, 4,649 public sources, and 6,478 published claims. Full-index
historical research remains unfinished.

## Local verification

The exact rebuilt tree passed these local release gates:

* Python unit suite: 139 / 139 passed.
* Ingest validation: all seven extraction and SQLite integrity checks passed.
* Stratified profile audit: 200 profiles across all four difficulty tiers and
  required personnel, confidence, duplicate, and conflict strata passed all
  seven structural checks.
* Astro diagnostics: 395 files, 0 errors, 0 warnings, 0 hints.
* Production build: 24,873 pages.
* Browser release suite: 87 / 87 checks passed across desktop, phone, and
  tablet, including 18 Batch 761, 33 core, six analytics, and 30 accessibility
  checks.
* Link check: 24,873 HTML files checked; every internal link resolved and
  50,863 unique external URLs were inventoried for the separate live check.
* Public manifest: 67 assets / 108,305,152 bytes verified; manifest SHA-256
  e21e9550a34ccb65137538331ebdc4bdc3897907fca65b6b29f8e2c8cc83f9fd.
* Private-identifier audit: 12,926 normalized identifiers, 120 formatted
  variants, 24,945 public artifacts, and 1,244 candidate substrings checked;
  zero aggregate false positives, manifest-size false positives, or unexpected
  boundary matches.
* Two consecutive production builds reproduced the 24,945-file,
  311,732,200-byte output tree at SHA-256
  1d06af9b81cc2bf0987844ab7b7f2eca1630eb1e509ac4a7b4ea4b8fe38bd87b.

## Publication verification

Release commit 1da3698ef1cab3048062dada69ff2309d39e9070 was pushed to
main. The [GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38340864212)
completed successfully at 2026-10-13T03:17:18Z, and the
[Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/38340864288)
completed successfully at 2026-10-13T03:20:24Z.

An unauthenticated immutable verification completed before
2026-10-13T03:20:42Z and confirmed the deployed commit and 67 public assets
totaling 108,305,152 bytes, with manifest SHA-256
e21e9550a34ccb65137538331ebdc4bdc3897907fca65b6b29f8e2c8cc83f9fd.
The verifier also checked eight core routes, all 31 source-register pages, and
all ten direct Batch 761 profile routes at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-761-pittard-pizor --page 370 --first-row 37 --last-row 46
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-12_batch761.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page370-pittard-pizor-review_batch-761_2026-10-12.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

The next unresearched person boundary is PDF page 371, row 1, Olga Pizzorno.
No API key, raw API response, full service or officer number, copyrighted page
image, unrelated Army coded occupation, street address, modern people-finder
record, or private reviewer note is committed or published.
