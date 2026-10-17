# Batch 875 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 875 covers NARA index PDF page 427, rows 24-46, from Stanley V
Sienkiewicz through Gerard I Sillman. All 23 immutable source rows remain
preserved and link to 23 active person entities. The table was checked against
both layout-preserving extraction and a rendered page image. Printed names,
initials, ranks, identifier columns, Boxes 710-711, notes and archive locations
remain recoverable. Full service and officer numbers remain private. The next
unresearched boundary is page 428, row 1, Oliver M Silsby.

The row printed as `Signal | Section` is preserved exactly rather than silently
deleted or converted into a person. Visual inspection shows it in the surname
and given-name columns as a separate Box 710 row. Its public profile therefore
records an ambiguous, non-person-form index entry and directs researchers to
the physical material.

## Research outcomes

- Official Army data supports high-confidence identities for Mark E Sikora,
  Mike Silaghi, Raymond H Silbaugh, Jack M Silberman, Steve Silianoff and
  Gerard I Sillman. The exact names and nonshared protected identifiers agree.
  Army-coded occupation fields were not converted into named employers or OSS
  ranks.
- Joseph V Sika's protected identifier leads to an Army candidate whose name
  field reads `EPH V`, not Joseph V Sika. That substantive conflict is public,
  the identity remains unaccepted, and no employment or chronology is
  inferred pending review of Box 710.
- NARA explicitly identifies Sally Sillcocks as Sarah J. Sillcocks and places
  her in the OSS Art Looting Investigation Unit. A Princeton institutional
  profile independently corroborates the Sarah/Sally name and OSS context.
  Vassar identifies Sarah J. Sillcocks Graham as a member of the class of
  1935. The resulting Vassar affiliation is published as `student`, not as an
  employer and not as her immediate pre-OSS affiliation. Her immediate
  affiliation and last civilian employer remain unresolved.
- Two official French military-archive finding aids identify Roger Marc
  Siffredi, born 2 January 1915 in Marseille, in resistance-related file
  series. The rare name, French note and lieutenant context make the match
  probable, not confirmed. The finding aids do not supply a shared identifier,
  pre-OSS employer, military unit or sequence into OSS.
- Steve Silianoff and the earlier Steve Sidianoff index row remain separate
  entities in one possible-duplicate group. Only Silianoff has the official
  Army identity match. Their Box 711 and Box 709 jackets must be compared
  before merging them or transferring any evidence.
- Warren M Sieverin's amateur-radio listing, Jeannette K Siewers's university
  record, Choon Silasuvan's Michigan manuscript, Chetman W Sillivent's burial
  lead and Louis Sigalas's later records lack an independent bridge to the OSS
  index person. They remain private rejected or unresolved leads rather than
  published biographies.
- Thirteen identities remain unresolved: Stanley V Sienkiewicz, Warren M
  Sieverin, Jeannette K Siewers, Louis Sigalas, Morris A Sigh, Domenico G
  Signore, Robert F Sikes, Mark A Sikora, Choon Silasuvan, Anne Silbert, Earl J
  Silliman, Chetman W Sillivent and Carl Sillman. Weak namesake, later-life and
  insufficiently linked records were rejected rather than promoted to facts.
- Targeted official, CIA, Library of Congress, institutional, newspaper,
  obituary and archival checks were recorded for the cohort. Access failures
  were treated as access failures, not negative evidence. No exposed NARA
  credential was used, logged or written to project data.

The cohort distribution is six `high_confidence`, one `confirmed`, one
`probable`, one `conflicting`, one `ambiguous` and 13 `unresolved` identities.
One person is `conflicting_sources` and 22 are `requires_archival_review`.
Every person has at least one saved non-planned research attempt. No Batch 875
person remains `not_started` or `in_progress`.

The evidence bundle contains seven sources, one reused organization, one
affiliation, 11 claims, 24 person updates and 23 research attempts. The extra
person update connects the earlier Steve Sidianoff profile to the new
Silianoff possible-duplicate group without changing its terminal research
outcome. The Army review file contains seven decisions: six accepted identity
decisions and one explicit conflict. Reimporting both files is idempotent.
SQLite's integrity check returned `ok`, and its foreign-key check returned no
rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,088 people (54.6769%).
- Verified-employer coverage: 431 people (1.8006%).
- Verified-affiliation coverage: 949 people (3.9646%).
- Archival-review coverage: 11,555 people (48.2725%).
- Not started: 10,844 people; in progress: 1,893 people.
- Possible duplicate groups: 583.
- Conflicts: 454 people.
- Claim confidence totals: 1,621 confirmed, 4,167 high, 1,733 medium,
  206 low, 382 conflicting and two unresolved.
- Citations: 6,613; unique source documents: 3,584.
- Public projection: 23,937 people, 2,897 affiliations, 1,089 organizations,
  5,376 sources and 7,899 published or qualified claims.
- Private derived exports: 2,918 affiliations, 1,103 organizations, 6,613
  sources, 26,659 research attempts, 23,618 NARA pull-list rows and 22,030
  unresolved rows.

Relative to Batch 874, research-attempt and archival-review coverage each
increased by 23 people. Verified-affiliation coverage increased by one for the
high-confidence Vassar student relationship; verified-employer coverage did
not change. One affiliation, seven public sources and 11 published or
qualified claims entered the public projection. No new canonical organization
was added because Vassar College already existed.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. The stratified 200-profile audit passed every check. Astro
checked 509 files with zero errors, warnings or hints and built 25,070 static
pages. The bounded Playwright release suite passed 90/90 checks across Batch
875, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. All internal links across 25,070 HTML
files resolve; 51,471 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,142 built
artifacts.

The public manifest covers 67 assets totaling 117,391,651 bytes with SHA-256
`e37b3b8b6f9ee95382e9cabd35071a7cd8d5c9b00c6df35fb29240c8c146f39a`.
Two production builds produced the identical 25,142-file static-site hash
`23f182bcd8bec12bf8a26366df8fa54cacb00d2035b6966f08011d1a18360801`.

## Publication status

Batch 875 is published at
<https://therealjameswilson.github.io/before-oss/> from immutable content
commit `50bec0727fa49efc7822f688ee501e55c17b75ba`. GitHub Actions test run
`39066522863` completed successfully in 5 minutes 2 seconds, and Pages
deployment run `39066522962` completed successfully. The unauthenticated
immutable live verifier checked 67 assets totaling 117,391,651 bytes, manifest
SHA-256 `e37b3b8b6f9ee95382e9cabd35071a7cd8d5c9b00c6df35fb29240c8c146f39a`,
eight core routes, 36 source-register pages and 24 directly affected profiles:
the 23 Batch 875 people plus the earlier Steve Sidianoff profile linked by this
batch's duplicate review.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch875.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page427-sienkiewicz-sillman-review_batch-875_2026-10-17.json
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
