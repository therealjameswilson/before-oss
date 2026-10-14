# Batch 794 research progress

Date: 2026-10-14 America/New_York

## Scope and preservation

Batch 794 covers PDF page 387, rows 1-23, Harold J Regan through Gordon S
Reid. All 23 printed rows remain preserved as distinct source records linked to
23 person entities. Page 387 was inspected against a 300 dpi render before
research. The next unresearched boundary is PDF page 387, row 24, Lesta L Reid.

The printed placement of `P-5` and `T-5` in rows 2-3 was confirmed visually
and was not silently shifted into another column. The notes `Record`, `French`,
and `French c` remain exactly as printed and were not expanded. Full service
identifiers remain private.

## Research protocol and review

- NARA Catalog and web adapters recorded bounded dry-run plans and made no
  authenticated NARA request. No Catalog API response bodies were stored.
- The CIA adapter failed closed before producing a usable result. The Library
  of Congress request timed out on the first eligible person. These access
  failures were recorded and were not treated as negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  military, variant-name, and archival query families were reviewed for all 23
  people.
- Seven Army bulk candidates were manually reviewed. Four exact-name,
  nonshared-identifier matches were accepted for identity only. Three candidates
  with substantive or unresolved name conflicts were rejected and routed to
  critical archival review. Coded Army occupation fields were not treated as
  employers.
- William L Rehm's existing conservative outcome was retained. Accessible
  official evidence identifies senior investment-trust experience but not the
  trust's name; a retrospective Brown Brothers Harriman lead was not promoted
  to an employer claim.
- All 23 people now have saved terminal research outcomes. Twenty require
  archival review or have explicit identity conflicts; Hans J Rehfisch has an
  earlier documented BBC affiliation; Felix Reichman has a verified civilian,
  military, and OSS chronology; William L Rehm remains occupation-only.

## Historical outcomes

- Official Army bulk data supports high-confidence identities for Thomas J
  Regan, Lucien J Rego, Andrew J Regusis, and William L Reichle. Each public
  claim states that the record corroborates identity and Army service only.
- A participant account names playwright Hans Jose Rehfisch in the OSS London
  group, and NARA-based scholarship identifies Dr. Hans J. Rehfisch, born 1891,
  as an OSS Morale Operations radio-script writer. Deutsche Biographie records
  his BBC work after his 1936 move to London. The BBC is published only as an
  earlier documented affiliation, not as his immediate or last civilian
  pre-OSS employer.
- The indexed Felix Reichman is identified at high confidence as Felix
  Reichmann. A scholarly institutional biography explicitly sequences his
  work as librarian at the Carl Schurz Memorial Foundation, 1944 Army entry,
  and assignment to OSS in Washington. The Army is modeled as his immediate
  pre-OSS military assignment; the foundation is his last documented civilian
  employer. Landis Valley Museum and the family Vienna bookstore are earlier
  documented employment.
- Protected identifiers for Raymond Regan, Jack Reichenstein, and Andrew G
  Reid Jr. point to Army bulk names that are fused, substantively different, or
  contain an unexplained extra initial. These candidates were rejected rather
  than forced into identity matches, and the conflicts remain visible.

## Exact coverage after Batch 794

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,255/23,939 (47.0153%).
- Verified-employer coverage: 364/23,939 (1.5205%).
- Verified-affiliation coverage: 810/23,939 (3.3836%).
- Archival-review coverage: 9,716/23,939 (40.5865%).
- Not started: 12,679.
- Possible duplicate groups: 550; conflicts: 384.
- Claims: 1,413 confirmed; 3,507 high; 1,611 medium; 202 low; 331
  conflicting; two unresolved.
- Citations: 6,046 records representing 3,138 unique source documents.
- Public data: 2,617 published affiliations, 935 organizations, 4,821 public
  sources, and 6,858 published claims.
- Total saved research attempts and plans: 21,531.

## Durable inputs and replay

Reviewed candidate decisions are stored in
`research/identity_review_decisions_2026-10-14_batch794.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page387-regan-reid-review_batch-794_2026-10-14.json`.
Both were replayed through the normal import commands to verify idempotence.

Resume new-person research at PDF page 387, row 24, Lesta L Reid. Full-index
historical research remains unfinished; 12,679 active people are still
`not_started`.
