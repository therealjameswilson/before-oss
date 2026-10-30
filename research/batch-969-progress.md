# Batch 969 research progress

Date: 2026-10-30

Scope: NARA OSS personnel index PDF page 475, rows 1-23 (Gaston E Tuggle
through Euclide Turcotte)

Boxes: 788-789

Archive location: 230/86/42/03

## Extraction and identity safeguards

- Visually audited index page 475 at 200 dpi and preserved all 23 researched
  rows as 23 separate people.
- Accepted ten Army identity bridges, rejected the Army candidate for Robt E
  Tullen and recorded both Tullen/Tulley duplicate candidates as conflicting.
- Robt E Tullen and Robert E Tulley share a protected index identifier but
  remain separate people. The official Army row favors Tulley; neither source
  row is silently merged.
- Protected identifiers were used only for private identity resolution. No
  full identifier, API credential, live API response or raw Army row appears
  in the evidence bundle, public data or downloads. No authenticated NARA
  Catalog API request was used.

## Reviewed outcomes

- A declassified Detachment 101 order independently confirms Gaston E
  Tuggle's exact identity and sergeant rank. His dated Army civilian-status
  category remains a qualified occupation, not a named employer.
- A National Park Service history identifies Corporal Joseph Tully as Area C
  cadre. His Army-entry category is student status and is not converted into
  a school or employer.
- A New York Times obituary links Anthony Turano to the OSS and documents an
  earlier commercial-photographer career. It does not date the beginning of
  his work with Anton Bruehl, so no studio employer is projected backward.
- Carmen Turco remains a probable, medium-confidence match to an OSS
  Operational Groups Peedee-team roster pending Box 789 review.
- The rare-name Sam/Sanguan Tularak lead remains low-confidence and withheld:
  NARA and Cambridge sources document Sanguan, but no reviewed source proves
  that the indexed forename Sam is an alias.
- Nine unresolved identities and five additional supported or ambiguous
  identities retain explicit archival-review outcomes. This batch establishes
  no new named employer.

## Exact batch outcome

- People researched: 23.
- Terminal statuses: 8 `occupation_only_found`; 14
  `requires_archival_review`; 1 `conflicting_sources`.
- Identity statuses: 1 `confirmed`; 10 `high_confidence`; 1 `probable`; 1
  `ambiguous`; 1 `conflicting`; 9 `unresolved`.
- Evidence imported: 11 sources, 0 organization inputs, 8 affiliations, 22
  claims, 57 claim-source links, 23 person updates and 23 research attempts.
- Review decisions imported: 10 accepted, 1 rejected and 2 conflicting.
- Batch claim confidence: 1 confirmed; 10 high; 9 medium; 1 low; 1
  conflicting.
- The deterministic evidence bundle SHA-256 is
  `a25642d704b8d9c38e33b82df0bf58bbae22b45a10b1896c2650567aa5de94e4`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,223 / 23,936 (63.5988%).
- Verified-affiliation coverage: 1,094 / 23,936 (4.5705%).
- Verified-employer coverage: 488 / 23,936 (2.0388%).
- Archival-review coverage: 13,699 / 23,936 (57.2318%).
- Not started: 8,708 people; in progress: 1,883 people.
- Possible-duplicate groups: 664.
- Conflicts: 521.
- Claim confidence: 1,706 confirmed; 5,080 high; 2,403 medium; 255 low;
  434 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,734 affiliations; 1,251
  organizations; 6,239 sources; 9,619 published, qualified or conflict claims.
- Private projection: 3,760 affiliations; 1,266 organizations; 7,525 sources;
  21,413 unresolved rows and 23,569 archival pull-list rows.
- Citations: 7,525 across 4,177 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- Evidence and review-decision imports are idempotent on repeated import.
- All 147 Python pipeline tests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 600 files with zero diagnostics and generated 25,237 static
  pages.
- All 30 Batch 969 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 99 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,237 HTML files resolve; 52,040 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit inspected 1,418 candidate substrings and found
  zero unexpected boundary matches.
- The local public manifest verified all 67 assets totaling 129,714,106 bytes;
  its SHA-256 is
  `613ea2528e0ea11003268877b423fc7ad8853482f7a122246c2bce1d2392f3c7`.
- The 70-file public tree totals 132,061,266 bytes and has SHA-256
  `5e0201b932da7ce51ec7722ecef1f10e75696601bb6b3cbbe82fa784cc805786`.
- The dependency audit reports zero vulnerabilities.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 969 itself is replayable and idempotent.

## Resume point

Continue with PDF page 475, row 24, **Joseph E Turcotte**, Box 789, archive
location 230/86/42/03.

## Publication verification

- Immutable content commit:
  `946b067cf7e60c4415535a0a2f69ae90031384dd`.
- GitHub Actions Test run `41006904745` and Pages run `41006904915` completed
  successfully.
- The unauthenticated deployed-release verifier matched the 67-asset,
  129,714,106-byte public manifest at SHA-256
  `613ea2528e0ea11003268877b423fc7ad8853482f7a122246c2bce1d2392f3c7`,
  all eight core routes, all 42 source-register pages and all 23 Batch 969
  profile routes to the content commit.
- Public site: <https://therealjameswilson.github.io/before-oss/>.
