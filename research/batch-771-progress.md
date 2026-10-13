# Batch 771 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 771 covers PDF page 375, rows 25-46, Eleanor A Powell through Richard W
Powers. All 22 printed rows remain preserved as distinct source records and are
linked to 22 distinct person entities. Page 375 was inspected against a 300 dpi
render before the batch was researched. The next unresearched boundary is PDF
page 376, row 1, Steele Powers.

## Research protocol and review

- NARA Catalog work was dry-run only: 22 planned searches and zero authenticated
  requests. No key or API response was stored.
- The CIA Reading Room adapter failed closed on its first request. The access
  failure is recorded as a source limitation, not negative evidence.
- Library of Congress searches completed for 20 people and returned source
  errors for two. Forty-four candidate pages were reviewed and rejected for a
  missing identity bridge, an incompatible date, or exclusively postwar
  evidence.
- Fifty-one review decisions are durable: six accepted exact-name plus protected-
  identifier Army matches, one identifier/name conflict, and 44 rejected LoC
  candidates.
- Twenty-two manual research attempts give every person in this batch a terminal
  disposition: 20 `requires_archival_review`, one
  `documented_prewar_employer_found`, and one `conflicting_sources`.

## Historical outcomes

- Eugene B Power is matched with high identity confidence to Eugene Barnum
  Power. University of Michigan institutional sources document his 1930-1938
  vice presidency at Edwards Brothers, Inc. and his 1938 founding of University
  Microfilms. Edwards Brothers is published as earlier documented employment.
  University Microfilms is published as a qualified, medium-confidence best-
  supported last civilian affiliation before OSS, not as an immediate
  affiliation, because a possible intervening government role remains
  unresolved.
- Garland W Powell, Louis G Powell, Roy E Powell, Sidney Powell, Justin J
  Powers, and Richard W Powers have high-confidence official Army identity
  matches using exact names and protected identifiers. Army coded-occupation
  fields were not treated as employers.
- Robert I Powell has a high-confidence name-and-rank identity bridge to a
  French national-library finding aid for a 12 September 1944 wartime France
  note signed by Robert I Powell, lieutenant colonel. This is identity evidence,
  not employer evidence.
- The John Powell row remains `conflicting`: its protected identifier agrees
  with an Army record printed as `POWELCZAK JOHN`, but the surname does not.
  Powelczak was not adopted as an alias.
- John L Power's indexed T/5 rank is transparently classified as enlisted Army
  personnel. An incompatible naval-officer namesake was rejected.
- No employer was inferred from rank, education, an Army occupation code, a
  postwar source, or an unbridged namesake.

## Exact coverage after Batch 771

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 10,735/23,939 (44.8431%).
- Verified-employer coverage: 351/23,939 (1.4662%).
- Verified-affiliation coverage: 790/23,939 (3.3001%).
- Archival-review coverage: 9,193/23,939 (38.4018%).
- Not started: 13,199.
- Possible duplicate groups: 540; conflicts: 363.
- Claims: 1,408 confirmed; 3,299 high; 1,586 medium; 201 low; 316
  conflicting; two unresolved.
- Citations: 5,921 records representing 3,045 unique source documents.

## Durable inputs and replay

The reviewed decisions are stored in
`research/identity_review_decisions_2026-10-13_batch771.csv`; the evidence,
claims, source metadata, person updates, and manual attempts are stored in
`research/evidence-page375-powell-powers-review_batch-771_2026-10-13.json`.
Both files validate and import idempotently through the normal pipeline.

Resume new-person research at PDF page 376, row 1, Steele Powers. Full-index
historical research remains unfinished; 13,199 active people are still
`not_started`.
