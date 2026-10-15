# Batch 820 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 820 covers PDF page 400, rows 1-23, Ronald E Rosen through Alvin
Rosenthal. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 400 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 400, row 24,
Franz W Rosenthal.

Printed names, initials, ranks or grades, blank cells, private identifiers, box
numbers, notes, and archival locations remain recoverable exactly as indexed.
The index spelling `Alfred Rosenhal` remains primary while `Alfred Rosenthal`
is preserved as an evidence-supported variant. The index spelling `Eliott H
Rosenblatt` likewise remains primary while the official Army record's `Eliot`
variant is visible. Full service identifiers remain private and are absent
from public outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks.
- The NARA Catalog adapter was used in dry-run mode because no API key was
  present in the process environment. The CIA adapter failed closed under its
  robots policy. The Library of Congress adapter recorded four no-results and
  one source error. Access failures were not treated as historical negative
  evidence.
- Four protected-identifier Army matches were accepted for identity only.
  Army occupation codes were not published as jobs or employers. Two corrupt
  or incompatible Army candidates were explicitly rejected.
- All 23 people now have saved, reviewable, terminal outcomes: three
  `completed` and 20 `requires_archival_review`.

## Historical outcomes

- USC and Princeton institutional memorials identify James N Rosenau as a
  University of Wisconsin undergraduate who was drafted into the Army and
  deployed to England as an OSS cryptographer. The university is modeled as
  student status, not employment, and the Army sequence is a military pathway.
- An official Army identifier plus independent Harvard and Smithsonian
  biographies confirm John M Rosenfield III, also documented as John Max
  Rosenfield. His University of Texas relationship is student status. His Army
  Military Intelligence assignment is published with a medium-confidence
  qualification because the exact timing relative to OSS remains unknown.
- A contemporary authorized account explicitly places Alfred Rosenthal in an
  unidentified Army reconnaissance battalion immediately before transfer to
  OSS training. A scholarly RG 226-based history independently corroborates
  the sergeant's Austrian Section and Operation Dania identity. The project
  preserves, rather than silently corrects, the index's `Rosenhal` spelling.
- A plausible Samuel Rosenberg obituary mentions OSS photo-analysis and
  prewar theater work, but the common index name lacks two corroborating
  identifiers. It remains a rejected lead pending Box 660 review.
- Common-name, incomplete-name, and postwar-only candidates that lacked the
  required identity and temporal bridges remain rejected leads. Their profiles
  direct researchers to the indexed personnel files instead of implying that
  no previous employment existed.

## Exact coverage after Batch 820

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,841/23,938 (49.4653%).
- Verified-employer coverage: 383/23,938 (1.6000%).
- Verified-affiliation coverage: 850/23,938 (3.5508%).
- Archival-review coverage: 10,305/23,938 (43.0487%).
- Not started: 12,092.
- Possible duplicate groups: 553; conflicts: 403.
- Claims: 1,514 confirmed; 3,673 high; 1,639 medium; 202 low; 347
  conflicting; two unresolved.
- Citations: 6,205 records representing 3,263 unique source documents.
- Total saved research attempts and plans: 23,142.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch820.csv`. Evidence,
affiliations, claims, person updates, rejection reasons, and terminal attempts
are stored in
`research/evidence-page400-rosen-rosenthal-review_batch-820_2026-10-15.json`.

The identity-decision replay skipped all six duplicate decisions on the second
import. Evidence replay retained exactly 23 Batch 820 attempts, five
affiliations, 11 claims, 24 claim-source links, four reused organizations, and
eight sources. SQLite reports no foreign-key violations.

## Local release verification

- Python: 145 tests passed.
- Astro: 454 source files checked with zero errors, warnings, or hints; 24,956
  static HTML pages built.
- Browser: 87/87 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 18 Batch 820 viewport checks.
- Links: all 24,956 generated HTML files passed internal-link checks; 51,121
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,028 built artifacts; aggregate and manifest false positives were zero.
- Manifest: 67 assets and 112,541,511 bytes verified in both public trees;
  manifest SHA-256
  `73f4445eb6787865760f17b5eee6a16da59d93747420e1e8c9e1a669ac15a6a7`.
- Determinism: two consecutive production builds produced SHA-256
  `9b736e30f235e10cb722b219327e5277205fcb04cd49b8e369addab058046400`
  across 25,028 files and 318,613,287 bytes.

Resume new-person research at PDF page 400, row 24. Full-index historical
research remains unfinished; 12,092 active people are still `not_started`.
