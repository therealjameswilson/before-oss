# Batch 584 release verification

Verified 2026-09-20 UTC. [PR #294](https://github.com/therealjameswilson/before-oss/pull/294)
merged as commit `7401f27a2278710501e825ebb732767965a8696d`.
The [PR Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35497439890),
merged-main [Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35497637702),
and [GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/35497637658)
all passed. The public site is
[Before OSS](https://therealjameswilson.github.io/before-oss/), with a
[featured oil-company category](https://therealjameswilson.github.io/before-oss/#oil-companies)
and its [seven-person directory filter](https://therealjameswilson.github.io/before-oss/people/?featured=oil_companies&sort=name_asc).

## Historical scope

Ten distinct [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf)
rows on PDF page 118, rows 1–10, were checked against the rendered page.
Rows 1–9 are in Box 186 and row 10 in Box 187. The index's truncated
`Norwegi` note for Arne Diesen remains literal; the two adjacent Digiovanni
rows remain separate people. Two accepted
[official Army bulk-file](https://catalog.archives.gov/id/1263923)
crosswalks establish high-confidence identity for Reardon Dight and
Augustine M Digiovanni, but no employer. Three LoC OCR contexts yielded
two rejections and one private unbridged Ed Dieckman police lead.

[University of Florida's finding aid](https://findingaids.uflib.ufl.edu/repositories/2/resources/1226)
and the contemporary [March 1933 *Deltasig*](https://www.deltasigmapi.org/docs/default-source/DELTASIG-Magazine/1930s/1933-deltasig-vol-25-no-3-march.pdf?sfvrsn=1596699b_2)
support Sigismond Diettrich's high-confidence *documented prewar*
employment as a university instructor. They do not establish his exact
immediate predecessor to OSS or a last civilian employer before an
intervening assignment. All ten have terminal online
`requires_archival_review` outcomes and Boxes 186–187 next actions. No
physical personnel file was opened. The NARA Catalog API was not used for
this cohort; the Army data is a separate official bulk file. See
`research/batch-584-terminal-review.md` and its importable evidence and
decision files.

## Reproducible coverage at the released commit

| Measure | Numerator / denominator | Rate |
| --- | ---: | ---: |
| Printed index rows linked | 23,978 / 23,978 | 100% |
| Active person entities with nonplanned research attempts | 5,610 / 23,940 | 23.4336% |
| Confirmed/high published employer evidence | 263 / 23,940 | 1.0986% |
| Confirmed/high published affiliation evidence | 601 / 23,940 | 2.5104% |
| Archival-review disposition assessed | 5,565 / 23,940 | 23.2456% |

The active queue retains 18,330 `not_started`, 43 `in_progress`, and
3,371 `requires_archival_review` people; other statuses are in
`reports/research_coverage.json`. There are 258 possible-duplicate groups
and 124 people with conflicting identity or source evidence. Private SQLite
has 10,316 research attempts and 4,754 claims: 1,307 confirmed, 1,774 high,
1,360 medium, 184 low, and 129 conflicting. It has 4,902 citation records
and 2,247 unique source documents. The reviewed public projection contains
2,168 affiliations, 676 organizations, 3,709 sources, and 4,566 published
claims. These figures do not imply completion of the full index.

## QA and publication evidence

- **110/110** Python tests passed; `validate-ingest` found all 522 PDF pages
  represented, all 23,978 printed rows present, no unresolved parser-warning
  reviews, and no SQLite integrity or foreign-key errors. The existing
  200-profile structural audit passed its available strata; its gender
  stratum still requires sourced person-level evidence.
- Astro checked 213 source files with no errors, warnings, or hints. The
  production build generated **24,648** direct HTML pages. The bounded
  browser release suite passed **75/75** checks across desktop, phone, and
  tablet, including 27 axe accessibility checks with no serious or critical
  violations. The existing oil-company homepage and directory interactions
  remained in the core tests.
- All internal links in 24,648 HTML pages resolved. The checker inventoried
  50,127 unique external URLs; it did not visit every external target.
  A separate redaction audit scanned 12,926 normalized private identifiers
  and 120 formatted variants across 24,720 public artifacts and found zero
  unexpected full-identifier matches.
- The local and unauthenticated live manifest verifiers matched all **67
  assets / 96,296,246 bytes**, manifest SHA-256
  `338af085e3113e500581a7c9c2322a351ed3dd01c9afbd97e19c08e02093f219`.
  The live verifier also checked seven core routes, all 25 Sources-register
  pages, and all ten direct Batch 584 profiles against the exact merge
  commit. Publication fidelity does not substitute for source-level
  historical review.

## Resumption and limits

The next bounded cohort starts at PDF page 118, row 11. Resume from the
existing private SQLite checkpoint using the commands in
`research/batch-584-terminal-review.md`. Boxes 186–187 remain archival
priorities. More than 18,000 person entities remain `not_started`; the
full pre-OSS research goal is ongoing. GitHub accepted this release but
warned that the repository's generated aggregate `people.json` is just
over its recommended 50 MB file size; the browser-facing data remains
partitioned, and the repository packaging should be improved separately.
