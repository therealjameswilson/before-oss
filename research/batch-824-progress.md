# Batch 824 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 824 covers PDF page 402, rows 1-23, Maurice H Rottersmann through Thora
H Rowe. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 402 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 402, row
24, Earl G Rowell.

Printed names, initials, ranks or grades, blank cells, private identifiers,
box numbers, notes, and archival locations remain recoverable exactly as
indexed. Maurice H Rottersmann and the earlier Maurice H Rettersmann remain
separate rows because their printed surnames and boxes differ despite a shared
protected identifier. Full service identifiers remain private and are absent
from public outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks.
- The NARA Catalog adapter recorded 23 deterministic dry-run queries because
  no securely configured API key was present in the process environment. The
  CIA and Library of Congress adapters each recorded a bounded source-access
  error. These access failures were not treated as historical negative
  evidence.
- Five exact protected-identifier Army matches were accepted for identity
  only. Army occupation codes were not published as jobs or employers. Five
  incompatible name candidates were explicitly rejected and remain visible
  in review notes.
- Immediate military or government pathways, last civilian employers, and
  earlier student or work affiliations were modeled separately. Overlapping
  1941 appointments were not forced into unsupported day-level sequences.
- All 23 people now have saved, reviewable, terminal outcomes: five
  documented-prewar outcomes, 17 archival-review outcomes, and one explicitly
  conflicting case.

## Historical outcomes

- Official Army data, a Denver Public Library roster, and a scholarly unit
  history confirm Lars N Rottinger and document his immediate path from
  Company B, 99th Infantry Battalion (Separate), to OSS. No civilian employer
  before Army service was inferred.
- Official Army history and a Foreign Service retrospective establish Leland
  L Rounds as the American Vice-Consul at Oran before Allied planning and
  liaison work. The assignment is a government relationship, not private
  employment, and its exact relation to OSS awaits Box 663.
- The National Gallery of Art documents Theodore D. Rousseau Jr. as Assistant
  Curator of Painting in 1940-1941 and identifies his later OSS Art Looting
  Investigation Unit work. A specialist biography places Naval Reserve attaché
  duties at Lisbon and Madrid before OSS, but the transfer remains qualified
  because no exact order was located.
- A Hoover Institution archival register identifies David N Rowe as David
  Nelson Rowe, a Princeton lecturer from 1938 to 1943 and an OSS Research and
  Analysis official in 1941-1942. Princeton is modeled as his last documented
  civilian employer; distinct 1941 Justice Department and Library of Congress
  research assignments are preserved separately.
- A reputable obituary identifies Captain Robert R Rovzar and sequences
  Georgetown student status, officer training, 82nd Airborne paratrooper
  service, and OSS service. The 82nd Airborne is published only as a probable
  immediate pathway because the exact transfer date is absent.
- A 1945 SSU document transcription supports a probable identity for Dorothy
  Rouden, and operational-group rosters support a probable identity for John
  Rovello. Neither source establishes pre-OSS employment.
- Official Army data confirms Marcello G Rotundo, Wesley J Rowan, Alvin T
  Rowe, and Harrison A Rowe for identity and Army-entry chronology only. No
  named employer was inferred from coded data.
- Army leads spelling the names George Reutsis, Oostas Routsis, Peter J
  Rovano, and Theodore J Roussos were rejected rather than silently replacing
  the printed index names. The candidate attached to John W Roward Jr. named
  Robert J King and was rejected as incompatible.
- The remaining unresolved profiles state that no reliable pre-OSS employer
  has yet been identified in the accessible sources reviewed and identify the
  indexed Box 663 or 664 personnel file as the next evidence target.

## Exact coverage after Batch 824

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,932/23,938 (49.8454%).
- Verified-employer coverage: 388/23,938 (1.6209%).
- Verified-affiliation coverage: 859/23,938 (3.5884%).
- Archival-review coverage: 10,396/23,938 (43.4289%).
- Not started: 12,001.
- Possible duplicate groups: 553; conflicts: 405.
- Claims: 1,537 confirmed; 3,693 high; 1,648 medium; 202 low; 348
  conflicting; two unresolved.
- Citations: 6,235 records representing 3,285 unique source documents.
- Total saved research attempts and plans: 23,426.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch824.csv`. Evidence,
identity claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page402-rottersmann-rowe-review_batch-824_2026-10-15.json`.

The identity-decision replay skipped all ten duplicate decisions on the second
import. Evidence replay retained exactly 23 Batch 824 attempts, nine
affiliations, 19 claims, 36 claim-source links, nine organizations, and 12
sources. SQLite reports no foreign-key violations.

## Local release verification

- Python: 145 tests passed.
- Astro: 458 source files checked with zero errors, warnings, or hints; 24,968
  static HTML pages built.
- Browser: 93/93 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 24 Batch 824 viewport checks.
- Links: all 24,968 generated HTML files passed internal-link checks; 51,149
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,040 built artifacts; aggregate and manifest false positives were zero.
- Manifest: 67 assets and 112,877,654 bytes verified in both public trees;
  manifest SHA-256
  `90d90d3370f681d5c7679b42cd520152788acbec6ca8d5e47b80aea965410baa`.
- Determinism: two consecutive production builds produced SHA-256
  `84769f92b4d02f2033cea91dc12a18e6e6b02d1992f8d69b8399dc273f4e7be2`
  across 25,040 files and 319,176,632 bytes.

Resume new-person research at PDF page 402, row 24. Full-index historical
research remains unfinished; 12,001 active people are still `not_started`.
