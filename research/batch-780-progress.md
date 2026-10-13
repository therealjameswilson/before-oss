# Batch 780 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 780 covers PDF page 380, rows 1-23, Peppino Puleo through Mary C
Purdy. All 23 printed rows remain preserved as distinct source records and are
linked to 23 distinct person entities. Page 380 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 380, row 24,
Raymond J Purdy.

The clipped printed notes `Also Gre`, `Extract fr`, `One fold`, and `Also in B`
remain exactly as printed. None was silently expanded or used to infer an
employer, nationality, unit, or cross-reference. Full service or officer
identifiers remain private and masked in public output.

## Research protocol and review

- NARA Catalog work was dry-run only: 23 planned searches, one duplicate query
  skipped, and zero authenticated requests. No API key or response was stored.
- CIA Reading Room access failed closed on the first eligible request. The
  Library of Congress request stalled and was stopped without data loss. These
  are access limitations, not negative evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  military, foreign-language, and archival query families were reviewed for
  all 23 people. Namesakes, discovery-only genealogy, people-finder pages,
  postwar employers, and temporally insufficient candidates were rejected.
- Six official Army candidate decisions are durable high-confidence identity
  matches. Army occupation codes were not treated as employers or immediate
  affiliations.
- The James S Purdum Army candidate was rejected as a duplicate-person match:
  the same protected identifier appears with the separately printed Perdum and
  Purdum rows, which remain unmerged pending archival comparison.
- All 23 people now have the terminal status `requires_archival_review`.

## Historical outcomes

- A 2010 Grosse Pointe News obituary probably describes the historical Peppino
  Puleo represented by one or both same-name, same-rank Box 624 index rows.
  Both rows remain distinct in a visible possible-duplicate group because the
  source cannot determine whether the index represents one person or two.
- An official Army record and an AHEPA institutional profile support a
  high-confidence identity for Harry J. Pulos and document his OSS service in
  Europe. The business named in the 1981 profile is postwar and was excluded
  from pre-OSS affiliations.
- A University of Wisconsin alumni publication supports a high-confidence
  identity for Chalong Pungtragul. Its 1946 class year and 1958 alumni role are
  postwar and were not converted into a pre-OSS affiliation.
- The adjacent Udom Pupadhana and Udom Puhpadhana entries share a rare given
  name, rank, and near-identical spelling but have different boxes and no direct
  file linkage. They remain separate in a possible-duplicate group. Miami
  University student evidence remains only on the Puhpadhana entity.
- The separately printed James S Perdum and James S Purdum entries remain
  unmerged in their existing possible-duplicate group. A Congressional Record
  supports the Purdum spelling but does not prove that both index rows are one
  person.
- A divisional-roster lead for Louis A Punzirudu lacked an OSS or protected-ID
  bridge and remains an archival lead rather than a published identity claim.
  A postwar Edmund J Pung namesake was also rejected.

## Exact coverage after Batch 780

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 10,940/23,939 (45.6995%).
- Verified-employer coverage: 356/23,939 (1.4871%).
- Verified-affiliation coverage: 799/23,939 (3.3376%).
- Archival-review coverage: 9,399/23,939 (39.2623%).
- Not started: 12,994.
- Possible duplicate groups: 543; conflicts: 370.
- Claims: 1,410 confirmed; 3,389 high; 1,594 medium; 202 low; 322
  conflicting; two unresolved.
- Citations: 5,973 records representing 3,083 unique source documents.
- Public data: 2,591 published affiliations, 923 organizations, 4,748 public
  sources, and 6,711 published claims.

## Durable inputs and replay

The reviewed identity decisions are stored in
`research/identity_review_decisions_2026-10-13_batch780.csv`; the evidence,
claims, source metadata, person updates, duplicate safeguards, and terminal
manual attempts are stored in
`research/evidence-page380-puleo-purdy-review_batch-780_2026-10-13.json`.
Both files validate and import idempotently through the normal pipeline.

Resume new-person research at PDF page 380, row 24, Raymond J Purdy. Full-index
historical research remains unfinished; 12,994 active people are still
`not_started`.
