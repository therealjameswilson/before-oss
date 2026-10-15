# Batch 817 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 817 covers PDF page 398, rows 24-46, Howard B Rogers Jr. through Albert
G Roloff. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 398 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 399, row 1,
Howard E Roman.

Printed names, initials, ranks or grades, blank cells, private identifiers, box
numbers, and archival locations remain recoverable exactly as indexed. The
source record for Charlene Roland was rechecked and retains the printed `P-3`
grade. Full service numbers remain private and are absent from public outputs.

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
- Twelve protected-identifier Army matches were accepted for identity only.
  The 1946 entries for Karl Rohe and Thomas A Rollo are explicitly post-OSS and
  are not used to infer pre-OSS chronology. Army occupation codes were not
  published as jobs or employers.
- All 23 people now have saved, reviewable, terminal Batch 817 outcomes: one
  `verified_employer_found`, one `documented_prewar_employer_found`, and 21
  `requires_archival_review`.

## Historical outcomes

- The Norwegian War Sailor Register documents Sverre B Rogne, also rendered
  Rockne, as a Norwegian merchant seaman aboard M/S Pleasantville from May 28
  through June 8, 1942. The Denver Public Library's 10th Mountain Division
  index independently lists the exact uncommon name in Company C, 99th
  Infantry Battalion (Separate). The vessel work is published as his latest
  documented civilian work before Army service, not as a proven immediate
  pre-OSS affiliation. The 99th Infantry is separately modeled as a military
  assignment.
- Contemporary 1942 and 1944 scholarly records identify George F Rohrlich as
  formerly affiliated with the Brookings Institution and then employed as an
  instructor in Sweet Briar College's Division of Social Studies. Brookings is
  modeled as a professional affiliation because the source says only
  `formerly of`; Sweet Briar is documented employment. Neither is claimed as
  the immediate predecessor to OSS because the transfer chronology remains
  unknown.
- Twelve official Army identifier matches establish confirmed identities but
  not civilian employers. Those profiles remain routed to Boxes 656-657 for
  employment and transfer chronology.
- A Bellingham blacksmith lead for Harry L Rohlfing and a Texas biographical
  lead for Mary O Rolater were rejected because they lacked a protected
  identifier, direct OSS bridge, and relevant employment chronology.

## Exact coverage after Batch 817

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,774/23,938 (49.1854%).
- Verified-employer coverage: 379/23,938 (1.5833%).
- Verified-affiliation coverage: 841/23,938 (3.5132%).
- Archival-review coverage: 10,238/23,938 (42.7688%).
- Not started: 12,159.
- Possible duplicate groups: 553; conflicts: 400.
- Claims: 1,494 confirmed; 3,650 high; 1,637 medium; 202 low; 344
  conflicting; two unresolved.
- Citations: 6,180 records representing 3,241 unique source documents.
- Total saved research attempts and plans: 22,969.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch817.csv`. Evidence,
affiliations, claims, person updates, rejection reasons, and terminal attempts
are stored in
`research/evidence-page398-rogers-roloff-review_batch-817_2026-10-15.json`.

The identity-decision replay skipped all 12 duplicate decisions. Evidence
replay retained exactly 23 Batch 817 attempts, four affiliations, 18 claims,
and 35 claim-source links. SQLite reports no foreign-key violations.

## Local release verification

- Python: 143 tests passed.
- Astro: 451 source files checked with zero errors, warnings, or hints; 24,942
  static HTML pages built.
- Browser: 84/84 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 15 Batch 817 viewport checks.
- Links: all 24,942 generated HTML files passed internal-link checks; 51,094
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,014 public artifacts; aggregate and manifest false positives were zero.
- Manifest: 67 assets and 112,187,101 bytes verified; manifest SHA-256
  `5728199e6431174b9fbce09fce594d38728d34b0140939dae6f08a4e656075f2`.
- Determinism: two consecutive production builds produced SHA-256
  `798a1ec5d68e3e9146c111219539db7263204d547a4a1b0218fe5e6c25e89b50`
  across 25,014 files and 318,020,860 bytes.

Resume new-person research at PDF page 399, row 1, Howard E Roman. Full-index
historical research remains unfinished; 12,159 active people are still
`not_started`.
