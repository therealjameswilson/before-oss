# Batch 561 discovery checkpoint

Date: 2026-09-16 UTC

## Cohort

Personnel-index PDF page 112 rows 40-46 and page 113 rows 1-3:

1. George C Demas, Box 179
2. John Demas Jr., Pfc, Box 179
3. Samuel F Demastrie, Box 179
4. Joseph A Dematteo, Box 179
5. Priscilla DeMauduit, Box 179
6. Anthony DeMayo, Box 179
7. Gertrude J Dembe, Box 179
8. Fernando DeMello, Box 179
9. Gilbert Dementis, Box 179
10. Leon M Demers, Box 179

All rows remain at archival location `230/86/29/07`. Both complete source
pages were rendered at 180 dpi and visually inspected. Original spelling,
capitalization, initials, rank, box and blank fields remain recoverable. Five
printed private values are preserved only in the private database and masked
in every public artifact. Leon M Demers's seven-digit value remains exactly as
printed; it is neither padded nor silently corrected.

## Adapter and source work

- CIA Reading Room: ten bounded exact-name OSS searches completed; no candidate
  was accepted.
- Library of Congress: ten bounded employment and occupation searches
  completed; no candidate was accepted.
- Web: ten staged query plans were saved before exact-name, punctuation,
  employment, institutional, obituary, directory, newspaper and archival
  review. Follow-up exact-name searches found no defensible pre-OSS employer.
- Army merged file: the complete 9,200,232-row file was scanned. Protected
  identifiers and every indexed name element agree for John Demas Jr., Joseph
  A Dematteo and Gilbert Dementis. Joseph's exact identifier selects the `De
  Matteo` spacing variant; a same-name row with another identifier is rejected.
  Samuel F Demastrie's identifier maps to a differently named entrant and no
  exact-name row, so the conflict remains explicit and no subject data is
  transferred. Anthony DeMayo and Leon M Demers each have one exact-name row,
  but name alone is insufficient; Leon's printed seven-digit value cannot be
  used for strict matching. George C Demas, Priscilla DeMauduit, Gertrude J
  Dembe and Fernando DeMello have no exact-name Army row. No raw Army row, full
  identifier or unrelated identity entered tracked artifacts.
- Army code list: Code No. 30 physical pages 173 and 304 were rendered at 180
  dpi and visually inspected. Codes 4-75 and 9-92 denote Machinists and
  Students. These are occupation or status categories, not employers.
- NARA Catalog API: no authenticated request was made. No credential, request
  header, raw live response or full private identifier entered the repository.

## Accepted outcomes

### Identifier-confirmed Army identities and statuses

Exact protected-identifier and normalized-name agreement confirms John Demas
Jr., Joseph A Dematteo and Gilbert Dementis as Army-file matches and Army
privates. Their Army-entry records support only these qualified categories:

- John Demas Jr.: student, 29 March 1943;
- Joseph A Dematteo: machinist, 17 November 1942;
- Gilbert Dementis: student, 10 April 1944.

No record names a school, employer, workplace, trade specialty or immediate
Army-to-OSS transition. The findings are medium-confidence, strongly
date-bounded affiliations excluded from verified-employer counts. Student is
modeled as `student`, never employment.

## Conflict and unresolved outcomes

- Samuel F Demastrie ends in `conflicting_sources` at critical archival
  priority. The unrelated Army identity and its subject details remain private;
  Box 179 and the original Army card must be compared.
- Leon M Demers remains unresolved because the source's seven-digit value
  cannot authorize a strict identifier match. The name-only candidate's
  footwear occupation is withheld.
- George C Demas, Priscilla DeMauduit, Anthony DeMayo, Gertrude J Dembe and
  Fernando DeMello remain unresolved. Anthony's separately documented
  pathfinder namesake and all other name-only candidates are rejected.
- Every unresolved profile directs researchers to Box 179. The absence of an
  accessible result is not treated as evidence that no prior employment
  existed.

## Evidence package

- `research/evidence-pages-one-hundred-and-twelve-and-thirteen-george-c-demas-through-leon-m-demers-pathways_batch-561_2026-09-16.json`
- `research/batch-561-discovery-checkpoint.md`
- `site/tests/batch561.spec.ts`

The reviewed bundle contains four sources, three affiliations, seventeen
claims, twenty-seven claim-source links, ten person updates and twenty
review/synthesis attempts. Together with thirty adapter attempts, the cohort
adds fifty durable attempts. All ten people receive five attempts and leave
`in_progress`; three end `occupation_only_found`, one ends
`conflicting_sources`, and six require archival review.

## Next cohort

After release, resume with personnel-index PDF page 113 rows 4-13, Lawrence G
Demgen through John J DeMoore. Preserve the printed source sequence and render
the complete page before research.
