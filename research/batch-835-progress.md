# Batch 835 research progress

Date: 2026-10-16 America/New_York

## Scope and preservation

Batch 835 covers PDF page 407, rows 24-46, Lily Salz through Armando
Sanchez. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 407 was inspected against a rendered
page before research. The next unresearched boundary is PDF page 408, row 1.

Printed names, initials, ranks or grades, blank cells, private identifiers, box
numbers, notes, and archival locations remain recoverable exactly as indexed.
Full service identifiers, coded Army occupations, and conflicting Army
candidate names remain private and are absent from public outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  marked-variant OSS searches, employment and occupation searches, and
  applicable military, obituary, institutional, newspaper, directory, and
  archival checks. NARA Catalog queries remained in dry-run mode.
- All 23 people now have saved, reviewable outcomes: 21
  `requires_archival_review` and two `needs_identity_review`.
- Identity resolution ends with one confirmed person, six high-confidence
  people, one ambiguous person, two conflicting people, and 13 unresolved
  people. Unresolved, ambiguous, and conflicting cases retain explicit Box 673
  or 674 next actions.
- Six exact-name or defensible marked-variant, nonshared protected-identifier
  Army candidates were accepted as identity crosswalks only. Two official Army
  rows carried materially different names under the index identifiers; these
  remain private conflicts, and no coded occupation or namesake biography was
  assigned.
- William Samolin remains ambiguous. A rare historian and professor namesake
  was rejected because no source established an OSS bridge and the documented
  military rank did not align with the index.

## Historical outcomes

- A contemporary *Evening Star* obituary confirms Major Forrest J. Sanborn as
  Forrest John Sanborn, a chemical engineer specializing in fire protection
  who entered the Army in 1942 and spent four years in OSS bombing research.
  An official 1947 Congressional Record independently documents his wartime
  plant-protection work.
- A later professional fire-protection history reports that Sanborn had many
  years of experience with Factory Mutual and Improved Risk Mutuals. The
  sources do not date or order the two relationships, so both are published as
  medium-confidence, timing-uncertain earlier employment and are excluded from
  default employer analytics. Neither is labeled his immediate pre-OSS or last
  civilian employer.
- Michael J. Sammarco, A. G. Sampatacacus, Bryan T. Samples, Alexander Z.
  Samu, Nicholas Sanabria, and Armando Sanchez receive high-confidence Army
  identity crosswalks. Protected identifiers support the private match but are
  not published.
- The remaining profiles preserve the negative search record and direct the
  next researcher to the indexed personnel file rather than claiming that no
  prior affiliation existed.

## Exact coverage after Batch 835

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 12,183/23,938 (50.8940%).
- Verified-employer coverage: 399/23,938 (1.6668%).
- Verified-affiliation coverage: 881/23,938 (3.6803%).
- Archival-review coverage: 10,648/23,938 (44.4816%).
- Not started: 11,750.
- Possible duplicate groups: 554; conflicts: 427.
- Claims: 1,579 confirmed; 3,761 high; 1,660 medium; 202 low; 364
  conflicting; two unresolved.
- Citations: 6,312 records representing 3,347 unique source documents.
- Total saved research attempts and plans: 24,378.
- Public projection: 23,938 people, 2,766 affiliations, 1,017 organizations,
  5,084 sources, and 7,360 claims.

## Durable inputs and replay

Evidence, identity claims, person updates, rejection reasons, and research
attempts are stored in
`research/evidence-page407-salz-sanchez-review_batch-835_2026-10-16.json`.
Eight Army candidate decisions are stored in
`research/army_review_decisions_2026-10-16_batch835.csv`. Evidence replay
retained exactly 23 Batch 835 research attempts, two affiliations, ten claims,
two organization inputs, five sources, and 20 claim-source links. Reimporting
the decision file skipped all eight existing decisions, and SQLite reports no
foreign-key violations.

## Release status

The database and generated public assets have been rebuilt locally. Python,
Astro, Playwright, internal-link, public-identifier, manifest, and deterministic
double-build checks all pass. GitHub Pages publication and immutable live
verification are pending.

Resume new-person research at PDF page 408, row 1.
