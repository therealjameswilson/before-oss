# Batch 791 research progress

Date: 2026-10-14 America/New_York

## Scope and preservation

Batch 791 covers PDF page 385, rows 24-46, Francis R. M. Rea through
Cornelia Reck. All 23 printed rows remain preserved as distinct source records
linked to 23 person entities. Page 385 was inspected against a 300 dpi render
before research. The next unresearched boundary is PDF page 386, row 1,
Margot F Reck.

The clipped notes "Record," "Dental Id," "photogra," and "Name pl" remain
exactly as indexed and were not expanded. Full service identifiers remain
private. The four Army bulk records used for identity review retain only
privacy-safe public summaries.

## Research protocol and review

- NARA Catalog and web adapters were dry-run only: 23 planned queries per
  adapter and zero authenticated NARA requests. No Catalog API response bodies
  were stored.
- The CIA Reading Room adapter failed closed on its first eligible request;
  the Library of Congress adapter recorded a timeout. These access outcomes
  are source limitations, not negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  directory, military, variant-name, and archival query families were reviewed
  for all 23 people.
- Official Army bulk candidates for Norman W Read, Daniel R Reason, Vincent
  Rebar, and Constantino Reboa were accepted as high-confidence identity
  evidence. Army coded fields were not treated as employers.
- All 23 people have saved terminal outcomes: Conyers Read and Constantino
  Reboa are `verified_employer_found`; the other 21 are
  `requires_archival_review`. Conyers Read's already published evidence was
  reaudited rather than duplicated.

## Historical outcomes

- A direct May 1944 OSS personnel interview preserved by the Hoover Institution
  identifies Constantino Reboa as a radio officer in the Italian Merchant
  Marine. The same report says he entered the Army through OSS in August 1943
  and was in an internment camp when recruited. The Merchant Marine is
  therefore published as his best-supported last civilian affiliation, not as
  his immediate pre-OSS status. No shipping company or vessel is inferred.
- The index, official Army bulk record, and OSS interview agree on Reboa's
  uncommon name and nonshared protected identifier, supporting a confirmed
  identity. The full identifier remains private.
- A National Park Service institutional history cites January 1945 memoranda
  by Louis M. Ream and identifies him as OSS deputy director for administrative
  services, matching the index's `Dpty Dir` notation. This resolves identity at
  high confidence but does not establish a pre-OSS employer. Banking and
  Princeton references for Louis Marshall Ream remain rejected namesake leads
  pending a direct bridge.
- The University of Pennsylvania finding aid was rechecked and continues to
  support Conyers Read's 1934 faculty appointment, 1941-1942 leave for the
  Coordinator of Information, and later OSS British Empire work. His existing
  immediate-affiliation and last-civilian-employer claims remain unchanged.
- Rare-name leads for Roby C Read and a corporate executive namesake for
  Second Lieutenant Robert C Ream were rejected because neither source bridged
  the candidate to the indexed OSS record.
- The remaining unresolved profiles direct researchers to the indexed
  personnel file rather than implying that no prior employment existed.

## Exact coverage after Batch 791

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,189/23,939 (46.7396%).
- Verified-employer coverage: 362/23,939 (1.5122%).
- Verified-affiliation coverage: 808/23,939 (3.3752%).
- Archival-review coverage: 9,649/23,939 (40.3066%).
- Not started: 12,745.
- Possible duplicate groups: 550; conflicts: 381.
- Claims: 1,413 confirmed; 3,476 high; 1,608 medium; 202 low; 331
  conflicting; two unresolved.
- Citations: 6,029 records representing 3,125 unique source documents.
- Public data: 2,610 published affiliations, 931 organizations, 4,804 public
  sources, and 6,824 published claims.

## Durable inputs and replay

Reviewed identity decisions are stored in
`research/identity_review_decisions_2026-10-14_batch791.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page385-rea-reck-review_batch-791_2026-10-14.json`.
Both were replayed through the normal import commands to verify idempotence.

Resume new-person research at PDF page 386, row 1, Margot F Reck. Full-index
historical research remains unfinished; 12,745 active people are still
`not_started`.
