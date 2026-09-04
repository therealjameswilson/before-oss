# Batch 402 discovery checkpoint — historical discovery record

Superseded on 2026-09-04 by the reviewed Batch 402 evidence bundle and
`reports/release_batch_402.md`. All ten outcomes have now been imported.
The text below preserves the earlier discovery state rather than silently
rewriting tentative findings as if they had already been adjudicated.

Started 2026-09-04 UTC while Batch 401's full local and GitHub test matrices
run. This is a research checkpoint, not ten completed outcomes. The database
and public coverage still end at Batch 401. Do not import these notes as facts.

## Cohort

Resolved directly from SQLite: source PDF page 78, rows 12-21; all Box 120,
location 230/86/28/06; printed ranks and notes blank. All ten rows were then
visually checked against the complete rendered page on 2026-09-04; the fields
match. The page really prints Jr. in both Leslie's first and last name fields.

| Row | Indexed/display name currently in SQLite | Person ID |
|---:|---|---|
| 12 | Catherine L Chaudet | 83fbb728-78d5-5937-8bff-05a2e9d52d71 |
| 13 | Harry D Chauvin | ab682014-4481-5aeb-82da-5f97fe88b403 |
| 14 | Albert Chavez | 5ed618ea-3fd5-59e9-ae65-19e324758389 |
| 15 | Aaron H Chayes | f0f65160-fc7a-5a54-a723-7aea9ae853a1 |
| 16 | Louis C Cheatham | a93259a6-252b-5580-b01d-d84a5f4a43c1 |
| 17 | Walter W Chechot | ba6b4769-c7f1-5ad4-a540-1186602077e8 |
| 18 | Abraham Checkoway | adccb97e-8d3e-5f93-a783-f4f200f35e8a |
| 19 | Lloyd Cheek | d183b618-59e9-5a78-a55c-e4ff5292df3f |
| 20 | Leslie, Jr. Cheek Jr. | 46cc3ed9-c738-5649-93c1-48994390bd94 |
| 21 | Bruce B Cheever | eaf8432d-7c3b-5e66-b131-2c2c0c7d9f7f |

The duplicated Jr. in the current Leslie display needs a reviewed normalized
display correction. Preserve both original name fields and the immutable row.

## Transient official Army bulk comparison

All 9,200,232 records in ASNEF.FIN.DAT were examined once. Three eligible
eight-digit private identifiers matched. No identifier, full raw row, or API
payload is retained here. Basic documentation physical pages 44-45 was visually
rechecked for field positions and alternate-card/coding limitations.

- Harry D Chauvin: exact name/identifier; date field 21 November **1946**,
  SGT, grade code 5, branch INF, occupation value 000, birth-year value 20.
  The postwar date prevents treating this as pre-OSS occupation or rank.
- Albert Chavez: exact name/identifier, 1 June 1943; grade text **7VT**,
  grade code 8, branch NO, occupation **345**, birth-year value 24. Four exact
  name candidates exist; only the identifier-backed one is potentially usable.
- Lloyd Cheek: exact identifier under **CHEEK LLOYD J**, 29 July 1943, PVT,
  grade 8, branch NO, occupation **590**, birth-year value 25. The middle J is
  a compatible candidate variant, not a correction to the printed index.

Important: visual inspection of compiled code list physical page 172 shows
3-44 followed by 3-47; **3-45 is not defined there**. Page 175 shows foremen
codes 5-91 onward, **not 5-90**. Do not guess neighboring occupations or copy
an unrelated decoded value. Earlier coding manuals or the underlying cards
may be required. No occupations are currently accepted from this comparison.
No earlier Army grade determines commissioned status during subsequent OSS
service. The remaining seven exact normalized name strings had zero matches;
this is not evidence of absent military service. Leslie's duplicated suffix
also makes the unexpanded exact-name comparison particularly limited.

## Item-level sources actually opened

### Leslie Cheek — promising institutional chronology, not yet adjudicated

