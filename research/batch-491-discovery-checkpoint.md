# Batch 491 discovery checkpoint

2026-09-13 UTC. This checkpoint covers personnel-index PDF page 97 rows
28-37, Virginia Crate through Eugene E Crawford. Page 97 was rendered at 180
dpi and visually checked against the extracted rows. Literal private
identifiers are omitted.

## Cohort and disposition

| PDF row | Source record | Person entity | Indexed name | Box | Disposition |
|---:|---|---|---|---:|---|
| 97:28 | 3962b676-50fc-507d-98a0-3ba3df8b84d8 | db3c624d-7dee-52c3-9db5-d03c585998ca | Virginia Crate | 152 | Unresolved; three newspaper hits were produce-market phrases rather than a person |
| 97:29 | 31ea175d-65c5-5bce-bf8f-2573cf5c54f9 | 8b13f39b-28a1-5dec-b1c2-a94bc65a4b2d | John H Craven | 152 | High-confidence enlisted Army identity; qualified managers/officials occupation, with the Army surname conflict explicit |
| 97:30 | f9564fe3-32cb-596b-bf5b-d764450222b0 | ddb91f00-acd8-56e7-9905-b79393540907 | William C Craven | 152 | Confirmed enlisted Army identity; alternate-card occupation value 417 withheld as unsafe to decode |
| 97:31 | 6bdecefd-608a-5a61-928c-73b65dd4ffe9 | 0f51260d-7a48-5849-9740-5220e0d7f9fa | William M Cravener | 152 | Confirmed enlisted Army identity; qualified welder/flame-cutter occupation at Army entry, no employer |
| 97:32 | 9768c77f-9a61-51a3-a4ee-e7b55e9b4a02 | ce10d4ed-b5e1-52f1-9f42-7ee6769ba198 | Kenneth W Craver | 152 | Ambiguous; literal seven-digit value was not padded and one name-only Army candidate is insufficient |
| 97:33 | 9aed6245-a23e-59a7-ba21-541d6af1d27a | 487ca004-c9a3-584f-8fbb-701dc70a614c | Alexander L Crawford | 152 | Confirmed enlisted Army identity; alternate-card occupation value 668 withheld as unsafe to decode |
| 97:34 | 7fbbce2d-2b53-5853-b9f9-ede567389938 | fd855d4a-79ca-5eac-8aa3-710aacf84f37 | Alice M Crawford | 152 | Ambiguous; one name-only Women's Army Corps candidate remains unassigned |
| 97:35 | 928a9b76-8152-5bbf-bfce-cc6429bb8c26 | 30f03ca7-5eb2-58ff-abf8-2bbd4dbe6114 | Archibald S Crawford | 152 | Unresolved; printed `aka Arch` note preserved and unsupported namesakes rejected |
| 97:36 | 6304d627-cbaf-5f38-8928-f591d291fa75 | a38a8f20-185c-51b5-81de-c1ad492e924a | Chester H Crawford | 152 | Ambiguous; literal seven-digit value was not padded and one name-only Army candidate is insufficient |
| 97:37 | 521814bd-c0d7-5535-b37c-d704e829bb0e | 72d10d6e-782c-53f2-b04e-7d7307e33634 | Eugene E Crawford | 152 | Ambiguous; four different exact-name Army rows cannot be selected |

All ten rows are at location 230/86/29/03. The next printed row is Hilary
Crawford, page 97 row 38, in Box 152.

## Official Army-file adjudication

The complete official Army merged file was scanned once across all 9,200,232
fixed-width records. The downloaded ZIP contained 185,043,578 bytes and had
SHA-256 `80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`;
the extracted data file contained 837,221,112 bytes and had SHA-256
`db10dbf90f0ef95dc327b0e8f8f0489923941b65399cf79bba71ac4b45d07e5b`.
These are transient official inputs and are not committed.

William C Craven, William M Cravener and Alexander L Crawford have exact
full-name and strict private-identifier agreements with Army records. John H
Craven's strict identifier selects one record whose converted name reads
`GRAVEN JOHN H`; the given name and middle initial agree, but the surname's
first letter does not. NARA's documentation warns of name-conversion defects,
so this is a high-confidence link with the discrepancy visible, not a silent
correction or a confirmed match.

The selected records date Army entry as privates on 21 April 1943, 8 July
1942, 8 December 1942 and 11 September 1942. Official Code No. 30 defines
John H Craven's value 097 as managers and officials not elsewhere classified
and William M Cravener's value 685 as welders and flame cutters. Both are
published only as medium-confidence, strongly date-bounded occupations. They
name no employer or workplace and do not prove the Army-to-OSS sequence.

The visually checked table does not safely support William C Craven's value
417 or Alexander L Crawford's value 668. Both are alternate ERC-card records,
and both values remain unpublished. Their identities and enlisted status are
documented without inventing an occupation.

Kenneth W Craver and Chester H Crawford each have a literal seven-digit index
value. Neither was padded or used as a strict identifier. Their single
exact-name Army rows remain private candidates. Alice M Crawford's single
exact-name WAC row also lacks a second identifier. Eugene E Crawford has four
different exact-name Army rows, and none is selected. Virginia Crate and
Archibald S Crawford have no exact-name Army row. Non-hits are not negative
evidence because the file is incomplete and is not a comprehensive OSS,
officer, Navy, women's-service or foreign roster.

## CIA, Library of Congress and web adjudication

One bounded CIA Reading Room exact-name query and one current Library of
Congress employment query completed for every person. CIA returned no adapter
candidates. Library of Congress returned eight candidates. Every candidate
was opened in official page JSON/OCR context and rejected through the imported
review-decision CSV; a repeat import skipped all eight as duplicates, proving
idempotency.

The rejected pages comprise three produce-market false phrases for Virginia
Crate, two century-old advertisements for John F. or John J. Craven, one
article naming William M. Cravens rather than either Craven or Cravener, and
an obituary for Alice Virginia Crawford rather than Alice M Crawford. Exact-
name OSS, employment, occupation, institutional, newspaper, obituary,
directory, military and archival searches were completed for the cohort.
Later, incompatible and discovery-only namesakes were not promoted.

The tracked adapter checkpoint now contains 2,279 attempts, 463 candidates
and 45 person updates. Batch 491 adds 20 machine attempts and eight adjudicated
candidates; its ten synthesized outcomes are stored separately in the durable
research-attempt history.

## Archival next actions

Box 152 is needed for every person in this cohort: to confirm the Craven/Graven
spelling and the two alternate-card occupation values; establish the Army-to-
OSS sequence and named employer for the four linked enlisted people; test the
name-only Army and WAC candidates; distinguish Eugene E Crawford's namesakes;
and identify Virginia Crate and Archibald S Crawford. Every unresolved profile
says that archival examination may be required rather than asserting that no
prior employment existed.

No authenticated NARA Catalog API request was made.
