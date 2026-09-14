# Batch 521 discovery checkpoint

Run: 2026-09-14 UTC

## Cohort

This checkpoint covers personnel-index PDF page 104 rows 6-16, spanning Box
164 and one linked Box 165 entry at archival location 230/86/29/05:

1. Amando Dalisay
2. James W Dallas
3. John E Dally
4. Miguel S Dalmau
5. Ronald E Dalrymple
6. Robert A Dalton
7. Dennis D Daly
8. Donald D Daly
9. Earle J Daly
10. Edward F Daly

The page was rendered and visually inspected. All eleven printed rows remain
immutable source records. Edward F Daly is represented by two separate rows,
one T-4 entry in Box 165 and one corporal entry in Box 164. Their shared
private identifier supports one person entity but does not erase either source
row. Seven printed private values were used only for controlled identity
review and remain absent from the reviewed evidence bundle and public
projection.

## Source checks

- The CIA Reading Room adapter completed ten bounded exact-name checks with no
  candidates or errors.
- The current Library of Congress adapter completed ten bounded checks. It
  returned seven candidates: one for John E Dally, one for Donald D Daly, and
  five for Edward F Daly. All seven full newspaper pages and official OCR
  contexts were inspected. They concerned a 1917 advertised-letter OCR hit,
  Donald J Daly rather than Donald D Daly, several judges or a trustee with
  different middle initials, or a postwar page with no exact-name context. All
  seven decisions were imported twice from
  `research/loc_review_decisions_2026-09-14_batch521.csv`; the second import
  created no new review decisions.
- The complete 9,200,232-row Army merged file was scanned transiently. Exact
  private-identifier and exact-name matches select John E Dally, Ronald E
  Dalrymple, Robert A Dalton, Dennis D Daly, and Edward F Daly. Five Army rows
  share Robert A Dalton's exact name, but only one shares the indexed private
  identifier. Four Army rows share Edward F Daly's exact name, but only one
  shares the identifier printed in both index rows.
- One exact-name James W Dallas Army row cannot be linked by any indexed field,
  so it remains an explicit unaccepted candidate. The printed value for Miguel
  S Dalmau is not eligible for standard eight-digit Army-file comparison.
  Army non-hits for Amando Dalisay, Miguel S Dalmau, Donald D Daly, and Earle J
  Daly are not negative proof because the file is incomplete and is not a
  comprehensive OSS, officer, Navy, Marine Corps, civilian, or foreign roster.
- NARA's fixed-width technical documentation and occupational code pages were
  rendered and visually checked. Values 992, 736, 732, 022, and 002 map to
  students; chauffeurs and drivers; residual construction occupations; lawyers
  and judges; and actors and actresses. These are statuses or occupations, not
  named employers.
- A contemporary Harvard Crimson article identifies Amando Dalisay as a
  second-year Harvard graduate student in March 1940 and as an organizer of the
  International Club. The Philippine National Academy's official biographical
  directory records Amando M. Dalisay's University of the Philippines B.S.A.
  in 1937 and Harvard economics M.A. in 1942 and Ph.D. in 1946. The rare name,
  Filipino context, graduate status, field, and wartime chronology support a
  probable match, but the index lacks a middle initial or another direct
  identifier. Both institutions are modeled as student affiliations, never as
  employers, and no immediate Harvard-to-OSS transition is inferred.
- A DPAA casualty record concerns a different John Dally with an incompatible
  identifier and is rejected. Targeted exact-name OSS, employment, occupation,
  military, obituary, institutional, newspaper, directory, and archival
  searches produced no defensible employer for the cohort.
- No authenticated NARA Catalog API request was made. The API key remains
  absent from the repository, generated data, logs, and public bundle.

## Saved outcomes

- Amando Dalisay: probable identity; documented University of the Philippines
  and Harvard student affiliations; no employer; Box 164 identity review
  required.
- John E Dally: confirmed identity; enlisted Army personnel; student status at
  Army entry; no institution or employer named.
- Ronald E Dalrymple: confirmed identity; enlisted Army personnel; qualified
  semiskilled driver group at Army entry; no employer.
- Robert A Dalton: confirmed identity; enlisted Army personnel; qualified
  semiskilled residual construction occupation at Army entry; no employer.
- Dennis D Daly: confirmed identity; enlisted Army personnel; qualified
  lawyers-and-judges occupation group at Army entry; no firm, court, practice,
  or employer.
- Edward F Daly: confirmed identity across two preserved index rows; enlisted
  Army personnel; actor occupation at Army entry; no employer or production.
- James W Dallas and Donald D Daly: ambiguous identities requiring Box 164
  review.
- Miguel S Dalmau and Earle J Daly: unresolved after the completed protocol and
  requiring Box 164 review.

All ten profiles have terminal saved outcomes and explicit archival next
actions. The reviewed bundle contains six sources, two organization upserts,
seven affiliations, thirteen claims, thirty-six claim-source links, ten person
updates, and ten synthesized terminal research outcomes. Repeat import leaves
all durable counts unchanged.

## Coverage after import

- Index coverage: 23,978 / 23,978 rows linked (100.0000%).
- Active person entities: 23,940.
- Research-attempt coverage: 4,977 / 23,940 (20.7895%).
- Verified-affiliation coverage: 566 / 23,940 (2.3642%).
- Verified-employer coverage: 252 / 23,940 (1.0526%).
- Archival-review coverage: 4,932 / 23,940 (20.6015%).
- Not started: 18,963 / 23,940 (79.2105%).

## Resume

Research resumes with personnel-index PDF page 104 row 17, George R Daly, in
Box 165. Do not infer an employer from an Army occupation code, student
affiliation, namesake, or a source describing service after the person had
already joined OSS.
