# Batch 879 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 879 covers NARA index PDF page 429, rows 24-46, from Rose A Simons
through Nathan Sinai. All 23 immutable source rows remain preserved and link
to 23 active person entities. The table was checked against layout-preserving
extraction and the rendered page image. Printed names, initials, the LT CMD
rank, protected identifier columns, Box 714 and archive location 230/86/40/06
remain recoverable. Full service and officer numbers remain private.

PDF page 430 was also rendered and checked to establish the next unresearched
boundary: page 430, row 1, William A Sincek.

## Research outcomes

- A scholarly history explicitly places Nathan Sinai in OSS Research and
  Analysis while documenting that his University of Michigan academic duties
  continued during his wartime work. The university's institutional history
  independently documents his professorship in hygiene and public health.
  Michigan is therefore a high-confidence, strongly date-bounded immediate
  civilian affiliation and last civilian employer. The sources do not say he
  was recruited from Michigan, so the profile does not make that stronger
  claim.
- UCLA scholarship citing an OSS internal history names theatrical designer
  Lee Simonson as a contracted consultant. The New York Public Library
  independently documents his work and founding membership in the Theatre
  Guild. The distinctive identity is accepted at high confidence. Theatre
  Guild is published as a documented prewar professional affiliation, not
  silently converted into employment or an immediate predecessor to OSS.
- An official New York State military roster documents Ronald S Simpson in
  Troop E, 101st Cavalry. Exact name plus a privately compared nonshared
  identifier support the identity at high confidence. The roster does not
  establish the transfer date or mechanism into OSS, so the military
  assignment is published with an uncertain temporal relationship and is not
  labeled immediate.
- Official Army data support high-confidence identities for Erik Simonsen,
  Collis Simpson, Deurell C Simpson, Maurice W Simpson, Ronald S Simpson,
  Wendel K. Simpson, Percy E Sims and William P Sims. Deurell's middle initial
  differs between sources, and the Army source spells Wendel as Wendell; both
  discrepancies remain visible. Army-coded entry grades and occupation codes
  remain private and were not converted into employers or OSS ranks.
- Stephen H Simpson remains unresolved as a biographical identity, while the
  printed LT CMD rank is independently retained as an indexed commissioned
  naval classification. The classification is not presented as proof of a
  matched external biography.
- A Wendell Kohl Simpson obituary and a Rochester directory entry for a Marie
  L Sinaguglia were rejected because neither was bridged to the indexed person.
  Their occupations and employers remain outside the public claims.
- Targeted NARA index, CIA FOIA, Library of Congress, newspaper, obituary,
  institutional, directory and archival searches were recorded for all 23
  people. The direct CIA adapter failed closed before searching and the
  Library of Congress adapter returned a network error on its first bounded
  request; grouped official and web-source checks were still completed. These
  access failures are not treated as negative evidence. No exposed NARA
  credential was used, logged or written to project data.

The cohort distribution is ten `high_confidence` and 13 `unresolved`
identities. Research status is one `verified_employer_found`, one
`occupation_only_found` and 21 `requires_archival_review`; no Batch 879 person
remains `not_started` or `in_progress`. Every person has a saved non-planned
research attempt.

The evidence bundle contains nine sources, three organizations, three
affiliations, 15 claims, 23 person updates, 23 staged research attempts and 31
claim-source links. Thirteen claims meet the public threshold; two unbridged
namesake claims remain rejected review evidence. The Army review file contains
eight accepted identity decisions. Reimporting both files is idempotent.
SQLite's integrity check returned `ok`, and its foreign-key check returned no
rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,180 people (55.0612%).
- Verified-employer coverage: 433 people (1.8089%).
- Verified-affiliation coverage: 954 people (3.9855%).
- Archival-review coverage: 11,647 people (48.6569%).
- Not started: 10,752 people; in progress: 1,893 people.
- Possible duplicate groups: 584.
- Conflicts: 458 people.
- Claim confidence totals: 1,623 confirmed, 4,213 high, 1,734 medium, 212 low,
  386 conflicting and two unresolved.
- Citations: 6,643; unique source documents: 3,608.
- Public projection: 23,937 people, 2,904 affiliations, 1,090 organizations,
  5,399 sources and 7,952 published or qualified claims.
- Private derived exports: 2,925 affiliations, 1,104 organizations, 6,643
  sources, 26,850 research attempts, 23,616 NARA pull-list rows and 22,027
  unresolved rows.

Relative to Batch 878, research-attempt and archival-review coverage each
increased by 23 people. Verified-employer coverage increased by one through
Nathan Sinai's University of Michigan employment, and verified-affiliation
coverage increased by two. Three affiliations, one canonical organization,
seven public sources and 13 public claims entered the public projection.

## Validation

The evidence imports, idempotency reimports, SQLite integrity check,
foreign-key check, regenerated coverage report, public-data build and
stratified 200-profile audit pass. All 145 Python tests and 81 parameterized
subtests pass. Astro reports zero errors, warnings or hints across 510 source
files and builds 25,071 pages. The bounded release suite passes 93/93 checks:
24 Batch 879 tests across desktop, phone and tablet, 33 core responsive tests,
six analysis tests and 30 axe scans with no serious or critical violations.
All 25,071 internal HTML routes resolve. The identifier audit checks 12,926
normalized private identifiers and 120 formatted variants across 25,143
artifacts, rejects 1,310 candidate substrings as non-boundary coincidences and
finds zero unexpected matches. The public manifest verifies 67 assets and
117,681,368 bytes at SHA-256
`ddbec30826f0df1830e0aa75858276abe3500e69613c191a716a832d97ea1cee`.
Two consecutive builds reproduce output-tree SHA-256
`532f708ef5388de8ff64e130465a9a4eb3aaaf92012301d0a9828ffc4c4795d3`.
The production dependency audit reports zero vulnerabilities.

## Publication status

Batch 879 is published at commit
`36386f3fa5d4b8a34cabc860060fa72339595ca8`. The clean Linux Test workflow
passed in [run 39085003393](https://github.com/therealjameswilson/before-oss/actions/runs/39085003393),
and the GitHub Pages build and deploy passed in
[run 39085003381](https://github.com/therealjameswilson/before-oss/actions/runs/39085003381).
The unauthenticated release verifier confirmed all 67 manifest assets, eight
core routes, 36 source-register pages and all 23 direct Batch 879 profiles at
`https://therealjameswilson.github.io/before-oss/`.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite assign-page-batch --batch-name batch-879 --page 429 --first-row 24 --last-row 46
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch879.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page429-simons-sinai-review_batch-879_2026-10-17.json
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
