# Batch 968 research progress

Date: 2026-10-30

Scope: NARA OSS personnel index PDF page 474, rows 24-46 (Michalis Tsirmulas
through Margaret E Tugas)

Boxes: 787-788

Archive location: 230/86/42/03

## Extraction and identity safeguards

- Visually audited index page 474 at 200 dpi and preserved all 23 researched
  rows as 23 separate people.
- Accepted seven protected-identifier Army identity bridges. Dated Army
  occupations are published only as qualified occupation, student or military
  evidence, never as invented employers.
- Michalis Tsirmulas has an exact official casualty-and-unit record and a
  documented OSS Greek Operational Group connection. James Tsolas retains the
  supported variant James A Tsolas and his Greek Operational Group context.
- Protected identifiers were used only for private identity resolution. No
  full identifier, API credential, live API response or raw Army row appears
  in the evidence bundle, public data or downloads. No authenticated NARA
  Catalog API request was used.

## Reviewed outcomes

- John E Tsouderos's U.S. Army Field Artillery pathway is separate from his
  last known civilian occupation as a busboy or waiter; no civilian employer
  is invented.
- Henry J Tsurutani's Manzanar Legal Aid work is classified as a government
  assignment, while his earlier Los Angeles attorney occupation remains
  separate and does not imply a named firm.
- Robert C Tucker's Harvard evidence is student status and Russian-language
  training, not Harvard employment. William R Tucker likewise remains a
  student-status finding rather than an employer claim.
- Laura W Tuckerman's earlier work in an unnamed dress shop is retained as
  qualified prewar employment and is not promoted to an immediate affiliation.
- Twelve unresolved identities retain dignified archival-review outcomes.
  This batch establishes no new named employer.

## Exact batch outcome

- People researched: 23.
- Terminal statuses: 11 `occupation_only_found`; 12
  `requires_archival_review`.
- Identity statuses: 1 `confirmed`; 10 `high_confidence`; 12 `unresolved`.
- Evidence imported: 14 sources, 3 organization input records, 14
  affiliations, 25 claims, 59 claim-source links, 23 person updates and 23
  research attempts.
- Review decisions imported: 7 accepted.
- Batch claim confidence: 1 confirmed; 13 high; 11 medium.
- The deterministic evidence bundle SHA-256 is
  `a3d757b130db4e76193f17d498c74b9259fa8eccfbb177add691909e525a61f3`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,200 / 23,936 (63.5027%).
- Verified-affiliation coverage: 1,094 / 23,936 (4.5705%).
- Verified-employer coverage: 488 / 23,936 (2.0388%).
- Archival-review coverage: 13,676 / 23,936 (57.1357%).
- Not started: 8,731 people; in progress: 1,883 people.
- Possible-duplicate groups: 664.
- Conflicts: 520.
- Claim confidence: 1,705 confirmed; 5,070 high; 2,394 medium; 254 low;
  433 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,726 affiliations; 1,251
  organizations; 6,230 sources; 9,598 published, qualified or conflict claims.
- Private projection: 3,752 affiliations; 1,266 organizations; 7,514 sources;
  21,421 unresolved rows and 23,569 archival pull-list rows.
- Citations: 7,514 across 4,172 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- Evidence and review-decision imports are idempotent on repeated import.
- All 147 Python pipeline tests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 599 files with zero diagnostics and generated 25,237 static
  pages.
- All 30 Batch 968 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 99 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,237 HTML files resolve; 52,038 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit inspected 1,418 candidate substrings and found
  zero unexpected boundary matches.
- The local public manifest verified all 67 assets totaling 129,586,516 bytes;
  its SHA-256 is
  `597416f9aa0a914f979bdaac5fec3697dfd30935ce57de564b97d1c01261050a`.
- The 70-file public tree totals 131,933,688 bytes and has SHA-256
  `0a73c5f3d9aee92fd978a2ab828d2cc65ad9fe55f918d2e84a4ff09302e06280`.
- The dependency audit reports zero vulnerabilities.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 968 itself is replayable and idempotent.

## Resume point

Continue with PDF page 475, row 1, **Gaston E Tuggle**, Box 788, archive
location 230/86/42/03.

## Publication verification

Publication is pending the immutable content commit, GitHub Actions checks and
unauthenticated deployed-release verification.
