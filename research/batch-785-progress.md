# Batch 785 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 785 covers PDF page 382, rows 25-46, Edwin R Raddatz through
Philip E Ragan. All 22 printed rows remain preserved as distinct source records
and are linked to 22 person entities. Page 382 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 383, row 1,
Peter Rago.

The clipped notes "Docume" and "file retai" and the printed note "French"
remain exactly as indexed. They were not silently expanded or converted into
employer, nationality, or record-status claims. Full service or officer
identifiers remain private and masked in public output.

## Research protocol and review

- NARA Catalog and web adapters were dry-run only: 22 planned searches per
  adapter, with zero authenticated NARA requests and no response bodies stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  the first eligible request. These access outcomes are limitations, not
  negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  military, variant-name, and archival query families were reviewed for all 22
  people. Namesakes, modern people-finder records, discovery-only genealogy,
  postwar evidence, and temporally insufficient candidates were rejected.
- Five official Army identity candidates were accepted: Alan R Rado, Charles C
  Raftell, Clarence T Rader, Harold R Raemer, and Vjekoslav Radic. Clarence T
  Rader's Army row adds a Jr. suffix. Army occupation codes were not treated as
  employers or immediate affiliations.
- Edwin R Raddatz remains probable because the official Army row spells the
  surname RADDARZ. Eugene Radzikowski remains conflicting because one exact-name
  Army row and three incompatible names share the printed index identifier.
  Nathan Raenoff remains conflicting because the official Army row tied to the
  printed identifier names a different person.
- Nineteen people now have the terminal status "requires_archival_review"; two
  have "conflicting_sources"; Aldo L Raffa has
  "documented_prewar_employer_found".

## Historical outcomes

- Mikkel Dack's Cambridge University Press history identifies Maj. Aldo Raffa
  as a political-science instructor at Georgetown University, says that the
  instructor had originally been recruited by OSS, and cites the identically
  named RG 226 Box 630 personnel file. This supports high-confidence identity
  and Georgetown as the best-supported last identifiable civilian employer.
  Because the source does not explicitly say Raffa left Georgetown directly for
  OSS, the affiliation is published as medium-confidence and
  "probable_immediate," not as a verified immediate predecessor.
- Official Army bulk evidence supports high-confidence identity matches for
  Alan R Rado, Charles C Raftell, Clarence T Rader, Harold R Raemer, and
  Vjekoslav Radic. It supports identity and military service only.
- Edwin R Raddatz's one-letter surname discrepancy remains visible as a
  qualified probable identity. Eugene Radzikowski and Nathan Raenoff receive
  public conflict explanations rather than silent matches.
- No new confirmed/high-confidence civilian employer was added, so default
  verified-employer analytics remain unchanged. Profiles without reliable
  employment evidence direct researchers to the indexed personnel files rather
  than implying that no prior employment existed.

## Exact coverage after Batch 785

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,054/23,939 (46.1757%).
- Verified-employer coverage: 358/23,939 (1.4955%).
- Verified-affiliation coverage: 803/23,939 (3.3544%).
- Archival-review coverage: 9,513/23,939 (39.7385%).
- Not started: 12,880.
- Possible duplicate groups: 547; conflicts: 375.
- Claims: 1,411 confirmed; 3,423 high; 1,606 medium; 202 low; 325
  conflicting; two unresolved.
- Citations: 6,000 records representing 3,104 unique source documents.
- Public data: 2,600 published affiliations, 929 organizations, 4,775 public
  sources, and 6,761 published claims.

## Durable inputs and replay

The reviewed identity decisions are stored in
"research/identity_review_decisions_2026-10-13_batch785.csv"; the evidence,
claims, source metadata, person updates, and terminal manual attempts are stored
in
"research/evidence-page382-raddatz-ragan-review_batch-785_2026-10-13.json".
Both files validate and replay idempotently through the normal pipeline.

Resume new-person research at PDF page 383, row 1, Peter Rago. Full-index
historical research remains unfinished; 12,880 active people are still
"not_started".
