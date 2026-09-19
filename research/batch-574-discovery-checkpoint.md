# Batch 574 discovery checkpoint

Date: 2026-09-19 UTC

## Cohort and extraction

Personnel-index PDF page 115, printed rows 33-42, Frank J Desuta through
Richard B Deufson. All ten rows point to Box 183 at `230/86/30/01`. The full
page was rendered at 180 dpi and visually inspected. The three printed private
identifiers are retained only in the private SQLite source rows and masked in
public projections. The separate adjacent Box 182 Frank J Desota and Box 183
Frank J Desuta entities remain a possible-duplicate group, not a merge.

## Bounded source protocol

- Ten completed CIA Reading Room and ten completed Library of Congress checks
  were persisted. The CIA adapter returned no candidates. The LoC adapter
  returned four Evening Star page leads for Wallace R Deuel; three were
  retained as plausible OCR leads pending original-image inspection, and a
  postwar 1950 item was rejected. None is used as the final employer source.
- Staged exact-name OSS, occupation, employer, newspaper, directory, obituary
  and archival searches were manually reviewed for all ten people. A complete
  9,200,232-record scan of NARA's official Army merged file yielded no
  exact-name cohort match. Two protected identifiers in the printed index led
  to different Army surnames and were rejected; the third had no Army match.
  No Army occupation was assigned on that basis. No authenticated NARA Catalog
  API request was made.
- The Library of Congress Manuscript Division's eleven-page Wallace Rankin
  Deuel finding aid was read in full. Physical pages 3-4 were rendered and
  visually inspected. Its chronology places him at the American University in
  Beirut in 1926-1929, at the Chicago Daily News in 1929-1941, and in wartime
  intelligence thereafter. An independent National Park Service history
  identifies the newspaper correspondent as Wallace R. Deuel and specifies
  that he joined the Coordinator of Information in 1941. This avoids treating
  1941 as an OSS founding date.

## Reviewed findings and exclusions

Wallace R Deuel has a high-confidence identity match and a high-confidence,
strongly date-bounded Chicago Daily News employment pathway through 1941. The
same newspaper is separately recorded as the last documented civilian
employer before his COI/OSS service. Earlier 1926-1929 Beirut teaching is a
different affiliation, not the immediate predecessor. The personnel file
could refine the exact recruitment date, so the claim does not assert that no
short intervening role could have existed.

The other nine people receive terminal `requires_archival_review` outcomes,
with the exact unresolved-employer statement in their public profiles. The
Frank Desuta/Desota spelling pair is not merged. A 1944 Navy-directory lead
for Lloyd Dethlefson is not a named employer. Mary Detmer obituary/genealogy
namesakes are not adopted. Louis Detore and Alan Detweiler postwar jobs are
not projected backward; a wartime Alan Detweiler air-officer lead lacks an OSS
identity bridge. Victor Detibertis and Henry Detmer Army identifier conflicts
remain private review questions, not public identity assertions. Richard
Deufson's indexed private rank does not identify a prior unit.

## Evidence and exact local coverage

- `research/evidence-page-one-hundred-and-fifteen-frank-j-desuta-through-richard-b-deufson_batch-574_2026-09-19.json`
- `research/loc_review_decisions_2026-09-19_batch574.csv`
- `site/tests/batch574.spec.ts`

The reviewed bundle has four source records, two organization records (one
reuses the prior American University of Beirut canonical entity), two
affiliations, thirteen claims, twenty claim-source links, ten person updates
and ten manual review attempts. Four LoC candidate decisions were imported.
The private database contains 23,978 linked source rows, 23,940 active people,
9,978 durable attempts, 2,178 affiliations, 687 organizations, 4,860 citation
records and 2,221 unique source documents. Claims by confidence: 1,307
confirmed, 1,720 high, 1,351 medium, 183 low and 129 conflicting.

- Index coverage: 23,978 / 23,978 source rows linked (100%).
- Research-attempt coverage: 5,505 / 23,940 active people (22.9950%).
- Verified-affiliation coverage: 597 / 23,940 (2.4937%).
- Verified-employer coverage: 261 / 23,940 (1.0902%).
- Archival-review disposition coverage: 5,460 / 23,940 (22.8070%).
- Remaining active `not_started`: 18,435; possible duplicate groups: 256.
- Public output: 2,162 published affiliations, 673 organizations, 3,669
  sources and 4,504 claims.

This cohort supplies a saved research outcome, not a claim that the entire
index has been researched. The next sequential cohort is PDF page 115 rows
43-46 followed by page 116 rows 1-6; continue the bounded protocol and
reconcile the printed-row transition before assigning a new batch.
