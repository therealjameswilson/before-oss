# Batch 617 release status — pages 241–250 and Felix M. Keesing

Date: 2026-09-21 UTC. This report records the audited local release candidate
and completed public release.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 241–250 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match; no correction was
needed. The complete-page visual-review ledger now covers **212/522** pages and
**9,718/23,978** rows, leaving **310** pages.

Fourteen possible-duplicate or spelling-variant groups covering 29 people were
reviewed. No source row or person entity was merged. A bounded Library of
Congress discovery pass completed 46 searches for page 241, recorded 43
no-result and three candidate-found outcomes, and created or revisited seven
unreviewed discovery candidates. These leads are not accepted identities or
claims. One initial sandboxed run stopped on DNS before making a request; the
authorized retries completed without adapter error.

Felix M. Keesing now has a high-confidence identity and two separately modeled
pre-OSS affiliations. The University of Hawaii professorship is his
high-confidence immediate pre-OSS affiliation and last documented civilian
employer. His earlier Institute of Pacific Relations research directorship is
documented prewar employment, not an immediate predecessor claim. Stanford is
excluded from the pre-OSS chronology because the institutional archival guide
dates that professorship to 1943.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Active person entities | 23,940 |
| People with nonplanned research attempts | 7,193 (30.0459%) |
| People with confirmed/high employer evidence | 279 (1.1654%) |
| People with confirmed/high affiliation evidence | 627 (2.6190%) |
| Archival-review dispositions assessed | 6,091 (25.4428%) |
| Not started | 16,747 |
| Possible duplicate groups | 424 |
| Conflicts | 131 |
| Attempts or plans | 12,249 |
| Claims by confidence | confirmed 1,311; high 1,894; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,041 / 2,368 |

The public projection contains 2,222 affiliations, 706 organizations, 3,838
sources, and 4,707 claims. The oil-company category remains a supported,
incomplete evidence set of seven people across nine companies. Full-index
historical research remains unfinished.

## Local verification

- Python `unittest`: **126/126 passed**.
- Stratified structural profile audit: **200** profiles; all seven checks pass.
- Astro check: **0 errors, 0 warnings, 0 hints**.
- Isolated tracked-only build: **24,680 HTML pages / 24,752 artifacts**.
- Bounded Playwright suite: **81/81 passed**, including 30 accessibility checks
  with no serious or critical axe violations.
- Internal links: all resolved; **50,233** unique external URLs inventoried.
- Public identifier audit: 12,926 normalized identifiers and 120 variants;
  zero unexpected full-number boundary matches.
- Public manifest: **67 assets / 97,925,474 bytes**, SHA-256
  `2b05867e22ee4aa1a8e690829ed4a01601d11e929082fd01dcc2b91adfca461b`.
- Determinism: two clean builds reproduce the **24,752-file** tree SHA-256
  `b9ddea8ce0a0405698b365b451e9af1452ce141c6d059ce87f16f14ca8b7d4c4`.

## Deployment

[Pull request 335](https://github.com/therealjameswilson/before-oss/pull/335)
merged as immutable commit
`fff3a4f6ded3d8ee479212ef9ac3b2f69eb2d3f2`. The pull-request test job passed,
and the post-merge [Test run
35589204108](https://github.com/therealjameswilson/before-oss/actions/runs/35589204108)
and [Pages run
35589204142](https://github.com/therealjameswilson/before-oss/actions/runs/35589204142)
both completed successfully.

The unauthenticated live verifier matched all 67 manifest assets / 97,925,474
bytes, all 26 source-register pages, eight core routes,
[Felix M. Keesing's direct profile](https://therealjameswilson.github.io/before-oss/people/207b22e8-a74e-58b1-9c8e-500660f2063c/),
and all 29 direct profiles in the duplicate-review bundle to the merged commit
at manifest SHA-256
`2b05867e22ee4aa1a8e690829ed4a01601d11e929082fd01dcc2b91adfca461b`.
The public release is available at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages241-250_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages241-250-duplicate-review_batch-617_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-felix-keesing-hawaii-ipr_batch-617_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The exact page-batch assignment commands are recorded in
`research/batch-617-progress.md`. No authenticated NARA request was made. No
API key, raw API response, full service number, or private reviewer note is
committed or published.
