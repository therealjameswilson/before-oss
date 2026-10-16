# Batch 827 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 827 covers PDF page 403, rows 24-46, Ferdinand M Ruff through Dorothy
E Runyon. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 403 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 404, row 1,
Arthur A Ruozzi.

Printed names, initials, ranks or grades, blank cells, private identifiers,
box numbers, notes, and archival locations remain recoverable exactly as
indexed. Full service identifiers remain private and are absent from public
outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks.
- The NARA Catalog and web adapters each recorded 23 deterministic dry-run
  queries. Bounded CIA and Library of Congress requests recorded access errors;
  neither failure was treated as historical negative evidence.
- Three exact protected-identifier Army matches were accepted for identity
  only. Army occupation codes were not published as jobs or employers. Three
  incompatible Army names were explicitly rejected and remain visible as
  conflicts.
- Immediate military assignment, immediate student status, earlier student
  affiliation, occupation-only evidence, and civilian employment remain
  separate concepts. Harvard and the Sorbonne are not presented as employers,
  and Runkle's Army path is not presented as civilian employment.
- All 23 people now have saved, reviewable, terminal outcomes. Cases without
  adequate online evidence identify the indexed Box 666 personnel file as the
  next evidence target.

## Historical outcomes

- Two Yale institutional sources identify Richard Francis Ruggles and place
  his Harvard economics degrees through 1942 immediately before his OSS work
  analyzing German production. Harvard is published as an immediate student
  affiliation, not an employer.
- Dartmouth's institutional memorial identifies Scott Frederick Runkle and
  establishes a strongly date-bounded pathway from General Omar Bradley's
  Army staff and French Resistance responsibilities to later OSS operations
  in Germany. His earlier Sorbonne study is separately classified as student
  status.
- A contemporary April 1942 Russian Review citation and a corroborative
  Arlington transcription support a qualified probable identity for Melville
  J. Ruggles. The profile publishes occupation-related scholarly authorship
  only; neither an employer nor immediate OSS chronology is asserted.
- Official Army data confirms George P. Ruff, Vito V. Ruggiero, and Donald L.
  Rundquist for identity and Army-entry chronology only. No coded occupation
  was converted into a public job or employer claim.
- Protected-identifier candidates for Ferdinand M. Ruff, John F. Ruhat, and
  Stefan J. Rundt were rejected because the Army file respectively names
  Ferdinand H. Ruff, John F. Rukat, and John E. Powers. The discrepancies
  remain visible for Box 666 review.

## Exact coverage after Batch 827

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,001/23,938 (50.1337%).
- Verified-employer coverage: 390/23,938 (1.6292%).
- Verified-affiliation coverage: 865/23,938 (3.6135%).
- Archival-review coverage: 10,465/23,938 (43.7171%).
- Not started: 11,932.
- Possible duplicate groups: 553; conflicts: 412.
- Claims: 1,547 confirmed; 3,709 high; 1,651 medium; 202 low; 355
  conflicting; two unresolved.
- Citations: 6,257 records representing 3,302 unique source documents.
- Total saved research attempts and plans: 23,662.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch827.csv`. Evidence,
identity claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page403-ruff-runyon-review_batch-827_2026-10-15.json`.

The identity-decision replay skipped all six duplicate decisions on the second
import. Evidence replay retained exactly 23 Batch 827 attempts, three
affiliations, 13 claims, 25 claim-source links, three organizations, and seven
sources. SQLite reports no foreign-key violations.

## Local release verification

- Python: 145 tests passed.
- Astro: 461 source files checked with zero errors, warnings, or hints; 24,976
  static HTML pages built.
- Browser: 87/87 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 18 Batch 827 checks.
- Links: all 24,976 generated HTML files passed internal-link checks; 51,171
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,048 built artifacts; aggregate false positives were zero and two allowed
  manifest-size coincidences were recorded.
- Manifest: 67 assets and 113,125,008 bytes verified in the built public tree;
  manifest SHA-256
  `2978c48646d32340ef0e7502a43a64f681895698a2797c9600691f6f5d63cad7`.
- Determinism: two consecutive production builds produced SHA-256
  `84a22b8da76762a3a1a86e8e6e76265ee74dd54d1962df5ba8ceb346fb24c594`
  across 25,048 files and 319,585,341 bytes.
- The release runner now assigns a distinct loopback port to each Playwright
  invocation, eliminating a teardown race that could reuse a dying server.

Resume new-person research at PDF page 404, row 1. Full-index historical
research remains unfinished; 11,932 active people are still `not_started`.
