# Batch 519 discovery checkpoint

Run: 2026-09-14 UTC

## Cohort

This checkpoint covers personnel-index PDF page 103 rows 32-41, all in Box
164 at archival location 230/86/29/05:

1. Rose Daigle
2. Alfred P Daignault
3. George E Dail Jr.
4. Lowell R Dailey
5. Pat H Dailey
6. James Daily
7. Harvey J Dain
8. John W Dain
9. Charles Daish
10. Edward J Dajewski

The page was visually inspected. All ten printed rows remain immutable source
records. Four printed private values were used only for controlled identity
comparison and remain absent from the reviewed evidence bundle and public
projection.

## Source checks

- The CIA Reading Room adapter completed ten bounded exact-name checks with no
  candidates or errors.
- The current Library of Congress adapter completed ten bounded checks. It
  returned three candidates: two for James Daily and one for John W Dain. Each
  full newspaper page and its OCR context was inspected. The 1940 James Daily
  item described a common-name gasoline-station attendant with no OSS or Box
  bridge; the other James Daily item dated from 1846; the John W Dain hit was
  an OCR line-break artifact for John Adams. All three decisions were imported
  twice from `research/loc_review_decisions_2026-09-14_batch519.csv`; the
  second import made no new decisions or state changes.
- The complete 9,200,232-row Army merged file was scanned transiently. Exact
  private-identifier and exact-name matches were found for Alfred P Daignault
  and Pat H Dailey. The printed values for Harvey J Dain and Edward J Dajewski
  did not produce a hit; this incomplete Army file is not a comprehensive OSS,
  officer, Navy, Marine Corps, civilian or foreign roster, so absence is not
  negative proof.
- NARA's fixed-width technical documentation and the relevant code-list page
  were visually checked. Alfred's Army-entry value maps to `Occupations in
  manufacture of automobiles, n.e.c.` and Pat's to `Machinists`. Neither code
  identifies an employer or workplace.
- The OSS Assessment Staff's own 1948 publication independently lists Alfred
  P. Daignault, B.S., as a corporal at five assessment stations. Its
  instructions say parenthetical institutions are predecessor institutions;
  Daignault has no parenthetical entry. That silence is not treated as proof
  that he lacked an employer.
- Lawrence C. Soley's scholarly history places Lieutenant George Dail in the
  OSS Morale Operations unit in China and describes administrative duties.
  The uncommon name, lieutenant grade and direct OSS context support a
  high-confidence match to the indexed 2nd Lt. George E. Dail Jr. The source
  omits the middle initial and suffix, so the identity is not promoted to
  confirmed. A different George W. Dail of the 117th Infantry was rejected by
  middle initial and incompatible European combat context.
- Targeted exact-name OSS, employment, occupation, military, obituary,
  institutional, newspaper and archival searches found no defensible
  pre-OSS employer for the remaining people. Psychiatrist Harvey J. Dain and
  other postwar namesakes were not assigned without an OSS or Box 164 bridge.
- No authenticated NARA Catalog API request was made. The API key remains
  absent from the repository, generated data, logs and public bundle.

## Saved outcomes

- Alfred P Daignault: confirmed identity; enlisted Army personnel; qualified
  residual automobile-manufacturing occupation at Army entry; no employer.
- Pat H Dailey: confirmed identity; enlisted Army personnel; qualified
  machinist occupation at Army entry; no employer.
- George E Dail Jr.: high-confidence identity; commissioned Army officer;
  wartime OSS China context documented, but deliberately excluded from
  pre-OSS affiliation fields.
- Harvey J Dain: indexed commissioned Army classification retained; identity
  remains unresolved; psychiatrist namesake rejected.
- Rose Daigle, Lowell R Dailey, James Daily, John W Dain, Charles Daish and
  Edward J Dajewski: unresolved after the completed protocol.

All ten profiles have terminal saved outcomes and explicit Box 164 archival
next actions. The reviewed bundle contains six sources, no organization
upserts, two affiliations, five claims, fifteen claim-source links, ten person
updates and ten synthesized terminal research outcomes. Repeat import leaves
all durable counts unchanged.

## Coverage after import

- Index coverage: 23,978 / 23,978 rows linked (100.0000%).
- Active person entities: 23,940.
- Research-attempt coverage: 4,957 / 23,940 (20.7059%).
- Verified-affiliation coverage: 565 / 23,940 (2.3601%).
- Verified-employer coverage: 252 / 23,940 (1.0526%).
- Archival-review coverage: 4,912 / 23,940 (20.5180%).
- Not started: 18,983 / 23,940 (79.2941%).

## Resume

Research resumes with personnel-index PDF page 103 row 42, John P Dalberg, in
Box 164. Do not infer an employer from an Army occupation code, a namesake, or
a source describing service after the person had already joined OSS.
