# Batch 787 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 787 covers PDF page 383, rows 25-46, Tommie I Rammage through Ruth E
Randall. All 22 printed rows remain preserved as distinct source records linked
to 22 person entities. Page 383 was inspected against a 300 dpi render before
research; page 388 was separately rendered to confirm the variant Tommie I
Remmage row. The next unresearched boundary is PDF page 384, row 1, Joseph J
Randazza.

The clipped notes "One fold", "Record", and "Certificat" remain exactly as
indexed. They were not expanded into record descriptions or research claims.
Full service or officer identifiers remain private and masked in public output.

## Research protocol and review

- NARA Catalog and web adapters were dry-run only: 22 planned searches per
  adapter, zero authenticated NARA requests, and no response bodies stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  the first eligible request. These access outcomes are source limitations,
  not negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  directory, military, variant-name, and archival query families were reviewed
  for all 22 people. Namesakes, people-finder records, discovery-only genealogy,
  postwar evidence, and temporally insufficient candidates were rejected.
- Eight official Army candidates were accepted as high-confidence identity
  evidence: Nick E Ramoundos, Charles F Ramsdell, Kenneth S Ramsey, Winters P
  Ramsey, Sgt Philip L Rancourt, Frank J Randall, Gale M Randall, and Kenneth C
  Randall. Army occupation codes were not treated as employers or immediate
  affiliations.
- All 22 people have a saved terminal outcome: 21 require archival review and
  Tommie I Rammage has `conflicting_sources` pending comparison of Boxes 632
  and 639.

## Historical outcomes

- A first-person British Diplomatic Oral History Programme transcript at the
  Churchill Archives Centre supports a high-confidence identity match for Major
  Peter E Ramsbotham. It documents security work in the British War Office and
  British Army Intelligence Corps service as captain and later major.
- Ramsbotham's two wartime roles are published as qualified other affiliations
  with `temporal_relation_uncertain`. The accessible source does not establish
  their sequence relative to the indexed OSS connection, so neither is labeled
  an immediate pre-OSS affiliation or a civilian employer.
- The index separately prints Tommie I Rammage on page 383 and Tommie I
  Remmage on page 388 under different boxes but with the same private
  identifier. The rows remain separate and the conflict is visible without
  publishing the identifier.
- The two separately printed Philip L Rancourt rows, one sergeant and one
  second lieutenant, remain separate person entities under one possible-
  duplicate group. Only the sergeant row has an accepted official Army match.
- A 1941 Ithaca directory lead for a same-name Kenneth C Randall was rejected
  because no geographic or identity bridge tied the business proprietor to the
  indexed soldier.
- No new confirmed or high-confidence civilian employer was added. Profiles
  without reliable employment evidence direct researchers to the indexed
  personnel files rather than implying that no prior employment existed.

## Exact coverage after Batch 787

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,100/23,939 (46.3679%).
- Verified-employer coverage: 358/23,939 (1.4955%).
- Verified-affiliation coverage: 803/23,939 (3.3544%). Ramsbotham's new
  affiliations are excluded from this default measure because their OSS
  sequence is uncertain.
- Archival-review coverage: 9,559/23,939 (39.9307%).
- Not started: 12,834.
- Possible duplicate groups: 548; conflicts: 376.
- Claims: 1,411 confirmed; 3,442 high; 1,606 medium; 202 low; 326
  conflicting; two unresolved.
- Citations: 6,007 records representing 3,109 unique source documents.
- Public data: 2,602 published affiliations, 929 organizations, 4,782 public
  sources, and 6,781 published claims.

## Durable inputs and replay

Reviewed identity decisions are stored in
`research/identity_review_decisions_2026-10-13_batch787.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page383-rammage-randall-review_batch-787_2026-10-13.json`.
Both were imported twice to confirm idempotent replay through the normal
pipeline.

Resume new-person research at PDF page 384, row 1, Joseph J Randazza. Full-
index historical research remains unfinished; 12,834 active people are still
`not_started`.
