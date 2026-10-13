# Batch 772 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 772 covers PDF page 376, rows 1-24, Steele Powers through Jack C Pratt.
All 24 printed rows remain preserved as distinct source records and are linked
to 24 distinct person entities. Page 376 was inspected against a 300 dpi render
before the batch was researched. The next unresearched boundary is PDF page
376, row 25, Philip P Pratt.

## Research protocol and review

- NARA Catalog work was dry-run only: 24 planned searches and zero
  authenticated requests. No key or API response was stored.
- The CIA Reading Room and Library of Congress adapters each failed closed on
  their first live request. These access failures are recorded as source
  limitations, not negative evidence.
- Exact-name OSS and employment/occupation search families were completed for
  all 24 people. Namesake, genealogy, people-finder, unbridged postwar, and
  otherwise temporally insufficient results were rejected.
- Five identity review decisions are durable: four accepted exact-name plus
  protected-identifier Army matches and one protected-identifier/name conflict.
- Twenty-four manual research attempts give every person in this batch a
  terminal disposition: 22 `requires_archival_review`, one
  `verified_employer_found`, and one `conflicting_sources`.

## Historical outcomes

- Nelson P Poynter is identified with high confidence. The St. Petersburg Times
  / Times Publishing Company is published as his high-confidence last civilian
  employer through 8 December 1940. His subsequent federal inter-American
  communications press assignment is separately published as the
  high-confidence immediate pre-OSS/COI affiliation. The civilian employer and
  government assignment are not conflated.
- Armand R Poyant has a high-confidence Army identity match using his exact name
  and protected identifier. A Washington Post obituary independently
  corroborates his Army, North Africa, and OSS chronology, but does not establish
  a pre-OSS civilian employer.
- Reno Prandini, Arnold L Prange, and Leland J Prater have high-confidence
  official Army identity matches using exact names and protected identifiers.
  Army coded-occupation fields were not treated as employers.
- Walter E Powers remains `conflicting`: the protected identifier agrees with
  an Army record printed as `POWERS WALTER JR`, while the index records Walter E
  Powers. `Jr` was not adopted as an alias.
- Branko Prastalo has a high-confidence rare-name OSS Bari Yugoslav Section
  identity bridge from scholarly research. The documented spelling variant
  `Branko Praštalo` is preserved; no recruitment path or employer was inferred.
- No employer was inferred from rank, education, occupation alone, a namesake,
  or a source lacking a defensible temporal relationship to OSS service.

## Exact coverage after Batch 772

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 10,759/23,939 (44.9434%).
- Verified-employer coverage: 352/23,939 (1.4704%).
- Verified-affiliation coverage: 791/23,939 (3.3042%).
- Archival-review coverage: 9,217/23,939 (38.502%).
- Not started: 13,175.
- Possible duplicate groups: 540; conflicts: 364.
- Claims: 1,408 confirmed; 3,307 high; 1,586 medium; 201 low; 317
  conflicting; two unresolved.
- Citations: 5,928 records representing 3,051 unique source documents.

## Durable inputs and replay

The reviewed decisions are stored in
`research/identity_review_decisions_2026-10-13_batch772.csv`; the evidence,
claims, source metadata, person updates, and manual attempts are stored in
`research/evidence-page376-powers-pratt-review_batch-772_2026-10-13.json`.
Both files validate and import idempotently through the normal pipeline.

Resume new-person research at PDF page 376, row 25, Philip P Pratt. Full-index
historical research remains unfinished; 13,175 active people are still
`not_started`.
