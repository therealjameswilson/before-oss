# Batch 776 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 776 covers PDF page 378, rows 1-23, Vangjel Prifti through Mario J
Procaccini. All 23 printed rows remain preserved as distinct source records and
are linked to 23 distinct person entities. Page 378 was inspected against a
300 dpi render before research. The next unresearched boundary is PDF page
378, row 24, Herbert V Prochnow.

The visibly truncated note `Netherla`, the note `Also in B`, and the
cross-reference `see fold` remain exactly as printed and are not expanded.
Full service or officer identifiers remain private and masked in public output.

## Research protocol and review

- NARA Catalog work was dry-run only: 23 planned searches and zero
  authenticated requests. No key or API response was stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  their first eligible request. These access limitations are recorded as
  limitations, not negative evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  and archival query families were reviewed for all 23 people. Namesakes,
  discovery-only genealogy and people-finder results, unbridged postwar
  records, and temporally insufficient candidates were rejected.
- Nine official Army candidate decisions are durable: eight accepted
  high-confidence identity matches and one retained duplicate conflict. Army
  occupation codes were not treated as employers or immediate affiliations.
- All 23 people now have terminal dispositions: 21
  `requires_archival_review`, one `conflicting_sources`, and one
  `documented_prewar_employer_found`.

## Historical outcomes

- Indexed Katharine Pringle is identified with high confidence as journalist
  Katharine Douglas Massel. Library of Congress, Society of Woman Geographers,
  and Association for Diplomatic Studies and Training sources bridge her
  maiden and married names and document her journalism, OWI, and OSS work.
- Time, Inc. is published as documented earlier pre-OSS employment, not as the
  immediate affiliation or last civilian employer. The Office of War
  Information is published, with a visible medium-confidence qualification, as
  her probable immediate pre-OSS government assignment. The accessible sources
  do not explicitly establish a direct OWI-to-OSS transfer.
- Edgar A Pritchard remains separate from Edgar A Prichard. The rows share a
  protected officer identifier but differ in surname spelling and archival box;
  the previously published Prichard occupation and Army-assignment claims are
  not transferred.
- Nancy M Pritchard likewise remains separate from Nancy M Prichard. The rows
  are linked only as possible duplicates pending comparison of Boxes 620 and
  621, and the Smithsonian employer claim is not transferred.
- Exact or core-name and protected-identifier Army identity matches were
  accepted for Russell G Primeaux, Roland Prince, Salvatore T Principato, Glen
  E Pringle, Nick Prioletti, Raymond W Priore, James J Prizio, and Mario J
  Procaccini. No coded Army occupation was converted into an employer.

## Exact coverage after Batch 776

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 10,848/23,939 (45.3152%).
- Verified-employer coverage: 355/23,939 (1.4829%).
- Verified-affiliation coverage: 794/23,939 (3.3168%).
- Archival-review coverage: 9,307/23,939 (38.878%).
- Not started: 13,086.
- Possible duplicate groups: 541; conflicts: 369.
- Claims: 1,408 confirmed; 3,343 high; 1,587 medium; 202 low; 322
  conflicting; two unresolved.
- Citations: 5,946 records representing 3,063 unique source documents.

## Durable inputs and replay

The reviewed decisions are stored in
`research/identity_review_decisions_2026-10-13_batch776.csv`; the evidence,
claims, source metadata, person updates, and terminal manual attempts are stored
in
`research/evidence-page378-prifti-procaccini-review_batch-776_2026-10-13.json`.
Both files validate and import idempotently through the normal pipeline.

Resume new-person research at PDF page 378, row 24, Herbert V Prochnow.
Full-index historical research remains unfinished; 13,086 active people are
still `not_started`.
