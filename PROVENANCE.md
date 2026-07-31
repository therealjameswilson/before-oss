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
