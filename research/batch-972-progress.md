# Batch 972 research progress

Date: 2026-10-30

Scope: NARA OSS personnel index PDF page 476, rows 24-46 (George B Tweed
through John Tyson)

Boxes: 791-792

Archive location: 230/86/42/03

## Extraction and identity safeguards

- Visually audited index page 476 at original detail and preserved all 23
  researched rows as 23 separate people.
- Accepted six people through seven official Army candidate rows. Marvin E
  Tyree's two same-identifier records remain duplicate official rows supporting
  one identity; both dates follow OSS dissolution and neither is projected
  backward into a pre-OSS claim.
- John E Tyczkowski's protected-identifier candidate prints the name as
  Tyczkowski Ohn E. The missing-initial conflict remains explicit, no occupation
  was transferred, and Box 791 review is required.
- Protected identifiers were used only for private identity resolution. No
  full identifier, API credential, live API response or raw Army row appears
  in the evidence bundle, public data or downloads. No authenticated NARA
  Catalog API request was used.

## Reviewed outcomes

- Denver Public Library's 10th Mountain Division roster places Otto Twingley
  in D Company, 99th Infantry. Vesterheim's institutional history documents
  July 1943 recruitment from the 99th into the OSS Norwegian Operational Group
  and names T/5 Otto Twingley in Percy Red. The 99th is accepted as his
  strongly date-bounded immediate military assignment, not a civilian employer.
- The same Denver roster places a probable John B Tweedy identity in E Company,
  86th Infantry. Because the roster lacks a service number or direct OSS bridge,
  the military assignment remains qualified and temporally uncertain pending
  Box 791 review.
- Princeton and Miami obituaries identify John Tyson as a partner in
  Hutchinson, Rivinus & Co. before he volunteered for OSS shortly after Pearl
  Harbor. The firm is accepted as his immediate and last civilian employer;
  his earlier Pennsylvania Railroad fireman work remains a separate documented-
  prewar affiliation. An independent U.S. Army Special Operations history
  corroborates Captain John Tyson's OSS training role.
- Official Army records support qualified occupation-only findings for
  Lawrence L Tweedy, John J Twork, Robert W Tyler and Stephen Tymonko. The
  historical categories identify no named employer or workplace and remain
  outside verified-employer analytics.
- Fourteen unresolved identities retain explicit archival-review outcomes.
  George R Tweed was rejected for George B Tweed because the middle initial
  conflicts; other exact-name and variant searches supplied no defensible
  identity bridge or pre-OSS chronology.

## Exact batch outcome

- People researched: 23.
- Terminal statuses: 1 `verified_employer_found`; 4
  `occupation_only_found`; 1 `conflicting_sources`; 17
  `requires_archival_review`.
- Identity statuses: 7 `high_confidence`; 1 `probable`; 1 `conflicting`; 14
  `unresolved`.
- Evidence imported: 10 sources, 4 organization inputs, 8 affiliations, 19
  claims, 50 claim-source links, 23 person updates and 23 research attempts.
- Review decisions imported: 6 accepted people across 7 accepted candidate
  rows and 1 conflicting candidate.
- Batch claim confidence: 11 high; 7 medium; 1 conflicting.
- The deterministic evidence bundle SHA-256 is
  `b79cbe1cee478051ee9f0477673442107725cb81121411927f9deeea04d932aa`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,292 / 23,936 (63.8870%).
- Verified-affiliation coverage: 1,097 / 23,936 (4.5831%).
- Verified-employer coverage: 490 / 23,936 (2.0471%).
- Archival-review coverage: 13,768 / 23,936 (57.5201%).
- Not started: 8,639 people; in progress: 1,883 people.
- Possible-duplicate groups: 664.
- Conflicts: 523.
- Claim confidence: 1,706 confirmed; 5,114 high; 2,426 medium; 255 low;
  436 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,759 affiliations; 1,255
  organizations; 6,263 sources; 9,678 published, qualified or conflict claims.
- Private projection: 3,785 affiliations; 1,270 organizations; 7,549 sources;
  21,394 unresolved rows and 23,567 archival pull-list rows.
- Citations: 7,549 across 4,189 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- Evidence and review-decision imports are idempotent on repeated import.
- All 147 Python pipeline tests and 84 subtests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 603 files with zero diagnostics and generated 25,241 static
  pages.
- All 30 Batch 972 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 99 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,241 HTML files resolve; 52,052 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit checked 12,926 normalized identifiers and 120
  formatted variants across 25,313 output artifacts, inspected 1,420 candidate
  substrings, and found zero unexpected boundary, aggregate or manifest-size
  matches.
- Two consecutive builds reproduced the same 67-asset, 130,131,796-byte public
  manifest at SHA-256
  `04bc0c5532115971d745853a0682a9a73077b799828b89e00505b53d9997b21c`.
- The reproduced 70-file public tree totals 132,478,960 bytes and has SHA-256
  `e7e2bd1ab4b4bb9ccc9cf9a01e87e07dd6910f6aef97d41bef8b07feb54ef5c4`.
- The reproduced 25,313-file output tree totals 418,070,510 bytes and has
  SHA-256
  `547b74b4f4be989c1e92936026e3d87e176cc9d181354e29dea0e155288c03c5`.
- The dependency audit reports zero vulnerabilities.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 972 itself is replayable and idempotent.

## Resume point

Continue with PDF page 477, row 1, **Robert M Tyson**, Box 792, archive
location 230/86/42/04.

## Publication verification

Published from immutable content commit
`5b9c9ccb50bdb78ad8fd2eda324d07e0909ba976`. GitHub Actions Test run
`41017086287` and Pages run `41017086290` succeeded. The unauthenticated
deployed-release verifier matched all 67 public assets (130,131,796 bytes;
manifest SHA-256
`04bc0c5532115971d745853a0682a9a73077b799828b89e00505b53d9997b21c`),
eight core routes, 42 source-register pages and all 23 Batch 972 direct profile
routes at <https://therealjameswilson.github.io/before-oss/>.
