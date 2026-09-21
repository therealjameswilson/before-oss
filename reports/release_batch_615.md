# Batch 615 release status — pages 221–230 and Alex Inkeles

Date: 2026-09-21 UTC. This report records the audited local release candidate
and the completed public release.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 221–230 were compared
against SQLite at 180 dpi. Indexed names, initials, rank, private-identifier
column occupancy, box, notes, location, and row order match; no correction was
needed. The complete-page visual-review ledger now covers **193/522** pages,
leaving **329**.

Sixteen possible-duplicate or spelling-variant groups covering 34 people were
reviewed. No source row or person entity was merged. A bounded Library of
Congress discovery pass completed 46 searches for page 221, created or revisited
64 discovery candidates, skipped one prior fingerprint, and encountered no
error or source block. These leads are not accepted identities or claims.

Alex Inkeles now has a high-confidence identity and two separately modeled
pre-OSS affiliations. Cornell University is his last documented civilian
employer; a Harvard University Press history explicitly places him in the U.S.
Army Signal Corps immediately before OSS recruitment. No military rank was
inferred, and Box 363 remains necessary for exact chronology.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Active person entities | 23,940 |
| People with nonplanned research attempts | 7,101 (29.6617%) |
| People with confirmed/high employer evidence | 277 (1.1571%) |
| People with confirmed/high affiliation evidence | 625 (2.6107%) |
| Archival-review dispositions assessed | 6,028 (25.1796%) |
| Not started | 16,839 |
| Possible duplicate groups | 395 |
| Conflicts | 131 |
| Attempts or plans | 12,156 |
| Claims by confidence | confirmed 1,311; high 1,888; medium 1,373; low 185; conflicting 132 |
| Citation records / unique source documents | 5,035 / 2,362 |

The public projection contains 2,218 affiliations, 703 organizations, 3,832
sources, and 4,700 claims. The oil-company category remains a supported,
incomplete evidence set of seven people across nine companies. Full-index
historical research remains unfinished.

## Local verification

- Python `unittest`: **126/126 passed**.
- Stratified structural profile audit: **200** profiles; all seven checks pass.
- Astro check: **0 errors, 0 warnings, 0 hints** across **246** source files.
- Isolated tracked-only build: **24,677 HTML pages / 24,749 artifacts**.
- Bounded Playwright suite: **81/81 passed**, including 30 accessibility checks
  with no serious or critical axe violations.
- Internal links: all resolved; **50,226** unique external URLs inventoried.
- Public identifier audit: 12,926 normalized identifiers and 120 variants;
  zero unexpected full-number boundary matches.
- Public manifest: **67 assets / 97,806,543 bytes**, SHA-256
  `ba1839fe7c086daa927371941ec2163ad8ec003bb11c9d720eaa82508b2c3aed`.
- Determinism: two clean builds reproduce the **24,749-file** tree SHA-256
  `4c67df1037fe1f6f5c54d7eee8831e48f76392db5d3f86464bfa3786a47a5bcf`.

## Deployment

[Pull request 331](https://github.com/therealjameswilson/before-oss/pull/331)
merged as immutable commit
`c9d4098e3ffd59db446ad9038b2cfa415c2f3c55`. The pull-request test job passed,
and the post-merge [Test run
35580202406](https://github.com/therealjameswilson/before-oss/actions/runs/35580202406)
and [Pages run
35580202400](https://github.com/therealjameswilson/before-oss/actions/runs/35580202400)
both completed successfully.

The unauthenticated live verifier matched all 67 manifest assets / 97,806,543
bytes, all 26 source-register pages, eight core routes, Alex Inkeles's direct
profile, and all 34 direct profiles in the duplicate-review bundle to the
merged commit at manifest SHA-256
`ba1839fe7c086daa927371941ec2163ad8ec003bb11c9d720eaa82508b2c3aed`.
The public release is available at
<https://therealjameswilson.github.io/before-oss/>.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages221-230_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-pages221-230-duplicate-review_batch-615_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-alex-inkeles-cornell-signal-corps_batch-615_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No authenticated NARA request was made. No API key, raw API response, full
service number, or private reviewer note is committed or published.
