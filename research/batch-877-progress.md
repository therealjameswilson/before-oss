# Batch 877 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 877 covers NARA index PDF page 428, rows 24-46, from Irimie Simion
through Frederick J Simon. All 23 immutable source rows remain preserved and
link to 23 active person entities. The table was checked against
layout-preserving extraction and the rendered page image. Printed names,
initials, ranks, protected identifier columns, Boxes 712-713 and archive
location 230/86/40/06 remain recoverable. Full service and officer numbers
remain private. The two Alfred Simon rows and two Arthur Simon rows remain four
separate people; neither a shared name nor a search result was used to merge
them. The next unresearched boundary is page 429, row 1, Harland Simon.

## Research outcomes

- An official congressional history confirms U.S. Army Private Semeon “Sam”
  Simollari and explicitly states that OSS recruited him after he enlisted in
  the Army for his Albanian language and cultural knowledge. The U.S. Army is
  therefore published as his immediate pre-OSS military assignment. His later
  radio work in the Albanian OSS unit is documented, but his postwar foreign-
  car business is not recast as pre-OSS employment. His last civilian employer
  before Army service remains unresolved.
- The 15th Infantry Regiment Association's ABMC-derived interment register
  supports a high-confidence identity for Technical Sergeant James U. Simmons
  through the exact full name and protected identifier. It documents his
  wartime rank, death and Epinal burial but does not establish whether his 15th
  Infantry service preceded or followed OSS. No immediate affiliation is
  inferred from that source.
- Exact official Army names plus nonshared protected identifiers support
  high-confidence identities for Harry C Simmons, Howard E Simmons, Clarence E
  Simms, both separately indexed Alfred Simon people and Charles E Simon. The
  same official bridge contributes to Simollari's confirmed identity. Army-
  coded entry grades and occupation codes remain private and were not
  converted into employers or unsupported OSS ranks.
- A detailed Bataan Project biography for Clarence Edward Simms carries a
  different service identifier from the indexed Clarence E Simms. That
  namesake is explicitly rejected, and his Booster Produce Company employment
  is not transferred to the OSS-index person.
- A TriCollege finding aid documents a historically relevant Bessie Simon as
  Peace Now Movement executive secretary and as formerly associated with the
  America First Committee. The indexed Bessie Simon has no middle initial,
  rank or protected identifier, however, and no source bridges the finding-aid
  subject to Box 713. The lead remains rejected rather than published as her
  affiliation.
- Fifteen identities remain unresolved. The printed spelling **Henerson B
  Simmons** is retained; `Henderson` was tested only as a search alias and not
  applied as a correction. The ranked and unranked Arthur Simon rows remain
  separate.
- Targeted official, CIA, Library of Congress, newspaper, obituary,
  institutional and archival searches were recorded for the cohort. The live
  CIA adapter failed closed because robots policy disallowed the request; the
  Library of Congress adapter timed out after bounded retries. These are
  recorded as access failures, not negative evidence. No exposed NARA
  credential was used, logged or written to project data.

The cohort distribution is one `confirmed`, seven `high_confidence` and 15
`unresolved` identities. All 23 people are `requires_archival_review`; no Batch
877 person remains `not_started` or `in_progress`. Every person has a saved
non-planned research attempt.

The evidence bundle contains six sources, one reused organization, one
affiliation, 11 claims, 23 person updates, 23 staged research attempts and 22
claim-source links. Nine evidence claims meet the publication threshold; two
namesake claims are retained as rejected review evidence and are not public
facts. The Army review file contains seven accepted identity decisions.
Reimporting both files is idempotent. SQLite's integrity check returned `ok`,
and its foreign-key check returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,134 people (54.8690%).
- Verified-employer coverage: 431 people (1.8006%).
- Verified-affiliation coverage: 951 people (3.9729%).
- Archival-review coverage: 11,601 people (48.4647%).
- Not started: 10,798 people; in progress: 1,893 people.
- Possible duplicate groups: 583.
- Conflicts: 455 people.
- Claim confidence totals: 1,623 confirmed, 4,187 high, 1,733 medium, 208 low,
  383 conflicting and two unresolved.
- Citations: 6,624; unique source documents: 3,593.
- Public projection: 23,937 people, 2,899 affiliations, 1,089 organizations,
  5,384 sources and 7,922 published or qualified claims.
- Private derived exports: 2,920 affiliations, 1,103 organizations, 6,624
  sources, 26,777 research attempts, 23,618 NARA pull-list rows and 22,030
  unresolved rows.

Relative to Batch 876, research-attempt and archival-review coverage each
increased by 23 people. Verified-affiliation coverage increased by one for
Simollari's documented Army pathway; verified-employer coverage did not change.
One affiliation, four public sources and nine published claims entered the
public projection. No new canonical organization was added because the United
States Army already existed.

## Validation

Local data and release validation passed. Python reports 145 tests and 81
parameterized subtests passing. The stratified 200-profile audit passed every
check. Astro reported zero errors, warnings or hints across 508 source files
and built 25,070 static pages. The bounded Playwright release suite passed
90/90 checks across Batch 877, core routes, the oil-company category, analytics
and accessibility at desktop, phone and tablet viewports. All internal links
across 25,070 HTML files resolve; 51,474 unique external URLs were inventoried
separately. The public-identifier audit found zero unexpected boundary matches
after checking 12,926 normalized identifiers and 120 formatted variants across
25,142 built artifacts. The production dependency audit found zero
vulnerabilities.

The public manifest covers 67 assets totaling 117,511,267 bytes with SHA-256
`0fd166bd9f2af6b3a5dfa9ed728a6f905d7872df55fac58d10687a2e06d2459f`.
Two production renders produced the identical 25,142-file static-site hash
`103707f98f9894324c56d9aa4635e37536d87e88c067b29e45a122630bc16652`.

## Publication status

Batch 877 is a locally verified release candidate. It is not recorded as
published until the immutable content commit, clean Linux workflow, Pages
deployment and unauthenticated live verifier all pass.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch877.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page428-simion-simon-review_batch-877_2026-10-17.json
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
.venv/bin/python scripts/verify_deployed_release.py --local-public-root site/dist
.venv/bin/python scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
.venv/bin/python scripts/hash_tree.py site/dist
```

## Current blocker

Authenticated NARA Catalog API research remains disabled until the API key
previously exposed in conversation is rotated and supplied through a local
environment or repository secret. That does not block publication or research
through official public sources and other configured adapters.
