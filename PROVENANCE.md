# Provenance

## Primary source

- Title: *OSS Personnel Files from Excel*
- Creator/publisher: National Archives and Records Administration
- Series: Record Group 226, Entry A1-224
- Official URL:
  <https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf>
- Retrieval date: 2026-07-28
- Retrieval method: user-supplied attachment, verified byte-for-byte against the
  current official NARA download
- File size: 1,799,300 bytes
- Page count: 522
- SHA-256:
  `7268492342ab131d3b6d2697cfa4f6856cbdcd16e0ed3877e8d6a0478f58c02b`

The frozen project copy is `data/source/personnel-database.pdf`. It is ignored
by Git because the official URL and cryptographic identity are sufficient to
restore it, and the document includes full service-number fields that are not
part of public project downloads.

The machine-readable manifest is
`data/provenance/source_manifest.json`.

## Reviewed digitized personnel-file sources

The second reviewed evidence batch used NARA's public digitized personnel-file
selections. The PDFs are not committed or republished. Their retrieval metadata
is preserved in
`research/evidence_selected-nara-personnel-files_batch-002_2026-07-29.json`:

| Person | Catalog | Pages | Bytes | SHA-256 |
|---|---|---:|---:|---|
| Ralph Bunche | <https://catalog.archives.gov/id/2168596> | 51 | 78,234,310 | `b345c88840420b5235e7ba081e18864c55a0f6ed59bee31485cc409c0699df77` |
| William J. Casey | <https://catalog.archives.gov/id/2169187> | 46 | 138,445,287 | `12b3acf13d71503b1555f730b6b84bb699896cf2a46db0b93a8cc9a4c988f0a7` |
| Arthur J. Goldberg | <https://catalog.archives.gov/id/2174048> | 46 | 46,920,770 | `dfda78854a11cbf1eb833a4caaff32ea69577872f32388996c299d8be690ec13` |
| Sterling Hayden / John Hamilton | <https://catalog.archives.gov/id/2175283> | 87 | 150,098,541 | `4fd5ab152bd7c00c15d0152a7ee26c314aadd916f5916d9cdd239959af6416bd` |

NARA's collection page describes these public copies as extracts or selected
highlights and says only Julia Child's copy is complete. Several PDF
introduction sheets use the label “complete file.” The database preserves that
disagreement and does not treat the four downloads as substitutes for the
original archival files.

## Reviewed CIA institutional histories

The third reviewed evidence batch matched four exact index rows to official CIA
histories. These are rated authoritative institutional sources, not direct
personnel files; the resulting identities are therefore high confidence rather
than confirmed. No full web page or PDF is committed or republished.

| Person | Official source | Locator |
|---|---|---|
| Morris Berg | <https://www.cia.gov/stories/story/moe-berg-baseball-player/> | “The Brainiest Man in Baseball” and “Joining a Different Kind of Team” |
| Virginia Hall | <https://www.cia.gov/resources/csi/static/7851e16f9e100b6f9cc4ef002028ce2f/Office-of-Strategic-Services.pdf> | PDF page 11, visually checked against the rendered page |
| Richard M. Helms | <https://www.cia.gov/resources/csi/static/Richard-Helms-Intel-Professional.pdf> | PDF pages 3–4, visually checked against the rendered pages |
| William E. Colby | <https://www.cia.gov/legacy/museum/artifact/office-of-strategic-services-compass/> | Artifact video transcript |

The project stores citation metadata, project-authored paraphrases, and
excerpts of no more than 25 words. It preserves the institutional histories'
limits: no civilian employer is inferred for Colby, Hall's unnamed ambulance
service is not reclassified as employment, and Berg's Red Sox last-employer
claim remains visibly qualified because his law-firm end date is unstated.

The fourth reviewed evidence batch extended the same official-source method:

| Person | Official source | Decision |
|---|---|---|
| John Ford | <https://www.cia.gov/stories/story/hollywood-and-the-office-of-strategic-services/> | Naval Reserve unit recorded as the immediate military assignment; no studio employer inferred |
| Christian J. Lambertsen | <https://www.cia.gov/stories/story/christian-lambertsen-and-the-secret-story-behind-scuba/> | Medical-school student status separated from qualified Ohio Chemical employment |
| Alfonso Rodriguez | <https://www.cia.gov/stories/story/the-glorious-amateurs-of-oss/> | Army G-2 recorded as a military assignment, not a civilian employer |
| Sidney L. Bartlett | <https://www.cia.gov/stories/story/hollywood-and-the-office-of-strategic-services/> | Identity and Army sequence remain medium-confidence pending Box 40 review; screenwriter occupation is not converted into an employer |

The CIA pages were reviewed as live HTML. No page copy was stored. Sidney L.
Bartlett remains outside default analytics because the institutional source
omits the index's middle initial and does not document an explicit Army-to-OSS
transfer.

The fifth reviewed evidence batch tested aliases, variant spellings, unnamed
occupations, and paired archival context:

| Indexed person | Official sources | Decision |
|---|---|---|
| Rene Veuve | <https://www.cia.gov/stories/story/the-glorious-amateurs-of-oss/> | Exact birth-name and French S/Lt context support a high-confidence Rene Joyeuse match; French Resistance is the immediate affiliation, with formal relationship left unknown |
| Jun Atshushi Iwamatsu | <https://id.loc.gov/authorities/names/n82056657> and [CIA institutional history](https://www.cia.gov/stories/story/the-glorious-amateurs-of-oss/) | Library of Congress variants bridge Jun and Atsushi Iwamatsu to Taro Yashima; OWI is recorded as the immediate government assignment and the index spelling remains visible |
| Tomoe Iwamatsu | <https://id.loc.gov/authorities/names/n82056669> and [CIA institutional history](https://www.cia.gov/stories/story/the-glorious-amateurs-of-oss/) | Exact authority-file variant, shared Box 365, and spouse context support the Mitsu Yashima match; unnamed art study is retained without inventing a school or employer |
| Joseph Savoldi Jr. | <https://www.cia.gov/stories/story/the-glorious-amateurs-of-oss/> | The distinctive match remains probable because the CIA history omits the index suffix; professional wrestler is an occupation, not a fabricated employer |

The Library of Congress authority JSON was inspected in memory and discarded.
The project retains only stable authority identifiers, source metadata, and
project-authored identity assessments.

The sixth reviewed evidence batch separated civilian, government, and military
wartime pathways:

| Indexed person | Official source | Decision |
|---|---|---|
| Peter J. Ortiz | <https://www.cia.gov/stories/story/the-glorious-amateurs-of-oss/> | U.S. Marine Corps recorded as the immediate military assignment; earlier French Foreign Legion service retained; an offered Hollywood job is not treated as accepted employment |
| Fisher Howe | <https://www.cia.gov/stories/story/the-spymasters-assistant/> | COI recorded as the immediate government assignment; Webb School remains the qualified probable last civilian employer; earlier employment and student status stay separate |
| Betty A. Lussier | <https://www.cia.gov/stories/story/the-intrepid-woman-betty-ann-lussier/> | Paid civilian Air Transport Auxiliary service separated from an unnamed B-26 plant; no aircraft manufacturer is guessed |
| Cordelia Dodson | <https://www.cia.gov/stories/story/glorious-amateurs-of-oss-sisterhood-of-spies/> | U.S. Military Intelligence recorded as the immediate government assignment; Reed College retained only as student status |

The Ortiz review also corrects the index-rank parser's generic Army category to
a distinct commissioned Marine Corps officer category. A forward-only SQLite
migration preserves the existing 23,978 source rows and 23,941 person entities.

The seventh reviewed evidence batch tested education-versus-employment
boundaries and direct military transfer evidence:

| Indexed person | Official source | Decision |
|---|---|---|
| James Angleton | <https://www.cia.gov/stories/story/agency-people-james-angleton-master-spy-hunter/> | Army training recorded as the immediate military assignment; Harvard Law and Yale retained only as student affiliations; adjacent James H. Angleton row remains separate |
| Edna W. Andrade | <https://www.cia.gov/stories/story/edna-andrade-from-the-oss-to-op-art/> | Pennsylvania Academy of Fine Arts retained as student status; no employer inferred from her husband's Navy position or her postwar work |
| Jane Burrell | <https://www.cia.gov/stories/story/the-mystery-of-jane-wallis-burrell-the-first-cia-officer-to-die-in-the-agencys-service> | Smith and Columbia retained as student affiliations; her husband's family business is not assigned as her employer |
| Edmund M. Burke | <https://www.cia.gov/stories/story/hollywood-and-the-office-of-strategic-services/> | Penn football retained as a non-employment affiliation; immediate assignment and employer remain unresolved |
| Robert C. Broughton | <https://www.cia.gov/stories/story/from-walt-disney-to-war-movies-bob-broughton/> | U.S. Army recorded as the immediate military assignment and Walt Disney Studios as the explicit last civilian employer; UCLA remains student status |

These cases leave three last-employer questions open for personnel-file and
directory review. The public profiles describe that incompleteness directly
rather than substituting a spouse's employer, a university, or a postwar job.

## Reviewed academic and military transitions

The twenty-fifth evidence batch tested immediate government and military
predecessors, civilian employment separated from those assignments, student
status, and an unresolved same-name pair:

