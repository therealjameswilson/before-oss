# Batch 616 release status — pages 231–240 and Garson Kanin

Date: 2026-09-21 UTC. This report records the audited local release candidate
and the completed public release.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 231–240 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match; no correction was
needed. The complete-page visual-review ledger now covers **203/522** pages,
leaving **319**.

Sixteen possible-duplicate or spelling-variant groups covering 32 people were
reviewed. No source row or person entity was merged. A bounded Library of
Congress discovery pass completed 45 searches for page 231, created or
revisited 22 discovery candidates, skipped two completed fingerprints, and
encountered no error or source block. These leads are not accepted identities
or claims.

Garson Kanin now has a high-confidence identity and two separately modeled
pre-OSS affiliations. RKO Radio Pictures is his high-confidence last documented
civilian employer. The U.S. Army Signal Corps film unit is his immediate
documented pre-OSS military assignment, published at medium confidence pending
Box 389 review for the exact transfer and commissioning chronology.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Active person entities | 23,940 |
| People with nonplanned research attempts | 7,147 (29.8538%) |
| People with confirmed/high employer evidence | 278 (1.1612%) |
| People with confirmed/high affiliation evidence | 626 (2.6149%) |
| Archival-review dispositions assessed | 6,061 (25.3175%) |
| Not started | 16,793 |
| Possible duplicate groups | 411 |
| Conflicts | 131 |
| Attempts or plans | 12,202 |
| Claims by confidence | confirmed 1,311; high 1,890; medium 1,374; low 185; conflicting 132 |
| Citation records / unique source documents | 5,039 / 2,366 |

The public projection contains 2,220 affiliations, 705 organizations, 3,836
sources, and 4,703 claims. The oil-company category remains a supported,
incomplete evidence set of seven people across nine companies. Full-index
historical research remains unfinished.

## Local verification

- Python `unittest`: **126/126 passed**.
- Stratified structural profile audit: **200** profiles; all seven checks pass.
- Astro check: **0 errors, 0 warnings, 0 hints** across **247** source files.
- Isolated tracked-only build: **24,679 HTML pages / 24,751 artifacts**.
- Bounded Playwright suite: **81/81 passed**, including 30 accessibility checks
  with no serious or critical axe violations.
- Internal links: all resolved; **50,231** unique external URLs inventoried.
- Public identifier audit: 12,926 normalized identifiers and 120 variants;
  zero unexpected full-number boundary matches.
- Public manifest: **67 assets / 97,869,420 bytes**, SHA-256
  `a616541f0e3670a8076eaccb978b50d2fb859e7c508708ddeec6da1452ce449c`.
- Determinism: two clean builds reproduce the **24,751-file** tree SHA-256
  `60d4916b9aa1ac1155d5f34bf77bfc3914f51631915ac8855f2c44b03aef177f`.

## Deployment

[Pull request 333](https://github.com/therealjameswilson/before-oss/pull/333)
merged as immutable commit
`1c7d4e7e68d19ba5f0786c1d951397c6995db516`. The pull-request test job passed,
and the post-merge [Test run
35584749401](https://github.com/therealjameswilson/before-oss/actions/runs/35584749401)
and [Pages run
35584749403](https://github.com/therealjameswilson/before-oss/actions/runs/35584749403)
both completed successfully.

The unauthenticated live verifier matched all 67 manifest assets / 97,869,420
bytes, all 26 source-register pages, eight core routes, Garson Kanin's direct
profile, and all 32 direct profiles in the duplicate-review bundle to the
merged commit at manifest SHA-256
`a616541f0e3670a8076eaccb978b50d2fb859e7c508708ddeec6da1452ce449c`.
The public release is available at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages231-240_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages231-240-duplicate-review_batch-616_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-garson-kanin-rko-signal-corps_batch-616_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No authenticated NARA request was made. No API key, raw API response, full
service number, or private reviewer note is committed or published.
