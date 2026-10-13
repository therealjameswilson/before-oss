# Batch 777 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 777 covers PDF page 378, rows 24-46, Herbert V Prochnow through
Catherine L Prosnak. All 23 printed rows remain preserved as distinct source
records and are linked to 23 distinct person entities. Page 378 was inspected
against a 300 dpi render before research. The next unresearched boundary is PDF
page 379, row 1, George P Prosnik.

The note `Also 327` remains exactly as printed. The adjacent Edward S Prorok
entries remain separate: one is an enlisted United States Army record and the
other is a French first-lieutenant record with a different protected
identifier. Full service or officer identifiers remain private and masked in
public output.

## Research protocol and review

- NARA Catalog work was dry-run only: 23 planned searches, one duplicate
  request skipped, and zero authenticated requests. No API key or response was
  stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  their first eligible request. These access limitations are recorded as
  limitations, not negative evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  radio, foreign-language, and archival query families were reviewed for all
  23 people. Namesakes, discovery-only genealogy, unbridged postwar records,
  and temporally insufficient candidates were rejected.
- Eight official Army candidate decisions are durable high-confidence identity
  matches. Army occupation codes were not treated as employers or immediate
  affiliations.
- All 23 people now have terminal dispositions: 20
  `requires_archival_review`, two `documented_prewar_employer_found`, and one
  `occupation_only_found`.

## Historical outcomes

- A July 1942 contemporary banking publication identifies Herbert V Prochnow
  as assistant vice president of the First National Bank of Chicago. The
  employer is published as high-confidence documented pre-OSS employment, not
  as the immediate affiliation or last civilian employer, because no accessible
  source establishes his OSS entry date or a direct transition.
- Official Luxembourg municipal sources identify Wenzel Profant as a sculptor
  who worked on Esch-sur-Alzette's 1935-1937 city hall and as a co-founder of
  the resistance organization ALWERAJE. The latter is modeled as volunteer
  resistance work, not employment. No employer is inferred from the occupation.
- A 1933 radio trade bulletin identifies Leopold Proser as a former member of
  the British Broadcasting Company's London staff, while the Paley Center
  credits him as a radio writer in 1936. Because neither source independently
  connects the broadcaster to OSS, the identity and BBC employment remain
  medium-confidence and visibly qualified.
- Exact name and nonshared protected-identifier Army matches were accepted for
  Albert M Proctor, Lewis J Proctor, Charles E Proffitt, Arthur J Prohl, Robert
  F Prokop, Buster R Propes, Sherman C Propes, and the enlisted Edward S Prorok
  row. The suffix `Jr` was preserved as a variant for Lewis Proctor and Arthur
  Prohl. No coded Army occupation was converted into an employer.
- The French Edward S Prorok row remains unresolved and separate from the
  enlisted row. The two profiles share only a privacy-safe duplicate-group key;
  no identity or affiliation claim crosses between them.

## Exact coverage after Batch 777

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 10,871/23,939 (45.4113%).
- Verified-employer coverage: 356/23,939 (1.4871%).
- Verified-affiliation coverage: 796/23,939 (3.3251%).
- Archival-review coverage: 9,330/23,939 (38.9741%).
- Not started: 13,063.
- Possible duplicate groups: 542; conflicts: 369.
- Claims: 1,408 confirmed; 3,356 high; 1,590 medium; 202 low; 322
  conflicting; two unresolved.
- Citations: 5,953 records representing 3,069 unique source documents.
- Public data: 2,586 published affiliations, 918 organizations, 4,728 sources,
  and 6,672 claims.

## Durable inputs and replay

The reviewed decisions are stored in
`research/identity_review_decisions_2026-10-13_batch777.csv`; the evidence,
claims, source metadata, person updates, and terminal manual attempts are stored
in
`research/evidence-page378-prochnow-prosnak-review_batch-777_2026-10-13.json`.
Both files validate and import idempotently through the normal pipeline.

Resume new-person research at PDF page 379, row 1, George P Prosnik.
Full-index historical research remains unfinished; 13,063 active people are
still `not_started`.