| Indexed record | Principal sources | Decision |
|---|---|---|
| Preston E. James | [Syracuse University Archives](https://library.syracuse.edu/digital/guides_sua/html/sua_james_pe_prt.htm), [U.S. Naval Institute Proceedings](https://www.usni.org/magazines/proceedings/1942/december/book-reviews), and NARA's RG 226 guide | COI is the immediate government affiliation; University of Michigan is the last documented civilian employer |
| Norman O. Brown | [Online Archive of California](https://oac.cdlib.org/findaid/ark:/13030/kt6m3nd4kj/) and [Wesleyan University Magazine](https://magazine.blogs.wesleyan.edu/2003/01/04/celebrated-philosopher-norman-o-brown-dies/) | Army service is the immediate military predecessor; Nebraska Wesleyan is the last documented civilian employer |
| Leonard Krieger | Barry M. Katz, *Foreign Intelligence* (DOI `10.4159/harvard.9780674181519`) and the [University of Chicago](https://college.uchicago.edu/news/perspective-difficult-times) | Army transfer is the immediate predecessor; Yale is retained as student status, not employment |
| Two Paul M. Sweezy rows | [Harvard Houghton Library](https://id.lib.harvard.edu/ead/hou02824/catalog), [Harvard Crimson](https://www.thecrimson.com/article/1955/1/7/charges-connect-paul-sweezy-to-pro-communists/), and [Monthly Review](https://monthlyreview.org/articles/on-the-laws-of-capitalism/) | The biographical candidate is documented, but neither distinct private service number is mapped to him; both rows remain separate and ambiguous pending Box 761 review |

PDF page 458 was rendered and visually checked. It contains two Paul M. Sweezy
rows with the same printed name, box, and location but different service
numbers. The public data omit those numbers, publish no employer candidate as a
fact, and expose the duplicate-review status.

## Reviewed Area B command and engineer cadre

The thirty-second evidence batch used the [National Park Service's official
training history](https://www.nps.gov/articles/instructing-for-dangerous-missions.htm),
the NARA personnel index, and the [California State University, Fullerton OSS
oral-history finding
aid](https://coph.fullerton.edu/collections/OHP_18_OSS%20Finding%20Aid.pdf).
No live NARA Catalog API request or retained API response was involved.

| Indexed record | Decision |
|---|---|
| Ainsworth Blogg | Active Army Military Police service is the immediate pre-OSS affiliation; the earlier Seattle insurance occupation is published without guessing the company |
| Louise D. Cohen | Rendered PDF page 86 confirms `Louise`; the NPS Louis/Lewis Cohen candidate remains a withheld low-confidence lead pending Box 133 review |
| Morris M. Kessler | The exact name supports a probable, visibly qualified Area B identity, but no pre-OSS employer or dated occupation is inferred |
| Joseph E/M Lazarsky | Rendered page 269, the NPS Fort Belvoir chronology, and CSUF's Joseph E. Lazarsky oral-history entries support a high-confidence identity and immediate Army Engineer assignment |
| Leopold Karwoski | Rendered page 241 confirms `Karwoski`; NPS uses `Karwaski`. Both forms remain visible, and Fort Belvoir Army Engineer service is the high-confidence immediate affiliation |

The three rendered index pages showed no visual defects and confirmed the
source spellings, ranks, boxes, and locations used in the evidence bundle.

## Reviewed Area C and special-operations pathways

The thirty-third evidence batch used the [National Park Service's official
training history](https://www.nps.gov/articles/instructing-for-dangerous-missions.htm),
the NARA personnel index, a contemporary
[Carnegie Institute of Technology alumni
record](https://iiif.library.cmu.edu/file/ALU_1939_025_002_12001939/ALU_1939_025_002_12001939.pdf),
and the [1940 Raleigh city
directory](https://lib.digitalnc.org/record/25789?ln=en). No live NARA Catalog
API request or retained API response was involved.

| Indexed record | Decision |
|---|---|
| George S. Wuchinich | Army service is the explicit immediate pre-OSS affiliation; Fairbanks, Morse and Company is the best-supported last identified civilian employer, visibly qualified because a 1940–1941 intervening employer has not been ruled out |
| Hans V. Tofte | U.S. Army service is the explicit immediate affiliation; earlier British Special Operations Executive service remains a distinct government assignment |
| Howard E. Manning | Individual legal practice in Raleigh is the strongly date-bounded last civilian work; the separate `Manning & Manning` directory entry is not assigned to him; Army instructional service is a qualified probable immediate pathway |
| John F. Navarro | The official history supports a pre-OSS New England restaurateur occupation, but it does not name a particular restaurant employer |
| Peter G. Mero | The official history supports a pre-OSS Chicago investment-executive occupation, but it does not name a particular investment employer |

The Carnegie alumni scan was visually checked at PDF page 17, printed page 15.
The Raleigh directory was visually checked at full-PDF sequence page 596,
printed page 596, and sequence page 754, printed page 770. Those pages support
the employer and individual-practice decisions without republishing either
source.

## Reviewed Area B staff and Allied pathway

The thirty-seventh evidence batch used the
[National Park Service's official training history](https://www.nps.gov/articles/instructing-for-dangerous-missions.htm),
the NARA personnel index, and the contemporary Prince Albert *Daily Herald*
article
[“Veteran of Lofoten Raid”](https://princealbertlibrary.ca/padh/1941/October/Oct%2015%2C%201941.pdf).
No live NARA Catalog API request or retained API response was involved.

| Indexed record | Decision |
|---|---|
| Benton E. Bickham Jr. | The uncommon exact name, middle initial, Louisiana origin, enlisted grade, and Area B staff context support a high-confidence identity; the accessible official history explicitly does not supply his earlier background, so no pre-OSS employer or occupation is inferred |
| Milton W. Griffith | The NPS diary transcription first uses `Milton Giffith` and then Griffith for the Pittsburgh camp staff member; the match remains probable because it lacks the indexed middle initial, grade, and service number, and “bus driver” is not published as pre-OSS employment because it may describe camp duty |
| Louis Lostfogel | The rare name, physician specialty, grade progression, and Areas B/A/C Medical Corps role support a high-confidence identity; physician and Philadelphia origin do not establish a named pre-OSS practice or employer |
| Edmund I. Stromholt | The 1941 newspaper identifies Lieutenant Edmund Stromholt in the Norwegian Army after the Lofoten raid and serving with a Norwegian infantry company in England; NPS calls him Edward and sequences his English commando instruction into OSS training. The discrepancy remains visible, and Norwegian Army service is published as the immediate military affiliation, not a civilian employer |
| James Herbert and James E. Herbert | The adjacent Box 329 rows remain separate ambiguous entities. NPS's 1943 James Herbert naval-officer and Chicago radio-instructor account lacks a middle initial, service number, or box reference, so both candidates and their Navy affiliations remain private and withheld pending review of both personnel files |

Index PDF pages 36, 182, 204, 283, and 453 were rendered and visually checked.
They confirm the source spellings, ranks, private service-number distinctions,
boxes, and archival locations used in the evidence bundle. Full service
numbers remain private and do not appear in public pages or downloads.

## Reviewed Area B enlisted staff and Velleman identities

The thirty-eighth evidence batch used the
[National Park Service's official training history](https://www.nps.gov/articles/instructing-for-dangerous-missions.htm),
the NARA personnel index, Moritz Velleman's first-person account at the
[Digitaal Joods Monument](https://www.joodsmonument.nl/nl/page/617617/emigration),
a family-supplied
[Moritz Velleman obituary](https://patch.com/new-york/portwashington/moritz-velleman-longtime-port-washington-resident-dies),
and a qualified secondary OSS document-production history. No live NARA
Catalog API request or retained API response was involved.

| Indexed record | Decision |
|---|---|
| Moritz Velleman | The rare exact name, Dutch/Belgian background, arrival in the United States after France fell, Army enlistment, and Area B account support a high-confidence identity. U.S. Army service is the immediate military affiliation; earlier French Army service and work for an unnamed Lisbon office remain separate pre-OSS affiliations. The office is not promoted to last civilian employer because the source does not establish that chronology. |
| Arthur H. Velleman | The adjacent index row is a separate person with a different private service number. Moritz's account identifies Arthur as his brother already in the United States after leaving Belgium in 1939. A secondary source's OSS Documents Division lead remains qualified and does not establish a pre-OSS affiliation. |
| George A. George | NPS's `Georges George` Area B staff member is retained as a probable, visibly qualified match because the source omits the indexed middle initial, service number, and box. No pre-OSS affiliation is inferred. |
| Howard C. Ressler | NPS's Corporal Ressler is a plausible Area B lead, but the common surname, different grade context, and missing middle initial leave the identity ambiguous. The lead remains withheld pending Box 640 review. |
| Raymond W. Deisher | NPS's Corporal Deisher is a plausible rare-surname lead, but the official history says his first name and background were unknown. The identity remains ambiguous and no employer is inferred. |

Index PDF pages 111, 165, 389, and 482 were rendered and visually checked.
They confirm the five source rows and show Arthur and Moritz Velleman as
adjacent but distinct records. A seeming Raymond W. Deisher hit in the 1943
Rochester directory was also rendered and rejected: the entry belongs to the
preceding Deisinger listing. The rejected lead and reason are retained in the
research audit trail; full service numbers remain private.

## Reviewed Field Photographic and media pathways

The thirty-ninth evidence batch used rendered NARA index pages, institutional
archival authority records from Dartmouth, Indiana University, and the
University of Wyoming, a near-contemporary Dartmouth alumni account, a
Washington Post obituary, a Marine Corps Association history, a Library of
Congress-hosted scholarly book, and the
[CIA's Hollywood and OSS history](https://www.cia.gov/stories/story/hollywood-and-the-office-of-strategic-services/).
No live NARA Catalog API request or retained API response was involved.

| Indexed record | Decision |
|---|---|
| Seymour W. Schulberg | Dartmouth's authority record bridges the indexed name to Budd Wilson Schulberg. Naval Reserve service is the explicit immediate military pathway. Columbia and RKO are jointly documented immediately before enlistment, but neither is promoted above the other as chronologically last; earlier Selznick Pictures employment is published separately. |
| Stuart H. Schulberg | Independent Marine, scholarly, and newspaper sources support the identity and correct the generic rank-based Army category to enlisted Marine Corps personnel. Marine service is the immediate pre-OSS affiliation; the Washington Daily News is the best-supported last civilian employer. |
| Robert R. Parrish | Indiana University's finding aid and a film-institution biography support the Robert Reese Parrish identity and prewar assistant- and sound-editor occupations. No employing studio or adequately sourced immediate military pathway is inferred; `CSP P` remains unexpanded. |
| Sol Kaplan | The American Heritage Center finding aid identifies a concert pianist and composer who worked for the Army Signal Corps and OSS. Because it does not establish the order or name a civilian employer, the profile publishes occupation only and sends the sequence to Box 390 review. |
| Corey Ford | CIA and Dartmouth records support the former OSS member and Army Air Corps colonel identity. Vanity Fair and The Saturday Evening Post are modeled as prewar professional publication relationships, not employers; the immediate pre-OSS assignment remains unresolved. |

Index PDF pages 150, 240, 358, and 415 were rendered at 180 DPI and visually
checked. They confirm all five rows, including the two adjacent Schulberg
records, raw ranks, boxes, and locations. Full service numbers remain private
and are masked from every public page and download.

The Stuart Schulberg review also adds a forward-only
`enlisted_marine_corps_personnel` category. The migration rebuilds only the
person-entity classification table, preserves all 23,978 immutable source rows,
and leaves the raw printed `S/SGT` value unchanged.

## Reviewed field officers, musicians, and Mayer duplicate group

The fortieth evidence batch used rendered NARA index pages, the CIA's official
biographies of
[Roderick Stephen Hall](https://www.cia.gov/stories/story/roderick-stephen-hall-the-saboteur-of-brenner-pass/)
and
[Miles Copeland](https://www.cia.gov/stories/story/miles-copeland/),
the National Park Service's
[Mediterranean and European theaters history](https://www.nps.gov/articles/oss-in-action-the-mediterranean-and-european-theaters.htm),
a reprint of George Musulin's 1946 sworn testimony, contemporary newspaper
obituaries, a historical football roster, and institutional and official
Operation Greenup accounts. No live NARA Catalog API request or retained API
response was involved.

| Indexed record | Decision |
|---|---|
| Roderick G.S. Hall | Hall's exact initials, name, Army engineer unit, Camp Adair location, and signed 1943 OSS proposal support a confirmed identity. The 270th Engineer Combat Battalion is the explicit immediate military pathway. Yale is published separately as student status, not an employer. |
| Miles A. Copeland | The uncommon name, matching middle initial, and CIA's jazz-to-Army-to-OSS chronology support a high-confidence Miles Axe Copeland Jr. identity. Divisional Army finance work is the immediate military affiliation; professional jazz musician is an occupation-only result because the reviewed source does not establish a single employing organization. |
| George S. Musolin | The index spelling remains visible alongside the documented Musulin variant. A private identifier match, compatible rank progression, official Yugoslavia role, and 1946 testimony support a confirmed identity. The 115th Regiment of the 29th Infantry Division is the explicit immediate pathway. Professional football is published as an occupation, but conflicting team coverage prevents selection of a last civilian employer. |
| Frederick Mayer, 2nd Lt | Exact name, commissioned grade, official OSS identification, refugee history, and Operation Greenup service support a high-confidence identity. Army service is the immediate pathway. Ford and General Motors mechanic work are documented as earlier prewar employment, but neither is labeled chronologically last. |
| Frederick Mayer, rank blank | This adjacent Box 494 row remains a separate ambiguous entity. It has a different private service number from the commissioned row, and no reviewed authoritative record links that identifier to Mayer's documented enlisted phase. The candidate link is withheld pending review of both files and authoritative service records. |

Index PDF pages 92, 189, 302, and 335 were rendered at 180 DPI and visually
checked. They confirm all five rows, including the two adjacent Frederick Mayer
records, the printed `Musolin` spelling, raw ranks, boxes, and archival
locations. A private identifier on the Musulin testimony page was compared
programmatically with the index value and recorded only as a match result; the
number itself is absent from the evidence bundle and all public data.

## Reviewed Mediterranean veterans and Obolensky duplicate group

The forty-first evidence batch used rendered NARA index pages; two National
Park Service chapters on OSS training and Mediterranean operations; a
contemporary Veterans of the Abraham Lincoln Brigade bulletin; the NYU
Tamiment Library's Milton Felsen finding aid; a 1939 *Harvard Crimson* report;
a 1989 *Los Angeles Times* obituary; and an August 1943 OSS mission-personnel
memorandum in the CIA Reading Room. No live NARA Catalog API request or
retained API response was involved.

| Indexed record | Decision |
|---|---|
| Milton Felsen, rank blank | This serial-only Box 231 row remains a separate ambiguous entity. Its adjacency, exact name, and box make it a plausible duplicate of the Sergeant row, but no reviewed source links the private identifier. The candidate is withheld pending joint file review. |
| Milton Felsen, Sgt. | NPS and NYU records support a high-confidence identity. University of Iowa attendance is student status; Abraham Lincoln Battalion service is a foreign military assignment; and the 1941 veterans-organization office is a professional affiliation. None is converted into a civilian employer. |
| Irving Goff | Official, contemporary, and obituary sources support a high-confidence identity and Captain rank progression. Lincoln Brigade service and the 1941 Veterans of the Abraham Lincoln Brigade office remain distinct affiliations. A contemporary report documents an adagio-dancer occupation but names no employer or self-employment arrangement. |
| Paul H. Gale | NPS explicitly identifies Captain Paul Gale as a 1st Infantry Division staff officer whom Donovan later recruited. The index's middle initial and later Colonel grade make the identity high confidence; Box 258 review is still required for confirmation and any civilian predecessor. |
| Serge Obolensky | The exact distinctive name and Lieutenant Colonel rank in an OSS memorandum confirm the identity. New York National Guard service is the explicit immediate military pathway. St. Regis Hotel consulting is documented earlier employment, but the source does not prove it was the last civilian role before Guard service. |

Index PDF pages 143, 159, 172, and 346 were rendered at 180 DPI and visually
checked. They confirm all five source rows, including the two adjacent Felsen
entries, their distinct rank/identifier layouts, raw notes, boxes, and archival
locations. Full service numbers remain private and are masked from every public
page and download.

## Reviewed analysts and maritime officers

The forty-second evidence batch used rendered NARA index pages; contemporaneous
University of Illinois Board minutes and its archival finding aid; a
contemporary *Public Opinion Quarterly* article and Museum of Broadcast
Communications biography; an official *London Gazette* notice and a specialized
British Army officer register; a visually checked 1944 Evros Mission report;
the CIA Center for the Study of Intelligence's Coast Guard history; and a
corroborating obituary. No live NARA Catalog API request or retained API
response was involved.

| Indexed record | Decision |
|---|---|
| Richard G. Arnold-Baker | The uncommon name, printed `British A` note, official expanded name, temporary-major rank, and Intelligence Corps branch support a high-confidence identity. British Army service is published only as a medium-confidence wartime affiliation because the OSS sequence remains unknown. |
| Everett J. Athens | The visually checked Evros report confirms the indexed naval lieutenant as `Everette J. Athens`, USNR, second in command. The spelling is retained as a variant; Box 24 remains necessary for the pre-OSS assignment and civilian-employer questions. |
| Clarence A. Berdahl | Contemporaneous Board minutes explicitly connect his University of Illinois professorship and chairmanship to departure for the OSS London staff. The university is both the confirmed immediate affiliation and last civilian employer. |
| Hugh M. Beville | A 1940 article and institutional biography document NBC research employment from 1930 and a brief wartime Army interruption. NBC is the high-confidence last civilian employer, but is not mislabeled immediate pre-OSS because the Army sequence remains unresolved. |
| John P. Booth | The CIA history identifies Coast Guard Lieutenant John Booth as an officer assigned to OSS duty and OSG II commander. Coast Guard service is the high-confidence immediate military pathway; no postwar occupation is repurposed as prewar evidence. |

Index PDF pages 14, 15, 33, 35, and 44 were rendered at 180 DPI and visually
checked. They confirm all five source rows, including the `British A`, `Doctor`,
`Army`, and `Coast G` notes and the naval rank. The Evros report's personnel
page was also rendered and checked. Full service numbers remain private and are
masked from every public page and download.

The Booth review adds forward-only
`commissioned_coast_guard_officer` and `enlisted_coast_guard_personnel`
categories. The parser now gives a printed `Coast G` note precedence over a
generic rank interpretation while retaining the raw rank and note unchanged.

## Reviewed scholarship, medicine, and ONI chronology

The forty-third evidence batch revisited six already partially researched
profiles using rendered NARA index pages; official or institutional histories
from Harvard, Hunter College, Princeton, Stanford, and the Marine Corps
University; and a contemporary wartime medical report. It closed each open
research attempt with a reviewable terminal outcome. No live NARA Catalog API
request or retained API response was involved.

| Indexed record | Decision |
|---|---|
| Carl E. Schorske | Harvard doctoral study remains the high-confidence immediate pre-OSS affiliation and is not converted into employment. No reliable civilian employer was found; Box 687 review remains the next action. |
| Cora Du Bois | Hunter College teaching is documented earlier employment. Work at Boston Psychopathic Hospital with Henry Murray is retained separately as a professional affiliation because the accessible biography does not establish an employment arrangement. Neither claim is promoted to immediate or last-civilian status. |
| Franklin L. Ford | Cornell graduate study is student status; the United States Army is the explicit immediate military pathway. No civilian employer is inferred from education. |
| Franklin P. Holcomb | Civilian Office of Naval Intelligence employment before Pearl Harbor is the last civilian employer. His subsequent active-duty Marine Reserve billet at ONI is the immediate military assignment before formal OSS entry in 1943. The shared institution does not collapse the two relationships. |
| Gordon A. Craig | Princeton doctoral study is a qualified probable immediate affiliation, not employment. The profile remains routed to Box 151 review for the unresolved interval and civilian-employer question. |
| James C. Luce | A wartime report supports the Navy Medical Corps-to-OSS Detachment 101 transfer. No pre-Navy civilian employer is inferred. |

Index PDF pages 97, 125, 150, 212, 284, and 414 were rendered at 180 DPI and
visually checked. They confirm all six printed rows, names, ranks, boxes, notes,
and archival locations. Full service numbers remain private and are masked from
every public page and download.

Migration 008 aligns the immutable `source_records` personnel-category
constraint with the person-entity constraint. It fixes a full-rebuild failure
introduced when earlier forward-only migrations added Marine Corps and Coast
Guard categories only to `person_entities`; it changes no raw PDF values.

## Reviewed employment transitions and terminal protocols

The forty-fourth evidence batch revisited eight already partially researched
profiles. It combined rendered NARA index pages with an Archives of American
Art oral history, a University of Rhode Island institutional biography,
official CIA material already in the database, official 1941 *Foreign
Relations* documentation, contemporary or reputable obituaries, and an
interview-based professional profile. No live NARA Catalog API request or
retained API response was involved.

| Indexed record | Decision |
|---|---|
| Edna W. Andrade | Andrade's Smithsonian oral history documents a three-month Hecht Company floor-manager job followed by government applications and appointment to an office that had become OSS. Hecht is therefore the high-confidence, strongly date-bounded immediate and last civilian employer; Newcomb College teaching from 1939 through spring 1941 is earlier employment. |
| Mort S. Bobrow | The completed online protocol supports University of Washington student status, Army Mandarin training, and later OSS service in China. No reliable civilian employer was identified; Box 63 remains the archival next action. |
| Edmund M. Burke | The available CIA source supports identity and the Penn football affiliation. An unreferenced tribute-page statement naming the Insurance Company of North America could not be corroborated and is not published as fact; Box 93 review is required. |
| Jane Burrell | Smith and Columbia remain student affiliations. Her husband's family business and Navy assignment are not evidence of her employment, and the 1937-1943 interval remains an archival question for Box 95 and contemporary directories. |
| John H. Hemingway | Dartmouth student status, Army entry, Military Police assignment, and the direct OSS transfer are supported. No civilian employer is inferred for the interval; the online protocol is terminal with Box 326 retained as a refinement step. |
| Conrad F. LaGueux | URI documents a 1938-1943 chemical-engineering and ROTC path followed by commission, active duty, Infantry School, and immediate OSS assignment. The university is a student affiliation, not an employer. |
| John Magruder | Official sources establish a continuous career-Army path through command of the U.S. Military Mission to China and into OSS. The profile is terminal; Box 475 is needed only to refine assignment dates. |
| Peter M. F. Sichel | Independent reputable profiles support an apprenticeship with the Bordeaux branch of H. Sichel Söhne as the last civilian employment before internment, escape, 1941 U.S. Army enlistment, and OSS. The adjacent Peter M. Sichel row has a different private service number and remains a separate entity pending joint Box 709 review. |

Index PDF pages 10, 41, 61, 62, 202, 263, 290, and 426 were rendered
at 180 DPI and visually checked. They confirm all eight target rows, and page
426 confirms the adjacent Sichel entries, distinct middle-initial layouts, and
different service numbers. Full service numbers remain private and are masked
from every public page and download.

The Smithsonian and other copyrighted sources are not copied into the
repository. The evidence bundle retains citation metadata, project-authored
paraphrases, and short excerpts within the project's 25-word limit.

## Reviewed terminal protocols and Allied pathways

The forty-fifth evidence batch completed nine bounded review protocols. It
combined rendered NARA index rows with the French Service historique de la
Défense personnel-file catalog, Fondation Charles de Gaulle and Free French
naval rosters, a British Normandy Memorial research profile grounded in SHD
records, and a reputable obituary. No live NARA Catalog API request or retained
API response was involved.

| Indexed record | Decision |
|---|---|
| Billie F. Akin | Exact-name, employer, occupation, official-source, newspaper, directory, obituary, and archival searches did not establish an identity beyond the CAF-7 index row. Box 7 is required; no employer is invented. |
| Étienne Ancergues | The French note, officer grade, SHD file pointer, full-name rosters, naval-radio rank, BCRA attachment, and Sussex mission support a high-confidence identity. His French Navy service is earlier military history; the BCRA assignment begun 1 February 1944 is the strongly date-bounded immediate pathway into joint OSS/SIS training, not a civilian employer. |
| Julia N. Barnhart | The accessible protocol did not securely distinguish the SP-7 record from namesakes or identify an employer. Box 38 and contemporary personnel records are the next action. |
| Philip H. Chadbourn Jr. | The uncommon name, suffix, Major rank, 1939 Harvard graduation, and OSS parachute service support a high-confidence identity. Harvard is published only as student status; Box 115 is required to resolve the 1939-to-wartime interval and immediate predecessor. |
| Jacqueline M. Landry | Married-name and namesake candidates lacked corroborating OSS identifiers and prewar chronology. Box 430 remains necessary. |
| Gus Macriyanni | A spelling-variant cemetery/genealogy lead lacked service-number or OSS linkage and was rejected. The private service number and Box 473 file are required for identity resolution. |
| Carl D. Marshall | Wrong-initial and OCR-token candidates did not match the private service identifier or OSS context. Box 485 and Army records are required. |
| Constantine Papadopoulos | The common name produced an unrelated Greek political figure and other unsupported namesakes. Box 583 and naval records are required before any affiliation can be published. |
| Lawrence N. Stevens | Common-name and wrong-initial naval candidates lacked Ensign, OSS, or pre-service corroboration. Box 745 remains the archival next action. |

Index PDF pages 4, 8, 23, 75, 264, 289, 296, 356, and 448 were rendered at
180 DPI and visually checked. Page 8 confirms that `14` is Ancergues's box,
not his PDF page. All nine rows, ranks or civilian grades, boxes, notes, and
archival locations match the immutable source records. Full service numbers
remain private and are masked from every public page and download.

The French roster's January 1941 value is retained as Free French entry context
and is not silently converted into a BCRA start date. The more specific
institutional biography dates Ancergues's BCRA volunteer entry to 1 February
1944; the profile preserves that distinction and routes the formal
BCRA/SIS/OSS administrative relationship to paired NARA and SHD file review.

## Reviewed student, employment, and terminal protocols

The forty-sixth evidence batch reviewed ten indexed people. The Congressional
Record explicitly places S. Douglass Cater Jr. at Harvard before his education
was interrupted for OSS service; Harvard is therefore modeled as student
status, not employment. A reviewed NARA JFK record and contemporary timeline
support Marshall W. Houts's FBI-to-unemployment-to-Eastern Air Lines-to-Army
and OSS sequence. Jane Lester's institutional oral history and a short
published-history excerpt support only the qualified historical wording “a
brokerage in Buffalo”; no firm name is invented. Seven additional searches
ended in box-specific archival review after unsupported candidates were
rejected.

Index PDF pages 74, 92, 112, 128, 217, 223, 274, 344, 462, and 470 were
rendered and visually checked. The three-page NARA Houts record was also
rendered and inspected. The evidence bundle stores citation metadata,
project-authored paraphrases, and short excerpts; it does not retain a NARA API
response or republish copyrighted pages.

## Reviewed first-page military pathway and terminal protocols

The forty-seventh evidence batch completed bounded protocols for ten records
on the first printed index page. Denver Public Library's institutional
*10th Mountain Division Name Index* supplies an exact private-identifier match
for Olaf H. Aanonsen and places him in Company C, 99th Infantry. Matthew T.
Bolland's published history independently names Aanonsen among the battalion
members selected for OSS training. Together they support a high-confidence,
explicitly immediate military pathway without inventing a civilian employer.
The source disagreement among PVT, Pfc., and the NARA index's Cpl grade remains
visible; the public affiliation uses the rank-neutral role “Company C soldier.”

| Indexed record | Decision |
|---|---|
| Sigurd J. Aalbu | An aviation-index lead and unsourced genealogy references lacked direct identifiers, OSS context, and employment chronology. Box 1 is required. |
| Olaf H. Aanonsen | High-confidence identity and immediate Company C, 99th Infantry Battalion assignment; Box 1 remains necessary for the grade sequence, exact transfer date, and last civilian employer. |
| Helen G. Abbenante | Exact-name and source-specific searches produced no corroborating identity or pre-OSS affiliation. Box 1 is required. |
| Charles R. Abele | Common-name and modern business candidates lacked direct wartime identifiers. Box 1 is required. |
| Herbert A. Abele Jr. | A World War I namesake and unsuffixed candidates were rejected. Box 1 and suffix-specific service evidence are required. |
| Norman W. Abendschein | Postwar Forest Service directories and a relative's 1940 death notice do not establish pre-OSS employment. Box 1 is required. |
| Michael K. Abraham | Modern and common-name candidates lacked direct identifiers and wartime chronology. Box 1 is required. |
| Alexander A. Abromaitis | No corroborating official, institutional, newspaper, directory, obituary, or archival source was found. Box 2 is required. |
| Salvatore H. Acampora | A same-name ABMC record lacks the direct identifier and pre-OSS evidence needed for acceptance. Box 2 is required. |
| John Achelis | John Fritz Achelis and another namesake lack direct linkage to the indexed enlisted record; Commercial Factors Corporation is not assigned. Box 2 is required. |

The NARA index page 1 and Denver Public Library PDF page 2 were rendered and
visually inspected. Full service identifiers remain private and are masked from
public pages and downloads. No live NARA Catalog API request or cached API
response was involved.

## Reviewed page-six Allen identities and federal pathway

The seventy-first evidence batch completed the bounded protocol for ten
contiguous page-six records, Hedvig J. Allen through Laura D. Allen. It combines
the frozen NARA index row, an official OSS monthly activity report, an official
IRS agency-history timeline, an institutional museum exhibition, a
descendant-authored family history grounded in wartime papers, and a
transcription of a wartime award citation. It stores only citation metadata,
project-authored paraphrases, and short evidence excerpts; it contains no NARA
Catalog API response.

The distinctive Hedvig J. Allen entry is published at high identity confidence
as Hedvig Elizabeth Johnson Allen. The family chronology places her at the
federal tax agency from July 1941 and says she applied to the newly organized
OSS one week after Pearl Harbor. Because that source uses the later name
“Internal Revenue Service,” the affiliation preserves the wording as found
while the organization table separately uses the historically accurate Bureau
of Internal Revenue, supported by the official agency timeline. The
government-assignment claim is medium-confidence and visibly qualified; no
last civilian employer is inferred.

The NARA index prints `Col` in Keith Allen's middle-initial cell and leaves the
rank cell blank. The row was rendered and visually reviewed before normalized
rank and commissioned status were corrected. An official September 1944 OSS
report names Lieutenant Colonel Keith Allen during an OSS-supported air
operation over Norway, and the award-citation transcription independently
expands the name to Keith Nichols Allen while matching rank, date, and Army Air
Forces context. The identity is high-confidence, but neither source establishes
his immediately pre-OSS assignment or last civilian employer. Box 10 remains
required. The other eight people remain unresolved after the minimum online
protocol and also route to Box 10.

The parser-wide audit found sixteen additional military grades printed in the
same displaced column pattern. All seventeen affected military rows were
rendered and inspected at original detail, along with the six earlier civilian
grade rows. Raw values remain immutable. The replay registry now records 23
row corrections across 20 pages and supports multiple audited corrections on
one page by validating unique page-row coordinates.

## Page-six Allen continuation, Batch 072

`research/evidence-page-six-allen-continuation-two-pathways_batch-072_2026-07-30.json`
records the minimum online research protocol for the ten contiguous Marian A.
Allen-through-Thomas B. Allen rows on PDF page six. The bundle contains ten
visually checked official index citations, ten terminal research attempts, and
ten person updates. It stores no live NARA Catalog response, credential,
service identifier, full copyrighted page, or sensitive modern-person detail.

The protocol reviewed official NARA index context, CIA Reading Room discovery,
exact-name and punctuation variants, employment and occupation searches,
obituaries, Library of Congress newspaper discovery, directories,
institutional sources, military or officer sources where applicable, and
archival leads. A 1945 Atlanta educator and later California contractor, a
1929-born veteran's spouse, a late-1945 Army enlistee, generic veteran and
officer records, modern people-finder results, and the historian Thomas Benton
Allen were rejected because chronology or corroborating identifiers did not
match. The bundle retains only project-authored rejection reasons and directs
all ten profiles to Box 10. No employer, affiliation, or resolved identity was
invented from these namesakes.

## Page-six Allen-through-Alley continuation, Batch 073

`research/evidence-page-six-allen-through-alley-pathways_batch-073_2026-07-30.json`
records the minimum online research protocol for the ten contiguous Vernon C.
Allen-through-John N. Alley rows on PDF page six. The bundle contains ten
visually checked official index citations, ten terminal research attempts, and
ten person updates. It stores no live NARA Catalog response, credential, full
service identifier, copyrighted page, or sensitive modern-person detail.

The protocol reviewed official NARA index context, CIA Reading Room discovery,
exact-name and punctuation variants, employment and occupation searches,
obituaries, Library of Congress newspaper discovery, directories,
institutional sources, military or officer sources where applicable, and
archival leads. A career-Army Walter Paul Allen, a West Virginia Carey
Allender, a Pennsylvania Josephine Allenovitch Smutny, a Texas medical
technologist named Clifford O. Allenson, ambiguous newspaper OCR concerning
Richard M. Allenson, and generic military, cemetery, and directory namesakes
were withheld because none supplied the required OSS link and corroborating
historical identifiers. The bundle directs the first three profiles to Box 10
and the remaining seven to Box 11. No postwar occupation, ambiguous military
status, employer, affiliation, or resolved identity was inferred from these
leads.

## Page-six/seven Alley-through-Allison continuation, Batch 074

`research/evidence-page-six-seven-alley-through-allison-pathways_batch-074_2026-07-30.json`
records the minimum online research protocol for the ten contiguous Roy
Alley-through-James S. Allison rows spanning PDF pages six and seven. The
bundle contains ten visually checked official index citations, ten terminal
research attempts, ten person updates, one normalized organization, one
qualified affiliation, and two public claims. It stores no live NARA Catalog
response, credential, full service identifier, full copyrighted page, or
sensitive modern-person detail.

An official OSS order in the CIA FOIA Electronic Reading Room names Harry B.
Allinsmith and records his April 1944 appointment as chief of the Radio
Intelligence Division. That direct OSS evidence confirms that the indexed H.
B. Allinsmith is Harry B. Allinsmith. The 1956 *International Television
Almanac* entry was downloaded, text-searched, rendered, and visually inspected
at printed page four; it reports that Harry Bryan Allinsmith entered the
motion-picture industry with the Bell System in 1929 and later worked in
commercial and managerial positions with several named subsidiaries and
successors. A 1942 city directory independently records the same Harry B.
Allinsmith as an assistant manager in New York but does not name the employer.
The project therefore publishes Bell System only as medium-confidence
documented prewar employment. It does not choose a subsidiary, infer an
unrecorded sequence, or present the affiliation as immediate or as the last
civilian employer.

The remaining nine profiles route to Box 11. A Roy Alley enlistment candidate
with a conflicting private identifier, plausible-age naval and Army namesakes,
a relative-only missionary-archive result, modern directory entries, and
rank-inconsistent cemetery evidence were withheld. Jack B. Allin's unfamiliar
printed `CSP P T` abbreviation remains unexpanded and unclassified. Full
private identifiers were used only for comparison and are absent from the
evidence bundle and public output.

## Page-eight Ambrose-through-Ames continuation, Batch 075

`research/evidence-page-eight-ambrose-through-ames-pathways_batch-075_2026-07-30.json`
records the minimum online research protocol for the ten contiguous Dadus I.
Ambrose-through-Robert L. Ames rows on PDF page eight. The bundle contains ten
visually checked official index citations, ten terminal research attempts, ten
person updates, two normalized organizations, two qualified student
affiliations, and four public claims. It stores no live NARA Catalog response,
credential, full service identifier, full copyrighted page, or sensitive
modern-person detail.

A contemporary *World Politics* contributor note records Ruth Amende Rosa's
OSS service from 1942 through 1946. Brown University's Pembroke Center
identifies Ruth Amende with the class of 1941, a 1941 Providence directory
records Ruth G. Amende as a student, and an official 1945 diplomatic record
corroborates her wartime identity. The project therefore publishes Brown
University only as a medium-confidence, documented-prewar student affiliation.
It is not classified as employment, immediate pre-OSS affiliation, or the last
civilian employer.

An OSS Operational Groups roster records Harry T. Ameredes as a Technician
Fifth Grade in Greek Group V. An independent Weirton newspaper account states
that Harry Ameredes served with OSS, and a memorial record supplies the
Theodore middle name. The newspaper documents his 1939 graduation from Weir
High School, which is published only as a medium-confidence, documented-prewar
student affiliation. Its undated reference to a later Weirton Steel career is
not used to infer pre-OSS employment.

An official May 1944 OSS board record names a Private Peter Ambrose, but the
record's private identifier materially conflicts with the indexed Box 12 row.
The project preserves that conflict and does not merge the records. The same
document names a Ben Ames in Cairo, but the blank-rank Box 13 index row lacks
the corroborating identifiers required for a match and remains ambiguous. The
remaining six identities are unresolved. All eight cases route to Box 12 or
Box 13 review without promoting discovery-only, common-name, or
chronologically incompatible candidates.

## Page-eight Ames-through-Amon continuation, Batch 076

`research/evidence-page-eight-ames-through-amon-pathways_batch-076_2026-07-30.json`
records the minimum online research protocol for the ten contiguous Ruth
Ames-through-Phillip J. Amon rows on PDF page eight. The bundle contains ten
visually checked official index citations, ten terminal research attempts, ten
person updates, and one public identity claim linked to three sources. It
contains no organization or pre-OSS affiliation assertion. It stores no live
NARA Catalog response, credential, full service identifier, full copyrighted
page, or sensitive modern-person detail.

An OSS Operational Groups roster names Technician Fifth Grade Nick J.
Amigdalitsis in Greek Group IV. An independent American War Memorials Overseas
record repeats the uncommon name, grade, 2671st Special Reconnaissance
Battalion, and OSS operational-group association. Together with the indexed
name, middle initial, and grade, these sources support a high-confidence
identity match while preserving `Amigdalitis` and `Amigdalitsis` as documented
variants. They concern wartime OSS service and do not establish his immediate
pre-OSS assignment, civilian employer, or the timing of any earlier Greek
Battalion association.

A specialist roster also names a Sergeant Paul Amico in an Italian Operational
Group. An official congressional tribute and an obituary describe a Secaucus
Paul Amico's Army entry and later civilian career, but neither supplies an OSS
link or unique identifier. The common-name candidates remain unmerged and the
postwar diner chronology is not published as pre-OSS employment. A newspaper
item for William W. Amick conflicts on the middle initial, a local James
Ammerman item lacks naval or OSS identifiers, and a William R. Ammon military
record belongs to a chronologically incompatible later namesake. The other
searches did not establish reliable identities or predecessor affiliations.
All ten profiles therefore route to Box 13 review, with Nick's wartime identity
published separately from the still-unresolved employer questions.

## Page-eight Amoruso-through-Amunrud continuation, Batch 077

`research/evidence-page-eight-amoruso-through-amunrud-pathways_batch-077_2026-07-30.json`
records the minimum online research protocol for the ten contiguous Vittorio
Amoruso-through-Sever B. Amunrud rows on PDF page eight. The bundle contains
ten visually checked official index citations, ten terminal research attempts,
ten person updates, two normalized organizations, two affiliations, and four
claims supported by sixteen source records. It stores no live NARA Catalog
response, credential, full service identifier, full copyrighted page, or
sensitive modern-person detail.

A visually inspected October 1944 OSS memorandum identifies the indexed
Uliuss L. Amoss as Ulius L. Amoss and states that he was president of
Gramtrade International Corporation when approached about joining the
Coordinator of Information in November 1941. The memorandum documents his
subsequent COI assignment. NARA's OSS history establishes the institutional
transition from COI to OSS in June 1942, and a University of Oregon finding
aid independently expands his name to Ulius Louis Amoss and corroborates his
OSS role. These sources support a high-confidence identity resolution,
Coordinator of Information as the immediate pre-OSS government assignment,
and Gramtrade as the last civilian employer. The evidence does not establish a
formal Gramtrade separation date, so none is asserted.

An OSS Operational Groups roster contains a Vittorio Amoruso at a different
printed grade, and a cemetery transcription contains an Earl S. Amspacher with
World War II Army service but no unique OSS link. Those candidates remain
low-confidence identity leads and are withheld from public facts. The
incomplete Amory row and the remaining six people yield no reliable identity
or pre-OSS affiliation after the official, exact-name, employment,
newspaper/directory/obituary, institutional, and archival stages. All nine
non-Amoss profiles retain actionable Box 13 or Box 14 archival-review
guidance.

## Page-eight Amy-through-Ancergues continuation, Batch 078

`research/evidence-page-eight-amy-through-ancergues-pathways_batch-078_2026-07-30.json`
records the minimum online research protocol for the ten contiguous Richard P.
Amy-through-Etienne Ancergues rows on PDF page eight. Etienne Ancergues already
had a completed Batch 045 outcome, so the new bundle does not repeat or alter
his research. It contains nine visually checked official index citations, nine
terminal research attempts, nine person updates, three normalized
organizations, three affiliations, and six claims supported by sixteen source
records. It stores no live NARA Catalog response, credential, full service
identifier, full copyrighted page, or sensitive modern-person detail.

Harvard Divinity School Library's institutional history documents Milton V.
Anastos as its librarian from 1936 through 1939. A Harvard finding aid and
Dumbarton Oaks source independently identify the same Byzantine scholar; the
latter documents his 1941–1943 Junior Fellowship. The librarian role is
published as high-confidence documented pre-OSS employment. The fellowship is
published as a visibly qualified, medium-confidence professional affiliation,
not employment and not an immediate predecessor to OSS.

A contemporary Library of Congress newspaper image identifies Harry H.
Anbender as an attorney working from United Auto Workers counsel Maurice
Sugar's office in May 1941. A later institutional newspaper obituary
corroborates his legal identity and World War II Air Force service. The record
supports a high-confidence professional affiliation with Sugar's office, but
does not establish formal employment, immediacy, or the last civilian employer;
the public profile therefore remains occupation-only.

Searches for Angelo Anastasio produced a plausible but underidentified
contemporary lieutenant, while `Anacap` and `Anania` were tested only as search
aliases for the clearly printed Anacab and Anamia rows. None was adopted as a
name correction or public fact. Richard Amy, John Anacab, Christian
Anagnostis, Ettore Anamia, Angelo Anastasio, Peter Anastasio, and Stella
Anastos retain Box 14 archival-review guidance. Etienne Ancergues's previously
reviewed Allied pathway remains unchanged.

## Page-eight and page-nine Ancrum-through-Anderson continuation, Batch 079

`research/evidence-page-eight-ancrum-through-page-nine-anderson-pathways_batch-079_2026-07-30.json`
records the minimum online research protocol for ten contiguous rows from
Calhoun Ancrum Jr. on PDF page eight through Albert C. Anderson on page nine.
It contains ten visually checked official-index citations, ten terminal
research attempts, ten person updates, two organizations, two student
affiliations, and eight claims supported by seventeen source records. It
stores no live NARA Catalog response, credential, full service identifier,
full copyrighted page, or sensitive modern-person detail.

An official Department of Defense Distinguished Service Cross list repeats
Calhoun Ancrum Jr.'s distinctive name, suffix, no-middle-initial form, and
First Lieutenant grade. A Military Times profile directly documents his OSS
service, while Duke's contemporary 1935 yearbook documents his student status.
Together they support a high-confidence identity resolution and a qualified
student affiliation. The evidence does not establish employment, an immediate
pre-OSS predecessor, or a last civilian employer. A published lead concerning
later writing and editing was not promoted because the cited book page could
not be inspected in an accessible lawful copy.

A Seattle Times obituary identifies Donald E. Anderegg as a Willamette
University graduate who studied radio communications before Army and OSS
radio service in the Burma-India theater. The uncommon exact name, middle
initial, technical field, and explicit OSS service support a high-confidence
identity resolution. Willamette is published only as a medium-confidence
student affiliation, not an employer or immediate predecessor.

A specialist OSS Operational Groups roster lists T/5 Harold Andersen and T/5
Jorgen Andersen under Norwegian Operations. The exact names, grades, and OSS
context support probable identities, but the roster omits a complete
identifier and does not item-cite its underlying primary records. Both claims
therefore remain visibly qualified at medium confidence. Harold Andersen's
printed `T-5` remains preserved in the raw middle-initial cell while the
reviewed normalized record transparently classifies it as the displaced rank.

Discovery-only or later-career namesakes for James T. Ander and Robert E.
Andersen remain withheld at low confidence. Searches also rejected an
unrelated former FBI employee named Harold E. Andersen, a Camp Shelby
Frederick Anderegg without a matching middle identifier, and a physician with
the wrong middle initial. Frederick C. Anderegg, Ora V. Anders, Erik J.
Andersen, and Albert C. Anderson remain unresolved. All ten profiles retain
Box 14 archival guidance for the immediate pre-OSS affiliation and last
civilian employer.

## Page-nine Anderson archival pathways, Batch 080

`research/evidence-page-nine-anderson-archival-pathways_batch-080_2026-07-30.json`
records the minimum online research protocol for ten contiguous rows from
Allen A. Anderson through Erik J. Anderson on PDF page nine. It contains ten
visually checked official-index citations, ten terminal research attempts,
and ten person updates. It adds no organization, affiliation, or employment
claim because no candidate met the project's identity and temporal standards.
It stores no live NARA Catalog response, credential, full service identifier,
full copyrighted page, or sensitive modern-person detail.

The visually checked rows preserve the distinctions among Corporal Allen A.
Anderson, civilian-grade employees Alvina S. Anderson and Beatrice M.
Anderson, Captain David F. Anderson, professional-grade employee Dorothy M.
Anderson, and five rows whose personnel category remains indeterminate.
Duane M. Anderson's unfamiliar printed `C8M` text is preserved without
expansion or forced classification.

An official Army Service Forces booklet lists a David F. Anderson in an
officer-candidate class, but the common name, absent private-identifier match,
and missing OSS and later-captain chronology do not meet the enhanced
disambiguation rule. A 1941 archival-correspondence result for Dorothy M.
Anderson similarly lacks an OSS link, P-3 grade connection, geography,
profession, or second corroborating identifier. Both leads remain rejected
for attribution. Obituary, veteran, genealogy, directory, newspaper,
institutional, CIA Reading Room, NARA Catalog-context, and Library of Congress
searches produced only unrelated, modern, or underidentified namesakes for
the remaining people.

All ten identities remain unresolved and retain dignified Box 14 or Box 15
archival-review guidance. Each profile states that no reliable pre-OSS
employer has yet been identified in the accessible sources reviewed; none
implies that the person had no prior employment.

## Page-nine Anderson continuation archival pathways, Batch 081

`research/evidence-page-nine-anderson-continuation-archival-pathways_batch-081_2026-07-30.json`
records the minimum online research protocol for ten contiguous rows from
Eugene N. Anderson through Howard B. Anderson on PDF page nine. It contains
ten visually checked official-index citations, ten terminal research attempts,
and ten person updates. It adds no organization, affiliation, or employment
claim because no candidate met the project's identity and temporal standards.
It stores no live NARA Catalog response, credential, full service identifier,
full copyrighted page, or sensitive modern-person detail.

The reviewed rows preserve the distinctions among civilian professional-grade
employees Eugene N. Anderson and Howard M. Anderson; enlisted Army personnel
George W. Anderson, George H. Anderson, Harold Anderson, Henry A. Anderson,
and Howard B. Anderson; commissioned Naval Reserve officer Henry J. Anderson;
and Frederick F. Anderson and Gordon Anderson, whose personnel categories
remain indeterminate.

An exact-name Eugene N. Anderson appears as a State Department official in the
1945 Official Register. The record is later than the relevant recruitment
period and supplies no OSS connection, P-7 link, recruitment chronology, or
second corroborating identifier, so it remains a rejected lead rather than an
identity or employment claim. Searches also rejected an exact-name Army
private without sufficient identifier agreement, multiple incompatible Harold
Anderson military and occupational biographies, underidentified Naval Reserve
and cemetery entries for Henry J. Anderson, and unrelated domestic, foreign,
genealogy, directory, obituary, and modern namesakes.

All ten identities remain unresolved and retain dignified Box 15 archival
guidance. Each profile states that no reliable pre-OSS employer has yet been
identified in the accessible sources reviewed; none implies that the person
had no prior employment. Full service identifiers and sensitive modern-person
details remain private.

## Page-nine Anderson James-and-John archival pathways, Batch 082

`research/evidence-page-nine-anderson-james-and-john-archival-pathways_batch-082_2026-07-30.json`
records the minimum online research protocol for ten contiguous rows from
Howell W. Anderson through John H. Anderson on PDF page nine. It contains ten
visually checked official-index citations, ten terminal research attempts, and
ten person updates. It adds no organization, affiliation, or employment claim
because no candidate met the project's identity and temporal standards. It
stores no live NARA Catalog response, credential, full service identifier,
full copyrighted page, or sensitive modern-person detail.

The reviewed rows preserve the distinctions among civilian professional-grade
employees James F. Anderson and Jean C. Anderson; enlisted Army personnel Jack
W. Anderson and James R. Anderson; commissioned Army officers James T.
Anderson, John W. Anderson, and John H. Anderson; and Howell W. Anderson,
James W. Anderson, and Jean R. Anderson, whose personnel categories remain
indeterminate.

The staged searches rejected several exact-name candidates rather than
silently attaching their careers to common-name index rows. These included a
postwar Tennessee electrical engineer, a World War II infantry officer, an
armored-division veteran, an Air Force photographic-reconnaissance commander,
a Tenth Air Force captain, and later-war or foreign military namesakes. Each
candidate lacked some combination of a matching private identifier, OSS
connection, compatible rank chronology, and a second corroborating historical
identifier. The rejected organizations and occupations were not promoted to
claims or public citations.

All ten identities remain unresolved and retain dignified Box 15 archival
guidance. Each profile states that no reliable pre-OSS employer has yet been
identified in the accessible sources reviewed; none implies that the person
had no prior employment. Full service identifiers and sensitive modern-person
details remain private.

## Page-nine Anderson John-through-Margaret archival pathways, Batch 083

`research/evidence-page-nine-anderson-john-through-margaret-archival-pathways_batch-083_2026-07-30.json`
records the minimum online research protocol for ten contiguous rows from
John K. Anderson through Margaret J. Anderson on PDF page nine. It contains
ten visually checked official-index citations, ten terminal research attempts,
and ten person updates. It adds no organization, affiliation, or employment
claim because no candidate met the project's identity and temporal standards.
It stores no live NARA Catalog response, credential, full service identifier,
full copyrighted page, or sensitive modern-person detail.

The reviewed rows preserve the distinctions among Chief Warrant Officer John
K. Anderson; civilian-grade employees Karl A. Anderson and Katherine G.
Anderson; enlisted Army personnel Kenneth A. Anderson, Kirk T. Anderson,
Lawrence A. Anderson Jr., and Leonard W. Anderson; commissioned Army officer
Kermit W. Anderson; and Loma J. Anderson and Margaret J. Anderson, whose
personnel categories remain indeterminate. Loma J. Anderson's unfamiliar
printed `WAE` text remains unexpanded and unclassified pending file review.

The staged searches rejected several namesake pathways rather than silently
attaching them to these common-name index rows. The rejected candidates
included a young Army veteran with a later civilian career, a British merchant
seaman killed in 1942, a national-cemetery corporal, a discovery-only shipyard
employment lead, underidentified military roster and city-directory
occurrences, and later or rank-incompatible cemetery records. Each lacked some
combination of a matching private identifier, an OSS connection, compatible
rank and chronology, and a second corroborating historical identifier.
People-finder results and results exposing sensitive identifiers were excluded;
the rejected organizations and occupations were not promoted to claims or
public citations.

All ten identities remain unresolved and retain dignified Box 15 or Box 16
archival guidance. Each profile states that no reliable pre-OSS employer has
yet been identified in the accessible sources reviewed; none implies that the
person had no prior employment. Full service identifiers and sensitive
modern-person details remain private.

## Page-nine/ten Anderson Margaret-through-Orval pathways, Batch 084

`research/evidence-page-nine-ten-anderson-margaret-through-orval-pathways_batch-084_2026-07-30.json`
records the minimum online research protocol for the final two rows on PDF page
nine and the first eight rows on page ten, from Margaret M. Anderson through
Orval W. Anderson. It contains ten visually checked official-index citations,
ten terminal research attempts, ten person updates, fifteen citation records,
one organization, one affiliation, and two claims. It stores no live NARA
Catalog response, credential, full service identifier, full copyrighted page,
or sensitive modern-person detail.

Nine common-name identities remain unresolved and retain high-priority Box 16
review guidance. The staged searches rejected military, banking, cemetery,
legislative, obituary, institutional, and modern namesakes that lacked the
indexed private identifier, compatible rank or surname chronology, an OSS
connection, or the additional identifiers required for a common-name match.
No rejected employer or assignment is promoted to a public claim.

Odd A. Anderson is the exception. Matthew T. Bolland's published Operation
Rype roster matches the indexed uncommon name, middle initial, enlisted
context, and private service identifier exactly. The identifier was compared
in the private database and is not reproduced in the evidence bundle or public
exports. Contemporary 1941 and 1942 publications independently place Odd
Anderson of Evanston at Purdue, and a Dartmouth alumni newsletter preserves a
family account and transcript of Tony Gordon's August 6, 1987 *Wilmette Life*
interview. In that interview Anderson said OSS recruited him during his
freshman year at Purdue.

The public result preserves the distinction the project is designed to make:
Purdue University is a medium-confidence, probably immediate student
affiliation, not an employer. The 1987 recollection is explicit about the
freshman-year timing, but the accessible evidence does not rule out a short
Army reception or unit assignment before formal OSS entry. A current official
Army history says NORSO was recruited from the 99th Infantry Battalion, but it
does not individually identify Anderson. The possible 99th pathway and any
last civilian employer therefore remain questions for Box 16 rather than
settled public facts.

## Page-ten Anderson Otto-through-Shirley archival pathways, Batch 085

`research/evidence-page-ten-anderson-otto-through-shirley-archival-pathways_batch-085_2026-07-30.json`
records the minimum online research protocol for ten contiguous rows from Otto
E. Anderson through Shirley J. Anderson on PDF page ten. It contains ten
visually checked official-index citations, ten terminal research attempts, and
ten person updates. It adds no organization, affiliation, or employment claim
because no candidate met the project's identity and temporal standards. It
stores no live NARA Catalog response, credential, full service identifier, full
copyrighted page, or sensitive modern-person detail.

The reviewed rows preserve Otto E. Anderson and Paul R. Anderson as enlisted
Army personnel; Pauline M. Anderson and Shirley J. Anderson as civilian-grade
personnel; Richard F. Anderson as a commissioned Army officer; Robert N.
Anderson and Robert E. Anderson Jr. as enlisted Army personnel; and Ralph J.
Anderson as indeterminate. Most importantly, two adjacent Robert J. Anderson
rows remain separate: the Master Sergeant and Technical Sergeant have
different private identifiers and therefore are not merged.

The staged searches exposed two particularly persuasive false-positive risks.
A 2019 first-person account by a Paul R. Anderson describes believed OSS work
but also describes commissioning as a second lieutenant, while the indexed
person is a Technical Sergeant; without a matching private identifier or
another corroborating identifier, the account remains a rejected identity
candidate. A declassified 1944 OSS-related travel order names a Technical
Sergeant Robert J. Anderson, but the order's private identifier differs from
both adjacent Box 16 records. It therefore establishes a third same-name person
rather than either index row.

Mount Rushmore employment, DPAA, cemetery, obituary, unit-roster, directory,
and modern namesake leads for the remaining rows likewise lacked a matching
private identifier, compatible rank and chronology, an OSS connection, or the
additional identifiers required for common names. No rejected employer,
occupation, unit, or institution is promoted to a public claim. All ten
identities remain unresolved with high-priority Box 16 guidance and the
evidence-limited employer statement.

## Page-ten Anderson-through-Andreasen pathways, Batch 086

`research/evidence-page-ten-anderson-through-andreasen-pathways_batch-086_2026-07-31.json`
records the minimum online protocol for ten contiguous rows from Stanley E.
Anderson through Knut Andreasen on PDF page ten. The bundle contains ten
person updates, ten terminal or carry-forward research attempts, fourteen
source records, two public claims, and five claim-source links. It creates no
new organization or affiliation because the new positive evidence establishes
an occupation but not a named employer or institutional relationship.

The index citations were visually checked against page ten. Common-name and
incomplete cases were searched through official/NARA context, CIA discovery,
exact-name and meaningful variant searches, employment and occupation queries,
newspaper or obituary paths, institutional sources, and archival leads.
Stanley E. Anderson, Tom L. Anderson, Walter Anderson, William M. Anderson,
Anna B. Andes, and George Andreas remain unresolved. Russell W. Anderton
remains ambiguous: a scholarly Gemological Institute of America article
documents a distinctive man's early-1940s gem work, but it does not link that
person to OSS or the indexed private identifier. Jean J. Andoire is probable
because the uncommon exact name appears in a contemporary Ninth Army roster
and the Ritchie Boys roster, but neither provides the index identifier or an
explicit OSS connection. These leads remain qualified identity-review notes,
not employer facts.

Edna W. Andrade's existing CIA- and Smithsonian-supported claims were reviewed
in place. The Hecht Company remains her strongly date-bounded immediate and
last civilian employer; Newcomb teaching remains earlier employment; and the
Pennsylvania Academy remains student status. No duplicate claim, affiliation,
organization, or citation was created.

Knut Andreasen's uncommon name and an exact private-identifier match connect
the NARA index row to an Operation Rype NORSO profile. Matthew T. Bolland's
published history independently identifies Corporal Andreasen in the same
mission context and states that he had been a first mate. The public profile
therefore reports a high-confidence occupation-only result. It does not infer
a vessel, shipping company, self-employment status, immediate predecessor, or
last civilian employer. The full identifier was compared privately and is not
stored in the evidence text, exposed in a citation, or emitted in public
assets. No authenticated NARA Catalog request or live API response was used or
retained.

## Page-ten Andreopoulos-through-Andrews archival pathways, Batch 087

`research/evidence-page-ten-andreopoulos-through-andrews-archival-pathways_batch-087_2026-07-31.json`
records the minimum online protocol for ten contiguous rows from Antony
Andreopoulos through Lewis W. Andrews Jr. on PDF page ten. The bundle contains
ten person updates, ten terminal research attempts, and ten official index
citations. It creates no organization, affiliation, claim, or claim-source
link because none of the reviewed candidates meets the identity and temporal
publication rules.

All ten index citations were visually checked against page ten. The research
protocol covered official/NARA context, CIA discovery, exact-name and
meaningful punctuation, suffix, diacritic, rank, and spelling variants,
employment and occupation searches, Library of Congress newspaper paths,
obituary or directory checks where applicable, institutional sources, and
archival leads. Common-name and no-rank cases were held to the enhanced
disambiguation rule. No authenticated NARA Catalog request was made and no
live API content was retained.

The source categories were not flattened. Andre Andreu remains foreign or
Allied military personnel because the printed row says French; `S/Lt` remains
preserved exactly and unexpanded pending Box 17 or French service-record
review. Ethel N. Andrew remains a CAF-3 civilian. Edward W. Andrews remains a
commissioned naval officer; Ernest F. and George H. Andrews remain
commissioned Army officers; Graydon L. and Lewis W. Andrews Jr. remain
enlisted Army personnel; and Antony Andreopoulos, Evelyn Andrews, and Horace
Andrews remain indeterminate because their rows print no rank or grade.

Search results included a Canadian printer and publisher, an insurance agent,
a carpet-industry employee, obituary and cemetery entries, genealogical
records, and modern people-finder results. None supplied the indexed private
identifier where one exists, an OSS or Box 17 link, compatible chronology, and
the additional corroborating identifiers required for these names. Modern
living-person details were excluded. No rejected employer, occupation,
organization, or assignment is promoted to a public claim, and full service
identifiers remain private.

## Page-ten/eleven Andrews-through-Andros pathways, Batch 088

`research/evidence-page-ten-eleven-andrews-through-andros-pathways_batch-088_2026-07-31.json`
records the minimum online protocol for ten contiguous rows from May E.
Andrews through Anthony N. Andros across PDF pages ten and eleven. The bundle
contains ten person updates, ten terminal research attempts, fourteen sources,
four normalized organizations, four published affiliations, seven published
claims, and twelve claim-source links.

All ten index rows were visually checked against the rendered PDF pages. The
seven unresolved records received official/NARA context, CIA discovery,
exact-name and meaningful punctuation, suffix, rank, and spelling variants,
employment and occupation searches, Library of Congress or regional newspaper
paths, obituary or directory checks, institutional research, and archival
searches. A Reuben K. Andrews Jr. directory entry, a William and Mary baseball
player named Virgil Andrews, a Chicago genealogy candidate for Anthony N.
Andros, and numerous common-name military, professional, obituary, and business
results lacked the indexed private identifier where one exists, an OSS or Box
17/18 connection, and the additional corroborating identifiers required for
publication. They remain rejected leads, not public claims.

Three high-confidence identities produce qualified historical pathways.
St. Paul's School's alumni memorial documents that Schofield Andrews Jr.
graduated from Harvard, enlisted in the Army in 1943, and was transferred to
OSS X-2. The Army is modeled as the immediate military affiliation; Harvard is
student status and is excluded from employer analytics. The Santa Barbara
News-Press obituary explicitly identifies Mortimer Andron's wartime OSS
service, while University of Illinois Board of Trustees records document his
1941-42 appointment as Assistant in Economics. That university role remains
`documented_prewar`, not immediate or last civilian, because the accessible
sources do not close the chronology. A CIA institutional historical paper says
SSU acquired Nicholas Andronovitch late in 1945 from his Army G-2 Military
Liaison Officer assignment in Jerusalem. Army G-2 is modeled as a military
assignment rather than a civilian employer.

The University of Illinois minutes' OCR misreads the counselor start year as
1947. The project does not silently reproduce that error: the 1941 meeting
date, June 1942 end date, surrounding appointments, and the separate 1941-42
staff register establish the academic-year context. No authenticated NARA
Catalog request was made, no API key was accessed, and no live NARA response
content was retained.

## Page-eleven Andros-through-Angelos archival pathways, Batch 089

`research/evidence-page-eleven-andros-through-angelos-archival-pathways_batch-089_2026-07-31.json`
records the minimum online protocol for ten contiguous rows from James H.
Andros through Anthony G. Angelos on PDF page eleven. The bundle contains ten
person updates, ten terminal research attempts, and ten official index
citations. It creates no organization, affiliation, claim, or claim-source
link because none of the reviewed candidates meets the identity and temporal
publication rules.

All ten index citations were visually checked against the rendered page. The
research protocol covered official/NARA context, CIA discovery, exact-name and
meaningful punctuation, middle-name, rank, and formal-given-name variants,
employment and occupation searches, Library of Congress or other contemporary
newspaper paths, obituary, cemetery, directory, military, institutional, and
archival checks where applicable. Common-name and no-rank cases were held to
the enhanced disambiguation rule. No authenticated NARA Catalog request was
made, no API key was accessed, and no live API content was retained.

Personnel categories remain separate from identity findings. Five rows remain
enlisted Army personnel, Joseph Angello remains a commissioned Army officer,
James B. Angell remains a P-7 civilian, and two blank-rank rows remain
indeterminate. Anthony G. Angelos's printed `S2 C` value is preserved in the
immutable source row while the documented normalization rule recognizes it as
the spacing variant `S 2/C`, classifying the row as enlisted naval personnel.
This rank normalization does not resolve his identity.

Rejected leads remain private research notes rather than public claims. They
include a World War II Army cemetery candidate for Frank J. Androvich, a 1956
Ford Motor Company directory entry for Andrew A. Anganes, a 1945
railroad-magazine reference to a staff sergeant Nick Angelo Jr., and the
University of Michigan president James B. Angell, who died in 1916. Each
lacked the indexed private identifier where one is printed, an OSS or Box 18
connection, compatible pre-OSS chronology, or the additional corroborating
identifiers required by the project rules. Privacy-sensitive modern data were
not retained. No rejected employer, occupation, organization, or assignment
is promoted to a public fact, and full service identifiers remain private.

## Page-eleven Angelos-through-Angulo pathways, Batch 090

`research/evidence-page-eleven-angelos-through-angulo-pathways_batch-090_2026-07-31.json`
records the minimum online protocol for ten contiguous rows from Michael T.
Angelos through Manuel R. Angulo on PDF page eleven. It also updates the
confirmed page-three Peter M. Aglione entity solely to expose a possible
duplicate relationship with the newly reviewed Peter M. Anglione row. The
bundle contains eleven person updates, ten durable research attempts, sixteen
sources, three normalized organizations, four published affiliations, seven
published claims, and eleven claim-source links.

All ten page-eleven index citations were visually checked against the rendered
PDF. A National Park Service institutional history identifies Petty Officer
Michael Angelos of Chicago as a Navy demolitions specialist trained for OSS
service. The uncommon name, naval petty-officer status, and direct OSS context
support a high-confidence identity, but the source does not print the index
middle initial or private identifier and does not establish a pre-OSS
affiliation. A Denver Public Library 10th Mountain Division name index lists
the exact uncommon name Bert W. Anger, and a 1929 official Senate document
lists Frank E. Anglim among Bureau of Prohibition field personnel. Both remain
probable review candidates: neither source supplies an OSS or Box 18 link,
matching identifier, or chronology sufficient for a public affiliation claim.

The May 4, 1944 OSS board report held by the Hoover Institution identifies
Private Damiano Angione with the unique private identifier printed for
`Damiamo Angione` in the NARA index. The project preserves `Damiamo` as the
immutable indexed spelling and adds `Damiano` only as a documented variant.
The same direct report records Army entry and infantry training before explicit
OSS recruitment, so United States Army service is published as the immediate
military affiliation. The report does not identify a civilian employer.

A 78-page digitized direct OSS personnel file for James Hugh Angleton was
reviewed page by page where relevant. The official employment history records
continuous National Cash Register Company employment from February 1922 and
senior responsibility in Italy; NCR is therefore published as the confirmed
last civilian employer before military service. An official personnel-history
card records release from the Army School of Military Government in
Charlottesville and assignment to OSS Washington on July 26, 1943, establishing
the immediate pre-OSS military assignment. The American Chamber of Commerce
for Italy is separately modeled as a professional affiliation, not employment.
The digitized file is cited through its stable Internet Archive item page; the
PDF itself is not committed or republished, and private identifiers remain
excluded from all public claims and downloads.

The adjacent First Lieutenant James Angleton profile passed a carry-forward
integrity review. Its prior `verified_employer_found` status was incorrect
because the published record documents Army and student affiliations rather
than employment; the status is now `completed` without changing or removing
the supported claims. James Angleton and James H. Angleton remain distinct
person entities.

The Box 18 Peter M. Anglione row is not silently merged with the confirmed Box
5 Peter M. Aglione row. Both now carry the same review-only possible-duplicate
group, while the public projection replaces the private group label with an
opaque value. The rows retain their different indexed spelling, rank,
identifier, box, source-record ID, and archival instructions. Nicholas A.
Angelos, Carlos J. Angulo, and Manuel R. Angulo remain unresolved after
official/NARA context, CIA Reading Room discovery, exact-name and meaningful
variant, employment/occupation, obituary/directory/newspaper, institutional,
and archival searches.

No authenticated NARA Catalog request was made, no API key was accessed, and
no live NARA API content was retained. The direct OSS personnel-file download
used for visual review remained temporary and is not a repository artifact.

## Page-eleven Ankeny-through-Anthony pathways, Batch 091

`research/evidence-page-eleven-ankeny-through-anthony-pathways_batch-091_2026-07-31.json`
records the minimum online protocol for ten contiguous rows from Richard J.
Ankeny through Kelly Anthony on PDF page eleven. The bundle contains ten person
updates, ten durable research attempts, fifteen sources, two normalized
organizations, two published affiliations, four published claims, and ten
claim-source links.

All ten index citations were checked against the rendered PDF page. The
research protocol covered NARA and CIA context, exact-name and meaningful
initial, rank, spelling, and punctuation variants, employment and occupation
searches, Library of Congress and other contemporary newspaper paths,
institutional records, obituaries, directories, military records, and archival
checks as applicable. Incomplete and common-name records were not resolved from
name matches alone.

An official declassified OSS European Theater order confirms Robert M.
Anstett's identity through exact name, compatible first-lieutenant rank, branch,
and a unique service identifier retained only in the private database. The
order confirms wartime OSS context but does not document his transfer
chronology or civilian employment. The Coast Artillery Corps entry is therefore
used for identity resolution only and is not published as an immediate pre-OSS
affiliation.

Two contemporary 1943 Cornell Alumni News notices and a Cornell institutional
alumni history support Bertel W. Antell as a high-confidence identity. The
January notice directly names The Chemical Construction Co. and describes his
personnel-director role in the past tense while documenting his then-current
Naval officer training. Chemical Construction Company is published as the
strongly date-bounded last civilian employer, without inventing an employment
end date or substituting its parent company as the employer. The Naval Training
School at Cornell is separately published as a medium-confidence, probable
immediate pre-OSS military assignment because the accessible sources do not
give the exact Navy-to-OSS transfer date or exclude intervening duty.

A 1952 official U.S. Geological Survey report names a postwar scientist Charles
Annell and supports a probable identity lead for the indexed Charles S. Annell.
It does not supply a wartime identifier, Box 19 link, OSS chronology, or
pre-OSS employment evidence, so no public affiliation claim is created.
Richard J. Ankeny, Dorothy S. Annan, Jayne L. Annis, Juliet K. Ansperry, Earl
K. Anthony, Fred D. Anthony, and Kelly Anthony remain unresolved after the
minimum protocol. All nine profiles other than Antell route to targeted Box 18
or Box 19 review.

The printed `Lt CMD` value for Antell remains unchanged in the immutable source
record. The tested normalization vocabulary now recognizes both `Lt CMD` and
`Lt Cmdr` as lieutenant-commander variants and classifies those rows as
commissioned naval officers. This classification change does not itself resolve
an identity or establish an affiliation.

No authenticated NARA Catalog request was made, no API key was accessed, and
no live NARA API content was retained. Temporary source downloads used for
page-level verification were deleted and were not committed.

## Page-eleven Anthony-through-Antonakis pathways, Batch 092

`research/evidence-page-eleven-anthony-through-antonakis-pathways_batch-092_2026-07-31.json`
records the minimum online protocol for ten contiguous rows from Robert
Anthony through James Antonakis on PDF page eleven. Direct OSS roster evidence
confirms Charles P. Antinopoulos and James M. Antonakis, while exact-name
roster and unit-history evidence supports Peter G. Anton at high confidence.
All three are published with strongly date-bounded 122nd Infantry Battalion
(Separate) pathways. The unit is modeled as a military assignment, and none is
assigned a civilian employer.

Alan A. Antik remains a probable postwar film-technician identity lead whose
sources do not establish an OSS personnel-file link or pre-OSS chronology.
Robert Anthony, James Anthony, John S. Anthony, Kelly Anthony, Stanley J.
Antosh, and John J. Antonetti remain unresolved after the minimum protocol.
Seven profiles route to Box 19 review. No authenticated NARA Catalog request
was made, no API key was accessed, and no live API content was retained.

## Page-eleven-and-twelve Antonelli-through-Apkarian pathways, Batch 093

`research/evidence-page-eleven-twelve-antonelli-through-apkarian-pathways_batch-093_2026-07-31.json`
records the minimum online protocol for ten contiguous rows from Charlote
Antonelli through Antranig Apkarian across PDF pages eleven and twelve.
Anargyros Antonopoulos has a high-confidence OSS roster match and a strongly
date-bounded 122nd Infantry Battalion pathway. Rudolf Anzbock has a confirmed
identity and strongly date-bounded 85th Mountain Infantry Regiment pathway
before OSS transfer.

Ivo Antunovic has a high-confidence identity and documented merchant-sea
captain occupation. The evidence names a vessel but not a civilian employer,
so the project publishes occupation-only status. His Yugoslav Seamen's Club
relationship is separately qualified as a professional affiliation. Dominic
J. Anzevino, Zumruth Apcar, and Antranig Apkarian remain probable identities
without published employer claims; Charlote Antonelli, Anthony Antony, Kukuji
Aoki, and Harry E. Apaar remain unresolved. Temporary source PDFs used for
visual inspection were not committed or republished.

## Page-twelve Apolito-through-Applebaum pathways, Batch 094

`research/evidence-page-twelve-apolito-through-applebaum-pathways_batch-094_2026-07-31.json`
records the minimum online protocol for ten contiguous rows from George F.
Apolito through William Applebaum on PDF page twelve. All ten index citations
were visually checked against the rendered page. The bundle contains ten
person updates, ten durable research attempts, twenty-one sources, four
normalized organizations, six published affiliations, fourteen published
claims, and thirty-four claim-source links.

A declassified May 4, 1944 OSS board proceeding confirms that the indexed
Rache S. Apostoi is the documented Rache S. Apostol. It directly dates Army
entry to September 1942 and OSS assignment to September 1943, so United States
Army service is published as the explicit immediate military affiliation.
The same proceeding adds occupation-only evidence that Ivo Antunovic
immediately preceded OSS as a captain in Yugoslavia's merchant marine; it does
not name his employer. Private identifiers used for resolution are excluded
from the evidence bundle's public excerpts and generated site.

Direct OSS roster evidence and independent unit histories support Jerry
Apostolatos and James M. Apostolopoulo, preserving their indexed names while
adding Gerasimos Apostolatos and James M. Apostolopoulos as documented
variants. Each receives a strongly date-bounded 122nd Infantry Battalion
(Separate) military pathway and no civilian-employer claim. George F. Apolito
remains only a probable match to a Lafayette-team roster entry because the
accessible record omits his middle initial and other corroborating identifiers.

An obituary and contemporary professional evidence support Leonard Appel at
high confidence. His immediate United States Army assignment is modeled
separately from his last civilian employment at the National Labor Relations
Board. An official Marine Corps history, a declassified OSS personnel notice,
and a contemporary marketing article support William Applebaum at high
confidence. Economy Grocery Stores Corporation is preserved as his historical
employer name and is documented as both his immediate pre-OSS affiliation and
last civilian employer. Stop & Shop appears only as a sourced historical-name
relationship, not as a substituted employer.

Garcia E. Aponte, Timothy Apostolos, Donald A. Appetrad, and Harold N.
Applebaum remain unresolved after the minimum protocol and route to Box 20
review. No authenticated NARA Catalog request was made, no API key was
accessed, and no live NARA API content was retained. Temporary source
downloads used for page-level inspection were not committed.

## Page-twelve Applegate-through-Arbucci pathways, Batch 095

`research/evidence-page-twelve-appleton-through-arbucci-pathways_batch-095_2026-07-31.json`
records ten visually checked, contiguous PDF-page-twelve rows from Rex
Applegate through Louis F. Arbucci. The bundle contains nine person updates,
ten durable research attempts, and nine official personnel-index citations.
It adds no organization, affiliation, or employment claim.

Rex Applegate's already published high-confidence United States Army Military
Police pathway received a new integrity review and remains unchanged. John B.
Appleton, Margaret E. Appleton, Sabri Appolini, Carlo E. Aprato, Helene A.
Apt, Samuel P. Aquilina, Joseph J. Aquino Jr., Pedro J. Aquirre, and Louis F.
Arbucci remain unresolved after the minimum online protocol and route to the
indexed Box 20 files. A rare-name wartime candidate was inspected in direct
source context and rejected because it did not establish that it described
the indexed OSS person or a pre-OSS employer; sensitive, irrelevant details
from that lead were not published.

The printed `Caf-3`, `Sgt USM`, `Pvt`, `2nd Lt`, and `T-5` strings remain
recoverable. `Sgt USM` is not expanded or forced into a category without
support. The index spelling Aquirre is preserved, while Aguirre is recorded
only as a search variant. No authenticated NARA Catalog request was made, no
API key was accessed, and no live NARA API content was retained. Temporary
source downloads and PDF inspection crops were not committed or republished.

## Page-twelve Arcaro-through-Archuleta pathways, Batch 096

`research/evidence-page-twelve-arcaro-through-archuleta-pathways_batch-096_2026-07-31.json`
records ten visually checked, contiguous PDF-page-twelve rows from Carmela E.
Arcaro through Eugene F. Archuleta. The bundle contains ten person updates,
ten durable research attempts, fourteen source records, three organizations,
three affiliations, five claims, and eleven claim-source links.

John D. Archbold is confirmed by the uncommon name, matching middle initial
and lieutenant-junior-grade rank, Naval Reserve status, and direct OSS
Maritime Unit evidence in U.S. Army Special Operations history. Clemson
University Libraries' John D. Archbold Papers finding aid independently
expands the middle name to Dana, documents his Navy and OSS service, and
records his purchase and agricultural operation of Springfield Plantation in
Dominica beginning in 1935. The public model therefore keeps United States
Naval Reserve service as a strongly date-bounded immediate military pathway
and Springfield as a separate, strongly date-bounded last civilian
self-employment affiliation. Neither source supplies the exact Navy entry or
OSS attachment date, so the temporal claims remain high rather than
confirmed.

Anthony A. Archuleta Jr. is confirmed by the exact indexed name, suffix, and a
unique service identifier retained only in the private database. A
NARA-derived Army-enlistment transcription records entry from `Civil Life` in
1942, and a separate Fort Bliss National Cemetery transcription corroborates
the expanded middle name Aaron and World War II Army service. The Army
pathway is published as strongly date-bounded; `Civil Life` remains a source
status and is not converted into an employer, occupation, or organization.
The exact Army-to-OSS transition date and civilian livelihood still require
Box 20 review.

Carmela E. Arcaro, Alford Archer, Flton W. Archer, Harold F. Archer, Raymond
Archer, William L. Archer, Robert Archibald, and Eugene F. Archuleta remain
unresolved after the staged official-context, CIA, exact-name OSS,
employment/occupation, obituary, institutional, newspaper, archival, and
Library of Congress protocol. The same-name Ohio State geography candidate
for Alford Archer was rejected because a name match alone does not link that
person to OSS. `Flton` was visually confirmed as the printed index form;
Fulton and Elton were tested only as search expansions and were not accepted
as corrections. An incompatible Canadian naval namesake for William L.
Archer was also rejected. All eight profiles retain dignified unresolved
pages and targeted Box 20 guidance.

No authenticated NARA Catalog request was made, no API key was accessed, and
no live NARA API response was retained. The PDF page render used for visual
inspection was removed after review. No full service identifier appears in
the evidence bundle or public projection.

## Page-twelve Arden-through-Arida pathways, Batch 097

`research/evidence-page-twelve-arden-through-arida-pathways_batch-097_2026-07-31.json`
records ten visually checked, contiguous PDF-page-twelve rows from Oliver W.
Arden through Edward Arida. The bundle contains ten person updates, ten
durable research attempts, nineteen source records, five organizations, five
affiliations, eight claims, and nineteen claim-source links.

Phillip J. Arengi is confirmed through the exact indexed name and middle
initial, matching Technical Sergeant rank, and an Italian Operational Group
Simcol mission roster whose compiler identifies the underlying NARA RG 226,
Entry 143, Box 9 reports. A Rochester *Democrat and Chronicle* obituary
independently corroborates OSS service. A contributor-maintained Army
directory supplies only a qualified 1940 Army starting point, so the immediate
Army pathway is medium confidence and strongly date-bounded rather than a
confirmed exact Army-to-OSS transfer. No civilian employer is asserted, and
the underlying mission reports remain an archival-review target.

Conrad Arensberg is a high-confidence identity. The Smithsonian National
Anthropological Archives finding aid, based partly on his curriculum vitae,
documents an MIT assistant professorship in 1938–1941, Brooklyn College
associate professorship and department chairmanship in 1941–1946, and Army
military-intelligence service in 1943–1946. Columbia University and the
Association for Cultural Equity independently corroborate the academic and
wartime chronology. Brooklyn College is therefore modeled as the
strongly-date-bounded last civilian employer and MIT as earlier documented
prewar employment. The exact significance of the indexed `WAE` grade and the
administrative transition into OSS still require the Box 21 file.

Lemonis J. Argyropais is high-confidence from two contemporary Clark
University geography newsletters. The 1941 issue identifies a graduate
student from Limni-Euboea who had graduated from the University of Athens; the
1945 issue places the same uncommon name in the OSS Topographic Mapping
Section. Clark is a qualified probable-immediate student affiliation, not an
employer, and the University of Athens remains an earlier student
relationship. The 1945 newsletter prints an M.A. date of 1942, while Clark's
later thesis index places the thesis under 1943; the discrepancy is preserved
rather than harmonized.

Oliver W. Arden, Joseph F. Ardinger, John G. Ardon, Julius Arensteim, Florence
T. Arft, Christian A. Argyris, and Edward Arida remain unresolved after the
staged official-context, CIA, exact-name OSS, employment/occupation, obituary,
institutional, newspaper, archival, and Library of Congress protocol. The
printed Arensteim spelling and unfamiliar `SP PS 1/` grade remain unchanged;
Arenstein and Arnstein are search aliases only. The well-known scholar Chris
Argyris was rejected because Yale's biography describes a Signal Corps second
lieutenant, conflicting with the indexed captain rank, and supplies no OSS or
other indexed-identifier link. All seven unresolved profiles retain targeted
Box 20 or Box 21 guidance.

No authenticated NARA Catalog request was made, no API key was accessed, and
no live NARA API response was retained. The PDF page render used for visual
inspection was removed after review. No full service identifier appears in
the evidence bundle or public projection.

## Page-thirteen Arlotta-through-Armer pathways, Batch 098

`research/evidence-page-thirteen-arlotta-through-armer-pathways_batch-098_2026-07-31.json`
records ten visually checked, contiguous PDF-page-thirteen rows from
Salvatoroe Arlotta through John E. Armer. The bundle contains ten person
updates, ten durable research attempts, seventeen source records, two
organizations, two affiliations, six claims, and seventeen claim-source
links.

Edward W. Arluck is a high-confidence identity. Louise E. Hoffman's
peer-reviewed history of the OSS Psychology Division names Edward W. Arluck
among its psychologists by autumn 1941. The University of Bern's Rorschach
Archives bibliography expands the rare name as Edward Wiltcher Arluck and
records a 1941 Columbia University psychology study; the University of
Pennsylvania Libraries' Online Books Page classifies the work as a
dissertation. Columbia is therefore modeled only as a medium-confidence,
probable-immediate student affiliation. It is not an employer claim, and the
file must still confirm the full name, indexed enlisted rank, and transition
into OSS.

Raymond Armandi is confirmed through an exact uncommon-name, matching-rank,
and direct-OSS convergence. A *Daily Bulldog* obituary explicitly states that
he joined the Army in March 1943 and was then selected for OSS because of his
French and Italian; a veteran-compiled Spokane/Sewanee roster independently
lists Technician Fifth Grade Raymond Armandi. The Army is modeled as his
explicit immediate military pathway. The same obituary gives a 43-year
International Paper career without dates, so that company is not classified
as pre-OSS employment.

Andrew Roy Armentor is confirmed by the exact uncommon expanded name, the
indexed middle initial, a funeral-home obituary identifying an Army Staff
Sergeant in OSS commandos, and an Operational Groups PEG roster. The roster
prints T/3 rather than Staff Sergeant; the difference is preserved for
archival review and is not silently harmonized. The obituary's undated
Armentor's Service Center ownership is not converted into a pre-OSS employer.
John E. Armer is high-confidence from an exact initials, uncommon-surname,
Corporal-rank, and direct-OSS roster match in the Chinese Operational Group's
BANANA commando. The roster does not expand his first name or reproduce the
private identifier, so the match remains short of confirmed. Neither Armentor
nor Armer receives a pre-OSS affiliation claim from sources that document
only OSS service.

Salvatoroe Arlotta, Joseph O. Armandariz, Virgile C. Armaos, Mary C. Armato,
William E. Armband, and George E. Armbruster remain unresolved after the
staged official-context, CIA, exact-name OSS, employment/occupation, obituary,
institutional, newspaper, archival, and Library of Congress protocol. The
visually verified `Salvatoroe`, `Armandariz`, `Armband`, and `cPL` forms remain
unchanged; Salvatore and Armendariz were used only as search aliases. All six
profiles retain targeted Box 21 guidance.

No authenticated NARA Catalog request was made, no API key was accessed, and
no live NARA API response was retained. The PDF page render used for visual
inspection was removed after review. No full service identifier appears in
the evidence bundle or public projection.

## Page-thirteen Armistead-through-Howard-Armstrong pathways, Batch 099

`research/evidence-page-thirteen-armistead-through-howard-armstrong-pathways_batch-099_2026-07-31.json`
records ten visually checked, contiguous PDF-page-thirteen rows from M. E.
Armistead through Howard H. Armstrong. The bundle contains ten person updates,
ten durable research attempts, fourteen source records, five organizations,
five affiliations, six claims, and ten claim-source links.

Lester Armour is confirmed by the uncommon exact name, indexed Captain rank,
a reproduced War Department award citation naming him as a United States Navy
captain serving with OSS in the European Theater, and Hoover Institution
records documenting his 1942-1943 naval intelligence training. A contemporary
Field Museum report records his imminent early-1942 return to active service
under a Navy reserve commission. The United States Navy is therefore modeled
as the strongly date-bounded immediate pathway, not as a civilian employer.

A FRASER copy of a 1963 banking-industry career retrospective documents Armour
& Co. employment from 1918 through 1934, General Stockyards chairmanship from
1935 through 1940, and a City National directorship beginning in 1937. The
company employment is medium-confidence documented-prewar work rather than a
last-civilian-employer claim. The chairmanship and directorship remain
professional affiliations because the source does not establish salaried
employment. The Field Museum's own 1941 report documents Armour's trusteeship,
which is likewise modeled as a professional affiliation. The pre-existing Field
Museum authority record is reused, preserving the institution's 1943-1966
historical name without creating a duplicate organization.

M. E. Armistead, Stanley N. Armitage, Albert L. Armstrong, Claude C. Armstrong
Jr., Delton V. Armstrong, Elizabeth H. Armstrong, Frank E. Armstrong, Herbert
E. Armstrong Jr., and Howard H. Armstrong remain unresolved after staged
official-context, CIA, exact-name OSS, employment/occupation, obituary,
institutional, newspaper, archival, and Library of Congress checks. Common-name
biographical and inventor candidates lacked the corroborating indexed
identifiers required for publication. All nine profiles retain targeted Box 21
guidance.

No authenticated NARA Catalog request was made, no API key was accessed, and
no live NARA API response was retained. The PDF page render used for visual
inspection was removed after review. No full service identifier appears in the
evidence bundle or public projection.

## Page-thirteen Armstrong-through-Arnberg pathways, Batch 100

`research/evidence-page-thirteen-armstrong-through-arnberg-pathways_batch-100_2026-07-31.json`
records ten visually checked, contiguous PDF-page-thirteen rows from James H.
Armstrong through George C. Arnberg. James H. Armstrong's 19th Weather
Squadron is published as a qualified immediate military pathway; Sinclair
Armstrong's 1941 Isham, Lincoln & Beale work is documented earlier employment;
and Claude G. Arnault's French Army connection is a high-confidence immediate
military affiliation. The remaining names route to Box 21 or 22. The bundle
retains the printed naval grade and rejects a plausible Arnberg bomber-group
namesake because direct OSS linkage is absent.

## Page-thirteen Arndt-through-Arnold pathways, Batch 101

`research/evidence-page-thirteen-arndt-through-arnold-pathways_batch-101_2026-07-31.json`
records ten visually checked, contiguous PDF-page-thirteen rows from Clifford
H. Arndt through Harry K. Arnold. Alf G. Arnesen is confirmed across the NARA
index, Denver Public Library unit index, and an official OSS special order;
his Company D, 99th Infantry pathway remains medium-confidence because the
individual transfer sequence is not explicit. Maynard C. Arney is a probable
identity without a promoted affiliation. Reider Arnesen's conflicting unit
candidate remains rejected, and the printed `possibly` note remains literal.
All unresolved profiles route to Box 22.

## Page-thirteen/fourteen Arnold-through-Arnone pathways, Batch 102

`research/evidence-page-thirteen-fourteen-arnold-through-arnone-pathways_batch-102_2026-07-31.json`
records ten visually checked, contiguous rows from Howard W. Arnold on PDF page
13 through Raymond Arnone on PDF page 14. The suffix in `Wilfred, Jr.`, the
hyphenated Arnold-Baker surname, the literal `British A` note, blank rank
fields, and the Box 22-to-23 transition were checked against rendered source
pages. The bundle contains ten person updates, thirteen source records, one
organization, one affiliation, two claims, seven claim-source links, and ten
durable research attempts.

A 5 March 1943 issue of *YANK, The Army Weekly* was inspected at its cover,
article title page, and printed page 21. Sgt. Bill Davidson's “They Fight with
Film” places Major Francis Arnoldy in the Army Film Branch, Special Service
Division, as technical adviser on Russian films. The article does not state
that Arnoldy belonged to the 834th Signal Company, so the project does not
merge his assignment into that unit. Nikolina Kurtovic's 2010 University of
Toronto dissertation was inspected at printed page 35, PDF page 53; it dates
Arnoldy's OSS Yugoslav Desk leadership from December 1943 to July 1944. A
Hoover Institution archival index independently aligns the exact name, Major
rank, and Bari station. These sources support a high-confidence identity and a
medium-confidence probable-immediate Army Film Branch pathway, not an explicit
transfer and not a civilian-employer claim.

The other newly attempted Arnold and Arnone rows remain unresolved after
official-context, CIA Reading Room, exact-name OSS, employment/occupation,
obituary, directory, newspaper, institutional, archival, and Library of
Congress checks. A later Colonel Wilfred Arnold Jr. and a same-name Army Air
Forces lieutenant were rejected pending direct identifiers. Richard G.
Arnold-Baker's existing evidence was sequentially re-audited without changing
his high-confidence identity or qualified Intelligence Corps affiliation.

No authenticated NARA Catalog request was made, no API key was accessed, and
no live NARA API response was retained. Temporary source PDFs, text
extractions, and page renders were used only for inspection and removed after
review. No full service identifier appears in the evidence bundle or public
projection.

## Page-fourteen Arnston-through-Arrington pathways, Batch 103

`research/evidence-page-fourteen-arnston-through-arrington-pathways_batch-103_2026-07-31.json`
records ten visually checked, contiguous PDF-page-fourteen rows from Anetta S.
Arnston through Mabel I. Arrington. The literal civilian grades, Army ranks,
blank rank fields, Bernard Aronson's `SP P 2/c` rating, Box 23, and archive
location were checked against the rendered source page. The bundle contains
ten person updates, fourteen source records, one organization, one affiliation,
three claims, nine claim-source links, and ten durable research attempts.

Matteo Paglia's 2024/2025 University of Genoa master's thesis was inspected at
its title page and printed/PDF pages 139-140. Its Operation Ginny I roster,
attributed to Fondo Albert Materazzi, Busta 1, Fascicolo 8 at ISRAL, lists Sgt
Carmine Aromando on the relief team for the 27-28 February 1944 mission. The
uncommon exact name, matching Sergeant rank, and direct OSS mission context
support a high-confidence identity. Because the roster describes service
inside OSS, it does not support any pre-OSS affiliation or civilian employer.

A 13 July 2007 *Journal News* obituary states that Bernard Aronson served in
the Navy during World War II and was later assigned to OSS because of his
photographic knowledge. Naval History and Heritage Command references identify
Sp(P) as Specialist (Photographic) and date the wartime rating to 1942-1943.
Those sources align with the literal index rating and support a high-confidence
identity plus a medium-confidence probable-immediate Navy pathway. The project
does not infer a formal transfer date or a last civilian employer, and the raw
rating remains recoverable.

The other eight profiles remain unresolved after official-context, CIA Reading
Room, exact-name OSS, employment/occupation, obituary, directory, newspaper,
institutional, archival, and Library of Congress checks. Maryland death-index
candidates for Anetta S. Arnston and Emanuel L. Aronhime and sibling-veteran
candidates for Burton and John E. Arrington are preserved only as rejected
leads. A relative is not used as the principal identity basis. Irrelevant
sensitive later-life material encountered for an Ernest G. Arons namesake was
neither retained nor used.

No authenticated NARA Catalog request was made, no API key was accessed, and
no live NARA API response was retained. Temporary source PDFs, text
extractions, and page renders were used only for inspection and removed after
review. No full service identifier appears in the evidence bundle or public
projection.

## Page-fourteen Arrington-through-Aserinsky pathways, Batch 104

`research/evidence-page-fourteen-arrington-through-aserinsky-pathways_batch-104_2026-07-31.json`
records ten visually checked, contiguous PDF-page-fourteen rows from Mable O.
Arrington through Eugene Aserinsky. The literal `Caf-4`, `CPC-2`, `SP-7`,
Sergeant, Technician Sergeant, Private, and blank rank cells, together with Box
23 and the printed archive locations, were checked against the rendered source
page. The bundle contains ten person updates, twenty sources, five
organizations, six affiliations, eleven claims, twenty-six claim-source links,
and ten durable research attempts.

The official 1944 OSS board proceeding in the Millard Preston Goodfellow papers
confirms Buford B. Arrowood through his exact uncommon name, matching private
identifier, Sergeant context, and person-specific chronology. It states that
OSS obtained him from Headquarters, USAFIME, and that he came to OSS in February
1944. NARA's Record Group 497 guide supplies the historical expansion, U.S.
Army Forces in the Middle East. The interview separately records rayon-mill
work before Army entry in February 1941. The unnamed mill is not normalized to
an organization or presented as a proved last civilian employer.

The Science History Institute's oral history with Willard C. Asbury documents
Standard Oil Development Company employment in 1940-41 and research-management
work from 1941 through 1947, together with wartime Washington and Strategic
Bombing Survey duties. A 1940 patent independently corroborates his exact name,
London location, technical work, and Standard Oil assignee. The employment is
published as documented prewar work, not as immediate, because the available
sources do not establish Asbury's OSS entry date or exclude concurrent company
employment.

Two consistent biographies support Eugene Aserinsky at high identity
confidence. They sequence Brooklyn College, transfer to the University of
Maryland, wartime Army entry, and high-explosives work in England. Army service
is therefore published only as a medium-confidence probable-immediate military
pathway; the colleges remain student affiliations and are excluded from
employer analytics. Paul E. Arther's exact-name dental and municipal service
records support a high-confidence identity but no predecessor claim. The
plausible Anita Arrow Summers candidate remains a withheld low-confidence lead,
and the other evidence-limited names remain unresolved pending Box 23 review.

No authenticated NARA Catalog request was made, no API key was accessed, and
no live NARA API response was retained. Temporary source PDFs, text
extractions, and page renders were used only for inspection and removed after
review. No full service identifier appears in the evidence bundle or public
projection.

## Page-fourteen Ash-through-Ashcraft pathways, Batch 105

`research/evidence-page-fourteen-ash-through-ashcraft-pathways_batch-105_2026-07-31.json`
records ten visually checked, contiguous PDF-page-fourteen rows from Charles H.
Ash through John J. Ashcraft Jr. The literal `Caf-6`, `T-4`, `Caf-4`, `Maj`,
`Pfc`, `Pvt`, `1st Lt`, and blank rank cells, together with Box 23 and the
printed archive locations, were checked against the rendered source page. The
unusual printed `Ashcraft, John, Jr., J.` field order and `Mckinley`
capitalization remain recoverable. The bundle contains ten person updates, ten
official index sources, no organizations, affiliations, or claims, and ten
durable research attempts.

All ten people remain unresolved after the complete terminal research protocol.
The searches covered official NARA context, CIA Reading Room, exact indexed
spellings and meaningful variants, military or civilian-grade clues,
employment and occupation, obituaries, directories, newspapers, institutional
archives, and Library of Congress discovery. The public profiles therefore say
that no reliable pre-OSS employer has yet been identified in the accessible
sources reviewed and direct researchers to Box 23; they do not imply that no
prior employment existed.

Two especially tempting namesakes were rejected rather than merged. The
dentist Major McKinley Ash Jr. has Major as his documented given name,
McKinley as his middle name, and an enlisted World War II grade incompatible
with the indexed given name Mckinley and rank Major. John W. Ashcraft Jr. has a
different middle initial and died in 1929; John Marion Ashcraft Jr. also has a
different middle name. Lyle, Lylle, and Lillie were used only as marked search
aliases for Lylie H. Ashby and were not treated as corrections.

No authenticated NARA Catalog request was made, no API key was accessed, and
no live NARA API response was retained. Temporary text extracts and the page
render were used only for inspection and removed after review. No full service
identifier appears in the evidence bundle or public projection.

## Page-fourteen Ashcraft-through-Ashworth pathways, Batch 106

`research/evidence-page-fourteen-ashcraft-through-ashworth-pathways_batch-106_2026-07-31.json`
records ten visually checked, contiguous PDF-page-fourteen rows from Wanda T.
Ashcraft through James M. Ashworth. The two adjacent Ashcraft rows, the printed
single-`l` spelling `Wiliam B. Asher`, Army ranks, civilian `P-1` grade, blank
rank and identifier cells, Box 23-to-24 transition, and archive location were
checked against the rendered source page. The bundle contains ten person
updates, sixteen sources, five organizations, five affiliations, seven claims,
twenty claim-source links, and ten durable research attempts.

Ira Ashley is confirmed through three mutually reinforcing contemporary or
near-contemporary sources. *Broadcasting* records his resignation as a
Lambert & Feasley producer-director effective 1 November 1942, later identifies
him as a private completing Army basic training at Keesler Field, and reports
his return from OSS duties in London in December 1945. Egon Larsen's 1985
eyewitness account identifies Second Lieutenant Ira Ashley as his OSS contact
in London in April 1944. The Army pathway is therefore published only as a
medium-confidence probable-immediate military assignment: the chronology is
strong, but no transfer order was found. Lambert & Feasley is the last named
civilian employer. Ashley's later Stage Door Canteen producing work is retained
separately as a professional affiliation because the source names a program,
not an employing organization.

Mark Ashin remains a probable identity. University of Chicago's institutional
obituary states that he joined its faculty in 1942 and left shortly afterward
for wartime service. Official Michigan State Board minutes appoint Mark Ashin
as an English instructor effective 1 September 1939. The uncommon exact name
and compatible chronology support qualified medium-confidence claims, but no
reviewed source directly links the institutional biography to the OSS index
row. University of Chicago is modeled as the strongly date-bounded last
civilian employer before military service; Michigan State College remains
earlier documented employment. Both are excluded from default verified-
employer analytics because the identity is probable rather than confirmed or
high confidence.

Wanda T. Ashcraft, William C. Ashcraft, Wiliam B. Asher, Alfred B. Ashley,
Belva L. Ashley, Richard Ashley, Margaret Ashton, and James M. Ashworth remain
unresolved after official-context, CIA Reading Room, exact-name OSS,
employment/occupation, obituary, directory, newspaper, institutional,
archival, NARA, and Library of Congress checks. An Alfred Ashley Silver Star
namesake, an unsourced Belva Lorraine Ashley genealogy candidate, and a
Margaret Ashton suffragist who died in 1937 were rejected rather than merged.
`William B. Asher` remains only a marked search alias and is not adopted as a
correction of the index.

All cited PDF pages were rendered and visually inspected. No authenticated
NARA Catalog request was made, no API key was accessed, and no live NARA API
response was retained. Temporary PDFs, text extractions, and page renders were
used only for inspection and removed after review. No full service identifier
appears in the evidence bundle or public projection.

## Page-fourteen-and-fifteen Askew-through-Aste pathways, Batch 107

`research/evidence-page-fourteen-and-fifteen-askew-through-aste-pathways_batch-107_2026-07-31.json`
records ten visually checked, contiguous rows from Leo G. Askew through John
Aste across PDF pages fourteen and fifteen. Raw spellings, initials, suffix,
ranks, Box 24, blank fields, and the page transition were checked against the
rendered source pages. The bundle contains ten person updates, thirteen
sources, two organizations, two affiliations, five claims, and ten durable
research attempts.

Monroe P. Askins is high-confidence through the exact name, matching Chief
Photographer's Mate rating, and contemporary evidence placing him in John
Ford's Field Photo unit. Because that unit was already part of OSS, it supports
identity and occupation but is not modeled as a pre-OSS predecessor. Gerard R.
Asselin remains probable. His obituary documents earlier H. P. Hood & Sons
employment, but it also names two other undated jobs and supplies no Army-entry
date; Hood therefore appears only as qualified earlier employment, not as the
immediate affiliation or last civilian employer.

Jean R. Assemat is confirmed by the official French military record that links
his indexed identity, documented Jacques Bauer alias, BCRA service, and
Jedburgh assignment. The Bureau Central de Renseignements et d'Action is
published as an explicit immediate military assignment rather than a civilian
employer. Leo G. Askew, Milton C. Askew, A. W. Asmuth Jr., Lea T. Aspinwall,
James D. Assaf, Graziella Asselin, and John Aste remain unresolved after the
terminal protocol and route to Box 24 review.

No authenticated NARA Catalog request was made, no API key was accessed, and
no live NARA API response was retained. Temporary PDFs, page renders, and text
extracts were used only for inspection and removed after review. No full
service identifier appears in the evidence bundle or public projection.

## Page-fifteen Atherton-through-Atkisson pathways, Batch 109

`research/evidence-page-fifteen-atherton-through-atkisson-pathways_batch-109_2026-07-31.json`
records ten visually checked, contiguous rows from David Atherton through
Kathryne J. Atkisson on PDF page fifteen. Raw spellings, initials, ranks,
service-number presence, the Box 24-to-25 transition, blank fields, and archival
location were checked against full-page and high-resolution renders. The bundle
contains ten person updates, twelve sources, one identity claim, and ten durable
research attempts.

David Atherton remains probable rather than confirmed. Two independently
published 2025 accounts based on a family photo donation identify him with OSS
Operational Group Emily in France in 1944. They disagree on a June 9 versus
July 9 parachute date, so the project retains only the shared year and records
the conflict. Neither account documents his immediate pre-OSS affiliation or
last civilian employer. Carl A. Atkins, Earl J. Atkins, Frank J. Atkins,
Geoffroy Atkinson, John W. Atkinson, Katrhryn C. Atkinson, Marion Atkinson,
William H. Atkinson, and Kathryne J. Atkisson remain unresolved after the
terminal online protocol and route to their indexed Box 24 or 25 files.

High-resolution inspection confirms that `Katrhryn C. Atkinson` is the source
index's literal spelling; likely conventional spellings are search aliases, not
silent corrections. No authenticated NARA Catalog request was made, no API key
was accessed, and no live NARA API response was retained. Temporary renders
were used only for inspection and removed after review. No full service
identifier appears in the evidence bundle or public projection.

## Page-fifteen Atkisson-through-Atwood pathways, Batch 110

`research/evidence-page-fifteen-atkisson-through-atwood-pathways_batch-110_2026-07-31.json`
records ten visually checked, contiguous rows from Russell E. Atkisson through
Donald F. Atwood on PDF page fifteen. Raw spellings, initials, suffixes, ranks,
service-number presence or absence, Box 25, blank fields, and archival location
were checked against a high-resolution page render. The bundle contains ten
person updates, twenty-one sources, one organization, one affiliation, six
claims, and ten durable research attempts.

Roy B. Attride Sr. is confirmed by NARA JFK record `104-10165-10120`, PDF page
108/document page 81, which names Pfc Roy R. B. Attride Sr. as an OSS X-2
Insurance Unit leader. The International Grenfell Association's July 1936
*Among the Deep-Sea Fishers*, printed page 66/PDF page 24, records his selection
as the St. Anthony District office bookkeeper for winter 1936-37. Its April
1943 alumni news calls him former staff, and its July 1945 issue places him in
the Army and OSS. The bookkeeper role is therefore published as
high-confidence, documented-prewar employment only. The accessible sequence
does not establish it as his immediate pre-OSS affiliation or last civilian
employer.

A November 29, 1944 *Heinl Radio Business Letter* notice, printed page 10/PDF
page 78, and official FCC Reports, volume 24, page 799, support the
high-confidence Leslie H. Atlass Jr./H. Leslie Atlass Jr. identity and Army
service. The FCC employment chronology begins after his 1945 discharge, and
his father's CBS role is not attributed to him. United States Design Patent
D132,141 and a scholarly citation to Aldon N. Attayer's March 17, 1944 Allied
Control Commission survey in NARA RG 331 support Attayer's identity, but patent
authorship is not treated as self-employment. The contemporary Ninth Army
history, page 336, supports only a probable Paul R. Attix identity because it
does not reproduce his indexed identifier or establish the pre-OSS sequence.
A NARA personnel-folder finding aid places Amariah G. C. Atwater at the start
of Naval Officers Personnel Cards Roll 22; a secondary full-name biography is
corroborative only. Its undated Wrigley role remains a lead, not a pre-OSS
employment claim.

Russell E. Atkisson, Ben C. Attardi, Allen R. Atwater Jr., Bert Atwater Jr.,
and Donald F. Atwood remain unresolved after the staged official, exact-name,
employment, occupation, newspaper, directory, obituary, institutional, NARA,
CIA Reading Room, and Library of Congress protocol. Their profiles route to
Box 25 rather than promoting common-name or genealogy candidates. No
authenticated NARA Catalog request was made, no API key was accessed, and no
live Catalog response was retained. Temporary source copies and page renders
were used only for inspection outside the repository. No full service
identifier appears in the evidence bundle or public projection.

## Page-fifteen-and-sixteen Atwood-through-Aubrey pathways, Batch 111

`research/evidence-page-fifteen-atwood-through-aubrey-pathways_batch-111_2026-07-31.json`
records ten visually checked, contiguous rows from Elmer E. Atwood through
Leland K. Aubrey across PDF pages fifteen and sixteen. Raw spellings, initials,
suffixes, ranks, service-number presence or absence, Box 25, blank fields, and
archival location were checked against high-resolution page renders. The
bundle contains ten person updates, fourteen sources, two organizations, two
affiliations, three claims, ten durable research attempts, and seven
claim-source links.

The Library of Congress Wallace W. Atwood papers finding aid, collection
G3201.S7 coll Atwood and LCCN 2016431101, expands the indexed identity to
Wallace Walter Atwood Jr., identifies him as Clark University's professor of
physiography by circa 1940, and records his 1941-45 Army Map Service
Topographic Model Section directorship. The December 11, 1940 *Waterbury
Evening Democrat*, page 14, independently calls the 34-year-old Atwood a Clark
University professor. Clark is therefore published as high-confidence last
civilian employment, but not as an immediate pre-OSS affiliation.

National Park Service administrative history documents Atwood's earlier
earth-sciences assignment and replacement in March 1932. A CIA OSS-collection
history, printed page 15/PDF page 17, documents the OSS Topographic Model
Section and the Atcorob globe named for Atwood, H. L. Cooke, and Arthur
Robinson. These sources do not establish whether Army Map Service preceded,
overlapped, or administratively enclosed the OSS work. The precise immediate
pre-OSS relationship remains unresolved rather than silently inferred.

Elmer E. Atwood, John L. Atwood, Margaret Atwood, Robert D. Atwood, Samuel J.
Atwood, Arthur S. Aubrey Jr., August O. Aubrey, Jules W. Aubrey, and Leland K.
Aubrey remain unresolved after the staged protocol and route to Box 25 review.
The aerospace executive John Leland Atwood lacks identifier or rank linkage to
the indexed person, and the Canadian novelist Margaret Atwood is
chronologically impossible; neither candidate is promoted. No authenticated
NARA Catalog request was made, no API key was accessed, and no live Catalog
response was retained. Temporary PDFs, API discovery responses, page renders,
and text extracts were used only for inspection outside the repository. No
full service identifier appears in the evidence bundle or public projection.

## Page-sixteen Aubuchon-through-Auerbach pathways, Batch 112

`research/evidence-page-sixteen-aubuchon-through-auerbach-pathways_batch-112_2026-07-31.json`
records ten visually checked, contiguous rows from Joseph A. Aubuchon through
Carl A. Auerbach on PDF page sixteen. Raw spellings, initials, the printed
Gordon Auchincloss `II` suffix, ranks and civilian grade, service-number
presence or absence, the Box 25-to-26 transition, blank fields, and archival
location were checked against a high-resolution page render. The bundle
contains ten person updates, twelve sources, two reused canonical
organizations, two affiliations, three claims, ten durable research attempts,
and seven claim-source links.

American Law Institute and University of Minnesota Law School memorials
provide a high-confidence match between indexed Second Lieutenant Carl A.
Auerbach and the lawyer who was drafted into the Army and served with the OSS
in London. The Office of Price Administration is published as his
high-confidence last civilian employment before wartime service. It is not
labeled his immediate pre-OSS affiliation because an intervening Army period
is documented but not dated or organizationally resolved. His earlier U.S.
Department of Labor position is preserved separately as documented prewar
government work. The sources do not name his brief Washington law firm, so the
project does not invent an employer, and an undated or later description of an
OPA General Counsel role is excluded from the predecessor claims.

Joseph A. Aubuchon, Roy A. Aubuchon, Gordon Auchincloss II, John W.
Auchincloss, Joseph P. Auclair, William S. Aud, Rene E. Audet, Marie Audibert,
and Joseph J. Audie remain unresolved after the staged protocol and route to
Box 25 or 26 review. CIA search results pointed to Gordon Auchincloss in an OSS
report, but the current document route did not provide inspectable page
context; the hit remains a lead rather than a citation or identity claim. The
three blank-rank rows retain indeterminate commissioned status. No
authenticated NARA Catalog request was made, no API key was accessed, and no
live Catalog response was retained. Temporary page renders and discovery
results were used only for inspection outside the repository. No full service
identifier appears in the evidence bundle or public projection.

## Page-sixteen Auerbach-through-Ault pathways, Batch 113

`research/evidence-page-sixteen-auerbach-through-ault-pathways_batch-113_2026-07-31.json`
records ten visually checked, contiguous rows from Herbert Auerbach through
Lawrence Ault, Jr. on PDF page sixteen. Raw spellings, initials, suffix,
ranks and civilian grade, service-number presence or absence, Box 26, blank
fields, and archival location were checked against a high-resolution page
render. The bundle contains ten person updates, fifteen sources, two canonical
organizations, two affiliations, four claims, ten durable research attempts,
and ten claim-source links.

The National WWII Museum oral history and episode transcript provide a
high-confidence match between indexed Sergeant Herbert Auerbach and the Army
cryptographer who served with V Force and OSS Detachment 101 in Burma. V Force
is published as his explicit immediate pre-OSS military assignment, while the
United States Army Signal Corps is preserved separately as earlier documented
military service. Neither is described as a civilian employer, and the
accessible chronology does not identify his last civilian employer before
enlistment.

A CSUN archival finding aid strongly links indexed Meyer Auerbach to Meyer
Morton Auerbach through his unusually specific 1946 Strategic Services Unit
work in China. Because that evidence is explicitly postwar, it supports only
the identity claim and is not converted into a pre-OSS affiliation. William
Auerbach, Douglas B. Auffmordt, Joseph R. Augello, Duplius P. Auguste, James R.
Augustine, Mary Augustine, Richard N. Auld, and Lawrence Ault, Jr. remain
unresolved and route to Box 26 review. The Harvard Law William Auerbach and
Army-enlistment Douglas B. Auffmordt candidates lack direct OSS or indexed-file
linkage and support no public claim. No authenticated NARA Catalog request was
made, no API key was accessed, and no live Catalog response was retained.
Temporary page renders and discovery results were used only for inspection
outside the repository. No full service identifier appears in the evidence
bundle or public projection.

## Page-sixteen Ault-through-Austreng pathways, Batch 114

`research/evidence-page-sixteen-ault-through-austreng-pathways_batch-114_2026-07-31.json`
records ten visually checked, contiguous rows from Lee A. Ault through Vernon
L. Austreng on PDF page sixteen. Raw spellings, initials, ranks and civilian
grades, service-number presence or absence, Box 26, blank fields, and archival
location were checked against a high-resolution page render. The bundle
contains ten person updates, sixteen sources, three affiliations, seven claims,
ten durable research attempts, and twenty claim-source links.

The public NARA Catalog description for National Archives Identifier 1263923
exposes the unrestricted compressed Electronic Army Serial Number Merged File
and its official technical documentation. The bulk file was downloaded to a
temporary ignored path, streamed once against the seven privately retained
Army identifiers in this batch, and deleted. No authenticated Catalog API
request was made, no API key was accessed, and no raw bulk record or downloaded
archive was retained in the repository.

Exact private-identifier matches confirm James W. Austin, Kenneth P. Austin,
and Vernon L. Austreng. NARA's Code No. 30 lists decode the first two records'
civilian occupation code as students and Austreng's as farm hands on general
farms. The student institutions and employing farm are not named; the project
therefore publishes status or occupation only, not an employer, self-employment,
or an immediate pre-OSS affiliation.

The Army merged file prints Kenneth R. Austin where the OSS index prints
Kenneth P. Austin. It also prints Vernon N. Austreng and a different December
1942 Army-entry day from the official North Dakota veterans register, which
prints Vernon L. Austreng and matches the private identifier. These conflicts
are preserved in name variants and research notes, consistent with NARA's
published warnings about scanning and keypunch errors. The underlying punch
card and Box 26 file remain the resolution targets.

The OSS Operational Groups historical roster lists T/4 Otis Ausen and Cpl.
Vernon L. Austreng in Norwegian operations. The distinctive exact Otis name,
middle initial, matching rank, and explicit OSS context support a
high-confidence identity but no pre-OSS affiliation. A Princeton memorial for
Lee A. Ault was reviewed and rejected as an identity basis because its
Newsweek, American Field Service, and Marine Corps chronology does not provide
OSS, Box 26, or direct-identifier linkage. Gino Austi, Benton M. Austin, Merry
A. Austin, Nancy R. Austin, and Robert W. Austin remain unresolved after the
staged protocol. No full service identifier appears in the evidence bundle or
public projection.

## Page-sixteen Autotte-through-Axelrad pathways, Batch 115

`research/evidence-page-sixteen-autotte-through-axelrad-pathways_batch-115_2026-08-01.json`
records ten visually checked, contiguous rows from Joseph R. Autotte through
Gerald Axelrad on PDF page sixteen. Raw spellings, initials, ranks and civilian
grades, service-number presence or absence, Boxes 26 and 27, blank fields, and
archival location were checked against a high-resolution page render. The
bundle contains ten person updates, eighteen sources, five canonical
organizations, six affiliations, fourteen claims, ten durable research
attempts, and twenty-four claim-source links.

A scanned official European Theater roster confirms Joseph R. Autotte through
the exact uncommon name and a private officer-identifier match. The roster's
second-lieutenant grade and the index's first-lieutenant grade are preserved as
a compatible wartime progression, but neither source establishes his pre-OSS
pathway. Targeted OCR was confined to this eleven-page image-only official
record and the result was visually checked.

U.S. Army Special Operations History explicitly cites Herbert Avedon's Box 27
personnel file and dates his 4th Ranger Infantry Battalion assignment and
recruitment from Camp Butner into OSS. The battalion is therefore published as
his immediate pre-OSS military assignment. His 1933-34 first-mate service on
the SS Birmingham City is separate earlier employment; later unnamed civilian
jobs prevent the ship from being labeled his last civilian employer.

Contemporary Wheaton College trustee minutes were visually reviewed at internal
pages 506 and 630. They clearly spell Grazia Avitabile, appoint her Instructor
in Italian and French in 1942, and extend her unpaid leave in 1945 because she
was in Italy with OSS. Wheaton is published as both immediate affiliation and
last civilian employer. Earlier part-time teaching at Bryn Mawr is separate.
The index's Crazia R. form remains the page title and an explicit variant rather
than being silently corrected.

The Oregon Encyclopedia supports a qualified high-confidence match between
indexed Jacob D. Avshalonoff and composer Jacob David Avshalomov through the
distinctive transliteration variant, middle name, age, and wartime U.S. Army
interpreter service. Eastman study is modeled as student status, and work as a
factory supervisor in three unnamed Chinese factories is published as an
occupation without inventing employers. Box 27 remains necessary for direct
identifier and OSS-link confirmation.

The unrestricted NARA Army enlistment bulk file confirms Gerald Axelrad by an
exact private identifier, but its surviving occupation-code documentation does
not support one unambiguous occupation. For James H. Awad, the index identifier
maps to a different name while an exact-name enlistment entry carries a
different identifier. That conflict is published without exposing either full
identifier or the unrelated name. Mary E. Autrey, Stella Avner, and Nabit Awad
remain unresolved after the staged protocol; plausible name-only candidates
were rejected. Cleveland E. Autry receives a high-confidence identity from a
contemporary authorized OSS account, but no predecessor affiliation is
assigned.

The Army bulk archive and records were downloaded only to temporary ignored
paths, inspected locally, and deleted after use. No authenticated NARA Catalog
request was made, no API key was accessed, and no raw bulk record, live API
response, full service identifier, or unrelated namesake was retained in the
repository or public projection.

## Page-sixteen-and-seventeen Axelrod-through-Aznavourian pathways, Batch 116

`research/evidence-page-sixteen-seventeen-axelrod-through-aznavourian-pathways_batch-116_2026-08-01.json`
records ten visually checked, contiguous rows from Kermit Axelrod through
Margaret Aznavourian across PDF pages sixteen and seventeen. Raw spellings,
initials, ranks and civilian grades, service-number presence or absence, Box
27, blank fields, and archival location were checked against high-resolution
page renders. The bundle contains ten person updates, fifteen sources, seven
claims, ten durable research attempts, and seventeen claim-source links. It
adds no organization or affiliation because none of the reviewed evidence
names an employer or supports an immediate pre-OSS institution.

Private identifiers were checked through NARA's public Access to Archival
Databases Army Enlistment Records and Reserve Corps tables. Exact identifier
and name agreement confirms Forrest R. Ayers, Henry C. Ayers, and John F.
Ayers. The official data records Forrest's civilian occupation category as
general office clerk and John's as sales clerk at Army entry. These findings
are published as occupations only: no employing organization is named, and
neither record establishes the immediate step into OSS. Henry's occupation
field is an undefined code, so no occupation is assigned.

The indexed private identifiers for Kermit Axelrod and Morris E. Aycock resolve
to different names in the official tables. NARA's published cautions about
scanning and keypunch errors prevent treating the merged data as infallible;
both conflicts remain visible and route to Box 27 and the original enlistment
records. The full identifiers and unrelated names are omitted. A Rutgers
exact-name Kermit Axelrod candidate was reviewed but not selected because it
supplies no OSS, Box 27, or identifier linkage.

R. A. Axlund, Frank W. Ayers, Barbara F. Aylesworth, John M. Ayshford, and
Margaret Aznavourian remain unresolved after the staged official, exact-name,
employment, occupation, newspaper, obituary, institutional, CIA, and Library
of Congress protocol. Namesakes and spelling variants remain rejection leads,
not asserted identities. The public AAD pages were inspected transiently;
only concise project-authored citation notes and stable Catalog pointers are
retained. No authenticated NARA Catalog API request was made, no API key was
accessed, and no raw response page or full service identifier was stored in the
repository or public projection.

## Page-seventeen Aznone-through-Babberle pathways, Batch 117

`research/evidence-page-seventeen-aznone-through-babberle-pathways_batch-117_2026-08-01.json`
records ten visually checked, contiguous rows from James W. Aznone through
Stanley L. Babberle on PDF page seventeen. Raw spellings, initials, ranks,
service-number presence or absence, Boxes 27 and 28, blank fields, and archival
location were checked against a 200-dpi page render. The bundle contains ten
person updates, eighteen sources, seven claims, ten durable research attempts,
and seventeen claim-source links. It creates no organization or affiliation
because none of the reviewed evidence names an employer or establishes an
immediate pre-OSS institution.

Exact name and private-identifier agreement in NARA's public Access to
Archival Databases Army table confirms Matthew F. Azzarone, Philip Azzolina,
Mike Baarsvik, and Gust J. Babalis. The table records occupation categories at
Army entry for Azzarone, Azzolina, and Baarsvik but names no employer; all three
are therefore published as occupation-only results and remain excluded from
employer and affiliation analytics. Babalis's occupation code is undefined and
is not expanded. Full identifiers are withheld from the evidence bundle,
public data, and site.

Denver Public Library's 10th Mountain Division index independently matches
Mike Baarsvik's name and private identifier and records Company A, 99th
Infantry. That unit is used as identity and wartime-context evidence only:
the reviewed sources do not establish whether it immediately preceded his OSS
service. A specialist OSS Operational Groups roster independently places T/5
Gust J. Babalis in Greek Group VII; it likewise supports identity and OSS
context rather than a pre-OSS employer claim.

James W. Aznone, Thomas T. Baba, and Stanley L. Babberle did not return a
matching identifier in either applicable AAD table. This absence is not
treated as a contradiction because NARA documents coverage and transcription
limits. Josephine Azzolina and John E. Babb carry officer identifiers outside
the enlisted AAD tables. Vassar and Tennessee exact-name candidates for
Josephine Azzolina and Knud Baagoe lack direct OSS, officer, Box, or identifier
linkage and remain rejected leads. Six identities remain unresolved and route
to Box 27 or 28; Babalis also retains Box 28 review for his unknown occupation
and predecessor chronology.

The public AAD and institutional pages were inspected transiently. The Denver
PDF was downloaded only to a temporary directory, its title and relevant entry
were inspected, and the temporary file was excluded from the repository. No
authenticated NARA Catalog API request was made, no API key was accessed, and
no raw Catalog response, full service identifier, or copyrighted source copy
was stored in the repository or public projection.

## Page-seventeen Babcock-through-Babyak pathways, Batch 118

`research/evidence-page-seventeen-babcock-through-babyak-pathways_batch-118_2026-08-01.json`
records ten visually checked, contiguous rows from George H. Babcock through
Andrew H. Babyak on PDF page seventeen. Raw spellings, initials, suffixes,
ranks, private-identifier presence or absence, Box 28, blank fields, and the
archival location were checked against a 200-dpi page render. The bundle
contains ten person updates, twenty-two sources, four claims, ten durable
research attempts, and fourteen claim-source links. It creates no organization
or affiliation because none of the reviewed evidence names a supportable
pre-OSS employer or establishes an immediate predecessor institution.

Exact name and private-identifier agreement in NARA's public Access to
Archival Databases Army table confirms George H. Babcock. His official
occupation field is an undefined code, so the project publishes neither an
occupation nor an employer. Millard A. Babin Jr.'s indexed private identifier
returned no record in the applicable public Army tables; NARA's documented
coverage and transcription limits mean that non-result is not treated as a
contradiction. Full private identifiers and transient response pages are not
stored in the evidence bundle or public projection.

Two official National Security Agency VENONA descriptions place Thomas Babin
with an OSS unit and OSS associates in July 1943. Haynes and Klehr's scholarly
*Venona* history independently describes his brief OSS service and wartime work
as a Hoboken longshoreman. Those sources support a high-confidence identity and
a medium-confidence occupation-only finding. They do not name an employer or
explicitly sequence the longshore work before OSS entry, so the site preserves
temporal uncertainty and excludes the claim from employer analytics.

Michigan State University archives and board minutes document a postwar
Raymond P. Babineau in the Vietnam Project. A CIA Reading Room copy of a 1966
third-party magazine article supplies corroborative career context, not an
official CIA-authored personnel determination. The rare-name match remains
probable because no reviewed source supplies the indexed officer identifier,
Box 28 linkage, or wartime chronology. It contributes no pre-OSS affiliation.
Steelworker and Goodyear obituaries for Mike and Milan Babich, along with
directory, obituary, and newspaper candidates for the other rows, remain
rejected leads rather than profile facts.

The public AAD pages were inspected transiently through the read-only form;
the current Library of Congress API was queried for discovery without saving
raw responses, and a blocked item page was not bypassed. No authenticated NARA
Catalog API request was made, no API key was accessed, and no raw Catalog
response, full service identifier, copyrighted book, or newspaper page was
stored in the repository or public projection.

## Page-seventeen Bachand-through-Backus pathways, Batch 119

`research/evidence-page-seventeen-bachand-through-backus-pathways_batch-119_2026-08-01.json`
records ten visually checked, contiguous rows from Albert E. Bachand through
Emmett F. Backus on PDF page seventeen. Raw spellings, initials, suffixes,
ranks, private-identifier presence or absence, Box 28, blank fields, civilian
grades, and the archival location were checked against a 200-dpi page render.
The bundle contains ten person updates, eighteen sources, five identity claims,
ten durable research attempts, and fourteen claim-source links. It creates no
organization or affiliation because none of the reviewed evidence establishes
a supportable pre-OSS employer or predecessor institution.

A declassified May 1944 U.S. government record in the Hoover Institution's
Millard Preston Goodfellow papers lists Walter F. Bachelder as a second
lieutenant at Algiers and Gilbert O. Backman as a second lieutenant at Bari.
Exact names and compatible ranks across that record and the NARA index confirm
both identities. Contemporary Dartmouth war directories corroborate
Bachelder's progression from sergeant in 1942 to second lieutenant in 1943.
His obituary states that Testing Machines Inc. employment began in 1947, so
the company is explicitly rejected as a pre-OSS employer.

University of Maryland repository and commencement records give Ross E.
Backenstoss Jr.'s full middle name and suffix in 1943. Because those records do
not contain the indexed private identifier or independently establish OSS
service, the identity remains probable, and student status is not converted
into employment or labeled immediately pre-OSS. A direct 1946 U.S. government
letter preserved by the Hellenic Literary and Historical Archive lists the
exact uncommon name Mary E. Backle in an Athens unit reporting to the Strategic
Services Unit. That supports a high-confidence identity while remaining
post-OSS evidence only. A secondary Jedburgh roster gives Albert V. Bacik's
exact uncommon name, compatible enlisted status, Team Arthur, and cover name;
the match remains probable and medium confidence pending Box 28.

Albert E. Bachand, Robert J. Bachman, Rose M. Backman, Alice C. Backus, and
Emmett F. Backus remain unresolved after staged NARA/index context, CIA,
exact-name OSS, employment, occupation, newspaper, obituary, directory, and
institutional searches. Name-only people-finder and unsourced genealogy leads
were rejected. A 1936 radio-amateur directory entry for an Albert V. Bacik was
not published because it establishes neither employment nor OSS identity; its
street address was not retained. All ten profiles route to Box 28 for the
missing chronology and employment evidence.

Only stable citations, concise project-authored evidence notes, and short
excerpts are retained. No authenticated NARA Catalog API request was made, no
API key was accessed, and no raw Catalog response, full service identifier,
home address, copyrighted source copy, or people-finder data was stored in the
repository or public projection.

## Page-seventeen Backus-through-Bader pathways, Batch 120

`research/evidence-page-seventeen-backus-through-bader-pathways_batch-120_2026-08-01.json`
records ten visually checked, contiguous rows from Samuel D. Backus through
James W. Bader on PDF page seventeen. NARA's public AAD Army enlistment tables
were searched through the read-only browser interface using private identifiers
only for comparison. Exact identifier-and-name matches confirm Samuel D.
Backus, Charles A. Bacon Jr., and Nate A. Badami; the two defined results are
retained as occupation categories only and are not treated as employers.

Direct University of Washington records, Smithsonian material, and a scholarly
institutional study support Elizabeth Emaline Bacon's qualified, date-bounded
university employment. A reproduced U.S. Army general order and a French
archival compilation support Albert E. Bacquet's qualified French Army/OSS
mission identity. Neither pathway is silently promoted to an immediate
pre-OSS affiliation. Five other identities remain unresolved. No authenticated
Catalog API request was made and no private identifier or raw AAD response was
retained.

## Page-eighteen Badia-through-Baerwald pathways, Batch 121

`research/evidence-page-eighteen-badia-through-baerwald-pathways_batch-121_2026-08-01.json`
records the first ten visually checked rows of PDF page eighteen. Exact
identifier-and-name comparisons in the public AAD Army tables confirm Edwin I.
Baer and Vivian L. Baer and publish only their occupation categories. A
conflicting identifier result for Joseph T. Badzik is retained as a conflict;
facts belonging to William R. Brandes are not transferred to Badzik. Ralph H.
Baer's famous-biography candidate remains withheld pending Box 29 evidence.

Berkeley archival material, contemporary chronology, a memoir, and an
institutional memorial support Ernest D. Baerwald's qualified prewar employment
and a separate professional affiliation. The available chronology does not
establish either as immediately pre-OSS. The public AAD pages were inspected
transiently, without an authenticated Catalog API call, retained raw response,
or published private identifier.

## Page-eighteen Bagby-through-Bahor pathways, Batch 122

`research/evidence-page-eighteen-bagby-through-bahor-pathways_batch-122_2026-08-01.json`
records ten visually checked, contiguous rows from Philip H. Bagby through
Frank P. Bahor on PDF page eighteen. Raw names, initials, ranks and civilian
grades, identifier presence or absence, Box 29, and archival location were
checked against the rendered page. The validated bundle contains ten person
updates, twenty sources, nine claims, twenty-one claim-source links, and ten
durable research attempts. It creates no organization or affiliation.

NARA's public AAD Army enlistment tables provide exact identifier-and-name
matches for Philip H. Bagby and Merrill B. Bahnson. The index's Irving J.
Bagle identifier resolves to Irving J. Eagle with the same given name and
middle initial, preserving the one-letter surname difference as an indexed
variant. The resulting clerk, motor-vehicle mechanic, and sailor/deckhand
descriptions are occupation-only findings; they establish no named employer or
vessel. No matching main- or reserve-table record was found for Robert K.
Baggot or Frank P. Bahor, which is recorded as a failed search rather than
negative evidence about their service.

The German Filmportal and Deutsche Digitale Bibliothek identify Douglas W.
Bagier as an alias of Wolfgang Loë-Bagier and document prewar work in film
editing, direction, assistant direction, and screenwriting. The identity is
high confidence, but the occupation finding remains medium confidence and
qualified because the sources do not name a single employing organization.
A NARA staff response in the archived History Hub confirms a matching Helene
B. Baginski Caf-5 personnel file in Box 29 and says it is not digitized; it
does not supply pre-OSS employment evidence.

Postwar Fort Worth and Greenbelt exact-name candidates and an older Philip
Haxall Bagby namesake were rejected because they do not establish the indexed
identity or the required chronology. Searches of official context, CIA,
exact-name OSS variants, employment and occupation sources, newspapers,
obituaries, directories, and institutional/archival material left Percy A.
Bagge, Robert K. Baggot, David J. Bagley, Sidney Bah-Oh, and Frank P. Bahor
unresolved. All ten route to Box 29 for the missing personnel-file evidence.

The AAD interface was used transiently and read-only. No authenticated NARA
Catalog API request was made, no API key was accessed, and no raw response,
full private identifier, copyrighted page, home address, or people-finder data
was stored in the repository or public projection.

## Page-eighteen Bahoric-through-Bailey pathways, Batch 123

`research/evidence-page-eighteen-bahoric-through-bailey-pathways_batch-123_2026-08-01.json`
records ten visually checked, contiguous rows from Bodizar Bahoric through Jay
E. Bailey on PDF page eighteen. Raw names, initials, ranks and civilian grades,
identifier presence or absence, the printed `aka Boz` note, Box 29, and archive
location were checked against a 200-dpi render at original detail. The
validated bundle contains ten person updates, eighteen sources, four claims,
nine claim-source links, and ten durable research attempts. It creates no
organization or affiliation.

NARA's public AAD Army enlistment table supplies exact private-identifier
matches for Guy B. Bailey and Harry F. Bailey. Compatible initials and the
Sergeant grade confirm Guy; exact name and identifier agreement confirm Harry,
whose 1940 Private grade is compatible with the later indexed Corporal grade.
Guy's record carries a dairy farm-hand occupation category at a November 1945
Army entry or recall. Because that date's relationship to his OSS service is
unknown, the project does not call the occupation pre-OSS. Harry's October
1940 record carries a semiskilled bus, taxi, truck, or tractor driver category.
Neither result names an employer, so both are occupation-only findings and are
excluded from employer and affiliation analytics.

The applicable AAD main and Reserve Corps tables returned no matching private
identifier for Robert J. Bahr, Irving S. Bailey, Jason S. Bailey, or Jay E.
Bailey. NARA's documented coverage and transcription limits mean that these
non-results are recorded as searches, not as contradictions. A secondary
troop-carrier record for a Robert J. Bahr lacks the indexed identifier and
remains an unlinked candidate. Official NSA material contains the similar
form Bozidar Bahoric but supplies no OSS, Box 29, employment, chronology, or
direct identity link; it remains a rejected search candidate, not a corrected
name or published biographical fact.

The current Library of Congress collection API, CIA Reading Room OSS
collection, NARA/Catalog context, exact-name OSS variants, employment and
occupation searches, newspapers, obituaries, directories, and institutional
or archival sources were reviewed under the staged minimum protocol. Bodizar
Bahoric, Robert J. Bahr, E. J. Bailey, Fay I. Bailey, Georgia M. Bailey, Irving
S. Bailey, Jason S. Bailey, and Jay E. Bailey remain unresolved and route to
Box 29 for the missing identity, chronology, and employment evidence.

The AAD interface and Library of Congress API were used transiently and
read-only. No authenticated NARA Catalog API request was made, no API key was
accessed, and no raw API response, full private identifier, copyrighted page,
home address, people-finder data, or rejected candidate biography was stored in
the public projection.

## Page-eighteen Bailey-through-Bailey pathways, Batch 124

`research/evidence-page-eighteen-bailey-through-bailey-pathways_batch-124_2026-08-01.json`
records ten visually checked, contiguous rows from Kenneth R. Bailey through
Walter L. Bailey on PDF page eighteen. Raw names, initials, ranks, identifier
presence or absence, Boxes 29 and 30, and archive locations were checked
against a 200-dpi render at original detail. The validated bundle contains ten
person updates, twenty sources, eight claims, twenty-one claim-source links,
and ten durable research attempts. It creates no organization or affiliation.

NARA's public AAD Army enlistment table supplies exact name and private-
identifier matches for Kenneth R. Bailey, Morris F. Bailey, Thomas H. Bailey,
and Walter H. Bailey. Compatible rank progression supports each match. The
records document, respectively, student status, a semiskilled-routeman
occupation, a photographer occupation, and the broad source category college
presidents, professors, and instructors at Army entry. The official student
code list was reviewed for Kenneth's numeric occupation code. None of the
records names a school or employer, and none establishes the exact OSS
recruitment sequence, so all four findings remain occupation/status only and
are excluded from employer and affiliation analytics.

The applicable AAD main and Reserve Corps tables supplied no match for Robert
C. Bailey's atypical printed identifier, Lieutenant Stephen K. Bailey's
officer-style identifier, Waldo E. Bailey, or Walter L. Bailey. Exact-name
checks also supplied no match for Marcella D. Bailey or Urcle G. Bailey. NARA's
documented file gaps mean these non-results are recorded as search outcomes,
not contradictions or corrections to the index.

Three contemporary *Harlem News* county-expenditure entries document laundry
work by an exact or near-exact Urcle Bailey name in 1937-1938. They supply no
OSS, military, Box 30, residence, birth, or other corroborating identifier.
The Montana person therefore remains an unlinked, rejected identity candidate;
no occupation, employer, or affiliation is assigned to the indexed person.

The current Library of Congress collection API and item records, CIA Reading
Room OSS collection, NARA/Catalog context, exact-name OSS variants, employment
and occupation searches, newspapers, obituaries, directories, and
institutional or archival sources were reviewed under the staged minimum
protocol. Marcella D. Bailey, Robert C. Bailey, Stephen K. Bailey, Urcle G.
Bailey, Waldo E. Bailey, and Walter L. Bailey remain unresolved and route to
Boxes 29 or 30 for the missing identity, chronology, and employment evidence.

The AAD interface and Library of Congress API were used transiently and
read-only. No authenticated NARA Catalog API request was made, no API key was
accessed, and no raw API response, full private identifier, copyrighted page,
home address, or people-finder data was stored in the repository or public
projection.

## Page-twenty Balfour-through-Ball pathways, Batch 132

`research/evidence-page-twenty-balfour-through-ball-pathways_batch-132_2026-08-01.json`
records ten contiguous rows from Francis A. Balfour through Leon F. Ball on
PDF page 20. The page was rendered at 300 dpi and inspected at original
resolution. All 46 printed rows match the parsed names, initials, grades or
ranks, identifier-column occupancy, boxes, and archive locations, so page 20
is now retained in the cumulative matching-page review manifest without a
parser correction. Full private identifiers remain in SQLite only.

The reviewed evidence bundle contains 23 source records, one normalized
organization, one affiliation, five claims, 14 claim-source links, ten person
updates, and ten terminal research attempts. Contemporary *Evening Star*
items support high-confidence identity matches for Berkley Clark Ball and
Frank L. Ball Jr. Their wartime Army evidence does not establish the date or
sequence of OSS entry, so no immediate pre-OSS affiliation or civilian
employer is assigned.

A sourced CND-Castille infiltration chronology identifies Leon F. Ball,
alias Niveau, as OSS and describes his June 1944 France mission. The Musée de
la Résistance en ligne and the municipality of Passy independently connect
Léon Ball or Niveau to the U.S. Army lieutenant and resistance context. Pierre
Sauvage's Varian Fry research documents Ball as a lard salesman in 1930s
France without naming a company. Villa Air-Bel and Sauvage place him with the
Marseille rescue team associated with the Centre américain de secours in
1940-1941. That relationship is modeled as a professional affiliation because
the sources do not establish paid or volunteer status, and it is not labeled
the immediate predecessor to OSS.

Francis A. Balfour, Nina Balfour, Julius M. Balick, Joseph A. Balint, Dorothy
L. Balkam, John Balko, and John J. Ball Jr. remain unresolved after official
context, CIA Reading Room, current Library of Congress API, exact-name OSS,
employment, occupation, newspaper, obituary, directory, institutional, and
archival searches. Nine profiles route to Box 32 review; Leon Ball retains an
occupation-only result and the same archival next action. The public AAD
interface returned HTTP 403, which is recorded only as an access limitation.
No authenticated NARA Catalog API request was made, no key was accessed, and
no raw API response, copyrighted page, full private identifier, home address,
or people-finder data was stored in the public projection.

## Page-twenty Ball-through-Ballard pathways, Batch 133

`research/evidence-page-twenty-ball-through-ballard-pathways_batch-133_2026-08-01.json`
records ten new contiguous page-twenty people from Maurice Ball through Harry
W. Ballard. Egerton L. Ballachey, the intervening printed row, remains preserved
and linked to the earlier Batch 130 adjudication. Page 20 had already been
rendered at 300 dpi and inspected at original resolution; all 46 printed rows
match the parser, including these names, initials, ranks or civilian grades,
identifier-column occupancy, boxes, and archive locations. Full private
identifiers remain in SQLite only.

The strict bundle contains 16 private source records, one public-visible
medium-confidence identity claim, three claim-source links, ten person updates,
and ten terminal research attempts. The specialist OSS Operational Groups
personnel page lists T/5 Frank L. Ballante in the Choctaw roster and Frank
Ballante in Alpha. Its Choctaw mission page independently repeats the exact
middle initial and grade and says the mission summary was compiled from
National Archives end-of-mission reports. Because both pages belong to one
secondary research project and neither prints Ballante's private identifier or
an item-level primary citation, the identity is published only as probable.
The sources document wartime OSS service, not a pre-OSS employer.

Maurice Ball, Mildred G. Ball, Ned B. Ball, Robert O. Ball, Rubye L. Ball,
Tellison F. Ball, Ernest L. Ballachino, Adele Ballantine, and Harry W. Ballard
remain unresolved after staged NARA/Catalog context, CIA Reading Room,
exact-name and meaningful variant, employment, occupation, newspaper,
obituary, directory, institutional, and archival searches. A Durham directory
job for a Ned B. Ball, family-based Adele Ballantine lead, discovery-only life
dates, and later Harry W. Ballard business evidence were rejected rather than
silently assigned. The Library of Congress API returned HTTP 429 for one
exact-name request; no retry was made, and broader newspaper discovery
continued without converting access failure into a negative result.

No authenticated NARA Catalog API request was made, no credential was accessed,
and no raw API response, full private identifier, copyrighted page, home
address, relative's details, or people-finder data was stored in the public
projection.

## Page-twenty and page-twenty-one Ballew-through-Bally pathways, Batch 134

`research/evidence-page-twenty-twenty-one-ballew-through-bally-pathways_batch-134_2026-08-01.json`
records the final seven researched people on page 20 and the first three on
page 21, from Mary J. Ballew through Georges S. Bally. Page 20 was already a
complete visual match. Page 21 was rendered at 300 dpi and inspected at
original resolution; all 46 printed rows match the parsed names, initials,
ranks or civilian grades, identifier-column occupancy, boxes, notes, and
archive locations. Full private identifiers remain in SQLite only.

The strict bundle contains 13 source records, three public-visible identity
claims, seven claim-source links, ten person updates, and ten terminal research
attempts. Phil McCombs's 1995 *Washington Post* history of OSS women directly
identifies Bette Balliet Grefe as a Wisconsin recruit who received American Red
Cross and OSS offers on the same day and chose OSS. That unusually specific
name and biographical context support a high-confidence index identity, but a
rejected job offer is not an affiliation. The article also names Bette's sister
as Lin Balliet Gregory and places her with OSS in Istanbul. Because it does not
print Ellin's middle name, married name, rank, or private identifier, the
adjacent Ellin M. Balliet row is published only as a probable identity.

Stefano Pruneri's article in *Bollettino Storico Alta Valtellina* identifies
Sergeant Bennie A. Ballone, born in 1921, as a member of OSS Operational Group
Santee who died in the April 13, 1945 crash of B-24 H *Queenie*. A derived
Italian historical article provides corroborative discovery context. The
uncommon exact name, middle initial, sergeant grade, and OSS unit make the
identity probable, not high-confidence, because neither source reproduces the
index's private identifier or directly links the personnel file. The evidence
documents OSS service, not a pre-OSS employer or predecessor assignment.

Mary J. Ballew, Robert H. Balliet, Dorman L. Ballinger, Harold E. Ballou, May L.
Ballou, Lyle B. Balluf, and Georges S. Bally remain unresolved after official
index context, CIA Reading Room, current Library of Congress API, exact-name
OSS, employment, occupation, newspaper, obituary, directory, institutional,
and archival searches. All ten profiles retain an explicit Box 33
archival-review path. No authenticated NARA Catalog API request was made, no
credential was accessed, and no raw response, copyrighted page, full private
identifier, home address, or people-finder data was stored in the public
projection.

## Page-twenty-one Balog-through-Balvott pathways, Batch 135

`research/evidence-page-twenty-one-balog-through-balvott-pathways_batch-135_2026-08-01.json`
records ten contiguous rows from Charles Balog through Harold J. Balvott on
PDF page 21. The page was rendered at 300 dpi and inspected at original
resolution. All 46 printed rows match the parsed names, initials, grades or
ranks, identifier-column occupancy, boxes, notes, and archive locations. Full
private identifiers remain in SQLite only.

The strict evidence bundle contains 16 source records, four organizations,
four affiliations, seven claims, 19 claim-source links, ten person updates,
and ten terminal research attempts. The bundle passed schema validation and
replayed idempotently.

The June 13, 1939 *Congressional Record* names Henry H. Balos alongside Bruce
Humphries, Inc. and United Publishers Association, Inc. in a publishing-trade
context. It does not state that either organization employed him, define the
relationship, or establish an immediate pre-OSS chronology. Both relationships
therefore remain medium-confidence professional affiliations. A 1920 *Harvard
Crimson* item supplies earlier exact-name context but is not an employer claim.

The University of Pennsylvania's institutional obituary and a 1934 issue of
*The Jewish Criterion* support a probable Henry H. Balter identity and Wharton
student status. A November 1941 issue of *The Nuntius*, corroborated by a later
institutional bibliography, supports a probable James H. Baltzell identity and
University of Illinois student status. Neither educational relationship is
classified as employment. John M. Balsamo retains the earlier qualified Wall
Street telegrapher occupation-only result; the renewed search found no named
employer.

Charles Balog, Leslie S. Balogh, James J. Balopitos, Ferdinand A. Balsamo, Hugh
C. Balsinger, and Harold J. Balvott remain unresolved after staged official
context, CIA Reading Room, current Library of Congress API, exact-name OSS,
employment, occupation, newspaper, obituary, directory, institutional, and
archival searches. All ten profiles route to Box 33 or 34 review for the
missing identity, chronology, and employment evidence.

No authenticated NARA Catalog API request was made, no credential was
accessed, and no raw API response, full private identifier, copyrighted page,
home address, relative's details, or people-finder data was stored in the
repository or public projection.

## Page-thirty-three Berg-through-Berge pathways and numeric-rank audit, Batch 191

`research/evidence-page-thirty-three-birger-berg-through-walter-berge-pathways_batch-191_2026-08-05.json`
records ten contiguous page-33 rows from Birger Berg through Walter A. Berge
Jr. Page 33 was rendered at 300 dpi and visually checked. John W. Berg III's
seven-digit value is visibly printed in the rank column rather than the serial
column. A parser-wide audit located seven other all-numeric rank cells on pages
162, 184, 275, 281, 292, 293, and 336; each was visually confirmed. Parser
version `bbox-columns-v7` preserves every raw cell privately, normalizes the
value as a probable identifier, leaves rank unknown, and masks the value in all
public profiles, search data, and downloads. The replay ledger now contains 95
reviewed pages and terminal decisions for all 31 warning rows.

The strict evidence bundle contains nine sources, three organizations, eight
affiliations, thirteen claims, 35 claim-source links, ten person updates, and
ten terminal research attempts. An exact official officer-identifier match
confirms Harold Lincoln Berg; a county veterans memorial reports his 1940
Border Publishing employment, which remains a medium-confidence last-civilian-
employer claim until the underlying draft-registration image is inspected.
Exact official Army matches confirm Osmund A. Berg, Peter Berg, Trygve Berge,
and Walter A. Berge Jr. Their Army-entry records support broad civilian
occupation groups, not named employers. The Denver Public Library documents
Osmund, Peter, and Trygve in the 99th Infantry Battalion; only Trygve's path is
published as a qualified probable immediate assignment because a corroborating
record places the same identified person in OSS NORSO II and unit history
documents NORSO recruitment from the 99th. Morris Berg's earlier reviewed CIA
profile was carried forward without duplicating claims.

Birger Berg, Charles Berg, John W. Berg III, and Mary J. Berg remain unresolved
and route to Box 51. The `Luxemb` note on Charles Berg's row remains
uninterpreted. No authenticated Catalog request, credential, raw API response,
full private identifier, or unsupported employer claim was used or published.

## Page-thirty-three Berger-through-Bergin pathways, Batch 192

`research/evidence-page-thirty-three-cecile-berger-through-edward-bergin-pathways_batch-192_2026-08-06.json`
records ten contiguous page-33 rows from Cecile M. Berger through Edward F.
Bergin. Page 33 was rendered at 300 dpi and visually checked against every raw
field. The printed rows, ranks or grades, identifier-column occupancy, Box 51,
and archive locations all match the immutable source records. Private
identifiers remain in SQLite only and are masked in all public surfaces.

The strict evidence bundle contains nine sources, two organizations, six
affiliations, twelve claims, ten person updates, and ten terminal research
attempts. Exact private-identifier matches in the official Army merged file
confirm Harold Berger, Milton A. Berger, Martial L. Bergeron, Lawrence W.
Bergheimer, and Edward F. Bergin. The corresponding official occupation codes
support general-office-clerk, lawyer-or-judge, broad nonprocess-manufacturing,
student, and stock-clerk categories. Except for Milton, these sources name no
civilian employer.

A reputable obituary reports that Milton practiced law in New York before Army
service. In combination with his exact official identifier and lawyer-or-judge
occupation code, the evidence supports high-confidence private law practice as
his last civilian self-employment. It does not establish the immediate
pre-OSS affiliation. A contemporary issue of *The Cache American* supports a
probable match between the indexed Tharrel A. Bergeson and North Cache High
School graduate Tharrel Ann Bergeson; this is published as student status, not
employment. Cecile M. Berger, G. B. Berger, Jane M. Berger, and Morris Berger
remain unresolved and route to Box 51 review. A prominent Harold Berger judge
namesake and Morris Berger name candidates were explicitly rejected.

The Army code-list pages and the newspaper page were visually inspected before
publication. No authenticated Catalog request, credential, raw API response,
full private identifier, copyrighted page, unsupported employer claim, or
irrelevant personal detail was stored or published.

## Page-thirty-three Bergman-through-Berkshire pathways and reviewed duplicate, Batch 193

`research/evidence-page-thirty-three-justin-bergman-through-chester-berkshire-pathways_batch-193_2026-08-06.json`
records ten contiguous page-33 people from Justin Bergman Jr. through Chester
F. Berkshire. Page 33 and the cross-referenced Louis Borin row on page 45 were
rendered at 300 dpi and visually checked. The same private identifier is visibly
printed for the `BERIN, LOUIS` and `BORIN, LOUIS` rows, while the boxes differ.
A human review decision therefore supersedes the Berin entity into the Borin
entity without deleting either immutable source record. Both index spellings,
pages, boxes, and archival locations remain visible on the canonical public
profile; the superseded entity stays in the private audit database and is
excluded from active-entity denominators.

Parser version `bbox-columns-v7` also handles the identical `Jr.` text printed
in two cells on Justin Bergman's row. It preserves both raw cells while emitting
the normalized display name `Justin Bergman Jr.` once and recording the
normalization note. A unit regression fixture protects that behavior.

The strict evidence bundle contains four official sources, six affiliations,
twelve claims, thirty claim-source links, ten person updates, and eleven durable
research attempts, including an evidence-integrity checkpoint for Abram
Bergson. Exact official Army identifier matches confirm Justin Bergman Jr.,
Ralph F. Bergman, Anthony H. Bergson, Louis Borin, Meyer Beringer, and Chester
F. Berkshire. The reviewed Army occupation codes support actor, radio operator,
secretary, consumer salesman, general-industry clerk, and general-farmer
categories. These are occupation findings, not named-employer evidence. Stanley
Bergmann, Raymond E. Bergstrom, Mary S. Berkeley, and William H. Berkeley remain
unresolved and route to archival review. Abram Bergson's existing University of
Texas employment claim was carried forward without duplication.

The official Army bulk file and its documentation were used transiently and
were not committed. No authenticated Catalog request, credential, raw API
response, full private identifier, copyrighted page, or unsupported employer
claim was stored or published.

## Page-thirty-three and thirty-four Berletic-through-Bernard pathways, Batch 194

`research/evidence-page-thirty-three-thirty-four-berletic-through-howard-bernard-pathways_batch-194_2026-08-06.json`
records ten contiguous people from Thomas Berletic through Howard F. Bernard.
Pages 33 and 34 were rendered at 300 dpi and visually checked against every raw
and normalized source field. The Army occupation-code pages were separately
rendered and checked before the bundle was imported.

The strict evidence bundle contains seven sources, five affiliations, nine
claims, twenty-seven claim-source links, ten person updates, and ten durable
research attempts. Exact private-identifier matches in the official Army bulk
file confirm Jacob B. Berlin, Sidney Berlin, and Max L. Berman and link the Sam
Berman index row to a commercial-artist Army record. The Berlin and Max Berman
records support only broad repairman-or-mechanic, general-office-clerk, and
retail-manager categories. They name no employer.

Two official CIA histories independently identify an OSS cartoonist or
caricaturist named Sam Berman. The exact Army commercial-artist occupation and
a Smithsonian Archives of American Art item documenting Sam Berman among
caricaturists in 1934 provide two additional compatible identifiers beyond the
name. The resulting public identity is high-confidence, while the two prewar
occupations remain medium-confidence and qualified. No client, publication,
studio, or named employer is inferred, and neither occupation is promoted to
the immediate pre-OSS affiliation.

Thomas Berletic, Theodore F. Berlinski, Dorothy D. Berman, Jack C. Berman,
Heloise A. Bernard, and Howard F. Bernard remain unresolved and route to Box 52
archival review. Jack C. Berman's commissioned-officer identifier was absent
from the enlisted-focused merged file, whose documented omissions prevent
treating that absence as disproof. No authenticated Catalog request, credential,
raw API response, full private identifier, copyrighted page, or unsupported
employer claim was stored or published.

## Page-thirty-four Bernard-through-Bernstein pathways, Batch 195

`research/evidence-page-thirty-four-jules-bernard-through-blanche-bernstein-pathways_batch-195_2026-08-06.json`
records ten contiguous people from Jules E. Bernard through Blanche Bernstein.
Page 34 was rendered at 300 dpi and visually checked against every raw and
normalized source field. The official Army occupation-code page was separately
rendered at 220 dpi and checked before the bundle was imported. The unusual
`SP X 2/c` and `pVT` strings remain exactly as printed; the former is not
expanded or assigned to a service category without supporting evidence.

The strict evidence bundle contains eight sources, two organization records,
three affiliations, seven claims, fifteen claim-source links, ten person
updates, and ten durable research attempts. An exact private-identifier match
confirms Jean D. Bernier and dates an official Army-entry occupation code to
August 4, 1943. NARA's code table defines code 227 as waiters and waitresses,
except private family. The code names no employer, establishment, location, or
Army-to-OSS sequence.

A contemporary Boston University alumni notice gives Roger P. Bernique's rare
exact name, a compatible Captain rank, December 1942 Military Intelligence
School chronology, OSS Indochina assignment, and an individual law practice he
would resume in New Bedford. The practice is published as self-employment and
documented prewar evidence, not as the immediate pre-OSS affiliation or last
civilian employer because the notice does not state its original dates or
pre-service sequence.

The September 1934 issue of *The Record of Sigma Alpha Epsilon* identifies
Harry L. Berno, Ohio Delta class of 1927, as vice president of the W. H. Davie
Seal Company in Cleveland. A February 1952 notice independently repeats his
name and class year and identifies his World War II colonel rank. William J.
Rust's 2020 research essay supplies the precise locator for Berno's January 1945
`OSS/SEAC Mission Report`: NARA RG 226, Entry A1 99, box 61. This combination
supports a high-confidence identity and a high-confidence 1934 employer, while
the eight-year gap prevents labeling the employer immediate or final before
wartime service. The underlying Box 61 report still requires direct review.

Philip B. Berns remains an explicit conflict. The private identifier printed in
the visually clear index row resolves to Donald J. Kreusch in the official Army
merged file. The public claim explains the mismatch while withholding the
identifier itself, and no Army entry date, occupation, birth-year code, or other
attribute from the incompatible record is assigned to Philip. Jules E. Bernard,
Melba M. Bernard, Gerard J. Bernier, Veronica Bernier, Aaron D. Bernstein, and
Blanche Bernstein remain unresolved after the minimum protocol and route to Box
52 review. The later West Point Aaron D. Bernstein and the prominent economist
Blanche Bernstein remain rejected namesake candidates until index-specific
identifiers corroborate them.

The official Army bulk file, Boston University PDF, and SAE periodicals were
used transiently for visual verification and were not committed. No
authenticated Catalog request, credential, raw API response, full private
identifier, copyrighted page, or unsupported employer claim was stored or
published.

## Page-thirty-four Bernstein pathways, Batch 196

`research/evidence-page-thirty-four-irvin-bernstein-through-shirley-bernstein-pathways_batch-196_2026-08-06.json`
records ten contiguous people from Irvin E. Bernstein through Shirley D.
Bernstein. Page 34 was rendered at 300 dpi and visually checked against every
raw and normalized source field. The official Army occupation-code pages were
also rendered and checked before import.

The strict evidence bundle contains nine sources, four organization records,
eight affiliations, thirteen claims, thirty-four claim-source links, ten person
updates, and ten durable research attempts. Exact private-identifier matches in
the official Army merged file confirm Irvin E. Bernstein, Irving Bernstein,
Nahum A. Bernstein, and Philip M. Bernstein. The associated entry records
support only grouped lawyer-or-judge and clerk occupations, and student status;
they name no civilian employer, school, or direct Army-to-OSS sequence.

The Department of Labor's author biography and the University of California's
memorial independently identify labor historian Irving Bernstein and date his
Brookings fellowship, Bureau of Labor Statistics industrial-economist role,
National War Labor Board hearing-officer assignment, 1943 military entry, and
later OSS Research and Analysis service. The timeline is strong, but it does
not establish a direct National War Labor Board-to-OSS transfer. Brookings is
therefore modeled as a professional fellowship and the two federal roles as
government assignments, not civilian employers or immediate OSS affiliations.

A CIA-hosted image of a contemporary newspaper article corroborates the rare
Nahum A. Bernstein identity and lawyer occupation after OSS service, while the
exact Army record independently places the grouped lawyer-or-judge occupation
at June 1943 entry. Neither source names a pre-OSS law firm. Separate publisher
and professional biographies explicitly identify Peter L. Bernstein's civilian
OSS service and subsequent Army Air Forces work. Both support his 1941 Federal
Reserve Bank of New York research job as the best-supported last civilian
employer, qualified as probable rather than explicit immediacy.

James J. Bernstein, Jeanette Bernstein, Marjorie J. Bernstein, Milton
Bernstein, and Shirley D. Bernstein remain unresolved after the minimum online
protocol and route to Box 52 review. The prominent Joseph Milton Bernstein is
retained only as a rejected namesake candidate. The official Army bulk file and
occupation tables were used transiently and were not committed. No authenticated
Catalog request, credential, raw API response, full private identifier,
copyrighted page, or unsupported employer claim was stored or published.

## Page-thirty-four Berntsen-through-Berry pathways, Batch 197

`research/evidence-page-thirty-four-berntsen-through-clifford-berry-pathways_batch-197_2026-08-06.json`
records ten contiguous people from Henry B. Berntsen through Clifford J.
Berry. Page 34 was rendered at 300 dpi and visually checked against every raw
and normalized source field. The official Army occupation-code pages and the
relevant page of the Seventh Army general orders were separately rendered and
checked before import.

The strict evidence bundle contains eight sources, two organization records,
six affiliations, ten claims, twenty-two claim-source links, ten person
updates, and ten durable research attempts. Exact private-identifier matches
in the official Army merged file confirm Anthony E. Berra and Clifford J.
Berry. Their entry records support only the grouped occupations managers and
officials not elsewhere classified, and mechanics and repairmen not elsewhere
classified; neither record names an employer.

Seventh Army General Orders No. 295 identifies Charles M. Bernuth by exact name
and officer identifier as an OSS captain awarded the Silver Star. A New York
Times family-paid obituary independently reports that he joined Bernuth Lembcke
Company, served as a cavalry officer at Fort Riley during World War II, and was
then recruited into OSS. The company is therefore modeled as his high-
confidence last civilian employer, and the Army cavalry assignment as his
high-confidence immediate pre-OSS affiliation.

A direct 4 May 1944 OSS survey preserved by the Hoover Institution identifies
Victor H. Berruti by exact name and private identifier, states that he entered
the Army in May 1943 and was recruited for OSS, and records that he had been a
printer in civilian life. The Army is modeled as his confirmed immediate
pre-OSS affiliation and printer as a confirmed occupation; no named civilian
employer is invented. Henry B. Berntsen, Stanley E. Berntsen, Malcolm E.
Berrett, Walter J. Berridge, Alfoster Berry, and Carolyn Berry remain unresolved
after the online protocol and route to Box 52 or 53 archival review.

The official Army bulk file, occupation tables, Seventh Army orders, and OSS
survey were used transiently for verification and were not committed. No
authenticated Catalog request, credential, raw API response, full private
identifier, copyrighted page, or unsupported employer claim was stored or
published.

## Page-thirty-four Berry pathways, Batch 198

`research/evidence-page-thirty-four-clyde-berry-through-patrick-berry-pathways_batch-198_2026-08-06.json`
records ten contiguous people from Clyde B. Berry through Patrick J. Berry,
Jr. Page 34 was rendered at 300 dpi and visually checked against every raw and
normalized source field. The official Army technical-documentation and
occupation-code pages were separately inspected before import.

The strict evidence bundle contains four sources, three affiliations, six
claims, fifteen claim-source links, ten person updates, and ten durable
research attempts. Exact private-identifier matches in the official Army
merged file confirm Dan P. Berry, Edward S. Berry, and Patrick J. Berry, Jr.
Their entry records support only the grouped occupations secondary-school
teacher or principal, financial-institution clerk not elsewhere classified,
and general-office clerk. The records name no school, financial institution,
office, employer, or direct Army-to-OSS sequence, so those categories remain
qualified occupation evidence and are excluded from verified-employer counts.

Clyde B. Berry, Floyd D. Berry, Harold A. Berry, James W. Berry, Jr., Lawrence
G. Berry, Maurice Berry, and Olivia M. Berry remain unresolved after the
minimum online protocol and route to Box 53 review. A one-page local-history
profile of a same-name Maurice Berry was rendered and inspected; its account of
104th Infantry Regiment service provides neither the indexed private identifier
nor an OSS connection and is retained only as a rejected candidate.

The official Army bulk file, technical documentation, occupation tables, and
the rejected local-history candidate were reviewed transiently and were not
committed. No authenticated Catalog request, credential, raw API response, full
private identifier, copyrighted page, or unsupported employer claim was stored
or published.

## Pages-thirty-four-and-thirty-five Berry-through-Bertin pathways, Batch 199

`research/evidence-pages-thirty-four-thirty-five-pierce-berry-through-andre-bertin-pathways_batch-199_2026-08-06.json`
records ten contiguous people from Pierce F. Berry through Andre V. Bertin.
Pages 34 and 35 were rendered at 300 dpi and visually checked against every raw
and normalized source field. The official Army technical-documentation pages
44-46 and occupation-code pages 171 and 174 were separately rendered and
checked before import.

The strict evidence bundle contains five sources, one normalized organization,
three affiliations, five claims, twelve claim-source links, ten person updates,
and ten durable research attempts. Exact private-identifier matches in the
official Army merged file confirm Constantin S. Bertakis and Andre V. Bertin.
The latter record's damaged or shifted name field is documented without turning
it into a public name variant. Their entry records support only skilled radio-
and-phonograph-manufacturing work and a general-office-clerk occupation; neither
record names a civilian employer, workplace, or direct Army-to-OSS sequence.

Commander Demetries Grimes's historical account places Bertakis by uncommon
name, middle initial, and T/5 grade in Greek Operational Group I and states that
the Greek OSS groups were formed from the 122nd Infantry Battalion at Camp
Carson. The 122nd is therefore modeled as Bertakis's high-confidence,
strongly-date-bounded, best-supported immediate military assignment. The claim
remains explicit that the reviewed source does not state his person-specific
transfer date, and the affiliation is not counted as civilian employment.

Pierce F. Berry, Gilbert M. Bers, Malcolm Berschn, Carol Bershad, Wilson M.
Berta, Arthur B. Berthold, Katherine H. Berthold, and Felix L. Berti remain
unresolved after the minimum online protocol and route to Box 53 review.
Postwar State Department library and interagency records for an Arthur B.
Berthold were retained only as rejected research leads because they neither
directly identify the indexed person nor document pre-OSS employment.

The official Army bulk file, technical documentation, and occupation tables
were reviewed transiently and were not committed. No authenticated Catalog
request, credential, raw API response, full private identifier, copyrighted
page, or unsupported employer claim was stored or published.

## Page-thirty-five Bertini-through-Berzon pathways, Batch 200

`research/evidence-page-thirty-five-geno-bertini-through-bernard-berzon-pathways_batch-200_2026-08-06.json`
records ten contiguous people from Geno L. Bertini through Bernard M. Berzon.
Page 35 was rendered at 300 dpi and checked against every raw and normalized
source field. The official Army field-layout page 65 and occupation-code page
171, a Reagan Library biographical sheet on physical page 8, and a contemporary
Rahway obituary on physical page 5 were separately rendered and visually
checked before import.

The strict evidence bundle contains seven sources, one normalized organization,
two affiliations, six claims, fifteen claim-source links, ten person updates,
and ten durable research attempts. The exact private identifier beside Armand
G. Bertolo resolves to Murray Markowitz in the official Army merged file. That
conflict is public and inspectable, but no incompatible Army attribute is
assigned to Bertolo. Bernard M. Berzon's exact identifier confirms identity.
The fixed-width field layout places his civilian occupation in columns 70-72;
the recorded code 175 resolves on the official table to `1-75. Salespersons`.
It does not name an employer, product, workplace, exact role, or Army-to-OSS
sequence.

The rare George G. Berzinec name is supported by a Reagan Library case-file
biographical sheet and an independent 1988 local obituary that both explicitly
document OSS service. A scholarly account supplies the documented Jerzy
Berzinec and Berziniec variants, an Olas family bridge, and a prewar Viestnik
editorship. The editorship is published only as a medium-confidence professional
affiliation, not employment or an immediate predecessor. The scholarly account
calls him a priest in 1935 while his later biographical sheet gives 1936 as his
ordination year; both statements are preserved as a visible conflict. The other
seven people remain unresolved after the minimum online protocol and route to
Box 53 review.

The official Army bulk file and technical documents, Reagan Library PDF,
newspaper scan, page renderings, and extracted text were reviewed transiently
and were not committed. No authenticated Catalog request, credential, raw API
response, full private identifier, full copyrighted page, or unsupported
employer claim was stored or published.

## Page-thirty-five Besancon-through-Bessermann pathways, Batch 201

`research/evidence-page-thirty-five-robert-besancon-through-molly-bessermann-pathways_batch-201_2026-08-06.json`
records ten contiguous people from Robert M. Besancon through Molly Bessermann.
Page 35 was rendered at 300 dpi and checked against every raw and normalized
source field. The official Army field-layout page 65 and occupation-code pages
173-175, Frank Bessac oral-history transcript pages 1-3, and the University of
Geneva diploma register page containing Molly Bessermann were separately
rendered and visually inspected before import.

The strict evidence bundle contains thirteen sources, seven normalized
organizations, eleven affiliations, eighteen claims, forty-three claim-source
links, ten person updates, and ten durable research attempts. Exact private-
identifier matches in the official Army merged file confirm Anthony E.
Beshensky, Frank B. Bessac, and Albert G. Besser. Alexander Besio's identifier
resolves to Alexander Bosio; that one-letter conflict is public and the source
spelling is not silently replaced. Broad Army-entry occupation codes for metal-
product fabrication, textile manufacturing, electrical-machinery
manufacturing, and foremen not elsewhere classified are retained only as
qualified evidence and do not identify employers.

Bessac's University of Montana first-person oral history explicitly documents
Fort Riley cavalry training immediately before OSS recruitment and separately
documents College of the Pacific and Stockton Junior College student status.
The educational affiliations are not classified as employers. The CIA's
official artist account, Smithsonian National Postal Museum record, and
Arlington County collection record support Auriel Bessemer's high-confidence
identity and a paid 1939-1940 federal mural commission. A contemporary account
of Representative Peter Welch's medal presentation supports Albert Besser's
Army Reserve-to-OSS pathway; an obituary's Yale chronology remains qualified
student evidence. The University of Geneva's official register supports Molly
Bessermann's 1942-1943 interpreter-program diploma, not an employment claim.

Robert M. Besancon, Justina Besharov, Howard J. Besnia, and William C. Bessemer
retain explicit archival-review outcomes for unresolved employer questions.
The official Army bulk file, technical documents, PDF page renderings, and
transient source copies were not committed. No authenticated Catalog request,
credential, raw API response, full private identifier, full copyrighted page,
or unsupported employer claim was stored or published.

## Page-thirty-five Bessho-through-Bettum pathways, Batch 202

`research/evidence-page-thirty-five-naotomi-bessho-through-leif-bettum-pathways_batch-202_2026-08-06.json`
records ten contiguous people from Naotomi Bessho through Leif L. Bettum. PDF
page 35 was rendered at 300 dpi and every printed field in rows 26-35 was
checked against the extraction. The merged Military Intelligence Service
registry's name page 10 and row-aligned service-note continuation page 219 were
also rendered at 300 dpi and inspected together before import.

The strict evidence bundle contains six sources, four normalized
organizations, four affiliations, five claims, ten claim-source links, ten
person updates, and ten durable research attempts. NARA Entry 211 explicitly
identifies Captain Marcel N. Bessony on detached service from the French Army
to OSS SCI Unit Z in Genova. The index's lieutenant grade and the later captain
description are both retained; no promotion date is inferred.

Richard Kiyoji Betsui is confirmed by an exact private officer identifier in
the OSS index and the merged MIS registry. The registry pairs his Camp Savage
class with a row-aligned CBI and
OSS Detachment 101 service note. A 442nd veterans institution's documented
chronology independently places him at Camp Shelby, Fort Benning, and Camp
Savage, while a contemporary 1943 newspaper identifies his earlier recruit-
class executive-officer role. Waialua High School is published as a qualified,
medium-confidence last civilian employer because the school and occupation are
well supported but the exact separation date is not.

Naotomi Bessho, John C. Bethea, Patricia D. Bethke, Nogah Bethlanmy, Elizabeth
R. Betts, Virginia Betts, and Leif L. Bettum retain explicit archival-review
outcomes. The plausible Evelyn Gloria Ohman candidate for Evelyn O. Betts
remains ambiguous pending Box 54 confirmation. Search-result pages, the
unreviewed NARA Catalog response body, technical PDF renderings, and transient
source copies were not committed. No authenticated Catalog request,
credential, raw API response, full private identifier, full copyrighted page,
or unsupported employer claim was stored or published.

During release QA, a formerly reviewed veterans-association document URL was
found to redirect to an unrelated domain. That citation and its durable source
record were removed before publication. The affected identity claim remains
independently supported by the exact private identifier shared by the NARA
index and the visually reviewed MIS registry; no person-level conclusion was
changed.

## Page-seven and page-twenty-four Alvey-through-Ambelang and Baron pathways, Batch 305

`research/evidence-page-seven-louis-r-alvey-jr-through-charles-d-ambelang-and-paul-baron-pathways_batch-305_2026-08-19.json`
records ten previously unresearched people: nine contiguous rows from Louis R.
Alvey Jr. through Charles D. Ambelang on PDF page 7 plus Paul Baron on PDF page
24. Both index pages and the relevant NARA occupation-code pages were visually
checked. The official Army merged file was searched by private identifier
outside version control; no raw Army record, full identifier, or authenticated
Catalog response was retained.

The strict evidence bundle contains nine sources, two normalized organizations,
six affiliations, eleven claims, twenty-three claim-source links, ten person
updates, and ten durable research attempts. Exact full-name and private-
identifier agreement confirms Louis R. Alvey Jr., Edwin D. Amado, Raymond H.
Amador, and Ralph G. Amato. Their Army-entry codes support qualified categories
for machinists; chauffeurs and several kinds of drivers; students; and
longshoremen and stevedores. These categories name no employer, school, port,
union, workplace, or immediate Army-to-OSS transition.

The 1942 University of Wisconsin yearbook places Charles Ambelang among Phi
Delta Phi's juniors, and a February 1943 Wisconsin alumni publication reports
Charles D. Ambelang attending officer-candidate school at State College,
Mississippi. Brian Masaru Hayashi's scholarly article cites a circa-August 1945
Charles D. Ambelang OSS record in Entry 224, Box 12. Together these sources
support a high-confidence identity, a student relationship, and a military-
training assignment. They do not establish a civilian employer or prove either
affiliation was immediately pre-OSS. Charles F. Amacker, Richard J. Amador,
Anthony R. Amarante, Chintamye Amatayakul, and Paul Baron remain unresolved and
route to their indexed boxes. The unfamiliar `SP P 1/c` string remains exactly
as printed and unclassified; later diplomatic references for Chintamye
Amatayakul remain rejected as postwar evidence.

No authenticated Catalog request, credential, raw API response, full private
identifier, full copyrighted page, or unsupported employer claim was stored or
published.

## Page-fifty-three Brock-through-Broder pathways, Batch 306

`research/evidence-page-fifty-three-mary-brock-through-stephen-broder-pathways_batch-306_2026-08-19.json`
records ten contiguous previously unresearched people from Mary Brock through
Stephen Broder on PDF page 53, all indexed to Box 81. The page and both relevant
NARA occupation-code pages were rendered and visually checked. The official
Army merged file was searched by private identifier outside version control; no
raw Army record, full identifier, or authenticated Catalog response was
retained.

The strict evidence bundle contains six sources, two affiliations, four claims,
eight claim-source links, ten person updates, and ten durable research attempts.
Exact full-name and private-identifier agreement confirms Elvin Brockman Jr. and
Harold I. Brodbeck. Brockman's official code records student status at Army
entry on June 30, 1945; it names no school, course, degree, employer, or OSS
sequence. Brodbeck's official code records a broad chauffeur-and-driver category
at Army entry on November 5, 1941; it names no workplace, vehicle type, exact
role, employer, or OSS sequence.

Mary Brock, Mildred L. Brockdorff, Paul Brockett, Muriel P. Brockhurst, Eric
Brockman, William Brockman, Jean M. Brodell, and Stephen Broder remain unresolved
and route to Box 81. A 1942 NBC reporter named Mary Brock, postwar State
Department evidence for Mildred L. Brockdorff, and a 1944 Washington newspaper
item for Jean Marie Brodell were reviewed but remain unassigned because they
lack independent OSS, identifier, or Box linkage. The Brodell candidate's
spouse and his assignment are not treated as her affiliation.

No authenticated Catalog request, credential, raw API response, full private
identifier, full copyrighted page, or unsupported employer claim was stored or
published.

## Page-fifty-three Broderick-through-Brogan pathways, Batch 307

`research/evidence-page-fifty-three-lawrence-broderick-through-william-brogan-pathways_batch-307_2026-08-19.json`
records ten contiguous previously unresearched people from Lawrence P.
Broderick through William Brogan on PDF page 53, all indexed to Box 81. The
source page and official occupation-code pages 171, 175, and 304 were rendered
and visually checked. The official Army merged file was searched by private
identifier outside version control; no raw Army record, full identifier, or
authenticated Catalog response was retained.

The strict evidence bundle contains nine sources, two organization records,
four affiliations, nine claims, eighteen claim-source links, ten person
updates, and ten durable research attempts. Exact private-identifier agreement
confirms Lawrence P. Broderick despite the official file's Laurence spelling,
and supports only student status at Army entry. Exact identifier agreement
also confirms Earl D. Brodie and supports only the residual civilian category
“professional occupations, not elsewhere classified.” Neither official code
names an employer or establishes the exact OSS sequence.

William J. Broere is confirmed by exact identifier agreement and the 1948
volume *Islip Town's World War II Effort*, which independently matches his
July 3, 1942 service-entry date and documents his OSS service. Printed page
724 explicitly identifies his prior work as shop maintenance mechanic at the
Grumman Aircraft Plant in Bethpage. The project preserves that historical name
on the affiliation and normalizes the organization separately as Grumman
Aircraft Engineering Corporation. The same source sequences Army Air Forces
service before the documented OSS role, so that pathway is published only as
qualified military-assignment evidence and is not labeled civilian employment.

The November 1981 Department of State magazine obituary for Henry Brodie and
the April 1946 *Field Artillery Journal* article about Captain James H. Brodie
support probable identities only. The former documents a Navy veteran and OSS
economic analyst in London but does not carry the Box 81 identifier; the latter
documents OSS examination of a landing system but does not establish that its
inventor served in OSS. David Brodie, Marie R. Brodnax, Albert Brodsky, Jan O.
Broek, and William Brogan remain unresolved. Jan O. M. Broek remains a rejected
namesake lead because no reviewed source links the geographer to OSS or Box 81.

No authenticated Catalog request, credential, raw API response, full private
identifier, full copyrighted page, or unsupported employer claim was stored or
published.

## Page-fifty-eight Bryant-through-Buchanan pathways, Batch 312

`research/evidence-page-fifty-eight-bryant-through-buchanan-pathways_batch-312_2026-08-19.json`
records ten contiguous previously unresearched people from William V. Bryant
through Thomas A. Buchanan on PDF page 58 in Boxes 89-90. The index page and
the relevant official Army occupation-code pages were rendered and visually
checked. The official Army merged file was searched by private identifier
outside version control; no raw row or full identifier was retained.

The strict evidence bundle contains seven sources, no organizations, three
affiliations, six claims, fifteen claim-source links, ten person updates, and
ten durable research attempts. Exact private-identifier and name agreement
confirms John S. Buc Jr. and Jack C. Buchanan. Buc's March 8, 1943 Army-entry
record maps only to the residual textile-products fabrication group. Buchanan's
June 19, 1943 record maps to student status without naming an institution.
Both findings are date-bounded and qualified; neither supplies a named
employer, exact workplace, immediate OSS predecessor, or Army-to-OSS sequence.

Washington and Lee University's institutional finding aid identifies Daniel
Crump Buchanan as a Presbyterian minister, missionary, and teacher in Japan who
worked at the OSS Japanese desk during World War II. The Republic of Korea's
National Institute of Korean History independently lists Daniel C. Buchanan in
1944-1945 OSS and FESI correspondence, corroborating the middle initial and
wartime context. The identity and documented prewar professional affiliation
are published with high confidence, but no mission board, church, school, or
college is inferred as an employer and the affiliation is not labeled immediate
or last civilian.

William V. Bryant, Virginia L. Brydon, Roscoe N. Bryson, Albert A. Buccina,
Joseph Buccola Jr., Henry C. Buchan Jr., and Thomas A. Buchanan remain
unresolved and route to Box 89 or 90 review. Buccina's unusual nine-digit value
is preserved exactly as printed rather than silently corrected. No authenticated
Catalog request, credential, raw API response, full private identifier, full
copyrighted page, or unsupported employer claim was stored or published.

## Page-fifty-eight Brussel-through-William-C.-Bryant pathways, Batch 311

`research/evidence-page-fifty-eight-brussel-through-william-c-bryant-pathways_batch-311_2026-08-19.json`
records ten contiguous previously unresearched people from Willy J. Brussel
through William C. Bryant on PDF page 58 in Box 89. The index page and the
relevant Army occupation-code page were rendered and visually checked. The
official Army merged file was searched by private identifier outside version
control; no raw row or full identifier was retained.

The strict evidence bundle contains five sources, no organizations, one
affiliation, three claims, seven claim-source links, ten person updates, and ten
durable research attempts. Exact private-identifier and full-name agreement
confirms Andrew Brutz. His Army-entry record dates entry to October 27, 1941
and carries civilian occupation code 882; the official code list maps that value
only to the broad residual group “Foundry occupations, n.e.c.” The site therefore
publishes a qualified occupation, not an employer, named foundry, exact trade,
or proven Army-to-OSS sequence.

A specialist history of United States psychological-warfare organization in
Europe lists Technician Fifth Grade Larry Bruzzese among personnel of the 2677th
Morale Operations Company in Rome and attributes the passage to a November 3,
1944 Donovan commendation. The distinctive exact name and indexed technician
grade support a probable identity only. The source does not establish a
pre-service occupation, employer, or immediate OSS predecessor, so none is
published.

Willy J. Brussel, Alice M. Brust, Robbie L. Bruton, Cloye A. Bryant, Flossie L.
Bryant, George F. Bryant, Kenneth L. Bryant, and William C. Bryant remain
unresolved and route to Box 89 review. A same-name student candidate for Robbie
L. Bruton in North Carolina directories was rejected because no reviewed source
linked that candidate to OSS or supplied a second corroborating identifier.
William C. Bryant remains separate from the adjacent William V. Bryant source
row. No authenticated Catalog request, credential, raw API response, full
private identifier, full copyrighted page, or unsupported employer claim was
stored or published.

## Page-twenty-eight and page-fifty-eight Beck, Brunner-through-Bruskin pathways, Batch 310

`research/evidence-pages-twenty-eight-and-fifty-eight-beck-brunner-through-bruskin-pathways_batch-310_2026-08-19.json`
records John H. Beck on PDF page 28 in Box 45 and nine previously unresearched
people from Frederick J. Brunner through Theodore R. Bruskin on PDF page 58 in
Box 89, skipping the Edward L. Brunner row completed in Batch 309. Both index
pages and all five relevant Army occupation-code pages were rendered and
visually checked. The official Army merged file was searched by private
identifier outside version control; no raw row or full identifier was retained.

The strict evidence bundle contains eight sources, two organizations, seven
affiliations, fourteen claims, twenty-eight claim-source links, ten person
updates, and ten durable research attempts. Exact private-identifier agreement
confirms John H. Beck, Arthur Bruno, Guy D. Bruno, Leonard C. Bruno, and Louis
F. Bruno. Their Army-entry records support, respectively, a general-office
clerk occupation, a grouped barber/beautician/manicurist category, student
status without a named institution, civil engineering, and a residual trades-
and-services category. Each finding is date-bounded and qualified; none is
converted into a named employer or a proven Army-to-OSS sequence.

The current NARA Persons of Exceptional Prominence list independently records
Frederick J. Brunner in the Marine Corps. The official Marine Corps history
*A Different War* expressly identifies Platoon Sergeant Frederick J. Brunner
among Marines serving with OSS in Europe. Those official sources support a
high-confidence enlisted Marine identity, but not a pre-Marine civilian
employer or OSS recruitment date.

Washington State University's institutional memorial gives Arthur Brunstad's
distinctive exact name, 1931 and 1933 chemistry degrees, a chemical-officer
assignment in the 4th Air Force, and later OSS service in Burma. The student
affiliation is kept separate from employment. The 4th Air Force assignment is
published as a qualified probable-immediate military pathway because the
sequence is explicit but the source does not exclude an intervening assignment.
Later employer names in the memorial are not treated as pre-OSS without dates.

Edwin F. Brush, Gilmer G. Brush, and Lieutenant Colonel Theodore R. Bruskin
remain unresolved and route to Box 89 review. The Bruskin rank remains a
commissioned-officer classification from the index, not a resolved biography.
No authenticated Catalog request, credential, raw API response, full private
identifier, full copyrighted page, or unsupported employer claim was stored or
published.

## Page-fifty-three and page-fifty-eight Brooker-through-Brunner pathways, Batch 309

`research/evidence-page-fifty-three-and-fifty-eight-brooker-through-brunner-pathways_batch-309_2026-08-19.json`
records nine contiguous previously unresearched people from Richard M. Brooker
through Harry P. Brooks on PDF page 53 in Box 82, plus Edward L. Brunner on PDF
page 58 in Box 89. Both index pages, the Army technical-documentation pages,
the official occupation-code page, and the CIA correspondence page were
rendered and visually checked. The official Army merged file was searched by
private identifier outside version control; no raw row or full identifier was
retained.

The strict evidence bundle contains nine sources, one organization, two
affiliations, four claims, eleven claim-source links, ten person updates, and
ten durable research attempts. Exact private-identifier and full-name agreement
confirms Edgar N. Brooks. His Army-entry record dates entry to July 17, 1943 and
carries civilian occupation code 513; the official code list maps that value
only to a broad residual miscellaneous-products manufacturing group. The site
therefore publishes an occupation with medium confidence, not an employer,
exact trade, product, plant, or proven Army-to-OSS sequence.

A 1986 letter from Director of Central Intelligence William J. Casey expressly
identifies Ernest Brooks, Jr. as an OSS member who served in London. Two
contemporary judicial opinions independently list Ernest Brooks, Jr. with
Breed, Abbott & Morgan in 1937 and 1938. The exact name and suffix support a
high-confidence OSS identity, while the law-firm affiliation remains a
medium-confidence documented-prewar finding: it is not labeled as the immediate
pre-OSS affiliation or the last civilian employer before service. The
discovery-only biographical entry is retained solely as a contextual bridge and
does not independently support a published claim.

Richard M. Brooker, Earline D. Brooks, Elmer O. Brooks, Everett S. Brooks,
Frank Brooks, Harold L. Brooks, Harry P. Brooks, and Edward L. Brunner remain
unresolved and route to Box 82 or Box 89 review. Exact-name Army, directory,
obituary, newspaper, CIA, and institutional candidates without sufficient
identifier or personnel-file linkage were rejected. No authenticated Catalog
request, credential, raw API response, full private identifier, full
copyrighted page, or unsupported employer claim was stored or published.

## Page-fifty-three Brogger-through-Brooke pathways, Batch 308

`research/evidence-page-fifty-three-arne-brogger-through-elizabeth-brooke-pathways_batch-308_2026-08-19.json`
records ten contiguous previously unresearched people from Arne W. Brogger
through Elizabeth D. Brooke on PDF page 53, all indexed to Box 81. The source
page, two city-directory pages, the Richard Broh handbook page, and Urie
Bronfenbrenner's Cornell Alumni News page were rendered and visually checked.
The official Army merged file was searched by private identifier outside
version control; no raw record or full identifier was retained.

The strict evidence bundle contains fourteen sources, five organization
records, seven affiliations, ten claims, twenty-two claim-source links, ten
person updates, and ten durable research attempts. Contemporary city
directories identify Arne W. Brogger as a New York lawyer in 1938 and in the
U.S. Army in 1942; Cornell's Donovan Nuremberg collection independently names
Major Arne W. Brogger in 1945. The identity and military pathway are published
with high confidence, but no law firm or exact OSS entry date is inferred.
The scholarly *Biographisches Handbuch der deutschsprachigen Emigration nach
1933* explicitly documents Richard Broh's 1945 OSS work and his earlier
freelance journalism in Great Britain, while preserving uncertainty created by
internment and intervening British wartime work.

Exact private-identifier agreement confirms Lester T. Brolliar. Reproduced
34th General Hospital and 110th Medical Battalion rosters document two Army
medical assignments, but their sequence relative to OSS remains unresolved. A
CIA staff list, Cornell institutional biography, and Bronfenbrenner's
first-person alumni account confirm the index's truncated Urie Bronfenbrenne
row as Urie Bronfenbrenner. His University of Michigan doctorate is classified
as student status, not employment, and his explicit Army Air Corps-to-OSS
transition is classified as a military assignment.

Norma Bromberg and Arthur B. Bromberger remain probable identity candidates;
no affiliation is published for either. Eleanor S. Brokaw, William Bromme,
Barbara R. Bronson, and Elizabeth D. Brooke remain unresolved and route to Box
81 review. No authenticated Catalog request, credential, raw API response,
full private identifier, full copyrighted page, or unsupported employer claim
was stored or published.

## Pages-fifty-eight-and-fifty-nine Buchhardt-through-Buckens pathways, Batch 313

`research/evidence-pages-fifty-eight-fifty-nine-buchhardt-through-buckens-pathways_batch-313_2026-08-19.json`
records ten contiguous previously unresearched people from Erik M. Buchhardt
through Ferdinand Buckens on PDF pages 58-59, all indexed to Box 90. Both index
pages, the relevant Army code-list pages, the 1935 Tokyo directory page, and
page 476 of the 1942 Belgian official gazette were rendered and visually
checked. The official Army merged file was searched by private identifier
outside version control; no raw record or full identifier was retained.

The strict evidence bundle contains six sources, one organization record,
three affiliations, seven claims, seventeen claim-source links, ten person
updates, and ten durable research attempts. Exact private-identifier agreement
confirms Joseph A. Buchkowskie and Peter C. Buchta. Their official Army-entry
records establish only broad transportation-equipment and boot-and-shoe
manufacturing occupation groups; neither record names an employer, workplace,
exact trade, or Army-to-OSS sequence.

The private identifier printed for Edgar J. Buck resolves to a differently
named subject in the official Army merged file. The public conflict claim
withholds that unrelated person's name, identifier, occupation, and chronology,
and routes the case to Box 90 and original-card review.

A contemporary 1935 directory identifies Ferdinand Buckens as interpreter at
the Belgian Embassy in Tokyo. Belgium's official gazette independently records
F. Buckens as a consul previously posted in Tokyo before a temporary 1942 New
York assignment. The unusual exact name and diplomatic continuity support a
high-confidence identity and documented prewar government assignment, but the
evidence does not establish an immediate OSS predecessor or a last civilian
employer. Erik M. Buchhardt, Richard S. Buchholz, Rosel A. Bucholz, Daryl L.
Buck, Warren E. Buck, and William N. Buck remain unresolved and route to Box 90
review. No authenticated Catalog request, credential, raw API response, full
private identifier, full copyrighted page, or unsupported employer claim was
stored or published.

## Page-fifty-nine Buckland-through-Bucky pathways, Batch 314

`research/evidence-page-fifty-nine-buckland-through-bucky-pathways_batch-314_2026-08-19.json`
records ten contiguous previously unresearched people from William L. Buckland
through Peter A. Bucky on PDF page 59, all indexed to Box 90. The index page and
the relevant Army code-list pages were rendered and visually checked. The
official Army merged file was searched by private identifier outside version
control; no raw record or full identifier was retained.

The strict evidence bundle contains four official sources, four affiliations,
eight claims, twenty claim-source links, ten person updates, and ten durable
research attempts. Exact private-identifier agreement confirms William L.
Buckland, John W. Buckles, John T. Buckley, and James A. Buckner. Their Army-
entry records respectively establish only a general-farmer occupation, a
residual foundry-occupations group, a general-industry clerk occupation, and an
actor occupation. These codes do not identify a farm, foundry, industry,
production, employer, workplace, self-employment status, or Army-to-OSS
sequence.

Claude W. Buckley, Robert E. Buckley, Vincent L. Buckley, Mildred L. Buckner,
Simon B. Buckner, and Peter A. Bucky remain unresolved and route to Box 90
review. Peter A. Bucky's printed 1st Lt grade remains sufficient for the
commissioned-officer filter, but neither a radiologist-author namesake nor a
prominent Simon B. Buckner military namesake was assigned without direct OSS,
Box 90, private-identifier, or two-person-specific corroborating links. No
authenticated Catalog request, credential, raw API response, full private
identifier, full copyrighted page, or unsupported employer claim was stored or
published.

## Page-fifty-nine Bucky-through-Buegnon pathways, Batch 315

`research/evidence-page-fifty-nine-bucky-through-buegnon-pathways_batch-315_2026-08-19.json`
records ten contiguous previously unresearched people from Thomas L. Bucky
through Raphael Buegnon on PDF page 59 in Boxes 90-91. The index page and the
relevant Army code-list pages were rendered and visually checked. The official
Army merged file was searched by private identifier outside version control;
no raw record or full identifier was retained.

The strict evidence bundle contains four official sources, two affiliations,
five claims, twelve claim-source links, ten person updates, and ten durable
research attempts. Exact private-identifier agreement confirms Francis J.
Bucolo, Bernard J. Budenosky, and Anthony J. Budraitis. The official Army-entry
records establish only Bucolo's sales-clerk occupation on January 16, 1941 and
Budraitis's meatcutter occupation on December 22, 1942. Neither code names an
employer, store, product, shop, market, workplace, or Army-to-OSS sequence.
Budenosky's official record confirms identity and an October 24, 1939 Army-
entry date, but its zero occupation field supports no occupation claim.

Thomas L. Bucky, Anthony Buda, William H. Budd, Adelaide M. Budde, Paul E.
Budrea, Walter A. Budz, and Raphael Buegnon remain unresolved and route to Box
90-91 review. The printed 1st Lt and 2nd Lt grades preserve Bucky, Budrea, and
Buegnon's commissioned-officer classifications, but no unsupported officer
biography or nationality is assigned. No authenticated Catalog request,
credential, raw API response, full private identifier, full copyrighted page,
or unsupported employer claim was stored or published.

## Page-fifty-nine Buehler-through-Bugelli pathways, Batch 316

`research/evidence-page-fifty-nine-buehler-through-bugelli-pathways_batch-316_2026-08-19.json`
records ten contiguous previously unresearched people from Carl Buehler III
through Delmas A. Bugelli on PDF page 59 in Box 91. The index page and relevant
Army documentation were rendered and visually checked. The official Army
merged file was searched by private identifier outside version control; no raw
record, unrelated subject identity, or full identifier was retained.

The strict evidence bundle contains eight sources, two organizations, three
affiliations, seven claims, seventeen claim-source links, ten person updates,
and ten durable research attempts. Exact private-identifier agreement confirms
Andrew P. Bugay; his official Army-entry record documents only the broad miners
and mining-machine operators group on December 29, 1942. No mine, operator,
employer, workplace, duties, or Army-to-OSS sequence is supplied.

Official BCRA archival inventory evidence gives René Darcy as André Germain
Buffard's service name, and a separate mission compilation places that identity
in an OSS/G2 mission. This supports a high-confidence Darcy Buffard identity
without establishing a pre-OSS employer. A 1936 institutional alumni notice
documents Howard C. Bugbee's Goodrich Rubber Co. advertising work and transfer
to Goodrich Company (S.S.) Limited in Singapore; an official 1944 State
Department record corroborates the middle-initial candidate. Because the OSS
index omits the middle initial and no direct Box 91 linkage is available, the
identity and both earlier employments remain visibly qualified.

Delmas A. Bugelli's printed private identifier resolves to a different subject
in the official Army merged file. The unrelated name, identifier, and record
details are withheld, and no evidence is transferred to Bugelli. Six additional
identities remain unresolved and route to Box 91 review. No authenticated
Catalog request, credential, raw API response, full private identifier, full
copyrighted page, or unsupported employer claim was stored or published.

## Page-fifty-nine Bugni-through-Bulfer pathways, Batch 317

`research/evidence-page-fifty-nine-bugni-through-bulfer-pathways_batch-317_2026-08-19.json`
records ten contiguous previously unresearched people from John D. Bugni
through Joseph E. Bulfer on PDF page 59 in Box 91. The index page and relevant
Army code-list pages were rendered and visually checked. The official Army
merged file was searched by private identifier outside version control; no raw
record or full identifier was retained.

The strict evidence bundle contains four official sources, three affiliations,
six claims, fifteen claim-source links, ten person updates, and ten durable
research attempts. Exact private-identifier agreement confirms John D. Bugni,
Albert Buhite, and Irving F. Buhman. Their official Army-entry records establish
only, respectively, a forestry occupation except logging on February 10, 1942,
a broad miscellaneous-products manufacturing occupation on July 5, 1943, and a
checker occupation on January 15, 1944. None of the codes names an employer,
agency, product, industry, workplace, exact duties, or Army-to-OSS sequence.

Conrad W. Buhler, Curt F. Buhler, Henry L. Buisson, Frank L. Bukacek, Milivoj
Bukorovic, Edward R. Bukovatz, and Joseph E. Bulfer remain unresolved and route
to Box 91 review. Search-only Buehler, Kurt, and Bukorović variants are retained
without correcting the index or assigning namesakes. Bulfer's printed
lieutenant grade remains sufficient for the commissioned-officer filter; the
enlisted-only Army merged file cannot disprove an officer record. No
authenticated Catalog request, credential, raw API response, full private
identifier, full copyrighted page, or unsupported employer claim was stored or
published.

## Pages-fifty-nine-sixty Bulfner-through-Bull pathways, Batch 318

`research/evidence-pages-fifty-nine-sixty-bulfner-through-bull-pathways_batch-318_2026-08-19.json`
records ten contiguous previously unresearched people from Mearice W. Bulfner
through Patricia Bull across PDF pages 59-60 in Boxes 91-92. Both index pages
and the relevant Army code-list page were rendered and visually checked. The
official Army merged file was searched by private identifier outside version
control; no raw record, unrelated subject identity, or full identifier was
retained.

The strict evidence bundle contains eight sources, one organization, two
affiliations, six claims, thirteen claim-source links, ten person updates, and
ten durable research attempts. Exact private-identifier agreement confirms
Carlton R. Bulger, but the civilian-occupation value in his official record has
no entry in NARA's published corrected code list. The project therefore
publishes the identity and Army-entry date but no guessed occupation or
employer.

The private identifier printed for Theodore J. Bulinski resolves to a
different subject in the official Army merged file. The unrelated name and
record details are withheld, and an otherwise plausible University of
Minnesota namesake is rejected for lack of Box 91 or identifier linkage.

The uncommon full name Dwight H. Bulkley appears as author of two December 1945
OSS reports in RG 226 and in an independent official FRUS record from Bangkok,
supporting a high-confidence identity without a pre-OSS affiliation. Southern
Oregon University's institutional biography and catalog connect Lucius D.
Bulkley to L. Daniel “Dan” Bulkley, OSS service, a 1939 Pomona College degree,
and unnamed prewar high-school teaching and coaching. The student status and
unnamed employment remain separate, medium-confidence, non-immediate
affiliations; Pomona is not counted as an employer and no high school is
invented. Six further identities remain unresolved and route to Boxes 91-92
review. No authenticated Catalog request, credential, raw API response, full
private identifier, full copyrighted page, or unsupported employer claim was
stored or published.

## Page-sixty Bullard-through-Bundick pathways, Batch 319

`research/evidence-page-sixty-bullard-through-bundick-pathways_batch-319_2026-08-19.json`
records nine newly researched people and a fresh integrity review of Ralph J.
Bunche across PDF page 60 in Box 92. The index page and official Army technical
documentation were visually checked; the official merged file was searched by
private identifier outside version control. No raw record or full identifier
was retained.

The strict bundle contains five sources, one organization, five affiliations,
ten claims, twenty-four claim-source links, nine person updates, and ten durable
research attempts. Exact private-identifier agreement confirms Joe L. Bullock,
Charles A. Bullwinkel, Leland Bunch, Henry Bund, and Billie B. Bundick. The
accepted evidence publishes only four date-bounded occupational groups: general
farm hand, packing/filling/labeling work, an otherwise-unspecified professional
occupation, and general-office clerk. Billie B. Bundick's contemporary school
record separately supports Big Sandy High School graduate status; it is not an
employer. Ralph J. Bunche's already reviewed personnel-file conclusions remain
unchanged. Four unsupported identities route to Box 92 review, while Leland
Bunch's confirmed identity still requires archival review because the official
occupation value is not decoded into a job or employer.

## Page-sixty Bundy-through-Buontempo pathways, Batch 320

`research/evidence-page-sixty-bundy-through-buontempo-pathways_batch-320_2026-08-19.json`
records ten contiguous people on PDF page 60 in Box 92. The strict bundle
contains four official sources, two affiliations, four claims, ten claim-source
links, ten person updates, and ten durable research attempts. Exact private-
identifier agreement confirms Rudolph N. Buonagura and John J. Buoncristiani;
their official Army-entry records support only, respectively, tailor and
draftsman occupational groups on November 25, 1942 and April 3, 1943. No shop,
firm, industry, specialty, workplace, duties, or Army-to-OSS chronology is
inferred. The remaining eight identities route to Box 92 review.

## Page-sixty Buonviso-through-Burdine pathways, Batch 321

`research/evidence-page-sixty-buonviso-through-burdine-pathways_batch-321_2026-08-19.json`
records ten contiguous people from Dora R. Buonviso through Gerald H. Burdine
across Boxes 92-93 on PDF page 60. The strict bundle contains six sources, one
organization, six affiliations, twelve claims, thirty claim-source links, ten
person updates, and ten durable research attempts.

Exact private-identifier agreement confirms Dora R. Buonviso, Max Buran, Ward
A. Burbidge, John J. Burchill, and Gerald H. Burdine. Their dated official
occupational groups remain qualified and name no employer: general-office
clerk; shipping or receiving clerk; chauffeur or driver; messenger, errand, or
office worker; and chauffeur or driver. A January 1942 federal court record and
Harvard's later Nuremberg archive support Charles S. Burdell's high-confidence
identity and documented prewar Justice Department assignment. The evidence does
not show that Justice immediately preceded OSS, so it is neither labeled
immediate nor converted into a civilian-employer claim. Four unsupported
identities route to Boxes 92-93 review. Across Batches 319-321, no authenticated
Catalog request, credential, raw API response, full private identifier, full
copyrighted page, or unsupported employer claim was stored or published.

## Pages-sixty-sixty-one Bureau-through-Burgess pathways, Batch 322

`research/evidence-pages-sixty-sixty-one-bureau-through-burgess-pathways_batch-322_2026-08-19.json`
records ten contiguous people from Lucien Bureau through Elsie J. Burgess
across PDF pages 60-61 in Box 93. Both index pages and the relevant official
Army code-list pages were visually checked. The official merged file was
searched by private identifier outside version control; no raw record, full
identifier, or unrelated subject detail was retained.

The strict bundle contains four official sources, three affiliations, six
claims, fifteen claim-source links, ten person updates, and ten durable research
attempts. Exact private-identifier agreement confirms Frank G. Burford, John K.
Burgan, and the qualified spelling pair Edward H. Burgesono/Burgeson. Their
official Army-entry records support only date-bounded radio-operator,
otherwise-unspecified inspector, and advertising-agent occupational groups.
None names an employer, station, branch, industry, agency, client, duties,
workplace, or Army-to-OSS chronology. The index's `possibly` note and the
official Burgeson spelling remain visible rather than silently correcting the
printed Burgesono row.

Lucien Bureau's printed French sub-lieutenant classification is preserved, but
a discovery-only alias lead lacks Box 93 linkage and remains unresolved. Robert
E. Burger's Library of Congress result was a substring occurrence for Robert
Weisenburger, not an identity match. Those two and five other unsupported
identities route to Box 93 review. No authenticated Catalog request, credential,
raw API response, full private identifier, full copyrighted page, or
unsupported employer claim was stored or published.

## Page-sixty-one Burgess-through-Burke pathways, Batch 323

`research/evidence-page-sixty-one-burgess-through-burke-pathways_batch-323_2026-08-19.json`
records ten contiguous people from William F. Burgess through Francis T. Burke
on PDF page 61 in Box 93. The index page and the relevant NARA Army technical-
documentation pages were visually checked. The official merged Army file was
searched by private identifier outside version control; no raw record, full
identifier, or unrelated subject detail was retained.

The strict bundle contains seven sources, three organization inputs, eight
affiliations, fourteen claims, twenty-six claim-source links, ten person
updates, and ten durable research attempts. Exact private-identifier agreement
confirms Victor A. Burisch, Robert F. Burk, and Edwin M. Burke. NARA's official
records support only machinist, agents-and-appraisers-not-elsewhere-classified,
and student fields. The student code was visually confirmed on physical page
304 of the corrected code list. None names an employer, school, client,
workplace, duties, or Army-to-OSS chronology.

The [Indiana University finding aid](https://archives.iu.edu/catalog/InU-Li-VAE1247)
supports Glenn A. Burgett's distinctive wartime lieutenant and military-lawyer
identity, but not a civilian employer or dated OSS transition. A
[Smith College institutional credit](https://www.smith.edu/libraries/libs/rarebook/exhibitions/dickens/17-dickens-in-america.htm)
documents Marion Calkins Burgweger as Class of 1935, a student relationship
rather than employment. Aleksandar Životić's archive-cited
[scholarly study](https://www.sistory.si/eng/publication/41444) supports Mirko
Leopold Burja's Royal Yugoslav general-staff, Washington military-attaché, and
Argentina military-mission assignments; the evidence does not date his OSS
entry, so no assignment is presented as an unqualified immediate predecessor.

William F. Burgess, Alexander Burjan, and Francis T. Burke remain unresolved
and route to Box 93 review. Edmund M. Burke's established identity and
University of Pennsylvania evidence remain unchanged; an uncorroborated
insurance-company lead stays out of the public claims. The adjacent Francis T.
Burke row in Box 94 remains a possible duplicate, not a merge. No authenticated
Catalog request, credential, raw API response, full private identifier, full
copyrighted page, or unsupported employer claim was stored or published.

## Page-sixty-one Francis-through-Paul Burke pathways, Batch 324

`research/evidence-page-sixty-one-francis-burke-through-paul-burke-pathways_batch-324_2026-08-19.json`
records the ten contiguous index rows from Francis T. Burke in Box 94 through
Paul L. Burke on PDF page 61, plus integrity reviews of the earlier Box 93
Francis T. Burke and Edmund M. Burke entities. The original-resolution index
page and the relevant NARA Army documentation pages were visually checked.
The official merged Army file was searched by private identifier outside
version control; no raw record, response body, full identifier, or unrelated
subject detail was retained.

The strict bundle contains six sources, no organization input, two
affiliations, four claims, ten claim-source links, twelve person updates, and
twelve durable research attempts. Exact private-identifier agreement confirms
the indexed George N. Burke row against the official Army form George N.
Burkett. Both forms are retained. NARA's corrected code list decodes the
recorded pre-entry field as the combined group “Shovelmen, cranemen,
derrickmen, and hoistmen.” Because the grouped code does not identify which
occupation applied, the site publishes the group with medium confidence and
does not infer an employer, machine, trade, industry, workplace, duties, or
Army-to-OSS sequence. The technical-documentation locator was checked against
physical pages 4-8, 12-13, and 44-46; the occupation entry was checked on
physical page 304 of the separate corrected code list.

The [CIA's institutional history](https://www.cia.gov/stories/story/hollywood-and-the-office-of-strategic-services/)
explicitly expands Edmund Michael “Mike” Burke and confirms his OSS identity.
The [Pennsylvania Gazette biography](https://thepenngazette.com/the-spy-who-owned-the-yankees/)
places him in New York selling maritime insurance when he met William J.
Donovan and says he agreed to OSS work in short order. This supports a high-
confidence, strongly date-bounded immediate occupation but not a named
employer or self-employment claim. The distinct Michael Burke row remains an
ambiguous possible duplicate and receives none of Edmund's occupation evidence
pending comparison of both Box 93 files.

The two Francis T. Burke rows remain separate unresolved entities in one
possible-duplicate group. Frank A. Burke, Honora E. Burke, James C. Burke,
James E. Burke, James R. Burke, Maurice L. Burke, and Paul L. Burke also remain
unresolved and route to Box 93-94 review. Documented gaps and conversion errors
in the Army electronic file explain two nonmatches and make the other absences
nondispositive; the file excludes officers, so Paul L. Burke's nonmatch is not
used against his printed first-lieutenant classification. A same-rank Fifth
Air Force roster result lacked the private identifier, OSS linkage, and Box 94
linkage and was rejected. No authenticated Catalog request, credential, raw API
response, full private identifier, full copyrighted page, or unsupported
employer claim was stored or published.

## Page-sixty-one Thomas Burke through Raymond Burkhart pathways, Batch 325

`research/evidence-page-sixty-one-thomas-burke-through-raymond-burkhart-pathways_batch-325_2026-08-20.json`
records the ten contiguous Box 94 rows from Thomas I. Burke through Raymond E.
Burkhart on PDF page 61. The original-resolution index page, NARA's Army-file
technical documentation, and occupation-code pages 170, 171, 174, 175, and
178 were visually checked. The official merged Army file was searched by
private identifier outside version control. Only project-authored decisions
and stable citation pointers were retained; no raw record, response body, full
identifier, or unrelated subject detail was stored.

The strict bundle contains eight sources, two organization inputs, seven
affiliations, fourteen claims, thirty-six claim-source links, ten person
updates, and ten durable research attempts. Exact private-identifier agreement
confirms Thomas W. Burke, Timothy J. Burke, William J. Burke, George W.
Burkett Jr., James E. Burkhardt, and Horace R. Burkhart. The official code
list supports qualified occupational groups for five of them: author, editor,
or reporter; secondary-school teacher or principal; general office clerk;
chauffeur or bus, taxi, truck, or tractor driver; and mineral-extraction or
construction driller. Those fields name no employer, school, vehicle, mine,
worksite, exact duties, or Army-to-OSS chronology. James E. Burkhardt's Army
entry occurred on October 18, 1945, after NARA's September 20, 1945 OSS
termination date, so his transportation-agent occupation is retained only as
identity context and deliberately excluded from pre-OSS affiliations and
claims.

The [University of Wisconsin Board of Regents minutes](https://asset.library.wisc.edu/1711.dl/6LB5IHLXSG6EQ83/E/file-cd1d9.pdf?dl=)
directly name Frederick H. Burkhardt as an assistant professor of philosophy
on leave without pay for the 1943-44 academic year. The [University of
Cambridge Darwin Correspondence Project](https://www.darwinproject.ac.uk/about/history-project/frederick-burkhardt-1912-2007)
and a [Los Angeles Times obituary](https://www.legacy.com/us/obituaries/latimes/name/frederick-burkhardt-obituary?id=10693845)
corroborate the distinctive identity and document the University of Wisconsin
to Navy to OSS sequence. The Navy is modeled as a strongly date-bounded
immediate military assignment; the university is the verified last civilian
employer. The historical university name remains in evidence while its
canonical organization is University of Wisconsin-Madison.

Thomas I. Burke, William E. Burke, and Raymond E. Burkhart remain unresolved
and route to Box 94 review. The Army technical documentation's missing ranges
and conversion warnings make their nonmatches nondispositive. No authenticated
Catalog request, credential, raw API response, full private identifier, full
copyrighted page, post-OSS occupation relabeled as pre-OSS evidence, or
unsupported employer claim was stored or published.

## Page-sixty-one Charles Burkle through George Burneston pathways, Batch 326

`research/evidence-page-sixty-one-charles-burkle-through-george-burneston-pathways_batch-326_2026-08-20.json`
records the ten contiguous Box 94 rows from Charles W. Burkle through George
I. Burneston Jr. on PDF page 61. The original-resolution index page, NARA's
Army-file technical documentation, and occupation-code pages 171 and 174 were
visually checked. The official merged Army file was searched by private
identifier outside version control. Only project-authored decisions and stable
citation pointers were retained; no raw record, response body, full identifier,
or unrelated subject detail was stored.

The strict bundle contains seven sources, two organization inputs, four
affiliations, nine claims, twenty-three claim-source links, ten person updates,
and ten durable research attempts. Exact private-identifier agreement confirms
Charles W. Burkle, Lowell Burmaster, and George I. Burneston Jr. NARA's
corrected list decodes code 499 as the broad group covering occupations in the
manufacture of electrical machinery and accessories, not elsewhere classified.
The grouped evidence is published for Burkle and Burneston with medium
confidence and names no employer, establishment, product, exact trade,
location, or Army-to-OSS chronology. Burmaster's code 147 is absent between
codes 145 and 148 in the corrected list, so it is retained only in private
review notes and supports no public occupation or employer claim.

The [Washington Post obituary](https://www.washingtonpost.com/archive/local/2002/12/01/edward-burling-jr-dies/e18f423b-49e3-427c-96a6-e4a76d3d0624/)
dates Edward Burling Jr.'s entry into Covington & Burling to 1935 and documents
later World War II Army Air Forces service. The [Library of Congress HABS
record](https://www.loc.gov/pictures/item/dc0262/) independently identifies him
as a lawyer and senior partner of Covington and Burling. [*Watch Hill Through
Time*](https://thewatchhillconservancy.org/wp4/wp-content/uploads/2019/04/WatchHill_TT.pdf)
names Edward Burling Jr. as a firm partner and identifies Carnealia Perin
Burling Tyler as his first wife. Together with the rare exact indexed name and
suffix, Washington legal context, and adjacent Burling rows, this supports a
high-confidence Edward identity and Covington & Burling as the last civilian
employer before wartime military service. The firm is not presented as the
immediate pre-OSS affiliation. The Army Air Forces evidence remains private
and review-pending because its sequence relative to OSS is not established.

The indexed Carnelealia P. Burling is a probable spelling variant of Carnealia
Perin Burling Tyler, supported by the rare near-exact first name, matching P
initial and surname, and adjacent independently resolved Edward row. Box 94
confirmation is still required. The same local history states that Carnealia's
sister Anne Wallingford Perin served in OSS; that statement is not transferred
to Carnealia and supports no employment claim for her. Richard V. Burks, Roy
F. Burleigh, Anson Burlingame, Richard G. Burlingame, and Margaret M. Burnes
remain unresolved. Anson retains the printed captain classification, and the
famous nineteenth-century diplomat is rejected as chronologically impossible.
No authenticated Catalog request, credential, raw API response, full private
identifier, full copyrighted page, unassigned occupation code, relative's
biography, or unsupported employer claim was stored or published.

## Page-sixty-three Bushnell through Butkevitch pathways, Batch 334

`research/evidence-page-sixty-three-virginia-bushnell-through-steve-butkevitch-pathways_batch-334_2026-08-21.json`
records ten contiguous Box 97 source rows on PDF page 63, from Virginia R.
Bushnell through Steve Butkevitch. The page was rendered and visually checked
at original resolution, and every source row remains immutable. The strict
bundle contains eleven sources, three organization inputs, five affiliations,
ten claims, twenty-five claim-source links, ten person updates, and ten durable
research attempts.

The NARA OSS index, official Army merged file, technical documentation, and
occupation code list were compared outside version control. Exact private-
identifier agreement confirms indexed Serfin S. Buta as Army entrant Serafin
S. Buta and indexed William E. Butke as William E. Butke Jr. The suffix and
spelling variants are stored separately without changing the printed index
values. The Army file dates their entry as privates to March 22, 1941 and
February 6, 1942. Its civilian-occupation codes decode to the broad
housekeeper/steward/hostess group and general-office clerks. Those findings are
published as bounded occupations, not named employers, workplaces, exact
duties, or immediate Army-to-OSS transfers. Steve Butkevitch's printed
identifier and exact name produced no processed-file match. The technical
documentation records omissions and conversion errors, so absence is not
treated as disproof.

The [American Battle Monuments Commission historical
article](https://www.abmc.gov/news-events/news/5-things-you-may-not-know-about-sicily-rome-american-cemetery/)
was inspected directly in the browser after automated HTTP retrieval was
refused. It explicitly identifies Sgt. Serafin Buta in the OSS San Fratello
mission and also documents the Sam variant and Ohio context. The [January 1931
*Laurel of Phi Kappa Tau*](https://s3.amazonaws.com/phikappatau.org/wp-content/uploads/2015/12/08192257/vol-19-no-2-january-1931.pdf)
was downloaded transiently, text-extracted, and visually checked at PDF
physical page 47. It lists Serafin Buta of Salem among Miami University's new
Alpha pledges. The evidence supports student status only and is excluded from
employer analytics.

The [1942 Elon College
yearbook](https://upload.wikimedia.org/wikipedia/commons/6/64/Phi_Psi_Cli_%28electronic_resource%29_%28IA_phipsicli1942elon%29.pdf)
and [1943 Burlington and Graham city
directory](https://lib.digitalnc.org/nanna/record/24832/files/diralamance_001083_000001.pdf?registerDownload=1&version=1&withMetadata=0&withWatermark=0)
were downloaded transiently and visually checked at PDF pages 14 and 84. They
independently identify Wilsie Florence or Wilsie F. Bussell as an Elon College
language instructor. The rare-name match is published as probable and the
employment as non-immediate; neither source prints OSS or Box 97. University
of Minnesota's [1940-1941 address
book](https://conservancy.umn.edu/server/api/core/bitstreams/3444532d-ea86-4080-8a0d-3bdc686680ce/content)
was retrieved through the institution's public bitstream endpoint and visually
checked at PDF page 106. It lists the exact unusual name Marillyn A. Butcher
with a class-year code. The [May 1942 *Crescent of Gamma Phi
Beta*](https://www.gpbarchives.org/wp-content/uploads/2017/07/1942_May.pdf)
corroborates the University of Minnesota chapter context. Together they
support a probable student affiliation, not employment.

The [New Mexico Historic Women Marker Program biography of Inez
Gill](https://www.nmhistoricwomen.org/new-mexico-historic-women/inez-gill/)
uses the rare maiden name Inez Bushner and documents World War II American
intelligence service. Because it omits the index's middle initial, OSS, Box 97,
and prewar employment, it supports only a medium-confidence probable identity.
Virginia R. Bushnell, Herbert Bussard, Elizabeth A. Busvine, Nina A. Butchart,
and Steve Butkevitch remain unresolved. No authenticated Catalog request,
credential, raw API response, raw Army record, full private identifier,
private address, full copyrighted page, postwar-employer substitution,
search-result-only claim, or unsupported namesake biography was stored or
published.

## Pages-sixty-three and sixty-four Butler through Buttram pathways, Batch 336

`research/evidence-pages-sixty-three-sixty-four-paul-butler-through-georgia-buttram-pathways_batch-336_2026-08-21.json`
records ten contiguous source rows from Paul B. Butler Jr. through Georgia E.
Buttram. Paul Butler through Robert L. Butt are in Box 97 on PDF page 63;
Alfrd C. Butterfield is the final reviewed page-63 row, and Robert E.
Butterfield through Georgia E. Buttram begin page 64 in Box 98. Both pages were
rendered and visually checked at original resolution. The strict bundle
contains seven source inputs, two organization inputs, four affiliations,
eight claims, twenty-one claim-source links, ten person updates, and ten
durable research attempts.

The NARA OSS index was compared privately with the official unrestricted
[Electronic Army Serial Number Merged File](https://catalog.archives.gov/id/1263923),
its [technical documentation](https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf),
and its [occupation code lists](https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf).
Exact private-identifier and full-name agreement confirms David S. Butterwick
and James J. Buttino. Their Army-entry records date to April 30 and October 21,
1942, respectively. The code list decodes the recorded civilian occupations
only as the residual `Miscellaneous occupations, n. e. c.` and `Metal products
fabrication occupations, n. e. c.` groups. Neither code names an employer,
workplace, product, exact trade, or immediate Army-to-OSS sequence. An exact-
name Army entrant for Robert L. Butt is retained only as a private low-
confidence lead because the index prints no identifier or other discriminator.

An official [1958 Congressional Record
roster](https://www.govinfo.gov/content/pkg/GPO-CRECB-1958-pt1/pdf/GPO-CRECB-1958-pt1-13-1.pdf)
provides exact uncommon-name and private-identifier agreement for Junichi
Buto. A contemporary [Pacific Citizen
clipping](https://ddr.densho.org/ddr-csujad-15-2/) places Second Lieutenant
Buto at the Infantry School at Fort Benning. The 442nd Veterans Club account
reprinted in [*Go for Broke*
](https://ddr.densho.org/ddr-csujad-1-184/) identifies him among the officers
who returned to the 442nd and then received OSS orders. The 442nd is modeled
as his explicit immediate military predecessor and the Infantry School as an
earlier Army training assignment. Neither is labeled a civilian employer.

Paul B. Butler Jr., Cynthia Butson, the index's printed Alfrd C. Butterfield,
Robert E. Butterfield, Lulu W. Buttermore, and Georgia E. Buttram remain
unresolved and route to Box 97 or 98 review. No authenticated Catalog request,
API credential, raw API response, raw Army record, full private identifier,
private address, full copyrighted page, search-result-only claim, or
unsupported namesake employer was stored or published.

## Page-sixty-three Butkus through Butler pathways, Batch 335

`research/evidence-page-sixty-three-william-butkus-through-marshall-butler-pathways_batch-335_2026-08-21.json`
records ten contiguous Box 97 source rows on PDF page 63, from William J.
Butkus through Marshall Butler. The page was rendered and visually checked at
original resolution. The strict bundle contains seven sources, one organization
input, two affiliations, seven claims, sixteen claim-source links, ten person
updates, and ten durable research attempts.

The NARA OSS index was compared privately with the official unrestricted
[Electronic Army Serial Number Merged File](https://catalog.archives.gov/id/1263923),
its [technical documentation](https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1ND_NC.pdf),
and its [occupation code lists](https://catalog.archives.gov/medialive/23/2639/1263923/content/arcmedia/electronic-records/rg-064/asnf/100.1CL_SD.pdf).
William J. Butkus's printed private identifier resolves to a differently named
Army subject, while an exact-name Army entrant carries another identifier. The
public conflict note retains neither full identifier nor the unrelated
subject's identity and assigns no entry detail from either candidate. Kenneth
D. Butler has exact private-identifier and full-name agreement across the index
and Army file. The Army record dates his entry as a private to July 22, 1941;
the official code list decodes the recorded civilian occupation as
`Compositors and typesetters`. That broad occupation is not represented as a
named employer, workplace, exact specialty, or immediate pre-OSS affiliation.

The [Digital Library of Georgia institutional biography of Henry Rutherford
Butler Jr.](https://dlg.usg.edu/record/dlg_aaed_aarl09-002-005-002) documents
matching initials and suffix, a prewar medical pathway, and wartime Army
service. It supplies no OSS, Box 97, or private-identifier link, so none of the
candidate's education, practice, hospital, fellowship, or Army details is
published for H. R. Butler Jr. A [1932 official Commerce Department
directory](https://www.govinfo.gov/content/pkg/SERIALSET-09708_00_00-002-0451-0000/pdf/SERIALSET-09708_00_00-002-0451-0000.pdf)
names Hugh D. Butler as the agency's Boston district manager. Exact-name
agreement is insufficient because the source does not link the man to the
printed identifier, OSS, or Box 97, and a separate Army namesake carries a
different identifier. Both leads remain private and low confidence.

An official [OSS Board Proceedings report preserved by the Hoover
Institution](https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full)
provides exact full-name and private-identifier agreement for Charles B.
Butler. It identifies him as a First Lieutenant in Infantry and dates Army
entry to October 4, 1939, commissioning to October 21, 1942, and OSS assignment
to July 7, 1943. The public record therefore publishes a high-confidence,
strongly date-bounded U.S. Army Infantry pathway as a military assignment, not
as a civilian employer. The report does not identify the school Butler had
just completed, his last civilian employer if any, or a specific Infantry
unit; those questions remain open for Box 97 review.

Fred J. Butler, Iris O. Butler, Juanita P. Butler, Mabel G. Butler, and Marshall
Butler remain unresolved and route to Box 97 review. No authenticated Catalog
request, API credential, raw API response, raw Army record, full private
identifier, full copyrighted page, private address, search-result-only claim,
relative's affiliation, or unsupported namesake employer was stored or
published.

## Page-sixty-three Bush through Bushnell pathways, Batch 333

`research/evidence-page-sixty-three-billie-bush-through-davis-bushnell-pathways_batch-333_2026-08-21.json`
records ten contiguous source rows on PDF page 63, from Billie V. Bush through
Davis Bushnell. Billie and F. E. Bush are in Box 96; George S. Bush through
Davis Bushnell are in Box 97. The page was rendered and visually checked at
original resolution, and every source row remains immutable. The strict bundle
contains five source inputs, no organization inputs, one qualified occupation
affiliation, three claims, seven claim-source links, ten person updates, and ten
durable research attempts.

The NARA OSS index, official Army merged file, official technical
documentation, and official occupation code list were compared outside version
control. Exact private-identifier and name agreement confirms Vernon A. Bush,
dates Army entry as a private to June 12, 1942, and records civilian occupation
code 401. NARA's code list decodes 401 as the broad `Bakers` group. That finding
is published only as a medium-confidence, strongly date-bounded occupation. It
does not name an employer, bakery, workplace, exact specialty, or immediate
Army-to-OSS pathway. Billie V. Bush retains the index's lieutenant and
commissioned Army classifications, and George S. Bush retains the index's
private and enlisted Army classifications without borrowing any namesake's
record.

Exact-name Army records for George S., Gordon W., and Howard T. Bush carry
different private identifiers and remain rejected namesakes. Stuart D. Bush
has no exact processed-file name match. The technical documentation identifies
missing ranges and conversion errors, so absence from the merged file is not
treated as disproof. An official Princeton institutional biography documents
Asa S. Bushnell II and his son Asa Bushnell III. The no-initial index row cannot
be assigned between them without a second corroborating identifier, so the
candidate identity is preserved as a withheld low-confidence claim requiring
critical Box 97 comparison. Billie V. Bush, F. E. Bush, George S. Bush, Gordon
W. Bush, Howard T. Bush, Stuart D. Bush, Bernice D. Bushnell, and Davis
Bushnell remain unresolved and route to Box 96 or 97 review.

No authenticated Catalog request, credential, raw API response, raw Army
record, full private identifier, copyrighted source page, unrelated namesake
detail, relative-derived claim, postwar employer substitution, or unsupported
employer claim was stored or published.

## Page-sixty-three Burton through Busey pathways, Batch 332

`research/evidence-page-sixty-three-robbie-burton-through-mildred-busey-pathways_batch-332_2026-08-21.json`
records ten contiguous source rows on PDF page 63, from Robbie Burton through
Mildred L. Busey. All ten rows are in Box 96. The page was rendered and
visually checked at original resolution, and every source row remains
immutable.

The strict bundle contains four source inputs, no organization or affiliation
inputs, three identity claims, six claim-source links, ten person updates, and
ten durable research attempts. The NARA OSS index and official Army merged
file were compared by the documented fixed-width private identifier field
outside version control. Indexed James C. Burwell's identifier leads to James
S. Burwell; indexed Watson B. Busby's identifier leads to Watson E. Busby.
Because no independent reviewed source resolves either middle-initial
conflict, the candidates' Army-entry status, occupations, dates, and employers
remain unassigned. Watson's printed T-4 grade independently supports enlisted
Army classification. Michael B. Burzynski's identifier and exact name do not
appear in the processed file, but the official technical documentation warns
of omissions and conversion errors, so absence is not treated as disproof.

A person-specific Legion of Merit citation names Lieutenant Commander Charles
C. Busenkell, United States Naval Reserve, as officer-in-charge of the OSS
Special Projects Office Electronics Section from October 1944 through October
1945. The exact uncommon full name and direct OSS context support high-
confidence identity and commissioned naval classification. The citation does
not establish his immediate pre-OSS naval assignment or last civilian
employer. A 1940 amateur-radio callbook and 1960 engineering directory were
reviewed only as identity or career leads and do not support a predecessor
claim.

Robbie Burton, Ronald R. Burton, Michael B. Burzynski, Giovanni S. Buscemi,
Homer F. Busch, Joan F. Buschmann, and Mildred L. Busey remain unresolved
after the complete accessible-source protocol and route to Box 96 review.
Common-name, directory, newspaper, obituary, cemetery, genealogy, military,
and modern candidates lacked two corroborating identifiers and Box 96 linkage.
No authenticated Catalog request, credential, raw API response, raw Army
record, full private identifier, unrelated candidate details, copyrighted
image, relative-derived identity, or unsupported employer claim was stored or
published.

## Pages-sixty-two and sixty-three Burt through Burton pathways, Batch 331

`research/evidence-pages-sixty-two-sixty-three-lillian-burt-through-mary-burton-pathways_batch-331_2026-08-21.json`
records the final nine source rows on PDF page 62 and the first source row on
page 63, from Lillian L. Burt through Mary Burton. All ten rows are in Box 96.
Both pages were rendered and visually checked at original resolution. Mary's
incomplete printed notes value remains exactly `docume`; it is not silently
expanded to a presumed word.

The strict bundle contains seven source inputs, two organization inputs, five
affiliations, seven claims, fourteen claim-source links, ten person updates,
and ten durable research attempts. Exact normalized private-identifier
agreement with the official North Dakota veterans roster confirms Lyman D.
Burtch and documents U.S. Army entry at Fort Benning on October 21, 1942,
Asiatic-Pacific service, and eventual separation as a lieutenant colonel. The
eventual grade and officer-format identifier support commissioned Army
classification, but the grade is not projected backward to every wartime date,
and the roster does not establish the immediate Army-to-OSS sequence or a
civilian employer.

Exact name and private-identifier agreement with NARA's official Army merged
file confirms Will Burtin and dates Army entry to July 14, 1943. NARA's
corrected code list supports the medium-confidence, date-bounded commercial-
artist occupation without naming an employer, client, studio, project, or
exact duty. RIT's Cary Graphic Arts Collection biography explicitly connects
his 1943 U.S. Army entry to OSS assignment and documents a prewar New York
freelance design practice and Pratt Institute teaching. The overlapping
practice and teaching are published separately; neither is selected as the
sole last civilian employer. A second RIT account corroborates the military-
to-OSS pathway. Because the two institutional accounts disagree on whether he
was drafted or volunteered, the public claim states only the supported 1943
military-entry and OSS-assignment sequence and preserves the disagreement.

Lillian L. Burt, Charlotte Burtis, Barbara J. Burton, Deloise E. Burton,
Dorothy V. Burton, Jonia Burton, Joseph S. Burton, and Mary Burton remain
unresolved after the complete accessible-source protocol and route to Box 96
review. Common-name census, directory, obituary, cemetery, genealogy,
military, and modern candidates lacked two corroborating identifiers and Box
96 linkage. An unrelated postwar CIA OCR hit for Mary Burton was rejected. No
authenticated Catalog request, credential, raw API response, raw Army record,
full private identifier, unrelated namesake identity, copyrighted image, or
unsupported employer claim was stored or published.

## Page-sixty-two Burrhus through Burt pathways, Batch 330

`research/evidence-page-sixty-two-donald-burrhus-through-edwin-burt-pathways_batch-330_2026-08-21.json`
records ten contiguous source rows on PDF page 62, from Donald M. Burrhus at
row 28 through Edwin B. Burt at row 37. The first two rows are in Box 95 and
the remaining eight are in Box 96. The page was rendered and visually checked
at original resolution, and every source row remains immutable.

The strict bundle contains four official source inputs, no organization
inputs, three affiliations, seven claims, seventeen claim-source links, ten
person updates, and ten durable research attempts. The NARA OSS index and
official Army merged file were compared by the documented fixed-width private
identifier field outside version control. Exact name and identifier agreement
confirms Donald M. Burrhus, John Burriack, and Edwin B. Burt as enlisted Army
personnel. NARA's corrected occupation list supports Donald's date-bounded
lithographer occupation, John's student status, and Edwin's date-bounded
general-industry clerk group. Each is medium-confidence and temporally tied to
Army entry. None is converted into a named employer, school, industry,
workplace, product, exact duty, or Army-to-OSS sequence.

Arthur L. Burt's printed identifier resolves to an official Army record for a
different person. The unrelated subject, raw record, and full identifiers are
withheld; the public profile records only the direct identity conflict and
assigns no Army rank, occupation, employer, or chronology. Richard M. Burrill,
Joseph F. Burrough, Herbert Burrows, Frank L. Bursaw, Noreen R. Burson, and
Isadore Burstein remain unresolved after the complete accessible-source
protocol and route to Box 96 review. The Army-file nonmatches for Richard,
Frank, and Isadore are nondispositive because the series has documented
omissions and excludes officers. Same-name obituary, broadcasting, directory,
military, census, cemetery, genealogy, and modern candidates lacking the
private identifier or folder linkage were rejected. No authenticated Catalog
request, credential, raw API response, raw Army record, full private
identifier, unrelated namesake identity, or unsupported employer claim was
stored or published.

## Page-sixty-two Burns through Burrell pathways, Batch 329

`research/evidence-page-sixty-two-olsen-burns-through-robert-burrell-pathways_batch-329_2026-08-20.json`
records ten Box 95 source rows on PDF page 62: rows 17-25, Olsen D. Burns
through Morris Burr, and row 27, Robert W. Burrell. Jane Burrell at row 26
already had a terminal reviewed outcome and was not reprocessed. The page was
rendered and visually checked at original resolution, and every source row
remains immutable.

The strict bundle contains four official source inputs, no organization
inputs, two occupation affiliations, five claims, twelve claim-source links,
ten person updates, and ten durable research attempts. The NARA OSS index and
official Army merged file were compared by the documented fixed-width private
identifier field outside version control. Exact full-name, middle-initial, and
private-identifier agreement confirms Robert T. Burns, Robert W. Burns, and
Melvin S. Buros. Robert T.'s November 9, 1942 Army-entry field is decoded by
NARA's corrected list as “Painters, construction and maintenance”; Robert W.'s
November 25, 1940 field is decoded as “Commercial artists.” Both are published
only as medium-confidence, date-bounded occupations. Neither record names an
employer, workplace, project, client, medium, industry, or sequence into OSS.

Melvin Buros's exact Army record carries occupation code 070, which is
unassigned in the corrected NARA list; it is not interpreted or published as
an occupation. Ralph Burns and Morris Burr produced no exact identifier match.
Robert W. Burrell's printed captain rank is preserved as a commissioned Army
classification; absence from the enlisted-only Army merged file is expected
and nondispositive. Olsen D. Burns, Ralph Burns, Robert C. Burns, Rosemary
Burns, Millman T. Burnside, Morris Burr, and Robert W. Burrell remain unresolved
after the complete accessible-source protocol and route to Box 95 review.
Same-name musicians, officers, architects, directory entries, obituaries, and
other namesakes lacking the index identifier or folder linkage were rejected.
No authenticated Catalog request, credential, raw Army record, full private
identifier, unassigned occupation, namesake identity, or unsupported employer
claim was stored or published.

## Page-sixty-two Burns pathways and duplicate review, Batch 328

`research/evidence-page-sixty-two-albert-burns-through-marian-burns-pathways_batch-328_2026-08-20.json`
records eleven contiguous Box 95 source rows on PDF page 62, from Albert V.
Burns through the second of two adjacent Marian H. Burns rows. The page was
rendered and visually checked at original resolution. All eleven rows remain
immutable and linked to separate cautious person entities, including both
visually identical Marian entries.

The strict bundle contains two official source inputs, no organization or
affiliation inputs, one conflict-visible identity claim, two claim-source
links, eleven person updates, and eleven durable research attempts. The NARA
OSS index and the official Army merged file were compared by private
identifier outside version control. Frank G. Burns's printed identifier
resolves to an Army record carrying a different name. The unrelated subject,
raw record, and full identifiers are withheld; the disagreement is published
only as a direct identity conflict and supplies no rank, occupation, employer,
or chronology. Gerald E. Burns produced no exact Army-file identifier match.
That absence is nondispositive because the series has omissions and excludes
officers.

The two adjacent Marian H. Burns rows have the same printed name, Box, and
location and no rank, identifier, note, occupation, or assignment. They remain
separate source records and person entities in one visible possible-duplicate
group pending comparison of both Box 95 folders. Albert V. Burns, Arvin Burns,
Catherine E. Burns, Erna J. Burns, Gerald E. Burns, Helen S. Burns, Janet T.
Burns, and Margaret M. Burns remain unresolved after NARA, CIA, Library of
Congress, exact-name OSS, employment, occupation, institutional, newspaper,
obituary, directory, military, and archival searches. All route to Box 95
review. No authenticated Catalog request, credential, raw API response, full
private identifier, unrelated namesake identity, or unsupported employer claim
was stored or published.

## Pages-sixty-one-and-sixty-two Burnet through Burnham pathways, Batch 327

`research/evidence-pages-sixty-one-sixty-two-maccurdy-burnet-through-robert-burnham-pathways_batch-327_2026-08-20.json`
records the final five Box 94 rows on PDF page 61 and first five Box 94-95 rows
on page 62, from Maccurdy Burnet through Robert J. Burnham. Both index pages,
NARA's Army-file technical documentation, and corrected occupation-code pages
171-172 were visually checked. The official Army merged file was searched by
private identifier outside version control. No full identifier or raw record
is stored in the evidence bundle or public projection.

The strict bundle contains ten sources, six organization inputs, eight
affiliations, thirteen claims, thirty-one claim-source links, ten person
updates, and ten durable research attempts. Exact private-identifier agreement
confirms Maccurdy Burnet, Floyd R. Burnett, and Robert J. Burnham. The corrected
code list decodes Maccurdy's 066 field as “Technicians, except laboratory” and
Robert's 185 field as “Agents, sales, except to consumers.” Both are published
as qualified, date-bounded occupation groups with no employer, specialty,
product, industry, workplace, customer, or OSS sequence. Floyd's matching May
23, 1946 Army entry postdates OSS termination and is retained only as identity
evidence.

The [1942 *Yackety Yack* institutional
record](https://lib.digitalnc.org/record/27391?ln=en), visually checked on PDF
page 71 and printed page 67, identifies MacCurdy Burnet as an A.B. candidate
and Red Cross field supervisor. UNC is modeled as student status. The Red Cross
role is a neutral professional affiliation because the source does not establish
whether it was paid or volunteer. The [Princeton memorial for Gilbert Burnett
Jr.](https://paw.princeton.edu/memorial/gilbert-burnett-jr-43) explicitly
sequences 1943 graduation, Army enlistment, and subsequent OSS service. It
supports a high-confidence identity, Princeton student affiliation, and the
Army as the immediate military pathway.

The [Princeton memorial for Philip
Burnham](https://paw.princeton.edu/memorial/philip-burnham-31) directly links
his Commonweal editorial career, Army Air Force officer status, and OSS
attachment. [Commonweal's institutional
history](https://www.commonwealmagazine.org/edward-s-skillin-1904-2000) dates
his co-editorship to 1938, while the [May 2, 1940 Congressional
Record](https://www.govinfo.gov/content/pkg/GPO-CRECB-1940-pt5-v86/pdf/GPO-CRECB-1940-pt5-v86-11.pdf)
names him as editor of the Commonweal. The Commonweal Publishing Company is
therefore published as the verified last civilian employer before wartime
service, separate from the Army Air Force attachment that led into OSS. A
colleague's [Commonweal memoir](https://www.commonwealmagazine.org/trying-my-hand)
corroborates his return from wartime service. The accessible evidence supplies
no rank, so the project's commissioned-officer classification remains
indeterminate.

Robert W. Burnet, Edgar L. Burnett, Russell A. Burnett, W. C. Burnett, and
Mary K. Burnham remain unresolved. The initials-only W. C. record receives
critical Box 94 review priority; the other unresolved cases route to Boxes
94-95. No authenticated Catalog request, credential, raw API response, full
private identifier, full copyrighted page, post-OSS occupation masquerading as
pre-OSS evidence, namesake biography, or unsupported employer claim was stored
or published.

## Pages 71-72 Carrolll through Carstones review, Batch 373

The source pages were rendered from the checksum-verified NARA index and
visually checked at original resolution. They preserve ten distinct rows from
Frank M. Carrolll through Irene Carstones in Boxes 109-110, including the
unusual three-l `Carrolll` spelling, John F. Carson's printed `Capt` rank, four
private identifiers, and all blank cells. Private identifiers are retained
only in the ignored SQLite database and never appear in the evidence bundle or
public files.

NARA's public unrestricted *Electronic Army Serial Number Merged File,
ca. 1938-1946* was reviewed transiently with its official field documentation
and Civilian Occupations code list. Exact private-identifier agreement confirms
Kenneth P. Carson and Norman M. Carson. The source supports only the historical
occupation category `Salespersons` for Kenneth and student status for Norman,
both at Army entry. It names no employer, company, school, product, industry,
field of study, workplace, or OSS transition.

The exact-name Army candidates for Vincent N. Carrozzo and Maurice S.
Carselowey carry identifiers that conflict with the index and therefore remain
rejected pending Box 110 review. The adjacent Vincent V. Carrazo row in Box 109
and Vincent N. Carrozzo row in Box 110 are flagged as a possible duplicate but
remain separate because spelling, middle initial, box, and identifier evidence
disagree. Later federal cultural-programming references for Irene Carstones are
postwar and remain discovery leads only. No raw Army row, bulk payload,
authenticated Catalog response, credential, full identifier, unrelated
namesake identity, or unsupported employer claim is stored or published.

The durable evidence is in
`research/evidence-pages-seventy-one-seventy-two-frank-m-carrolll-through-irene-carstones-pathways_batch-373_2026-08-30.json`.

## Page 72 Carswell through Carter review, Batch 374

PDF page 72 was rendered from the checksum-verified NARA index and visually
checked at original resolution. The review preserves ten distinct Box 110 rows
from Stuart R. Carswell through Jim F. Carter, including every blank rank cell,
the incomplete `George Carter` and `Hie Carter` names, and the private
identifiers printed for four people. Those identifiers remain confined to the
ignored SQLite database and are masked in public output.

NARA's public unrestricted *Electronic Army Serial Number Merged File,
ca. 1938-1946* was reviewed transiently with the official technical
documentation and Civilian Occupations code list. Exact private-identifier
agreement confirms Albert W. Carter and Eugene C. Carter as Army enlisted
personnel. Eugene's entry row supports only the historical occupation category
`Steam fitters, gas fitters, and plumbers`; it names no exact trade, employer,
workplace, or Army-to-OSS transition. Albert's residual value `999` is not
interpreted because the accessible documentation does not establish a safe
meaning for that field in his row.

The official 1946 Army register, reproduced by NARA in the National Personnel
Records Center Case Reference Guide, agrees with Stuart R. Carswell's uncommon
name and private officer identifier and records his Infantry career and June
12, 1939 promotion to lieutenant colonel. The contemporary *Congressional
Record* independently supplies the full middle name Randall. This is published
as a documented prewar military assignment, not as an immediate pre-OSS
affiliation or civilian employer, because neither source establishes the OSS
transfer sequence.

Bernard S. Carter, Clifton C. Carter, and George Carter remain ambiguous:
plausible exact-name or OSS-associated candidates lack Box 110 linkage and the
required corroborating identifiers. Miro Cartelli, Henrietta K. Carter, and
Hie Carter remain unresolved. The exact-name Army candidate for Jim F. Carter
has a private identifier that conflicts with the index and is exposed only as
an identity-review conflict. No authenticated Catalog request, credential, raw
API response, raw Army row, full private identifier, unsupported employer,
unrelated namesake biography, or full copyrighted page is stored or published.

The durable evidence is in
`research/evidence-page-seventy-two-stuart-r-carswell-through-jim-f-carter-pathways_batch-374_2026-08-30.json`.

## Official reference material

- NARA OSS personnel records:
  <https://www.archives.gov/iwg/declassified-records/rg-226-oss/personnel.html>
- NARA OSS records overview:
  <https://www.archives.gov/research/military/ww2/oss>
- National Archives Catalog: <https://catalog.archives.gov/>
- NARA Catalog API guidance:
  <https://www.archives.gov/research/catalog/help/api>
- CIA Reading Room OSS Collection:
  <https://www.cia.gov/readingroom/collection/oss-collection>
- Library of Congress Chronicling America:
  <https://www.loc.gov/collections/chronicling-america/>
- Library of Congress APIs: <https://www.loc.gov/apis/>

## Transformation lineage

```text
frozen PDF
  -> pdftotext layout + bbox agreement
  -> immutable source_records
  -> cautious person_entities and links
  -> staged research attempts and human review
  -> claims, sources, organizations, affiliations
  -> redacted public exports and static pages
```

Every generated public-data file has a file size and SHA-256 in
`site/public/data/public_build_manifest.json`.

## API storage boundary

NARA Catalog responses are processed in memory and discarded. The project may
retain request time/status/fingerprint, a selected NAID and public Catalog URL,
and concise project-authored acceptance or rejection notes. It does not preserve
live response bodies or snapshots.
