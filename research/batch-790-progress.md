# Batch 790 research progress

Date: 2026-10-14 America/New_York

## Scope and preservation

Batch 790 covers PDF page 385, rows 1-23, Clement Rault through Gregory S
Razran. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities. Page 385 was inspected against a 300 dpi render before
research. The next unresearched boundary is PDF page 385, row 24.

The clipped notes "photogra" and "Record" remain exactly as indexed and were
not expanded. Full service identifiers remain private. C P Rayon's 13 earlier
auditable attempts were preserved when that person was reassigned from the
stale pilot batch.

## Research protocol and review

- NARA Catalog and web adapters were dry-run only: 22 planned new searches per
  adapter, with duplicate prior searches skipped and zero authenticated NARA
  requests. No API response bodies were stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  the first eligible request. These access outcomes are source limitations, not
  negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  directory, military, variant-name, and archival query families were reviewed
  for all 23 people.
- Official Army bulk candidates for David Rawle and John M Rawlins were
  accepted as high-confidence identity evidence. Candidates for Eugene A Ray
  and George E Ray were preserved as conflicts because the protected
  identifiers agree but the Army names are printed as "R Y EUGENE" and "R Y
  GEORGE E." Neither spelling was silently corrected, and Army coded fields
  were not treated as employers.
- All 23 people have a saved terminal outcome: one
  `verified_employer_found`, two `conflicting_sources`, and 20
  `requires_archival_review`.

## Historical outcomes

- Queens College's institutional history directly links psychologist Gregory
  S. Razran to OSS statistical consulting and dates his Queens professorship
  from 1940 to 1972. Queens College is therefore the best-supported immediate
  institutional affiliation and last civilian employer, with an explicit note
  that the employment continued during the wartime consultancy. Columbia
  University is recorded separately as an earlier prewar affiliation, supported
  by the Queens history and a contemporary April 1938 TIME article.
- A Service historique de la Défense finding aid identifies Pierre Ravarre's
  individual intelligence-network file, and a mission chronology links the
  distinctive name and alias Jean Vernez to OSS Sussex/Ossex radio operations.
  Identity is high confidence, but neither source identifies a pre-OSS
  employer. An unbridged 1922 namesake was rejected.
- Wyman H. Packard's official naval history identifies Lieutenant Commander
  Daniel Ravenel Jr., USNR, as officer in charge of the Naval Command, OSS
  Liaison Division. This resolves identity and wartime assignment, not
  pre-OSS employment. A postwar travel-agency reference was not used as
  prewar evidence.
- Polish military and academic namesakes for Tadeusz Rawski were rejected as
  incompatible with the indexed Sergeant and lacking an OSS bridge. A burial
  lead for Faris N Razook and a postwar radio-engineering lead for Thomas D
  Razovich were also rejected.
- The remaining unresolved profiles direct researchers to the indexed
  personnel file rather than implying that no prior employment existed.

## Exact coverage after Batch 790

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,167/23,939 (46.6477%).
- Verified-employer coverage: 361/23,939 (1.5080%).
- Verified-affiliation coverage: 807/23,939 (3.3711%).
- Archival-review coverage: 9,627/23,939 (40.2147%).
- Not started: 12,767.
- Possible duplicate groups: 550; conflicts: 381.
- Claims: 1,412 confirmed; 3,471 high; 1,608 medium; 202 low; 331
  conflicting; two unresolved.
- Citations: 6,025 records representing 3,122 unique source documents.
- Public data: 2,609 published affiliations, 930 organizations, 4,800 public
  sources, and 6,818 published claims.

## Durable inputs and replay

Reviewed identity decisions are stored in
`research/identity_review_decisions_2026-10-14_batch790.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page385-rault-razran-review_batch-790_2026-10-14.json`.
Both are designed for idempotent replay through the normal import commands.

Resume new-person research at PDF page 385, row 24. Full-index historical
research remains unfinished; 12,767 active people are still `not_started`.
