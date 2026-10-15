# Batch 804 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 804 covers PDF page 392, rows 1-23, Carrie E Rider through Edward L
Rigby. All 23 printed rows remain preserved as immutable source records and map
to 23 active person entities. Page 392 was inspected against a 300 dpi render
before research. The next unresearched boundary is PDF page 392, row 24, Ivan B
Rigby.

The Box 644-to-645 transition and clipped notes `Record`, `folder is`, and
`photogra` remain intact. None was silently expanded or converted to an
occupation. Public profiles and downloads continue to mask protected
identifiers.

## Research protocol and review

- NARA index context, exact-name OSS searches, source-specific CIA Reading Room
  checks, Library of Congress checks, employment and occupation searches, and
  obituary, institutional, newspaper, military-history, and archival searches
  were reviewed for every person. NARA Catalog requests remained planned
  because no API key was present in the process environment.
- All 23 people now have terminal outcomes: one `verified_employer_found`, two
  `documented_prewar_employer_found`, two `occupation_only_found`, one
  `conflicting_sources`, and 17 `requires_archival_review`.
- Three official Army bulk identity candidates were accepted after exact-name
  and nonshared protected-identifier agreement. Coded Army fields were not
  converted into employers.
- Alfred Riefman remains separate from the previously researched Alfred Reifman.
  The rows share a rank and protected identifier but differ in indexed surname
  and archival box, so the possible duplicate is public and conflicting until
  Boxes 638 and 644 can be compared.
- No low-confidence lead was published as fact. Common and incomplete names
  remain unresolved with explicit Box 644 or 645 review guidance.

## Historical outcomes

- An official 1925 Supreme Court report identifies a Harry S. Ridgely as a
  Department of Justice attorney. The site publishes this only as a probable,
  medium-confidence documented-prewar match, not as the immediate pre-OSS role.
- A biographical account says Manek Riegelhaupt worked in New York as a busboy,
  cashier, and diamond cutter. The employers are unnamed and the temporal
  relationship to the indexed file remains uncertain.
- A rare-name chain supported by an obituary and an official FBI record supports
  a high-confidence Gertrude Rient identity. Her documented U.S. Embassy Moscow
  role as a Czech linguist is qualified and is not labeled immediate pre-OSS.
- Institutional sources identify Felix Riesenberg Jr. as a writer in San
  Francisco in 1939. Writer remains an occupation; no employer is invented.
- An official CIA study identifies Curt Riess as a freelance writer and states
  that his 1944 OSS application was disapproved. The index entry is not treated
  as evidence that he served in OSS.
- Official Army bulk data supports high-confidence identities for Bernard J
  Riedeman, Herman J Rief, and Elwood C Rieser, but no employer for any of them.

## Exact coverage after Batch 804

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,479/23,938 (47.9530%).
- Verified-employer coverage: 372/23,938 (1.5540%).
- Verified-affiliation coverage: 824/23,938 (3.4422%).
- Archival-review coverage: 9,942/23,938 (41.5323%).
- Not started: 12,454.
- Possible duplicate groups: 552; conflicts: 394.
- Claims: 1,418 confirmed; 3,606 high; 1,626 medium; 202 low; 338
  conflicting; two unresolved.
- Citations: 6,112 records representing 3,192 unique source documents.
- Public data: 2,651 published affiliations, 952 organizations, 4,887 public
  sources, and 6,984 published claims.
- Total saved research attempts and plans: 22,251.

## Durable inputs and replay

Evidence, claims, affiliations, person updates, rejection reasons, and terminal
attempts are stored in
`research/evidence-page392-rider-rigby-review_batch-804_2026-10-15.json`.
Reviewed duplicate and Army candidate decisions are stored in
`research/identity_review_decisions_2026-10-15_batch804.csv`. Both import paths
were replayed: review decisions were recognized as duplicates and evidence
object counts remained identical, confirming idempotent outcomes.

Resume new-person research at PDF page 392, row 24, Ivan B Rigby. Full-index
historical research remains unfinished; 12,454 active people are still
`not_started`.
