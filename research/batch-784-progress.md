# Batch 784 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 784 covers PDF page 382, rows 1-24, John E Quintrell through
John M Radaszewski. All 24 printed rows remain preserved as distinct source
records and are linked to 23 person entities. Rows 23 and 24 are the same
indexed John M Radaszewski record: they share the same protected identifier but
point to Boxes 629 and 630, and therefore remain separate source rows linked to
one cautious person entity. Page 382 was inspected against a 300 dpi render
before research. The next unresearched boundary is PDF page 382, row 25,
Edwin R Raddatz.

The clipped notes "Extract fr" and "No first n" remain exactly as printed.
Neither was silently expanded or used to infer an employer, unit, or
cross-reference. Full service or officer identifiers remain private and masked
in public output.

## Research protocol and review

- NARA Catalog work was dry-run only: 23 first-pass planned searches and 17
  distinct serial-focused plans, with zero authenticated requests. No API key
  or response was stored.
- The CIA Reading Room adapter failed closed after one permitted retry. The
  Library of Congress adapter completed its bounded retry loop with two
  searches, one source-access error, three people attempted, and no adapter
  candidate. These access outcomes are limitations, not negative evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  military, variant-name, and archival query families were reviewed for all 23
  people. Namesakes, people-finder records, discovery-only genealogy, postwar
  evidence, and temporally insufficient candidates were rejected.
- Eleven official Army candidate rows representing ten people were accepted.
  The protected identifiers and indexed names agree; Carl H Raab's Army row
  adds a Jr. suffix, Frank D Quisenberry's Army name field repeats the middle
  initial, and the two John M Radaszewski candidates contain a fixed-width
  surname spacing artifact. Army occupation codes were not treated as employers
  or immediate affiliations.
- Twenty-one people now have the terminal status "requires_archival_review";
  Akeley P Quirk and Gregory L Rabassa have "occupation_only_found".

## Historical outcomes

- The State Bar of California record, the unusual full name, the indexed naval
  rank, and a citation to Akeley P Quirk's first-person USNR memoir support a
  high-confidence identity. His May 1935 California bar admission establishes
  prewar attorney status but not a named employer, law firm, or immediate
  pre-OSS role.
- Official U.S. Copyright Office/Library of Congress evidence identifies
  Gregory L Rabassa as a Dartmouth student who enlisted in the Army in 1942 and
  served as an OSS cryptographer. Dartmouth is modeled as student status, not
  employment; the Army is modeled separately as the immediate military pathway.
  No civilian employer before enlistment was established.
- An official U.S. Army Special Operations history independently identifies
  Melbourne L Rackett with OSS Detachment 101 in Burma in early 1944. This
  confirms wartime identity and OSS context but does not establish a pre-OSS
  employer or predecessor assignment.
- Official Army bulk evidence supports high-confidence identity matches for
  Alex Radak, Carl H Raab, Carlo A Racano, Edward J Rada, Frank D Quisenberry,
  Gregory L Rabassa, John M Radaszewski, Maurice A Quirk, Melbourne L Rackett,
  and Simon Rad. It supports identity and military service only.
- No new verified civilian employer claim was added. Profiles without reliable
  employment evidence explicitly direct researchers to the indexed personnel
  files rather than implying that no prior employment existed.

## Exact coverage after Batch 784

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,032/23,939 (46.0838%).
- Verified-employer coverage: 358/23,939 (1.4955%).
- Verified-affiliation coverage: 803/23,939 (3.3544%).
- Archival-review coverage: 9,491/23,939 (39.6466%).
- Not started: 12,902.
- Possible duplicate groups: 547; conflicts: 373.
- Claims: 1,411 confirmed; 3,417 high; 1,604 medium; 202 low; 323
  conflicting; two unresolved.
- Citations: 5,997 records representing 3,102 unique source documents.
- Public data: 2,599 published affiliations, 929 organizations, 4,772 public
  sources, and 6,751 published claims.

## Durable inputs and replay

The reviewed identity decisions are stored in
"research/identity_review_decisions_2026-10-13_batch784.csv"; the evidence,
claims, source metadata, person updates, and terminal manual attempts are stored
in
"research/evidence-page382-quintrell-radaszewski-review_batch-784_2026-10-13.json".
Both files validate and replay idempotently through the normal pipeline.

Resume new-person research at PDF page 382, row 25, Edwin R Raddatz. Full-index
historical research remains unfinished; 12,902 active people are still
"not_started".
