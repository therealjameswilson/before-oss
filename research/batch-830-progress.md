# Batch 830 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 830 covers PDF page 405, rows 1-23, William J Rust through Joseph A
Ryan. All 23 printed rows remain preserved as immutable source records and map
to 23 active person entities. Page 405 was inspected against a 300 dpi render
before research. The next unresearched boundary is PDF page 405, row 24, Joseph
M F Ryan Jr.

Printed names, initials, ranks or grades, blank cells, private identifiers, box
numbers, notes, and archival locations remain recoverable exactly as indexed.
Full service identifiers remain private and are absent from public outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks.
- NARA work remained in dry-run mode. A bounded CIA query for Ellis W Ryan
  failed closed because the searched path was disallowed by the site's robots
  policy. A Library of Congress query for Louis Ruzich returned no candidate;
  an earlier Ellis Ryan query timed out. None of these access outcomes was
  treated as proof that historical evidence does not exist.
- Four exact protected-identifier Army matches were accepted for identity
  only. Louis Ruzich's Army match was accepted at high confidence, rather than
  confirmed, because the Army source spells his first name Louie; two
  independent accounts corroborate the indexed identity and OSS Detachment
  101 service. No coded Army occupation was published as a job or employer.
- Identity resolution for the batch ends with four confirmed people, three
  high-confidence people, and 16 unresolved people. All 23 people have saved,
  reviewable, terminal research outcomes. Cases without adequate online
  evidence identify the indexed archival box as the next evidence target.

## Historical outcomes

- A Phi Kappa Psi biographical article identifies Ellis W Ryan as an Army Air
  Corps lieutenant at Randolph Field immediately before his OSS selection.
  The same source identifies the Toledo Ice House, which he built just before
  the war, as his last civilian work before military service. The W. F. Ryan
  Company insurance business and his Cleveland Arena directorship are retained
  separately as earlier documented pre-OSS affiliations.
- Two independent family and local-history accounts identify Louis Ruzich,
  including the Louie spelling variant, with OSS Detachment 101 in Burma. One
  account places him in the Army Corps of Engineers before parachute training
  and OSS service. That evidence is published as a qualified prior military
  assignment, not as a civilian employer; no family-farm employment is
  inferred.
- An official Marine Corps bibliography names Capt. Winthrop Rutherford among
  Marine officers who served with the OSS. This supports his high-confidence
  identity and commissioned Marine classification, but does not supply a
  pre-OSS employer. John P Rutherford's printed `LT NR` is transparently
  classified as a commissioned naval officer.
- Protected-identifier Army records confirm William J Rust, David Rutzisky,
  Andrew J Ryan, and Joseph A Ryan for identity and Army-entry chronology only.
  Public evidence did not establish their pre-OSS employers, and Army
  occupation codes were not converted into employment claims.

## Exact coverage after Batch 830

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,070/23,938 (50.4219%).
- Verified-employer coverage: 394/23,938 (1.6459%).
- Verified-affiliation coverage: 872/23,938 (3.6427%).
- Archival-review coverage: 10,534/23,938 (44.0053%).
- Not started: 11,863.
- Possible duplicate groups: 553; conflicts: 417.
- Claims: 1,563 confirmed; 3,726 high; 1,653 medium; 202 low; 360
  conflicting; two unresolved.
- Citations: 6,275 records representing 3,315 unique source documents.
- Total saved research attempts and plans: 23,897.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch830.csv`. Evidence,
identity claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page405-rust-ryan-review_batch-830_2026-10-15.json`.

The identity-decision replay skipped all five duplicate decisions on the
second import. Evidence replay retained exactly 23 Batch 830 attempts, five
affiliations, 12 claims, five organizations, and six sources. SQLite reports
no foreign-key violations.

## Local release verification

Local release verification passed:

- 145/145 Python tests passed.
- Astro reported zero errors, warnings, or hints and built 24,982 pages.
- 84/84 bounded Playwright release tests passed across Batch 830, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- All internal links across 24,982 HTML files resolved; 51,186 unique external
  URLs were inventoried for separate review.
- Public-identifier redaction found zero unexpected boundary matches,
  aggregate false positives, or manifest-size false positives.
- The public manifest contains 67 assets totaling 113,407,833 bytes, with
  SHA-256 `a74b9d43e4a949da0109930765e712a73f25495b14a0094ab162eadb964e44d9`.
- Two clean production builds produced the same 25,054-file tree hash,
  `812e34bf8d52c43186d9630321258419db40e17918fe244e2927c4af2557e294`.

GitHub Pages run 38837901932 published commit
`a9b02bbcc9c6f613fd60b7250a1b098c7eb7327b` successfully. The immutable live
verifier matched all 67 public assets (113,407,833 bytes), the release manifest,
eight core routes, 34 source-register pages, and all 23 Batch 830 profile URLs
without authentication.

Resume new-person research at PDF page 405, row 24. Full-index historical
research remains unfinished; 11,863 active people are still `not_started`.
