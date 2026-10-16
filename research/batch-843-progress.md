# Batch 843 research progress

Date: 2026-10-16 America/New_York

## Scope and source validation

Batch 843 covers the 23 printed personnel rows on NARA index PDF page 411,
rows 24-46, from Mack J. Schaefer through Franklin O. Scheiber. The rows remain
23 immutable source records linked to 23 active person entities. Page 411 was
rendered and visually inspected at 180 dpi before research. The truncated
`Schaffenberge` surname, printed ranks and grades, change from Box 681 to Box
682, and row-46 boundary were confirmed against the image. The next unassigned
boundary is PDF page 412, row 1, Henry Scheiber III.

## Research outcomes

- Institutional and scholarly sources identify **Francis Schehl** at high
  confidence as Franz/Francis W. Schehl. They independently date his Portsmouth
  Priory School Classics-department leadership to 1941-1944 and explicitly
  place his OSS analyst appointment in 1944. The school is published as both
  his immediate pre-OSS affiliation and last civilian employer.
- Contemporary book front matter, a Jabotinsky Institute memorial and an
  American Jewish Archives reference identify **Joseph B. Schechtmann** as
  Joseph B. Schechtman at high confidence. The Research Bureau on Population
  Movements is published as his immediate and last civilian affiliation; the
  Institute of Jewish Affairs remains a separate earlier or overlapping role.
- A Directors Guild of America biography identifies **Franklin J. Schaffner**
  at high confidence and places Navy amphibious service before later OSS work
  in the Far East. Franklin & Marshall College is recorded as student status,
  not an employer.
- The official Entry 210 finding aid identifies **Paul Scheffer** as a
  journalist and points to WN#13481-WN#13482 concerning his OSS employment and
  reports. Deutsche Biographie supports his occupation, freelance work and
  earlier Berliner Tageblatt employment. The broad OSS-file date range overlaps
  the freelance chronology, so no unqualified immediate-employer claim is made.
- A first-person interview, a contemporary Stars and Stripes item and a
  specialized comics reference identify indexed **Kurt P. Schaffenberge** as
  Kurt P. Schaffenberger at high confidence. Binder Studio is published as a
  qualified medium-confidence last civilian employer. His Army-to-OSS pathway
  is probable, with no unit or exact transfer date inferred.
- A family obituary and official University of Wisconsin minutes support a
  probable match for **Hildegarde R. Scheibe**, including Knox School teaching,
  UW-Madison graduate study and OSS translation work. The obituary prints
  middle initial M while the index and university record print R, so the
  identity and associated affiliations remain visibly qualified.
- Edgar Schauber, Edward L. Scheaf, Edward M. Scharf, Max Schatzberg and
  Raymond B. Schantz have accepted identity-only links to private official Army
  crosswalks. Full identifiers and coded occupations remain private. Schantz
  remains separate from the earlier unnumbered Raymond B. Scantz row in a
  visible duplicate group.
- The official Army row associated with Franklin O. Scheiber's protected index
  identifier prints a materially different full name. The alternate identity,
  coded occupation and raw record remain private; the public profile exposes
  only the existence of the conflict and the need for Box 682 review.
- A possible spouse-based lead for Rachel D. Schechtmann was rejected because
  relatives cannot be the principal basis for identification. A modern Erich
  Scheiber namesake and a Tacoma-area Paul Scheffer society-page namesake were
  also rejected.
- LoC completed all 23 bounded searches and produced one candidate, which was
  rejected after item-level OCR review. CIA automated access failed closed and
  is recorded as a source limitation, not negative evidence. NARA Catalog API
  work remains disabled pending safe credential rotation.

The final assigned-cohort identity distribution is ten `high_confidence`, one
`probable`, one `conflicting`, and eleven `unresolved`. Research status is 17
`requires_archival_review`, two `verified_employer_found`, one
`documented_prewar_employer_found`, one `occupation_only_found`, one
`needs_identity_review`, and one `conflicting_sources`. The reviewed evidence
bundle contains 15 source inputs, ten organization inputs, 11 affiliations, 19
claims, 23 person updates, 23 manual staged research attempts, and 38
claim-source links. Import and idempotent replay produced identical counts;
Army and LoC review-decision replays skipped all duplicates. SQLite's
foreign-key check returned no rows and integrity check returned `ok`.

## Updated project coverage

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,366 people (51.6585%).
- Verified-employer coverage: 407 people (1.7002%).
- Verified-affiliation coverage: 895 people (3.7388%).
- Archival-review coverage: 10,831 people (45.2461%).
- Not started: 11,567 people.
- Possible duplicate groups: 558.
- Conflicts: 440 people.
- Claim confidence totals: 1,588 confirmed, 3,837 high, 1,674 medium,
  202 low, 370 conflicting, and two unresolved.
- Citations: 6,375; unique source documents: 3,399.
- Public projection: 23,938 people, 2,799 affiliations, 1,033 organizations,
  5,145 sources, and 7,465 claims.

## Validation

Local release validation passed. Python reports 145/145 passing tests. Astro
checked 477 files with zero errors, warnings or hints and built 25,014 static
pages. The bounded Playwright release suite passed 99/99 checks across Batch
843, core routes, analytics and accessibility at desktop, phone and tablet
viewports. The stratified 200-profile audit passed every check. All internal
links across 25,014 HTML files resolve; 51,286 unique external URLs were
inventoried separately. The public-identifier audit found zero unexpected
boundary matches after checking 12,926 normalized identifiers and 120
formatted variants across 25,086 artifacts. The public manifest covers 67
assets totaling 114,630,416 bytes with SHA-256
`1e5a7d00ffcdb993afb946365945c5d9a8d02a69fad17a34305aa97adf2fcd94`.
Two clean builds produced the identical 25,086-file tree hash
`e7bc2b76ee5243dd6bd2ad8f3f9b886947b2ab2cc933ae271feb4a93e4c6d754`.

## Publication status

Published. GitHub Pages run 38883687680 deployed content commit
`25ab24eda24169852789e80fac7c00c5fab609a1` successfully, and Test run
38883687577 passed. The immutable unauthenticated verifier matched all 67
public assets (114,630,416 bytes), the release manifest, eight core routes, 35
source-register pages, and all 23 directly affected profile URLs. Public URL:
https://therealjameswilson.github.io/before-oss/.
