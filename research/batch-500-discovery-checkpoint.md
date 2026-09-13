# Batch 500 discovery checkpoint

2026-09-13 UTC. This checkpoint covers personnel-index PDF page 99 rows
26-35, Paul L Crosby through Paul W Crouch, all in Box 156 at archival
location 230/86/29/04. The page was rendered at 180 dpi and every extracted
field was visually checked. Literal private identifiers are omitted.

## Cohort and disposition

| PDF row | Source record | Person entity | Indexed name | Disposition |
|---:|---|---|---|---|
| 99:26 | 5c55dab0-7a35-5692-94af-996471372256 | 62a6316b-a612-5d6e-baa6-d4ee8673673a | Paul L Crosby | Confirmed enlisted Army identity; qualified warehousing or material-handling occupation, no named employer |
| 99:27 | 7487084b-680b-54fc-b842-15a4e84238d2 | d29d09eb-caf5-56bb-98e3-383f542ee39e | Richard Crosby | Unresolved; six-digit value preserved literally and two different-identifier Army namesakes rejected |
| 99:28 | 58291f47-faf6-5e6e-b523-55f0feeb6eae | 44229cf5-f9c6-5547-a640-c999cc95ba33 | Vernon R Crosby | Confirmed enlisted Army identity; qualified railroad-clerk occupation, no named railroad or employer |
| 99:29 | 9c158ae3-b745-50a5-8c27-762418808de3 | e984ea64-f5cc-5691-902d-8d1ac1672d4b | Allan B Cross | Confirmed Enlisted Reserve Corps identity; qualified radio-and-phonograph-manufacturing occupation; impossible birth-year code retained as a source anomaly |
| 99:30 | d94b9c5c-f0e3-5821-85c8-824e9e7d106c | 774bcf91-44a4-58a6-9e51-0a5bb687a683 | J A Cross | Unresolved initials-only identity; six-digit value not padded; five newspaper token matches rejected |
| 99:31 | 21658f8c-6887-5e75-b89b-bf59bbc01227 | a89936c7-8775-53f2-b0fb-b0c6d17f960d | James E Cross | Ambiguous; sixteen Army namesakes and five newspaper namesakes rejected without an identifier bridge |
| 99:32 | 0dd1040e-e1af-52ac-ba4b-21b5c5636a0d | f1b41fee-b483-5aa2-bcc1-8237c625cab3 | Arthur W Crossley | Ambiguous; W-prefixed value preserved literally; a different-identifier exact-name Army occupation candidate retained privately at low confidence |
| 99:33 | b899a988-81b4-5900-8719-b3656df72afc | 5bf50f1c-5a7b-5310-83a8-a38baed557b1 | Phyllis R Croswell | Unresolved; no reliable identity or pre-OSS affiliation bridge found online |
| 99:34 | d99f766c-cfbf-5455-b1ad-5faf471afd7e | 262bac81-d2be-5b79-8012-54eceb89ec80 | Gregg E Crouch | High-confidence match to Gregg Elwyn Crouch; Washta High School, Air Corps, OSS, and a qualified pre-service trade category documented; one-character identifier conflict retained |
| 99:35 | 7fbd8fc4-7a74-5182-bfa8-4ebca301caaa | 1af8322e-3d2b-5657-a6bb-582901396464 | Paul W Crouch | Unresolved; no reliable identity or pre-OSS affiliation bridge found online |

## Army merged-file adjudication

The complete 9,200,232-record Army Serial Number Merged File was scanned from
the official fixed-width data. Four printed values meet the documented strict
eight-digit Army-identifier pattern.

- Paul L Crosby, Vernon R Crosby, and Allan B Cross each have one exact-name,
  exact-identifier row. They entered as enlisted Army personnel in 1943, 1942,
  and 1942 respectively. Their occupation codes are published only as
  qualified pre-service categories.
- Gregg E Crouch's exact printed index identifier resolves to an Army row for
  a different name. A separate exact-name row differs by one identifier
  character and matches 1925 birth year, Iowa residence, and Air Corps branch.
  Neither record was silently overwritten or merged.
- Richard Crosby and James E Cross have two and sixteen exact-name Army rows,
  respectively, but no identifier bridge. Arthur W Crossley has one exact-name
  row with a different identifier; its tool-sharpener category remains a
  low-confidence private candidate. J A Cross has no exact-name Army row.

