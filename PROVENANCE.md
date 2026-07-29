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
