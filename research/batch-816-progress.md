# Batch 816 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 816 covers PDF page 398, rows 1-23, Camden L Rogers through William G
Rogers. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 398 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 398, row 24,
Howard B Rogers, Jr.

Printed name order, initials, ranks, blank rank fields, and box numbers remain
exact. In particular, row 6 retains the printed first-name field `George Jr.`,
middle initial `A`, and rank `S SGT`. Rows 15 and 16 remain separate Martin R
Rogers people: one indexed as `P-5`, the other as `2D LT`. Full service
numbers remain private and are absent from public outputs.

## Research protocol and review

- Every person received NARA index context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks.
- The NARA Catalog adapter was used in dry-run mode because no API key was
  present in the process environment. A bounded CIA Reading Room adapter
  attempt encountered the adapter's robots-policy limitation, and the Library
  of Congress adapter timed out. Neither access problem was treated as
  historical negative evidence. Targeted manual CIA searches were completed
  for all 23 names.
- Protected-identifier Army matches for John R Rogers, John Albert A Rogers,
  Preston Rogers, and William G Rogers were accepted for identity only. Army
  occupation codes were not published as jobs or employers.
- The Army candidates for George A Rogers Jr. and Robert M Rogers carry the
  indexed protected identifiers but name different people. Both candidates
  were rejected rather than merged, and the conflicts remain public and
  reviewable.
- All 23 people now have saved, reviewable, terminal Batch 816 outcomes.

## Historical outcomes

- Four official Army identifier matches establish confirmed identities but do
  not establish civilian employers. Each profile therefore points to Box 656
  for employment and Army-to-OSS chronology.
- The George A Rogers Jr. identifier maps to an Army record naming Harry
  Koretsky; the Robert M Rogers identifier maps to a record naming Rutin M
  Rojas. The project preserves these as conflicts and makes no person merge.
- An American Film Institute record identifies a Stanwood Rogers as an MGM
  production designer or art director. The uncommon name is a useful lead, but
  the record lacks the middle initial, private identifier, military chronology,
  or direct OSS bridge required to assign it to Stanwood N Rogers.
- A Cornell alumni lead identifies a William W Rogers as a Rochester technical
  school instructor and engineering-textbook coauthor. It lacks the indexed
  identifier, OSS link, military chronology, or Box 656 bridge and therefore
  remains private and unassigned.
- Famous or common-name results for Carl Ransom Rogers, Fred McFeely Rogers,
  Joanne Rogers, Harold Rogers, and James G Rogers Jr. were rejected when the
  source did not establish the indexed person.

## Exact coverage after Batch 816

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,751/23,938 (49.0893%).
- Verified-employer coverage: 377/23,938 (1.5749%).
- Verified-affiliation coverage: 839/23,938 (3.5049%).
- Archival-review coverage: 10,215/23,938 (42.6727%).
- Not started: 12,182.
- Possible duplicate groups: 553; conflicts: 400.
- Claims: 1,482 confirmed; 3,644 high; 1,637 medium; 202 low; 344
  conflicting; two unresolved.
- Citations: 6,174 records representing 3,236 unique source documents.
- Total saved research attempts and plans: 22,921.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch816.csv`. Evidence, claims,
person updates, rejection reasons, and terminal attempts are stored in
`research/evidence-page398-rogers-review_batch-816_2026-10-15.json`.

The identity-decision import replay skipped all six duplicate decisions. The
evidence import retained exactly 23 Batch 816 attempts, six claims, and 12
claim-source links. SQLite reports no foreign-key violations.

## Local release verification

- Python: 143 tests and 81 subtests passed.
- Astro: 450 source files checked with zero errors, warnings, or hints; 24,939
  static HTML pages built.
- Browser: 87/87 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 18 Batch 816 viewport checks.
- Links: all 24,939 generated HTML files passed internal-link checks; 51,088
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across 70
  public artifacts; aggregate and manifest false positives were also zero.
- Manifest: 67 assets and 112,085,107 bytes verified; manifest SHA-256
  `72aa9382b12a520900520e3809e7e06915052c938beb78018f31556e6ab46fa3`.
- Determinism: two consecutive production builds produced SHA-256
  `f4e9a9f27f8122b18c5db2088d8d9406d90706b372b47873c15cf5fae402d372`
  across 25,011 files and 317,850,806 bytes.

Resume new-person research at PDF page 398, row 24, Howard B Rogers, Jr. Full-
index historical research remains unfinished; 12,182 active people are still
`not_started`.
