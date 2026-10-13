# Batch 788 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 788 covers PDF page 384, rows 1-23, Joseph J Randazza through Michel
Rapaport. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities. Page 384 was inspected against a 300 dpi render before
research. The next unresearched boundary is PDF page 384, row 24, Maurice H
Rapf.

The clipped notes "photogra", "Record", "Honorab", and "no first n" remain
exactly as indexed. They were not expanded into record descriptions or research
claims. Full service or officer identifiers remain private and masked in public
output.

## Research protocol and review

- NARA Catalog and web adapters were dry-run only: 23 planned searches per
  adapter, zero authenticated NARA requests, and no response bodies stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  the first eligible request. These access outcomes are source limitations, not
  negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  directory, military, variant-name, and archival query families were reviewed
  for all 23 people. Namesakes, people-finder records, discovery-only genealogy,
  postwar evidence, and temporally insufficient candidates were rejected.
- Seven official Army candidates were accepted as high-confidence identity
  evidence: Joseph J Randazza, Stephen T Randolph, Joseph S Ransmeier, Robert E
  Ransom, Thomas J Ranson, the enlisted-style Richard Raoul-Duval row, and the
  enlisted-style Bergen B Rapalyea row. Army occupation codes were not treated
  as employers or immediate affiliations.
- All 23 people have a saved terminal outcome. James F Ranney's prior completed
  result was audited and preserved; two people have `conflicting_sources`, one
  has `verified_employer_found`, one has
  `documented_prewar_employer_found`, and the remaining 18 require archival
  review.

## Historical outcomes

- Dartmouth Alumni Magazine's institutional biographies identify Joseph S.
  Ransmeier as a Vanderbilt University economics instructor beginning in 1940
  and as an Army enlistee in 1943. Vanderbilt is therefore published as his
  strongly date-bounded last civilian employer before wartime service, not as a
  proven immediate recruitment source into OSS.
- Ransmeier's 1939-40 Brookings Institution research fellowship is published as
  an earlier professional affiliation, not silently converted into employment.
- An official Archives nationales (France) finding aid identifies Lieutenant
  Richard Raoul-Duval, alias Dorsay, in OSS mission Freelance. A contemporary
  1938 San Francisco directory separately documents legal practice under his
  uncommon name. That role is published as earlier self-employed legal practice;
  the Hibernia Bank Building is an office address, not an inferred bank
  employer, and the evidence does not prove an immediate pre-OSS sequence.
- The two Richard Raoul-Duval rows remain separate under one possible-duplicate
  group because their protected identifiers differ. The officer row is tied to
  the French archival evidence; the enlisted-style row has the accepted Army
  bulk match. Neither source row was discarded or silently merged.
- The two Bergen B Rapalyea rows likewise remain separate under one
  possible-duplicate group. Only the enlisted-style row has an accepted Army
  match and the sourced Jr. variant. A Pan American World Airways lead was
  rejected because accessible evidence was postwar or undated.
- Thomas J Ransom and Vincent P Rao have visible identity conflicts caused by
  protected identifiers shared with unrelated indexed names. The full numbers
  remain private, no records were merged, and the affected physical files have
  critical archival-review priority.
- The incomplete `* Raoul` row remains unresolved. It was not linked to either
  Raoul-Duval row merely because of name proximity.

## Exact coverage after Batch 788

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,122/23,939 (46.4598%).
- Verified-employer coverage: 360/23,939 (1.5038%).
- Verified-affiliation coverage: 805/23,939 (3.3627%).
- Archival-review coverage: 9,581/23,939 (40.0226%).
- Not started: 12,812.
- Possible duplicate groups: 550; conflicts: 378.
- Claims: 1,411 confirmed; 3,453 high; 1,606 medium; 202 low; 328
  conflicting; two unresolved.
- Citations: 6,013 records representing 3,114 unique source documents.
- Public data: 2,605 published affiliations, 929 organizations, 4,788 public
  sources, and 6,794 published claims.

## Durable inputs and replay

Reviewed identity decisions are stored in
`research/identity_review_decisions_2026-10-13_batch788.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page384-randazza-rapaport-review_batch-788_2026-10-13.json`.
Both were imported twice to confirm idempotent replay through the normal
pipeline.

Resume new-person research at PDF page 384, row 24, Maurice H Rapf. Full-index
historical research remains unfinished; 12,812 active people are still
`not_started`.
