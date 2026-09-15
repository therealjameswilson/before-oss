# Batch 535 discovery checkpoint

Run date: 2026-09-14 ET / 2026-09-15 UTC

## Cohort

Personnel-index PDF page 107 rows 10-19, Charlotte M Davis through the
indexed spelling Emiliy C Davis. The first nine rows are in Box 169 and Emiliy
C Davis is in Box 170, all at location 230/86/29/06. The index page was
rendered and visually inspected before research. The spelling `Emiliy` is
preserved as printed; `Emily` was used only as a labeled search alias.

## Bounded discovery completed

- Ten CIA Reading Room adapter checks completed with zero candidates or
  errors.
- Sixteen current Library of Congress query attempts completed with 45
  candidates. A transient incomplete-response error interrupted the first
  pass; the resumable adapter reused six completed fingerprints and finished
  without duplicating them. All 45 candidates were reviewed in official item
  or full-text context and rejected through the durable, idempotent review
  workflow.
- The complete 9,200,232-row Army merged file was scanned transiently. David
  M Davis has the sole exact private-identifier and exact-name match; his Army
  row records entry on December 15, 1942, as private. Full identifiers and raw
  Army rows were not retained.
- Thirteen other exact-name David M Davis Army rows carry different
  identifiers. Seven Cleveland Davis, five Curtis C Davis, sixteen David R
  Davis and two Dorothy Davis name-only rows remain unassigned. Curtis C
  Davis's six-character protected value was not compared with the Army
  file's eight-digit identifier position. Army non-hits are not treated as
  negative proof.
- The historical Army occupation value `944` was checked against NARA's Code
  No. 30 table. Physical PDF page 174 was rendered and visually inspected:
  the table defines `5-44` and `7-44` as railroad switchmen but not `9-44`.
  The value is therefore preserved as undefined and no occupation is
  published.
- Exact-name OSS, employment, occupation, obituary, institutional,
  newspaper, directory, military and archival searches used meaningful name
  and initial variants. Results were modern people-finder pages, unrelated
  obituaries, mismatched initials or ages, or common-name records without a
  Box 169/170 or OSS bridge. Sensitive people-finder details were neither
  retained nor published.
- No authenticated NARA Catalog API request was made because no local key was
  available. The official NARA index, Army bulk data and Army technical
  documentation remained the authoritative starting points.

## Reviewed outcomes

- David M Davis has a confirmed Army identity from exact private-identifier
  and full-name agreement. His enlisted status, private grade and Army entry
  date are retained, but value `944` is not decoded and no occupation or
  employer claim is created. Box 169 remains required to resolve the original
  occupation wording and Army-to-OSS chronology.
- Charlotte M Davis, Cleveland Davis, Cora J Davis, Curtis C Davis, David R
  Davis, Doris Davis, Dorothy Davis, Elizabeth T Davis and Emiliy C Davis
  remain unresolved after the minimum protocol. Their profiles preserve
  candidate-rejection reasons and Box 169/170 archival guidance.
- No common-name Army row, 1941 Dorothy Davis byline, compatible-initial birth
  or burial index, modern biography, or spelling-expanded `Emily` candidate is
  assigned without corroborating identifiers.

## Durable artifacts

- `research/evidence-page-one-hundred-and-seven-charlotte-m-davis-through-emiliy-c-davis-pathways_batch-535_2026-09-14.json`
- `research/loc_review_decisions_2026-09-14_batch535.csv`
- `tmp/scan_army_batch.py`
- `tmp/b535_review_loc.py`
- `tmp/pdfs/batch534/index-107.png`
- `tmp/pdfs/batch535/code-174.png`

The reviewed bundle contains three sources, no organization or affiliation
records, one identity claim, two claim-source links, ten person updates and
ten synthesized terminal research outcomes. It validates and imports
idempotently. The durable LoC review import accepts 45 decisions and skips all
45 as duplicates on a second run.

## Coverage after import

- Index coverage: 23,978 of 23,978 source rows linked (100%).
- Research-attempt coverage: 5,118 of 23,940 active people (21.3784%).
- Verified-affiliation coverage: 569 of 23,940 (2.3768%).
- Verified-employer coverage: 253 of 23,940 (1.0568%).
- Archival-review coverage: 5,073 of 23,940 (21.1905%).
- Remaining `not_started`: 18,822.

## Resume boundary

Resume with personnel-index PDF page 107 rows 20-29: Emiscah Davis, Eugene M
Davis, Eugenia C Davis, Farrell J Davis, Foster E Davis, Fred C Davis, Gerald
W Davis, Grover C Davis, Horace B Davis and Howard Davis. All ten rows are in
Box 170 at location 230/86/29/06. Gerald W Davis retains the indexed `Maj`
rank without an external identity claim; the private values for Eugene M,
Fred C, Horace B and Howard Davis require protected handling.
