# Batch 810 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 810 covers PDF page 395, rows 1-23, Henry B Roberts through Charles W
Robertson Jr. All 23 printed rows remain preserved as immutable source records
and map to 23 active person entities. Page 395 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 395, row 24,
Elizabeth A Robertson.

The clipped printed note `docume` remains intact and was not expanded into a
document type, employer, or OSS assignment. The two William A Roberts rows
remain separate: row 18 is a Private and row 19 is a Chief Boatswain's Mate,
and their protected identifiers differ. Full service numbers remain private
and are absent from public outputs.

## Research protocol and review

- Every person received NARA index context review, exact-name OSS searches,
  employment and occupation searches, and an applicable mix of military,
  obituary, institutional, newspaper, directory, and archival searches.
- The NARA Catalog adapter saved 23 deterministic dry-run plans because no API
  key was present in the local process environment. One duplicate request was
  skipped. Targeted CIA Reading Room and Library of Congress adapter attempts
  each failed after bounded handling. Neither access failure was treated as a
  negative historical result.
- All 23 people now have terminal attempted outcomes: 22 archival-review
  outcomes and one official-source conflict outcome.
- Eight identity review decisions were replayed idempotently: seven accepted
  exact-identifier matches and one conflicting identifier match.
- The reviewed evidence bundle was imported twice with identical object
  counts: three sources, zero organizations, zero affiliations, eight claims,
  23 person updates, 23 terminal manual attempts, and 17 claim-source links.
- No search snippet, family relationship, postwar employer, coded occupation,
  unlinked directory candidate, or famous namesake was published as a pre-OSS
  employer.

## Historical outcomes

- Exact protected-identifier comparisons confirm official Army entry records
  for Henry B. Roberts, Joe B. Roberts, Marcus Roberts, Odie G. Roberts Jr.,
  Ralph G. Roberts Jr., the Private William A. Roberts row, and Charles W.
  Robertson Jr. Their public identity claims omit full identifiers and coded
  occupations. The Army records alone do not establish employers or immediate
  OSS predecessors.
- Arthur C. Robertson's printed protected identifier points to an official
  Army record for John J. Perazza. The public profile preserves the conflict;
  no identity, chronology, occupation, or employer evidence is transferred.
- A Field Artillery officer-school roster for John R. Roberts, a 446th Bomb
  Group record for Joseph B. Roberts, a postwar Air Force lieutenant-colonel
  named Paul Roberts, and a cemetery result for Lucille T. Roberts were
  rejected because none bridges safely to the indexed person.
- Walter R. Roberts's documented Coordinator of Information and Office of War
  Information career was not assigned to the no-middle-initial Walter Roberts
  row. The name alone is insufficient, and Box 650 is required.
- No accepted source establishes a pre-OSS employer or affiliation for these
  23 people. Their profiles state that the accessible online protocol did not
  identify one and direct researchers to Box 650.

## Exact coverage after Batch 810

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,617/23,938 (48.5295%).
- Verified-employer coverage: 374/23,938 (1.5624%).
- Verified-affiliation coverage: 831/23,938 (3.4715%).
- Archival-review coverage: 10,080/23,938 (42.1088%).
- Not started: 12,316.
- Possible duplicate groups: 552; conflicts: 396.
- Claims: 1,443 confirmed; 3,631 high; 1,633 medium; 202 low; 340
  conflicting; two unresolved.
- Citations: 6,145 records representing 3,218 unique source documents.
- Public data: 2,665 published affiliations, 956 organizations, 4,920 public
  sources, and 7,043 published claims.
- Total saved research attempts and plans: 22,634.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch810.csv`. Evidence, claims,
person updates, rejection reasons, and terminal attempts are stored in
`research/evidence-page395-roberts-robertson-review_batch-810_2026-10-15.json`.
Both imports were replayed without duplicate decision rows or changed evidence
object counts.

Resume new-person research at PDF page 395, row 24, Elizabeth A Robertson.
Full-index historical research remains unfinished; 12,316 active people are
still `not_started`.
