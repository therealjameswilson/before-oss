# Batch 452 discovery checkpoint

Date: 2026-09-09 UTC

Scope: PDF page 89, printed rows 6-15

Indexed range: Edward A Condon through William J Coneys

Archive range: Boxes 137-138, location 230/86/29/01

## Source-row validation

The complete page was rendered at 150 dpi and compared with the immutable
source rows before research. All ten rows have blank printed rank and notes
fields. Edward A Condon, Jack G Condon, Richard S Condon, William A Condon,
Charles W Cone and Edward T Cone have private identifiers; Alma P Coneby,
Lucien E Conein, Leonard R Coneley and William J Coneys do not. The six-digit
value printed for Jack G Condon and the seven-digit value printed for Richard S
Condon remain literal private source values. They were not padded or replaced.

The indexed sequence and stable IDs are:

| Printed row | Indexed name | Box | Person ID | Source-record ID |
|---:|---|---:|---|---|
| 6 | Edward A Condon | 137 | `f83974d4-b345-5b59-a600-afa15f861e9e` | `35cef676-1321-508b-8b06-83f36e87b121` |
| 7 | Jack G Condon | 137 | `988d541b-9b5a-5b6a-889e-a081e7f3ea82` | `cd6e766c-5696-579f-8cf9-444475999b32` |
| 8 | Richard S Condon | 137 | `989e84b8-5283-5652-9e96-7c4bfbd74592` | `63b72a24-228c-5082-82d3-21091ec266df` |
| 9 | William A Condon | 137 | `680a7cd5-df36-549c-b6ae-e92488d17b55` | `1dceb812-986a-50a9-b731-e472d636a5a4` |
| 10 | Charles W Cone | 137 | `0e4fffa3-2043-502f-bb32-30f7eeb38c79` | `2b9be4a8-67d4-574c-a3ce-aee05ffa927b` |
| 11 | Edward T Cone | 138 | `bb558e11-f0e8-58ad-ae78-a7e9e6da4aaa` | `863096d0-809f-5d9e-9bbd-65b0ea5235f2` |
| 12 | Alma P Coneby | 138 | `5452b4fa-cffd-5541-b4b1-022ebe48770d` | `1a0537bb-87e0-54d6-978f-55dd83bfd0a7` |
| 13 | Lucien E Conein | 138 | `5e7905c6-6565-5f51-8b37-03e0f57205a1` | `245e5283-d3b7-5d93-b9eb-c85bf836ae81` |
| 14 | Leonard R Coneley | 138 | `963d955d-b76a-5694-996e-8afbabe87922` | `f586980c-43a9-5265-973d-9f278be8f852` |
| 15 | William J Coneys | 138 | `2edf51e5-1e6e-5a6b-b45d-18422496dfc1` | `ebf8b80e-a00a-5403-9e15-8b9cbb02f9b9` |

## Official Army comparison

