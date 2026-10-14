# Batch 798 research progress

Date: 2026-10-14 America/New_York

## Scope and preservation

Batch 798 covers PDF page 389, rows 1-23, John V Rentzeperis through Evelyn
Reyer. All 23 printed rows remain preserved as distinct source records linked
to 23 person entities. Page 389 was inspected against a 300 dpi render before
research. The next unresearched boundary is PDF page 389, row 24, Benjamin P
Reyes.

The printed spelling `Robe R Reubell`, the displaced `Capt` value on the Carlo
Resio row, and the clipped notes `photogra`, `Extract fr`, `Record`, and
`fingerpri` remain recoverable exactly as printed. The displaced value was
reviewed without rewriting the immutable raw row. Full service identifiers
remain private.

## Research protocol and review

- NARA index and Army context, exact-name OSS searches, employment and
  occupation searches, official and institutional sources, and newspaper,
  directory, obituary, and archival searches were reviewed for all 23 people.
  NARA live API access was not available because the key was absent from the
  runtime; the adapter failed closed without sending a request. CIA direct
  access was disallowed by robots policy, and Library of Congress checks
  produced no additional publishable employer evidence before a later timeout.
  These access limits were recorded and were not treated as negative historical
  evidence.
- Ten candidate decisions were recorded. Eight Army matches were accepted for
  identity only, one same-identifier spelling conflict was retained without a
  merge, and one wholly different Army name was rejected.
- Maurice H Rettersmann and Maurice H Rottersmann share a protected identifier
  but have different printed surnames, boxes, and grades. Both rows and person
  entities remain separate pending a two-file archival comparison.
- William Reuff's printed protected identifier points to an Army bulk-data row
  for Richard V Goldie. The mismatch remains a visible conflict; no identity or
  employer was assigned.
- All 23 people now have terminal research outcomes: 20 require archival
  review, two have conflicting sources, and one has a documented prewar
  employer. Qualified medium-confidence findings remain excluded from default
  verified-employer analytics.

## Historical outcomes

- Official ODNI counterintelligence history identifies Carlo Resio as chief of
  the Italian Naval Intelligence Service when he approached OSS X-2 in November
  1944 and as the pre-armistice head of SIS Section D. The Italian Naval
  Intelligence Service is published as his high-confidence immediate military
  affiliation, not as a civilian employer.
- An official CIA history identifies T/4 Robert T. Reppenhagen as a member of
  the OSS Blackberry Mission. This supports identity and OSS service only; it
  supplies no pre-OSS employer.
- New York's official 1940 Adjutant General report lists Lieutenant Colonel
  Alfred D. Reutershan as the 27th Division chemical officer. The 27th Division
  is published as an earlier documented military assignment, not as an
  immediate predecessor or civilian employer.
- Contemporary Dartmouth records and official Army data provide a continuous
  identity chronology for John Rexford. Dartmouth College is published as
  student status. German-language study in the Army Specialized Training
  Program at Fordham is a qualified, medium-confidence probable immediate
  military assignment, not Fordham employment.
- Glenville State College's institutional newspaper states that Vorley M
  Rexroad first taught history and geography at Cowen High School, entered the
  Army Air Corps in 1941, served as a training-center instructor, and was then
  selected for OSS in November 1943. The training center is published as his
  high-confidence immediate military affiliation. Cowen High School is his
  best-supported last civilian employer at medium confidence and remains
  visibly qualified.
- French Service historique de la Defense records and a mission compilation
  identify the indexed Rene Reverett as Rene Reveret of the OSS Sussex Jeanne
  team, with aliases Rene Duvallet and Ramadier. This supports identity only;
  no pre-OSS employer has been established.

## Exact coverage after Batch 798

- Index coverage: 23,978/23,978 linked source rows (100%).
- Active person entities: 23,939.
- Research-attempt coverage: 11,344/23,939 (47.3871%).
- Verified-employer coverage: 368/23,939 (1.5372%).
- Verified-affiliation coverage: 818/23,939 (3.4170%).
- Archival-review coverage: 9,805/23,939 (40.9583%).
- Not started: 12,590.
- Possible duplicate groups: 550; conflicts: 390.
- Claims: 1,413 confirmed; 3,560 high; 1,615 medium; 202 low; 334
  conflicting; two unresolved.
- Citations: 6,072 records representing 3,160 unique source documents.
- Public data: 2,632 published affiliations, 947 organizations, 4,847 public
  sources, and 6,918 published claims.
- Total saved research attempts and plans: 21,835.

## Durable inputs and replay

Reviewed candidate decisions are stored in
`research/identity_review_decisions_2026-10-14_batch798.csv`; evidence, claims,
source metadata, person updates, and terminal attempts are stored in
`research/evidence-page389-rentzeperis-reyer-review_batch-798_2026-10-14.json`.
Both were replayed through the normal import commands to verify idempotence.

Resume new-person research at PDF page 389, row 24, Benjamin P Reyes.
Full-index historical research remains unfinished; 12,590 active people are
still `not_started`.
