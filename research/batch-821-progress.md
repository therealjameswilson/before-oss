# Batch 821 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 821 covers PDF page 400, rows 24-46, Franz W Rosenthal through Darrell
E Ross. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 400 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 401, row 1,
E P Ross.

Printed names, initials, ranks or grades, blank cells, private identifiers, box
numbers, notes, and archival locations remain recoverable exactly as indexed.
Andrew Roskos remains the indexed form while the official Army record's
Andrew Roskos Jr variant is retained as identity evidence. Full service
identifiers remain private and are absent from public outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks.
- The NARA Catalog adapter recorded 23 deterministic dry-run queries because
  no API key was present in the process environment. The CIA adapter failed
  closed under its access policy, and the Library of Congress adapter recorded
  one source error. Access failures were not treated as historical negative
  evidence.
- Six protected-identifier Army matches were accepted for identity only. Army
  occupation codes were not published as jobs or employers. Two incompatible
  protected-identifier candidates were explicitly rejected.
- All 23 people now have saved, reviewable, terminal outcomes: four
  `completed` and 19 `requires_archival_review`.

## Historical outcomes

- Yale's memorial notice and the official Army enlistment record identify
  Franz W Rosenthal as a Hebrew Union College professor from 1940 to 1943,
  followed by Army service and basic training before his OSS assignment. The
  site separates the civilian employer from the military pathway.
- The University of Wisconsin-Stevens Point archival finding aid documents
  Malcolm L Rosholt's earlier work at The China Press and his later China News
  Service employment before a 1942 U.S. Army Air Forces commission. His 14th
  Air Force assignment remains qualified because its exact relationship to
  OSS service is not yet established.
- A Washington Post obituary, a contemporary University of Rochester
  directory, and the official OSS roster support University of Rochester as
  Harry A Rositzke's last documented civilian employer before wartime service.
- The Rochester directory also identifies Barbara B Rositzke as a news-bureau
  film assistant. Because the identity bridge is probable rather than
  conclusive, the claim is visibly qualified and is not presented as an
  immediate or last civilian employer.
- Official or authoritative sources confirm the indexed identities of Francis
  C Rosett and Douglas A Rosher without supplying a defensible pre-OSS employer
  claim. Identity-only Army matches likewise remain separate from employment
  claims.
- Chester J Rosinski and Anthony E Ross identifier candidates were rejected
  because their protected identifiers resolve to different people. Their
  profiles direct researchers to the indexed personnel files instead of
  adopting the incompatible matches.

## Exact coverage after Batch 821

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,864/23,938 (49.5614%).
- Verified-employer coverage: 386/23,938 (1.6125%).
- Verified-affiliation coverage: 853/23,938 (3.5634%).
- Archival-review coverage: 10,328/23,938 (43.1448%).
- Not started: 12,069.
- Possible duplicate groups: 553; conflicts: 403.
- Claims: 1,521 confirmed; 3,681 high; 1,642 medium; 202 low; 347
  conflicting; two unresolved.
- Citations: 6,214 records representing 3,271 unique source documents.
- Total saved research attempts and plans: 23,213.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch821.csv`. Evidence,
affiliations, claims, person updates, rejection reasons, and terminal attempts
are stored in
`research/evidence-page400-rosenthal-ross-review_batch-821_2026-10-15.json`.

The identity-decision replay skipped all eight duplicate decisions on the
second import. Evidence replay retained exactly 23 Batch 821 attempts, seven
affiliations, 18 claims, 34 claim-source links, five reused organizations, one
new organization, and nine sources. SQLite reports no foreign-key violations.

## Local release verification

- Python: 145 tests passed.
- Astro: 455 source files checked with zero errors, warnings, or hints; 24,957
  static HTML pages built.
- Browser: 90/90 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 21 Batch 821 viewport checks.
- Links: all 24,957 generated HTML files passed internal-link checks; 51,128
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,029 built artifacts; aggregate and manifest false positives were zero.
- Manifest: 67 assets and 112,654,291 bytes verified in both public trees;
  manifest SHA-256
  `c73ce8f4f07cdd69aabc83b8a60ae7cb0251df77926856bf8feb9cf7274e9d5d`.
- Determinism: two consecutive production builds produced SHA-256
  `de218ef719e5576250b98386f8e6db15d4445a1eda833904a56a8c9f9e14c5ca`
  across 25,029 files and 318,787,851 bytes.

Resume new-person research at PDF page 401, row 1. Full-index historical
research remains unfinished; 12,069 active people are still `not_started`.
