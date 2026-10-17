# Batch 866 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 866 covers the 23 printed personnel rows on NARA index PDF page 423,
rows 1-23, from R B Sheeks through Hubert L Shepard. All 23 immutable source
rows remain preserved and link to 23 active person entities. The reviewed
table preserves names, initials, printed ranks, private identifier columns,
Boxes 701-703 and archive location 230/86/40/05. Full service and officer
numbers remain private. The next unresearched boundary is PDF page 423, row
24, John M Shepard.

## Research outcomes

- A nonshared protected identifier links indexed Willard D Sheeler to official
  Army source form `SHEELER WILLARD D`; the malformed Army entry-grade code
  remains private and is not normalized into a rank. A *Washington Post*
  obituary expands his name to Willard DeMont Sheeler and explicitly places
  further linguistic study at Harvard before OSS. Harvard is recorded as a
  student affiliation, not an employer.
- Harvard Law School and United Press International independently support Paul
  Cushing Sheeline's identity, Army Air Forces service and wartime sequence.
  His Army Air Forces liaison assignment with the French Air Force is modeled
  as the immediate pre-OSS military affiliation, not civilian employment by
  the French Air Force.
- American Contract Bridge League and *Los Angeles Times* sources identify
  Alfred Sheinwold and his OSS cryptographic-security work. His editorship of
  *The Bridge World* from 1934 is a named documented prewar employment
  affiliation. The more immediate New York newspaper remains unidentified and
  is retained as occupation-only evidence rather than a fabricated employer.
- Two Ramsey County Historical Society histories place Gordon Shepard at
  Oppenheimer, Woolf & Donnelly from 1939 until wartime OSS service and record
  his 1945 return. The firm is modeled both as his strongly date-bounded
  immediate pre-OSS affiliation and last civilian employer.
- Exact names and nonshared protected identifiers support official Army
  identity bridges for Henry W Sheinwold, Arnold H Sheldon, George F Sheldon
  and James G Shelley. Army entry-grade and occupation codes remain private and
  are not converted into employers, OSS ranks or predecessor assignments.
- A NARA-hosted postwar history names Colonel Henry G Sheen in an intelligence
  context. It lacks a direct personnel-file or protected-identifier bridge to
  the indexed Captain, so the candidate remains low confidence, private and
  excluded from public facts and analytics.
- A later Ventura directory entry for Hubert L Shepard lacks an OSS bridge or
  corroborating identifiers and remains a rejected namesake lead.
- CIA-domain, NARA Catalog-domain, Library of Congress, exact-name OSS,
  employment, occupation, obituary, newspaper, institutional and archival
  searches were completed for the bounded cohort. The CIA adapter respected
  robots restrictions, the LoC adapter timeout for Arnold H Sheldon was saved,
  and independent discovery checks continued without treating either access
  failure as negative evidence. Authenticated NARA Catalog research remains
  disabled pending safe credential rotation.

The batch distribution is eight `high_confidence`, four `ambiguous` and 11
`unresolved` identities. Gordon Shepard is `verified_employer_found`; Alfred
Sheinwold is `documented_prewar_employer_found`; Paul C Sheeline and Willard D
Sheeler are `completed`; the remaining 19 people are
`requires_archival_review`. Every person has a saved non-planned attempt, and
no Batch 866 person remains `not_started` or `in_progress`. The evidence bundle
contains 11 sources, four organizations, four affiliations, 15 claims, 23
person updates, 23 manual research attempts and 33 embedded claim-source links.
Five Army candidates were accepted. SQLite's foreign-key check returned no
rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,885 people (53.8288%).
- Verified-employer coverage: 425 people (1.7755%).
- Verified-affiliation coverage: 937 people (3.9144%).
- Archival-review coverage: 11,352 people (47.4245%).
- Not started: 11,047 people.
- Possible duplicate groups: 578.
- Conflicts: 447 people.
- Claim confidence totals: 1,612 confirmed, 4,087 high, 1,712 medium,
  203 low, 373 conflicting and two unresolved.
- Citations: 6,547; unique source documents: 3,534.
- Public projection: 23,937 people, 2,871 affiliations, 1,075 organizations,
  5,315 sources and 7,780 published or qualified claims.

Research-attempt and archival-review coverage each increased by 23 people.
Verified-employer coverage increased by two people and verified-affiliation
coverage increased by four people. Fourteen new public claims document
identity or pre-OSS pathways; the low-confidence Henry G Sheen candidate
remains private.

## Validation

Local release validation passed. The evidence import is idempotent, SQLite's
integrity check returned `ok`, and the foreign-key check returned zero rows.
Python reports 145 tests and 81 parameterized subtests passing. The stratified
200-profile audit passed every check. Astro checked 500 files with zero errors,
warnings or hints and built 25,056 static pages. The bounded Playwright release
suite passed 81/81 checks across Batch 866, core routes, the oil-company
category, analytics and accessibility at desktop, phone and tablet viewports.
All internal links across 25,056 HTML files resolve; 51,427 unique external
URLs were inventoried separately. The public-identifier audit found zero
unexpected boundary matches after checking 12,926 normalized identifiers and
120 formatted variants across 25,128 built artifacts.

The public manifest covers 67 assets totaling 116,667,402 bytes with SHA-256
`76c20cb1919e4393c016906395819fd248371ccce932935f990a6c2c66181953`.
Two production builds produced the identical 25,128-file static-site hash
`724f2e71b718841a4395f2a027fc18f9c3aea7446f968d7ee9914b2cd6fc83cf`.

## Publication status

Batch 866 is published at
<https://therealjameswilson.github.io/before-oss/> from immutable content
commit `ce0795827ce2b21ac0a1a1be6db8c53c42721f6f`. GitHub Actions test run
`39044008840` and Pages deployment run `39044008876` both completed
successfully. The post-deployment verifier checked 67 assets totaling
116,667,402 bytes against manifest SHA-256
`76c20cb1919e4393c016906395819fd248371ccce932935f990a6c2c66181953`,
eight core routes, 36 source-register pages and all 23 Batch 866 direct
profiles.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch866.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page423-sheeks-shepard-review_batch-866_2026-10-17.json
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