Library of Virginia, Dictionary of Virginia Biography:
https://old.lva.virginia.gov/public/dvb/bio.asp?b=Cheek_Leslie
(the www.lva.virginia.gov URL redirects here). Accessed 2026-09-04.
The Arts Educator/Arts Administrator sections were read. They describe the
junior Leslie Cheek, teaching at William and Mary from 1935, becoming Baltimore
Museum of Art director in September 1939, leaving in spring 1942 for the Army
Corps of Engineers camouflage school, and serving with OSS during 1945.
This supports distinct civilian and military pathways, subject to identity
adjudication. Exact transition to OSS and commissioned status require care.
Do not transfer his father's business affiliations to him.

Smithsonian Archives of American Art, Leslie Cheek papers (collection 6457):
https://www.aaa.si.edu/collections/leslie-cheek-papers-6457
Search discovery reports museum and camouflage-unit dates; two direct web
opens returned internal errors. **Not a reviewed final source yet.** An oral
history interview of June 8, 1982 was also discovered, not yet opened.

### Bruce B Cheever — Marine/OSS evidence and a pre-OSS unit lead

Robert E. Mattingly, Herringbone Cloak–GI Dagger: Marines of the OSS,
USMC History and Museums Division, 1989 (1979 research paper):
https://www.usmcu.edu/Portals/218/Herringbone%20Cloak%20-%20GI%20Dagger%20Marines%20Of%20The%20OSS.pdf
Opened and text reviewed: physical page 163 / printed 139 identifies Cheever
as major commanding the OSS parachute training unit in England at the start
of 1944; physical page 341 / printed 313 lists him among Marine majors.
These establish an OSS role, not by themselves a pre-OSS assignment. The
publication retains the author's copyright; do not republish the full work.
Relevant page images still need inspection.

John H. Johnstone, United States Marine Corps Parachute Units, Historical
Reference Series 32, revised 1962, mirror of an official publication:
https://www.generalstaff.org/WW2/Pubs/USMC_Pamplets/USMC_HRS-32_Parachute_Units.htm
Opened, but the specific command-table section still needs full review and,
preferably, comparison with a page image or official-host copy. Discovery
indicates intermittent Cheever command dates in early 1943. Do not assign
another person's prior unit or employment to Cheever from adjacent narrative.

University of Washington 1947-48 catalog lists a Bruce B Cheever with a 1946
appointment; discovered, not opened and not linked. Model-railroad historian
Bruce Bissell Cheever is another plausible namesake, not automatically the
Marine. Dwight Cheever's obituary concerns a relative, not Bruce's employer.

### Other leads not reviewed as final evidence

- Abraham Checkoway appears in discovery of NSA Friedman collection file
  41722289076155.pdf, Civilian Employment Board agenda January 20, 1948:
  https://www.nsa.gov/Portals/70/documents/news-features/declassified-documents/friedman-documents/panel-committee-board/FOLDER_471/41722289076155.pdf
  Direct open failed. This is postwar and does not establish a pre-OSS job.
  A Coast Guard ensign cemetery transcription is an identity lead only.
- Walter Chechot, musician, appears in discovery of Billboard June 1, 1940:
  https://www.worldradiohistory.com/Archive-All-Music/Billboard/40s/1940/Billboard-1940-06-01.pdf
  Direct open failed. Middle W and OSS linkage remain unproved; no employer
  is named by the discovery text. Do not infer employment in an orchestra
  from a spouse's role.
- NCSU's Lloyd McForrest Cheek student page failed to open. Do not replace the
  identifier-backed Army middle J with an unrelated expanded name.

## Searches actually run

- Quoted indexed name plus OSS for all ten (Leslie searched as Leslie Cheek,
  Bruce also as Bruce B Cheever); Albert also with Office of Strategic Services.
- CIA-domain name searches: Catherine Chaudet, Harry Chauvin, Albert Chavez
  OSS, Aaron + Chayes, Louis Cheatham, Walter Chechot, Abraham Checkoway,
  Lloyd Cheek, Leslie Cheek, Bruce Cheever OSS.
