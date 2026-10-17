# Batch 861 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 861 covers the 23 printed personnel rows on NARA index PDF page 420,
rows 24-46, from Francis D Severance through Andrew W Shaffer. All 23 immutable
source rows remain preserved and linked to 23 separate active person entities.
The reviewed table preserves names, initials, printed ranks, private identifier
columns, Boxes 697-698 and archive location 230/86/40/04. Full service
identifiers remain private. The next unresearched boundary is PDF page 421,
row 1.

## Research outcomes

- A University of Washington institutional history identifies Marjorie M.
  Severyns Ravenholt and explicitly documents her OSS service in India and
  China. Her University of Washington graduation and Fletcher School study are
  published as student affiliations, not employers. A Board of Economic
  Warfare reference was not modeled as pre-OSS because the source does not
  establish its sequence relative to OSS service.
- A 1975 interview with artist Kurt Schaffenberger supplies a rare-name and
  rank-specific bridge to the indexed Kurt P. Shaffenberger. It documents Jack
  Binder's studio as his last civilian employer before Army induction and an
  Army art assignment as his immediate pre-OSS military affiliation. The
  interview does not name a formal Army unit, so none was invented. The index
  spelling remains authoritative and `Kurt Schaffenberger` is preserved as a
  documented variant.
- German National Library authority data and a contemporary *Time* books list
  support a probable Felizia M. Seyd identity and the visibly qualified
  medium-confidence conclusion that she was a published author before U.S.
  entry into World War II. Viking was the publisher of a cited book, not a
  documented employer, and no employment affiliation was created.
- The Library of Congress European Mission roster supports a probable Daniel
  Shacter identity but documents a 1945-1946 postwar assignment. It is retained
  as identity context and is not misrepresented as a pre-OSS affiliation.
- Official Army bulk data supplies identity-only bridges for Francis D.
  Severance, William K. Severin, Glen H. Severt, Joe H. Sevier, Lewis V.
  Sevier, Pete S. Sfikas, Jack Shafer and Andrew W. Shaffer. The `Jr.` form for
  Joe H. Sevier is retained as a documented variant. Army-coded occupation and
  entry fields were not published as employers, OSS ranks or affiliations.
- Postwar restaurant evidence for Pete S. Sfikas and insufficient namesake
  matches for the remaining people were rejected rather than converted into
  pre-OSS claims. Authenticated NARA Catalog research remains disabled pending
  safe credential rotation.

The batch distribution is ten `high_confidence`, two `probable`, seven
`ambiguous` and four `unresolved` identities. One record is
`verified_employer_found`, one is `occupation_only_found`, and 21 are
`requires_archival_review`. All 23 records have a saved non-planned research
attempt and no Batch 861 record remains `not_started`. The evidence bundle
contains seven sources, four organizations, four affiliations, 17 published
or qualified claims, 23 person updates, 23 research attempts and 31
claim-source links. Eight Army candidates were individually reviewed and
accepted. SQLite's foreign-key check returned no rows and its integrity check
returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,772 people (53.3567%).
- Verified-employer coverage: 422 people (1.7630%).
- Verified-affiliation coverage: 929 people (3.8810%).
- Archival-review coverage: 11,239 people (46.9524%).
- Not started: 11,160 people.
- Possible duplicate groups: 572.
- Conflicts: 447 people.
- Claim confidence totals: 1,608 confirmed, 4,047 high, 1,709 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,516; unique source documents: 3,510.
- Public projection: 23,937 people, 2,861 affiliations, 1,069 organizations,
  5,285 sources and 7,733 published or qualified claims.

Research-attempt and archival-review coverage each increased by all 23 people.
Verified-employer coverage increased by Kurt Schaffenberger. Verified-
affiliation coverage increased by Kurt Schaffenberger and Marjorie Severyns
Ravenholt. Felizia Seyd's medium-confidence occupation remains outside the
default confirmed/high employer and affiliation metrics.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. Astro checked 495 files with zero errors, warnings or hints
and built 25,050 static pages. The bounded Playwright release suite passed
87/87 checks across Batch 861, core routes, the oil-company category, analytics
and accessibility at desktop, phone and tablet viewports. The stratified
200-profile audit passed every check. All internal links across 25,050 HTML
files resolve; 51,404 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,122 built
artifacts.

The public manifest covers 67 assets totaling 116,338,637 bytes with SHA-256
`fc6f9af1cd318a363f67b4db75f92afb4d1ce1fb171097543f866db59a95229b`.
Two production builds produced the identical 25,122-file tree hash
`2b49e3b2a169da6a4f8bd487641556f20b27e2712acb901a6135e004bbc407ab`.

## Publication status

Ready for publication after all local data, redaction, software, link and
deterministic-build gates passed. The prior public release remains Batch 860
until the reviewed content commit is deployed and verified unauthenticated.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch861.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page420-severance-shaffer-review_batch-861_2026-10-17.json
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
.venv/bin/python scripts/hash_tree.py site/public site/dist
```
