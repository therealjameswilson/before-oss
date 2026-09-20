# Batch 581 release verification

Verified 2026-09-20 UTC. [PR #287](https://github.com/therealjameswilson/before-oss/pull/287)
merged as commit `cbec90e90debbc4107b9a9b28485135feaa73b3d`.
The [PR Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35490979806),
merged-main [Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35491167699),
and [GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/35491167728)
all passed. The public site is
[Before OSS](https://therealjameswilson.github.io/before-oss/).

## Historical scope

The cohort comprises ten separate [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf)
rows on PDF page 117, rows 11–20, Box 185, location `230/86/30/01`.
The original page was rendered and visually checked. Five official Army
bulk-file crosswalks support identity only. The two adjacent George C Dibert
rows remain separate and flagged as possible duplicates. Nine people have
terminal `requires_archival_review` outcomes, and the numbered Major Dibert
has `verified_employer_found`; all ten retain appropriate archival next
actions. No physical Box 185 file was inspected.

A contemporary [*Broadcasting* item](https://www.worldradiohistory.com/Archive-BC/BC-1942/1942-10-19-BC.pdf)
and Lawrence C. Soley's [*Radio Warfare*](https://device.report/m/e9158badfd31ef45c1f1ef2e1c1562f9d4b35b7710bdd77b93b5c3583dccb029)
support J. Walter Thompson Co. as the numbered major's **last civilian
employer before Army service**. They do not establish his immediate pre-OSS
affiliation. The adjacent unnumbered row receives no inherited employer.
See `research/batch-581-terminal-review.md` for source-level reasoning and
the importable evidence bundle. The NARA Catalog API was not called for this
cohort, and no full protected identifiers are public.

## Reproducible coverage at the released commit

| Measure | Numerator / denominator | Rate |
| --- | ---: | ---: |
| Printed index rows linked | 23,978 / 23,978 | 100% |
| Active person entities with nonplanned research attempts | 5,574 / 23,940 | 23.2832% |
| Confirmed/high published employer evidence | 262 / 23,940 | 1.0944% |
| Confirmed/high published affiliation evidence | 600 / 23,940 | 2.5063% |
| Archival-review disposition assessed | 5,529 / 23,940 | 23.0952% |

The active queue retains 18,366 `not_started` people, 44 `in_progress`,
and 3,335 `requires_archival_review`; the other statuses are in
`reports/research_coverage.json`. There are 258 possible-duplicate groups
and 124 people with conflicting identity or source evidence. Private SQLite
has 10,198 research attempts and 4,742 claims: 1,307 confirmed, 1,763
high, 1,359 medium, 184 low, and 129 conflicting. It has 4,890 citation
records and 2,238 unique source documents. The reviewed public projection
contains 2,166 affiliations, 675 organizations, 3,698 sources, and 4,554
published claims. These figures do not imply completion of the full index.

## QA and publication evidence

- **104/104** Python tests passed. SQLite integrity and foreign-key checks,
  522-page/23,978-row ingest validation, and the deterministic 200-profile
  structural audit passed.
- Astro checked 210 source files with no errors, warnings or hints. The
  production build generated 24,647 direct HTML pages. The bounded browser
  release suite passed **75/75** checks across desktop, phone, and tablet,
  including 27 axe checks with no serious or critical violations. The final
  wording adjustment was followed by a fresh build and **12/12** focused
  Batch 581 browser checks.
- All internal links in 24,647 HTML pages resolved. The checker inventoried
  50,121 unique external URLs; that is not a comprehensive live link check.
  A separate redaction audit scanned 12,926 normalized private identifiers
  and 120 formatted variants across 24,719 public artifacts and found zero
  unexpected full-identifier matches.
- The local and unauthenticated live manifest verifiers matched all **67
  assets / 96,190,102 bytes**, manifest SHA-256
  `91c10b8a42f5fd0f6583b419afe9862780176af5ed954043dcf03c28b7f62c93`.
  The live verifier also checked seven core routes, all 25 Sources-register
  pages, and all ten direct Batch 581 profiles against merge commit
  `cbec90e90debbc4107b9a9b28485135feaa73b3d`. This verifies
  publication fidelity, not historical claims beyond the cited source review.

## Resumption

The next bounded cohort starts at PDF page 117, row 21 (Ann J Dick).
Continue from the existing private SQLite checkpoint using the documented
online protocol. Box 185 files remain an archival priority for unresolved
identity, duplication, and predecessor-affiliation questions.
