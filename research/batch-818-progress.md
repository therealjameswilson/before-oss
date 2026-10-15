# Batch 818 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 818 covers PDF page 399, rows 1-23, Howard E Roman through Archibald B
Roosevelt. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 399 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 399, row 24,
James F Roosevelt.

Printed names, initials, ranks or grades, blank cells, private identifiers, box
numbers, notes, and archival locations remain recoverable exactly as indexed.
The printed `2D LT` grade for Edwin P Romanoski is preserved verbatim and now
normalizes transparently to second lieutenant; the classification refresh
upgraded 35 source rows and 29 active entities without altering their raw
values. Full service numbers remain private and are absent from public outputs.

## Research protocol and review

- Every person received NARA index context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks.
- The NARA Catalog adapter was used in dry-run mode because no API key was
  present in the process environment. A bounded CIA Reading Room attempt
  encountered the adapter's robots-policy limitation. The Library of Congress
  adapter returned three valid no-result searches and then timed out. Access
  problems were not treated as historical negative evidence.
- Nine protected-identifier Army matches were accepted for identity only,
  including the indexed `Fedencio` / Army `FIDENCIO` variant. Three candidates
  were rejected as different people because their identifiers resolved to
  Harold Burdette, Roland J Rondeau, and Lewis B Whitley. Army occupation codes
  were not published as jobs or employers.
- All 23 people now have saved, reviewable, terminal outcomes: one newly
  `verified_employer_found`, one `occupation_only_found`, three
  `conflicting_sources`, 17 `requires_archival_review`, and the previously
  verified Archibald B Roosevelt profile, which was reaudited without being
  downgraded.

## Historical outcomes

- Cornell's Kheel Center finding aid, OCLC ArchiveGrid, a scholarly article,
  and NARA Entry 210 records identify Serafino Romualdi at high identity
  confidence and preserve the chronology rather than collapsing it into one
  employer field. The Office of the Coordinator of Inter-American Affairs,
  Labor Division, is the best-supported immediate pre-OSS government
  assignment; the International Ladies' Garment Workers' Union is the
  best-supported last civilian employer before his intervening wartime roles.
  Earlier work for the Italian Labor Publishing Company and `Il Mundo`, plus a
  1941 Free Italy Committee affiliation, remain separately modeled and cited.
- A contemporary September 6, 1946 newspaper column identifies Kenneth Romney
  Jr. through his father, OSS service, China duty, and return to radio work. The
  word `again` supports a pre-service radio occupation, but the article does
  not name the pre-service employer. The profile therefore publishes an
  occupation-only result and does not infer the American Broadcasting Company
  from postwar context.
- The three mismatching Army candidates remain visible public conflicts and do
  not transfer occupations, identifiers, or identities to the indexed people.
- Existing evidence for Archibald B Roosevelt remains intact. The indexed
  nephew is not conflated with Archibald Roosevelt Sr. or assigned the elder
  man's oil and investment-banking career.

## Exact coverage after Batch 818

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,796/23,938 (49.2773%).
- Verified-employer coverage: 380/23,938 (1.5874%).
- Verified-affiliation coverage: 842/23,938 (3.5174%).
- Archival-review coverage: 10,260/23,938 (42.8607%).
- Not started: 12,137.
- Possible duplicate groups: 553; conflicts: 403.
- Claims: 1,502 confirmed; 3,658 high; 1,637 medium; 202 low; 347
  conflicting; two unresolved.
- Citations: 6,187 records representing 3,247 unique source documents.
- Total saved research attempts and plans: 23,020.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch818.csv`. Evidence,
affiliations, claims, person updates, rejection reasons, and terminal attempts
are stored in
`research/evidence-page399-roman-roosevelt-review_batch-818_2026-10-15.json`.

The identity-decision replay skipped all 12 duplicate decisions. Evidence
replay retained exactly 23 Batch 818 attempts, five affiliations, 19 claims,
38 claim-source links, five organizations, and seven sources. SQLite reports
no foreign-key violations.

## Local release verification

- Python: 144 tests passed.
- Astro: 452 source files checked with zero errors, warnings, or hints; 24,947
  static HTML pages built.
- Browser: 84/84 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 15 Batch 818 viewport checks.
- Links: all 24,947 generated HTML files passed internal-link checks; 51,103
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,019 public artifacts; aggregate and manifest false positives were zero.
- Manifest: 67 assets and 112,308,431 bytes verified in both public trees;
  manifest SHA-256
  `41954d2bfa4589414f8899b4cbb4131ed13bbfffc7f238b7977ae2d7859dde8c`.
- Determinism: two consecutive production builds produced SHA-256
  `ba50cee0d9223ef04a285eb7b8b637acc01828b4e4ed0be95e3042fd0d79dce2`
  across 25,019 files and 318,227,927 bytes.

Resume new-person research at PDF page 399, row 24, James F Roosevelt.
Full-index historical research remains unfinished; 12,137 active people are
still `not_started`.
