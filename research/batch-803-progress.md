# Batch 803 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 803 covers PDF page 391, rows 24-46, Roy K Richerson through Harry C
Riddle Jr. All 23 printed rows remain preserved as immutable source records.
After a reviewed merge of the Richerson and Rickerson rows, the batch represents
22 active person entities. Page 391 was inspected against a 300 dpi render
before research. The next unresearched boundary is PDF page 392, row 1, Carrie
E Rider.

The Box 643-to-644 transition and the clipped notes `photogra`, `French c`,
`Charged`, and `Record` remain intact. None was silently expanded or converted
to an occupation. Public profiles and downloads continue to mask protected
identifiers.

## Research protocol and review

- NARA index context, exact-name OSS searches, source-specific CIA Reading Room
  checks, Library of Congress checks, employment and occupation searches, and
  obituary, institutional, newspaper, military-history, and archival searches
  were reviewed for every active person. NARA Catalog requests remained planned
  because no API key was present in the process environment.
- All 22 active people now have terminal outcomes: one
  `verified_employer_found`, two `occupation_only_found`, and 19
  `requires_archival_review`.
- Four official Army bulk identity candidates were accepted after exact-name
  and nonshared protected-identifier agreement. A duplicate John G Riddell bulk
  row was rejected as redundant and does not inflate independent-source counts.
  Coded Army fields were not converted into employers.
- Roy K Richerson and Roy K Rickerson share the same protected identifier. NPS
  and Army historical sources consistently use Rickerson and document the
  indexed lieutenant-to-captain progression. The two source rows are linked to
  one confirmed entity while both spellings and ranks remain public.
- The two Allen R Richter rows remain separate because their protected
  identifiers differ. Official NPS evidence supports the master-sergeant row
  and documents prior communications-industry experience, but the adjacent
  Captain row is only a probable later record pending personnel-file review.
- No low-confidence lead was published as fact. Common and incomplete names
  remain unresolved with explicit Box 643 or 644 review guidance.

## Historical outcomes

- Peirson Ricks has a high-confidence immediate pre-OSS affiliation: an
  authoritative biography states that he was briefly employed by an unnamed
  technical school and then by OSS. It also documents earlier copywriting for
  an unnamed Philadelphia advertising firm and work in an unnamed
  Winston-Salem cotton mill. The unnamed organizations were not guessed or
  normalized to modern institutions.
- Melvin Richter has a high-confidence identity through exact official Army
  matching and an independent Army historical roster for OSS Operation MAGPIE.
  Institutional sources document a Harvard College B.A. in 1943. Harvard is
  published as student status, not as employment.
- Official NPS history identifies Sergeant Allen R Richter of Detachment 101
  and states that he had worked in the communications industry. Because no
  company is named, this remains qualified occupational context rather than a
  named employer claim.
- Official Army bulk data supports high-confidence identities for Leonal D
  Rickard, John G Riddell, and James H Riddle, but no named employer for any of
  them.
- A probable Section JUSTINE lead for Nathan L Richman remains qualified because
  the specialist roster uses initials, differs on rank, and supplies no
  protected identifier.

## Exact coverage after Batch 803

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,456/23,938 (47.8570%).
- Verified-employer coverage: 371/23,938 (1.5498%).
- Verified-affiliation coverage: 822/23,938 (3.4339%).
- Archival-review coverage: 9,919/23,938 (41.4362%).
- Not started: 12,477.
- Possible duplicate groups: 551; conflicts: 393.
- Claims: 1,418 confirmed; 3,600 high; 1,623 medium; 202 low; 337
  conflicting; two unresolved.
- Citations: 6,102 records representing 3,183 unique source documents.
- Public data: 2,646 published affiliations, 951 organizations, 4,877 public
  sources, and 6,974 published claims.
- Total saved research attempts and plans: 22,136.

## Durable inputs and replay

Evidence, claims, affiliations, person updates, rejection reasons, and terminal
attempts are stored in
`research/evidence-page391-richerson-riddle-review_batch-803_2026-10-15.json`.
Reviewed merge and Army candidate decisions are stored in
`research/identity_review_decisions_2026-10-15_batch803.csv`. Both import paths
were replayed: review decisions were recognized as duplicates and evidence
object counts remained identical, confirming idempotent outcomes.

Resume new-person research at PDF page 392, row 1, Carrie E Rider. Full-index
historical research remains unfinished; 12,477 active people are still
`not_started`.