The official occupation code list was rendered and visually checked on
physical pages 171, 174, and 175. It defines code 111 as railroad clerks not
elsewhere classified, 480 as tinsmiths, coppersmiths, and sheet-metal workers,
584 as tool sharpeners and dressers, 699 as semiskilled work in manufacture of
radios and phonographs, and 788 as warehousing, storekeeping, material handling,
loading, unloading, and related work. No code is treated as a named employer.

Allan Cross's exact-identifier Army row carries a 1932 birth-year code despite
a 1942 entry date. That impossible value is documented as a source anomaly and
is not used for identity resolution.

## Gregg Elwyn Crouch

A Boothby Funeral Home obituary explicitly says that Gregg Elwyn Crouch was
born in Cherokee, Iowa, in 1925, graduated from Washta High School in 1943,
and served in both the United States Air Corps and OSS before discharge in
1946. The rare full name, matching middle initial, year, Iowa context, and
service statements corroborate the exact-name Army row and support a
high-confidence identity despite the one-character identifier conflict.

Washta High School is modeled as student status, not employment. It is
strongly bounded before the December 1943 Army entry, but not labeled the
immediate pre-OSS affiliation. The Air Corps is modeled as a military
assignment with uncertain temporal relation to OSS; neither source establishes
a transfer date. Army occupation code 480 is published at medium confidence
with the identifier discrepancy visible. It is not narrowed to one trade and
does not name an employer.

## CIA, Library of Congress, web, and review adjudication

One bounded CIA Reading Room exact-name query and one current Library of
Congress employment query completed for every person. All twenty adapter
queries succeeded. CIA produced no candidates. Library of Congress produced
five J A Cross and five James E Cross candidates; every item and OCR context
was inspected.

The J A Cross pages contained only separated search tokens and no exact-name
context. The James Cross pages concern James G., T., A., or W. Cross, or date
to 1865. All ten candidates were rejected with item-specific reasons. The
review ledger was imported twice: ten state changes on the first pass and ten
duplicate skips on the second.

Exact-name OSS, employment, occupation, institutional, directory, newspaper,
obituary, military, and archival searches were completed for all ten people.
Search snippets, modern namesakes, family references, people-finder pages, and
short-value guesses were not promoted. The tracked adapter checkpoint now
contains 2,459 attempts, 511 candidates, and 45 person updates. Batch 500 adds
twenty machine attempts, ten candidate records, ten review decisions, and ten
synthesized outcomes.

## Corrective data audit

Visual review of Code No. 30 confirmed that occupation code 699 is the
semiskilled form of `6-99`, “Occupations in manufacture of radios and
phonographs.” Three earlier evidence bundles had mislabeled the same code as
electrical-machinery manufacturing. The existing stable claims for Herbert G.
Benshadle, Frank B. Bessac, and Vincent T. Catalano were corrected in place and
reimported; no duplicate claim or affiliation was created.

## Coverage after Batch 500

- Index coverage: 23,978 of 23,978 source rows linked, 100.0000%.
- Research-attempt coverage: 4,768 of 23,940 active person entities, 19.9165%.
- Verified-affiliation coverage: 544 people, 2.2723%.
- Verified-employer coverage: 242 people, 1.0109%.
- Archival-review coverage: 4,723 people assessed, 19.7285%.
- Claims by confidence: 1,132 confirmed; 1,403 high; 1,129 medium; 104 low;
  103 conflicting.
- Current research statuses: 227 verified employer; 95 documented prewar
  employer; 866 occupation only; 2,973 requires archival review; 230 needs
  identity review; 17 needs temporal review; 91 conflicting; 82 no reliable
  result after protocol; 135 completed; 44 in progress; 7 candidate found;
  1 blocked by source access; 19,172 not started.

## Archival next actions

Box 156 remains necessary for every person in this cohort. It must establish
the immediate pre-OSS pathway and any named employer for Paul Crosby, Vernon
Crosby, Allan Cross, and Gregg Crouch; identify Richard Crosby, J A Cross,
James E Cross, Arthur Crossley, Phyllis Croswell, and Paul Crouch; resolve
Allan Cross's birth-year anomaly; and resolve Gregg Crouch's identifier and
Air Corps-to-OSS sequence.

No authenticated NARA Catalog API request was made. Research resumes with
Sherman J Crough, PDF page 99 row 36, followed by the next nine immutable
source rows.
