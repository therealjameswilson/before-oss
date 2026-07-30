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
