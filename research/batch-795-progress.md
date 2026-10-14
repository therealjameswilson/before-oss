# Batch 795 research progress

Date: 2026-10-14 America/New_York

## Scope and preservation

Batch 795 covers PDF page 387, rows 24-46, Lesta L Reid through Albert C
Reinert. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities. Page 387 was inspected against a 300 dpi render before
research. The next unresearched boundary is PDF page 388, row 1, Arthur F
Reinhardt.

The clipped notes `certificat`, `also pos`, and `British A` remain exactly as
printed and were not silently expanded. Full service identifiers remain
private.

## Research protocol and review

- NARA Catalog and web adapters recorded bounded dry-run plans and made no
  authenticated NARA request. No Catalog API response bodies were stored.
- The CIA and Library of Congress adapters each failed closed before producing
  a usable result. These access failures were recorded and were not treated as
  negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  military, variant-name, and archival query families were reviewed for all 23
  people.
- Seven Army bulk candidates were manually reviewed. Six exact or compatible,
  nonshared-identifier matches were accepted for identity only. The Richard K
  Reilly candidate was rejected because the bulk record gives the substantive
  given name Robert. Coded Army occupation fields were not treated as
  employers.
- All 23 people now have saved terminal research outcomes. Twenty-two require
  archival review or preserve an explicit identity conflict; Alfred Reifman has
  a verified employer and a documented military-to-OSS chronology.

## Historical outcomes

- Official Army bulk data supports high-confidence identities for Marne F
  Reid, Bertram Reifkind, Gordon E Reilly, Richard W Reilly, George Reim, and
  Charles F Reimer. Each public claim states that the record corroborates
  identity and Army service only.
- The official *Congressional Record* chronology for Alfred Reifman identifies
  employment as an economist at the Office of Price Administration from June
  1941 through October 1942, Army service from 1942 through 1944, and OSS work
  beginning in July 1944. The Army is modeled as his best-supported immediate
  pre-OSS military affiliation; the Office of Price Administration is his last
  documented civilian employer before service.
- A separate index row spells Alfred's surname `Riefman` while repeating the
  rank and protected identifier. Both source rows and person entities remain
  visible and unmerged pending review of the personnel files.
- The protected identifier for Richard K Reilly points to an Army bulk row
  named `REILLY ROBERT K`. That candidate was rejected rather than forced into
  an identity match, and the conflict remains visible.

## Exact coverage after Batch 795

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,278/23,939 (47.1114%).
- Verified-employer coverage: 365/23,939 (1.5247%).
- Verified-affiliation coverage: 811/23,939 (3.3878%).
- Archival-review coverage: 9,739/23,939 (40.6826%).
- Not started: 12,656.
- Possible duplicate groups: 550; conflicts: 385.
- Claims: 1,413 confirmed; 3,516 high; 1,611 medium; 202 low; 331
  conflicting; two unresolved.
- Citations: 6,049 records representing 3,139 unique source documents.
- Public data: 2,619 published affiliations, 935 organizations, 4,824 public
  sources, and 6,867 published claims.
- Total saved research attempts and plans: 21,602.

## Durable inputs and replay

Reviewed candidate decisions are stored in
`research/identity_review_decisions_2026-10-14_batch795.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page387-reid-reinert-review_batch-795_2026-10-14.json`.
Both were replayed through the normal import commands to verify idempotence.

Resume new-person research at PDF page 388, row 1, Arthur F Reinhardt.
Full-index historical research remains unfinished; 12,656 active people are
still `not_started`.
