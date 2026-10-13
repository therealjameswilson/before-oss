# Batch 786 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 786 covers PDF page 383, rows 1-24, Peter Rago through Angelo Ramirez.
All 24 printed rows remain preserved as distinct source records linked to 24
person entities. Page 383 was inspected against a 300 dpi render before
research. The next unresearched boundary is PDF page 383, row 25, Tommie I
Rammage.

The clipped notes "Polish Ar", "Also Ann", and "Also Par" and the printed note
"French" remain exactly as indexed. They were not silently expanded or
converted into employer, nationality, alias, or record-status claims. Full
service or officer identifiers remain private and masked in public output.

## Research protocol and review

- NARA Catalog and web adapters were dry-run only: 24 planned searches per
  adapter, with zero authenticated NARA requests and no response bodies stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  the first eligible request. These access outcomes are limitations, not
  negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  military, variant-name, and archival query families were reviewed for all 24
  people. Namesakes, people-finder records, discovery-only genealogy, postwar
  evidence, and temporally insufficient candidates were rejected.
- Seven official Army candidates were accepted as high-confidence identity
  evidence: Peter Rago, Maurice T Ragsdale, Charles E Rahn, Milton E Raichle,
  Archie B Rainey, Matti Raivio, and Floyd B Rambin. Army occupation codes were
  not treated as employers or immediate affiliations.
- Official NARA and Department of Defense sources support a high-confidence
  identity match for 1st Lt Michael Rajacich and corroborate his OSS Operation
  Halyard service. A discovery-only pre-OSS War Department employment claim was
  not published because its underlying source was not directly inspected.
- All 24 people now have the terminal status "requires_archival_review".

## Historical outcomes

- Official Army bulk evidence supports seven high-confidence identity matches.
  It supports identity and Army service only.
- A declassified 1946 U.S. Army record names Lieutenant Michael Rajacich in
  military-intelligence context, and a Department of Defense history identifies
  him on the OSS Operation Halyard team. Neither source establishes his
  pre-OSS employer.
- A secondary Operation RYPE roster lists Matti Raivio, but it does not
  establish pre-OSS employment and was not used as employer evidence.
- No new confirmed/high-confidence civilian employer was added. Profiles
  without reliable employment evidence direct researchers to the indexed
  personnel files rather than implying that no prior employment existed.

## Exact coverage after Batch 786

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,078/23,939 (46.2760%).
- Verified-employer coverage: 358/23,939 (1.4955%).
- Verified-affiliation coverage: 803/23,939 (3.3544%).
- Archival-review coverage: 9,537/23,939 (39.8388%).
- Not started: 12,856.
- Possible duplicate groups: 547; conflicts: 375.
- Claims: 1,411 confirmed; 3,431 high; 1,606 medium; 202 low; 325
  conflicting; two unresolved.
- Citations: 6,004 records representing 3,107 unique source documents.
- Public data: 2,600 published affiliations, 929 organizations, 4,779 public
  sources, and 6,769 published claims.

## Durable inputs and replay

Reviewed identity decisions are stored in
`research/identity_review_decisions_2026-10-13_batch786.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page383-rago-ramirez-review_batch-786_2026-10-13.json`.
Both validate and replay idempotently through the normal pipeline.

Resume new-person research at PDF page 383, row 25, Tommie I Rammage. Full-index
historical research remains unfinished; 12,856 active people are still
`not_started`.
