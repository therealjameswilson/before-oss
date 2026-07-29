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
