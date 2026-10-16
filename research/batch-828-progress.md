# Batch 828 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 828 covers PDF page 404, rows 1-23, Arthur A Ruozzi through John P
Russell. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 404 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 404, row 24,
John S Russell.

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
- Five exact protected-identifier Army matches were accepted for identity
  only. Army occupation codes were not published as jobs or employers. Three
  incompatible Army names were explicitly rejected and remain visible as
  conflicts.
- Civilian employment, wartime military assignment, occupation-only evidence,
  and unresolved archival leads remain separate concepts. Crowell-Collier is
  not conflated with Louis Ruppel's later Marine Corps service, and a tree
  topper occupation is not converted into a named employer.
- All 23 people now have saved, reviewable, terminal outcomes. Cases without
  adequate online evidence identify the relevant Box 666, 667, or 668
  personnel file as the next evidence target.

## Historical outcomes

- Two contemporary *Broadcasting* notices establish Louis Ruppel as executive
  assistant to the president and publisher of Crowell-Collier Publishing
  Company beginning in October 1942 and document his departure for the Marine
  Corps in January 1943. Crowell-Collier is published as his last civilian
  employer; Marine Corps service is modeled separately as a qualified probable
  immediate wartime affiliation. His indexed first-lieutenant row is therefore
  reviewed as a commissioned Marine Corps officer rather than a generic Army
  officer.
- An official OSS record names Major Robert F. Rushin as head of the X-2
  Insurance Unit. A *Los Angeles Times* archival report independently identifies
  him as a Home Insurance Company executive recruited into OSS. Home Insurance
  Company is published as his high-confidence, probable-immediate civilian
  employer.
- The official OSS Unit Rype record, protected Army identifier, and a scholarly
  unit history identify Tom Rusdal with the Tosten and Torsten Rusdal name
  variants. The scholarly source documents a prewar tree-topper occupation but
  does not name an employer, so the result remains occupation-only.
- Official Army data confirms Arthur A. Ruozzi, Lawrence V. Ruppel, Andrew L.
  Ruscio, Tom Rusdal, and Arthur J. Russ Jr. for identity and Army-entry
  chronology only. No coded occupation was converted into a public job or
  employer claim.
- Protected-identifier candidates for Horace E. Rupert Jr., Donald E. Russell,
  and Donald W. Russell were rejected because the Army records respectively
  name Oliver J. Headings, Charles C. Smith, and Donald N. Russell. The
  discrepancies remain visible for archival review.

## Exact coverage after Batch 828

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,024/23,938 (50.2298%).
- Verified-employer coverage: 392/23,938 (1.6376%).
- Verified-affiliation coverage: 868/23,938 (3.6260%).
- Archival-review coverage: 10,488/23,938 (43.8132%).
- Not started: 11,909.
- Possible duplicate groups: 553; conflicts: 415.
- Claims: 1,553 confirmed; 3,714 high; 1,652 medium; 202 low; 358
  conflicting; two unresolved.
- Citations: 6,264 records representing 3,307 unique source documents.
- Total saved research attempts and plans: 23,733.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch828.csv`. Evidence,
identity claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page404-ruozzi-russell-review_batch-828_2026-10-15.json`.

The identity-decision replay skipped all eight duplicate decisions on the
second import. Evidence replay retained exactly 23 Batch 828 attempts, four
affiliations, 15 claims, 33 claim-source links, three organizations, and seven
sources. SQLite reports no foreign-key violations.

## Local release verification

- Python: 145 tests passed.
- Astro: 462 source files checked with zero errors, warnings, or hints; 24,978
  static HTML pages built.
- Browser: 87/87 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 18 Batch 828 checks.
- Links: all 24,978 generated HTML files passed internal-link checks; 51,176
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,050 built artifacts; aggregate and manifest-size false positives were
  both zero.
- Manifest: 67 assets and 113,230,500 bytes verified in the public tree;
  manifest SHA-256
  `0d2ed51ed87332d3dc01f9a966a45bd19689962e4456112d318831e66bfaedb7`.
- Determinism: two consecutive production builds produced SHA-256
  `53885133bbd50ad295aec0754849b1d004f532a10033343aab917bc6d519f79b`
  across 25,050 files and 319,753,098 bytes.

Resume new-person research at PDF page 404, row 24. Full-index historical
research remains unfinished; 11,909 active people are still `not_started`.
