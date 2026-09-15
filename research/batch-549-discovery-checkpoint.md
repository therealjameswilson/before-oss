# Batch 549 discovery checkpoint

Date: 2026-09-15 UTC

## Cohort

Personnel-index PDF page 110, rows 12-21:

1. George L DeCoster, `2nd Lt`, Box 176
2. Calvin C DeCray, `2nd Lt`, Box 176
3. Jehan DeCrequy, `S/Lt`, note `French`, Box 176
4. Fiore DeCristoforo, Box 176
5. Nicholas G D'Ecsery, Box 176
6. Leonard Decunha, Box 176
7. Charles J DeDero, Box 176
8. John Dedes, Box 176
9. E T Deerfield, Box 176
10. Joseph L Dees, Box 176

All ten rows remain at archival location `230/86/29/07`. The source page was
rendered and visually inspected at original resolution. Six printed private
values are preserved privately and masked publicly. The source spelling
`D'Ecsery`, Jehan DeCrequy's `S/Lt` rank and literal `French` note, and the
initial-only `E T Deerfield` name remain recoverable without silent expansion.

## Adapter work

- CIA Reading Room: ten exact-name and meaningful-variant searches, zero
  candidate matches and zero adapter errors.
- Library of Congress: ten current-API searches. Five candidates returned for
  E T Deerfield and were rejected through the imported review workflow. The
  newspaper pages use Deerfield as a Massachusetts or Florida place name or as
  a Maryland telephone exchange; none identifies a person named E T Deerfield.
  The other nine checks returned no candidates. A transient incomplete response
  on the first E T Deerfield request was retried successfully and did not create
  a duplicate attempt.
- Web: ten query plans were preserved in dry-run form, followed by targeted
  manual review of exact-name, rank, military, institutional, newspaper,
  obituary, directory, genealogy and archival results. A Columbia College Class
  of 1944 George L. DeCoster namesake lacked any OSS, Box 176, branch or
  identifier bridge and was rejected. Search-result snippets were never
  accepted as evidence.
- Army merged file: one complete 9,200,232-row scan. Four eight-character
  protected identifiers were eligible for strict comparison. Three produce
  exact identifier and normalized-name matches under transparent spacing or
  punctuation variants. The fourth selects `De Fero Charles J`, conflicting
  with the indexed `DeDero Charles J`; no Army occupation or other personal
  detail is assigned to Charles pending archival review.
- Army code list: physical PDF pages 171, 172 and 177 were rendered at 180 dpi
  and visually inspected. They decode the three accepted occupation values as
  `Financial institution clerks, n. e. c.`, `Kitchen workers in hotels,
  restaurants, railroads, steamships, etc., n. e. c.`, and `Laundering
  occupations, apparel and other articles`. These broad categories name no
  employer.
- NARA Catalog API: no authenticated request because no local key was available.
  The official bulk Army file and public Catalog citation pointers were used
  without retaining API payloads.

## Accepted outcomes

### Fiore DeCristoforo

The protected index identifier selects one official Army row under the spaced
surname variant `Fiore De Cristoforo`, confirming the identity and August 27,
1943 Army entry. The official code table supports only the broad civilian
category `Laundering occupations, apparel and other articles`. It is published
at medium confidence as a qualified occupation, not an employer, immediate OSS
predecessor or last civilian employer.

### Nicholas G D'Ecsery

The protected identifier selects one Army row under the punctuation-normalized
variant `Nicholas G Decsery`, confirming the identity and September 26, 1941
Army entry. The official code table supports the broad civilian category
`Kitchen workers in hotels, restaurants, railroads, steamships, etc., n. e.
c.` The qualified occupation is published at medium confidence without a named
employer or OSS-transition inference.

### Leonard Decunha

The protected identifier selects one Army row under the spaced surname variant
`Leonard De Cunha`, confirming the identity and April 20, 1943 Army entry. The
official code table supports the broad civilian category `Financial institution
clerks, n. e. c.` The qualified occupation is published at medium confidence
without naming a financial institution or an OSS transition.

## Unresolved and conflicting outcomes

- George L DeCoster and Calvin C DeCray remain unresolved and require high-
  priority Box 176 review. Their printed `2nd Lt` ranks support the commissioned
  Army classification but do not identify an employer. Their shorter protected
  values were not forced into an enlisted-accessions match.
- Jehan DeCrequy remains unresolved and requires critical archival review. The
  printed `S/Lt` and `French` fields support a foreign or Allied commissioned-
  personnel classification, but the abbreviation is not silently expanded and
  no namesake biography is assigned.
- Charles J DeDero is `conflicting_sources`: the protected identifier selects an
  official Army row under `Charles J De Fero`. The substantive surname conflict
  is public, excluded from default analytics and routed to critical Box 176
  review. The candidate's occupation and other nonessential details are withheld.
- John Dedes and Joseph L Dees are `no_reliable_result_after_protocol`. Common-
  name candidates lacked an OSS, Box or corroborating-identifier bridge.
- E T Deerfield remains `requires_archival_review`. Both given names are
  abbreviated, and all five newspaper candidates were place-name or telephone-
  exchange collisions. Critical Box 176 review is the next step.

## Evidence package

- `research/evidence-page-one-hundred-and-ten-george-l-decoster-through-joseph-l-dees-pathways_batch-549_2026-09-15.json`
- `research/loc_review_decisions_2026-09-15_batch549.csv`
- `research/batch-549-discovery-checkpoint.md`
- `site/tests/batch549.spec.ts`

The reviewed bundle contains three sources, no organizations, three
affiliations, seven claims, fourteen claim-source links, ten person updates and
twenty review/synthesis attempts. Together with the thirty adapter attempts,
every cohort person has five durable attempts. Evidence import and LoC-review
import are idempotent and were each verified through consecutive imports.

## Next cohort

Resume with personnel-index PDF page 110 rows 22-31, Kathleen M Dees through
Serge Defleury, all in Box 176 at archival location `230/86/29/07`. Render and
inspect the source region before research; preserve the indexed spelling
`Slyvester S Defazio`, Maurice Defenin's `Lt` and `French` fields, and all
unfamiliar names exactly.
