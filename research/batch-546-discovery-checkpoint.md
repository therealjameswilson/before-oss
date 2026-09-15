# Batch 546 discovery checkpoint

Date: 2026-09-15 UTC

## Cohort

Personnel-index PDF page 109, rows 28-37, all in Box 175 at archival
location `230/86/29/06`:

1. John F Debardeleben
2. Sidney A Debarthy
3. Hans N Debecker
4. Frederick S Debeer Jr.
5. Fritz Debeer
6. Eugene V DeBell
7. Larry V DeBell
8. Rene Debia, Lieutenant, French
9. `* DeBlasi`, note `see file o`
10. Louis D DeBottari

The ten printed rows were rendered from the source PDF and visually inspected
at original resolution. Five printed private values are preserved privately
and masked publicly. The starred DeBlasi entry and its cross-reference note
remain literal.

## Adapter work

- CIA Reading Room: ten exact-name and meaningful-variant searches, zero
  candidate matches and zero adapter errors.
- Library of Congress: current API searches across exact names and selected
  variants; no accepted candidates. Thirteen no-result attempts were created
  during the resumable pass.
- Web: ten query plans preserved in dry-run form, followed by manual review of
  trade, institutional, official French and newspaper sources.
- Army merged file: one complete 9,200,232-row scan. No exact-name rows were
  found. Four eligible protected identifiers each matched a row under a
  different surname; all unrelated identities and row fields remain withheld.
- NARA Catalog API: no authenticated request because no local key was
  available. The official bulk Army file and public Catalog citation pointers
  were used without retaining API payloads.

## Accepted outcomes

### John F Debardeleben

A Worldradio obituary identifies John F. “Tex” DeBardeleben and documents
shipboard radio work, Houston broadcasting, and service with the Federal
Communications Commission's Radio Intelligence Division from the beginning
of World War II. A separate Isthmian Lines crew biography supplies the full
name John Frederick DeBardeleben and corroborates the shipboard and FCC radio
pathway. Identity is high confidence. The FCC assignment is a documented
prewar government affiliation, not a proven immediate predecessor to OSS.
The SS Bessemer City role is published as a qualified earlier occupation; the
legal employer is not inferred.

### Frederick S Debeer Jr. and Fritz Debeer

The National Sporting Goods Association explicitly styles its subject
“Frederick S. (Fritz) deBeer Jr.” A contemporary obituary corroborates the
formal name and Yale 1943 education. This is a strong alias lead for the two
consecutive index rows, but the formal row's private identifier conflicts with
a different Army surname and neither external source supplies an OSS or Box
175 bridge. Both rows remain separate and share only a visible
possible-duplicate group. No school or postwar company is treated as an
immediate pre-OSS affiliation.

### René Débia

The Service historique de la Défense index lists `DEBIA, René`, born 21
September 1911 in Marseille, under `GR 16 P 161919`, with FFC homologation.
The original 823-page PDF was text-searched, physical page 171 was rendered,
and the exact row was visually inspected. An institutional biographical
dictionary supplies René Marie Albert Yves Débia with the same exact birth
details, documents commercial-diplomatic service in Australia in 1930 and
1938, a 1941 chief-of-cabinet post in Hautes-Pyrénées, a 1943 subprefect post
in Prades, and Allied Resistance-network participation. Identity is high
confidence. The 1930-41 posts are qualified documented-prewar government
assignments; the 1943 role remains temporally uncertain relative to OSS.

### Louis D DeBottari

A January 1948 Heinl Radio News Service trade note documents Louis deBottari
at RCA Communications and dates promotions to assistant commercial manager
in 1939 and manager in 1941. The original page was rendered and visually
inspected. A 1965 RCA employee publication lists retired member “deBottari,
Louis D.,” providing the middle-initial bridge. Identity and the documented
prewar RCA employment are high confidence. The evidence does not establish
RCA as the immediate pre-OSS affiliation or last civilian employer.

## Unresolved and conflicting outcomes

- Hans N Debecker, Frederick S Debeer Jr., Eugene V DeBell and Larry V DeBell
  remain `conflicting_sources` because each protected identifier points to a
  different Army surname. The cause is not guessed.
- Sidney A Debarthy remains `no_reliable_result_after_protocol`; his
  seven-character private value was not padded or treated as a strict match.
- `* DeBlasi` remains `requires_archival_review`. No candidate can be selected
  responsibly until the Box 175 `see file o` cross-reference is interpreted.

## Evidence package

- `research/evidence-page-one-hundred-and-nine-john-f-debardeleben-through-louis-d-debottari-pathways_batch-546_2026-09-15.json`
- `research/batch-546-discovery-checkpoint.md`
- `site/tests/batch546.spec.ts`

The reviewed bundle contains ten sources, four normalized organizations, six
affiliations, fourteen claims, thirty-two claim-source links, ten person
updates and ten terminal synthesis outcomes. Import is idempotent and was
verified by two consecutive imports.

## Next cohort

Resume with personnel-index PDF page 109 rows 38-46, Michel DeBourbon through
Laura F DeCarvalho, plus page 110 row 1, Louis DeCastro, after rendering and
visually inspecting both source regions. Preserve every source row and do not
merge normalized-name matches without direct evidence.
