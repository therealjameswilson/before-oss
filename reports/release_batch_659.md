# Batch 659 release - Miller research

Research and release date: 2026-09-23 America/New_York.

## Historical work

The contiguous queue across PDF page 320 rows 36-46 and page 321 rows 1-11,
from `Arthur R. Miller` through `Francis Miller`, contains 22 source rows and
22 cautious people. Every person now has a saved, reviewed outcome. The cohort
ends with 20 `requires_archival_review` and two `conflicting_sources` statuses.
Identity statuses are eight `high_confidence`, two `conflicting`, and twelve
`unresolved`.

Eight nonshared protected Army matches establish high-confidence identities
for Carl W. Miller, Claire D. Miller, Clarence A. Miller, David Miller, Edward
N. Miller, Edwin Miller, Ernest L. Miller, and Francis Miller. The supporting
Army occupation codes are identity evidence only and are not converted into
employer claims. Ernest L. Miller's unusual coded entry date is likewise not
used to infer chronology.

Bernard L. Miller remains conflicting because the Army entry tied to the
indexed identifier spells the given name `Benard`. Eli D. Miller remains
conflicting because the Army entry tied to the indexed identifier instead
names Charles E. Tallent. Both conflicts remain explicit pending comparison
with the Box 524 jackets; no occupation or identity evidence is transferred
across either mismatch.

The well-documented Francis Pickens Miller was rejected as the indexed
corporal because the known OSS figure was an officer and no protected
identifier bridges him to this row. Captain Edward C. Miller received enhanced
officer disambiguation, but the reviewed award lists and biographies still
lacked a branch, unit, identifier, or Box 524 bridge. Patent, city-directory,
cemetery, obituary, company, newspaper, military, and genealogy leads for the
remaining common names likewise lacked enough corroboration to publish.

The index's own `possible` note for initials-only E. W. Miller and `possibly`
note for Yeoman First Class Edwin J. Miller remain visible and unresolved.
These and the other unresolved profiles direct researchers to the indexed
personnel file instead of implying that no earlier employment existed.

The reviewed bundle adds ten identity claims: eight high and two conflicting.
It adds no employer or affiliation. All ten generated Army candidates received
decisions, zero candidates remain unreviewed in the cohort, and all 22 people
have terminal batch dispositions.

The top oil-company category remains evidence-scoped to **eight people across
ten historically named companies**. No identity-only record in this batch is
counted as oil-company employment.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,250 (34.4626%) |
| People with confirmed/high employer evidence | 294 (1.2281%) |
| People with confirmed/high affiliation evidence | 654 (2.7319%) |
| Archival-review dispositions assessed | 6,706 (28.0129%) |
| Not started | 15,684 |
| Possible duplicate groups | 500 |
| Conflicts | 202 |
| Attempts or plans | 14,380 |
| Claims by confidence | confirmed 1,323; high 2,140; medium 1,416; low 189; conflicting 177 |
| Citation records / unique source documents | 5,197 / 2,488 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 161;
`documented_prewar_employer_found` 129; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,684;
`occupation_only_found` 1,027; `requires_archival_review` 3,625; and
`verified_employer_found` 266.

The public projection contains **2,287** published affiliations, **751**
organizations, **3,987** public sources, and **5,052** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **135** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- Astro check with zero errors, warnings, or hints across **290** source files;
- a static build of **24,725** HTML pages;
- **87/87** bounded Playwright checks across desktop, phone, and tablet,
  including **18/18** Batch 659 checks and **30/30** accessibility checks with
  no serious or critical axe violations;
- all internal links across **24,725** HTML files, with **50,354** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,164,389** bytes verified
  at manifest SHA-256
  `ce81c171426041c5974a0de395ff86143afedd550cd82aa34087bc6f7a0c97fd`;
- zero unexpected private-identifier boundary matches across **24,797** public
  artifacts; and
- identical consecutive tree digests:
  `5f4ac962c4485cdb887130e23a7ec90bb55cc59bace0c6d7322ea2a484df9277`
  for `site/public` and
  `7f4f7f0ed282f606239ce005546e198c9eb152d7084593d29f6499350996fac9`
  for `site/dist`.

The optional monolithic historical Playwright command now exceeds Node's heap
while collecting all 263 accumulated specification files, even with an 8 GiB
heap. A chronological shard collected 2,178 tests and passed its first 83
assertions before the diagnostic run was intentionally stopped. No assertion
failed. The bounded release suite used by CI is unaffected and passed in full;
future harness work should make the historical archive suite sharded by
default.

External URLs were inventoried, not all requested. The CIA Reading Room check
was blocked by its robots restriction, and the Library of Congress adapter
stopped after a repeated service failure; neither access failure was treated
as a negative research result. No authenticated NARA Catalog request was made.
The previously exposed API key must be rotated before authenticated work
resumes.

## Release status

The reviewed dataset and static build are ready for the Batch 659 pull request.
Commit, workflow, deployment, and exact live-verification identifiers will be
recorded here after the release reaches GitHub Pages.

## Resume

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch659.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page320-321-miller-review_batch-659_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
