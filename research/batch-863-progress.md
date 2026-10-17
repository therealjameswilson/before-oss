# Batch 863 research progress

Date: 2026-10-17 America/New_York

## Scope and source validation

Batch 863 covers the 23 printed personnel rows on NARA index PDF page 421,
rows 24-46, from Eli Shapiro through Lee M Sharrar. All 23 immutable source
rows remain preserved and linked to 23 separate active person entities. The
reviewed table preserves names, initials, printed ranks, private identifier
columns, Boxes 699-700 and archive location 230/86/40/04. Full service
identifiers remain private. The next unresearched boundary is PDF page 422,
row 1.

## Research outcomes

- Official Army bulk data, the Library of Congress finding aid for the Karl
  Jay Shapiro Papers and Baltimore Heritage evidence support a high-confidence
  identity for Karl J Shapiro. His 1939-1941 Enoch Pratt Library School
  attendance is published as student status, not employment. Army service
  intervened before OSS, so the school is not marked as an immediate pre-OSS
  affiliation or last civilian employer.
- The uncommon name and major rank confirm Lee M Sharrar through direct NARA
  OSS and Strategic Services Unit records. A March 4, 1940 Texas General Land
  Office scan of Humble Oil & Refining Company Legal Department letterhead
  identifies Sharrar as an attorney. It is published as the latest identifiable
  civilian employer before wartime service, not as a proven direct transition
  into the Army or OSS. A January 6, 1933 contemporary newspaper separately
  documents his earlier work as an economics instructor at Rice Institute.
  Sharrar therefore appears in the evidence-qualified oil-company category.
- The adjacent John B Sharp rows remain separate. The Corporal row has a
  high-confidence official Army identity bridge. The official candidate tied
  to the rankless row's different protected identifier names Bletz Fred R and
  was rejected; no information was transferred from that namesake.
- The two Samuel L Sharp rows remain separate because their protected
  identifiers differ and no direct source proves duplication. Doris Sharrai
  and Doris A Sharrar also remain separate in a visible possible-duplicate
  group: the one-letter surname difference and shared box justify comparison,
  not a merge. Existing high-confidence evidence for Doris A Sharrar is not
  transferred to Doris Sharrai.
- Walter R Sharp remains unresolved. The Walter Rice Sharp academic biography
  is a plausible namesake lead, but no accessible source bridges it to the
  indexed OSS person, so no biography or employer claim was assigned.
- Official Army bulk data supplies six accepted identity-only bridges and one
  rejected candidate. Army-coded occupation and entry fields remain private
  and were not published as employers, OSS ranks or affiliations.
- CIA Reading Room, Library of Congress, exact-name OSS, employment,
  occupation, obituary and institutional searches were saved for all 23
  people. Incompatible namesakes and search snippets were rejected rather than
  converted into claims. Authenticated NARA Catalog research remains disabled
  pending safe credential rotation.

The batch distribution is one `confirmed`, seven `high_confidence`, one
`ambiguous` and 14 `unresolved` identities. Twenty-two records are
`requires_archival_review`; Lee M Sharrar is
`documented_prewar_employer_found`. Every person has a saved non-planned
research attempt and no Batch 863 record remains `not_started`. The evidence
bundle contains seven sources, three organizations, three affiliations, ten
published claims, 23 person updates, 23 research attempts and 22 embedded
claim-source links. Six Army candidates were individually accepted and one was
rejected. SQLite's foreign-key check returned no rows and its integrity check
returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,817 people (53.5447%).
- Verified-employer coverage: 423 people (1.7671%).
- Verified-affiliation coverage: 932 people (3.8936%).
- Archival-review coverage: 11,284 people (47.1404%).
- Not started: 11,115 people.
- Possible duplicate groups: 575.
- Conflicts: 447 people.
- Claim confidence totals: 1,611 confirmed, 4,062 high, 1,712 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,529; unique source documents: 3,520.
- Public projection: 23,937 people, 2,866 affiliations, 1,072 organizations,
  5,298 sources and 7,754 published or qualified claims.

Research-attempt and archival-review coverage each increased by 22 people;
Doris A Sharrar already had a prior attempt and archival disposition. Verified
affiliation coverage increased through Karl J Shapiro and Lee M Sharrar.
Verified-employer coverage increased through Lee M Sharrar.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. Astro checked 497 files with zero errors, warnings or hints
and built 25,053 static pages. The bounded Playwright release suite passed
87/87 checks across Batch 863, core routes, the oil-company category, analytics
and accessibility at desktop, phone and tablet viewports. The stratified
200-profile audit passed every check. All internal links across 25,053 HTML
files resolve; 51,414 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,125 built
artifacts.

The public manifest covers 67 assets totaling 116,488,321 bytes with SHA-256
`c5eb292a751bc4f3ad87e0e7c0a9bcd45cc8b79c2738a854d22ab3f762d8bdca`.
Two production builds produced the identical 25,125-file static-site hash
`d79441e41246bc4c8e1d1d9a7740d2b69e4cdc0196599d06da5cfe913df43f3a`.

## Publication status

Published from content commit
`b2657badbac2d12dfcfc2412efd72d0f48421058`. GitHub Pages run
`39038466789` and Test run `39038466806` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(116,488,321 bytes), eight core routes, 36 source-register pages and all 23
direct profile routes referenced by the evidence bundle at
`https://therealjameswilson.github.io/before-oss/`. The live manifest SHA-256
is `c5eb292a751bc4f3ad87e0e7c0a9bcd45cc8b79c2738a854d22ab3f762d8bdca`,
matching the reviewed release. Live statistics report generation time
`2026-10-17T15:32:00Z`, 12,817 research-attempted people, 423 verified-
employer profiles, 932 verified-affiliation profiles and 11,284 people with
archival-review assessment.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-17_batch863.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page421-shapiro-sharrar-review_batch-863_2026-10-17.json
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
