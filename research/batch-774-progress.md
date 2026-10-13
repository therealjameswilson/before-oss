# Batch 774 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 774 covers PDF page 377, rows 1-23, Thomas G Presutti through Harvey O
Price. All 23 printed rows remain preserved as distinct source records and are
linked to 23 distinct person entities. Page 377 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 377, row 24,
Isma L Price.

This batch corrects the Batch 773 handoff text, which had incorrectly named
Daniel A Preston as the next indexed person. The source PDF, derived source-row
export, and SQLite database all identify page 377 row 1 as Thomas G Presutti.
No Daniel Preston source row was found. The Batch 773 progress and release
records now state the corrected boundary.

The visibly truncated note `Extract fr` for Francis B Price remains exactly as
printed and is not expanded. Full service or officer identifiers remain private
and masked in public output.

## Research protocol and review

- NARA Catalog work was dry-run only: 23 planned searches and zero
  authenticated requests. No key or API response was stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  their first attempted request. These source-access limitations are recorded
  as limitations, not negative evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, and archival
  query families were completed for all 23 people. Namesakes, discovery-only
  genealogy pages, people-finder results, unbridged postwar records, and
  temporally insufficient candidates were rejected.
- Twelve candidate decisions are durable: eleven accepted exact or core-name
  official Army records and one retained different-name conflict. Francis B
  Price's accepted exact-name Army candidate does not resolve the adjacent
  conflicting Army record.
- Twenty-three manual research attempts give every person in the batch a
  terminal disposition: 20 `requires_archival_review`, two
  `conflicting_sources`, and one `documented_prewar_employer_found`.

## Historical outcomes

- Ernest B Price has a high-confidence identity match. A guide to Franklin D.
  Roosevelt's office files names Ernest B. Price as OSS China Desk staff, while
  contemporary University of Chicago sources identify Ernest Batson Price as
  director of International House and a professor in 1938.
- The University of Chicago role is published as high-confidence
  `documented_prewar` employment. It is not labeled the immediate pre-OSS
  affiliation or the last civilian employer before wartime service. A postwar
  Standard-Vacuum Oil role and a temporally ambiguous January 1943 Brookings
  reference were excluded from the pre-OSS claim.
- Roger Prevost has a high-confidence exact-name plus protected-identifier Army
  match. A National Park Service history also places an exact-name Roger Prevost
  in June 1942 OSS Advanced Special Operations training, calling him a Free
  French Army lieutenant. Because the Army record reports an entry grade of
  private, the personnel-status disagreement remains a visible conflict and is
  not converted into a pre-OSS affiliation.
- Francis B Price remains conflicting. One official Army candidate is an exact
  name match, while an adjacent record tied to the same protected identifier
  names Clark Roland E. Neither record is treated as employer evidence.
- Exact-name and protected-identifier Army identity matches were accepted for
  Samuel J Prete, Walter Pretzat, Joseph J Previte, Francis H Prevost, John C
  Prevost, Roger Prevost, George D Prewitt, Barney L Priar, Venda A Pribramsky,
  and Arnold H Price. The Army coded occupations are not employers.
- The Army source adds `Jr` to Venda A Pribramsky; that suffix is retained as a
  documented variant rather than overwriting the indexed form.
- A 1952 alumni item about a same-name Thomas G Presutti lawyer is postwar and
  was rejected as pre-OSS evidence. Institutional records for a same-name
  Blanche E Price were withheld because no protected identifier or OSS bridge
  establishes that they belong to the indexed person.

## Exact coverage after Batch 774

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 10,804/23,939 (45.1314%).
- Verified-employer coverage: 353/23,939 (1.4746%).
- Verified-affiliation coverage: 792/23,939 (3.3084%).
- Archival-review coverage: 9,262/23,939 (38.69%).
- Not started: 13,130.
- Possible duplicate groups: 540; conflicts: 367.
- Claims: 1,408 confirmed; 3,320 high; 1,586 medium; 202 low; 320
  conflicting; two unresolved.
- Citations: 5,937 records representing 3,056 unique source documents.

## Durable inputs and replay

The reviewed decisions are stored in
`research/identity_review_decisions_2026-10-13_batch774.csv`; the evidence,
claims, source metadata, person updates, and manual attempts are stored in
`research/evidence-page377-presutti-price-review_batch-774_2026-10-13.json`.
Both files validate and import idempotently through the normal pipeline.

Resume new-person research at PDF page 377, row 24, Isma L Price. Full-index
historical research remains unfinished; 13,130 active people are still
`not_started`.
