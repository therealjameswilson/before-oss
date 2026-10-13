# Batch 778 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 778 covers PDF page 379, rows 1-23, George P Prosnik through
Charles D Psilopoulos. All 23 printed rows remain preserved as distinct source
records and are linked to 23 distinct person entities. Page 379 was inspected
against a 300 dpi render before research. The next unresearched boundary is PDF
page 379, row 24, Alvin G Psinas.

Alice R Provensen's clipped printed note `Extract fr` remains exactly as
printed. It was not expanded, completed, or used to infer an employer. Full
service or officer identifiers remain private and masked in public output.

## Research protocol and review

- NARA Catalog work was dry-run only: 23 planned searches and zero
  authenticated requests. No API key or response was stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  their first eligible request. These access limitations are recorded as
  limitations, not negative evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  military, foreign-language, and archival query families were reviewed for
  all 23 people. Namesakes, modern people-finder pages, discovery-only
  genealogy, postwar employers, and temporally insufficient candidates were
  rejected.
- Nine official Army candidate decisions are durable high-confidence identity
  matches. Army occupation codes were not treated as employers or immediate
  affiliations.
- All 23 people now have terminal dispositions: 21
  `requires_archival_review`, one `documented_prewar_employer_found`, and one
  `occupation_only_found`.

## Historical outcomes

- An official 1933 Ohio Attorney General opinion identifies Knox P. Pruden as
  an auditor in the Ohio Bureau of Motor Vehicles. A contemporary 1938 Ohio
  National Guard history separately documents his command of Headquarters
  Company, 74th Brigade from 17 January 1930 through at least 1938. The state
  job and military assignment are modeled separately; neither is labeled the
  immediate pre-OSS affiliation or last civilian employer.
- A detailed obituary traces Henry A. Prunier from three years as a student at
  Assumption College into the Army, through Army language and cryptology
  training, and then by explicit order to Washington to join OSS Deer Team.
  The Army is therefore published as his confirmed immediate pre-OSS military
  affiliation. Assumption remains student status, not employment, and no
  pre-enlistment civilian employer is inferred.
- A detailed obituary identifies Charles Provenzano as Charles Louis
  Provenzano, born Calogero, and matches his Navy Specialist First Class and
  OSS service. Its art-and-antiques business evidence is postwar and is not
  presented as pre-OSS employment.
- The Foreign Service Journal identifies Virginia Pryor among the first nine
  OSS women sent toward Ceylon in March 1944. National Park Service history
  identifies Corporal Spero Psarakis of Brooklyn in the Greek Operational
  Groups. These establish high-confidence wartime identities but not pre-OSS
  employers.
- Exact name and nonshared protected-identifier Army matches were accepted for
  George P Prosnik, Leonard S Prout, Palmiro P Provenzano, Charles N Province,
  James B Pruett, Henry A Prunier, Edward S Przybyla, Spero Psarakis, and
  Charles D Psilopoulos. No coded Army occupation was converted into an
  employer.

## Exact coverage after Batch 778

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 10,894/23,939 (45.5073%).
- Verified-employer coverage: 356/23,939 (1.4871%).
- Verified-affiliation coverage: 798/23,939 (3.3335%).
- Archival-review coverage: 9,353/23,939 (39.0701%).
- Not started: 13,040.
- Possible duplicate groups: 542; conflicts: 369.
- Claims: 1,410 confirmed; 3,369 high; 1,590 medium; 202 low; 322
  conflicting; two unresolved.
- Citations: 5,961 records representing 3,075 unique source documents.
- Public data: 2,590 published affiliations, 922 organizations, 4,736 sources,
  and 6,687 claims.

## Durable inputs and replay

The reviewed decisions are stored in
`research/identity_review_decisions_2026-10-13_batch778.csv`; the evidence,
claims, source metadata, person updates, and terminal manual attempts are stored
in
`research/evidence-page379-prosnik-psilopoulos-review_batch-778_2026-10-13.json`.
Both files validate and import idempotently through the normal pipeline.

Resume new-person research at PDF page 379, row 24, Alvin G Psinas.
Full-index historical research remains unfinished; 13,040 active people are
still `not_started`.
