# Batch 792 research progress

Date: 2026-10-14 America/New_York

## Scope and preservation

Batch 792 covers PDF page 386, rows 1-23, Margot F Reck through Catherine C
Reed. The 23 printed rows remain preserved as distinct source records linked
to 22 person entities. Everett S Redmond appears twice with the same name and
protected identifier; both source rows remain visible while one cautious person
entity carries the documented possible-duplicate group. Page 386 was inspected
against a 300 dpi render before research. The next unresearched boundary is PDF
page 386, row 24, Dean E Reed.

The clipped notes `Record`, `Extract fr`, `extract fr`, `photogra`, `WWII ce`,
`French`, and `1st Lt A` remain exactly as printed and were not expanded. Full
service identifiers remain private.

## Research protocol and review

- NARA Catalog and web adapters recorded 22 dry-run plans per adapter and made
  no authenticated NARA request. No Catalog API response bodies were stored.
- The CIA adapter failed closed on its first eligible request. The Library of
  Congress adapter returned one postwar Benjamin W Reed candidate and one
  timeout; neither access outcome was treated as negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  directory, military, variant-name, and archival query families were reviewed
  for all 22 people.
- Ten Army bulk candidates for nine people were accepted using exact-name and
  nonshared protected-identifier agreement. Everett Redmond's two candidates
  correspond to the two separately preserved index rows. Army coded fields
  were not treated as employers.
- The Library of Congress Benjamin Reed candidate was rejected after page
  review because the 1951 newspaper page contained no bridge to the indexed
  person and was postwar.
- All 22 people have saved terminal outcomes: Willis C Reddick is
  `occupation_only_found`; the other 21 are `requires_archival_review`.

## Historical outcomes

- A Kansas City Star obituary identifies Margot F Reck as Margot Ford Reck and
  explicitly documents her OSS cartography. It says she joined the WASP
  program in 1942, but its chronology does not justify treating WASP as a
  pre-OSS affiliation. Her immediate pre-OSS status remains unresolved.
- A Hoover Institution finding aid has a 1941-1944 correspondence folder titled
  `Hood College (Olive I. Reddick, Henry I. Stahr)`. A 1950 contemporary
  newspaper independently identifies Dr. Olive I. Reddick as head of Hood's
  sociology and economics department and a faculty member. The project
  publishes a medium-confidence prewar professional affiliation, not an
  employer claim; the later faculty title is not backdated.
- A detailed secondary history identifies Willis C Reddick as Willis Calhoun
  Reddick, matches his OSS document-printing role and lieutenant-colonel rank,
  and describes him as an Illinois printer. The project publishes a qualified
  occupation-only claim and does not invent a printing-company employer.
- The 1942 *Journal of the United States Artillery* credits Captain Ralph H
  Redford as a coauthor in the Coast Artillery context. This supports a
  qualified dated military affiliation and plausible promotion to the indexed
  major rank, but not an immediate pre-OSS transfer.
- Official CIA and Congressional records identify Hugh F Redmond as Hugh
  Francis Redmond, a former paratrooper and stay-behind staff employee. Their
  postwar businessman description is not converted into pre-OSS employment.
- Official Army evidence and an OSS Operational Groups roster identify Martin
  Redovian at high confidence and place him in Greek Group VIII. Those sources
  document wartime service, not a pre-OSS employer.
- Common-name, casualty, alumni, patent, directory, and vital-record leads were
  rejected when they lacked the required OSS bridge or corroborating
  identifiers. Sensitive identifiers from unrelated vital records were neither
  retained nor published.

## Exact coverage after Batch 792

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,211/23,939 (46.8315%).
- Verified-employer coverage: 362/23,939 (1.5122%).
- Verified-affiliation coverage: 808/23,939 (3.3752%).
- Archival-review coverage: 9,671/23,939 (40.3985%).
- Not started: 12,723.
- Possible duplicate groups: 550; conflicts: 381.
- Claims: 1,413 confirmed; 3,490 high; 1,611 medium; 202 low; 331
  conflicting; two unresolved.
- Citations: 6,037 records representing 3,132 unique source documents.
- Public data: 2,612 published affiliations, 932 organizations, 4,812 public
  sources, and 6,841 published claims.
- Total saved research attempts and plans: 21,347.

## Durable inputs and replay

Reviewed identity decisions are stored in
`research/identity_review_decisions_2026-10-14_batch792.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page386-reck-reed-review_batch-792_2026-10-14.json`.
Both were replayed through the normal import commands to verify idempotence.

Resume new-person research at PDF page 386, row 24, Dean E Reed. Full-index
historical research remains unfinished; 12,723 active people are still
`not_started`.
