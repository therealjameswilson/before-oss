# Batch 660 release - Miller research

Research and release date: 2026-09-23 America/New_York.

## Historical work

The contiguous queue on PDF page 321 rows 12-33, from `Francis P. Miller`
through `John K. Miller`, contains 22 source rows and 22 cautious people. Every
person now has a saved, reviewed outcome. The cohort ends with one
`verified_employer_found`, one `conflicting_sources`, and 20
`requires_archival_review` statuses. Identity statuses are five
`high_confidence`, one `conflicting`, and 16 `unresolved`.

Francis P. Miller is a high-confidence match to Francis Pickens Miller. The
best-supported last civilian employer is the Council on Foreign Relations,
where he served as Organization Director from 1938 through 1941. The chronology
is strongly date-bounded but not called explicit recruitment. His simultaneous
Virginia House of Delegates service is modeled separately as a government
assignment. His 1934 Yale Divinity School teaching and later Foreign Policy
Association field-secretary work are qualified as documented-prewar roles,
not immediate predecessors.

Four nonshared protected Army matches establish high-confidence identities for
Fred L. Miller, Harris Miller, Hasbrouck B. Miller, and Jacob H. Miller. The
supporting Army occupation codes are identity evidence only and are not
converted into employer claims. Garth H. Miller remains conflicting because
the Army entry tied to the indexed identifier instead names Andrew J. Shima.
No occupation or identity evidence is transferred across the mismatch.

All 22 stored rows were checked against the rendered page. That check confirmed
the uncommon printed rank `Cpt` for James G. Miller. A tested normalization rule
now preserves the raw spelling while classifying it as `CAPT`, a commissioned
Army officer. The same rule corrects the only other `Cpt` row in the index.

The reviewed bundle adds ten claims: seven high, two medium, and one
conflicting. It adds four affiliations for Francis Pickens Miller. All 15
generated candidates received decisions: six accepted, one conflicting, and
eight rejected. Zero candidates remain unreviewed in the cohort, and all 22
people have terminal batch dispositions.

The top oil-company category remains evidence-scoped to **eight people across
ten historically named companies**. No identity-only record in this batch is
counted as oil-company employment.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,272 (34.5545%) |
| People with confirmed/high employer evidence | 295 (1.2323%) |
| People with confirmed/high affiliation evidence | 655 (2.7361%) |
| Archival-review dispositions assessed | 6,728 (28.1048%) |
| Not started | 15,662 |
| Possible duplicate groups | 501 |
| Conflicts | 203 |
| Attempts or plans | 14,513 |
| Claims by confidence | confirmed 1,323; high 2,147; medium 1,418; low 189; conflicting 178 |
| Citation records / unique source documents | 5,204 / 2,494 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 162;
`documented_prewar_employer_found` 129; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,662;
`occupation_only_found` 1,027; `requires_archival_review` 3,645; and
`verified_employer_found` 267.

Personnel categories now include 2,135 commissioned Army officers and 15,474
unknown or indeterminate people. The public projection contains **2,291**
published affiliations, **754** organizations, **3,994** public sources, and
**5,062** published claims. Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **136** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- Astro check with zero errors, warnings, or hints across **291** source files;
- a static build of **24,728** HTML pages;
- **87/87** bounded Playwright checks across desktop, phone, and tablet,
  including **18/18** Batch 660 checks and **30/30** accessibility checks with
  no serious or critical axe violations;
- all internal links across **24,728** HTML files, with **50,362** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,251,296** bytes verified
  at manifest SHA-256
  `9afcf8089c3af5e9283fc9e153f10ceca295a251b884f0fff33ed41febae7671`;
- zero unexpected private-identifier boundary matches across **24,800** public
  artifacts; and
- identical consecutive tree digests:
  `a634467999ce48926c36af65b1b34a2991c7e505297f80aa9010a95c2c8c2c0e`
  for `site/public` and
  `75d8b049d3a5dc5e4a2bfdb0f237a1ad976ae44f73b4be9573d1fa93f9728065`
  for `site/dist`.

External URLs were inventoried, not all requested. The CIA Reading Room check
encountered its access restriction, and one Library of Congress adapter request
failed; neither access failure was treated as a negative research result. No
authenticated NARA Catalog request was made. The previously exposed API key
must be rotated before authenticated work resumes.

## Release status

The public release, exact merged commit, CI runs, and deployed-manifest check
are recorded here after GitHub Pages deployment completes.

## Resume

```sh
python3 -m oss_research refresh-classifications
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch660.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page321-miller-review_batch-660_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
