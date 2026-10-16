# Batch 855 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 855 covers the 23 printed personnel rows on NARA index PDF page 417,
rows 24-46, from Dagmar S Scott through Robert F Scott. All 23 immutable
source rows remain preserved and linked to 23 separate active person entities.
The page was rendered and visually reviewed at 180 dpi; names, ranks or grades,
serial-number columns, Boxes 692-693 and archive location 230/86/40/03 align
with the printed table. Full service identifiers remain private.

Three Edward F Scott rows and two Marianne Scott rows remain distinct. Their
shared normalized names are recorded as possible-duplicate groups, but the
rows are not silently merged. `Dharles R Scott` and Herbert W Scott's printed
note `British Ci` are preserved exactly as indexed rather than silently
corrected or expanded. The next unresearched boundary is PDF page 418, row 1,
Robert Scott.

## Research outcomes

- Official Army data provides high-confidence identity bridges for **Delbert
  Scott**, **George H Scott** and **James M Scott** through nonshared protected
  identifiers. The Army suffix `Sr` is retained as a documented George H Scott
  name variant rather than inserted into the printed index name. These are
  identity findings only: Army entry-grade and occupation codes are neither
  employers nor pre-OSS affiliations.
- The three Edward F Scott records remain separate ambiguous identities. Two
  have different protected identifiers and the third has no printed identifier.
  No external evidence supports joining them.
- The two Marianne Scott records remain separate ambiguous identities. One has
  a protected identifier and one does not. A chronologically incompatible
  modern Canadian librarian was rejected as a namesake.
- Northwestern University's Franklin Daniel Scott is retained only as a
  plausible lead. The institutional evidence documents his 1935 faculty work,
  but no OSS reference or second identifier connects that historian to the
  indexed Franklin D Scott; Northwestern is therefore not published as this
  person's employer.
- An obituary describing a Lillie Scott who performed wartime aircraft work
  lacks a middle name or OSS bridge and was rejected. A public award candidate
  for Richard P Scott has an identifier incompatible with the private index
  row and was rejected. Library of Congress and West Virginia University
  records describe different Robert F Scott service contexts; neither bridges
  to the index record. No occupation or employer was imported from these
  namesakes.
- The remaining incomplete or common-name records received exact-name,
  OSS-context, employment-oriented and institutional or archival discovery
  checks. Unsupported biographical matches were rejected rather than assigned.
- Library of Congress discovery timed out after bounded retries, and CIA
  automated discovery remained unavailable under the source's robots policy.
  These are access limitations, not evidence that relevant records do not
  exist. Authenticated NARA Catalog research remains disabled pending safe API
  credential rotation.

The batch distribution is three `high_confidence`, six `ambiguous` and 14
`unresolved` identities. All 23 records have the terminal
`requires_archival_review` status and a saved staged-protocol attempt. The
evidence bundle contains two sources, no organizations or affiliations, three
published identity claims, 23 person updates, 23 research attempts and six
claim-source links. Three Army candidates were accepted for identity only.
SQLite's foreign-key check returned no rows and its integrity check returned
`ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  unlinked superseded entities retained for auditability.
- Research-attempt coverage: 12,635 people (52.7844%).
- Verified-employer coverage: 414 people (1.7295%).
- Verified-affiliation coverage: 912 people (3.8100%).
- Archival-review coverage: 11,101 people (46.3759%).
- Not started: 11,297 people.
- Possible duplicate groups: 569.
- Conflicts: 445 people.
- Claim confidence totals: 1,601 confirmed, 3,961 high, 1,700 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,464; unique source documents: 3,470.
- Public projection: 23,937 people, 2,834 affiliations, 1,055 organizations,
  5,234 sources and 7,631 claims.

Research-attempt coverage increased by 22 rather than 23 because Dharles R
Scott already had a prior pilot attempt. Archival-review coverage increased by
all 23 Batch 855 records.

## Validation

Local release validation passed. Python reports 145/145 tests plus 81
subtests passing. Astro checked 489 files with zero errors, warnings or hints
and built 25,035 static pages. The bounded Playwright release suite passed
81/81 checks across Batch 855, core routes, the oil-company category,
analytics and accessibility at desktop, phone and tablet viewports. The
stratified 200-profile audit passed every check. All internal links across
25,035 HTML files resolve; 51,359 unique external URLs were inventoried
separately. The public-identifier audit found zero unexpected boundary matches
after checking 12,926 normalized identifiers and 120 formatted variants across
25,107 built artifacts.

The public manifest covers 67 assets totaling 115,681,276 bytes with SHA-256
`063483284b40af23676cbc5e8bba6cecf69a82906c244fc7807ccaf42090b739`.
Two production builds produced the identical 25,107-file tree hash
`23743b6c483d6eccb47490b3189c923964210aa7f0128b309795383054417e04`.

## Publication status

Published from content commit
`aebd6175f057ea09b3a6b69da607595ec97ced64`. GitHub Pages run
`38941387184` and Test run `38941387020` completed successfully. The
unauthenticated immutable verifier checked all 67 manifested assets
(115,681,276 bytes), eight core routes, 35 source-register pages and all 23
Batch 855 direct profile routes at
`https://therealjameswilson.github.io/before-oss/`. The live manifest SHA-256
is `063483284b40af23676cbc5e8bba6cecf69a82906c244fc7807ccaf42090b739`,
matching the reviewed release. Live statistics report 12,635
research-attempted people, 414 verified-employer profiles, 912
verified-affiliation profiles and 11,101 people with archival-review
assessment. The overall every-person research goal remains active.

## Resume commands

```bash
.venv/bin/python -m oss_research --db research/research.sqlite import-review-decisions research/army_review_decisions_2026-10-16_batch855.csv
.venv/bin/python -m oss_research --db research/research.sqlite import-reviewed-evidence research/evidence-page417-scott-review_batch-855_2026-10-16.json
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
.venv/bin/python -m oss_research --db research/research.sqlite assign-page-batch --batch-name batch-856 --page 418 --first-row 1 --last-row 23
```
