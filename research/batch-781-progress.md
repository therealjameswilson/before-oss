# Batch 781 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 781 covers PDF page 380, rows 24-46, Raymond J Purdy through Florence E
Pyatte. All 23 printed rows remain preserved as distinct source records and are
linked to 23 distinct person entities. Page 380 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 381, row 1,
William A Pye.

The clipped printed notes `Also in B`, `Also Ra`, and `Also 335` remain exactly
as printed. None was silently expanded or used to infer an employer, unit, or
cross-reference. Full service or officer identifiers remain private and masked
in public output.

## Research protocol and review

- NARA Catalog work was dry-run only: 23 planned searches, zero authenticated
  requests, zero duplicate skips, and zero errors. No API key or response was
  stored.
- CIA Reading Room access failed closed on the first eligible request. The
  Library of Congress cohort adapter stalled and was stopped without data loss;
  a later direct read of one public Library of Congress item succeeded. These
  adapter outcomes are access limitations, not negative evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  military, foreign-language, and archival query families were reviewed for all
  23 people. Namesakes, discovery-only genealogy, people-finder pages, postwar
  employers, and temporally insufficient candidates were rejected.
- Two official Army candidate decisions are durable high-confidence identity
  matches. Army occupation codes were not treated as employers or immediate
  affiliations.
- Twenty-two people now have the terminal status `requires_archival_review`;
  Edwin J Putzell has `verified_employer_found`.

## Historical outcomes

- Library of Congress, NARA, and Harvard Law School sources confirm Edwin J.
  Putzell Jr.'s identity, his OSS Director's Office role, and his employment as
  a legal clerk at Donovan, Leisure, Newton and Lumbard. The 1937 law-firm
  employment and 1942 Navy/OSS transition support the firm as both the
  strongly date-bounded immediate pre-OSS affiliation and the best-supported
  last civilian employer before service.
- The separately printed Edward J Putzell and Edwin J Putzell rows remain
  separate in a visible possible-duplicate group. All reviewed Donovan and OSS
  evidence names Edwin; none of Edwin's employer evidence is transferred to
  Edward pending comparison of both Box 626 files.
- A scholarly archival study supports a high-confidence identity for Stuart O.
  Pusey and documents him as a major in the OSS Special Operations Branch
  during the July 1945 Operation Airedale deliberations. It does not establish
  a pre-OSS employer.
- Official Army evidence supports high-confidence identity matches for Raymond
  J Purdy and Andrew B Puskas. The coded occupations and grade data remain
  excluded from employer claims.
- A motion-picture projectionist named Cecil R Putnam, a French physician and
  politician named Louis Puy, later lumber-industry records for Leonard R
  Putnam, and other common-name candidates were rejected because no direct OSS
  or protected-identifier bridge linked them to the indexed rows.

## Exact coverage after Batch 781

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 10,963/23,939 (45.7956%).
- Verified-employer coverage: 357/23,939 (1.4913%).
- Verified-affiliation coverage: 800/23,939 (3.3418%).
- Archival-review coverage: 9,422/23,939 (39.3584%).
- Not started: 12,971.
- Possible duplicate groups: 544; conflicts: 370.
- Claims: 1,411 confirmed; 3,394 high; 1,594 medium; 202 low; 322
  conflicting; two unresolved.
- Citations: 5,979 records representing 3,088 unique source documents.
- Public data: 2,592 published affiliations, 924 organizations, 4,754 public
  sources, and 6,717 published claims.

## Durable inputs and replay

The reviewed identity decisions are stored in
`research/identity_review_decisions_2026-10-13_batch781.csv`; the evidence,
claims, source metadata, person updates, duplicate safeguards, and terminal
manual attempts are stored in
`research/evidence-page380-purdy-pyatte-review_batch-781_2026-10-13.json`.
Both files validate and replay idempotently through the normal pipeline.

Resume new-person research at PDF page 381, row 1, William A Pye. Full-index
historical research remains unfinished; 12,971 active people are still
`not_started`.
