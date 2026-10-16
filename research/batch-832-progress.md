# Batch 832 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 832 covers PDF page 406, rows 1-23, Harriet W Sabine through George M
Saharov. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 406 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 406, row 24,
Hans Sahl.

Printed names, initials, ranks or grades, blank cells, private identifiers, box
numbers, notes, and archival locations remain recoverable exactly as indexed.
Full service identifiers remain private and are absent from public outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks. NARA Catalog queries remained in dry-run mode.
- Official Army data confirmed Philip Sagon, Preston Saenz, and Saul Sacks by
  exact name and protected identifier. Stanley J Sabolepski was accepted at
  high confidence under the one-letter Army surname variant Sabolefski. These
  decisions establish identity and Army chronology only; no coded Army
  occupation was converted into an employer or public occupation claim.
- The protected-identifier Army candidate for Bernard Sachs was rejected
  because the Army record prints Sachs Gerhard. The conflict remains visible,
  and neither the Army biography nor its coded occupation was assigned to the
  indexed person.
- Identity resolution for the batch ends with three confirmed people, four
  high-confidence people, one conflicting person, and 15 unresolved people.
  Research statuses are 19 `requires_archival_review`, two
  `documented_prewar_employer_found`, one `conflicting_sources`, and one
  existing `verified_employer_found` profile preserved by continuity review.

## Historical outcomes

- A contemporary 1945 New Yorker profile identifies Alexander Sachs as an OSS
  consultant, dates his Lehman Corporation vice-presidency to 1936-1942, and
  says he began independent economic consulting in 1942. Independent
  consulting is therefore published as a medium-confidence probable-immediate
  civilian status; Lehman Corporation remains a separate, high-confidence
  documented earlier employer. It is not silently renamed Lehman Brothers.
- An official 1941 Interstate Commerce Commission report and a 1944 U.S.
  Department of Agriculture Graduate School bulletin identify George M.
  Saharov by exact name and transportation-economist occupation. His work in
  the ICC Bureau of Transport Economics and Statistics is published as a
  documented prewar government assignment. The sources do not prove that it
  immediately preceded OSS, so no immediate-transfer claim is made.
- Official Army data and a Washington Post obituary support Philip H. Sagon's
  identity and 1943 OSS chronology. Later legal and real-estate work is not
  recast as a prewar employer.
- Jerry M Sage's previously reviewed profile survives the rebuild unchanged:
  Fort Lewis is his immediate Army assignment and Procter and Gamble his last
  civilian employer. No duplicate claims were added.
- The remaining cases received documented negative-result protocols and
  explicit archival next actions. Those outcomes state that no reliable
  pre-OSS employer has yet been identified in accessible sources; they do not
  claim that the person had no prior employer.

## Exact coverage after Batch 832

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,115/23,938 (50.6099%).
- Verified-employer coverage: 396/23,938 (1.6543%).
- Verified-affiliation coverage: 876/23,938 (3.6595%).
- Archival-review coverage: 10,579/23,938 (44.1933%).
- Not started: 11,818.
- Possible duplicate groups: 554; conflicts: 421.
- Claims: 1,571 confirmed; 3,737 high; 1,654 medium; 202 low; 364
  conflicting; two unresolved.
- Citations: 6,288 records representing 3,326 unique source documents.
- Total saved research attempts and plans: 24,035.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch832.csv`. Evidence,
identity claims, person updates, rejection reasons, and research attempts are
stored in
`research/evidence-page406-sabine-saharov-review_batch-832_2026-10-15.json`.

The identity-decision replay skipped all five duplicate decisions on the
second import. Evidence replay retained exactly 23 Batch 832 attempts, three
affiliations, ten claims, three organizations, and six sources. SQLite reports
no foreign-key violations.

## Local release verification

Local release verification passed:

- 145/145 Python tests and 81 subtests passed.
- Astro reported zero errors, warnings, or hints and built 24,986 pages.
- 90/90 bounded Playwright release tests passed across Batch 832, core routes,
  analytics, accessibility, and phone, tablet, and desktop viewports.
- All internal links across 24,986 HTML files resolved; 51,197 unique external
  URLs were inventoried for separate review.
- Public-identifier redaction found zero unexpected boundary matches,
  aggregate false positives, or manifest-size false positives.
- The public manifest contains 67 assets totaling 113,579,621 bytes, with
  SHA-256 `0c9077ae5aedb3ebc5ffbfb0a379c20d6d7e0f837e89da7af291d9e278275331`.
- Two clean production builds produced the same 25,058-file tree hash,
  `0bcc9e798a1c6f3cb6f382468373ab82753112dfe78432a5a8066400139bc135`.

GitHub Pages run 38842994263 published commit
`e2b694d7242d74248e24fc8b06fc901c56ce08af` successfully, and Test run
38842994273 passed. The immutable live verifier matched all 67 public assets
(113,579,621 bytes), the release manifest, eight core routes, 34
source-register pages, and all 23 Batch 832 profile URLs without
authentication.

Resume new-person research at PDF page 406, row 24. Full-index historical
research remains unfinished; 11,818 active people are still `not_started`.
