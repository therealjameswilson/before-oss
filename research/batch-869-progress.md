# Batch 869 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 869 covers the 23 printed personnel rows on NARA index PDF page 424,
rows 24-46, from John Sherry through William L Shimko. All 23 immutable source
rows remain preserved and link to 23 active person entities. The reviewed table
preserves original names, initials, printed ranks, private identifier columns,
Box 704 and archive location 230/86/40/05. Full service and officer numbers
remain private. The next unresearched boundary is page 425, row 1.

## Research outcomes

- University of California and Densho institutional sources support a
  high-confidence identification of Tamotsu Shibutani. They document his work
  as a research assistant and participant observer with the Japanese American
  Evacuation and Resettlement Study in 1942-1944. The study is modeled as his
  high-confidence, strongly date-bounded last civilian employer before Army
  service. His University of California, Berkeley student status remains a
  separate relationship and is not mislabeled as employment.
- A contemporary issue of *Broadcasting* supports a probable identification of
  Frederick N. Shilzony and documents 1942 work as an RCA Communications
  engineer and as a technical adviser to Twentieth Century-Fox. Both are
  medium-confidence documented-prewar affiliations. Neither is labeled
  immediate or last civilian because the accessible evidence does not establish
  the final sequence before OSS service.
- An official OSS Unit Certificate of Merit citation names Staff Sergeant
  Haldor G. Shields and carries the same protected identifier as the indexed
  person. This confirms his identity, but the award record does not establish a
  pre-OSS employer. His profile therefore remains in archival review rather
  than receiving an invented employment claim.
- Exact names and nonshared protected identifiers support official Army
  identity bridges for nine additional people. Army entry-grade and occupation
  codes remain private and are not converted into employers, OSS ranks or
  predecessor assignments.
- Edward A. Shils's previously reviewed, high-confidence profile and verified
  employer outcome were preserved without adding a duplicate research attempt.
- CIA-domain, NARA Catalog-domain, Library of Congress, exact-name OSS,
  employment, occupation, obituary, newspaper, institutional and archival
  searches were completed for the bounded cohort. One CIA robots failure and
  one LoC timeout were saved as source-access outcomes, not treated as negative
  historical evidence. Authenticated NARA Catalog research remains disabled
  pending safe credential rotation.

The cohort distribution is one `confirmed`, 11 `high_confidence`, one
`probable` and ten `unresolved` identities. Tamotsu Shibutani and the previously
reviewed Edward A. Shils are `verified_employer_found`; Frederick N. Shilzony
is `documented_prewar_employer_found`; the remaining 20 people are
`requires_archival_review`. Every person has at least one saved non-planned
attempt. The cohort contains 25 total attempts, including the preserved Shils
attempt and two bounded source-adapter outcomes. No Batch 869 person remains
`not_started` or `in_progress`.

The new evidence bundle contains seven sources, four organizations, four
affiliations, 16 claims, 22 person updates, 22 manual research attempts and 34
embedded claim-source links. Ten Army candidates were accepted for identity
only. Reimporting the review files is idempotent. SQLite's integrity check
returned `ok`, and its foreign-key check returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,952 people (54.1087%).
- Verified-employer coverage: 428 people (1.7880%).
- Verified-affiliation coverage: 940 people (3.9270%).
- Archival-review coverage: 11,419 people (47.7044%).
- Not started: 10,980 people.
- Possible duplicate groups: 579.
- Conflicts: 448 people.
- Claim confidence totals: 1,613 confirmed, 4,121 high, 1,721 medium,
  206 low, 374 conflicting and two unresolved.
- Citations: 6,569; unique source documents: 3,551.
- Public projection: 23,937 people, 2,882 affiliations, 1,082 organizations,
  5,334 sources and 7,825 published or qualified claims.

Relative to Batch 868, research-attempt and archival-review coverage each
increased by 22 people. Verified-employer and verified-affiliation coverage
each increased by one person. Two new organizations, four affiliations, seven
public sources and 16 published or qualified claims entered the projection.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. The stratified 200-profile audit passed every check. Astro
checked 503 files with zero errors, warnings or hints and built 25,063 static
pages. The bounded Playwright release suite passed 90/90 checks across Batch
869, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. All internal links across 25,063 HTML
files resolve; 51,445 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,135 built
artifacts.

The public manifest covers 67 assets totaling 116,942,304 bytes with SHA-256
`87e9ff47717ac829c484f81b355b7e76f067af7eaaff5bd03e996e919e4b5a62`.
Two production builds produced the identical 25,135-file static-site hash
`2ef16a14068b7183c0b12097b995a38c3a597b2396efa2e84e5ad726e73a222f`.

## Publication status

Batch 869 is published at
<https://therealjameswilson.github.io/before-oss/> from immutable content
commit `b5674bdd8a01b088d096540e09eeb2665d0f745c`. GitHub Actions test run
`39054095697` and Pages deployment run `39054095633` both completed
successfully. The post-deployment verifier checked 67 assets totaling
116,942,304 bytes against manifest SHA-256
`87e9ff47717ac829c484f81b355b7e76f067af7eaaff5bd03e996e919e4b5a62`,
eight core routes, 36 source-register pages and all 22 newly updated profiles
listed in the evidence bundle. The preserved Edward A. Shils route was checked
separately, completing live verification of all 23 Batch 869 profiles.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch869.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page424-sherry-shimko-review_batch-869_2026-10-17.json
.venv/bin/python -m oss_research --db research/research.sqlite export-adapter-checkpoints
.venv/bin/python -m oss_research --db research/research.sqlite export-derived
.venv/bin/python -m oss_research --db research/research.sqlite export-review-queue
.venv/bin/python -m oss_research --db research/research.sqlite build-public-data
.venv/bin/python -m oss_research --db research/research.sqlite coverage-report
.venv/bin/python -m oss_research --db research/research.sqlite audit-profiles --sample-size 200
.venv/bin/python -m pytest -q
npm --prefix site run build
npm --prefix site run test:release
npm --prefix site run check:links
.venv/bin/python scripts/verify_deployed_release.py --local-public-root site/public
.venv/bin/python scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
.venv/bin/python scripts/hash_tree.py site/public site/dist
```
