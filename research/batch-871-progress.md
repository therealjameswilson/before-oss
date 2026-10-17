# Batch 871 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 871 covers the 23 printed personnel rows on NARA index PDF page 425,
rows 24-46, from David L Shoemaker through Evelyn N Showers. All 23 immutable
source rows remain preserved and link to 23 active person entities. The table
was checked against both layout-preserving extraction and a rendered page
image. Printed names, initials, the Lieutenant Colonel rank for Henry Shore,
identifier columns, Boxes 706-707 and archive location 230/86/40/05 remain
recoverable. Full service and officer numbers remain private. The next
unresearched boundary is page 426, row 1.

## Research outcomes

- A direct wartime OSS Personnel Board report identifies the page 425 row 27
  Herbert B Sholar by exact name and a nonshared protected identifier. It says
  he was a civilian intelligence analyst in the A-2 Section of the Air Staff,
  Air Operational Division, immediately before entering the Army on 2 July
  1943. This is published as his last civilian employer before service, not as
  an immediate civilian-to-OSS transition.
- The adjacent page 425 row 28 Herbert B Sholar has a different protected
  identifier. It remains a separate unresolved person in an explicit duplicate
  group; the Air Staff biography and employer are not transferred to it.
- The National Archives OSS glossary directly confirms Max Shoop as OSS
  reference 284. Scholarly history and contemporary Sullivan & Cromwell
  letterhead support the firm as his last documented civilian employer before
  wartime intelligence work. An intervening Red Cross cover or affiliation
  prevents an immediate-pre-OSS label.
- A CIA-released official OSS history identifies Major Henry Shore as an RCA
  radio expert involved in early portable agent-radio development. The exact
  uncommon name and compatible officer rank support a high-confidence identity.
  RCA is published as documented prewar employment, not as an explicitly
  immediate predecessor to OSS.
- A detailed Washington Post obituary supports a high-confidence identification
  of Susan K. Sholar as Susan King Sholar and documents University of South
  Carolina degree and graduate history study before wartime OSS work. The
  university is modeled as student status, not employment.
- Official and contemporary institutional rosters place Edwin L Sholine at
  Colorado A&M in 1942, while official Army data supplies the protected-
  identifier bridge. The university relationship is student and basketball-
  letterwinner status; possible overlap with Army entry keeps the exact sequence
  qualified.
- Seven official Army bulk candidates were accepted for identity only: David L
  Shoemaker, the row 27 Herbert B Sholar, Edwin L Sholine, Elsic Shoopman,
  George Shorall, Charley Short and George J Shotzbarger. Shotzbarger's `Jr`
  suffix is retained as a variant. Army-coded occupation fields are not used as
  named employers or OSS ranks.
- The page 425 Frank Shoonmaker row may be a spelling variant of the separately
  indexed and previously researched Frank Schoonmaker, but the two source rows,
  boxes and person entities remain separate. Both are placed in a possible-
  duplicate group pending comparison of Boxes 706 and 687; no biography or
  employer crosses that boundary.
- The prominent geophysicist George G Shor remains a rejected namesake lead
  because no source supplied an OSS or personnel-file bridge.
- CIA and Library of Congress adapter failures recorded for Charles W Shoenhair
  were treated as access errors, not negative historical evidence. No exposed
  NARA credential was used, logged or written to project data.

The cohort distribution is two `confirmed`, eight `high_confidence`, one
`ambiguous` and 12 `unresolved` identities. Two people are
`verified_employer_found`, one is `documented_prewar_employer_found`, one is
`occupation_only_found`, two are `needs_identity_review`, and 17 are
`requires_archival_review`. Every person has at least one saved non-planned
attempt. No Batch 871 person remains `not_started` or `in_progress`.

The evidence bundle contains ten sources, five organizations, five
affiliations, 15 claims, 24 person updates, 23 research attempts and 30
claim-source links. Seven Army candidates were accepted. Reimporting both
review files is idempotent. SQLite's integrity check returned `ok`, and its
foreign-key check returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,998 people (54.3009%).
- Verified-employer coverage: 430 people (1.7964%).
- Verified-affiliation coverage: 946 people (3.9520%).
- Archival-review coverage: 11,465 people (47.8966%).
- Not started: 10,934 people.
- Possible duplicate groups: 581.
- Conflicts: 450 people.
- Claim confidence totals: 1,617 confirmed, 4,139 high, 1,725 medium,
  206 low, 376 conflicting and two unresolved.
- Citations: 6,587; unique source documents: 3,563.
- Public projection: 23,937 people, 2,891 affiliations, 1,087 organizations,
  5,352 sources and 7,853 published or qualified claims.

Relative to Batch 870, research-attempt and archival-review coverage each
increased by 23 people. Verified-affiliation coverage increased by five and
verified-employer coverage increased by two. Five affiliations, four net new
organizations, ten public sources and 15 published claims entered the public
projection. Two additional possible-duplicate groups are now explicit.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. The stratified 200-profile audit passed every check. Astro
checked 505 files with zero errors, warnings or hints and built 25,068 static
pages. The bounded Playwright release suite passed 93/93 checks across Batch
871, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. All internal links across 25,068 HTML
files resolve; 51,458 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,140 built
artifacts.

The public manifest covers 67 assets totaling 117,120,430 bytes with SHA-256
`e99bda3c40e3519512654a3d0b3a0818e003f50b493e5a1c6df56581a8dad65a`.
Two production builds produced the identical 25,140-file static-site hash
`3a7f0440e69916ffc7c3ced4f90c643a6d6117e4dd4c909ad7f282075c9e30ff`.

## Publication status

Batch 871 has passed local release gates but is not described as published
until the immutable content commit, GitHub Actions test workflow, Pages deploy
workflow and unauthenticated live verifier all succeed.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch871.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page425-shoemaker-showers-review_batch-871_2026-10-17.json
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
