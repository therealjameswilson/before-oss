# Batch 663 release - Millett-Milton research

Research and local release date: 2026-09-23 America/New_York.

## Historical work

Batch 663 resolves the next contiguous 22-person queue on PDF page 322 rows
32-46 and page 323 rows 1-7. Rendered page inspection confirmed all fields and
the page break. Anne Milliken's truncated `British ar` note remains literal.

The strongest new employment findings are Cary B. Millholland's own landscape-
architecture practice from 1937 to 1942 and John R. Milodragovich's prewar
U.S. Forest Service career. Both are explicitly modeled as last civilian work
before service rather than immediate pre-OSS affiliations. Millholland's
American Horticultural Society office and Donald D. Millikin's New York
University teaching remain professional affiliations, not silently promoted
employers. Anne Milliken and Francis B. Mills receive high-confidence identity
findings without invented employers.

Protected Army matching leaves Spiro H. Millios and Hiram J. Mills high
confidence, George T. Milstein probable, and Clayton G. Milligan conflicting
with the official Clayton G. Millikan record. Army occupation codes remain
private identity evidence. All 22 people have saved terminal outcomes, and the
review bundle adds 13 claims with 24 source links.

The top oil-company category remains evidence-scoped to **eight people across
ten historically named companies**. No identity-only person in this batch is
counted as historical oil-company employment.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,336 (34.8218%) |
| People with confirmed/high employer evidence | 296 (1.2365%) |
| People with confirmed/high affiliation evidence | 657 (2.7445%) |
| Archival-review dispositions assessed | 6,792 (28.3721%) |
| Not started | 15,598 |
| Possible duplicate groups | 506 |
| Conflicts | 210 |
| Attempts or plans | 14,728 |
| Claims by confidence | confirmed 1,323; high 2,168; medium 1,423; low 189; conflicting 185 |
| Citation records / unique source documents | 5,219 / 2,504 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 169;
`documented_prewar_employer_found` 130; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 227; `not_started` 15,598;
`occupation_only_found` 1,028; `requires_archival_review` 3,681; and
`verified_employer_found` 269.

The public projection contains **2,296** published affiliations, **755**
organizations, **4,009** public sources, and **5,095** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **136** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- Astro check with zero errors, warnings, or hints across **294** source files;
- a static build of **24,729** HTML pages;
- **93/93** bounded Playwright checks across desktop, phone, and tablet,
  including **24/24** Batch 663 checks, **33/33** core route and interaction
  checks, **6/6** analytics checks, and **30/30** accessibility checks with no
  serious or critical axe violations;
- all internal links across **24,729** HTML files, with **50,370** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,448,674** bytes verified
  at manifest SHA-256
  `f7a5fde19ca56e775b89988ccbd1029791eff5862f2c5823e17f7a11ff02d027`;
- zero unexpected private-identifier boundary matches across **24,801** built
  artifacts and all **70** tracked public assets; and
- a production dependency audit with **zero known vulnerabilities** after
  updating the transitive `devalue` package from 5.8.2 to 5.9.4; and
- identical consecutive tree digests:
  `d5d2c3ca310f1c6c9eb693647588c03703ffeeaa413799ad974a63f9765d2473`
  for `site/public` and
  `8104386f6d5a4de09d0864ef88c400282c270b917f53fb90bb201f476050cced`
  for `site/dist`.

The first Batch 663 regression pass exposed four test-only phrase mismatches;
the assertions were corrected to the rendered evidence language and all 24
batch checks passed. A later bounded-run transition briefly observed an
incomplete read of the valid analytics fixture; an immediate standalone rerun
passed all six analytics checks. A full unbounded load of 264 historical batch
specifications exceeded Node's default 4 GB heap because many older tests each
parse the complete people fixture. The bounded release suite is the maintained
CI gate and passed all 93 checks after the dependency patch. External URLs were inventoried, not all
requested. No authenticated NARA Catalog request was made. The previously
exposed API key must be rotated before authenticated work resumes.

## Release status

Batch 663 is a verified local release candidate. It has not been pushed,
merged, or deployed. The public site continues to expose the previously
deployed research state; this batch is not described as live until an immutable
pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch663.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page322-millett-page323-milton-review_batch-663_2026-09-23.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
