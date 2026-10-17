# Batch 874 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 874 covers NARA index PDF page 427, rows 1-23, from David K Sidbury
through Casimir A Sienkiewicz. All 23 immutable source rows remain preserved
and link to 23 active person entities. The table was checked against both
layout-preserving extraction and a rendered page image. Printed names,
initials, ranks, identifier columns, Boxes 709-710, notes and archive
locations remain recoverable. Full service and officer numbers remain private.
The next unresearched boundary is page 427, row 24, Stanley V Sienkiewicz.

The Batch 873 progress report described its next boundary as page 426, row 47,
Annie E Siebert. That was a reporting error: page 426 ends at row 46. The
authoritative continuation is page 427, row 1, David K Sidbury, which this
batch processes. Annie E Siebert belongs to an earlier section of the index and
was not silently skipped.

## Research outcomes

- Official Army data supports high-confidence identities for Gus Sideris,
  Robert K Sieben, Joseph G Siebert, Frank I Siegel, Howard F Siegle, Carol F
  Siekierski and August K Siemen. Robert Sieben's Army given-name field is
  visibly damaged, so his acceptance rests on the nonshared protected
  identifier together with the surname and middle initial, not on a guessed
  reconstruction. Army-coded occupation fields were not converted into named
  employers or OSS ranks.
- The protected identifier printed for Constant Sideropoulos leads to an Army
  candidate named Gus Sideris. Because the index also has a separate Gus
  Sideris row, the two people remain separate in a possible-duplicate group and
  the shared candidate is recorded as a conflict. No evidence or affiliation
  crosses that boundary.
- A scholarly obituary supports a probable identification of Morris Siegel and
  documents graduate study at Columbia University before his wartime work, as
  well as earlier work managing his family's restaurant and driving a taxi.
  Columbia is published as a student affiliation, not an employer. The two
  occupations remain occupation evidence only because no named employer is
  established and the chronology does not show either role as immediately
  pre-OSS.
- A CIA FOIA request-log entry and a contemporary *Daily Iowan* notice support
  a probable Rosemary Sidley lead. They do not disclose the requested file or
  establish a pre-OSS employer. Her profile therefore remains explicitly
  qualified and archival review is still required.
- A 1936 Episcopal mission publication identifies a Hall A Siddall as a
  teacher appointed to Sagada High School. A Federal Reserve oral-history
  interview documents Casimir A Sienkiewicz's long Federal Reserve career.
  Neither lead has an independent bridge to the corresponding OSS index
  person, so both remain private candidate leads and were not promoted to
  public affiliations.
- Steve Sidianoff has a possible Steve Silianoff spelling lead, but the index
  jacket and corroborating identifiers must be compared before any variant or
  merge is accepted. William J Sieben has no defensible Army match; the printed
  identifier was not altered to manufacture one. Postwar Edward Sidenius leads
  were rejected as nonresponsive to the pre-OSS question.
- Thirteen identities remain unresolved: David K Sidbury, Hall A Siddall, Paul
  Sideman, Edward F Sidenius, Steve Sidianoff, William J Sieben, Elva L Sieber,
  Jeanette I Siebert, Helen M Siegel, Helen E Siegel, Marguerite N Siegel,
  Walter Siemen and Casimir A Sienkiewicz. Weak namesake, postwar and
  insufficiently linked career leads were rejected rather than promoted to
  facts.
- Targeted official, institutional, newspaper, obituary and archival checks
  were recorded for the cohort. Access failures were treated as access
  failures, not negative evidence. No exposed NARA credential was used, logged
  or written to project data.

The cohort distribution is seven `high_confidence`, two `probable`, one
`conflicting` and 13 `unresolved` identities. Two people are
`conflicting_sources`, one is `occupation_only_found`, and 20 are
`requires_archival_review`. Every person has at least one saved non-planned
research attempt. No Batch 874 person remains `not_started` or `in_progress`.

The evidence bundle contains seven sources, one organization, one affiliation,
12 claims, 23 person updates and 23 research attempts. The Army review file
contains ten decisions: seven accepted identity decisions, one explicit
identity conflict and two accepted possible-duplicate links that preserve the
two entities separately. Reimporting both files is idempotent. SQLite's
integrity check returned `ok`, and its foreign-key check returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,065 people (54.5808%).
- Verified-employer coverage: 431 people (1.8006%).
- Verified-affiliation coverage: 948 people (3.9604%).
- Archival-review coverage: 11,532 people (48.1765%).
- Not started: 10,867 people; in progress: 1,893 people.
- Possible duplicate groups: 582.
- Conflicts: 453 people.
- Claim confidence totals: 1,620 confirmed, 4,159 high, 1,732 medium,
  206 low, 381 conflicting and two unresolved.
- Citations: 6,606; unique source documents: 3,578.
- Public projection: 23,937 people, 2,896 affiliations, 1,089 organizations,
  5,369 sources and 7,888 published or qualified claims.
- Private derived exports: 2,917 affiliations, 1,103 organizations, 6,606
  sources, 26,612 research attempts, 23,618 NARA pull-list rows and 22,030
  unresolved rows.

Relative to Batch 873, research-attempt and archival-review coverage each
increased by 23 people. Verified-affiliation and verified-employer coverage did
not change because the one new affiliation is student status attached to a
probable identity at medium confidence. One affiliation, five public sources
and 12 published or qualified claims entered the public projection. No new
canonical organization was added because Columbia University already existed.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. The stratified 200-profile audit passed every check. Astro
checked 508 files with zero errors, warnings or hints and built 25,070 static
pages. The bounded Playwright release suite passed 87/87 checks across Batch
874, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. All internal links across 25,070 HTML
files resolve; 51,468 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,142 built
artifacts.

The public manifest covers 67 assets totaling 117,323,615 bytes with SHA-256
`ccc188058d34ce536c304e13f8bec12871df78323c9ee4fe3ca3e5a19e8b32ed`.
Two production builds produced the identical 25,142-file static-site hash
`bf49eb59f5b9102247ccf3d08d7c7c13c4d9bb25d3b59fe5e2ae8829540137e1`.

## Publication status

Batch 874 is published at
<https://therealjameswilson.github.io/before-oss/> from immutable content
commit `95ece7bdd3bd8d6cbab15b19e118acf2bf7bd39f`. GitHub Actions test run
`39064601349` completed successfully in 4 minutes 20 seconds, and Pages
deployment run `39064601372` completed successfully. The unauthenticated
immutable live verifier checked 67 assets totaling 117,323,615 bytes, manifest
SHA-256 `ccc188058d34ce536c304e13f8bec12871df78323c9ee4fe3ca3e5a19e8b32ed`,
eight core routes, 36 source-register pages and all 23 direct profiles in the
new evidence bundle.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch874.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page427-sidbury-sienkiewicz-review_batch-874_2026-10-17.json
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
.venv/bin/python scripts/hash_tree.py site/dist
```

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. That does not block publication or research
through official public sources and other configured adapters.
