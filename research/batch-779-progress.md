# Batch 779 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 779 covers PDF page 379, rows 24-46, Alvin G Psinas through
Michael C Puleo. All 23 printed rows remain preserved as distinct source
records and are linked to 23 distinct person entities. Page 379 was inspected
against a 300 dpi render before research. The next unresearched boundary is PDF
page 379, row 47.

George J Pugliese's printed note `Ind. Arm` and Michael C Puleo's printed note
`French` remain exactly as printed. Neither note was expanded or used to infer
an employer, nationality, or unit. Full service or officer identifiers remain
private and masked in public output.

## Research protocol and review

- NARA Catalog work was dry-run only: 23 planned searches and zero
  authenticated requests. No API key or response was stored.
- The CIA Reading Room adapter failed closed on its first eligible request.
  Library of Congress completed three no-result checks before a later request
  stalled and was stopped without data loss. These are access limitations, not
  negative evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  military, foreign-language, and archival query families were reviewed for
  all 23 people. Namesakes, people-finder pages, discovery-only genealogy,
  postwar employers, and temporally insufficient candidates were rejected.
- Ten official Army candidate decisions are durable high-confidence identity
  matches. Army occupation codes were not treated as employers or immediate
  affiliations.
- Two protected-identifier candidates were rejected: one mapped George J
  Pugliese to a wholly different Army name; the other mapped Peter N Pugliese
  to Peter F Pugliese even though the index preserves separate Peter N and
  Peter F rows.
- All 23 people now have terminal dispositions: 22
  `requires_archival_review` and one `occupation_only_found`.

## Historical outcomes

- National Park Service history identifies George N. Psoinos as a
  Greek-American radio operator on the OSS Peking mission. This establishes a
  high-confidence wartime identity but not a pre-OSS employer.
- Contemporary University of Notre Dame reporting identifies Udom Puhpadhana
  as a Miami University student in 1942. A University of Minnesota alumni
  report independently corroborates the distinctive identity and later Free
  Thai service. Miami University is modeled as student status, not employment,
  and is not labeled the immediate pre-OSS affiliation.
- Exact name and nonshared protected-identifier Army matches were accepted for
  Alvin G Psinas, Alexander Psomas, Alexander L Puccinelli, Edward W Pucel,
  Tode Puchovich, Arthur Pugh, Leon L Pugh, Vincent Puglisi, Chester J Pulaski,
  and Michael C Puleo. No coded Army occupation was converted into an employer.
- A 1958 directory entry placing a Leo F Ptacek at Signal Oil was rejected as
  both postwar and unbridged to the index row. It is not included in the site's
  oil-company category.
- A 1946 official record identifying Alexander L Puccinelli as a district
  attorney was also rejected for the pre-OSS question because it is postwar.

## Exact coverage after Batch 779

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 10,917/23,939 (45.6034%).
- Verified-employer coverage: 356/23,939 (1.4871%).
- Verified-affiliation coverage: 799/23,939 (3.3376%).
- Archival-review coverage: 9,376/23,939 (39.1662%).
- Not started: 13,017.
- Possible duplicate groups: 542; conflicts: 369.
- Claims: 1,410 confirmed; 3,382 high; 1,590 medium; 202 low; 322
  conflicting; two unresolved.
- Citations: 5,966 records representing 3,078 unique source documents.
- Public data: 2,591 published affiliations, 923 organizations, 4,741 public
  sources, and 6,700 published claims.

## Durable inputs and replay

The reviewed decisions are stored in
`research/identity_review_decisions_2026-10-13_batch779.csv`; the evidence,
claims, source metadata, person updates, and terminal manual attempts are stored
in
`research/evidence-page379-psinas-puleo-review_batch-779_2026-10-13.json`.
Both files validate and import idempotently through the normal pipeline.

Resume new-person research at PDF page 379, row 47. Full-index historical
research remains unfinished; 13,017 active people are still `not_started`.
