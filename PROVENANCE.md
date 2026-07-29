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
