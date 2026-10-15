# Batch 815 research progress

Date: 2026-10-15 America/New_York

## Scope and preservation

Batch 815 covers PDF page 397, rows 24-46, Elizabeth A Rodnick through Bruce
Rogers. All 23 printed rows remain preserved as immutable source records and
map to 23 active person entities. Page 397 was inspected against a 300 dpi
render before research. The next unresearched boundary is PDF page 398, row 1,
Camden L Rogers.

Printed surname variants, initials, military ranks, civilian grades, blank
rank fields, and box numbers remain exact. The printed `S SGT` and `CSK` forms
are preserved while normalized classifications now identify those ranks as
enlisted Army and enlisted naval personnel, respectively. Full service numbers
remain private and are absent from public outputs.

## Research protocol and review

- Every person received NARA index context review, exact-name and meaningful
  variant OSS searches, employment and occupation searches, and applicable
  military, obituary, institutional, newspaper, directory, and archival
  checks.
- The NARA Catalog adapter saved 23 deterministic dry-run plans because no API
  key was present in the local process environment. A bounded CIA Reading Room
  adapter attempt encountered the adapter's current robots-policy limitation,
  and the Library of Congress adapter timed out. Neither access problem was
  treated as historical negative evidence. Targeted manual CIA searches were
  completed for all 23 names.
- Protected-identifier Army matches for Manuel Rodrigues, Harry Rody, William
  G Roessel, Louis C Rofrano, and Albert S Rogers were accepted for identity
  only. Army occupation codes were not published as jobs or employers.
- The Army candidate for Delmar M Roeder shares the private identifier but
  names `CALARY WILLIAM R`. It was rejected rather than merged, and the
  conflicting identity state remains public and reviewable.
- All 23 people now have saved, reviewable, terminal Batch 815 outcomes. The
  previously verified Alfonso Rodriguez profile was re-audited without
  downgrading or duplicating its existing evidence.

## Historical outcomes

- The Farm Credit Administration's contemporary employee periodical identifies
  Lieutenant Colonel Joseph Rodrigo as formerly of the Federal Intermediate
  Credit Bank of Berkeley. The site publishes that institution as his
  strongly date-bounded last civilian employer before wartime military
  service. It does not claim that the bank immediately preceded OSS service or
  invent an unstated job title or departure date.
- The 1939 *Oregana* identifies Bruce Rogers of Newberg as a University of
  Oregon business-administration student and Japan-American Student Conference
  delegate. Student status remains separate from employment.
- Charlotte DeForest's retrospective places Bruce Rogers at the U.S. consulate
  in Osaka during his prewar Japan period, while Lawrence C. Soley's scholarly
  history identifies the Japanese-speaking Bruce Rogers who recruited
  personnel for OSS Morale Operations. The distinctive Oregon-Japan-Osaka-OSS
  path supports a high-confidence identity. The consular assignment is
  published as a qualified, documented prewar government affiliation, not as
  an immediate pre-OSS predecessor.
- A nonofficial Operational Groups roster provides compatible S/Sgt. context
  for Harry Rody but is not used as employer evidence. The official Army
  identifier match is the identity basis.
- Elizabeth Amis Rodnick, Hellmuth Paul Rodrian, Charles E Roethe, and Jose O
  Rodriguez appeared in plausible external records, but none had the required
  OSS, box, or private-identifier bridge. Those candidates remain rejected or
  unresolved rather than being assigned to the index rows.

## Exact coverage after Batch 815

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,938.
- Research-attempt coverage: 11,729/23,938 (48.9974%).
- Verified-employer coverage: 377/23,938 (1.5749%).
- Verified-affiliation coverage: 839/23,938 (3.5049%).
- Archival-review coverage: 10,192/23,938 (42.5767%).
- Not started: 12,204.
- Possible duplicate groups: 553; conflicts: 398.
- Claims: 1,478 confirmed; 3,644 high; 1,637 medium; 202 low; 342
  conflicting; two unresolved.
- Citations: 6,172 records representing 3,235 unique source documents.
- Public data: 2,680 published affiliations, 960 organizations, 4,947 public
  sources, and 7,097 published claims.
- Total saved research attempts and plans: 22,874.

## Durable inputs and replay

Identity decisions are stored in
`research/identity_review_decisions_2026-10-15_batch815.csv`. Evidence, claims,
person updates, rejection reasons, and terminal attempts are stored in
`research/evidence-page397-rodnick-rogers-review_batch-815_2026-10-15.json`.
The evidence import was replayed and retained exactly 23 Batch 815 attempts,
with no foreign-key violations.

Resume new-person research at PDF page 398, row 1, Camden L Rogers. Full-index
historical research remains unfinished; 12,204 active people are still
`not_started`.
