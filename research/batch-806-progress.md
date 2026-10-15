# Batch 806 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 806 covers PDF page 393, rows 1-23, Thomas R Riley through Walter F
Risdon. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 393 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 393, row 24,
Ove A Rise.

The clipped notes `Record`, `possible`, and `photogra` remain intact. None was
silently expanded or converted into an occupation. Public profiles and
downloads continue to exclude full service numbers and unrelated personal
addresses.

## Research protocol and review

- NARA index context, exact-name OSS searches, employment and occupation
  searches, and obituary, institutional, newspaper, military-history, and
  archival searches were reviewed for every person. NARA Catalog requests
  remained dry-run plans because no API key was available in the local process
  environment.
- A live CIA Reading Room attempt for Janet Rioch failed closed under the
  site's robots policy. A live Library of Congress attempt for Sidney D. Ripley
  exhausted bounded retries after a network error. Neither access failure was
  treated as a negative research result.
- All 23 people now have terminal attempted outcomes: 19 require archival
  review, two have verified employers, one has occupation-only evidence, and
  one has a completed military-assignment outcome.
- Three official Army bulk identity candidates were accepted after exact-name
  and protected-identifier agreement. Coded Army occupation fields were not
  converted into employers.
- No low-confidence lead or modern namesake was published as fact.

## Historical outcomes

- Janet M. Rioch's best-supported immediate pre-OSS affiliation and last
  civilian employer was the Presbyterian Hospital in the City of New York,
  where she was acting director of the pediatric psychiatric clinic. The
  hospital's 1944 annual report says she resigned for federally sponsored
  research in Washington. Because it does not itself name OSS, the transition
  is classified `strongly_date_bounded`, not `explicit_immediate`. Her 1943
  role as a William Alanson White Institute co-founder remains a separate
  professional affiliation, not an employer.
- Smithsonian Institution Archives explicitly documents that S. Dillon Ripley
  was assistant curator of birds at the U.S. National Museum and left to
  volunteer for OSS. This is a confirmed immediate-affiliation and last-civilian-
  employer sequence.
- The CIA Museum confirms Robert H. Riplow's identity, 1939-1945 Army service,
  initial tank-destroyer assignment, and detail to OSS beginning in 1944. The
  Army role is published as a military assignment, not a civilian employer.
- A Washington Post obituary supports a high-confidence Peter Ringland
  identity, two years of student status at St. John's College, and wartime Army
  order-of-battle work. It does not explicitly identify OSS service, so those
  affiliations remain qualified and no employer is inferred.
- A later official presidential-library record supports only a probable
  identity bridge from Tena L. Rips to Tena Lowe Rips. The clipped index note
  `photogra` remains unexpanded, and the later record's address is excluded.
- Official Army bulk records support identity and Army-service claims for
  Andrew Rinko, Norbert J. Rioux, and Raymond J. Ripkowski without supplying
  pre-OSS employers.

## Exact coverage after Batch 806

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,525/23,938 (48.1452%).
- Verified-employer coverage: 374/23,938 (1.5624%).
- Verified-affiliation coverage: 828/23,938 (3.4589%).
- Archival-review coverage: 9,988/23,938 (41.7245%).
- Not started: 12,408.
- Possible duplicate groups: 552; conflicts: 394.
- Claims: 1,423 confirmed; 3,623 high; 1,629 medium; 202 low; 338
  conflicting; two unresolved.
- Citations: 6,124 records representing 3,202 unique source documents.
- Public data: 2,657 published affiliations, 955 organizations, 4,899 public
  sources, and 7,009 published claims.
- Total saved research attempts and plans: 22,393.

## Durable inputs and replay

Evidence, claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page393-riley-risdon-review_batch-806_2026-10-15.json`.
Reviewed Army candidate decisions are stored in
`research/identity_review_decisions_2026-10-15_batch806.csv`. Both import paths
were replayed: review decisions were recognized as duplicates and evidence
object counts remained identical, confirming idempotent outcomes.

Resume new-person research at PDF page 393, row 24, Ove A Rise. Full-index
historical research remains unfinished; 12,408 active people are still
`not_started`.
