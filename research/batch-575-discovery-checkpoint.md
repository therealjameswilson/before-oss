# Batch 575 discovery checkpoint

Date: 2026-09-19 UTC

## Cohort and source preservation

Nine previously unresearched index people: PDF page 115 rows 43-46 and page
116 rows 2-6, John B Deull through Hector F DeVega. Harold C Deutsch at page
116 row 1 was already researched and was deliberately excluded. Both complete
pages were rendered at 180 dpi and visually checked. All ten printed rows
remain separate in the immutable source table; the nine new outcomes retain
Box 183 and archive location `230/86/30/01`. Protected service identifiers
appear only in the private database, not in this evidence bundle or public
downloads.

## Bounded source protocol

- Nine completed CIA Reading Room and nine completed Library of Congress
  searches were persisted. CIA supplied no candidates. The LoC adapter
  surfaced one 1919 newspaper-page discovery lead for William C Deutsch; its
  page-level hit has no inspected identity or employer bridge and was rejected
  through `loc_review_decisions_2026-09-19_batch575.csv`.
- Exact-name OSS, occupation, employer, obituary, institutional, newspaper,
  directory, and archival searches were reviewed for all nine people. The
  visually checked NARA index provides the official personnel-file context.
  An official unrestricted Army bulk-file crosswalk supplied private
  identifier comparisons for five of the nine; the file was scanned in an
  earlier bounded operation, not downloaded or queried through the Catalog
  API for this batch. No authenticated Catalog API request was made.
- William C Deutsch agrees with an official Army entry on full name and a
  unique protected identifier. Hector F DeVega agrees on protected identifier
  and all name elements; `De Vega` differs only in surname spacing. Both are
  high-confidence identity matches, not employer findings. Francis A
  Devautor has a protected-identifier lead to a differently spelled Army
  surname, retained as ambiguous. The two Deull index rows share a protected
  identifier and `see also` notes; the Army entry names John, not Sol. Their
  separate entities remain unmerged pending Box 183 comparison.
- A reviewed [Daily Voice obituary](https://dailyvoice.com/article/catherine-devaney-wallace-87-longtime-fairfield-resident/)
  may identify indexed Catherine DeVaney as Catherine Devaney Wallace and
  describes OSS recruitment from Rhode Island College. The index and article
  lack a second person-specific bridge, so this remains a qualified probable
  identity. The school was a student affiliation, not an employer. Two jobs
  named in the obituary have no reliable pre-OSS dates; neither was assigned
  as a previous employer. A 1958 college student of the same name was not
  conflated with the wartime person.
- Edna Deut, Dorothea J Deuth, and Janet M Deutsch have no accepted external
  identity or employer match. A Janet M Deutsch obituary for someone born in
  1941 is an incompatible namesake, not wartime employment evidence.

## Saved outcomes and QA

The reviewed bundle has three source records, twelve claims, twenty-one
claim-source links, nine person updates, and nine manual review attempts; it
adds no employer or affiliation. All nine receive terminal
`requires_archival_review` status and a specific Box 183 next action. The
public pages use the exact unresolved-employer wording, keep the Deull pair
separate, and cite the qualified Catherine and high-confidence Army identity
claims. The NARA pull list remains grouped by location and box.

Current local SQLite coverage after import and export:

- Index coverage: 23,978 / 23,978 source rows linked (100%).
- Research-attempt coverage: 5,514 / 23,940 active people (23.0326%).
- Verified-affiliation coverage: 597 / 23,940 (2.4937%).
- Verified-employer coverage: 261 / 23,940 (1.0902%).
- Archival-review disposition coverage: 5,469 / 23,940 (22.8446%).
- Remaining active `not_started`: 18,426; possible-duplicate groups: 256.
- Private database: 10,005 durable attempts, 4,703 claims, 2,179
  affiliations, 687 organizations, 4,864 citation records, and 2,222 unique
  source documents. Confidence: 1,307 confirmed, 1,731 high, 1,353 medium,
  183 low, and 129 conflicting claims.
- Public projection: 2,163 affiliations, 673 organizations, 3,673 sources,
  and 4,516 claims. The oil-company category remains seven documented people
  employed by nine historically named oil companies; this batch adds none.

`validate-ingest` passed all extraction, page, and SQLite checks; the
200-profile structural audit passed all seven checks. All 97 Python unittest
cases passed. The site built 24,621 direct HTML pages. The bounded release
suite passed 69/69 desktop, phone, and tablet checks, including 27 axe
accessibility checks; all internal links resolve. The local public-manifest
guard verified 67 assets (95,955,642 bytes) at SHA-256
`8cd0c06d7b96538b7c8680e489c6379bca0b64df9cfe0dd8a56e30b8af03189c`.
The full historical Playwright suite exceeds the local test-runner's Node
heap during test discovery; the bounded release suite runs the latest batch
and core routes without that failure. No new Pages deployment is asserted
until CI and live verification succeed.

Resume with the next sequential index cohort at PDF page 116 row 7. Before
adding claims, visually inspect its page context and run bounded official,
exact-name, employment, and archival checks. Do not convert Army occupation
codes into employer claims or merge the Deull rows without file-level evidence.
