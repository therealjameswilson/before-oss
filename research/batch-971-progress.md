# Batch 971 research progress

Date: 2026-10-30

Scope: NARA OSS personnel index PDF page 476, rows 1-23 (Olive J Turner
through Edgar H Twamley)

Boxes: 789-790

Archive location: 230/86/42/03

## Extraction and identity safeguards

- Visually audited index page 476 at 200 dpi and preserved all 23 researched
  rows as 23 separate people.
- Accepted seven exact Army identity bridges. Four publish only qualified,
  dated occupation categories; three provide identity evidence without a
  usable pre-OSS occupation.
- Wilmore J Turner's protected-identifier candidate records the name as
  Turner J W. The initial conflict remains explicit, no occupation was
  transferred, and Box 789 review is required.
- Protected identifiers were used only for private identity resolution. No
  full identifier, API credential, live API response or raw Army row appears
  in the evidence bundle, public data or downloads. No authenticated NARA
  Catalog API request was used.

## Reviewed outcomes

- Official NARA awards-board minutes and attachment identify Pierre M Turquet
  as a British Army major in the OSS Secret Intelligence context in June-July
  1945. An independent biographical record supports his Royal Army Medical
  Corps assignment. The military affiliation is published as temporally
  uncertain, not as an immediate pre-OSS predecessor or civilian employer.
- Contemporary September 1944 and July 1945 issues of *Broadcasting* identify
  Edgar H Twamley as WBEN's station director before a confidential overseas
  government assignment and later as recently in OSS. WBEN is accepted as his
  strongly date-bounded immediate and last civilian employer; his earlier NBC
  station-relations work remains a separate documented-prewar affiliation.
- Official Army category records support qualified occupation-only findings
  for Vernon R Turner, Willison H Turney, Kenneth D Tuttle and Albert Tversky.
  They identify no employer or workplace and are excluded from verified-
  employer analytics.
- Exact Army rows for Cipriano E Turri, Everett D Tutor and Hiram D Tuttle
  support identity only because the category or chronology cannot sustain a
  pre-OSS occupation claim.
- Thirteen unresolved identities retain explicit archival-review outcomes.
  An Oscar Turner broadcasting lead, an Everett Tutor obituary-aggregator
  lead and a Hiram Tuttle lawyer namesake were rejected as insufficient or
  incompatible evidence.

## Exact batch outcome

- People researched: 23.
- Terminal statuses: 1 `verified_employer_found`; 4
  `occupation_only_found`; 1 `conflicting_sources`; 17
  `requires_archival_review`.
- Identity statuses: 9 `high_confidence`; 1 `conflicting`; 13 `unresolved`.
- Evidence imported: 8 sources, 3 organization inputs, 7 affiliations, 18
  claims, 49 claim-source links, 23 person updates and 23 research attempts.
- Review decisions imported: 7 accepted and 1 conflicting.
- Batch claim confidence: 12 high; 5 medium; 1 conflicting.
- The deterministic evidence bundle SHA-256 is
  `131eac4b75569c94f034a3e8579a23914595800f308e9d24de6edb78f34d6d32`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,269 / 23,936 (63.7909%).
- Verified-affiliation coverage: 1,095 / 23,936 (4.5747%).
- Verified-employer coverage: 489 / 23,936 (2.0429%).
- Archival-review coverage: 13,745 / 23,936 (57.4240%).
- Not started: 8,662 people; in progress: 1,883 people.
- Possible-duplicate groups: 664.
- Conflicts: 522.
- Claim confidence: 1,706 confirmed; 5,103 high; 2,419 medium; 255 low;
  435 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,751 affiliations; 1,253
  organizations; 6,253 sources; 9,659 published, qualified or conflict claims.
- Private projection: 3,777 affiliations; 1,268 organizations; 7,539 sources;
  21,399 unresolved rows and 23,568 archival pull-list rows.
- Citations: 7,539 across 4,185 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- Evidence and review-decision imports are idempotent on repeated import.
- All 147 Python pipeline tests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 602 files with zero diagnostics and generated 25,239 static
  pages.
- All 27 Batch 971 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 96 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,239 HTML files resolve; 52,047 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit checked 12,926 normalized identifiers and 120
  formatted variants across 25,311 output artifacts, inspected 1,421 candidate
  substrings, and found zero unexpected boundary, aggregate or manifest-size
  matches.
- Two consecutive builds reproduced the same 67-asset, 129,991,591-byte public
  manifest at SHA-256
  `4f2c14042587715d3f04d9e3396c92bd707b931b1f08a5f38f3e3697df6d26d7`.
- The reproduced 70-file public tree totals 132,338,745 bytes and has SHA-256
  `9acf8dd244706757713433d85c3698e8999750dc263c1714610dbc32d88e96f1`.
- The reproduced 25,311-file output tree totals 417,837,682 bytes and has
  SHA-256
  `7ed01368e9e78363d99d656cbed34390810a9edface8a5429a04563cd0a060af`.
- The dependency audit reports zero vulnerabilities.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 971 itself is replayable and idempotent.

## Resume point

Continue with PDF page 476, row 24, **George B Tweed**, Box 791, archive
location 230/86/42/03.

## Publication verification

- Immutable content commit:
  `2aebdc7a742253c84781dcfa2c3d101612cdfb97`.
- GitHub Actions Test run `41014679644` and Pages run `41014679691` completed
  successfully.
- The unauthenticated deployed-release verifier matched the 67-asset,
  129,991,591-byte public manifest at SHA-256
  `4f2c14042587715d3f04d9e3396c92bd707b931b1f08a5f38f3e3697df6d26d7`,
  all eight core routes, all 42 source-register pages and all 23 Batch 971
  profile routes to the content commit.
- Public site: <https://therealjameswilson.github.io/before-oss/>.
