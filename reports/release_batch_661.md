# Batch 661 release - Miller research

Research and local release date: 2026-09-23 America/New_York.

## Historical work

The contiguous queue on PDF page 321 rows 34-46 and page 322 rows 1-9,
from `John B. Miller` through `Robert D. Miller`, contains 22 source rows and
22 cautious people. Every person now has a saved, reviewed outcome. The cohort
ends with one `verified_employer_found`, one `conflicting_sources`, and 20
`requires_archival_review` statuses. Identity statuses are seven
`high_confidence`, one `conflicting`, and 14 `unresolved`.

Six nonshared protected Army matches establish high-confidence identities for
Linwood R. Miller, Lou Miller, Morris I. Miller, Peter Miller, Richard G.
Miller, and Robert D. Miller. The supporting Army occupation codes remain
private identity evidence and are not converted into employer claims. Raymond
E. Miller remains conflicting because the fixed-width Army entry tied to the
indexed identifier prints `MILLER RAY OND E`; the likely-looking spacing or
transcription defect was not silently corrected, and no occupation evidence
was transferred.

Both index pages were checked visually against all 22 stored rows. The literal
`possibly` note beside Richard G. Miller remains in the public source record,
and his strong Army identity comparison does not override the index's own
uncertainty. Perry G.E. Miller's existing high-confidence identity and
reviewed Harvard University last-civilian-employer chronology remain
unchanged.

The reviewed bundle adds seven claims: six high and one conflicting. All seven
generated Army candidates received decisions: six accepted and one
conflicting. Zero candidates remain unreviewed in the cohort, and all 22
people have terminal batch dispositions. No plausible modern professional,
cemetery, obituary, or military namesake found in the staged searches was
converted into an employment claim.

The top oil-company category remains evidence-scoped to **eight people across
ten historically named companies**. No identity-only record or rejected
modern oil-company namesake in this batch is counted as historical oil-company
employment.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,293 (34.6422%) |
| People with confirmed/high employer evidence | 295 (1.2323%) |
| People with confirmed/high affiliation evidence | 655 (2.7361%) |
| Archival-review dispositions assessed | 6,749 (28.1925%) |
| Not started | 15,641 |
| Possible duplicate groups | 502 |
| Conflicts | 204 |
| Attempts or plans | 14,583 |
| Claims by confidence | confirmed 1,323; high 2,153; medium 1,418; low 189; conflicting 179 |
| Citation records / unique source documents | 5,206 / 2,495 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 163;
`documented_prewar_employer_found` 129; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,641;
`occupation_only_found` 1,027; `requires_archival_review` 3,665; and
`verified_employer_found` 267.

Personnel categories include 2,135 commissioned Army officers and 15,474
unknown or indeterminate people. The public projection contains **2,291**
published affiliations, **754** organizations, **3,996** public sources, and
**5,069** published claims. Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **136** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- Astro check with zero errors, warnings, or hints across **292** source files;
- a static build of **24,728** HTML pages;
- **90/90** bounded Playwright checks across desktop, phone, and tablet,
  including **21/21** Batch 661 checks and **30/30** accessibility checks with
  no serious or critical axe violations;
- all internal links across **24,728** HTML files, with **50,362** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,288,497** bytes verified
  at manifest SHA-256
  `bc43f4e4707ec381afab4159e3e807a77610e13c6862ed55dfb47a5406baa7bc`;
- zero unexpected private-identifier boundary matches across **24,800** public
  artifacts; and
- identical consecutive tree digests:
  `b4905625590d3c67613491728b579c06293208895d56977bb1815bb2c14e8483`
  for `site/public` and
  `ac2aa046975e70d65a24f010864acfee9e58d9cd29ad765694367c2366534325`
  for `site/dist`.

External URLs were inventoried, not all requested. The CIA Reading Room and
Library of Congress adapter checks encountered access or service errors;
neither failure was treated as a negative research result. No authenticated
NARA Catalog request was made. The previously exposed API key must be rotated
before authenticated work resumes.

The site dependency restoration used the locked dependency graph under Node
22 because this checkout's pre-existing `node_modules` placeholders were not
usable. `npm ci` reported one moderate dependency advisory; no automatic
dependency mutation was made.

## Release status

Batch 661 is verified and committed locally only. It has not been pushed,
merged, or deployed. The public site continues to expose the previously
deployed research state, including the oil-company category; this batch is not
described as live until an immutable pushed commit and deployed manifest are
verified.

## Resume

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch661.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages321-322-miller-review_batch-661_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
