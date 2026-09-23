# Batch 658 release - Mileff-Miller research

Research and release date: 2026-09-23 America/New_York.

## Historical work

The PDF-page 320 queue from `Christie E. Mileff` through `Alice E. Miller`
contains 22 source rows and 22 cautious people. Every person now has a saved,
reviewed outcome. The cohort ends with 17 `requires_archival_review`, three
`occupation_only_found`, one `documented_prewar_employer_found`, and one
`conflicting_sources` status. Identity statuses are two `confirmed`, eight
`high_confidence`, one `conflicting`, and eleven `unresolved`.

Newton Scott Miler is confirmed through a direct 75-page federal file. His
August 1946 forms identify him as a Dartmouth College student, unemployed while
still attending school, after Navy V-12/NROTC training ended on 1 July 1946.
The profile deliberately describes this as immediate pre-SSU status, not proof
of wartime OSS service or a civilian employer.

Milton Edward Miles is a high-confidence match to the career naval officer.
The official Navy biography places him on the Navy Department Interior Control
Board from July 1939 through March 1942, before China command beginning 4 May
1942. This is modeled as a military assignment; the biography does not state a
formal OSS transfer date. Lloyd S. Millegan's Library of Congress employment is
supported by a November 1942 scholarly byline and an independent newspaper
chronology, making it his high-confidence last civilian employer before
wartime Army service without claiming direct Library-to-OSS recruitment.

A contemporary OSS personnel report confirms George Milkovich and explicitly
dates his Army entry, commissioning, and OSS assignment on 10 August 1943. It
calls him a mechanical engineer in civilian life but names no company, so no
employer is inferred. Six nonshared protected Army matches support
high-confidence identities for Christie E. Mileff, Joseph M. Miles, Anthony J.
Milikas, Harris R. Mill, Robert R. Millar, and Aaron H. Miller without turning
Army occupation codes into employment claims.

Walter E. Millen remains separate from a later Walter Miller row in Box 526
despite a shared protected identifier. Both candidate decisions are marked
conflicting pending comparison of the two personnel files. An officer-class
booklet candidate for William H. Miley was rejected because it lacked an OSS or
identifier bridge. The remaining unresolved profiles preserve the open
question and direct researchers to the indexed file rather than implying that
no earlier employment existed.

The reviewed bundle adds 18 claims: seven confirmed, ten high, and one
conflicting. It adds five published affiliations and seven cited source
documents. All eight generated candidates received decisions: six accepted as
identity evidence and two marked conflicting. Zero remain unreviewed in the
cohort, and all 22 people have terminal batch dispositions.

The top oil-company category remains evidence-scoped to **eight people across
ten historically named companies**. No occupation-only or identity-only record
in this batch is counted as oil-company employment.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 23,978 / 23,978 rows; 522 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 8,228 (34.3707%) |
| People with confirmed/high employer evidence | 294 (1.2281%) |
| People with confirmed/high affiliation evidence | 654 (2.7319%) |
| Archival-review dispositions assessed | 6,684 (27.9210%) |
| Not started | 15,706 |
| Possible duplicate groups | 498 |
| Conflicts | 200 |
| Attempts or plans | 14,332 |
| Claims by confidence | confirmed 1,323; high 2,132; medium 1,416; low 189; conflicting 175 |
| Citation records / unique source documents | 5,195 / 2,487 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 159;
`documented_prewar_employer_found` 129; `in_progress` 1,906;
`needs_identity_review` 427; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 15,706;
`occupation_only_found` 1,027; `requires_archival_review` 3,605; and
`verified_employer_found` 266.

The public projection contains **2,287** published affiliations, **751**
organizations, **3,985** public sources, and **5,042** published claims.
Full-index historical research remains unfinished.

## Local verification

The local release gates pass:

- all **135** Python unit tests;
- extraction validation for **23,978** rows across **522** pages, including all
  warning rows and selected visual-audit pages, with clean SQLite integrity and
  foreign keys;
- Astro check with zero errors, warnings, or hints across **289** source files;
- a static build of **24,725** HTML pages;
- **90/90** bounded Playwright checks across desktop, phone, and tablet,
  including **21/21** Batch 658 checks and **30/30** accessibility checks with
  no serious or critical axe violations;
- all internal links across **24,725** HTML files, with **50,354** unique
  external URLs inventoried for the separate live check;
- the seven-check deterministic 200-profile structural audit;
- all **67** manifest-listed public assets and **100,118,070** bytes verified
  at manifest SHA-256
  `11b621dc778307ab5ab1ac61098002f6186c40f5cf6a4ae6e8654f2c75ee9513`;
- zero unexpected private-identifier boundary matches across **24,797** public
  artifacts; and
- identical consecutive tree digests:
  `25c9206a17bc7dac51bb2af3a9abad051f1be7fa9026edaa819bb270aafd9723`
  for `site/public` and
  `2a0a8dc16f2aa01676981d0c299e26526bb6125d0ec10be0a29fec7881379ce9`
  for `site/dist`.

External URLs were inventoried, not all requested. The CIA Reading Room check
was blocked by its robots restriction, and the Library of Congress adapter
stopped after a repeated transient 503; neither access failure was treated as a
negative research result. No authenticated NARA Catalog request was made. The
previously exposed API key must be rotated before authenticated work resumes.

## Released and verified live

Pull request [#417](https://github.com/therealjameswilson/before-oss/pull/417)
merged as commit
[`694e03963c31dc567de740242e95a02665fe709e`](https://github.com/therealjameswilson/before-oss/commit/694e03963c31dc567de740242e95a02665fe709e).
The pull-request test run
[`35924866236`](https://github.com/therealjameswilson/before-oss/actions/runs/35924866236),
post-merge test run
[`35925316970`](https://github.com/therealjameswilson/before-oss/actions/runs/35925316970),
and Pages deployment
[`35925316930`](https://github.com/therealjameswilson/before-oss/actions/runs/35925316930)
all passed.

The deployed-release verifier matched **67** manifest-listed assets totaling
**100,118,070** bytes to manifest SHA-256
`11b621dc778307ab5ab1ac61098002f6186c40f5cf6a4ae6e8654f2c75ee9513`.
It also verified eight core routes, 27 source-register pages, and all 22 Batch
658 direct person-profile routes against the exact merged commit. The live
[oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/)
and its placement at the top of the
[personnel directory](https://therealjameswilson.github.io/before-oss/people/)
remain in the released build.

## Resume

```sh
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch658.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page320-mileff-miller-review_batch-658_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

No API key, raw API response, full service number, copyrighted page image, or
private reviewer note is committed or published.
