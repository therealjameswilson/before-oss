# Batch 873 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 873 covers NARA index PDF page 426, rows 24-46, from Leon E Shurman
through James P Sicuranza. All 23 immutable source rows remain preserved and
link to 23 active person entities. The table was checked against both
layout-preserving extraction and a rendered page image. Printed names,
initials, ranks, identifier columns, Boxes 708-709, 711 and 716, notes and
archive locations remain recoverable. Full service and officer numbers remain
private. Rows 40-41, the two Peter Sichel entries, already had terminal research
outcomes; this batch completed the other 21 people. The next unresearched
boundary is page 426, row 47, Annie E Siebert.

## Research outcomes

- A scholarly Korean-history article identifies Doo Sik Shynn as editor in
  chief of *The New Korea* in 1938. The uncommon name and documented variants
  support a probable identity, but no accessible personnel-file bridge has yet
  confirmed it. The role is therefore published at medium confidence as
  documented prewar employment, not as the immediate pre-OSS affiliation or
  last civilian employer.
- A declassified official OSS Greek operational-group roster, the index and
  official Army data confirm Paul Siapicas's identity. The roster establishes
  wartime service but supplies no pre-OSS employer. His Box 709 jacket remains
  necessary for his civilian background and recruitment path.
- Official Army data supports high-confidence identities for Merle R Shuster,
  Michael Shuwarger, Bruce E Sibley, Michael J Sicilian, one of the two Richard
  C Sickler rows and James P Sicuranza. Army-coded occupation fields were not
  converted into named employers or OSS ranks.
- The protected identifier for Emily L Shwetzer agrees with an official Army
  candidate whose given name is Emil. The disagreement remains a visible
  conflict; the project does not silently correct the index or accept the
  candidate as the same person.
- A declassified NARA X-2 document names 2nd Lt. Richard C. Sickler and
  describes X-2 and SCI service. Because page 426 contains two same-name rows
  with distinct private identifiers, the document is retained as context for
  both profiles and assigned to neither as a settled identity fact. The two
  entities remain separate pending comparison of their Box 709 jackets.
- The official Army surname and middle initial support the James P Sicuranza
  row, but its protected identifier is also printed on an earlier James
  Securanza row. Both entities remain visible in a possible-duplicate group;
  no employer evidence crosses that boundary.
- Eleven identities remain unresolved: Leon E Shurman, Bertha Shurtok, Robert
  L Shutt, Helen K Shynn, Victor J Siaholm, Leona L Siberman, Mina L Sibley,
  Virginia M Sibley, Geraldine P Sica, Frank Siccone and Paul H Sickor. Weak
  namesake, postwar, genealogy and directory leads were rejected rather than
  promoted to facts.
- Targeted CIA Reading Room, Library of Congress and exact-name web searches
  were recorded for the cohort. Access failures were treated as access
  failures, not negative evidence. No exposed NARA credential was used, logged
  or written to project data.

The cohort distribution is one `confirmed`, seven `high_confidence`, one
`probable`, two `ambiguous`, one `conflicting` and 11 `unresolved` identities.
One person is `verified_employer_found`, one is
`documented_prewar_employer_found`, five are `needs_identity_review`, and 16
are `requires_archival_review`. Every person has at least one saved non-planned
research attempt. No Batch 873 person remains `not_started` or `in_progress`.

The new evidence bundle contains five sources, one organization, one
affiliation, 12 claims, 21 person updates, 21 research attempts and 24 embedded
claim-source links. The Army review file contains ten decisions: nine accepted
and one explicitly conflicting. Reimporting both review files is idempotent.
SQLite's integrity check returned `ok`, and its foreign-key check returned no
rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,042 people (54.4847%).
- Verified-employer coverage: 431 people (1.8006%).
- Verified-affiliation coverage: 948 people (3.9604%).
- Archival-review coverage: 11,509 people (48.0804%).
- Not started: 10,890 people; in progress: 1,893 people.
- Possible duplicate groups: 582.
- Conflicts: 451 people.
- Claim confidence totals: 1,620 confirmed, 4,152 high, 1,728 medium,
  206 low, 380 conflicting and two unresolved.
- Citations: 6,599; unique source documents: 3,572.
- Public projection: 23,937 people, 2,895 affiliations, 1,089 organizations,
  5,364 sources and 7,876 published or qualified claims.
- Private derived exports: 2,916 affiliations, 1,103 organizations, 6,599
  sources, 26,564 research attempts, 23,618 NARA pull-list rows and 22,031
  unresolved rows.

Relative to Batch 872, research-attempt and archival-review coverage each
increased by 21 people. Verified-affiliation and verified-employer coverage did
not change because the new employment claim remains medium-confidence and the
person identity remains probable. One affiliation, one organization, five
public sources and 12 published or qualified claims entered the public
projection. The possible-duplicate-group total increased by one.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. The stratified 200-profile audit passed every check. Astro
checked 507 files with zero errors, warnings or hints and built 25,070 static
pages. The bounded Playwright release suite passed 90/90 checks across Batch
873, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. All internal links across 25,070 HTML
files resolve; 51,465 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,142 built
artifacts.

The public manifest covers 67 assets totaling 117,264,357 bytes with SHA-256
`bf9dbf0228a62ce4c514d47d7d26c391566dacdcad70c1c663d1da988997accd`.
Two production builds produced the identical 25,142-file static-site hash
`af868a3ac4bd5853fa5ec36411b168d344495dbc34ce884ae1cf38a7b5687d46`.

## Publication status

Batch 873 has passed every local release gate and is ready to publish to the
existing site at <https://therealjameswilson.github.io/before-oss/>. The
immutable content commit, GitHub Actions results and unauthenticated live
verification will be recorded here after deployment.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch873.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page426-shurman-sicuranza-review_batch-873_2026-10-17.json
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
