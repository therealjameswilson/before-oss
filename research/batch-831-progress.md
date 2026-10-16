# Batch 831 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 831 covers PDF page 405, rows 24-46, Joseph M F Ryan Jr through Gerald V
Sabatino. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 405 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 406, row 1,
Harriet W Sabine.

Printed names, initials, ranks or grades, blank cells, private identifiers, box
numbers, notes, and archival locations remain recoverable exactly as indexed.
Full service identifiers remain private and are absent from public outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks. NARA Catalog queries remained in dry-run mode.
- Five exact protected-identifier Army matches were accepted for identity and
  Army chronology only: William C Ryan, William H Ryan, Albert P Ryavec,
  William L Rye, and Jacques Sabathe. No coded Army occupation was converted
  into an employer or occupation claim.
- Three incompatible Army-name candidates were rejected and preserved as
  conflicts: William P Ryan, Robert L Rybovich, and John Rydgis. The rejected
  names do not appear as affiliations.
- Identity resolution for the batch ends with five confirmed people, two
  high-confidence people, two ambiguous people, three conflicting people, and
  11 unresolved people. The research statuses are five
  `requires_archival_review` confirmed identities, one high-confidence
  `requires_archival_review`, one `verified_employer_found`, two
  `needs_identity_review`, three `conflicting_sources`, and 11 unresolved
  `requires_archival_review` cases.

## Historical outcomes

- The Washington Post obituary for Joseph Michael Francis Ryan Jr explicitly
  places him in the United States Army Air Forces and says he was detailed to
  the OSS. The Army Air Forces is therefore published as his immediate pre-OSS
  military assignment with high identity and claim confidence. His UCLA
  physics and meteorology certificate is education, not an inferred employer.
- An official CIA history of Eero Saarinen says he was recruited to the OSS,
  worked there until 1944, and had joined his father at Cranbrook before OSS.
  The Cranbrook Archives finding aid dates the formation of Saarinen and
  Swanson to 1939. Together with the exceptionally rare near-match, these
  sources support the indexed Egro Saarinew as Eero Saarinen at high confidence.
  Saarinen and Swanson is published as the strongly date-bounded pre-OSS
  enterprise; Cranbrook Academy of Art is retained separately as an earlier
  professional affiliation. Box 671 remains the archival target for direct
  confirmation of the printed-name corruption.
- National Park Service and Aspen historical evidence identifies a Ted Ryan
  who left Aspen for OSS and supplies a strong employer lead. The index,
  however, contains adjacent Theodore Ryan and Theodore S Ryan rows in Boxes
  669 and 670. Neither source supplies the middle name or box needed to select
  one row. Both profiles therefore remain ambiguous, are grouped for review,
  and publish no employer from that biography. The candidate is preserved only
  in the private research evidence for archival follow-up.
- The other 11 people received documented negative-result protocols and
  explicit archival next actions. Those outcomes state that no reliable
  pre-OSS employer has yet been identified in accessible sources; they do not
  claim that the person had no prior employer.

## Exact coverage after Batch 831

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,093/23,938 (50.5180%).
- Verified-employer coverage: 395/23,938 (1.6501%).
- Verified-affiliation coverage: 874/23,938 (3.6511%).
- Archival-review coverage: 10,557/23,938 (44.1014%).
- Not started: 11,840.
- Possible duplicate groups: 554; conflicts: 420.
- Claims: 1,568 confirmed; 3,732 high; 1,653 medium; 202 low; 363
  conflicting; two unresolved.
- Citations: 6,282 records representing 3,321 unique source documents.
- Total saved research attempts and plans: 23,966.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch831.csv`. Evidence,
identity claims, person updates, rejection reasons, and research attempts are
stored in
`research/evidence-page405-ryan-sabatino-review_batch-831_2026-10-15.json`.

The identity-decision replay skipped all eight duplicate decisions on the
second import. Evidence replay retained exactly 23 Batch 831 attempts, three
affiliations, 14 claims, three organizations, and seven sources. SQLite reports
no foreign-key violations.

## Local release verification

Local release verification passed:

- 145/145 Python tests and 81 subtests passed.
- Astro reported zero errors, warnings, or hints and built 24,984 pages.
- 87/87 bounded Playwright release tests passed across Batch 831, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- All internal links across 24,984 HTML files resolved; 51,191 unique external
  URLs were inventoried for separate review.
- Public-identifier redaction found zero unexpected boundary matches,
  aggregate false positives, or manifest-size false positives.
- The public manifest contains 67 assets totaling 113,498,804 bytes, with
  SHA-256 `15a5ac35bf6cc5d9081d3b06c46ab3fcba3737d2194aeb3c7496139aca4013b2`.
- Two clean production builds produced the same 25,056-file tree hash,
  `d374769677336c25740eb632dd045647351b530477f67dcf7f0e4ebb19c4f53d`.

GitHub Pages run 38840399804 published commit
`17d2b6286c42203c30af14693f2972e70a52c69a` successfully. The immutable live
verifier matched all 67 public assets (113,498,804 bytes), the release manifest,
eight core routes, 34 source-register pages, and all 23 Batch 831 profile URLs
without authentication.

Resume new-person research at PDF page 406, row 1. Full-index historical
research remains unfinished; 11,840 active people are still `not_started`.
