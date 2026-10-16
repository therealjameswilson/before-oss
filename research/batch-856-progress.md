# Batch 856 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 856 covers the 23 printed personnel rows on NARA index PDF page 418,
rows 1-23, from Robert Scott through Helen Seeman. All 23 immutable source
rows remain preserved and linked to 23 separate active person entities. The
page was rendered and visually reviewed at 180 dpi; names, the printed
Lieutenant Commander rank, private identifier columns, Boxes 693-694 and
archive locations 230/86/40/03-04 align with the printed table. Full service
identifiers remain private.

Jay Seeley and the adjacent Jay S Seely remain separate entities in an opaque
possible-duplicate group. James Securanza remains separate from James P
Sicuranza on page 426. Their private identifier conflict is represented by an
opaque archival group label rather than embedding the identifier in durable
review metadata. The next unresearched boundary is PDF page 418, row 24,
Catherine C Seerley.

## Research outcomes

- CIA-published biographical evidence supports a high-confidence Winston
  Mackinley Scott identity. The Federal Bureau of Investigation is published
  as his explicit immediate pre-OSS government assignment, while University
  of Alabama teaching is separately published as his strongly date-bounded
  last civilian employment before wartime government service. Exact dates and
  academic rank remain unstated. The FBI Vault subject file was located, but
  its document download returned an access challenge and was not used as claim
  evidence.
- A direct official OSS Cairo report confirms Jay Seeley as the Research and
  Analysis Branch chief. Richard Clogg's scholarly history connects the same
  uncommon name to teaching at Anatolia College in Thessaloniki. The teaching
  is published as documented prewar employment, not as the immediate
  predecessor or last civilian employer.
- The same official Cairo report and Amherst College's institutional finding
  aid confirm Dorothea C Seelye as Dorothea Chambers Seelye Franck. Bryn Mawr
  College is published as a student affiliation, not employment. Box 694 is
  still needed for her immediate predecessor and last civilian employer.
- The Washington Post obituary supports a high-confidence Theodora Sedgwick
  Bond identity and documents Radcliffe attendance before her wartime OSS
  service. Radcliffe is published as student status, not an employer; her work
  in Washington remains an archival question.
- Official Army data provides high-confidence identity bridges for Antonio
  Sechi, Fred R Sechler, Peter A Seckan, Walter A Seder, Wilfred E Sederholm,
  Thomas I Sedgwick and Robert G Seeley through nonshared protected
  identifiers. These are identity findings only: Army entry-grade and coded
  occupation values are neither employers nor pre-OSS affiliations.
- The Army candidate for James Securanza was rejected because its surname and
  middle initial align with the separate James P Sicuranza row, whose private
  identifier is also shared. Both rows remain separate pending comparison of
  Boxes 694 and 709.
- Historical New York Guard and Episcopal records for Charles B Scovil remain
  a plausible but unbridged namesake lead. A postwar government-register entry
  for Wilfred E Sederholm was explicitly excluded from the pre-OSS question.
  Other common-name, modern, cemetery and sensitive people-search results were
  rejected rather than imported.
- CIA automated discovery and Library of Congress access limits were recorded
  as source-access constraints, not negative evidence. Authenticated NARA
  Catalog research remains disabled pending safe API credential rotation.

The batch distribution is two `confirmed`, nine `high_confidence`, two
`ambiguous`, one `conflicting` and nine `unresolved` identities. Two records
have `verified_employer_found`, one has `conflicting_sources`, and 20 have
`requires_archival_review`. All 23 records have a saved non-planned research
attempt and no Batch 856 record remains `not_started`. The evidence bundle
contains seven sources, five organizations, five affiliations, 16 published
claims, 24 person updates, 23 research attempts and 30 claim-source links.
SQLite's foreign-key check returned no rows and its integrity check returned
`ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,657 people (52.8763%).
- Verified-employer coverage: 416 people (1.7379%).
- Verified-affiliation coverage: 916 people (3.8267%).
- Archival-review coverage: 11,124 people (46.4720%).
- Not started: 11,275 people.
- Possible duplicate groups: 570.
- Conflicts: 446 people.
- Claim confidence totals: 1,603 confirmed, 3,975 high, 1,700 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,471; unique source documents: 3,476.
- Public projection: 23,937 people, 2,839 affiliations, 1,057 organizations,
  5,241 sources and 7,647 published claims.

Research-attempt coverage increased by 22 rather than 23 because Robert G
Seeley already had prior adapter attempts. Verified-employer coverage increased
by Winston M Scott and Jay Seeley. Verified-affiliation coverage increased by
those two people plus Dorothea C Seelye and Theodora Sedgwick. Archival-review
coverage increased by all 23 Batch 856 records.

## Validation

Local release validation passed. Python reports 145 tests passing. Astro
checked 489 files with zero errors, warnings or hints and built 25,037 static
pages. The bounded Playwright release suite passed 84/84 checks across Batch
856, core routes, the oil-company category, analytics and accessibility at
desktop, phone and tablet viewports. The stratified 200-profile audit passed
every check. All internal links across 25,037 HTML files resolve; 51,366 unique
external URLs were inventoried separately. The public-identifier audit found
zero unexpected boundary matches after checking 12,926 normalized identifiers
and 120 formatted variants across 25,109 built artifacts.

The public manifest covers 67 assets totaling 115,786,491 bytes with SHA-256
`4acbcef01fe19cf8a36866c212a160c265b9bce6be83d2a5b955adc3855e4524`.
Two production builds produced the identical 25,109-file tree hash
`2349552601ceb52d845e7b38d80b2a971de60ca1aabf7b9b434cf31b31e17176`.

## Publication status

The reviewed Batch 856 release is locally complete and awaiting commit,
GitHub Pages deployment and unauthenticated immutable verification. The
overall every-person research goal remains active.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-16_batch856.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page418-scott-seeman-review_batch-856_2026-10-16.json
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
.venv/bin/python -m oss_research --db research/research.sqlite assign-page-batch --batch-name batch-857 --page 418 --first-row 24 --last-row 46
```
