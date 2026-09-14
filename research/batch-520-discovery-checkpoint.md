# Batch 520 discovery checkpoint

Run: 2026-09-14 UTC

## Cohort

This checkpoint covers personnel-index PDF page 103 rows 42-46 and page 104
rows 1-5, all in Box 164 at archival location 230/86/29/05:

1. John P Dalberg
2. Hope Dale
3. Ernest D'Alessandro
4. Giuseppe D'Alessandro
5. Donald D Daley
6. John F Daley
7. Mary Daley
8. John H Dalgarn
9. James B Dalgliesh
10. Lucille Dalious

Both pages were rendered and visually inspected. All ten printed rows remain
immutable source records. Seven printed private values were used only for
controlled identity review and remain absent from the reviewed evidence
bundle and public projection.

## Source checks

- The CIA Reading Room adapter completed ten bounded exact-name checks with no
  candidates or errors.
- The current Library of Congress adapter completed ten bounded checks. It
  returned five candidates for John F Daley and one for Mary Daley. All six
  newspaper pages and official OCR contexts were inspected. The John results
  concerned people with middle initials P, L, M, C, or D, much earlier people,
  or OCR occurrences of the word daily. The Mary item identified a 1941
  bridesmaid but supplied no middle identifier, occupation, OSS context, or
  Box 164 bridge. All six decisions were imported twice from
  `research/loc_review_decisions_2026-09-14_batch520.csv`; the second import
  created no new review decisions.
- The complete 9,200,232-row Army merged file was scanned transiently. Exact
  private-identifier matches select John P Dalberg, Ernest D'Alessandro,
  Giuseppe D'Alessandro, and James B Dalgliesh. The file records Ernesto for
  Ernest, Guiseppe for Giuseppe, and Delgliesh for Dalgliesh; those differences
  are exposed as variants rather than silently corrected.
- Ten exact-name John F Daley Army rows cannot be distinguished by any indexed
  field, so none is accepted. The printed value for John H Dalgarn has no exact
  Army-file match. The incomplete Army file is not a comprehensive OSS,
  officer, Navy, Marine Corps, WAC, civilian, or foreign roster, so non-hits
  are not negative proof.
- One exact-name Lucille Dalious Army row records Women's Army Corps auxiliary
  grade, Texas residence, Army entry on 15 May 1943, and civilian-occupation
  value 137. The rare name, Dallas context, compatible education and chronology
  support high-confidence identity, but the lack of a shared public identifier
  keeps the match below confirmed.
- NARA's fixed-width technical documentation and occupational classification
  pages were rendered and visually checked. Values 455, 657, 072, and 137 map
  to a skilled petroleum-refining group, a semiskilled rubber-goods production
  group, retail managers, and stenographers and typists. These are occupations,
  not employers.
- Gamma Phi Beta's December 1939 institutional magazine was downloaded,
  searched, rendered, and visually checked. Under Alpha Xi at
  Southern-Methodist University, it lists Lucille Dalious of Dallas among the
  chapter's pledges. The relationship is modeled as student affiliation, not
  university employment.
- The University of North Texas Libraries' high-resolution scan of the 1939
  Dallas City Directory was visually checked. It independently places Lucille
  Dalious in Dallas; the street address is neither retained in claims nor
  exposed in public output.
- A 377th Infantry roster and veteran burial record share John H Dalgarn's
  exact name, but neither supplies the private identifier, direct OSS context,
  Box 164 bridge, or an Army-to-OSS sequence. The candidate remains explicit
  and unaccepted.
- Targeted exact-name OSS, employment, occupation, military, obituary,
  institutional, newspaper, directory, and archival searches produced no
  defensible pre-OSS employer for the remaining people.
- No authenticated NARA Catalog API request was made. The API key remains
  absent from the repository, generated data, logs, and public bundle.

## Saved outcomes

- John P Dalberg: confirmed identity; enlisted Army personnel; qualified
  skilled petroleum-refining occupation at Army entry; no employer.
- Ernest D'Alessandro: confirmed identity; enlisted Army personnel; preserved
  Ernesto variant; qualified semiskilled rubber-goods production occupation at
  Army entry; no employer.
- Giuseppe D'Alessandro: confirmed identity; enlisted Army personnel;
  preserved Guiseppe variant; qualified retail-manager occupation at Army
  entry; no employer.
- James B Dalgliesh: confirmed identity; enlisted Army personnel; preserved
  Delgliesh variant; qualified retail-manager occupation at Army entry; no
  employer.
- Lucille Dalious: high-confidence identity; enlisted Women's Army Corps
  personnel; documented 1939 Southern Methodist University student
  affiliation; qualified stenographer-or-typist occupation at Army entry; no
  employer.
- Hope Dale, John F Daley, and John H Dalgarn: ambiguous identities requiring
  Box 164 review.
- Donald D Daley and Mary Daley: unresolved after the completed protocol and
  requiring Box 164 review.

All ten profiles have terminal saved outcomes and explicit Box 164 archival
next actions. The reviewed bundle contains six sources, one organization,
six affiliations, eleven claims, thirty-six claim-source links, ten person
updates, and ten synthesized terminal research outcomes. Repeat import leaves
all durable counts unchanged.

## Coverage after import

- Index coverage: 23,978 / 23,978 rows linked (100.0000%).
- Active person entities: 23,940.
- Research-attempt coverage: 4,967 / 23,940 (20.7477%).
- Verified-affiliation coverage: 566 / 23,940 (2.3642%).
- Verified-employer coverage: 252 / 23,940 (1.0526%).
- Archival-review coverage: 4,922 / 23,940 (20.5597%).
- Not started: 18,973 / 23,940 (79.2523%).

## Resume

Research resumes with personnel-index PDF page 104 row 6, Amando Dalisay, in
Box 164. Do not infer an employer from an Army occupation code, student
affiliation, namesake, directory residence, or source describing service after
the person had already joined OSS.
