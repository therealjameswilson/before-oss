# Batch 805 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 805 covers PDF page 392, rows 24-46, Ivan B Rigby through Margaret R
Riley. All 23 printed rows remain preserved as immutable source records and map
to 23 active person entities. Page 392 was inspected against a 300 dpi render
before research. The next unresearched boundary is PDF page 393, row 1, Thomas
R Riley.

The clipped notes `photogra`, `Honorab`, `Record`, and `also AS` remain intact.
None was silently expanded or converted to an occupation. The two separately
printed John E Riley rows remain separate people because their protected
identifiers differ. Public profiles and downloads continue to mask those
identifiers.

## Research protocol and review

- NARA index context, exact-name OSS searches, employment and occupation
  searches, and obituary, institutional, newspaper, military-history, and
  archival searches were reviewed for every person. NARA Catalog requests
  remained planned because no API key was available in the local process
  environment.
- A live CIA Reading Room attempt failed closed under the site's robots policy.
  A live Library of Congress attempt exhausted bounded retries on a timeout.
  Neither access failure was treated as a negative research result.
- All 23 people now have terminal `requires_archival_review` outcomes. Eight
  identities are `high_confidence`, one is `probable`, and 14 remain
  `unresolved`.
- Seven official Army bulk identity candidates were accepted after exact-name
  and nonshared protected-identifier agreement. Coded Army occupation fields
  were not converted into employers.
- No defensible pre-OSS employer was found for this batch. No low-confidence
  lead or modern namesake was published as fact.

## Historical outcomes

- An authoritative U.S. Army Special Operations history supports a
  high-confidence identification of French sub-lieutenant Andre Rigot as the
  observer of OSS-linked Team FILAN. The evidence documents wartime service,
  not a pre-OSS employer.
- A NARA-released 1946 government travel voucher names F. Catherine Rigsbee as
  an administrative assistant. The site presents it only as a probable,
  postwar identity bridge and does not use it as pre-OSS employment evidence.
- Official Army bulk data supports high-confidence identities for Ivan B
  Rigby, Walter M Riggs Jr., Edward F Rijos, James A Riley, James L Riley, and
  both separately indexed John E Riley people. It establishes identity and
  Army service only.
- Other apparent Andre Rigot and Riley namesakes were rejected when chronology,
  role, geography, or identifiers did not support the indexed person.

## Exact coverage after Batch 805

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,502/23,938 (48.0491%).
- Verified-employer coverage: 372/23,938 (1.5540%).
- Verified-affiliation coverage: 824/23,938 (3.4422%).
- Archival-review coverage: 9,965/23,938 (41.6284%).
- Not started: 12,431.
- Possible duplicate groups: 552; conflicts: 394.
- Claims: 1,418 confirmed; 3,614 high; 1,627 medium; 202 low; 338
  conflicting; two unresolved.
- Citations: 6,116 records representing 3,195 unique source documents.
- Public data: 2,651 published affiliations, 952 organizations, 4,891 public
  sources, and 6,993 published claims.
- Total saved research attempts and plans: 22,367.

## Durable inputs and replay

Evidence, claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page392-rigby-riley-review_batch-805_2026-10-15.json`.
Reviewed Army candidate decisions are stored in
`research/identity_review_decisions_2026-10-15_batch805.csv`. Both import paths
were replayed: review decisions were recognized as duplicates and evidence
object counts remained identical, confirming idempotent outcomes.

Resume new-person research at PDF page 393, row 1, Thomas R Riley. Full-index
historical research remains unfinished; 12,431 active people are still
`not_started`.
