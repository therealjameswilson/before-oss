# Batch 823 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 823 covers PDF page 401, rows 24-46, Otto Rossmeyer through the
printed `Saymour A Rottenberg`. All 23 printed rows remain preserved as
immutable source records and map to 23 active person entities. Page 401 was
inspected against a 300 dpi render before research. The next unresearched
boundary is PDF page 402, row 1, Maurice H Rottersmann.

Printed names, initials, ranks or grades, blank cells, private identifiers,
box numbers, notes, and archival locations remain recoverable exactly as
indexed. The printed `Saymour A Rottenberg` spelling remains authoritative;
`Seymour A. Rottenberg` and `Seymour A. Rattenberg` are retained as reviewable
variants rather than silently merged. Full service identifiers remain private
and are absent from public outputs.

## Research protocol and review

- Every person received NARA index-context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks.
- The NARA Catalog adapter recorded 23 deterministic dry-run queries because
  no securely configured API key was present in the process environment. The
  CIA adapter failed closed under its access policy, and the Library of
  Congress adapter recorded one source error. Access failures were not treated
  as historical negative evidence.
- Four protected-identifier Army matches were accepted for identity only.
  Army occupation codes were not published as jobs or employers. Three
  incompatible candidates and two unresolved spelling/duplicate candidates
  were explicitly rejected.
- Walt W Rostow's existing Columbia University claim was re-audited without
  creating a duplicate affiliation or claim.
- All 23 people now have saved, reviewable, terminal outcomes: 22 archival-
  review or documented-prewar outcomes and one explicitly conflicting case.

## Historical outcomes

- Official Army bulk data and a published obituary confirm indexed Sergeant
  Otto Rossmeyer's identity and OSS Army service. His later and family
  business history was not converted into a pre-OSS employer claim.
- The exact distinctive name and a 1937 institutional thesis record support a
  probable match for Major Harold R Rossmiller. The University of Nebraska
  medical-school relationship is published as a qualified student affiliation,
  not an employer, and is not presented as immediately pre-OSS.
- Two contemporary Foreign Service journals establish Robert Rossow Jr. as a
  Foreign Service officer from 1940 and place him at Panama in 1943. His exact
  name, suffix, and second-lieutenant rank support a high-confidence identity.
  The State Department relationship is modeled as a government assignment and
  does not claim an immediate transfer to OSS.
- Official Army data confirms the identities of Joseph A Rost, Walter
  Rothschild, and Paul Rothstein in addition to Otto Rossmeyer. It establishes
  Army-entry chronology only and does not identify a named employer or prove
  an immediate Army-to-OSS sequence.
- Army candidates attached to Tovio D Roswall, Sidney Roth, and Egan G
  Rothelini resolve to incompatible names and were rejected. The conflicts
  remain visible for personnel-file review.
- The protected identifier associated with printed Saymour A Rottenberg also
  appears with another indexed spelling, Seymour A Rattenberg. Neither
  candidate was adopted, the rows were not merged, and the profile is marked
  `conflicting_sources` pending comparison of the Box 663 files.
- The remaining unresolved profiles state that no reliable pre-OSS employer
  has yet been identified in the accessible sources reviewed and identify the
  indexed Box 662 or 663 personnel file as the next evidence target.

## Exact coverage after Batch 823

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,909/23,938 (49.7494%).
- Verified-employer coverage: 386/23,938 (1.6125%).
- Verified-affiliation coverage: 854/23,938 (3.5675%).
- Archival-review coverage: 10,373/23,938 (43.3328%).
- Not started: 12,024.
- Possible duplicate groups: 553; conflicts: 404.
- Claims: 1,532 confirmed; 3,683 high; 1,645 medium; 202 low; 347
  conflicting; two unresolved.
- Citations: 6,223 records representing 3,277 unique source documents.
- Total saved research attempts and plans: 23,355.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch823.csv`. Evidence,
identity claims, person updates, rejection reasons, and terminal attempts are
stored in
`research/evidence-page401-rossmeyer-rottenberg-review_batch-823_2026-10-15.json`.

The identity-decision replay skipped all nine duplicate decisions on the
second import. Evidence replay retained exactly 23 Batch 823 attempts, two
affiliations, eight claims, 16 claim-source links, two organizations, and six
sources. SQLite reports no foreign-key violations.

## Local release verification

- Python: 145 tests passed.
- Astro: 457 source files checked with zero errors, warnings, or hints; 24,959
  static HTML pages built.
- Browser: 90/90 bounded desktop, phone, tablet, analysis, and accessibility
  checks passed, including all 21 Batch 823 viewport checks.
- Links: all 24,959 generated HTML files passed internal-link checks; 51,134
  unique external URLs were inventoried for the separate live check.
- Redaction: zero unexpected protected-identifier boundary matches across
  25,031 built artifacts; aggregate and manifest false positives were zero.
- Manifest: 67 assets and 112,747,399 bytes verified in both public trees;
  manifest SHA-256
  `f0d25497717eab484345137c6bc44b0d18ad1c7a2eb941f78033c415417b7e53`.
- Determinism: two consecutive production builds produced SHA-256
  `98d5f1f50781b507ce571ae5a6999d941d3b37171d219de470f179e77c9d1afb`
  across 25,031 files and 318,941,538 bytes.

Resume new-person research at PDF page 402, row 1. Full-index historical
research remains unfinished; 12,024 active people are still `not_started`.
