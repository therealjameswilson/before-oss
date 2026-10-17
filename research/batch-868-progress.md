# Batch 868 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 868 covers the 23 printed personnel rows on NARA index PDF page 424,
rows 1-23, from Thomas J Sheridan through Byron P Sherry. All 23 immutable
source rows remain preserved and link to 23 active person entities. The
reviewed table preserves original names, initials, printed ranks, private
identifier columns, Boxes 703-704 and archive location 230/86/40/05. Full
service and officer numbers remain private. The next unresearched boundary is
page 424, row 24.

## Research outcomes

- NARA's official Entry 210 inventory and A.G. Becker's corporate history and
  biography identify Irving H. Sherman. He joined A.G. Becker in 1926, became
  a vice president in 1935, and was recruited by William J. Donovan in 1941.
  A.G. Becker is therefore modeled as Sherman's high-confidence immediate
  pre-OSS affiliation and last civilian employer.
- A February 1944 Wesleyan College bulletin supports a probable identification
  of Florence Janson Sherriff and documents teaching at the University of
  Shanghai, St. John's University in Shanghai and the Shanghai American School.
  These are three medium-confidence, documented-prewar affiliations. None is
  labeled immediate or last civilian because the accessible source does not
  establish the final sequence before OSS service.
- The March 1934 Foreign Service Journal supports a probable identification of
  Victor F. Sheronas and places him among personnel selected for the American
  Embassy and Consulate General in Moscow. The relationship is modeled as a
  medium-confidence documented-prewar government assignment without inferring
  an unsupplied job title or immediate-predecessor status.
- Exact names and nonshared protected identifiers support official Army
  identity bridges for William T. Sheridan, Eugene Sherman, James R. Sherrill,
  Bowden Sherrod and Byron P. Sherry. Army entry-grade and occupation codes
  remain private and are not converted into employers, OSS ranks or predecessor
  assignments.
- A TIME article names an OSS veteran Eugene Sherman in China. Because the
  common name lacks a protected-identifier or Box 704 bridge to the indexed
  person, the lead remains low confidence and withheld from public factual
  claims.
- CIA-domain, NARA Catalog-domain, Library of Congress, exact-name OSS,
  employment, occupation, obituary, newspaper, institutional and archival
  searches were completed for the bounded cohort. CIA and LoC adapters stopped
  after the first source-wide service failure, and those failures were not
  treated as negative historical evidence. Authenticated NARA Catalog research
  remains disabled pending safe credential rotation.

The batch distribution is six `high_confidence`, two `probable` and 15
`unresolved` identities. Irving Sherman is `verified_employer_found`, Florence
J Sherriff and Victor F Sheronas are `documented_prewar_employer_found`, and
the remaining 20 people are `requires_archival_review`. Every person has at
least one saved non-planned attempt; the cohort contains 25 total attempts
because bounded CIA and LoC source-adapter checks supplement the 23 manual
attempts. No Batch 868 person remains `not_started` or `in_progress`.

The evidence bundle contains eight sources, five organizations, five
affiliations, 15 claims, 23 person updates, 23 manual research attempts and 27
embedded claim-source links. Five Army candidates were accepted for identity
only. Reimporting the review files is idempotent. SQLite's integrity check
returned `ok`, and its foreign-key check returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,930 people (54.0168%).
- Verified-employer coverage: 427 people (1.7838%).
- Verified-affiliation coverage: 939 people (3.9228%).
- Archival-review coverage: 11,397 people (47.6125%).
- Not started: 11,002 people.
- Possible duplicate groups: 579.
- Conflicts: 448 people.
- Claim confidence totals: 1,612 confirmed, 4,109 high, 1,718 medium,
  206 low, 374 conflicting and two unresolved.
- Citations: 6,562; unique source documents: 3,546.
- Public projection: 23,937 people, 2,878 affiliations, 1,080 organizations,
  5,327 sources and 7,809 published or qualified claims.

Relative to Batch 867, research-attempt and archival-review coverage each
increased by 23 people. Verified-employer and verified-affiliation coverage
each increased by one person. Four new organizations and seven new public
sources entered the projection; the low-confidence Eugene Sherman lead remains
outside public claims, sources and default analytics.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. The stratified 200-profile audit passed every check. Astro
checked 502 files with zero errors, warnings or hints and built 25,061 static
pages. The bounded Playwright release suite passed 90/90 checks across Batch
868, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. All internal links across 25,061 HTML
files resolve; 51,439 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,133 built
artifacts.

The public manifest covers 67 assets totaling 116,842,725 bytes with SHA-256
`841b27a5d04449170bfbcb23e45c5472fd97bf3cb61f54710e700391875ffee3`.
Two production builds produced the identical 25,133-file static-site hash
`08fc3bd1303f1558a9cd66d1b7373a25eb26fc2b94563b16baecca92bdc462b9`.

## Publication status

Batch 868 is a locally validated release candidate. Publication and immutable
live verification are still pending.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch868.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page424-sheridan-sherry-review_batch-868_2026-10-17.json
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
