# Batch 876 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 876 covers NARA index PDF page 428, rows 1-23, from Oliver M Silsby
through Uumo A Simila. All 23 immutable source rows remain preserved and link
to 23 active person entities. The table was checked against layout-preserving
extraction and a rendered page image. Printed names, initials, ranks, protected
identifier columns, Boxes 711-712 and archive location 230/86/40/06 remain
recoverable. Full service and officer numbers remain private. The next
unresearched boundary is page 428, row 24, Irimie Simion.

## Research outcomes

- National Park Service and Washington Post evidence confirms Oliver Mowrer
  Silsby Jr. as the Detroit-born Army radio operator who volunteered for
  special duty with OSS. The U.S. Army is published as his immediate pre-OSS
  military assignment with an explicit sequence into OSS. His last civilian
  employer remains unresolved; his postwar University of Michigan attendance
  is not presented as pre-OSS evidence.
- Exact official Army names plus nonshared protected identifiers support
  high-confidence identities for Louis J Silva, Stelvio Silvani, Irwin S
  Silver, Jack M Silver, Milton Silverman, Norman Silverman, Sidney Silverman,
  Raymond J Silverstein, Rene Simard, Frank G Simeone and Dominic J Simeri.
  Army-coded fields were not converted into employers or unsupported OSS
  roles.
- Mario J Silvestri's protected identifier instead leads to an Army name field
  reading `SELLERS JIM`. That substantive conflict remains public, the identity
  is not accepted and no employment or chronology is inferred.
- A CIA-hosted document mentioning a Dr. Albert Simard in connection with
  France Forever and the Society for the Prevention of World War III lacks a
  shared identifier, OSS link or Box 712 bridge. It is retained only as a
  rejected lead, not as Albert Simard's affiliation.
- An unsourced genealogy lead for Uumo Simila lacks a middle initial, protected
  identifier, OSS connection or employer evidence. It was rejected rather than
  published.
- Ten identities remain unresolved: Fernando A Silveire, Augusta Silverman,
  Gerald S Silverman, Carl Silvestri, Agnes F Silvey, Joseph M Silvis, Irwin W
  Simans, Albert Simard, Elizabeth K Simeon and Uumo A Simila.
- Targeted official, CIA, Library of Congress, newspaper, obituary,
  institutional and archival searches were recorded for the cohort. The live
  CIA adapter failed closed because its robots policy disallowed the request;
  the Library of Congress adapter timed out after bounded retries. These are
  recorded as access failures, not as negative evidence. No exposed NARA
  credential was used, logged or written to project data.

The cohort distribution is one `confirmed`, 11 `high_confidence`, one
`conflicting` and ten `unresolved` identities. One person is
`conflicting_sources` and 22 are `requires_archival_review`. Every person has
at least one saved non-planned research attempt. No Batch 876 person remains
`not_started` or `in_progress`.

The evidence bundle contains five sources, one reused organization, one
affiliation, 14 claims, 23 person updates, 23 staged research attempts and 29
claim-source links. The Army review file contains 12 decisions: 11 accepted
identity decisions and one explicit conflict. Reimporting both files is
idempotent. SQLite's integrity check returned `ok`, and its foreign-key check
returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,111 people (54.7729%).
- Verified-employer coverage: 431 people (1.8006%).
- Verified-affiliation coverage: 950 people (3.9688%).
- Archival-review coverage: 11,578 people (48.3686%).
- Not started: 10,821 people; in progress: 1,893 people.
- Possible duplicate groups: 583.
- Conflicts: 455 people.
- Claim confidence totals: 1,622 confirmed, 4,179 high, 1,733 medium, 206 low,
  383 conflicting and two unresolved.
- Citations: 6,618; unique source documents: 3,588.
- Public projection: 23,937 people, 2,898 affiliations, 1,089 organizations,
  5,380 sources and 7,913 published or qualified claims.
- Private derived exports: 2,919 affiliations, 1,103 organizations, 6,618
  sources, 26,752 research attempts, 23,618 NARA pull-list rows and 22,030
  unresolved rows.

Relative to Batch 875, research-attempt and archival-review coverage each
increased by 23 people. Verified-affiliation coverage increased by one for
Oliver Silsby's confirmed Army pathway; verified-employer coverage did not
change. One affiliation, four public sources and 14 published or qualified
claims entered the public projection. No new canonical organization was added
because the United States Army already existed.

## Validation

Local data and release validation passed. Python reports 145 tests and 81
parameterized subtests passing. The stratified 200-profile audit passed every
check. Astro's production renderer built 25,070 static pages. The bounded
Playwright release suite passed 87/87 checks across Batch 876, core routes, the
oil-company category, analytics and accessibility at desktop, phone and tablet
viewports. All internal links across 25,070 HTML files resolve; 51,472 unique
external URLs were inventoried separately. The public-identifier audit found
zero unexpected boundary matches after checking 12,926 normalized identifiers
and 120 formatted variants across 25,142 built artifacts.

The public manifest covers 67 assets totaling 117,460,018 bytes with SHA-256
`484ef20bd60671a5209db30c75e1caf65e3cd46bd7531f13a17209cb8212c0ef`.
Two production renders produced the identical 25,142-file static-site hash
`2d1e40507debe0ee3875f8a0544f20d8ae74cacc9c2836a0c0b357baa49b14f5`.

The local Astro diagnostic pass stalled without emitting an error on the
current macOS/Node runtime and was terminated after a bounded retry. GitHub's
clean Linux test workflow independently completed the full test and release
gate successfully in 3m36s (run `39077612048`).

## Publication status

Batch 876 is published at <https://therealjameswilson.github.io/before-oss/>.
Content commit `7b1001988eb2e9751409ec53f135f2c8253b29aa` passed the GitHub
Actions test workflow (run `39077612048`) and GitHub Pages deployment (run
`39077612032`). An unauthenticated immutable verification matched all 67 assets
and 117,460,018 bytes to the committed manifest, then checked all eight core
routes, all 36 source-register pages and all 23 Batch 876 person profiles.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch876.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page428-silsby-simila-review_batch-876_2026-10-17.json
.venv/bin/python -m oss_research --db research/research.sqlite export-adapter-checkpoints
.venv/bin/python -m oss_research --db research/research.sqlite export-derived
.venv/bin/python -m oss_research --db research/research.sqlite export-review-queue
.venv/bin/python -m oss_research --db research/research.sqlite build-public-data
.venv/bin/python -m oss_research --db research/research.sqlite coverage-report
.venv/bin/python -m oss_research --db research/research.sqlite audit-profiles --sample-size 200
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 .venv/bin/python -m pytest -q
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
