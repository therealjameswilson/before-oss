# Batch 547 discovery checkpoint

Date: 2026-09-15 UTC

## Cohort

Personnel-index PDF page 109, rows 38-46, plus page 110, row 1, all in Box
175 at archival location `230/86/29/06`:

1. Michel DeBourbon
2. John W DeBoy
3. George DeBraux
4. Mary E DeBurr
5. William D DeCamp, T/Sgt
6. Michael Decapite
7. Joseph F DeCarli, T-3
8. Rinaldo DeCarolis, note `Italian Ci`
9. Laura F DeCarvalho
10. Louis DeCastro

Both source pages were rendered and visually inspected at original resolution.
Three printed private values are preserved privately and masked publicly. The
truncated `Italian Ci` note remains literal and has not been expanded by
inference.

## Adapter work

- CIA Reading Room: ten exact-name and meaningful-variant searches, zero
  candidate matches and zero adapter errors.
- Library of Congress: ten current-API searches across exact names and selected
  variants, zero accepted candidates and zero adapter errors.
- Web: ten query plans preserved in dry-run form, followed by manual review of
  veteran oral history, contemporary press, institutional literary history,
  military-roster, art-archive, obituary, directory and newspaper results.
- Army merged file: one complete 9,200,232-row scan. Three protected identifiers
  were eligible for strict comparison. Two produce exact identifier and
  normalized-name matches; one selects a record with a different middle initial.
  Full identifiers, raw rows and unrelated personal details remain withheld.
- Army code list: physical PDF page 170 was rendered and visually inspected. It
  decodes civilian occupation code 006 as the broad category `Authors, editors,
  and reporters`. Joseph F DeCarli's occupation value could not be decoded from
  the reviewed list and was not guessed or published.
- NARA Catalog API: no authenticated request because no local key was available.
  The official bulk Army file and public Catalog citation pointers were used
  without retaining API payloads.

## Accepted outcomes

### Michel DeBourbon

The Washington Post and Legasee Educational Trust independently identify
Prince Michel de Bourbon-Parma, document the wartime form `Michel Bourbon`,
and describe the same Fort Benning-to-OSS sequence. The Washington Post places
William Casey's OSS invitation immediately after Michel's commissioning
ceremony; Legasee independently records the American Army, Fort Benning,
second-lieutenant status and recruitment by Casey. The indexed identity is
high confidence. The United States Army is published as an
`explicit_immediate` military assignment, not a civilian employer. No last
civilian employer or school-as-employer claim is inferred.

### Michael Decapite

The protected index identifier selects one official Army row under the
transparent spacing variant `Michael De Capite`, confirming the index identity.
The record places Army entry as a private in December 1944 and carries civilian
occupation code 006. An official code list identifies that broad category as
authors, editors and reporters. A contemporary September 1940 Ukrainian Weekly
notice identifies Michael De Capite as the author of a contribution to the
first issue of *Common Ground*, and CUNY's Italian American Studies Open
Syllabus identifies his 1943 novel *Maria*. Authorship and the Common Ground
professional affiliation are published at high confidence, but the periodical
is not called his employer and the sequence relative to OSS remains explicitly
uncertain.

### Joseph F DeCarli

The protected index identifier selects one official Army row under normalized
spacing `Joseph F De Carli`, confirming the identity. The Army record dates
entry as a private in January 1943; the index later prints rank T-3. No reliable
employer or occupation was found. The source occupation value was not decoded,
and OSS Operational Group results for differently named people were rejected.
Box 175 remains necessary for the Army-to-OSS sequence.

## Unresolved, ambiguous and conflicting outcomes

- John W DeBoy remains `conflicting_sources`: the protected identifier selects
  a normalized De Boy Army row whose middle initial is M rather than the index's
  W. Surname spacing was normalized; the substantive initial discrepancy was
  not. The unrelated identity and occupation details remain withheld.
- William D DeCamp remains `needs_identity_review`. A New York State Military
  Museum roster contains a same-name sergeant with compatible wartime service,
  but name and rank alone do not satisfy the common-name identity rule. The
  candidate is not published as his military assignment or employer.
- George DeBraux, Mary E DeBurr, Laura F DeCarvalho and Louis DeCastro remain
  `no_reliable_result_after_protocol`. Postwar or uncontextualized namesakes
  were rejected rather than projected backward.
- Rinaldo DeCarolis remains `requires_archival_review`. The literal truncated
  note `Italian Ci` needs Box 175 interpretation before nationality, civilian
  status or another category can be assigned.

## Evidence package

- `research/evidence-page-one-hundred-and-nine-through-one-hundred-and-ten-michel-debourbon-through-louis-decastro-pathways_batch-547_2026-09-15.json`
- `research/batch-547-discovery-checkpoint.md`
- `site/tests/batch547.spec.ts`

The reviewed bundle contains seven sources, two normalized organizations, two
affiliations, six claims, fifteen claim-source links, ten person updates and
twenty review/synthesis attempts. Together with the thirty adapter attempts,
every cohort person has five durable attempts. Import is idempotent and was
verified by two consecutive imports.

## Next cohort

Resume with personnel-index PDF page 110 rows 2-11: Edmund J Decaussin Jr.
through Francis E Decker. Render and inspect the source region before research,
preserve the incomplete `Ha Deck` row and truncated `Alias Fa` note literally,
and keep Pierre F D'Echert's Box 176/location boundary distinct from the Box 175
rows.
