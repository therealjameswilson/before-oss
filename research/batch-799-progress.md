# Batch 799 research progress

Date: 2026-10-14 America/New_York

## Scope and preservation

Batch 799 covers PDF page 389, rows 24-46, Benjamin P Reyes through Charles E
Rhetts. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities. Page 389 was inspected against a 300 dpi render before
research. The next unresearched boundary is PDF page 390, row 1, Larry A Rhine.

The printed singular surname `Reynold`, the first-name field `Dana, Jr.`, the
spelling `Eward R Rhead`, the clipped notes `Record`, `British A`, `photogra`,
`permane`, and `middle in`, and Charles E Rhetts's combined `P-8 Lt J` grade
remain recoverable exactly as printed. Raymond E Reynolds's `PhM 2/c` grade was
reviewed as enlisted naval personnel without altering the raw index field.
Protected identifiers remain private.

## Research protocol and review

- NARA index context, exact-name OSS searches, employment and occupation
  searches, official and institutional sources, and newspaper, directory,
  obituary, military-roster, and archival searches were reviewed for all 23
  people. NARA live Catalog API access was unavailable because the runtime key
  was absent; the adapter failed closed without sending a request. CIA direct
  access was disallowed by robots policy, and the Library of Congress adapter
  encountered a network failure. These access limits were recorded and were
  not treated as negative historical evidence.
- All 23 people now have terminal `requires_archival_review` outcomes: one
  confirmed identity, one high-confidence identity, two probable identities,
  and 19 unresolved identities. Qualified medium-confidence findings remain
  excluded from default verified-employer analytics.
- A 1941 San Diego directory entry for a firefighter named Willard G Reynolds
  was rejected because it supplied no Naval Reserve, OSS, protected-identifier,
  or other identity bridge. A Navy S1 memorial candidate for Henry D Reynolds
  was rejected for an incompatible branch and rank.
- George Alexander Lucien Rheims's importing-company history belongs to George
  Loring Rheims's father and was explicitly rejected as employer evidence for
  the indexed son.
- No reliable employer was forced onto the remaining namesake-heavy Reynolds
  entries. Their profiles direct researchers to Boxes 640 or 641.

## Historical outcomes

- A contemporaneous official OSS awards record independently identifies Major
  Eward R. Rhead as British Army personnel and discusses the sufficiency of his
  contact with OSS activities. The identical unusual spelling, middle initial,
  rank, service, and OSS context support a high-confidence identity. British
  Army status is published as a military affiliation with uncertain temporal
  relation to OSS, not as a civilian employer or immediate predecessor.
- A family-submitted obituary in *The Norman Transcript* probably identifies
  the indexed Captain Hugh Reynolds: it dates his Army entry to 1937, states
  that he served with OSS at Omaha Beach, and records his later
  lieutenant-colonel rank. Because the name is common and no unique identifier
  is public, the identity and continuous Army-to-OSS pathway are published at
  medium confidence and require Box 641 confirmation.
- The Ritchie Boys roster and a record-cited family biography support George L
  Rheims as George Loring Rheims, who entered the Army in 1942 and later served
  as a captain in 2nd Infantry Division headquarters. The identity and Army
  status remain qualified at medium confidence because no accessible source
  directly bridges the biography to OSS or the indexed identifier.
- Dartmouth's institutional obituary explicitly identifies Charles Edward
  Rhetts as an OSS member and Navy lieutenant. Contemporary Dartmouth rosters
  document him at the War Production Board in August 1942 and as assistant to
  the attorney general in February 1943. Both are published as dated government
  assignments. Neither is labeled immediate pre-OSS because the accessible
  sources do not fully sequence his WPB, Justice, State, Navy, and OSS service.
- No source in this batch established a new confirmed or high-confidence
  civilian employer. Verified-employer coverage therefore remains unchanged.

## Exact coverage after Batch 799

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,366/23,939 (47.4790%).
- Verified-employer coverage: 368/23,939 (1.5372%).
- Verified-affiliation coverage: 818/23,939 (3.4170%).
- Archival-review coverage: 9,828/23,939 (41.0543%).
- Not started: 12,568.
- Possible duplicate groups: 550; conflicts: 390.
- Claims: 1,414 confirmed; 3,564 high; 1,619 medium; 202 low; 334
  conflicting; two unresolved.
- Citations: 6,080 records representing 3,166 unique source documents.
- Public data: 2,637 published affiliations, 948 organizations, 4,855 public
  sources, and 6,927 published claims.
- Total saved research attempts and plans: 21,972.

## Durable inputs and replay

Evidence, claims, source metadata, person updates, rejection reasons, and
terminal attempts are stored in
`research/evidence-page389-reyes-rhetts-review_batch-799_2026-10-14.json`.
The bundle was replayed through the normal importer and returned identical
object counts, verifying idempotence.

Resume new-person research at PDF page 390, row 1, Larry A Rhine. Full-index
historical research remains unfinished; 12,568 active people are still
`not_started`.
