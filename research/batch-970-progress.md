# Batch 970 research progress

Date: 2026-10-30

Scope: NARA OSS personnel index PDF page 475, rows 24-46 (Joseph E Turcotte
through Mildred M Turner)

Boxes: 365 and 789-790

Archive locations: 230/86/33/06 and 230/86/42/03

## Extraction and identity safeguards

- Visually audited index page 475 at 200 dpi and preserved all 23 researched
  rows as 23 separate people.
- Accepted eleven Army identity bridges. The exact protected identifier for
  August A Turlano connects to the official Army spelling August A Iurlano;
  both spellings remain visible and the records were not silently rewritten.
- Carl W Turley's 1946 Army-entry row and Grady V Turley's unusable historical
  category support identity only. Neither row is projected backward into an
  occupation or employer claim.
- Protected identifiers were used only for private identity resolution. No
  full identifier, API credential, live API response or raw Army row appears
  in the evidence bundle, public data or downloads. No authenticated NARA
  Catalog API request was used.

## Reviewed outcomes

- Nine accepted Army records publish qualified, dated occupation or student
  categories. They identify no employer or workplace and are excluded from
  verified-employer analytics. John L Turner's 1945 Army-entry student category
  is explicitly marked temporally uncertain.
- Contemporary *American Foreign Service Journal* advertisements identify
  Colonel Campbell Turner with Turner's Diplomatic School in May 1938 and as
  its director in February 1942. Because neither source identifies OSS service
  or Box 789, this remains a probable identity and qualified professional
  affiliation, not a settled employment or immediate-pre-OSS claim.
- The existing organization record for Mr. Turner's Diplomatic School was
  normalized to the contemporary name Turner's Diplomatic School; its earlier
  Fisher Howe affiliation remains intact and no modern successor was assigned.
- A Ritchie Boys roster lead for Leonard S Turkowski was not admitted because
  the accessible result supplied neither inspectable evidence nor a second
  person-specific identifier. A Utah namesake for Marden S Turner was rejected
  because its chronology conflicts with the protected-identifier-linked Army
  record.
- Eleven unresolved identities retain explicit archival-review outcomes. This
  batch establishes no new named employer.

## Exact batch outcome

- People researched: 23.
- Terminal statuses: 9 `occupation_only_found`; 14
  `requires_archival_review`.
- Identity statuses: 11 `high_confidence`; 1 `probable`; 11 `unresolved`.
- Evidence imported: 6 sources, 1 reused organization input, 10 affiliations,
  22 claims, 65 claim-source links, 23 person updates and 23 research attempts.
- Review decisions imported: 11 accepted.
- Batch claim confidence: 11 high; 11 medium.
- The deterministic evidence bundle SHA-256 is
  `1bc6bc13d3036e33da53da9cd3153122e998db3f3fafd776d390cf8bb3d64c29`.

## Exact post-import coverage

- Index coverage: 23,978 / 23,978 linked rows (100.0000%).
- Active people: 23,936.
- Research-attempt coverage: 15,246 / 23,936 (63.6949%).
- Verified-affiliation coverage: 1,094 / 23,936 (4.5705%).
- Verified-employer coverage: 488 / 23,936 (2.0388%).
- Archival-review coverage: 13,722 / 23,936 (57.3279%).
- Not started: 8,685 people; in progress: 1,883 people.
- Possible-duplicate groups: 664.
- Conflicts: 521.
- Claim confidence: 1,706 confirmed; 5,091 high; 2,414 medium; 255 low;
  434 conflicting; 2 unresolved.
- Public projection: 23,936 profiles; 3,744 affiliations; 1,251
  organizations; 6,245 sources; 9,641 published, qualified or conflict claims.
- Private projection: 3,770 affiliations; 1,266 organizations; 7,531 sources;
  21,404 unresolved rows and 23,569 archival pull-list rows.
- Citations: 7,531 across 4,180 unique source documents.

## Verification

- SQLite integrity and foreign-key checks passed after the durable import.
- Evidence and review-decision imports are idempotent on repeated import.
- All 147 Python pipeline tests passed.
- The 200-profile stratified audit passed every check.
- Astro checked 601 files with zero diagnostics and generated 25,237 static
  pages.
- All 24 Batch 970 browser checks passed across desktop, phone and tablet.
- The bounded release suite passed all 93 browser and accessibility checks,
  including 30 axe scans with no serious or critical violations.
- All internal links across 25,237 HTML files resolve; 52,042 unique external
  URLs were inventoried for the separate live check.
- The public identifier audit checked 12,926 normalized identifiers and 120
  formatted variants across 25,309 output artifacts, inspected 1,418 candidate
  substrings, and found zero unexpected boundary, aggregate or manifest-size
  matches.
- Two consecutive builds reproduced the same 67-asset, 129,858,075-byte public
  manifest at SHA-256
  `06bb20ef155a3338304a9e904445f0367c36120a18a346d18c07af95b7a1be38`.
- The reproduced 70-file public tree totals 132,205,234 bytes and has SHA-256
  `5877da6e7eee688813342d9d315a7febc18a41911bed8a324ee3a696bab37f6e`.
- The reproduced 25,309-file output tree totals 417,614,147 bytes and has
  SHA-256
  `a50f1139835122bf0d31bd664e72d9eaffb340b60b3df364451e0521b017b013`.
- The dependency audit reports zero vulnerabilities.
- The known older replay gap disclosed in Batch 959 remains open: 473
  pre-Batch-959 person-status changes are not yet represented in durable replay
  inputs. Batch 970 itself is replayable and idempotent.

## Resume point

Continue with PDF page 476, row 1, **Olive J Turner**, Box 790, archive
location 230/86/42/03.

## Publication verification

- Immutable content commit:
  `3e0bb36b12da7a2e92921411c754bd2b0b849e3f`.
- GitHub Actions Test run `41009050588` and Pages run `41009050610` completed
  successfully.
- The unauthenticated deployed-release verifier matched the 67-asset,
  129,858,075-byte public manifest at SHA-256
  `06bb20ef155a3338304a9e904445f0367c36120a18a346d18c07af95b7a1be38`,
  all eight core routes, all 42 source-register pages and all 23 Batch 970
  profile routes to the content commit.
- Public site: <https://therealjameswilson.github.io/before-oss/>.
