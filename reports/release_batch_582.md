# Batch 582 release verification

Verified 2026-09-20 UTC. [PR #290](https://github.com/therealjameswilson/before-oss/pull/290)
merged as commit `3a2a9c0784016bed6f1e192eb4d6452eeabc777e`.
The [PR Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35493409395),
merged-main [Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35493594603),
and [GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/35493594717)
all passed. The public site is
[Before OSS](https://therealjameswilson.github.io/before-oss/).

## Historical scope

The cohort comprises ten distinct [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf)
rows on PDF page 117, rows 21–30, Boxes 185–186. The original page was
rendered and visually checked. [Official Army bulk data](https://catalog.archives.gov/id/1263923)
supports high-confidence wartime identity links for Roger H Dickens,
indexed Gelnn/Army Glenn O Dickerson, and Harold E Dickerson. The original
Gelnn spelling remains visible with Glenn as a documented variant. These
three claims identify people, not employers or an Army-to-OSS sequence.
Four official LoC newspaper OCR discovery hits for Ann J Dick and Harold E
Dickerson were reviewed and rejected; none establishes identity or work for
the indexed people. All ten have terminal `requires_archival_review` online
outcomes and Box 185 or 186 next actions. No physical file was inspected,
and no new reliable pre-OSS employer was identified. The NARA Catalog API
was not called for this cohort. See `research/batch-582-terminal-review.md`
and the importable evidence and decision files.

## Reproducible coverage at the released commit

| Measure | Numerator / denominator | Rate |
| --- | ---: | ---: |
| Printed index rows linked | 23,978 / 23,978 | 100% |
| Active person entities with nonplanned research attempts | 5,584 / 23,940 | 23.3250% |
| Confirmed/high published employer evidence | 262 / 23,940 | 1.0944% |
| Confirmed/high published affiliation evidence | 600 / 23,940 | 2.5063% |
| Archival-review disposition assessed | 5,539 / 23,940 | 23.1370% |

The active queue retains 18,356 `not_started`, 43 `in_progress`, and
3,345 `requires_archival_review` people; other statuses are in
`reports/research_coverage.json`. There are 258 possible-duplicate groups
and 124 people with conflicting identity or source evidence. Private SQLite
has 10,238 research attempts and 4,745 claims: 1,307 confirmed, 1,766 high,
1,359 medium, 184 low, and 129 conflicting. It has 4,892 citation records
and 2,239 unique source documents. The reviewed public projection contains
2,166 affiliations, 675 organizations, 3,700 sources, and 4,557 published
claims. These figures do not imply completion of the full index.

## QA and publication evidence

- **106/106** Python tests passed. SQLite integrity and foreign-key checks,
  522-page/23,978-row ingest validation, and the deterministic 200-profile
  structural audit passed.
- Astro checked 211 source files with no errors, warnings, or hints. The
  production build generated 24,647 direct HTML pages. The bounded browser
  release suite passed **72/72** checks across desktop, phone, and tablet,
  including 27 axe checks with no serious or critical violations.
- All internal links in 24,647 HTML pages resolved. The checker inventoried
  50,121 unique external URLs; it did not visit every external target. A
  separate redaction audit scanned 12,926 normalized private identifiers
  and 120 formatted variants across 24,719 public artifacts and found zero
  unexpected full-identifier matches.
- The local and unauthenticated live manifest verifiers matched all **67
  assets / 96,210,168 bytes**, manifest SHA-256
  `c3a4b45c6cf80f72da58ff4a9f89f6fd10c2c570455b72f38d713166edbfacea`.
  The live verifier also checked seven core routes, all 25 Sources-register
  pages, and all ten direct Batch 582 profiles against the exact merge
  commit. Publication fidelity does not substitute for source-level
  historical review.

## Resumption and limits

The next bounded cohort starts at PDF page 117, row 31. Resume from the
existing private SQLite checkpoint using the documented online protocol.
Boxes 185–186 remain archival priorities. More than 18,000 person entities
remain `not_started`; the full pre-OSS research goal is ongoing.
