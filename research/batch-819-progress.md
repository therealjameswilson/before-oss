# Batch 819 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 819 covers PDF page 399, rows 24-46, James F Roosevelt through David V
Rosen. All 23 printed rows remain preserved as immutable source records and map
to 23 active person entities. Page 399 was inspected against a 300 dpi render
before research. The next unresearched boundary is PDF page 400, row 1.

Printed names, initials, ranks or grades, blank cells, private identifiers, box
numbers, notes, and archival locations remain recoverable exactly as indexed.
The printed `1/SGT` grade for George F Rose is preserved verbatim and now
normalizes transparently to first sergeant. The classification refresh upgraded
five source rows and five active entities, including two `1/SGT` and three
`1/Sgt.` variants, without altering raw values. Full service identifiers remain
private and are absent from public outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks.
- The NARA Catalog adapter was used in dry-run mode because no API key was
  present in the process environment. Existing official NARA, CIA, Library of
  Congress, Marine Corps, Cornell, Hoover, and Army records were reviewed
  directly. Source-access problems were not treated as historical negative
  evidence.
- Three protected-identifier Army matches were accepted for identity only.
  Army occupation codes were not published as jobs or employers. Mack A Roper's
  exact London OSS roster entry also supports identity only.
- All 23 people now have saved, reviewable, terminal outcomes: three
  `verified_employer_found`, two `completed`, one previously
  `documented_prewar_employer_found`, and 17 `requires_archival_review`.

## Historical outcomes

- The official CIA war report and Marine Corps chronology establish James F
  Roosevelt's extended active Marine duty and explicit temporary detachment
  into the Coordinator of Information in August 1941. This is modeled as an
  immediate military assignment, not civilian employment. A Marine Corps
  historical monograph separately identifies him as vice president of Samuel
  Goldwyn's production company before mobilization, making Samuel Goldwyn,
  Inc. the best-supported last named civilian employer.
- The Library of Congress identifies Quentin Roosevelt as a Harvard graduate
  who entered the Army in 1941, while NARA Entry 210 identifies him as Chief,
  SI, Chungking, China, during 1944-1945. Harvard is modeled as student status,
  and the Army service is preserved without claiming an exact transfer sequence
  that the accessible records do not establish.
- Cornell's Roper Center documents Elmo Roper at the Traub Company, as a
  co-founder of Cherington, Wood, and Roper in 1933, and operating his own
  polling organization by 1940 before Donovan recruited him during the war.
  The immediate company is published at medium confidence because the source
  does not fix the exact 1941 legal style; the earlier firms are high-confidence
  documented prewar employment.
- Direct Goodfellow Board interviews at OSS Headquarters in Cairo establish
  Krisanthe Rose's immediate pre-OSS government assignment with War Department
  Ordnance in Detroit and Telphi Rose's immediate prior finance work at the
  Gotham Hotel in New York. The transcript's `Telpi Rose` spelling remains a
  documented variant rather than a silent correction.
- Common-name, incomplete-name, and postwar-only candidates that lacked the
  required identity and temporal bridges remain rejected leads. Their profiles
  direct researchers to the indexed personnel files instead of implying that
  no previous employment existed.

## Exact coverage after Batch 819

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,818/23,938 (49.3692%).
- Verified-employer coverage: 383/23,938 (1.6000%).
- Verified-affiliation coverage: 847/23,938 (3.5383%).
- Archival-review coverage: 10,282/23,938 (42.9526%).
- Not started: 12,115.
- Possible duplicate groups: 553; conflicts: 403.
- Claims: 1,510 confirmed; 3,667 high; 1,638 medium; 202 low; 347
  conflicting; two unresolved.
- Citations: 6,197 records representing 3,256 unique source documents.
- Total saved research attempts and plans: 23,067.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch819.csv`. Evidence,
affiliations, claims, person updates, rejection reasons, and terminal attempts
are stored in
`research/evidence-page399-roosevelt-rosen-review_batch-819_2026-10-15.json`.

The identity-decision replay skipped all three duplicate decisions on the
second import. Evidence replay retained exactly 23 Batch 819 attempts, nine
affiliations, 18 claims, 32 claim-source links, nine organizations, and ten
sources. SQLite reports no foreign-key violations.

## Local release verification

- Python: 145 tests passed.
- Astro: 453 source files checked with zero errors, warnings, or hints; 24,956
  static HTML pages built.
- Browser: 87/87 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 18 Batch 819 viewport checks.
- Links: all 24,956 generated HTML files passed internal-link checks; 51,116
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,028 public artifacts; aggregate and manifest false positives were zero.
- Manifest: 67 assets and 112,452,219 bytes verified in both public trees;
  manifest SHA-256
  `117ab12e0a6a4c4af68ccb9c09d69fde2f269352a1754910b289044e25637b7d`.
- Determinism: two consecutive production builds produced SHA-256
  `a55d7d6675db350b1497e4e62a9aa75efed6b1db4942dd084a333897aeaf9f11`
  across 25,028 files and 318,480,123 bytes.

Resume new-person research at PDF page 400, row 1. Full-index historical
research remains unfinished; 12,115 active people are still `not_started`.
