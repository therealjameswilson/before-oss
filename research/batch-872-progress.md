# Batch 872 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 872 covers the first 23 printed personnel rows on NARA index PDF page
426, from Myron Shpur through Marshall J Shumate. All 23 immutable source rows
remain preserved and link to 23 active person entities. The table was checked
against both layout-preserving extraction and a rendered page image. Printed
names, initials, identifier columns, Boxes 707-708 and archive location
230/86/40/05 remain recoverable. Full service and officer numbers remain
private. The next unresearched boundary is page 426, row 24, Leon E Shurman.

## Research outcomes

- Official Army identity data and a detailed Washington Post obituary confirm
  the indexed Myron Shpur. The obituary says he was a civilian employee of the
  United States War Department before entering active Army duty. That role is
  published as his last civilian employer before service; the intervening Army
  service prevents an immediate-pre-OSS label.
- Official Army data and the Monuments Men and Women Foundation confirm
  Frederick C Shrady as the artist and Second Lieutenant who later received a
  brief OSS assignment. His full-time painting career, placed on hold at June
  1943 enlistment, is modeled as self-employment and his last civilian role,
  not as employment by an invented organization.
- An official U.S. Army history identifies Lieutenant Colonel William G.
  Suhling as Allen Dulles's assistant and chief of the German mission during
  the OSS-to-SSU transition. The index spelling `W G Shuling` remains
  recoverable, while William G Suhling Jr is retained as a documented variant.
  A transcribed 1939 VMI register supports his presidency of Suhling & Company,
  Inc.; a 1940 government catalog independently corroborates the historical
  company. The role is published at medium confidence as documented prewar
  employment, not as the immediate predecessor to OSS.
- Six exact official Army identity candidates were accepted for Myron Shpur,
  Frederick C Shrady, Robert F Shreves, Marshall E Shroyer, Harvey B Shulman
  and Marshall J Shumate. Army-coded occupation fields were not converted into
  named employers or OSS ranks.
- The page 426 Kenneth D Shuckers row and the earlier page 415 Kenneth D
  Schuckers row share a protected identifier but differ in indexed surname
  spelling and archive box. They remain two visible entities in one possible-
  duplicate group pending comparison of Boxes 708 and 688. No biography or
  employer crosses that boundary, and the protected identifier is never
  published.
- Fifteen unresolved identities remain explicit: Henry J Shrader, Ernest H
  Shrenzel, Charles E Shrewsbury, Kathleen Shrier, Glenn K Shriver, Shirley
  Shropshire, Mortimer Shuart, Elizabeth C Shub, Louise K Shuberg, Richard T
  Shubert, Marcia V Shufelt, Rachel M Shugars, Herman Shukovsky, Helen Shulman
  and Ralph C Shultz. Weak namesake, postwar, genealogy and cemetery leads were
  rejected rather than promoted to facts. CIA robots denial and a Library of
  Congress timeout for Charles Shrewsbury were recorded as access failures,
  not negative evidence.
- No exposed NARA credential was used, logged or written to project data.

The cohort distribution is two `confirmed`, five `high_confidence`, one
`ambiguous` and 15 `unresolved` identities. Two people are
`verified_employer_found`, one is `documented_prewar_employer_found`, one is
`needs_identity_review`, and 19 are `requires_archival_review`. Every person
has at least one saved non-planned research attempt. No Batch 872 person remains
`not_started` or `in_progress`.

The evidence bundle contains seven sources, three organizations, three
affiliations, 11 claims, 23 person updates, 23 research attempts and 25
claim-source links. The Army review file contains eight decisions: six accepted
exact identities, one probable identity candidate and one accepted duplicate
relation. Reimporting both review files is idempotent. SQLite's integrity check
returned `ok`, and its foreign-key check returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,021 people (54.3970%).
- Verified-employer coverage: 431 people (1.8006%).
- Verified-affiliation coverage: 948 people (3.9604%).
- Archival-review coverage: 11,488 people (47.9926%).
- Not started: 10,911 people; in progress: 1,893 people.
- Possible duplicate groups: 581.
- Conflicts: 450 people.
- Claim confidence totals: 1,619 confirmed, 4,146 high, 1,726 medium,
  206 low, 377 conflicting and two unresolved.
- Citations: 6,594; unique source documents: 3,569.
- Public projection: 23,937 people, 2,894 affiliations, 1,088 organizations,
  5,359 sources and 7,864 published or qualified claims.
- Private derived exports: 2,915 affiliations, 1,102 organizations, 6,594
  sources, 26,474 research attempts, 23,618 NARA pull-list rows and 22,032
  unresolved rows.

Relative to Batch 871, research-attempt and archival-review coverage each
increased by 23 people. Verified-affiliation coverage increased by two and
verified-employer coverage increased by one. Three affiliations, one net new
organization, seven public sources and 11 published claims entered the public
projection. The possible-duplicate-group total remains 581.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. The stratified 200-profile audit passed every check. Astro
checked 506 files with zero errors, warnings or hints and built 25,069 static
pages. The bounded Playwright release suite passed 90/90 checks across Batch
872, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. All internal links across 25,069 HTML
files resolve; 51,463 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,141 built
artifacts.

The public manifest covers 67 assets totaling 117,201,448 bytes with SHA-256
`71d95da3e8641020da9792e5fe6fe011cfc4fe18eec524e00f8b662cdcdc56e4`.
Two production builds produced the identical 25,141-file static-site hash
`a7bbd321e9e6c294b505e75b5692ecdd4efabffa17fabe2b9bb232d3030237db`.

## Publication status

Batch 872 is release-ready locally but not yet published. The current public
site remains the verified Batch 871 release until the Batch 872 content commit,
GitHub Actions test workflow, Pages deployment and immutable live verification
all succeed.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch872.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page426-shpur-shumate-review_batch-872_2026-10-17.json
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
