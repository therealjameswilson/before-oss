# Batch 881 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 881 covers NARA index PDF page 430, rows 24-46, from Anne Sirotenko
through H Skgolsvik. All 23 immutable source rows remain preserved and link to
23 active person entities. The table was checked against layout-preserving
extraction and the rendered page image. Printed names, initials, protected
identifier columns, Boxes 715-716 and archive locations 230/86/40/06-07 remain
recoverable. The rendered spelling is **Skeppstedt**, with two p characters.
Full service and officer numbers remain private.

The rendered page also establishes the next unresearched boundary: page 431,
row 1, Arthur A Skiathitis.

## Research outcomes

- An official OSS SI Branch memorandum dated 18 July 1945 identifies Youri
  Skarzynski as a stateless civilian and documents his exceptional mission
  service. Daniel Stotland's scholarly Operation Ruppert account, citing NARA
  RG 226, Entry A1-210, Box 243, WN9387-WN9400, says that Yuri Skarzynski
  escaped to join the French Army and was recruited by OSS in Paris. The
  French Army is therefore published as a high-confidence,
  `explicit_immediate` military assignment, not a civilian employer. Youri
  remains the indexed spelling and Yuri is retained as a documented variant.
- The official *Year Book of the State of Indiana, 1922* and a contemporary
  1938 Indiana National Guard roster document Hans H Skabo first as a first
  lieutenant in the 113th Engineers and later as a lieutenant colonel in the
  Corps of Engineers serving on headquarters staff. The Indiana National Guard
  is published as a high-confidence documented-prewar military affiliation.
  The sources do not prove uninterrupted service or an immediate transfer to
  OSS, and no civilian employer is inferred.
- An official Air University biography links Alfred A Skerpan's distinctive
  exact name to Harvard, Yale and OSS service from 1942 to 1945. A contemporary
  Harvard notice documents him as an upperclass scholarship recipient, and a
  Yale institutional register corroborates the full-name variant Alfred Andrew
  Skerpan. Harvard is published only as a student affiliation, not employment;
  no postwar employer is projected backward.
- Six official Army identity bridges were accepted for Anthony Sirtaut,
  Fidencio Sisneros, Paul D Sivak, Michael W Sivy, Paul E Skeen and Axel B
  Skeppstedt. Army-coded fields and protected identifiers remain private and
  were not converted into employers or OSS ranks.
- The H Skgolsvik row and the page-431 Hakon A Skjolsvik row carry the same
  protected identifier, while the official Army file associates that
  identifier with a third, unrelated name. Both index people remain separate,
  the Army candidate is rejected, and H Skgolsvik is published as a conflict
  requiring joint review of both Box 716 files. The identifier appears only as
  a masked suffix in the public projection.
- Targeted NARA index, official military, institutional, scholarly, obituary,
  directory and exact-name web searches were recorded for all 23 people. The
  CIA and Library of Congress adapters failed closed because their public
  endpoints were inaccessible during the bounded run; those transport errors
  are saved and are not treated as negative search results. No exposed NARA
  credential was used, logged or written to project data.

The cohort distribution is nine `high_confidence`, 13 `unresolved` and one
`conflicting` identity. Research status is three `occupation_only_found`, 19
`requires_archival_review` and one `conflicting_sources`; no Batch 881 person
remains `not_started` or `in_progress`. Every person has a saved non-planned
research attempt.

The evidence bundle contains nine sources, three organizations, three
affiliations, 13 claims, 23 person updates, 23 staged research attempts and 29
claim-source links. All 13 claims meet the public or conflict-publication
threshold. The Army review file contains six accepted and two conflicting
decisions. Reimporting both files is idempotent. SQLite's integrity check
returned `ok`, and its foreign-key check returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,225 people (55.2492%).
- Verified-employer coverage: 433 people (1.8089%).
- Verified-affiliation coverage: 959 people (4.0064%).
- Archival-review coverage: 11,692 people (48.8449%).
- Not started: 10,707 people; in progress: 1,893 people.
- Possible duplicate groups: 584.
- Conflicts: 459 people.
- Claim confidence totals: 1,623 confirmed, 4,242 high, 1,734 medium, 212 low,
  387 conflicting and two unresolved.
- Citations: 6,657; unique source documents: 3,619.
- Public projection: 23,937 people, 2,910 affiliations, 1,092 organizations,
  5,413 sources and 7,982 published or qualified claims.
- Private derived exports: 2,931 affiliations, 1,106 organizations, 6,657
  sources, 26,898 research attempts, 23,615 NARA pull-list rows and 22,022
  unresolved rows.

Relative to Batch 880, research-attempt and archival-review coverage each
increased by 23 people. Verified-employer coverage is unchanged because the
new accepted relationships are two military assignments and one student
affiliation. Verified-affiliation coverage increased by three. Three
affiliations, one canonical organization, nine public sources and 13 public
claims entered the public projection.

## Validation

The evidence imports, idempotency reimports, SQLite integrity check,
foreign-key check, regenerated coverage report, public-data build and
stratified 200-profile audit pass. All 145 Python tests and 81 parameterized
subtests pass. Astro reports zero errors, warnings or hints across 512 source
files and builds 25,074 pages. The bounded release suite passes 90/90 checks:
21 Batch 881 tests across desktop, phone and tablet, 33 core responsive tests,
six analysis tests and 30 axe scans with no serious or critical violations.
All 25,074 internal HTML routes resolve. The identifier audit checks 12,926
normalized private identifiers and 120 formatted variants across 25,146
artifacts, rejects 1,336 candidate substrings as non-boundary coincidences and
finds zero unexpected matches. The public manifest verifies 67 assets and
117,860,306 bytes at SHA-256
`4724d5fdb8f2a75bf23b60beccd588ac4e393106d94fbf384fd17528d6e8ccde`.
Two consecutive builds reproduce output-tree SHA-256
`c96e480bc392bdaae989c2f2ea36df2987dcffeac83ac4273ad8f66540abd401`.
The dependency audit reports zero vulnerabilities.

## Publication status

Batch 881 is published at content commit
`fcb603cd2f0db67bb869e068618a1e97728b12f9`. The clean Linux Test workflow
passed in [run 39090244921](https://github.com/therealjameswilson/before-oss/actions/runs/39090244921),
and the GitHub Pages build and deploy passed in
[run 39090244822](https://github.com/therealjameswilson/before-oss/actions/runs/39090244822).
The unauthenticated release verifier confirmed all 67 manifest assets, eight
core routes, 37 source-register pages and all 23 direct Batch 881 profiles at
`https://therealjameswilson.github.io/before-oss/`.

The tested SQLite file was promoted to the canonical research database after
a recoverable Batch 880 backup was saved at
`/private/tmp/beforeoss-pre-batch881-research.sqlite`.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite assign-page-batch --batch-name batch-881 --page 430 --first-row 24 --last-row 46
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch881.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page430-sirotenko-skgolsvik-review_batch-881_2026-10-17.json
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
