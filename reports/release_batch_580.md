# Batch 580 release verification

Verified 2026-09-20 UTC. [PR #285](https://github.com/therealjameswilson/before-oss/pull/285)
merged as commit `894fb0430500fef70d4ba5d2c861692d0d93301c`.
The PR [Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35489341159),
merged-main [Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35489530629),
and [GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/35489530624)
all completed successfully. The public site is
[Before OSS](https://therealjameswilson.github.io/before-oss/).

## Historical scope

The batch covers ten separate rows on the [NARA OSS personnel
PDF](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf),
page 117, rows 1-10, Box 185, location `230/86/30/01`. The source page was
visually checked. All ten people have terminal online
`requires_archival_review` outcomes, documented attempts, and public status
profiles. None received an unsupported pre-OSS employer.

Official Army bulk records provide three high-confidence identity-only
findings. An original [OSS Mission to France award
list](https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf)
independently corroborates Goodhue Diament's wartime identity. Paul and
Pavlos Diamantoukos remain separate despite a protected-identifier/given-name
conflict. A [Densho biography](https://encyclopedia.densho.org/John%20E.%20de%20Young)
is a qualified John E Deyoung identity lead, not a settled match; its
University of Chicago *student* chronology remains a private low-confidence
candidate, not an employer claim. See
`research/batch-580-terminal-review.md` and the importable evidence bundle.
The NARA Catalog API was not called for this batch; no key or raw API payload
was included in the release.

## Reproducible coverage at the released commit

| Measure | Numerator / denominator | Rate |
| --- | ---: | ---: |
| Printed index rows linked | 23,978 / 23,978 | 100% |
| Active person entities with nonplanned research attempts | 5,564 / 23,940 | 23.2414% |
| Confirmed/high published employer evidence | 261 / 23,940 | 1.0902% |
| Confirmed/high published affiliation evidence | 599 / 23,940 | 2.5021% |
| Archival-review disposition assessed | 5,519 / 23,940 | 23.0535% |

The active queue retains 18,376 `not_started` people, 44 `in_progress`, and
3,326 `requires_archival_review`; other statuses are in
`reports/research_coverage.json`. There are 257 possible-duplicate groups
and 124 people with conflicting identity or source evidence. Private SQLite
holds 10,156 research attempts and 4,735 claims: 1,307 confirmed, 1,756
high, 1,359 medium, 184 low, and 129 conflicting. It has 4,885 citation
records and 2,235 unique source documents. The reviewed public projection
contains 2,165 affiliations, 674 organizations, 3,694 sources and 4,547
published claims. These numbers do not imply completion of the full index.

## QA and publication evidence

- **104/104** Python tests passed. SQLite integrity and foreign-key checks,
  522-page/23,978-row ingest validation, and the deterministic 200-profile
  structural audit passed.
- Astro checked 209 source files with no errors, warnings or hints. The
  production build generated 24,646 direct HTML pages and 24,718 artifacts.
  The bounded browser suite passed **75/75** checks across desktop, phone,
  and tablet, including 27 axe checks with no serious or critical violations.
- The 3,694-source register is now 25 directly addressable static pages. The
  first Sources HTML page fell from about 1.5 MB to about 68 KB. An initial
  tablet axe run timed out on the old unpaginated page; after the change, the
  complete suite and a further three-viewport Sources check passed under the
  standard timeout.
- All internal links in 24,646 HTML pages resolved. The checker inventoried
  50,119 unique external URLs; that is not a comprehensive live link check.
  A separate redaction audit scanned 12,926 normalized private identifiers
  and 120 formatted variants across 24,718 artifacts and found zero
  unexpected full-identifier matches.
- Two local production builds reproduced the 70-file public tree digest
  `e7827ab78bcf48466ff4294b24064c37bd8247171cdd6d883081448dc91ea86e`
  and 24,718-file production tree digest
  `ee93ab4b0db1dd60f7d32c6606be8edc3651d09158fed2b9b8b0618a724a56f8`.
- The unauthenticated, read-only live verifier compared the public site with
  merge commit `894fb0430500fef70d4ba5d2c861692d0d93301c` and matched
  all **67 manifest assets / 96,140,066 bytes**, manifest SHA-256
  `57a2093ae9e4e34530c87122095c7cec51854afe08f2325ef4b4d079558b30e1`,
  seven core routes, all 25 source-register pages and all ten direct Batch 580
  profiles. This verifies publication fidelity, not the historical claims
  beyond the cited source review.

## Resumption

The next bounded online cohort begins at PDF page 117, row 11 (Ismael E Diaz)
and continues through row 20 (Louis D DiCicco). Two adjacent George C Dibert
rows need cautious duplicate assessment. Reuse the existing private SQLite
checkpoints and the documented protocol; do not infer a predecessor employer
from rank, namesake results, or Army occupation coding. Physical Box 185
files remain the principal unresolved archival source for Batch 580.
