# Batch 793 research progress

Date: 2026-10-14 America/New_York

## Scope and preservation

Batch 793 covers PDF page 386, rows 24-46, Dean E Reed through Jack J
Reeves. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities. Page 386 was inspected against a 300 dpi render before
research. The next unresearched boundary is PDF page 387, row 1, Harold J
Regan.

The clipped notes `Certificat`, `Record`, `Extract fr`, `photogra`, `British
A`, and `Italian Ar` remain exactly as printed and were not expanded. The
unusual indexed spelling `William Reeda Jr.` and printed grade `BM2/C T` also
remain unchanged. Full service identifiers remain private.

## Research protocol and review

- NARA Catalog and web adapters recorded 23 dry-run plans per adapter and made
  no authenticated NARA request. No Catalog API response bodies were stored.
- The CIA adapter failed closed for all 23 people. The Library of Congress
  adapter recorded 23 bounded outcomes: one candidate-bearing search, three
  no-result searches, and 19 transport errors. Access failures were not treated
  as negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  directory, military, variant-name, and archival query families were reviewed
  for all 23 people.
- Six Army bulk candidates were accepted using exact-name and nonshared
  protected-identifier agreement. Coded Army occupation fields were not
  treated as employers, and a coded date anomaly for Clifford H Reeh remains
  an archival question.
- Three Library of Congress candidates for William F Reedy were rejected after
  full-page OCR review: two named postwar choir director William W. Reedy and
  one named postwar taxicab-license holder William H. Reedy.
- All 23 people have the terminal status `requires_archival_review`. Six have
  high-confidence official identity matches; 17 remain unresolved. No employer
  or pre-OSS affiliation claim was created for this batch.

## Historical outcomes

- Official Army bulk data supports high-confidence identities for Marvin J
  Reed, William F Reedy, Clifford H Reeh, Emory K Rees, Lewis Y Rees, and
  Merlin C Reese. Each public claim states that the record corroborates identity
  and Army service only.
- Directory, university, obituary, memorial, grave, and family-history leads
  for other people were rejected when they lacked a direct OSS bridge or the
  required corroborating identifiers.
- A plausible John Embree Rees Jr. officer candidate was not adopted because
  it lacked the indexed protected identifier and a direct OSS link. No college
  affiliation was assigned to indexed John E Rees.
- Postwar photographer and naval-veteran namesakes were not used to expand
  Thomas W Reese's clipped `photogra` note into an occupation.
- The `British A` and `Italian Ar` notes remain unresolved. The presence of an
  Army bulk match for Merlin C Reese does not justify silently expanding or
  overriding the printed note.

## Exact coverage after Batch 793

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,234/23,939 (46.9276%).
- Verified-employer coverage: 362/23,939 (1.5122%).
- Verified-affiliation coverage: 808/23,939 (3.3752%).
- Archival-review coverage: 9,694/23,939 (40.4946%).
- Not started: 12,700.
- Possible duplicate groups: 550; conflicts: 381.
- Claims: 1,413 confirmed; 3,496 high; 1,611 medium; 202 low; 331
  conflicting; two unresolved.
- Citations: 6,039 records representing 3,133 unique source documents.
- Public data: 2,612 published affiliations, 932 organizations, 4,814 public
  sources, and 6,847 published claims.
- Total saved research attempts and plans: 21,462.

## Durable inputs and replay

Reviewed candidate decisions are stored in
`research/identity_review_decisions_2026-10-14_batch793.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page386-reed-reeves-review_batch-793_2026-10-14.json`.
Both were replayed through the normal import commands to verify idempotence.

Resume new-person research at PDF page 387, row 1, Harold J Regan. Full-index
historical research remains unfinished; 12,700 active people are still
`not_started`.
