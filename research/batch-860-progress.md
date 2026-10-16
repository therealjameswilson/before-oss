# Batch 860 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 860 covers the 23 printed personnel rows on NARA index PDF page 420,
rows 1-23, from Walter Sereda through Paul D Sevcik. All 23 immutable source
rows remain preserved and linked to 23 separate active person entities. The
reviewed table preserves names, initials, printed ranks, private identifier
columns, Boxes 696-697 and archive location 230/86/40/04. Full service
identifiers remain private. The next unresearched boundary is PDF page 420,
row 24, Francis D Severance.

## Research outcomes

- An American-Turkish Society of Indiana memorial identifies Beurt R.
  SerVaas and explicitly states that he taught chemistry and Spanish at
  Shortridge High School immediately before joining OSS. Shortridge is
  therefore published as both his immediate pre-OSS affiliation and last
  civilian employer. The Congressional Record independently corroborates his
  wartime service.
- A contemporary *New Yorker* profile and the Smithsonian National Air and
  Space Museum document Boris Sergievsky's earlier work as Sikorsky Aircraft's
  chief test pilot and his later vice-presidency at the Helicopter Corporation
  of America by August 1940. Both are published as documented prewar
  employment, but neither is labeled immediate or last because the sources do
  not close the chronology to OSS entry.
- Paul Paillole's AASSDN biography and its linked chronology support Andre
  Serot as French officer André Sérot. His French military-intelligence and
  Air Force security assignments are published as military assignments, not
  civilian employers. His personnel category is corrected to foreign or
  Allied military personnel while preserving commissioned status.
- Rhode Island Historical Society and Alfred de Grazia sources support a
  probable Renzo Sereno identity and document University of Chicago
  political-science research-assistant employment. The medium-confidence claim
  is visibly qualified and excluded from default confirmed/high analytics.
- Operational Group sources corroborate Anthony J. Serelis and John J. Sersen
  as enlisted Army personnel. Those sources do not establish pre-OSS
  employers.
- Official Army bulk data supplies identity-only bridges for Walter Sereda,
  Anthony J Serelis, William Seremitis, Edwin P Serian, Edison C Serna, John J
  Sersen, Harry M Servis and Raymond P Sessions. The William G. Seremetis
  spelling is retained as a documented variant. Army-coded occupation and
  entry fields were not published as employers, OSS ranks or pre-OSS
  affiliations.
- Plausible but insufficient namesakes and undated references were rejected
  rather than converted into claims. Authenticated NARA Catalog research
  remains disabled pending safe credential rotation.

The batch distribution is eleven `high_confidence`, one `probable` and eleven
`unresolved` identities. One record is `verified_employer_found`, two are
`documented_prewar_employer_found`, and 20 are `requires_archival_review`. All
23 records have a saved non-planned research attempt and no Batch 860 record
remains `not_started`. The evidence bundle contains 13 sources, six
organizations, six affiliations, 19 published claims, 23 person updates, 23
research attempts and 39 claim-source links. Eight Army candidates were
individually reviewed and accepted. SQLite's foreign-key check returned no
rows and its integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,749 people (53.2606%).
- Verified-employer coverage: 421 people (1.7588%).
- Verified-affiliation coverage: 927 people (3.8727%).
- Archival-review coverage: 11,216 people (46.8563%).
- Not started: 11,183 people.
- Possible duplicate groups: 572.
- Conflicts: 447 people.
- Claim confidence totals: 1,608 confirmed, 4,033 high, 1,706 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,509; unique source documents: 3,504.
- Public projection: 23,937 people, 2,857 affiliations, 1,068 organizations,
  5,278 sources and 7,716 published claims.

Research-attempt and archival-review coverage each increased by all 23 people.
Verified-employer coverage increased by Beurt SerVaas and Boris Sergievsky.
Verified-affiliation coverage increased by SerVaas, Sergievsky and André
Sérot. Renzo Sereno's medium-confidence result remains outside the default
confirmed/high verified metrics.

## Validation

Local release validation passed. Python reports 145 tests and 81 parameterized
subtests passing. Astro checked 494 files with zero errors, warnings or hints
and built 25,049 static pages. The bounded Playwright release suite passed
87/87 checks across Batch 860, core routes, the oil-company category, analytics
and accessibility at desktop, phone and tablet viewports. The stratified
200-profile audit passed every check. All internal links across 25,049 HTML
files resolve; 51,399 unique external URLs were inventoried separately. The
public-identifier audit found zero unexpected boundary matches after checking
12,926 normalized identifiers and 120 formatted variants across 25,121 built
artifacts.

The public manifest covers 67 assets totaling 116,241,856 bytes with SHA-256
`02cfe97ad88d326979996746b65ee051a3f8d3f251a27eab5b3da358dace1127`.
Two production builds produced the identical 25,121-file tree hash
`f76328427f5bc93da4c4369d388c36e20657f69687a3ae984f436914945ca4d9`.

## Publication status

Publication and immutable live verification are pending. The overall
every-person research goal remains active.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-16_batch860.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page420-sereda-sevcik-review_batch-860_2026-10-16.json
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
.venv/bin/python -m oss_research --db research/research.sqlite assign-page-batch --batch-name batch-861 --page 420 --first-row 24 --last-row 46
```
