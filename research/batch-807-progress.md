# Batch 807 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 807 covers PDF page 393, rows 24-46, Ove A Rise through Fred R
Riveglia. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 393 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 394, row 1,
Mildred B Rivkin.

The clipped notes `British A`, `extract fr`, `Record`, `photogra`, and `also
1st` remain intact. None was silently expanded into a nationality, branch,
occupation, or assignment. Full service numbers remain private and are absent
from public outputs.

## Research protocol and review

- Every person received NARA index context review, exact-name OSS searches,
  employment and occupation searches, and an applicable mix of military,
  obituary, institutional, newspaper, directory, and archival searches.
- The NARA Catalog adapter saved 23 deterministic dry-run plans because no API
  key was present in the local process environment. A live CIA Reading Room
  attempt failed closed under the site's robots policy, and a Library of
  Congress attempt exhausted bounded retries after a network error. Neither
  access failure was counted as a negative historical result.
- All 23 people now have terminal attempted outcomes: three completed military
  or student-pathway outcomes, one occupation-only outcome, three identity-
  review outcomes, and 16 archival-review outcomes.
- The reviewed evidence bundle was imported twice with identical object
  counts: eight sources, four reused organizations, five affiliations, nine
  claims, 23 person updates, 23 terminal attempts, and 18 claim-source links.
- No search snippet, family tree, modern successor, postwar employer, or
  low-confidence candidate was published as a pre-OSS fact.

## Historical outcomes

- Official Marine Corps records confirm indexed Sergeant Jack R. Risler by
  exact name, rank, and a privately compared protected identifier, and place
  him in the OSS Union II mission. A detailed military-history account says he
  was recruited while serving as a Marine parachute instructor at New River.
  That immediate assignment is published as a qualified medium-confidence
  military claim, not as civilian employment. His rank-only parser category was
  corrected from Army to enlisted Marine Corps personnel on this direct
  evidence.
- A 1947 newspaper notice supports a high-confidence Oskar Rismondo identity
  and documents New York University graduation and wartime Army service in
  Africa and Italy. NYU remains student status, not employment; neither item is
  called the immediate OSS predecessor because the sequence is not established.
- A reputable obituary explicitly says Haiden Ritchie served as an OSS officer
  after graduating from Dartmouth College. Contemporary Dartmouth evidence
  identifies him with the class of 1944 in Egypt. Dartmouth is therefore his
  high-confidence immediate pre-OSS affiliation as a student, not an employer.
- Brown University's alumni magazine directly identifies Fred R. Riveglia as
  a U.S. Army paratrooper and OSS group member. The Army relationship is
  published with uncertain sequence; Brown study and Pratt & Whitney employment
  were postwar and are not backdated.
- A middle-initial conflict keeps Herschel G. Rismiller separate from a
  Herschel C. Rismiller Army candidate. Alvis O. Ritter's different grade and
  Albert Ritzenberg's missing OSS bridge likewise remain review leads rather
  than public identity or employer claims.

## Exact coverage after Batch 807

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,548/23,938 (48.2413%).
- Verified-employer coverage: 374/23,938 (1.5624%).
- Verified-affiliation coverage: 829/23,938 (3.4631%).
- Archival-review coverage: 10,011/23,938 (41.8205%).
- Not started: 12,385.
- Possible duplicate groups: 552; conflicts: 394.
- Claims: 1,424 confirmed; 3,628 high; 1,632 medium; 202 low; 338
  conflicting; two unresolved.
- Citations: 6,132 records representing 3,210 unique source documents.
- Public data: 2,662 published affiliations, 955 organizations, 4,907 public
  sources, and 7,018 published claims.
- Total saved research attempts and plans: 22,464.

## Durable inputs and replay

Evidence, claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page393-rise-riveglia-review_batch-807_2026-10-15.json`.
Its import was replayed with identical counts, confirming idempotent outcomes.

Resume new-person research at PDF page 394, row 1, Mildred B Rivkin. Full-index
historical research remains unfinished; 12,385 active people are still
`not_started`.
