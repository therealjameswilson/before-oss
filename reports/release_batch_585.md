# Batch 585 release verification

Verified 2026-09-20 UTC. [PR #296](https://github.com/therealjameswilson/before-oss/pull/296)
merged as commit `d01a71916bc0dd9a2734a887c251235780b5f72d`.
The [PR Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35499900026),
merged-main [Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35500101505),
and [GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/35500101508)
all passed. The public site is
[Before OSS](https://therealjameswilson.github.io/before-oss/), with a
[featured oil-company category](https://therealjameswilson.github.io/before-oss/#oil-companies)
and its [seven-person directory filter](https://therealjameswilson.github.io/before-oss/people/?featured=oil_companies&sort=name_asc).

## Historical scope

Twenty distinct [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf)
rows on PDF page 118, rows 11–30, were checked against a rendered page.
Row 11 is in Box 186; rows 12–30 are in Box 187. The source's clipped
`British A` note for E P Dillon remains literal. Eight accepted
[official Army bulk-file](https://catalog.archives.gov/id/1263923)
crosswalks support high-confidence identity only, without a named employer
or OSS transition date. John B, William J and William F Dillon remain
separate from newspaper namesakes and one another.

[University of Illinois 1937](https://www.trustees.uillinois.edu/trustees/minutes/1937/1937-04-14-uibot.pdf)
and [1938](https://www.trustees.uillinois.edu/trustees/minutes/1938/1938-02-11-uibot.pdf)
trustee minutes establish Konrad C Dillow's graduate fellowship in
Education, ending February 1, 1938. His
[Washington Post obituary](https://www.washingtonpost.com/archive/local/1998/05/18/obituaries/c152246f-16fb-443b-ba74-f03e91dc821b/)
corroborates the distinctive name's University of Illinois graduate study
and wartime Army service in France. The fellowship is published as
**student affiliation**, not university employment or his immediate
pre-OSS affiliation. The university's
[WPA research-project finding aid](https://archon.library.illinois.edu/archives/?id=3207&p=collections%2Fcontrolcard)
is an archival lead, not proof of his job title or employer.

Eleven LoC candidates were assessed: eight rejected and three kept as
private plausible/unresolved leads. A 1944 newspaper employer belonged
to **John T** Dillon Jr, not indexed **John B**; a later Clair F Dillman
employer was not backdated. All twenty records have terminal online
`requires_archival_review` outcomes and Box 186–187 next actions. No
physical personnel file was opened. The NARA Catalog API was not used for
this cohort; the Army data is a separate official bulk file. See
`research/batch-585-terminal-review.md` and its importable evidence and
decision files.

## Reproducible coverage at the released commit

| Measure | Numerator / denominator | Rate |
| --- | ---: | ---: |
| Printed index rows linked | 23,978 / 23,978 | 100% |
| Active person entities with nonplanned research attempts | 5,630 / 23,940 | 23.5171% |
| Confirmed/high published employer evidence | 263 / 23,940 | 1.0986% |
| Confirmed/high published affiliation evidence | 602 / 23,940 | 2.5146% |
| Archival-review disposition assessed | 5,585 / 23,940 | 23.3292% |

The active queue retains 18,310 `not_started`, 43 `in_progress`, and
3,391 `requires_archival_review` people; other statuses are in
`reports/research_coverage.json`. There are 258 possible-duplicate groups
and 124 people with conflicting identity or source evidence. Private SQLite
has 10,376 research attempts and 4,764 claims: 1,307 confirmed, 1,784 high,
1,360 medium, 184 low, and 129 conflicting. It has 4,908 citation records
and 2,251 unique source documents. The reviewed public projection contains
2,169 affiliations, 677 organizations, 3,714 sources, and 4,576 published
claims. These figures do not imply completion of the full index.

## QA and publication evidence

- **110/110** Python tests passed. `validate-ingest` found all 522 PDF pages
  represented, all 23,978 printed rows present, no unresolved parser-warning
  reviews, and no SQLite integrity or foreign-key errors. The existing
  200-profile structural audit passed its available strata; its gender
  stratum still requires sourced person-level evidence.
- Astro checked 214 source files with no errors, warnings, or hints. The
  production build generated **24,649** direct HTML pages. The bounded
  browser release suite passed **72/72** checks across desktop, phone, and
  tablet, including 27 axe accessibility checks with no serious or critical
  violations. The oil-company homepage and directory interactions remained
  in the core tests.
- All internal links in 24,649 HTML pages resolved. The checker inventoried
  50,131 unique external URLs; it did not visit every external target. A
  separate redaction audit scanned 12,926 normalized private identifiers
  and 120 formatted variants across 24,721 public artifacts and found zero
  unexpected full-identifier matches.
- Two Pages-configured builds reproduced identical 70-file public-tree
  SHA-256 `3e9f7b8f30c6432d81ed4b49d4d8f2d9d7045bf5acbd1fe4275646be86138ca2`
  and 24,721-file production-tree SHA-256
  `90532d9c5f7c2ee745bd345a92467cc2fb57b1a99705e3e93943150c844144c0`.
- The local and unauthenticated live manifest verifiers matched all **67
  assets / 96,356,622 bytes**, manifest SHA-256
  `1ef6d8e04a6f80c68b4521fe6a592a848a0e2cf3984ecc1d95ae08bee15131e0`.
  The live verifier also checked seven core routes, all 25 Sources-register
  pages, and all twenty direct Batch 585 profiles against the exact merge
  commit. Publication fidelity does not substitute for historical review.

## Resumption and limits

The next bounded cohort starts at PDF page 118, row 31. Resume from the
existing private SQLite checkpoint using the commands in
`research/batch-585-terminal-review.md`. Boxes 186–187 remain archival
priorities. More than 18,000 people remain `not_started`; the full pre-OSS
research goal is ongoing. The generated aggregate `people.json` is just
over GitHub's recommended 50 MB repository-file threshold; browser-facing
data is partitioned, but repository packaging warrants separate work.
The LoC text service could not yield bounded context for one Laredo page,
and an Alfred Dilello obituary host blocked direct reinspection; neither
lead was promoted to a public employer claim.
