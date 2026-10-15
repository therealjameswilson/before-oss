# Batch 822 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 822 covers PDF page 401, rows 1-23, E P Ross through Harold T Rossman.
All 23 printed rows remain preserved as immutable source records and map to 23
active person entities. Page 401 was inspected against a 300 dpi render before
research. The next unresearched boundary is PDF page 401, row 24, Otto
Rossmeyer.

Printed names, initials, ranks or grades, blank cells, private identifiers,
box numbers, notes, and archival locations remain recoverable exactly as
indexed. The printed `Guiseppe Rossetti` spelling remains authoritative;
`Giuseppe Rossetti` is retained only as a search alias. Full service
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
- Seven protected-identifier Army matches were accepted for identity only.
  Army occupation codes were not published as jobs or employers. One
  incompatible protected-identifier candidate was explicitly rejected.
- All 23 people now have saved, reviewable, terminal
  `requires_archival_review` outcomes.

## Historical outcomes

- Official Army bulk data confirms the indexed identities of Henry H Ross,
  Michael J Ross, Otto H Ross, Robert T Ross, Victor H Ross, Peter S Rossello,
  and Thomas G Rossi. It establishes Army-entry chronology only and does not
  identify a named employer or prove an immediate Army-to-OSS sequence.
- The Department of Veterans Affairs Veterans Legacy Memorial provides a
  probable match between indexed Major Stephen O Rossetti and the Army
  lieutenant colonel of that name. The match remains qualified until Box 662
  supplies an identifier bridge; the memorial does not document pre-OSS work.
- The Army candidate attached to Lawrence F Rossi's protected identifier names
  Jesse A Carvalho and was rejected. The public profile preserves the conflict
  and directs researchers to Box 662.
- A 1941 Brooklyn College publishing record and postwar World Bank records
  document an economist named Murray Ross, but no accessible source connects
  him to the indexed OSS captain. The lead therefore remains unassigned and no
  Brooklyn College employer claim is published.
- A Minnesota namesake lead for Harlow N Ross and Italian sports namesakes for
  Guiseppe or Giuseppe Rossetti lacked OSS, rank, identifier, and chronological
  corroboration. They were not adopted.
- The remaining unresolved profiles state that no reliable pre-OSS employer
  has yet been identified in the accessible sources reviewed and identify the
  indexed Box 661 or 662 personnel file as the next evidence target.

## Exact coverage after Batch 822

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,887/23,938 (49.6574%).
- Verified-employer coverage: 386/23,938 (1.6125%).
- Verified-affiliation coverage: 853/23,938 (3.5634%).
- Archival-review coverage: 10,351/23,938 (43.2409%).
- Not started: 12,046.
- Possible duplicate groups: 553; conflicts: 403.
- Claims: 1,528 confirmed; 3,681 high; 1,643 medium; 202 low; 347
  conflicting; two unresolved.
- Citations: 6,217 records representing 3,273 unique source documents.
- Total saved research attempts and plans: 23,284.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch822.csv`. Evidence,
identity claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page401-ross-rossman-review_batch-822_2026-10-15.json`.

The identity-decision replay skipped all eight duplicate decisions on the
second import. Evidence replay retained exactly 23 Batch 822 attempts, no
affiliations, eight claims, 16 claim-source links, and three sources. SQLite
reports no foreign-key violations.

## Local release verification

- Python: 145 tests passed.
- Astro: 456 source files checked with zero errors, warnings, or hints; 24,957
  static HTML pages built.
- Browser: 87/87 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 18 Batch 822 viewport checks.
- Links: all 24,957 generated HTML files passed internal-link checks; 51,129
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,029 built artifacts; aggregate and manifest false positives were zero.
- Manifest: 67 assets and 112,691,870 bytes verified in both public trees;
  manifest SHA-256
  `959ccb3c2682c937776248ef731e812de2bc39beee3eef6ba48c3dd83ac13d36`.
- Determinism: two consecutive production builds produced SHA-256
  `227e454ff2435c05268b89e078873a30a9d81f3c82569f0516a15498236985f0`
  across 25,029 files and 318,848,029 bytes.

Resume new-person research at PDF page 401, row 24. Full-index historical
research remains unfinished; 12,046 active people are still `not_started`.
