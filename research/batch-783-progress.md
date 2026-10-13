# Batch 783 research progress

Date: 2026-10-13 America/New_York

## Scope and preservation

Batch 783 covers PDF page 381, rows 24-46, John P Quertermous through
Waldo S Quinney. All 23 printed rows remain preserved as distinct source
records and are linked to 23 distinct person entities. Page 381 was inspected
against a 300 dpi render before research. The next unresearched boundary is PDF
page 382, row 1, John E Quintrell.

The clipped notes "Extract fr" and "One of t" remain exactly as printed. Neither
was silently expanded or used to infer an employer, unit, or cross-reference.
Full service or officer identifiers remain private and masked in public output.

## Research protocol and review

- NARA Catalog work was dry-run only: 23 distinct planned searches and zero
  authenticated requests. No API key or response was stored.
- CIA Reading Room and Library of Congress adapters each failed closed on the
  first eligible request. These access outcomes are limitations, not negative
  evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  military, variant-name, and archival query families were reviewed for all 23
  people. Namesakes, people-finder records, discovery-only genealogy, postwar
  evidence, and temporally insufficient candidates were rejected.
- Four official Army candidate decisions were reviewed. Three exact-name,
  nonshared protected-identifier matches are durable high-confidence identity
  evidence. One protected-identifier/name discrepancy remains conflicting.
  Army occupation codes were not treated as employers or immediate
  affiliations.
- Twenty-two people now have the terminal status "requires_archival_review";
  Martin S Quigley has "documented_prewar_employer_found".

## Historical outcomes

- Official Army bulk evidence supports high-confidence identity matches for
  John P Quertermous, Glenford Quick, and Timothy B Quill. It supports identity
  and military service only, not a named employer.
- The protected identifier attached to Luther P Quick instead names Quick H R P
  in the Army data. The discrepancy remains a visible conflict, and no Army
  coded fields were transferred.
- A career-directory biography and Martin S Quigley's published first-person
  account establish a high-confidence identity. The directory places him at
  Motion Picture Herald and Motion Picture Daily in 1939-41, followed by the
  Office of the Coordinator of Information in 1942 and OSS in 1943-45. Quigley
  Publishing Company is the normalized last civilian employer; COI is modeled
  separately as the immediate government affiliation.
- A Washington Post obituary probably identifies LaVonne S Quidley and
  documents a federal secretarial job after secretarial school. The obituary
  does not mention OSS, and its War Department attribution is family
  recollection, so the public claim is medium-confidence, visibly qualified,
  and excluded from default employer analytics.
- An official Air Force unit history probably identifies Lt. Col. Robert S
  Quinn as commander of the 50th Fighter Group from 9 November to 1 December
  1943. The source does not establish whether that assignment preceded,
  overlapped, or followed OSS service, so it remains a medium-confidence,
  temporally uncertain military affiliation.
- General William W Quinn, Governor William F Quinn, and Professor Harold Scott
  Quigley were not assigned to incomplete index rows merely because their names
  or wartime work appeared plausible.
- Jean B Quinn and Jean Q Quinn remain separate. Different middle initials,
  grade information, and a clipped note do not justify a merge.

## Exact coverage after Batch 783

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,009/23,939 (45.9877%).
- Verified-employer coverage: 358/23,939 (1.4955%).
- Verified-affiliation coverage: 801/23,939 (3.3460%).
- Archival-review coverage: 9,468/23,939 (39.5505%).
- Not started: 12,925.
- Possible duplicate groups: 547; conflicts: 373.
- Claims: 1,411 confirmed; 3,403 high; 1,604 medium; 202 low; 323
  conflicting; two unresolved.
- Citations: 5,990 records representing 3,097 unique source documents.
- Public data: 2,596 published affiliations, 928 organizations, 4,765 public
  sources, and 6,737 published claims.

## Durable inputs and replay

The reviewed identity decisions are stored in
"research/identity_review_decisions_2026-10-13_batch783.csv"; the evidence,
claims, source metadata, person updates, and terminal manual attempts are stored
in
"research/evidence-page381-quertermous-quinney-review_batch-783_2026-10-13.json".
Both files validate and replay idempotently through the normal pipeline.

Resume new-person research at PDF page 382, row 1, John E Quintrell. Full-index
historical research remains unfinished; 12,925 active people are still
"not_started".
