# Batch 880 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 880 covers NARA index PDF page 430, rows 1-23, from William A Sincek
through Angelo Sirico. All 23 immutable source rows remain preserved and link
to 23 active person entities. The table was checked against layout-preserving
extraction and the rendered page image. Printed names, initials, the T/5 rank,
protected identifier columns, Boxes 714-715 and archive location 230/86/40/06
remain recoverable. Full service and officer numbers remain private.

The rendered page also establishes the next unresearched boundary: page 430,
row 24, Anne Sirotenko.

## Research outcomes

- A NARA-hosted official memorandum dates Charles Siragusa's OSS assignment
  from March 1944 through December 1945 and identifies his early-1940s federal
  narcotics work. A DEA Museum oral-history transcript independently records
  that he joined the Federal Bureau of Narcotics in 1939 after four years with
  the Immigration and Naturalization Service, then entered OSS/naval
  counterintelligence. The Federal Bureau of Narcotics is therefore published
  as a high-confidence, strongly date-bounded immediate government affiliation
  and last civilian employer. The source does not explicitly say that OSS
  recruited him from the bureau, so the profile does not make that stronger
  claim. The Immigration and Naturalization Service appears separately as an
  earlier documented government assignment.
- Filmportal's authoritative biographical record documents Curt Siodmak's
  Curt/Curtis name variants, a 1942 RKO screenplay and his 1943 volunteering
  for OSS. RKO is published as a documented prewar professional affiliation,
  not silently converted into employment or an immediate predecessor to OSS.
- Ten official Army identity bridges were accepted for William Sincek, Howard
  Sinclair, Nick Sineveck, David Sing, Loren Singer, Martin Singer, Louis
  Singleton, Aristole Sioris, Sterling Sippola and Angelo Sirico. Nick
  Sineveck's suffix and the Aristotle/Aristole spelling difference remain
  visible. Army-coded fields and protected identifiers remain private and were
  not converted into employers or OSS ranks.
- John Singlaub's existing high-confidence 515th Parachute Infantry Regiment
  claim was revalidated without creating a duplicate affiliation.
- Henry E Singleton's famous Teledyne namesake and Irving Singer's philosopher
  namesake remain rejected as unbridged leads. Martin Singer and Martin R
  Singer remain separate people; neither a shared surname nor a partial-name
  search was used to merge them.
- Targeted NARA index, CIA FOIA, official military, institutional, obituary,
  directory and exact-name web searches were recorded for all 23 people. No
  exposed NARA credential was used, logged or written to project data.

The cohort distribution is 13 `high_confidence` and ten `unresolved`
identities. Research status is two `verified_employer_found`, one
`occupation_only_found` and 20 `requires_archival_review`; no Batch 880 person
remains `not_started` or `in_progress`. Every person has a saved non-planned
research attempt. John Singlaub already had a qualifying attempt and archival
disposition before this batch, so the project-wide attempt and archival
coverage measures each rise by 22 rather than 23.

The evidence bundle contains five sources, three organizations, three
affiliations, 17 claims, 23 person updates, 23 staged research attempts and 32
claim-source links. All 17 claims meet the public threshold. The Army review
file contains ten accepted identity decisions. Reimporting both files is
idempotent. SQLite's integrity check returned `ok`, and its foreign-key check
returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,202 people (55.1531%).
- Verified-employer coverage: 433 people (1.8089%).
- Verified-affiliation coverage: 956 people (3.9938%).
- Archival-review coverage: 11,669 people (48.7488%).
- Not started: 10,730 people; in progress: 1,893 people.
- Possible duplicate groups: 584.
- Conflicts: 458 people.
- Claim confidence totals: 1,623 confirmed, 4,230 high, 1,734 medium, 212 low,
  386 conflicting and two unresolved.
- Citations: 6,648; unique source documents: 3,612.
- Public projection: 23,937 people, 2,907 affiliations, 1,091 organizations,
  5,404 sources and 7,969 published or qualified claims.
- Private derived exports: 2,928 affiliations, 1,105 organizations, 6,648
  sources, 26,873 research attempts, 23,615 NARA pull-list rows and 22,025
  unresolved rows.

Relative to Batch 879, research-attempt and archival-review coverage each
increased by 22 people. Verified-employer coverage is unchanged because the
new immediate pathway is correctly modeled as a government assignment rather
than employment or self-employment. Verified-affiliation coverage increased by
two. Three affiliations, one canonical organization, five public sources and
17 public claims entered the public projection.

## Validation

The evidence imports, idempotency reimports, SQLite integrity check,
foreign-key check, regenerated coverage report, public-data build and
stratified 200-profile audit pass. All 145 Python tests and 81 parameterized
subtests pass. Astro reports zero errors, warnings or hints across 511 source
files and builds 25,073 pages. The bounded release suite passes 90/90 checks:
21 Batch 880 tests across desktop, phone and tablet, 33 core responsive tests,
six analysis tests and 30 axe scans with no serious or critical violations.
All 25,073 internal HTML routes resolve. The identifier audit checks 12,926
normalized private identifiers and 120 formatted variants across 25,145
artifacts, rejects 1,339 candidate substrings as non-boundary coincidences and
finds zero unexpected matches. The public manifest verifies 67 assets and
117,774,034 bytes at SHA-256
`ec59662b6707f2060f07351ec493affd19f5e7d6dca3c446a106abcd5d2ffa86`.
Two consecutive post-update builds reproduce output-tree SHA-256
`b6f79b32be10dce973377a4dcea892651ebb50252e9db3296613851b516201f0`.
The dependency advisory audit initially identified four build-time issues;
non-breaking lockfile updates were applied, the complete site was rebuilt and
retested, and the current audit reports zero vulnerabilities.

## Publication status

Batch 880 is locally release-ready. Publication and unauthenticated live-site
verification are the remaining release steps.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite assign-page-batch --batch-name batch-880 --page 430 --first-row 1 --last-row 23
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch880.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page430-sincek-sirico-review_batch-880_2026-10-17.json
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
