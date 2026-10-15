# Batch 826 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 826 covers PDF page 403, rows 1-23, Howard L Ruble through David F
Ruf. All 23 printed rows remain preserved as immutable source records and map
to 23 active person entities. Page 403 was inspected against a 300 dpi render
before research. The next unresearched boundary is PDF page 403, row 24,
Ferdinand M Ruff.

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
  queries. A CIA robots-policy failure and a transient Library of Congress
  request error were recorded but were not treated as historical negative
  evidence.
- Four exact protected-identifier Army matches were accepted for identity
  only. Army occupation codes were not published as jobs or employers. One
  duplicate-person candidate was explicitly rejected and remains visible as a
  conflict.
- Immediate military assignments, last civilian employers, and earlier
  documented pre-OSS roles were modeled separately. The database does not
  turn an Army assignment into civilian employment or a 1941 job into an
  unsupported immediate-predecessor claim.
- All 23 people now have saved, reviewable, terminal outcomes. Cases without
  adequate online evidence identify the indexed Box 665 or 666 personnel file
  as the next evidence target.

## Historical outcomes

- National Park Service history identifies Lucius O. Rucker Jr. as a career
  Army officer and paratrooper who brought Fort Benning personnel to establish
  the OSS parachute school in June 1942. The broad U.S. Army assignment is
  published as the strongly date-bounded immediate affiliation; the exact
  prior unit remains unknown.
- An official CIA history confirms Merritt K. Ruddock's OSS identity. A
  contemporary December 1941 broadcasting notice documents him as a newsman
  at WRNL in Richmond and as a Mutual Broadcasting System news analyst. Both
  jobs are earlier documented pre-OSS employment, not asserted to be the
  immediate predecessor.
- Jack Marlin Rudolph's obituary explicitly links the indexed Major to Army
  officer and OSS service and documents Kimberly-Clark Corporation as his last
  civilian employer before wartime service. No prewar job title was inferred.
- A CIA note and a contemporary Seventh Army general order establish a
  high-confidence wartime identity for Gilbert J. Ruest. The Seventh Army
  headquarters assignment remains identity context because its temporal
  relation to OSS is uncertain.
- A cataloged 1941 Albert Einstein letter supplies a qualified probable
  identity lead for Eryl Joyce Rudlin and documents refugee-assistance
  activity. It does not establish an employer, a formal organization, or the
  link to Box 665; the profile remains qualified and archival-review dependent.
- Official Army data confirms Theobald J. Ruby, Joseph Rudas, Carl E. Ruder,
  and Fritz Ruesch for identity and Army-entry chronology only. No coded
  occupation was converted into a public job or employer claim.
- The protected identifier attached to John B. Rudd also appears for John B.
  Rodd in Box 653. The candidate was rejected rather than silently merged, and
  both files must be compared.

## Exact coverage after Batch 826

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,978/23,938 (50.0376%).
- Verified-employer coverage: 390/23,938 (1.6292%).
- Verified-affiliation coverage: 863/23,938 (3.6051%).
- Archival-review coverage: 10,442/23,938 (43.6210%).
- Not started: 11,955.
- Possible duplicate groups: 553; conflicts: 409.
- Claims: 1,544 confirmed; 3,704 high; 1,649 medium; 202 low; 352
  conflicting; two unresolved.
- Citations: 6,250 records representing 3,296 unique source documents.
- Total saved research attempts and plans: 23,591.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch826.csv`. Evidence,
identity claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page403-ruble-ruf-review_batch-826_2026-10-15.json`.

The identity-decision replay skipped all five duplicate decisions on the
second import. Evidence replay retained exactly 23 Batch 826 attempts, four
affiliations, 14 claims, 29 claim-source links, four organizations, and nine
sources. SQLite reports no foreign-key violations.

## Local release verification

- Python: 145 tests passed.
- Astro: 460 source files checked with zero errors, warnings, or hints; 24,973
  static HTML pages built.
- Browser: 90/90 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 21 Batch 826 checks.
- Links: all 24,973 generated HTML files passed internal-link checks; 51,163
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,045 built artifacts; aggregate and manifest false positives were zero.
- Manifest: 67 assets and 113,043,771 bytes verified in the built public tree;
  manifest SHA-256
  `4094eabf818d785b086e655ff8769c89c981f4a6e753ee70f16ebd16d3206237`.
- Determinism: two consecutive production builds produced SHA-256
  `42f1c7333d40faeefda24b7d499a3ed1dee9728e10e3fe295834ef466bd8b01a`
  across 25,045 files and 319,448,863 bytes.

Resume new-person research at PDF page 403, row 24. Full-index historical
research remains unfinished; 11,955 active people are still `not_started`.
