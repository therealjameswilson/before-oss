# Batch 548 discovery checkpoint

Date: 2026-09-15 UTC

## Cohort

Personnel-index PDF page 110, rows 2-11:

1. Edmund J Decaussin Jr., Box 175
2. Eugene Dechelette, Col, Box 175
3. Pierre F D'Echert, Box 176
4. Jean DeChezelles, Col, note `Alias Fa`, Box 175
5. Jorg DeChochor, Box 175
6. Anthony J DeCicco, Box 175
7. Joseph G Decicco, Box 175
8. Ha Deck, Box 175
9. Robert Deckelbaum, Box 175
10. Francis E Decker, Box 175

The source page was rendered and visually inspected at original resolution.
Pierre F D'Echert's Box 176 / `230/86/29/07` boundary remains distinct from
the nine Box 175 / `230/86/29/06` rows. Six printed private values are
preserved privately and masked publicly. `Ha Deck` remains literal as an
incomplete or uncertain given name. Jean DeChezelles's truncated `Alias Fa`
note is preserved without expansion.

## Adapter work

- CIA Reading Room: ten exact-name and meaningful-variant searches, zero
  candidate matches and zero adapter errors.
- Library of Congress: ten current-API searches. One candidate returned for Ha
  Deck and was rejected through the imported review workflow: a September 23,
  1948 *Montana labor news* page is postwar and supplies no personal-name, OSS,
  Box, identity or employment context. The remaining checks returned no
  candidates or errors.
- Web: ten query plans preserved in dry-run form, followed by targeted manual
  review of institutional biography, military, newspaper, obituary, directory,
  genealogy and archival results. Search-result snippets were never accepted as
  evidence.
- Army merged file: one complete 9,200,232-row scan. Four protected identifiers
  were eligible for strict comparison. Three produce exact identifier and
  normalized-name matches under transparent surname-spacing variants. Francis
  E Decker's identifier produces no match; an exact-name Army row carries a
  different private identifier and was rejected rather than merged.
- Army code list: physical PDF pages 171, 174 and 175 were rendered and visually
  inspected. They decode the three matched civilian-occupation values as
  `Agents and appraisers, n. e. c.`, `Occupations in manufacture of automobiles,
  n. e. c.` and `Mechanics and repairmen, n. e. c.` These broad categories name
  no employer.
- NARA Catalog API: no authenticated request because no local key was available.
  The official bulk Army file and public Catalog citation pointers were used
  without retaining API payloads.

## Accepted outcomes

### Edmund J Decaussin Jr.

The protected index identifier selects one official Army row under the
transparent spacing variant `Edmund J De Caussin`, confirming the identity.
The row dates Army entry to December 14, 1942, and the official code table
supports only the broad civilian category `Occupations in manufacture of
automobiles, n. e. c.` It is published at medium confidence as a qualified
occupation, not an employer, immediate OSS predecessor or last civilian
employer.

### Eugène Déchelette

The official Ordre de la Libération biography supplies the rare exact name,
French reserve-officer status, Free French and BCRA intelligence chronology
that align with the indexed Eugene Dechelette, Col. Identity is high confidence.
The biography places his employment and later administrative role at the
family textile company S.A. Déchelette-Despierres in Roanne before his August
1939 military mobilization. That company is published at high confidence as
his last civilian employer before wartime service. It is not called his
immediate pre-OSS affiliation because the biography does not date or define
the relationship that caused the OSS personnel file to be opened.

### Jorg DeChochor

The protected identifier selects one Army row under `Jorg De Chochor`,
confirming the identity and January 27, 1942 Army entry. The official code list
supports the broad civilian category `Agents and appraisers, n. e. c.` The
qualified occupation is published at medium confidence without an employer or
immediate-OSS inference.

### Joseph G Decicco

The protected identifier selects one Army row under `Joseph G De Cicco`,
confirming the identity and February 16, 1942 Army entry. The official code
list supports the broad civilian category `Mechanics and repairmen, n. e. c.`
The qualified occupation is published at medium confidence without naming an
employer or an OSS transition.

## Unresolved and ambiguous outcomes

- Pierre F D'Echert, Anthony J DeCicco and Robert Deckelbaum are
  `no_reliable_result_after_protocol`. Modern, postwar, genealogy and common-name
  candidates lacked the required OSS, Box or corroborating-identifier bridge.
- Jean DeChezelles remains `requires_archival_review`. The printed Colonel rank
  remains visible; nationality is not inferred, results for Yves Dechezelles
  were rejected, and the literal `Alias Fa` note needs critical Box 175 review.
- Ha Deck remains `requires_archival_review`. The incomplete name and rejected
  postwar newspaper phrase collision leave critical Box 175 review as the next
  step.
- Francis E Decker remains `needs_identity_review`. The complete Army scan found
  no row with the index identifier. The exact-name Army row with a different
  identifier is not assigned, and no occupation or employer is published.

## Evidence package

- `research/evidence-page-one-hundred-and-ten-edmund-j-decaussin-jr-through-francis-e-decker-pathways_batch-548_2026-09-15.json`
- `research/loc_review_decisions_2026-09-15_batch548.csv`
- `research/batch-548-discovery-checkpoint.md`
- `site/tests/batch548.spec.ts`

The reviewed bundle contains four sources, one normalized organization, four
affiliations, eight claims, fifteen claim-source links, ten person updates and
twenty review/synthesis attempts. Together with the thirty adapter attempts,
every cohort person has five durable attempts. Evidence import and LoC-review
import are idempotent and were each verified through consecutive imports.

## Next cohort

Resume with personnel-index PDF page 110 rows 12-21, George L DeCoster through
Joseph L Dees, all in Box 176 at archival location `230/86/29/07`. Render and
inspect the source region before research; preserve Jehan DeCrequy's `S/Lt`
rank and `French` note literally, retain Nicholas G D'Ecsery's apostrophe, and
do not expand the initial-only `E T Deerfield` name.
