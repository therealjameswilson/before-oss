# Batch 775 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 775 covers PDF page 377, rows 24-46, Isma L Price through Charles E
Prieve. All 23 printed rows remain preserved as distinct source records and are
linked to 23 distinct person entities. Page 377 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 378, row 1,
Vangjel Prifti.

The visibly truncated notes `Also Puc`, `One fold`, and `Also in B` remain
exactly as printed and are not expanded. The cross-references `Also 335` and
`Also 016`, and the note `French`, are also preserved. Full service or officer
identifiers remain private and masked in public output.

Ursula E Price had been stranded in the old `pilot-v1` batch with nonterminal
work. This batch adds a controlled, explicit, audited reassignment option and
migrates only that named prior assignment. Twenty-two people were newly
assigned to Batch 775 and one was reassigned from the pilot.

## Research protocol and review

- NARA Catalog work was dry-run only: 22 new planned searches, one duplicate
  prior search, and zero authenticated requests. No key or API response was
  stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  their first eligible request. These access limitations are recorded as
  limitations, not negative evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  and archival query families were reviewed for the batch. Namesakes,
  discovery-only genealogy and people-finder results, unbridged postwar
  records, and temporally insufficient candidates were rejected.
- Eleven official Army candidate decisions are durable: ten accepted
  high-confidence identity matches and one retained different-name conflict.
  Army occupation codes were not treated as employers or immediate
  affiliations.
- Edgar A Prichard already had a completed reviewed protocol and published
  evidence from an earlier cross-index batch. Twenty-two new manual attempts
  complete the remaining people without duplicating his claims.
- All 23 people now have terminal dispositions: 20
  `requires_archival_review`, one `conflicting_sources`, one
  `occupation_only_found`, and one `verified_employer_found`.

## Historical outcomes

- Nancy M Prichard is identified with high confidence as Nancy Montague
  McCandlish Prichard. Smithsonian Institution Archives states that she worked
  for three years as Special Assistant to the Meteorologist at the Smithsonian
  Astrophysical Observatory before joining OSS. A Washington Post obituary
  independently sequences Smithsonian administrative employment before her
  civilian OSS service and Cairo assignment.
- The Smithsonian Astrophysical Observatory is published as Nancy Prichard's
  immediate pre-OSS affiliation and last documented civilian employer. The
  Observatory remains a distinct historical organization rather than being
  silently collapsed into the Smithsonian Institution. The sources' differing
  role descriptions are both retained in the evidence record.
- Edgar A Prichard's previously published record remains unchanged: an
  official National Park Service history identifies his immediate pre-OSS
  assignment as an Army company clerk and describes him as a former Tulsa
  journalist, without naming the newspaper employer.
- Exact or core-name and protected-identifier Army identity matches were
  accepted for John S Price, Norman B Price, Norman S Price, Robert R Price,
  Roy T Price, Wayne E Price, Ellwood Pride, Sylvan A Priebe, Robert E
  Prieshoff, and Charles E Prieve. `Jr` is retained as a documented variant for
  Robert R Price and Wayne E Price. `Elwood` is retained as an Army-source
  spelling variant for indexed Ellwood Pride.
- Raford C Price remains conflicting because the Army record tied to the
  protected identifier carries a materially different name. It is not silently
  attributed to him.

## Exact coverage after Batch 775

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 10,825/23,939 (45.2191%).
- Verified-employer coverage: 354/23,939 (1.4788%).
- Verified-affiliation coverage: 793/23,939 (3.3126%).
- Archival-review coverage: 9,284/23,939 (38.7819%).
- Not started: 13,109.
- Possible duplicate groups: 540; conflicts: 368.
- Claims: 1,408 confirmed; 3,332 high; 1,586 medium; 202 low; 321
  conflicting; two unresolved.
- Citations: 5,941 records representing 3,059 unique source documents.

## Durable inputs and replay

The reviewed decisions are stored in
`research/identity_review_decisions_2026-10-13_batch775.csv`; the evidence,
claims, source metadata, person updates, and manual attempts are stored in
`research/evidence-page377-price-prieve-review_batch-775_2026-10-13.json`.
Both files validate and import idempotently through the normal pipeline.

Resume new-person research at PDF page 378, row 1, Vangjel Prifti. Full-index
historical research remains unfinished; 13,109 active people are still
`not_started`.
