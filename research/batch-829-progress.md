# Batch 829 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 829 covers PDF page 404, rows 24-46, John S Russell through Vincent J
Russo. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 404 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 405, row 1,
William J Rust.

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
  queries. A bounded CIA request for Charles J. Russhon recorded a robots
  access error, while the Library of Congress probe returned no candidate;
  neither result was treated as proof that no evidence exists.
- Four exact protected-identifier Army matches were accepted for identity
  only. Army occupation codes were not published as jobs or employers. Two
  incompatible Army-name candidates were explicitly rejected and remain
  visible as conflicts.
- Civilian employment, student status, wartime military assignment and
  unresolved archival leads remain separate concepts. Pratt Institute is not
  classified as Alexander P. Russo's employer, and Theodore W. Russell's Army
  pathway is not labeled civilian employment.
- All 23 people now have saved, reviewable, terminal outcomes. Cases without
  adequate online evidence identify Box 667 or 668 as the next evidence
  target.

## Historical outcomes

- An official Air Force Special Operations Command history identifies Charles
  J. Russhon as a pre-Pearl Harbor sound engineer for both NBC in New York and
  Republic Pictures in Hollywood before he joined the Army Air Corps. Both are
  published as documented prewar employers. The source does not sequence the
  two jobs, so neither is mislabeled as the immediate affiliation or last
  civilian employer.
- An archived official Naval History and Heritage Command biography identifies
  Alexander P. Russo as a U.S. Naval Reserve specialist who studied art at
  Pratt Institute before his 1942 enlistment. Pratt is published as student
  status only. The biography says Specialist First Class while the index says
  SP2C, so identity remains high-confidence rather than confirmed pending Box
  668 review.
- A contemporary OSS Board of Officers report confirms Theodore W. Russell by
  exact name, rank, branch and protected identifier. It explicitly documents
  his recruitment from the Army for Operational Group duty as communications
  officer of a Greek unit. The Army is therefore modeled as an
  explicit-immediate military assignment; no civilian employer is invented.
- Official Army data confirm Robert W. Russell, William H. Russell, William J.
  Russell and Fred B. Russo for identity and Army-entry chronology only. No
  coded occupation was converted into a public job or employer claim. The
  screenwriter Robert Wallace Russell remains an unassigned namesake because
  public evidence does not bridge him to the indexed sergeant.
- Protected-identifier candidates for John M. Russo and Pirto Russo were
  rejected because the Army records contain respectively a different first
  name and an incompatible damaged name field. The discrepancies remain
  visible for archival review.

## Exact coverage after Batch 829

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,047/23,938 (50.3258%).
- Verified-employer coverage: 393/23,938 (1.6417%).
- Verified-affiliation coverage: 871/23,938 (3.6386%).
- Archival-review coverage: 10,511/23,938 (43.9093%).
- Not started: 11,886.
- Possible duplicate groups: 553; conflicts: 417.
- Claims: 1,559 confirmed; 3,719 high; 1,652 medium; 202 low; 360
  conflicting; two unresolved.
- Citations: 6,269 records representing 3,310 unique source documents.
- Total saved research attempts and plans: 23,804.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch829.csv`. Evidence,
identity claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page404-russell-russo-review_batch-829_2026-10-15.json`.

The identity-decision replay skipped all six duplicate decisions on the second
import. Evidence replay retained exactly 23 Batch 829 attempts, four
affiliations, 13 claims, 22 claim-source links, four organizations, and five
sources. SQLite reports no foreign-key violations.

## Local release verification

Local release verification passed:

- 145/145 Python tests passed.
- Astro reported zero errors, warnings, or hints and built 24,979 pages.
- 87/87 bounded Playwright release tests passed across Batch 829, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- All internal links across 24,979 HTML files resolved; 51,179 unique external
  URLs were inventoried for separate review.
- Public-identifier redaction found zero unexpected boundary matches, aggregate
  false positives, or manifest-size false positives.
- The public manifest contains 67 assets totaling 113,317,973 bytes, with
  SHA-256 `7c4764340e917b7ff6cfcba25880f58b98b653c81859cfa2459dcdae683cf621`.
- Two clean production builds produced the same 25,051-file tree hash,
  `bd5e0e863d2338502f089c7d811826c3b62a8043290e9d8e033c9e94d30e4170`.

GitHub Pages publication and unauthenticated live verification are pending.

Resume new-person research at PDF page 405, row 1. Full-index historical
research remains unfinished; 11,886 active people are still `not_started`.
