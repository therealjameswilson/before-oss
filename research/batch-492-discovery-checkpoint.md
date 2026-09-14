# Batch 492 discovery checkpoint

2026-09-13 UTC. This checkpoint covers personnel-index PDF page 97 rows
38-46 and page 98 row 1, Hilary Crawford through James W Crayhon. Both pages
were rendered at 180 dpi and visually checked against the extracted rows.
Literal private identifiers are omitted.

## Cohort and disposition

| PDF row | Source record | Person entity | Indexed name | Box | Disposition |
|---:|---|---|---|---:|---|
| 97:38 | 4bbd96c2-4d10-5f23-bd1b-9a22dfd0edf5 | 6e2f2941-0dad-5363-91ad-5afd66b3f4d7 | Hilary Crawford | 152 | Ambiguous; literal seven-digit value selects an unrelated Army name and one name-only Hilary H Crawford Jr. candidate is insufficient |
| 97:39 | ab6d1364-4d19-50f7-901e-6711323bf160 | a1f07e88-1d63-580c-8aa6-09290f707b6e | Jack B Crawford | 152 | Confirmed enlisted Army identity; qualified tool-sharpeners-and-dressers occupation, no named employer |
| 97:40 | 332bda4f-f4b4-5fc1-9f58-65e902ea483a | b6df8604-a52b-58ad-94f6-3c02b57615bb | John E Crawford Jr. | 152 | Confirmed enlisted Army identity; qualified general-office-clerk occupation, no named employer |
| 97:41 | 797ee5d7-fb33-5313-a2bc-3ba9a63efc72 | 7963d00d-25f1-581e-bf60-5de659d93ba0 | Ruth E Crawford | 152 | Unresolved; no defensible identity bridge or employer found in the accessible sources reviewed |
| 97:42 | 07fb6ca2-024b-578b-8e10-eb19b6c7d906 | 3c9f0d39-40c8-5c50-a09b-6fa35743b539 | Samuel J Crawford | 152 | Confirmed enlisted Army identity selected from six same-name rows; qualified carpenter occupation, no named employer |
| 97:43 | a6275ab6-c98a-55e6-a5d4-9f25d282c238 | e4ab74b0-c118-5a2d-93cb-5b26ea19eedb | William E Crawford | 152 | Confirmed identity, but the matching Army entry dates after OSS dissolution; status and occupation are not projected backward |
| 97:44 | b4a231d8-4ade-5e88-a7d2-ed11dc09f3cc | 71b3c835-7d1e-563d-8207-5000e34842f5 | William S Crawford Jr. | 152 | Ambiguous; one name-and-suffix Army row has no second identifier and an anomalous converted birth-year value |
| 97:45 | 52dcd087-4e1f-5221-9cfc-9429c9859430 | 54b07c9d-fbcc-5d67-b7c5-abf51761e15d | Alton O Crawley | 152 | Ambiguous; literal six-digit value collides with seven unrelated Army rows and was not padded |
| 97:46 | 96411817-f74f-5a97-b8ed-7b90e421fed3 | d7e21c57-6d30-588a-9e45-22483a598526 | Carlotta B Crawley | 153 | Unresolved; no defensible identity bridge or employer found in the accessible sources reviewed |
| 98:1 | 3de0661a-fef9-510c-a989-5cb6fc13bf4d | 2027bd17-62fb-51a8-90ee-785b6c079cae | James W Crayhon | 153 | Probable identity; qualified 1938 Associated Press photo city assignment editor employment, not immediate or last civilian |

All ten rows are at location 230/86/29/03. The next printed row is Robert N
Creadick, page 98 row 2, in Box 153. Its short printed value must be preserved
literally until the personnel file resolves it.

## Official Army-file adjudication

The complete official Army merged file was scanned once across all 9,200,232
fixed-width records. The downloaded ZIP contained 185,043,578 bytes and had
SHA-256 `80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`;
the extracted data file contained 837,221,112 bytes and had SHA-256
`db10dbf90f0ef95dc327b0e8f8f0489923941b65399cf79bba71ac4b45d07e5b`.
These are transient official inputs and are not committed.

Jack B Crawford, John E Crawford Jr., Samuel J Crawford and William E
Crawford have exact full-name and strict private-identifier agreements with
Army records. The first three entered as privates on 26 July 1943, 22 July
1942 and 15 July 1942. Official Code No. 30 defines their civilian-occupation
values as tool sharpeners and dressers, general office clerks, and carpenters.
Each occupation is published only at medium confidence and as strongly date
bounded. None names an employer or establishes the Army-to-OSS sequence.

William E Crawford's identifier selects one record from 28 exact-name Army
candidates, but it dates Army entry to 21 November 1945, after OSS
dissolution. The record confirms identity only. Its converted grade, infantry
branch and ore-dressing occupation remain private research context and are
not used to infer pre-OSS status, commissioned classification or employment.

Hilary Crawford's literal seven-digit value matches an unrelated Army name;
the one name-only Hilary H Crawford Jr. row lacks an OSS or Box 152 bridge.
William S Crawford Jr.'s one name-and-suffix row likewise lacks a second
identifier and contains an anomalous converted birth-year code. Alton O
Crawley's literal six-digit suffix occurs in seven unrelated Army rows, while
no exact-name row exists. None of these candidates is assigned. Ruth E
Crawford, Carlotta B Crawley and James W Crayhon have no exact-name Army row.
Non-hits are not negative evidence because the file is incomplete and is not
a comprehensive OSS, officer, Navy, women's-service, civilian or foreign
roster.

## CIA, Library of Congress and web adjudication

One bounded CIA Reading Room exact-name query and one current Library of
Congress employment query completed for every person. CIA returned no adapter
candidates. Library of Congress returned ten candidates. Every candidate was
opened in official page JSON/OCR context and rejected through the imported
review-decision CSV; a repeat import skipped all ten as duplicates, proving
idempotency.

The rejected pages concerned different people, incompatible initials,
historical namesakes or generic place-name wording. Exact-name OSS,
employment, occupation, institutional, newspaper, obituary, directory,
military and archival searches were completed for the cohort. Later careers,
discovery-only pages and unbridged namesakes were not promoted.

For James W Crayhon, Columbia University's 1938 annual report identifies
James Crayhon as Associated Press Photo city assignment editor on 11 March
1938. Loren Ghiglione's scholarly biography independently describes Crayhon
as an Associated Press supervisor and cites the author's 11 July 1975
interview with him. The uncommon exact first-and-last name and independent
sources support a probable identity and medium-confidence employment claim.
Neither source provides middle initial W, an OSS bridge, employment endpoints
or evidence that Associated Press was the immediate affiliation or last
civilian employer. The profile therefore labels the role documented prewar,
qualifies it visibly and excludes it from default employer analytics.

The tracked adapter checkpoint now contains 2,299 attempts, 473 candidates
and 45 person updates. Batch 492 adds 20 machine attempts and ten adjudicated
candidates; its ten synthesized outcomes are stored separately in the durable
research-attempt history.

## Archival next actions

Boxes 152 and 153 are needed for every person in this cohort: to establish
the Army-to-OSS sequence and named employer for the three occupation-only
profiles; reconstruct William E Crawford's post-OSS Army chronology; resolve
the two literal short values and the name-only William S Crawford Jr.
candidate; identify Ruth E Crawford and Carlotta B Crawley; and confirm the
probable Crayhon-Associated Press link and intervening chronology. Every
unresolved profile says that archival examination may be required rather than
asserting that no prior employment existed.

No authenticated NARA Catalog API request was made.
