# Batch 878 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 878 covers NARA index PDF page 429, rows 1-23, from Harland Simon
through Hans Simons. All 23 immutable source rows remain preserved and link to
23 active person entities. The table was checked against layout-preserving
extraction and the rendered page image. Printed names, initials, ranks,
protected identifier columns, Box 713 and archive location 230/86/40/06 remain
recoverable. Full service and officer numbers remain private.

The five adjacent Joseph Simon rows remain five separate person entities. One
has an accepted official Army identity bridge, one carries a distinct officer
identifier, two are identical unnumbered M/SGT entries, and one numbered row
has a one-digit conflict with a separate official OSS commendation. They share
a possible-duplicate review group but are not merged. The next unresearched
boundary is page 429, row 24, Rose A Simons.

## Research outcomes

- The New School's institutional history documents Hans Simons joining its
  Graduate Faculty in 1935, teaching political science and international
  relations, and becoming dean in 1943. A scholarly review independently says
  he briefly worked for OSS as a Germany expert. The New School is therefore a
  high-confidence, strongly date-bounded immediate civilian affiliation and
  his last documented civilian employer before that OSS work. The source does
  not use an explicit “recruited from” formulation or provide an OSS start
  date.
- Pierre Simon is supported at high confidence by a nonshared protected
  identifier plus independent evidence of U.S. Army service and an OSS/French
  Resistance liaison role. The Army bulk name field is visibly corrupted, so
  the mismatch remains documented rather than silently corrected. The exact
  Army-to-OSS sequence is uncertain, and the Army affiliation is not labeled
  immediate. Machine & Products began in 1948 and is explicitly excluded as a
  postwar company rather than recast as pre-OSS employment.
- Exact official Army names plus nonshared protected identifiers support
  high-confidence identities for Joseph Simon at row 2, Julius Simon, Philip
  Simon, Salim I Simon, Swils Simon, Roy L Simonds, Henry J Simoneau, Daniel J
  Simonelli and Fred W Simons. Pierre Simon's identifier match is accepted
  with the additional name-conflict qualification. Army-coded entry grades and
  occupation codes remain private and were not converted into employers or
  unsupported OSS ranks.
- An official OSS commendation names an M Sgt Joseph Simon. Its protected
  identifier differs by one digit from the numbered Joseph T Simon row, while
  the two adjacent M/SGT rows carry no identifiers. The conflict is published
  without full numbers. All five Joseph rows remain separate, and Box 713 is
  required to resolve them.
- A reproduced OSS European Theater organizational chart dated 6 December
  1944 names Major Theodore Simon as the Pontarlier commanding officer. This
  is retained as a medium-confidence, visibly qualified identity lead. The
  chart does not connect that officer to the protected identifier in the index,
  so the Major rank is not copied into the normalized personnel classification
  and no pre-OSS pathway is inferred.
- A Martin Sebastian Simon obituary documents conventional Army intelligence
  training and a music career but no OSS or Box 713 bridge. A Julius M. Simon
  obituary documents Army service and later scrap-metal work but lacks the
  protected-identifier link to the indexed person. Both employment leads are
  rejected rather than transferred.
- Seven identities remain unresolved. Targeted NARA index, CIA FOIA, Library
  of Congress, newspaper, obituary, institutional, directory and archival
  searches were recorded for all 23 people. The direct CIA adapter failed
  closed on robots policy and the Library of Congress adapter returned a
  network error on the first bounded request; grouped browser searches were
  still completed. These access failures are not treated as negative evidence.
  No exposed NARA credential was used, logged or written to project data.

The cohort distribution is 11 `high_confidence`, one `probable`, one
`ambiguous`, three `conflicting` and seven `unresolved` identities. Research
status is one `verified_employer_found`, three `conflicting_sources` and 19
`requires_archival_review`; no Batch 878 person remains `not_started` or
`in_progress`. Every person has a saved non-planned research attempt.

The evidence bundle contains ten sources, two reused organizations, two
affiliations, 19 claims, 23 person updates, 23 staged research attempts and 41
claim-source links. Seventeen claims meet the public or conflict-publication
threshold; two namesake claims remain rejected review evidence. The Army
review file contains ten accepted identity decisions. Reimporting both files
is idempotent. SQLite's integrity check returned `ok`, and its foreign-key
check returned no rows.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 13,157 people (54.9651%).
- Verified-employer coverage: 432 people (1.8047%).
- Verified-affiliation coverage: 952 people (3.9771%).
- Archival-review coverage: 11,624 people (48.5608%).
- Not started: 10,775 people; in progress: 1,893 people.
- Possible duplicate groups: 584.
- Conflicts: 458 people.
- Claim confidence totals: 1,623 confirmed, 4,200 high, 1,734 medium, 210 low,
  386 conflicting and two unresolved.
- Citations: 6,634; unique source documents: 3,601.
- Public projection: 23,937 people, 2,901 affiliations, 1,089 organizations,
  5,392 sources and 7,939 published or qualified claims.
- Private derived exports: 2,922 affiliations, 1,103 organizations, 6,634
  sources, 26,802 research attempts, 23,617 NARA pull-list rows and 22,029
  unresolved rows.

Relative to Batch 877, research-attempt and archival-review coverage each
increased by 23 people. Verified-employer and verified-affiliation coverage
each increased by one through Hans Simons's New School employment. Two
affiliations, eight public sources and 17 public or conflict claims entered the
public projection. No new canonical organization was added because the United
States Army and New School for Social Research already existed.

## Validation

The evidence imports, idempotency reimports, SQLite integrity check,
foreign-key check, regenerated coverage report, public-data build and
stratified 200-profile audit pass. All 145 Python tests and 81 parameterized
subtests pass. Astro reports zero errors, warnings or hints across 509 source
files and builds 25,070 pages. The bounded release suite passes 90/90 checks:
21 Batch 878 tests across desktop, phone and tablet, 33 core responsive tests,
six analysis tests and 30 axe scans with no serious or critical violations.
All 25,070 internal HTML routes resolve. The identifier audit checks 12,926
normalized private identifiers and 120 formatted variants across 25,142
artifacts, rejects 1,312 candidate substrings as non-boundary coincidences and
finds zero unexpected matches. The public manifest verifies 67 assets and
117,604,659 bytes at SHA-256
`e4733ee5b2f659b75f56e56bf84eb6514f73ae6d7bc86510d46c37e9dabe52d5`.
Two consecutive builds reproduce output-tree SHA-256
`ffcaa28cfa4a15c2394bff856a504b2c80d3b5b429226d07d039414324911f69`.
The production dependency audit reports zero vulnerabilities.

## Publication status

Batch 878 is published at commit
`2d990fc0c395d135dcece498cd20aa9b7206d4e7`. The clean Linux Test workflow
passed in [run 39083222731](https://github.com/therealjameswilson/before-oss/actions/runs/39083222731),
and the GitHub Pages build and deploy passed in
[run 39083222717](https://github.com/therealjameswilson/before-oss/actions/runs/39083222717).
The unauthenticated release verifier confirmed all 67 manifest assets, eight
core routes, 36 source-register pages and all 23 direct Batch 878 profiles at
`https://therealjameswilson.github.io/before-oss/`.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite assign-page-batch --batch-name batch-878 --page 429 --first-row 1 --last-row 23
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch878.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page429-simon-simons-review_batch-878_2026-10-17.json
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
