# Batch 630 release status - pages 371-380 and McCarthy-McClelian research

Date: 2026-09-22 UTC. This report records the audited and deployed release.

## Historical and extraction work

All **460** printed rows on original NARA PDF pages 371-380 were compared
against SQLite at 180 dpi. Page 372 retains its earlier authoritative review;
the other nine pages match the current extraction. This adds nine pages and
414 rows to the complete-page ledger. Visual review now covers **314/522 pages**
and **14,410/23,978 rows**. Of those rows, **14,378** match the extraction and
**32** retain reviewed corrections.

The page-304 `Joseph P. McCarthy` through `Grant S. McClelian` queue contained
23 people. Its Library of Congress pass completed 23 live exact-name searches
and returned 20 discovery candidates. Nineteen were rejected after official
item-level context review. A probable John W. McClain newspaper lead remains a
private low-confidence identity/occupation candidate: it names no employer and
lacks the second identity bridge required for publication. The public profile
does not expose the occupation, item citation, or private affiliation.

Three official Army identity candidates were accepted at high confidence on
matching full or normalized names and nonshared protected identifiers. Rex H.
McCauley's protected identifier instead conflicts with an Army record naming
Lawrence R. Chambers; that discrepancy is published as an identity conflict
without attaching an Army occupation or employer. Three probable-duplicate
clusters and the near-matching McCausland/McClausland rows remain separate for
archival review.

The final queue state is 16 `in_progress` and seven
`needs_identity_review`. This is research-attempt progress, not completion of
the minimum research protocol.

The featured oil-company category remains prominently available in the top
navigation, near the top of the home page, and above the personnel-directory
filters. It lists the current evidence-scoped set of **seven people** across
**nine historically named companies**. It includes only cited employment or
self-employment relationships; qualified findings are labeled and mere text
matches or professional representation are excluded.

## Reproducible coverage

| Measure | Count |
| --- | ---: |
| Printed index rows preserved and linked | 23,978 / 23,978 |
| Visually audited extraction | 14,410 / 23,978 rows; 314 / 522 pages |
| Active person entities | 23,939 |
| People with nonplanned research attempts | 7,607 (31.7766%) |
| People with confirmed/high employer evidence | 280 (1.1696%) |
| People with confirmed/high affiliation evidence | 628 (2.6233%) |
| Archival-review dispositions assessed | 6,300 (26.3169%) |
| Not started | 16,311 |
| Possible duplicate groups | 488 |
| Conflicts | 159 |
| Attempts or plans | 12,665 |
| Claims by confidence | confirmed 1,311; high 1,901; medium 1,374; low 187; conflicting 133 |
| Citation records / unique source documents | 5,050 / 2,377 |

Research statuses are: `blocked_by_source_access` 1; `candidate_found` 333;
`completed` 147; `conflicting_sources` 120;
`documented_prewar_employer_found` 118; `in_progress` 1,501;
`needs_identity_review` 398; `needs_temporal_review` 23;
`no_reliable_result_after_protocol` 210; `not_started` 16,311;
`occupation_only_found` 1,021; `requires_archival_review` 3,500; and
`verified_employer_found` 256.

The public projection contains 2,224 affiliations, 708 organizations, 3,843
sources, and 4,715 claims. Full-index historical research remains unfinished.

## Local verification

The clean tracked-only release candidate passed all local gates:

- Python: **132/132** tests passed.
- Playwright: **84/84** release tests passed - 15 Batch 630 identity,
  privacy-boundary, duplicate-cluster, coverage, and oil-category checks; 33
  core route/interaction tests; six analysis tests; and 30 accessibility tests
  across desktop, phone, and tablet projects.
- Astro: zero errors, warnings, or hints across **261** source files.
- Deterministic build: two successive builds each produced **24,681 HTML
  files**, **24,753 total artifacts**, and **294,389,645 bytes**, with tree
  SHA-256 `c8f97ad1daa276df103cf1cc72d88efb138a8b52be8c3df7cb2b376602b39c2b`.
- Link check: all internal links in 24,681 HTML files resolved; **50,236**
  unique external URLs were inventoried for the separate live check.
- Public-identifier audit: 12,926 normalized private identifiers, 120
  formatted variants, and 24,753 artifacts produced zero aggregate false
  positives, zero manifest-size false positives, and zero unexpected boundary
  matches.
- Public-data manifest: **67 assets**, **98,138,968 bytes**, SHA-256
  `d664836bd59004478131e195dcc06e6230b0dcc501459c97153345e347e32742`.
- Ingest validation remained complete, SQLite `quick_check` returned `ok`,
  foreign-key errors remained zero, and the 200-profile stratified structural
  audit retained all seven checks. The structural audit is not the required
  independent manual historical audit of 200 profiles.

## Deployment

Pull request [#361](https://github.com/therealjameswilson/before-oss/pull/361)
passed its required test check and was squash-merged to `main` as commit
`3bd0b70f83957bcb1dd0f1207dbb337008d8ff58`.

The post-merge [Test workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35691872742)
passed, including the research tests, checked-in manifest check, bounded site
release suite, regenerated private-identifier audit source, and public
identifier-redaction audit. The post-merge
[GitHub Pages workflow](https://github.com/therealjameswilson/before-oss/actions/runs/35691872775)
also passed and deployed the site.

Read-only verification against the immutable merge commit and the public site
confirmed all **67 manifest assets** and **98,138,968 bytes**, with manifest
SHA-256 `d664836bd59004478131e195dcc06e6230b0dcc501459c97153345e347e32742`.
It also confirmed eight core routes, all 26 paginated source-register routes,
and five direct profiles affected by the Batch 630 evidence bundle. The live
[oil-company directory](https://therealjameswilson.github.io/before-oss/oil-companies/)
and its [personnel-directory filter](https://therealjameswilson.github.io/before-oss/people/?featured=oil_companies&sort=name_asc)
both returned HTTP 200 and displayed the evidence-scoped total of seven people
across nine historically named companies.

The workflows emitted advance notices that GitHub-hosted actions currently
targeting Node.js 20 are being forced to Node.js 24, and that `ubuntu-latest`
will migrate to Ubuntu 26 in October 2026. These notices did not fail either
release workflow, but the workflow action versions should be reviewed before
those platform changes become mandatory.

## Resume

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages371-380_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch630.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch630.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page304-mccarthy-mcclelian-review_batch-630_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, raw API response, full service number, or private reviewer note is
committed or published.
