# Batch 586 release verification

Verified 2026-09-20 UTC. [PR #298](https://github.com/therealjameswilson/before-oss/pull/298)
merged as commit `3565891fb4048d0de757f6f38d9cb8428e1fff63`.
The [PR Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35501690019),
merged-main [Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35501872310),
and [GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/35501872322)
all passed. The public site is
[Before OSS](https://therealjameswilson.github.io/before-oss/), with the
[featured oil-company category](https://therealjameswilson.github.io/before-oss/#oil-companies)
and its [seven-person directory filter](https://therealjameswilson.github.io/before-oss/people/?featured=oil_companies&sort=name_asc).

## Historical scope

Sixteen distinct [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf)
rows on PDF page 118, rows 31–46, were checked against a rendered page.
Rows 31–35 are in Box 187; rows 36–46 are in Box 188. Six accepted
[official Army bulk-file](https://catalog.archives.gov/id/1263923)
crosswalks support high-confidence identity only, without inferring an
employer from an Army record. The index calls Charles DiMary `Capt` but
gives no service branch; the category remains indeterminate while the
commissioned-officer flag preserves the printed rank.

A contemporaneous
[OSS Cairo field-board interview with Martin Dinga](https://digitalcollections.hoover.org/internal/media/dispatcher/331585/full),
interview LVI, printed pp. 62–63, documents that he was with the Red Cross
immediately before OSS recruitment in March 1944. The compensation exchange
supports a civilian-employment relationship. The exact job title and Red
Cross national society are not given, so the public employer is
**Red Cross (society unspecified)**. Earlier New York social work is
recorded as occupation evidence only, not assigned to an invented employer.
The Hoover media URL provides the direct source but an item-level landing
citation remains a follow-up because command-line HEAD returns 403.

A [Harvard Law Bulletin notice](https://hls.harvard.edu/wp-content/uploads/2008/09/WEB-HLB-f08-NCN.pdf)
corroborates Eugene A. Dinet Jr.'s OSS identity but documents postwar work,
not a pre-OSS employer. Five Alaska newspaper hits for `D M Dimond` were
rejected as Delegate Anthony J Dimond; a 1940 John M Dimick engineer notice
remains a private lead because it lacks an OSS or indexed-file bridge.
French military/diplomatic finding aids for Charles Dimary similarly remain
unconfirmed identity leads. Fifteen people have terminal online
`requires_archival_review` outcomes; Dinga has
`verified_employer_found`, with the physical file still useful for finer
attribution. These are bounded online outcomes, not physical-file reviews.
No NARA Catalog API calls were made, and no API key was used. See
`research/batch-586-terminal-review.md` and its importable evidence and
review-decision files.

## Reproducible coverage at the released commit

| Measure | Numerator / denominator | Rate |
| --- | ---: | ---: |
| Printed index rows linked | 23,978 / 23,978 | 100% |
| Active person entities with nonplanned research attempts | 5,646 / 23,940 | 23.5840% |
| Confirmed/high published employer evidence | 264 / 23,940 | 1.1028% |
| Confirmed/high published affiliation evidence | 603 / 23,940 | 2.5188% |
| Archival-review disposition assessed | 5,601 / 23,940 | 23.3960% |

The active queue retains 18,294 `not_started`, 43 `in_progress`, and
3,406 `requires_archival_review` people; other statuses are in
`reports/research_coverage.json`. There are 258 possible-duplicate groups
and 124 conflict cases. Private SQLite has 10,424 research attempts and
4,775 claims: 1,307 confirmed, 1,795 high, 1,360 medium, 184 low, and 129
conflicting. It has 4,912 citation records and 2,254 unique source documents.
The reviewed public projection contains 2,170 affiliations, 678
organizations, 3,718 sources, and 4,587 published claims. These figures do
not imply completion of the full index.

## QA and publication evidence

- **110/110** Python tests passed. `validate-ingest` found all 522 PDF pages
  represented, all 23,978 printed rows present, no unresolved parser-warning
  reviews, and no SQLite integrity or foreign-key errors. The existing
  200-profile structural audit passed its available strata; its gender
  stratum still requires sourced person-level evidence.
- Astro checked 215 source files with no errors, warnings, or hints. The
  production build generated **24,650** direct HTML pages. The bounded
  browser release suite passed **72/72** checks across desktop, phone, and
  tablet, including 27 axe accessibility checks with no serious or critical
  violations. The oil-company category remains in the core checks. An
  attempted all-187-spec historical Playwright run exceeded Node's default
  4 GB heap; no full-suite pass is claimed for that run.
- All internal links in 24,650 HTML pages resolved. The checker inventoried
  50,133 unique external URLs; it did not visit every target. A separate
  redaction audit scanned 12,926 normalized private identifiers and 120
  formatted variants across 24,722 public artifacts, with zero unexpected
  full-identifier matches.
- Two Pages-configured builds reproduced identical 70-file public-tree
  SHA-256 `a9745caacaa5091466f0c2bf7723ffcec1798f056a62664372d807f7457224b5`
  and 24,722-file production-tree SHA-256
  `3c151f34189acefa7daaa36125d4c6e49d44dccf9ed31ebae12d559b40bec5f0`.
- The local and unauthenticated live manifest verifiers matched all **67
  assets / 96,411,664 bytes**, manifest SHA-256
  `846455d0e1eb2869009e2df19dac3e548fb3439d359659789dc1235257ce91a0`.
  The live verifier also checked seven core routes, all 25 Sources-register
  pages, and all sixteen direct Batch 586 profiles against the exact merge
  commit. Publication fidelity does not substitute for historical review.

## Resumption and limits

The next bounded cohort begins at PDF page 119, row 1. Resume from the
existing private SQLite checkpoint using the commands in
`research/batch-586-terminal-review.md`. Boxes 187–188 remain archival
priorities. More than 18,000 people remain `not_started`; the full pre-OSS
research goal is ongoing. The generated aggregate `people.json` exceeds
GitHub's recommended 50 MB repository-file threshold; browser-facing data
is partitioned, but repository packaging warrants separate work. GitHub's
Actions runs carried a Node.js 20 deprecation advisory for action versions;
the checks passed, and the action migration remains maintenance work.
