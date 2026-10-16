# Batch 857 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 857 covers the 23 printed personnel rows on NARA index PDF page 418,
rows 24-46, from Catherine C Seerley through Max Seitelman. All 23 immutable
source rows remain preserved and linked to 23 separate active person entities.
The reviewed table preserves names, initials, printed ranks, private identifier
columns, Boxes 694-695 and archive location 230/86/40/04. Full service
identifiers remain private.

The two Robert N Seiple source rows remain separate because they carry
different protected identifiers. Only the first has an accepted official Army
identity bridge. Both use the same opaque public duplicate label without
exposing the durable private review key. The next unresearched boundary is PDF
page 419, row 1, Albert B Seitz.

## Research outcomes

- A contemporary May 1943 radio-industry article places Manuel Segal among
  National Broadcasting sound engineers. Lawrence C. Soley's scholarly OSS
  history identifies the same uncommon name and sound-effects specialty on the
  Soldatensender staff, while the official Army record supplies the intervening
  military chronology. National Broadcasting Company is published as his
  high-confidence, strongly date-bounded last civilian employer before service,
  not as his explicit immediate OSS predecessor.
- Brian Masaru Hayashi's scholarship explicitly says OSS recruited Fumiko
  Segawa and other privates from the WAAC Third Training Center at Fort
  Oglethorpe. The Women's Army Auxiliary Corps is therefore published as her
  immediate military assignment, never as a civilian employer.
- A February 1941 *Sozialistische Mitteilungen* supplement identifies Gerhart
  Seger as editor of Neue Volkszeitung in New York. That employment is published
  as documented prewar work only; the reviewed chronology does not show that it
  immediately preceded OSS or was his final civilian employer.
- Florian Traussnig's scholarly biography and its source notes to RG 226,
  Entry 224, Box 694 confirm Francis Seidler as Franz von Seidler. The 7th
  Photographic Intelligence Detachment of the Army Air Forces is published as
  his explicit immediate pre-OSS military assignment. His Austrian Federal
  Chancellery press-service work is an earlier government assignment. Unnamed
  Washington journalism remains occupation context rather than an invented
  employer.
- University of Bath scholarship confirms David F. Seiferheld's OSS identity.
  Source-linked secondary research documents his textile-executive occupation
  and treasurer roles with American Friends of German Freedom and the Emergency
  Rescue Committee. The two organizations remain medium-confidence professional
  affiliations rather than assumed paid employment, and the unnamed textile
  firm remains unresolved.
- An OSS Operational Groups roster corroborates Steven F. Segeti Jr.'s Greek
  Group VII identity and suffix. It establishes an OSS assignment only, not a
  pre-OSS employer or predecessor unit.
- Official Army data provides identity bridges for Alf Seierstad, Allen J
  Seilheimer, Francis Seidler, Guy E Seiber, Harry Segen, Herbert H Seidell,
  Manuel Segal, Maurice J Segal, Max Seitelman, one Robert N Seiple row and
  Steven F Segeti Jr. through nonshared protected identifiers. Army-coded
  occupation and entry-grade fields were not published as employers,
  affiliations or OSS ranks.
- CIA automated discovery was disallowed by the site's robots policy. Bounded
  Library of Congress searches returned no result for Alf Seierstad, Allen J
  Seilheimer and Elvin A Seidner, while the Francis Seidler request exhausted
  its timed retries. These constraints are retained as access limitations, not
  negative historical evidence. Authenticated NARA Catalog research remains
  disabled pending safe credential rotation.

The batch distribution is one `confirmed`, 13 `high_confidence`, one
`ambiguous` and eight `unresolved` identities. One record has
`verified_employer_found`, one has `documented_prewar_employer_found`, one has
`occupation_only_found`, two have `completed`, and 18 have
`requires_archival_review`. All 23 records have a saved non-planned research
attempt and no Batch 857 record remains `not_started`. The evidence bundle
contains 11 sources, seven organizations, seven affiliations, 22 published
claims, 23 person updates, 23 research attempts and 46 claim-source links.
SQLite's foreign-key check returned no rows and its integrity check returned
`ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,680 people (52.9724%).
- Verified-employer coverage: 418 people (1.7463%).
- Verified-affiliation coverage: 920 people (3.8434%).
- Archival-review coverage: 11,147 people (46.5681%).
- Not started: 11,252 people.
- Possible duplicate groups: 571.
- Conflicts: 446 people.
- Claim confidence totals: 1,604 confirmed, 3,993 high, 1,703 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,482; unique source documents: 3,485.
- Public projection: 23,937 people, 2,846 affiliations, 1,062 organizations,
  5,252 sources and 7,669 published claims.

Research-attempt coverage increased by all 23 people. Verified-employer
coverage increased by Manuel Segal and Gerhart Seger. Verified-affiliation
coverage increased by four people. Archival-review coverage increased by all
23 Batch 857 records.

## Validation

Local release validation passed. Python reports 145 tests passing. Astro
checked 491 files with zero errors, warnings or hints and built 25,043 static
pages. The bounded Playwright release suite passed 93/93 checks across Batch
857, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. The stratified 200-profile audit passed
every check. All internal links across 25,043 HTML files resolve; 51,379 unique
external URLs were inventoried separately. The public-identifier audit found
zero unexpected boundary matches after checking 12,926 normalized identifiers
and 120 formatted variants across 25,115 built artifacts.

The public manifest covers 67 assets totaling 115,935,683 bytes with SHA-256
`8f6e0a80a50c95a486f046108ed323c3abb6cde3ad6532748fae3cc817d374fd`.
Two production builds produced the identical 25,115-file tree hash
`69dae9dd476b512190341408b3746423acdfccbf89ad202d8c2b47d776c46b91`.

## Publication status

The reviewed Batch 857 release is locally complete. Publication and
unauthenticated immutable-release verification are pending the content commit
and successful GitHub Pages workflow.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-16_batch857.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page418-seerley-seitelman-review_batch-857_2026-10-16.json
.venv/bin/python -m oss_research --db research/research.sqlite export-derived
.venv/bin/python -m oss_research --db research/research.sqlite export-review-queue
.venv/bin/python -m oss_research --db research/research.sqlite build-public-data
.venv/bin/python -m oss_research --db research/research.sqlite coverage-report
.venv/bin/python -m oss_research --db research/research.sqlite audit-profiles --sample-size 200
.venv/bin/python -m unittest discover -s tests -v
npm --prefix site run build
npm --prefix site run test:release
npm --prefix site run check:links
.venv/bin/python scripts/verify_deployed_release.py --local-public-root site/public
.venv/bin/python scripts/audit_public_identifiers.py --database research/research.sqlite --public-root site/dist
.venv/bin/python scripts/hash_tree.py site/public site/dist
.venv/bin/python -m oss_research --db research/research.sqlite assign-page-batch --batch-name batch-858 --page 419 --first-row 1 --last-row 23
```
