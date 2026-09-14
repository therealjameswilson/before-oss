# Batch 473 discovery checkpoint

2026-09-12 UTC. This checkpoint covers PDF page 93 rows 32-41, Tully R
Cornick Jr. through John P Corriera. All ten records are in Box 145 at location
230/86/29/02. The page was rendered at 180 dpi and every field was visually
compared with the immutable source records. Literal identifiers are omitted.

## Cohort and disposition

| PDF row | Source record | Person entity | Indexed name | Identifier class | Disposition |
|---:|---|---|---|---|---|
| 32 | 30d600cd-6e0a-5f54-95da-4a50a2346917 | 5c4ccadb-8b8a-50e0-8e71-8fae0cff6c3f | Tully R Cornick Jr. | eight digits | Confirmed Army identity; qualified sales-clerk occupation only |
| 33 | a61979f8-0883-528b-9b90-b7f9e3c39a5e | 66969e0a-fbe9-5585-b23e-a42d32a0e659 | George H Cornish | six digits | Army namesake carries a different identifier; ambiguous |
| 34 | ad1fa1b0-8d37-599f-ba4a-c65f6e75e419 | 846a5268-845f-57c7-b6a8-163e9246b300 | Andre Cornut | none | High-confidence French captain identity; no pre-OSS affiliation |
| 35 | 43de920c-d10c-59b9-9ceb-6781bb2aee3a | 21ca6b99-0cf9-5fc4-926d-02463a24b05f | Beatrice L Corr | none | Unresolved |
| 36 | f5dbca15-35bd-5bba-a84a-24f6367aefcd | 89491a94-b0da-5edf-bcd6-76316e01f4c1 | Margaret M Corragio | A-prefixed | Unresolved; identifier needs archival interpretation |
| 37 | d7d49e0f-04f6-5243-b3a2-cf07cd01d630 | 3525173e-a159-573d-ad9f-10e4889e028c | William I Correa | eight digits | Confirmed Army identity; qualified stenographer-and-typist occupation only |
| 38 | 00c1c12d-1a46-588e-9e7c-7b79f42bd771 | 717ce632-7dd4-5519-99f1-f138e180c085 | Louise J Correri | none | Indexed private rank retained; identity unresolved |
| 39 | e9d0a601-7d1b-52f3-9336-54bb56d69de4 | fa649630-9bf9-5c87-acdf-bb5e3a5b77ae | Bruce Corrick | seven digits | Unresolved |
| 40 | 9ae887cb-f0e4-5ab6-9be2-61be456e09b9 | c4c8394a-c3c6-52f9-9cce-eed2d158edb1 | John H Corridon | five digits | Unresolved; older military namesake rejected |
| 41 | a19674e3-42ac-5933-b779-a9419122b464 | bbbc2fac-83f2-5f77-8aac-65bf979c87c6 | John P Corriera | seven digits | High-confidence Army identity after one leading-zero format difference; no pre-OSS affiliation |

The adjacent next row is page 93 row 42, John F Corrigan.

## Army merged-file adjudication

The complete official Army merged file was scanned across all 9,200,232
fixed-width records.

- Tully R Cornick Jr. and William I Correa each produced one exact-name,
  exact-private-identifier match. Their Army-entry records are dated 12
  February 1942 and 20 August 1941. The official table defines their categories
  as Sales clerks and Stenographers and typists. Each is published only as a
  broad, temporally uncertain occupation. No employer, workplace, paid
  relationship or immediate OSS predecessor is inferred.
- John P Corriera produced one exact-name Army row whose eight-character
  identifier equals the seven printed index digits after one leading zero is
  restored. Its 1913 birth-year and Rhode Island context align with an official
  state veteran-graves inventory. The status remains high confidence because
  the Army-entry date, 10 November 1945, follows OSS dissolution. The late
  record supports identity and enlisted context only.
- George H Cornish produced one exact-name Army row with a different identifier.
  No fact is transferred. The other six people produced no exact-name Army row.

Nonappearance is not negative proof because the merged file is incomplete and
is not a comprehensive OSS, officer, Navy, women's-service or foreign roster.

## Public-source adjudication

One bounded exact-name CIA Reading Room query and one current Library of
Congress employment query were completed for each person; all returned zero
candidates. A transient CIA transport failure exposed a checkpoint bug: failed,
429 and server-error audits could suppress a deterministic retry. The adapter
now clears only those transient request-audit rows on resume, with a regression
test proving that a failed query can later succeed. Successful completed
requests remain deduplicated.

A compiled infiltration history identifies Captain Andre Cornut, alias
Guermantes, in a joint BCRA-OSS Proust mission near Confracourt on 9 September
1944 and supplies NARA M1623 and French SHD locators. The rare name, captain
rank, French nationality and OSS-associated context support high-confidence
identity, not a pre-OSS employer.

An 885th Bombardment Squadron roster corroborates Tully Cornick's identifier,
name, 1912 birth year and Nevada context. It documents later wartime service,
not pre-OSS employment. Common-name obituaries, directories, genealogy pages,
wrong-initial records, an older John H Corridon military record and a modern
John P Corriera junior-generation obituary were rejected.

## Archival next actions

Box 145 remains the controlling source for every person. It is needed to
establish employers and OSS-entry chronology; resolve George Cornish's
identifier conflict; interpret Margaret Corragio's A-prefixed identifier;
confirm John Corriera's leading-zero bridge and late Army chronology; and
identify the unresolved people.

No authenticated NARA Catalog API request was made. The exposed credential
remains unusable; the adapter stays fail-closed until a rotated key is supplied
outside chat.
