# Batch 833 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 833 covers PDF page 406, rows 24-46, Hans Sahl through Theodore S
Saliaris. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 406 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 407, row 1,
Edgar Salinger.

Printed names, initials, ranks or grades, blank cells, private identifiers, box
numbers, notes, and archival locations remain recoverable exactly as indexed.
Full service identifiers remain private and are absent from public outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks. NARA Catalog queries remained in dry-run mode.
- All 23 people now have saved, reviewable terminal outcomes: four
  `verified_employer_found`, one `documented_prewar_employer_found`, and 18
  `requires_archival_review`.
- Identity resolution ends with three confirmed people, three high-confidence
  people, and 17 unresolved people. Unresolved cases retain explicit Box 672
  next actions and do not receive namesake biographies or inferred employers.
- The Ritchie Boys lead for Vitaly Sakouta was rejected because it used middle
  initial M rather than the index's W. Postwar namesakes for Nils Sahlin and
  Kataro Saimoto and common-name results for the Salerno entries were not
  projected backward.

## Historical outcomes

- A direct 1944 OSS Cairo interview confirms Captain George C. Sakellaris and
  names Cities Service Company, where he had been a cost accountant, as his
  civilian employer before Army entry. The same interview supports Camp Carson
  as his probable immediate Army assignment before OSS. Cities Service is
  preserved under its historical oil-company name, adding Sakellaris to the
  site's cited oil-company category.
- A Washington Post obituary and the UCLA Yoneo Sakai Papers place Yoneo Sakai
  at a wartime Japanese-language school before OSS and document earlier work as
  an Asahi Shimbun reporter in Los Angeles. The obituary says Naval Language
  School; the finding aid says Military Intelligence Service Language School.
  Both labels remain visible pending archival reconciliation.
- An official Congressional Record chronology places William A. Salant at the
  Federal Reserve Board, Office of Price Administration, and White House before
  1942-43 OSS employment. The White House is published as the immediate
  government assignment, not a private civilian employer.
- An institutional biography identifies Richard S. Salant's 1941-43 Office of
  the Solicitor General work as his last dated civilian government role before
  Naval Reserve service, with earlier National Labor Relations Board work kept
  separate. No direct OSS transfer is inferred.
- Direct 1943-44 OSS correspondence confirms Hans Sahl. A reputable biography
  documents qualified pre-OSS subtitle-translation work for Metro-Goldwyn-Mayer
  and earlier Marseille refugee-aid work, but no immediate predecessor role.
- An official 1945 OSS order confirms Konstantine A. Salaris by exact name,
  grade, and protected identifier. It is used for identity only and not
  converted into an employer claim.

## Exact coverage after Batch 833

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,138/23,938 (50.7060%).
- Verified-employer coverage: 398/23,938 (1.6626%).
- Verified-affiliation coverage: 880/23,938 (3.6762%).
- Archival-review coverage: 10,602/23,938 (44.2894%).
- Not started: 11,795.
- Possible duplicate groups: 554; conflicts: 421.
- Claims: 1,575 confirmed; 3,748 high; 1,656 medium; 202 low; 364
  conflicting; two unresolved.
- Citations: 6,298 records representing 3,334 unique source documents.
- Total saved research attempts and plans: 24,150.

## Durable inputs and replay

Evidence, identity claims, person updates, rejection reasons, and research
attempts are stored in
`research/evidence-page406-sahl-saliaris-review_batch-833_2026-10-15.json`.
Evidence replay retained exactly 23 Batch 833 attempts, 11 affiliations, 17
claims, 11 organization inputs, and ten sources. SQLite reports no foreign-key
violations.

## Local release verification

Local release verification passed:

- 145/145 Python tests and 81 subtests passed.
- Astro reported zero errors, warnings, or hints and built 24,991 pages.
- 84/84 bounded Playwright release tests passed across Batch 833, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- All internal links across 24,991 HTML files resolved; 51,209 unique external
  URLs were inventoried for separate review.
- Public-identifier redaction found zero unexpected boundary matches,
  aggregate false positives, or manifest-size false positives.
- The public manifest contains 67 assets totaling 113,711,988 bytes, with
  SHA-256 `6fe56d00dc64a8a6c93b3833d5fc073c7920fccccec825abf1c4e0ade0aab4a0`.
- Two clean production builds produced the same 25,063-file tree hash,
  `03247edc1671d55819c545e7c2ed26068ae3e1478338f11a19c9ff2071033906`.

GitHub Pages publication is pending. Resume new-person research at PDF page
407, row 1, Edgar Salinger, after the Batch 833 release is verified.
