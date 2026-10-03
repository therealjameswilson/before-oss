# Batch 662 release - Miller-Millett research

Research and local release date: 2026-09-23 America/New_York.

## Historical work

The contiguous queue on PDF page 322 rows 10-31, from `Robert L. Miller`
through `Stephen C. Millett`, contains 22 source rows and 21 cautious people.
Every person now has a saved, reviewed outcome. William R. Miller's two printed
rows remain preserved while linking to one cautious person entity. The cohort
ends with five `conflicting_sources`, one
`documented_prewar_employer_found`, and 15 `requires_archival_review`
statuses. Identity statuses are six `high_confidence`, two `probable`, five
`conflicting`, and eight `unresolved`.

Five nonshared protected Army matches establish high-confidence identities for
Robert E. Miller, Staff Sergeant Walter Miller, Walter H. Miller, William H.
Miller, and William S. Miller. William R. Miller is also high confidence as the
person represented by two preserved index rows. Technician Fifth Grade Robert
L. Miller remains probable because the index assigns the same protected
identifier to Robert H. Miller. The supporting Army occupation codes remain
private identity evidence and are not converted into employer claims.

Robert H. Miller, Technician Sergeant Robert L. Miller, Stuart D. Miller,
Victor L. Miller, and the unranked Walter Miller remain conflicting because of
shared identifiers, mismatching official Army names, or both. Victor's exact
name and grade in the Greek Operational Group roster corroborate an OSS context
but do not cure the official Army-identifier conflict.

A directly inspected *Texas Jewish Post* obituary explicitly places Roberta
Miller's work as Edward R. Murrow's assistant at CBS before her move to
Washington and OSS work. The finding is published as a qualified
medium-confidence immediate pre-OSS and last civilian employer claim, not as a
confirmed fact. Her personnel file remains necessary for confirmation.

A CIA Reading Room search exposed a potentially relevant Stephen C. Millett
record, but the original document and PDF were not inspectable during review.
The search-result text was therefore rejected as final evidence and no law-
practice or employer claim was published.

The reviewed bundle adds 13 claims: six high, two medium, and five conflicting.
All 16 generated candidates received decisions: five accepted, one probable,
and ten conflicting. Zero candidates remain unreviewed in the cohort, and all
21 people have terminal batch dispositions.

The top oil-company category remains evidence-scoped to **eight people across
ten historically named companies**. No identity-only person in this batch is
counted as historical oil-company employment.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,314 (34.7299%) |
| People with confirmed/high employer evidence | 295 (1.2323%) |
| People with confirmed/high affiliation evidence | 655 (2.7361%) |
| Archival-review dispositions assessed | 6,770 (28.2802%) |
| Not started | 15,620 |
| Possible duplicate groups | 505 |
| Conflicts | 209 |
| Attempts or plans | 14,669 |
| Claims by confidence | confirmed 1,323; high 2,159; medium 1,420; low 189; conflicting 184 |
| Citation records / unique source documents | 5,210 / 2,497 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 168;
`documented_prewar_employer_found` 130; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,620;
`occupation_only_found` 1,027; `requires_archival_review` 3,680; and
`verified_employer_found` 267.

Personnel categories include 2,135 commissioned Army officers and 15,474
unknown or indeterminate people. The public projection contains **2,292**
published affiliations, **754** organizations, **4,000** public sources, and
**5,082** published claims. Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **136** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- Astro check with zero errors, warnings, or hints across **293** source files;
- a static build of **24,728** HTML pages;
- **93/93** bounded Playwright checks across desktop, phone, and tablet,
  including **24/24** Batch 662 checks and **30/30** accessibility checks with
  no serious or critical axe violations;
- all internal links across **24,728** HTML files, with **50,363** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,358,583** bytes verified
  at manifest SHA-256
  `9aee927589e54a9b975da6e89e358d304617b778b774bb0ecd532178e5cf8fc8`;
- zero unexpected private-identifier boundary matches across **24,800** public
  artifacts; and
- identical consecutive tree digests:
  `a143f6d7b79169d31986860ec44e9b2ccb655fe1d78eb84674230c5004021ad1`
  for `site/public` and
  `a81752accfe3c6db2447d7fc1e6787c22e9b2012359e4ccab45e950a7c94c587`
  for `site/dist`.

The first bounded Playwright pass exposed one test-only wording mismatch for
William R. Miller's boxes. The assertion was corrected to match the rendered
plural wording, and the full 93-test suite then passed. External URLs were
inventoried, not all requested. CIA Reading Room and Library of Congress
adapter requests encountered access or service errors; neither failure was
treated as a negative research result. No authenticated NARA Catalog request
was made. The previously exposed API key must be rotated before authenticated
work resumes.

## Release status

Batch 662 is verified and committed locally only. It has not been pushed, merged, or
deployed. The public site continues to expose the previously deployed research
state, including the oil-company category; this batch is not described as live
until an immutable pushed commit and deployed manifest are verified.

## Resume

```sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch662.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page322-miller-millett-review_batch-662_2026-09-23.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
