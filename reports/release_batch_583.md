# Batch 583 release verification

Verified 2026-09-20 UTC. [PR #292](https://github.com/therealjameswilson/before-oss/pull/292)
merged as commit `290c475de5f93e402cce9dd59c1401b38fc538b1`.
The [PR Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35495605036),
merged-main [Test run](https://github.com/therealjameswilson/before-oss/actions/runs/35495823445),
and [GitHub Pages deployment](https://github.com/therealjameswilson/before-oss/actions/runs/35495823415)
all passed. The public site is
[Before OSS](https://therealjameswilson.github.io/before-oss/).

## Historical scope

The cohort comprises sixteen distinct [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf)
rows on PDF page 117, rows 31–46, all in Box 186. Original rendered pages
117–118 were visually checked. Four accepted
[official Army bulk-file](https://catalog.archives.gov/id/1263923)
crosswalks support high-confidence wartime identities for Philip C
Dickinson, Doyle E Dickson, Martin Dickson and Angelo DiDomenico. The
index/Army spelling differences **Dickson/Diclson** and
**DiDomenico/Di Domenico** remain explicit; no Army occupation code was
turned into an employer. Eleven official LoC OCR discovery hits were
context-reviewed: ten rejected and a postwar Edward T Dickinson Jr lead
retained only as private plausible. No physical personnel file was opened.

Martin Dickson has one visibly qualified, medium-confidence U.S. Army
institutional pathway before OSS, supported by the official Army entry,
[Cornell Fleischer's memorial](https://doi.org/10.1017/S0026318400024937)
and [Encyclopaedia Iranica](https://www.iranicaonline.org/articles/dickson/).
The exact transfer date and unit remain unknown; Army service is not a
civilian employer. William J Dickman's lawyer biography and William Diebod
Jr.'s competing Diebold namesakes remain unbridged leads, not public
employer claims. All sixteen have terminal `requires_archival_review`
online outcomes and Box 186 next actions. The NARA Catalog API was not
called for this cohort. See `research/batch-583-terminal-review.md` and
the importable evidence and decision files.

## Reproducible coverage at the released commit

| Measure | Numerator / denominator | Rate |
| --- | ---: | ---: |
| Printed index rows linked | 23,978 / 23,978 | 100% |
| Active person entities with nonplanned research attempts | 5,600 / 23,940 | 23.3918% |
| Confirmed/high published employer evidence | 262 / 23,940 | 1.0944% |
| Confirmed/high published affiliation evidence | 600 / 23,940 | 2.5063% |
| Archival-review disposition assessed | 5,555 / 23,940 | 23.2038% |

The active queue retains 18,340 `not_started`, 43 `in_progress`, and
3,361 `requires_archival_review` people; other statuses are in
`reports/research_coverage.json`. There are 258 possible-duplicate groups
and 124 people with conflicting identity or source evidence. Private SQLite
has 10,286 research attempts and 4,750 claims: 1,307 confirmed, 1,770 high,
1,360 medium, 184 low, and 129 conflicting. It has 4,897 citation records
and 2,243 unique source documents. The reviewed public projection contains
2,167 affiliations, 675 organizations, 3,704 sources, and 4,562 published
claims. These figures do not imply completion of the full index.

## QA and publication evidence

- **110/110** Python tests passed. The deterministic 200-profile structural
  audit passed its available strata; a gender stratum still requires sourced
  person-level evidence because the index has no gender field.
- Astro checked 211 source files with no errors, warnings, or hints. The
  production build generated 24,647 direct HTML pages. The bounded browser
  release suite passed **72/72** checks across desktop, phone, and tablet,
  including 27 axe checks with no serious or critical violations.
- All internal links in 24,647 HTML pages resolved. The checker inventoried
  50,123 unique external URLs; it did not visit every external target. A
  separate redaction audit scanned 12,926 normalized private identifiers
  and 120 formatted variants across 24,719 public artifacts and found zero
  unexpected full-identifier matches.
- The local and unauthenticated live manifest verifiers matched all **67
  assets / 96,257,044 bytes**, manifest SHA-256
  `627cbe5739353460d5be678585e846f3def345622e52ef550a50d0e4f110770d`.
  The live verifier also checked seven core routes, all 25 Sources-register
  pages, and all sixteen direct Batch 583 profiles against the exact merge
  commit. Publication fidelity does not substitute for source-level
  historical review.

## Resumption and limits

The next bounded cohort starts at PDF page 118. Resume from the existing
private SQLite checkpoint using the documented online protocol. Box 186
remains an archival priority. More than 18,000 person entities remain
`not_started`; the full pre-OSS research goal is ongoing.