- Employment/biography/obituary discovery: Catherine Chaudet obituary;
  Harry Chauvin Army 1940 and Harry D. Chauvin occupation; Albert Chavez OSS
  employment; Aaron H. Chayes biography, Aaron Chayes occupation/obituary;
  Louis C. Cheatham obituary and Louis Cheatham occupation 1940; Walter
  Chechot biography; Abraham Checkoway FCC and occupation newspaper;
  Lloyd J Cheek occupation obituary; Leslie Cheek war museum 1942 and
  Strategic; Bruce B. Cheever biography/1940, Bruce Cheever marines 1941 and
  Parachute Training School Cheever.
- Catherine L Chaudet site:loc.gov; Aaron Chayes site:archives.gov;
  Parachute Units Cheever site:usmcu.edu.

Rejected discovery classes: modern people-finders and LinkedIn profiles;
separate Aaron/Chayes names in unrelated documents; Senator/modern Chayes
namesakes; nineteenth-century house histories; Lloyd Cheek born 1931 (not the
matched Army birth-year 25); Katherine **T.** Chaudet without OSS linkage;
Magali Catherine Chaudet born after WWII. No living-family contact data or
medical details are retained. Search snippets are not accepted evidence.

## Resume

1. Inspect the relevant Marine-history pages and resolve Leslie's display only
   through a recorded review decision.
2. Complete meaningful variants and applicable institutional/newspaper checks
   for the unresolved identities. Pursue accessible official corroboration of
   Cheek and Cheever and assess immediacy separately from known earlier roles.
3. Preserve uncertain Army codes rather than inventing occupation labels.
4. Produce and validate a reviewed evidence bundle with individual dispositions
   only after adjudication. None of these ten has a terminal outcome yet.

## Continued checks before Batch 401 release

- The LVA byline/citation was reviewed: Brent Tarter; published 2006. This
  bibliography points to VMFA director's office accession 33863 at LVA and
  other institutional papers; those collections have not been examined.
- Johnstone's complete New River command-table section was reviewed. It
  lists Cheever intermittently January-May 1943, with the final listed
  interval April 19-May 5. It does not establish uninterrupted command or
  a direct transfer from that unit to OSS. There is a later unit redesignation;
  retain the contemporaneous name, Parachute Battalion, New River.
- The requested Mattingly PDF screenshots were not delivered as inspectable
  images by the tool (one also reported an internal error). Text review is
  completed, image review is not. No copyrighted pages were saved locally.
- The Smithsonian oral history URL was opened and returned an explicit
  Request Rejected page; stop automated retrieval there. The Cummings oral
  history failed to open. The museum's own director's-office finding aid
  https://cdn.artbma.org/2021/07/15131222/BMA_DirectorsOfficeFindingAid.pdf
  failed with 502, and a direct retry yielded no document. These remain
  collection leads rather than reviewed evidence.
- Added discovery queries: Harry Chauvin obituary 1920; Albert Chavez 1924
  OSS; Catherine Chaudet 1940; Aaron H Chayes Office; Leslie Cheek 1942
  site:artbma.org; Bruce Cheever 1943 Marine; Aaron H. Chayes Hayes; Walter W
  Chechot newspaper; Aaron Hayes OSS (search alias only); Catherine Chaudet
  OSS secretary; Walter Chechot Office of Strategic Services; Louis C
  Cheatham Office of Strategic Services; plus LoC-domain name queries for
  Louis Cheatham, Walter Chechot, Harry Chauvin, Aaron Chayes. These returned
  unrelated names/eras or the original index, not new accepted claims.
- An embedded-text scan of the complete Army code-list PDF found neither
  exact code 345 nor 590. This is not proof no alternate historical manual
  defines them; it reinforces withholding the occupation interpretations.
- Additional discovery: Johnstone Parachute Units PDF 1962; Leslie Cheek
  camouflage OSS; Abraham Checkoway Radio Intelligence; Walter Chechot
  musician. A Marine Corps official publication gateway for Silk Chutes and
  Hard Fighting was found, but not opened or used as evidence:
  https://www.marines.mil/News/Publications/MCPEL/Electronic-Library-Display/Article/899880/silk-chutes-and-hard-fighting-usmc-parachute-units-in-ww-ii/
