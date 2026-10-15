# Batch 825 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 825 covers PDF page 402, rows 24-46, Earl G Rowell through Christopher
Rubio. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 402 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 403, row 1,
Howard L Ruble.

Printed names, initials, ranks or grades, blank cells, private identifiers,
box numbers, notes, and archival locations remain recoverable exactly as
indexed. Full service identifiers remain private and are absent from public
outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks.
- The NARA Catalog adapter recorded deterministic dry-run queries because no
  securely configured API key was present in the process environment. A CIA
  adapter access failure and a bounded Library of Congress search without a
  candidate were not treated as historical negative evidence.
- Three exact protected-identifier Army matches were accepted for identity
  only. Army occupation codes were not published as jobs or employers. Three
  incompatible name candidates were explicitly rejected and remain visible
  in review notes.
- Immediate affiliations, last civilian employers, and earlier documented
  pre-OSS roles were modeled separately. Morton W Royse's Federal Writers'
  Project role was not forced into an unsupported immediate-predecessor claim.
- All 23 people now have saved, reviewable, terminal outcomes. Cases without
  adequate online evidence identify the indexed Box 664 or 665 personnel file
  as the next evidence target.

## Historical outcomes

- A direct 1944 OSS report identifies Morton W Royse and records his April
  1942 entry into the Foreign Nationalities Branch. An Oxford University Press
  scholarly account documents his earlier work as social-ethnic studies
  editor for the Federal Writers' Project. The federal role is published as
  other documented pre-OSS government work, not as immediate, because the
  accessible chronology does not rule out an intervening affiliation.
- A Library of Congress finding aid and the Congressional Record corroborate
  the career-Army identity of Herbert F Roye across captain, major, and
  colonel references. They do not establish his exact pre-OSS unit or a
  civilian employer.
- Official Army data confirms Emile G Roy, Anthony P Rua, and Herbert Rubin
  for identity and Army-entry chronology only. No coded occupation was
  converted into a public job or employer claim.
- The protected-identifier candidates attached to Alexander M Rozanoff, Wilmo
  R Roy, and Stanley Rubini named Stratton Earl E, Kuelling Herbert W, and
  Rubint Stanley. Those candidates were rejected as incompatible, and all
  three indexed people remain conflicting pending review of Box 664.
- The remaining unresolved profiles state that no reliable pre-OSS employer
  has yet been identified in the accessible sources reviewed and explain why
  the indexed personnel file may require archival examination.

## Exact coverage after Batch 825

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,955/23,938 (49.9415%).
- Verified-employer coverage: 388/23,938 (1.6209%).
- Verified-affiliation coverage: 860/23,938 (3.5926%).
- Archival-review coverage: 10,419/23,938 (43.5249%).
- Not started: 11,978.
- Possible duplicate groups: 553; conflicts: 408.
- Claims: 1,540 confirmed; 3,696 high; 1,648 medium; 202 low; 351
  conflicting; two unresolved.
- Citations: 6,241 records representing 3,289 unique source documents.
- Total saved research attempts and plans: 23,497.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch825.csv`. Evidence,
identity claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page402-rowell-rubio-review_batch-825_2026-10-15.json`.

The identity-decision replay skipped all six duplicate decisions on the second
import. Evidence replay retained exactly 23 Batch 825 attempts, one
affiliation, nine claims, 19 claim-source links, one organization, and six
sources. SQLite reports no foreign-key violations.

## Local release verification

- Python: 145 tests passed.
- Astro: 459 source files checked with zero errors, warnings, or hints; 24,969
  static HTML pages built.
- Browser: 84/84 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 15 Batch 825 checks.
- Links: all 24,969 generated HTML files passed internal-link checks; 51,153
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,041 built artifacts; aggregate and manifest false positives were zero.
- Manifest: 67 assets and 112,935,863 bytes verified in the built public tree;
  manifest SHA-256
  `5ce709a09a06e84ef491a7366994d7981835105b74ddb783e6525f590f010b54`.
- Determinism: two consecutive production builds produced SHA-256
  `0daf17416eb230655bacb5e6291716ba6d881d271a9ce146c9f11430c12351c2`
  across 25,041 files and 319,270,491 bytes.

Resume new-person research at PDF page 403, row 1. Full-index historical
research remains unfinished; 11,978 active people are still `not_started`.
