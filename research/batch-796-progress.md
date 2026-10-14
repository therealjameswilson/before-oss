# Batch 796 research progress

Date: 2026-10-14 America/New_York

## Scope and preservation

Batch 796 covers PDF page 388, rows 1-23, Arthur F Reinhardt through Erich M
Remarque. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities. Page 388 was inspected against a 300 dpi render before
research. Arthur F Reinhardt already had a completed reviewed profile; the
other 22 people advanced from `not_started` to terminal attempted outcomes. The
next unresearched boundary is PDF page 388, row 24, Anton H Remenih.

The clipped notes `extract fr`, `photogra`, `French c`, `Certificat`, and
`enlistme` remain exactly as printed and were not silently expanded. `Record`
and `no folder` also remain verbatim. Full service identifiers remain private.

## Research protocol and review

- NARA Catalog and web adapters recorded bounded plans; no live Catalog API
  response body was retained. The CIA and Library of Congress adapters failed
  closed before producing usable results, and those access failures were not
  treated as negative historical evidence.
- Exact-name OSS, employment, occupation, obituary, institutional, newspaper,
  military, variant-name, and archival query families were reviewed for all 23
  people.
- Thirteen Army bulk candidates were manually reviewed. Eleven exact-name,
  nonshared-identifier matches were accepted for identity only. The Morris
  Reisman candidate was rejected because the Army row names Michael M Reece;
  the Herbert G Reller candidate was rejected because the Army row names
  Herbert G Roller. Army occupation codes were not treated as employers.
- All 23 people now have terminal research outcomes. Twenty require archival
  review or preserve explicit conflicts; Arthur F Reinhardt retains a completed
  Air Corps profile, Gilbert J Reiter has a qualified documented prewar
  employer, and Erich Maria Remarque has a verified immediate civilian
  affiliation and earlier employment history.

## Historical outcomes

- Official Army data supports high-confidence identities for Olav S
  Reinholdtsen, Chris Reinisch, Harry Reis, Roy R Reis, Leonard F Reisig, Milton
  Reissman, Gilbert J Reiter, Carl C Reith, John W Reith, and Steve Rejko. An
  official North Dakota roster independently corroborates Chris Reinisch and
  supports Calvin W Reister's identity. These claims establish identity and
  service only unless separately stated.
- A local historical account, used with the official Army match and a reputable
  obituary, identifies Krause's Cafe as Gilbert J Reiter's best-supported last
  civilian employer before Army service. The claim is published visibly
  qualified at medium confidence and is not labeled his immediate pre-OSS
  affiliation.
- A transcribed 1945 award citation identifies Robert Reitzer as a French
  sous-lieutenant serving with OSS. It supports identity but not a pre-OSS
  employer or immediate prior assignment.
- Authoritative USHMM and Erich Maria Remarque Peace Center chronologies place
  Remarque's independent novel writing immediately before work on an OSS
  memorandum in September 1944. Self-employed writing is therefore modeled as
  his best-supported immediate affiliation and last civilian work. His earlier
  employment with *Echo Continental* and *Sport im Bild* is recorded separately
  as documented prewar employment.
- Discovery-only or insufficiently linked leads for Rene C Reitenbach,
  Gertrude M Reith, and Harry Reis were rejected rather than converted into
  employment claims.

## Exact coverage after Batch 796

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,300/23,939 (47.2033%).
- Verified-employer coverage: 366/23,939 (1.5289%).
- Verified-affiliation coverage: 812/23,939 (3.3920%).
- Archival-review coverage: 9,761/23,939 (40.7745%).
- Not started: 12,634.
- Possible duplicate groups: 550; conflicts: 387.
- Claims: 1,413 confirmed; 3,533 high; 1,612 medium; 202 low; 331
  conflicting; two unresolved.
- Citations: 6,056 records representing 3,146 unique source documents.
- Public data: 2,623 published affiliations, 938 organizations, 4,831 public
  sources, and 6,885 published claims.
- Total saved research attempts and plans: 21,673.

## Durable inputs and replay

Reviewed candidate decisions are stored in
`research/identity_review_decisions_2026-10-14_batch796.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page388-reinhardt-remarque-review_batch-796_2026-10-14.json`.
Both were replayed through the normal import commands to verify idempotence.

Resume new-person research at PDF page 388, row 24, Anton H Remenih.
Full-index historical research remains unfinished; 12,634 active people are
still `not_started`.
