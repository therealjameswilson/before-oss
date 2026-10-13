# Batch 773 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 773 covers PDF page 376, rows 25-46, Philip P Pratt through Julia J
Preston. All 22 printed rows remain preserved as distinct source records and
are linked to 22 distinct person entities. Page 376 was inspected against a
300 dpi render before the batch was researched. The next unresearched boundary
is PDF page 377, row 1, Thomas G Presutti.

The printed scientific-notation-like serial value for Thomas M Preen remains
preserved literally in the private source record and masked in public output.
The visibly truncated notes for Henry S Prescott and Theodore R Press remain
unexpanded pending personnel-file review.

## Research protocol and review

- NARA Catalog work was dry-run only: 22 planned searches and zero
  authenticated requests. No key or API response was stored.
- The CIA Reading Room adapter failed closed on its first request. The Library
  of Congress adapter completed three searches, returned one candidate, and
  timed out on a fourth. These access failures are source limitations, not
  negative evidence.
- Exact-name OSS and employment/occupation search families were completed for
  all 22 people. Namesake, genealogy, people-finder, unbridged postwar, and
  otherwise temporally insufficient results were rejected.
- Three candidate decisions are durable: one accepted official Army identity,
  one protected-identifier/name conflict, and one rejected newspaper namesake.
- Twenty-two manual research attempts give every person in the batch a terminal
  disposition: 21 `requires_archival_review` and one `conflicting_sources`.

## Historical outcomes

- John E Preston has a high-confidence identity match: his exact indexed name
  and a nonshared protected identifier agree with the official Army bulk
  record. Army occupation code 992 is not treated as an employer.
- Howard V Prenzel remains `conflicting`: the protected identifier agrees with
  an Army record printed as `RE E HOWARD V`, but the surname conflict is not
  resolved and the Army name is not adopted as an alias.
- A 1944 Milford Chronicle candidate for Howard J Preston was rejected after
  page-level OCR review showed Howard K Preston and no protected-identifier,
  OSS, or employment bridge.
- A same-name Joseph E. Persico Papers finding-aid result for Julio Prester is
  retained privately as a low-confidence archival lead. It is not published as
  a biographical claim without review of the folder contents.
- No employer was inferred from rank, civilian grade, Army occupation code,
  education, a namesake, or a source lacking a defensible temporal relationship
  to OSS service.

## Exact coverage after Batch 773

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 10,781/23,939 (45.0353%).
- Verified-employer coverage: 352/23,939 (1.4704%).
- Verified-affiliation coverage: 791/23,939 (3.3042%).
- Archival-review coverage: 9,239/23,939 (38.5939%).
- Not started: 13,153.
- Possible duplicate groups: 540; conflicts: 365.
- Claims: 1,408 confirmed; 3,308 high; 1,586 medium; 202 low; 318
  conflicting; two unresolved.
- Citations: 5,931 records representing 3,052 unique source documents.

## Durable inputs and replay

The reviewed decisions are stored in
`research/identity_review_decisions_2026-10-13_batch773.csv`; the evidence,
claims, source metadata, person updates, and manual attempts are stored in
`research/evidence-page376-pratt-preston-review_batch-773_2026-10-13.json`.
Both files validate and import idempotently through the normal pipeline.

Resume new-person research at PDF page 377, row 1, Thomas G Presutti. Full-index
historical research remains unfinished; 13,153 active people are still
`not_started`.
