# Batch 851 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 851 covers the 23 printed personnel rows on NARA index PDF page 415,
rows 24-46, from Ann M Schuetz through Bernard G Schulz. All 23 immutable
source rows remain preserved and linked to 23 separate active person entities.
The rendered page was visually reviewed at 180 dpi; names, ranks or grades,
serial-number columns, Boxes 688-689 and archive location 230/86/40/03 align
with the printed table. Full service identifiers remain private. The next
unassigned boundary is PDF page 416, row 1, Ernest C Schulz.

## Research outcomes

- An official congressional Pearl Harbor investigation transcript directly
  identifies **Robert E Schukraft** as the officer in charge of radio
  intercepts for the Signal Intelligence Service, War Department, before and
  on December 7, 1941. An official National Security Agency history independently
  corroborates his exact identity through the protected officer identifier.
  This is published as a `documented_prewar` military assignment, not as an
  immediate OSS predecessor or civilian employer; Box 689 is still needed to
  establish the later sequence into OSS.
- Official Army data supports high-confidence identity decisions for **John G
  Schuetz**, **Preston R Schuler**, **Ira J Schulman**, the first of the two
  separately preserved **Curtis C Schultz** rows, **Robert A Schultz** and
  **William J Schultz**. Army occupation codes remain private and were not
  converted into employer, rank or affiliation claims.
- The second Curtis C Schultz row remains unresolved because its protected
  identifier points to the materially conflicting Army name Kenneth C Nelson.
  The printed T/4 and T/5 rows remain separate and visibly linked in one
  possible-duplicate group pending review of both personnel files.
- **Audrey B Schultz** and **Audrey B Schulz** likewise remain separate person
  entities in one visible spelling-variant group. A name variant alone is
  insufficient for a merge; both Box 689 files require comparison.
- Chronologically incompatible or otherwise unsupported namesakes for
  Ellsworth F Schug, Eric T Schuler, Walter F. L. Schulte and other batch
  members were retained only as rejected research leads, never as published
  employment facts.
- **Seymour W Schulberg** and **Stuart H Schulberg** retain their previously
  verified employer outcomes. The remaining unresolved people received
  terminal archival-review outcomes rather than invented employers.
- CIA automated access failed closed under the source's robots policy. A
  Library of Congress request timed out after bounded retries and remains an
  access failure rather than a negative historical result. Authenticated NARA
  Catalog research remains disabled pending safe credential rotation.

The batch distribution is one `confirmed`, eight `high_confidence` and 14
`unresolved` identities. Research status is one `completed`, two
`verified_employer_found` and 20 `requires_archival_review`. The new evidence
bundle contains four source inputs, one organization, one affiliation, eight
claims, 21 person updates, 21 manual staged-protocol attempts and 16
claim-source links. Six Army candidates were accepted and one was rejected.
Evidence and decision replays were idempotent. SQLite's foreign-key check
returned no rows and its integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,937; stored entities: 23,941, including four
  superseded entities retained for auditability.
- Research-attempt coverage: 12,545 people (52.4084%).
- Verified-employer coverage: 412 people (1.7212%).
- Verified-affiliation coverage: 909 people (3.7975%).
- Archival-review coverage: 11,010 people (45.9957%).
- Not started: 11,387 people.
- Possible duplicate groups: 564.
- Conflicts: 443 people.
- Claim confidence totals: 1,596 confirmed, 3,933 high, 1,686 medium,
  202 low, 373 conflicting and two unresolved.
- Citations: 6,432; unique source documents: 3,444.
- Public projection: 23,937 people, 2,826 affiliations, 1,048 organizations,
  5,202 sources and 7,584 claims.

## Validation

Local release validation passed. Python reports 145/145 tests and 81 subtests
passing. Astro checked 485 files with zero errors, warnings or hints and built
25,028 static pages. The bounded Playwright release suite passed 87/87 checks
across Batch 851, core routes, analytics and accessibility at desktop, phone
and tablet viewports. The stratified 200-profile audit passed every check. All
internal links across 25,028 HTML files resolve; 51,331 unique external URLs
were inventoried separately. The public-identifier audit found zero unexpected
boundary matches after checking 12,926 normalized identifiers and 120 formatted
variants across 25,100 built artifacts. The public manifest covers 67 assets
totaling 115,374,097 bytes with SHA-256
`fb812ebe3c22189305708ae7a1b3479acbb55530753893d21b1ded1d448947c9`.
Two production builds produced the identical 25,100-file tree hash
`11ce470a3aa7047704b7d3d0e470e6f96f810fe3a750ed6a6964c2306369e719`.

## Publication status

The reviewed Batch 851 release is ready for publication. This section will be
updated with the immutable content commit, GitHub Actions run identifiers and
unauthenticated live-verification result after GitHub Pages deploys it.
