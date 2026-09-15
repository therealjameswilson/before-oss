# Batch 536 discovery checkpoint

Run date: 2026-09-15 UTC

## Cohort

Personnel-index PDF page 107 rows 20-29, Emiscah Davis through Howard Davis.
All ten rows are in Box 170 at location 230/86/29/06. The page was rendered
and visually inspected before research. Four printed private values remain in
the protected database and appear only as masked suffixes in public data.

## Bounded discovery completed

- Ten CIA Reading Room adapter checks completed with zero candidates or
  errors.
- Forty current Library of Congress query attempts completed with 114 unique
  candidates across employment, occupation, obituary and biography query
  families. One transient incomplete-response error was resumed by request
  fingerprint. Direct official-item review reached 107 candidates before the
  service returned HTTP 429; the remaining seven Howard Davis candidates were
  screened through their public LoC/search context and rejected. All 114
  decisions were imported durably; a second import skipped all 114 as
  duplicates.
- The complete 9,200,232-row Army merged file was scanned transiently. Fred C
  Davis and Howard Davis each have one strict exact-private-identifier and
  exact-name match. The Army rows record entry as private on June 9, 1943,
  and March 20, 1941, respectively, with civilian-occupation value `226`.
  Full identifiers and raw Army rows were not retained.
- Thirteen exact-name Fred C Davis rows and 36 exact-name Howard Davis rows
  were found in total; all nonmatching identifiers remain unassigned. Name-
  only Army results for Eugene M, Farrell J, Foster E, Gerald W, Grover C and
  Horace B Davis likewise remain unassigned. Eugene's shorter protected value
  and Horace's alphanumeric value were ineligible for the strict digit-only
  Army comparison. Army non-hits are not treated as negative proof.
- NARA's official Code No. 30 table defines `2-26` as “Cooks, except private
  family.” Physical PDF page 172 was rendered and visually inspected. The
  historical entry-time occupation is published with medium confidence for
  Fred and Howard, but no employer, establishment, household, work location,
  self-employment, or immediate OSS predecessor is inferred.
- Exact-name OSS, employment, occupation, obituary, institutional,
  newspaper, directory, military and archival searches used meaningful name
  and initial variants. No candidate supplied an adequate Box 170 or OSS
  identity bridge.
- No authenticated NARA Catalog API request was made because no local key was
  available. The official NARA index, Army bulk data and Army technical
  documentation remained the authoritative starting points.

## Reviewed outcomes

- Fred C Davis and Howard Davis have confirmed Army identities from exact
  protected-identifier and name agreement. Each has a qualified entry-time
  occupation finding, not an employer finding. Their profiles direct further
  work to Box 170 for employer, Army unit, OSS role and chronology.
- Gerald W Davis remains an unresolved external identity. The public profile
  faithfully preserves the index-derived `Maj` rank and commissioned Army
  classification without assigning any of seven Army namesakes or a postwar
  Fort Myers source credit.
- Horace B Davis remains unresolved. Sources for Horace Bancroft Davis describe
  Federated Press, Simmons College and CIO News roles, but none connects that
  person to the protected value, Box 170 or OSS; those leads are rejected and
  no affiliation is published.
- Emiscah Davis, Eugene M Davis, Eugenia C Davis, Farrell J Davis, Foster E
  Davis and Grover C Davis also remain unresolved after the minimum protocol.
  Their profiles preserve candidate-rejection reasons and Box 170 archival
  guidance.
- A newspaper title associating a Howard Davis with the Florida-Georgia News
  is not assigned to the exact-identifier Army match; the evidence supplies no
  identity bridge and conflicts with neither the documented Army-entry
  occupation nor the project's no-employer finding.

## Durable artifacts

- `research/evidence-page-one-hundred-and-seven-emiscah-davis-through-howard-davis-pathways_batch-536_2026-09-15.json`
- `research/loc_review_decisions_2026-09-15_batch536.csv`
- `tmp/scan_army_batch.py`
- `tmp/pdfs/batch534/index-107.png`
- `tmp/pdfs/batch536/code-172.png`

The reviewed bundle contains three sources, no organizations, two occupation
affiliations, four claims, eight claim-source links, ten person updates and ten
synthesized terminal research outcomes. It validates and imports idempotently.

## Coverage after import

- Index coverage: 23,978 of 23,978 source rows linked (100%).
- Research-attempt coverage: 5,128 of 23,940 active people (21.4202%).
- Verified-affiliation coverage: 569 of 23,940 (2.3768%).
- Verified-employer coverage: 253 of 23,940 (1.0568%).
- Archival-review coverage: 5,083 of 23,940 (21.2322%).
- Remaining `not_started`: 18,812.

## Resume boundary

Resume with personnel-index PDF page 107 rows 30-39: Howell A Davis Jr, Hoyt
B Davis, Irvin P Davis, Isabelle M Davis, Jack E Davis, James A Davis, James E
Davis, James M Davis, Jane M Davis and Jean Davis. These rows remain in Box
170 at location 230/86/29/06. Protected values require the established
private-identifier workflow.
