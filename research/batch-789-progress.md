# Batch 789 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 789 covers PDF page 384, rows 24-46, Maurice H Rapf through Michael
Ratushni. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities. Pages 384 and 401 were inspected against 300 dpi renders
before the cross-page identity review. The next unresearched boundary is PDF
page 385, row 1, Clement Rault.

The clipped notes "see file", "Record", and "photogra" remain exactly as
indexed and were not expanded. Edward G Ratcliffe's identifier is genuinely
printed in scientific notation; it remains raw only in the private source record
and masked in public output. Full service identifiers remain private.

## Research protocol and review

- NARA Catalog and web adapters were dry-run only: 23 planned searches per
  adapter, zero authenticated NARA requests, and no API response bodies stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  the first eligible request. These access outcomes are source limitations, not
  negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  directory, military, variant-name, and archival query families were reviewed
  for all 23 people. Namesakes, postwar-only records, discovery-only genealogy,
  and temporally insufficient candidates were rejected.
- Nine official Army candidates were accepted as high-confidence identity
  evidence: Erwin E Raphael, Milton J Raport, Manuel C Raposa, Alfred M Rasero,
  Dale M Raska, George P Rasmussen, Charles Rata, William H Rath, and Michael
  Ratushni. Army occupation codes were not treated as employers or immediate
  affiliations.
- All 23 people have a saved terminal outcome: one
  `documented_prewar_employer_found`, one `occupation_only_found`, one
  `conflicting_sources`, and 20 `requires_archival_review`.

## Historical outcomes

- Dartmouth Libraries' archival authority record probably identifies the
  indexed Maurice H Rapf as Maurice Harry Rapf. It documents freelance
  Hollywood screenwriting after his 1935 Dartmouth graduation. Because no
  reviewed source directly bridges that biography to this OSS row, both the
  identity and self-employment claim remain medium-confidence and visibly
  qualified. The freelance role is earlier documented work, not a claimed
  immediate pre-OSS affiliation or named studio employer.
- An official 1944 NARA caption and a Skidmore College institutional account
  confirm Virginia Rathbun as Virginia Rathbun Stuart. Skidmore places her 1943
  graduation only months before her November 1943 OSS entry. The college is
  modeled as a strongly date-bounded immediate student affiliation, not an
  employer, and no civilian employer is inferred.
- The page-384 Seymour A Rattenberg row and page-401 Saymour A Rottenberg row
  are separately printed in Boxes 634 and 663 but share a protected identifier;
  the Army bulk spelling is Rottenberg. Both source rows and person entities
  remain separate in one visible conflict group pending examination of both
  personnel files. The full identifier is not published.
- A French civil-registry namesake for Andre L Rapicault was rejected because
  the middle name conflicted and no OSS bridge existed. Genealogy candidates
  for Anastas D Rapoff were rejected as discovery-only and contradictory. A
  postwar student-list namesake for Michael Ratushni was rejected as temporally
  irrelevant.
- No new confirmed or high-confidence civilian employer was added. Unresolved
  profiles direct researchers to the indexed personnel file rather than
  implying that no prior employment existed.

## Exact coverage after Batch 789

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,145/23,939 (46.5558%).
- Verified-employer coverage: 360/23,939 (1.5038%).
- Verified-affiliation coverage: 806/23,939 (3.3669%).
- Archival-review coverage: 9,604/23,939 (40.1186%).
- Not started: 12,789.
- Possible duplicate groups: 550; conflicts: 379.
- Claims: 1,412 confirmed; 3,463 high; 1,608 medium; 202 low; 329
  conflicting; two unresolved.
- Citations: 6,018 records representing 3,118 unique source documents.
- Public data: 2,607 published affiliations, 930 organizations, 4,793 public
  sources, and 6,808 published claims.

## Durable inputs and replay

Reviewed identity decisions are stored in
`research/identity_review_decisions_2026-10-13_batch789.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page384-rapf-ratushni-review_batch-789_2026-10-13.json`.
Both were replayed through the normal import path to confirm idempotent evidence
updates and duplicate-decision skipping.

Resume new-person research at PDF page 385, row 1, Clement Rault. Full-index
historical research remains unfinished; 12,789 active people are still
`not_started`.