The same official `ASNEF.FIN.DAT` file used in preceding batches was checked
at 185,043,578 compressed bytes and SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`.
The complete 9,200,232-record fixed-width file was scanned, not a surname
sample.

Four eligible eight-digit index identifiers produced exact-identifier and
exact-name matches:

- Edward A Condon: Army entry 5 March 1943, grade private, civilian-occupation
  value 992. NARA's official code list defines 9-92 as Students.
- William A Condon: Enlisted Reserve Corps entry 24 July 1942, grade private,
  civilian-occupation value 524. NARA defines the value as Operators,
  construction machinery. A plainly impossible birth-year field in the same
  converted row is withheld, documented as damage and not used for identity.
- Charles W Cone: Army entry 27 May 1943, grade private, civilian-occupation
  value 992, Students.
- Edward T Cone: Army entry 14 October 1942, grade private, civilian-occupation
  value 024, Musicians and teachers of music, and a 1917 birth-year value.

The matches support confirmed index-to-Army identities and enlisted Army
classification. The occupation fields are published as strongly date-bounded
historical categories, not employers and not proof of an immediate OSS
predecessor.

Jack G Condon's literal six-digit value and Richard S Condon's literal
seven-digit value have no Army identifier hit. Seven broad Jack Condon rows
and seventeen broad Richard Condon rows do not carry the indexed middle
initials. No candidate is assigned by name alone. Alma P Coneby, Lucien E
Conein and Leonard R Coneley have no exact-name row. William J Coneys has one
exact full-name Army row, but no private identifier joins it to the index, its
converted birth-year value is impossible for a 1942 entry, and other namesakes
remain possible. The row is retained as a rejected candidate, not a match.

The Army file is incomplete and is not a comprehensive OSS, officer, Navy,
Marine Corps, women's-service or foreign-personnel roster. Non-hits are not
negative proof.

## Public-source review

The current CIA adapter ran one bounded public OSS Collection search for each
person and returned no new candidate. The current Library of Congress adapter
ran one bounded exact-name employment search for each person. Seven candidate
newspaper pages were inspected in OCR context and rejected through
`loc_review_decisions_2026-09-09_batch452.csv`:

- five Edward A Condon pages refer to physicist Edward U. Condon or retired
  Major Edward S. Condon;
- one Charles W Cone page refers to painter Charles R. Conely;
- one William J Coneys page does not contain the name in its OCR.

None is used as employment or identity evidence.

Princeton University's detailed institutional biography identifies Edward T.
Cone as born in 1917, Princeton class of 1939, recipient of an MFA in music in
1942, and a wartime member of the Army's Office of Strategic Services. The
private-identifier match, birth year, music field and explicit OSS bridge
confirm that the indexed person is Edward Toner Cone. Princeton is modeled as
high-confidence student status ending in 1942. It is not modeled as an
employer; Cone's faculty appointment began in 1946. The Army occupation group
is separately qualified because it does not establish paid teaching,
performance work or a named employer.

Lucien E Conein already had reviewed high-confidence evidence. The contiguous
cohort review found no contradiction and preserves, without duplication, the
existing unnamed Kansas City printer as last civilian employer, U.S. Army
officer-candidate pathway as immediate pre-OSS affiliation, and earlier Kansas
National Guard and French Army service.

## Adjudication

| Person | Identity | Personnel category | Terminal status | Publishable pre-OSS result | Next action |
|---|---|---|---|---|---|
| Edward A Condon | confirmed | enlisted Army | occupation_only_found | student status, no institution | Review Box 137 for school and chronology |
| Jack G Condon | unresolved | unknown | needs_identity_review | none | Interpret the six-digit value in Box 137 |
| Richard S Condon | unresolved | unknown | needs_identity_review | none | Interpret the seven-digit value in Box 137 |
| William A Condon | confirmed | enlisted Army | occupation_only_found | construction-machinery occupation, qualified | Review original card and Box 137 |
| Charles W Cone | confirmed | enlisted Army | occupation_only_found | student status, no institution | Review Box 137 for school and chronology |
| Edward T Cone | confirmed | enlisted Army | occupation_only_found | Princeton student; music occupation | Review Box 138 for Army-to-OSS chronology |
| Alma P Coneby | unresolved | unknown | requires_archival_review | none | Establish identity in Box 138 |
| Lucien E Conein | high confidence | commissioned Army officer | verified_employer_found | existing printer and military pathway preserved | Seek direct Box 138 confirmation |
| Leonard R Coneley | unresolved | unknown | requires_archival_review | none | Confirm spelling and identity in Box 138 |
| William J Coneys | unresolved | unknown | needs_identity_review | none | Test the damaged Army candidate against Box 138 |

Every person has recorded NARA index context, complete Army comparison, CIA
and Library of Congress adapter checks, exact-name OSS searches with meaningful
variants, employment and occupation queries, and applicable institutional,
obituary, directory, newspaper, military and archival checks. No authenticated
NARA Catalog API request was made.

The evidence bundle adds five citation records, one organization, five
affiliations, nine claims, twenty-eight claim-source links, ten person updates
and ten reviewed-public research attempts. The adapters add twenty sanitized
attempts and seven separately reviewable candidate decisions. Private
identifiers, raw Army records, live API payloads and copyrighted pages are not
stored or published.

## Resulting coverage

After import and public-data generation, the durable database contains 23,978
source rows linked to 23,940 active person entities. Research-attempt coverage
is 4,294 / 23,940 (17.9365%); verified-employer coverage is 226 / 23,940
(0.9440%); verified-affiliation coverage is 511 / 23,940 (2.1345%); and
archival disposition has been assessed for 4,249 / 23,940 (17.7485%). There
are 19,646 active people still `not_started`.

The release and clean-rebuild checks are recorded in
`../reports/release_batch_452.md`.
