# Batch 450 discovery checkpoint

Date: 2026-09-09
Scope: PDF page 88 rows 32-41, Simone J Companardi through Alfred F Conard
Archive grouping: Box 137; location 230/86/29/01

## Review method

PDF page 88 was rendered at 150 dpi and visually inspected. Every printed name,
initial, rank or blank, private identifier or blank, box, note and location in
the ten-row cohort was compared with the immutable database. Charles R
Compton's six-digit printed value remains literal; it was not padded or treated
as a complete Army identifier. James M Compton's eight-digit identifier remains
private and masked publicly.

The complete official Army merged file was scanned across all 9,200,232
fixed-width records. Its compressed source was previously verified at
185,043,578 bytes with SHA-256
`80c46e83937c6483d11def47fbb1629cab0ac135694fdfa09268b66d826f1066`.
James M Compton was the cohort's only record with an eligible eight-digit index
identifier; it produced no identifier match. Every exact full-name Army row was
reviewed. Charles R, James M, James R and William D Compton produced three,
three, five and six exact-name rows respectively, but no further identifier
selects one. Their occupations and grades remain unassigned. Alfred F Conard
produced one exact-name row dated 24 September 1943 with birth-year value `11`
and civilian-occupation value `022`. The Army file is not an officer, Navy,
Marine Corps, women's-service, foreign-personnel or comprehensive OSS roster,
so non-hits are not negative proof.

The current project CIA adapter ran one bounded official OSS Collection search
for each person. It returned no candidate matches. The current Library of
Congress adapter likewise ran bounded exact-name employment searches. Seven
page candidates were checked at OCR-context level and rejected through the
review-decision workflow. The 12 March 1960 *Kodiak Mirror* item names James
Alfred Compton, not James M or James R. Five William Compton items name William
H, William Henry, William A or William R Compton, or supply no exact William D
identity; none has an OSS or Box 137 bridge. The decisions are idempotently
preserved in `research/loc_review_decisions_2026-09-09_batch450.csv`.
The sanitized adapter state is preserved in
`research/adapter_attempt_checkpoints.json`; the Batch 450 cohort contributes
twenty-one attempts and seven candidates. Its total attempt count grows by
twenty-two from the preceding export because the regenerated checkpoint also
recovers one previously reviewed Batch 406 attempt that was absent there.

The rare exact name Coalter B Compton expands to Coalter Bates Compton in the
official *Congressional Record*. The April 30, 1917 Senate record lists him
under the Cavalry Arm as a second lieutenant with rank from April 20, 1917. The
2010 West Point graduate register independently records Coalter B. Compton,
Cullum number 5701, in the April 1917 class. Both pages were rendered at 150 dpi
and visually inspected. The unusual full name and mutually consistent military
sources support high-confidence identity and commissioned Army classification.
The 1917 Cavalry appointment is published as other documented prewar history,
not as the assignment immediately before OSS service; Box 137 remains necessary
to bridge the quarter-century gap.

Alfred F Conard's single exact-name Army row aligns with institutional sources
on two identifiers beyond the name. Grinnell College's institutional history
identifies Alfred Fletcher Conard with a 1911 birth year, matching the Army
birth-year value. A 1940 *Washington University Law Quarterly* article names
Alfred F. Conard as Assistant Professor of Law at the University of Kansas
City, and Columbia University's 1942 annual report independently names the
same person, title and law school. Both PDF pages were rendered at 150 dpi and
visually inspected. The Army occupation value `022` maps through NARA's
official code list to `Lawyers and judges`.

The combined name, birth year, legal occupation and two pre-service
institutional sources support high-confidence identity but not confirmation,
because no private index identifier or direct personnel-file linkage selects
the Army row. The University of Kansas City School of Law is published as the
best-supported candidate for his last civilian employer before Army service,
with medium confidence and visible qualification: the sources document the
role in 1940 and 1942 before Army entry in September 1943, but do not exclude an
intervening role or establish the later Army-to-OSS sequence. The historical
institutional name is preserved without substitution of a modern successor.

Isabel L Comstedt produced a secondary biographical lead involving the surname
Comstedt, but it lacks direct identity, OSS, employment and Box 137 links. The
lead remains rejected, and no marital-name relationship or foreign status is
inferred. A Dorothy G Comstock women's-service Army row has the wrong middle
initial for Dorothy D Comstock and likewise remains unassigned.

Every person received recorded NARA index context, official CIA checks,
exact-name OSS and meaningful variant searches, employment and occupation
queries, and applicable institutional, obituary, directory, newspaper, current
Library of Congress and archival discovery. No authenticated NARA Catalog API
request was used.

## Adjudicated results

| Indexed person | Identity result | Best-supported pre-OSS result | Publication decision |
|---|---|---|---|
| Simone J Companardi | Unresolved; no identifier or assignable source | No reliable result | Archival review, Box 137 |
| Charles R Compton | Unresolved; literal six-digit value and three unassigned Army namesakes | No reliable result | Critical identity review, Box 137 |
| Coalter B Compton | High confidence; official 1917 appointment and West Point register | Second lieutenant, Cavalry Arm, 20 April 1917 | Publish as other documented prewar military assignment; not immediate |
| James M Compton | Unresolved; index identifier has no Army match; three namesakes | No reliable result | Critical identity review, Box 137 |
| James R Compton | Unresolved; five unassigned Army namesakes | No reliable result | Archival review, Box 137 |
| William D Compton | Unresolved; six Army namesakes and five newspaper candidates rejected | No reliable result | Archival review, Box 137 |
| Isabel L Comstedt | Unresolved; indirect surname lead rejected | No reliable result | Archival review, Box 137 |
| Anne E Comstock | Unresolved; no identifier or assignable source | No reliable result | Archival review, Box 137 |
| Dorothy D Comstock | Unresolved; Dorothy G Army row rejected | No reliable result | Archival review, Box 137 |
| Alfred F Conard | High confidence; birth year, legal occupation and institutional sources align | University of Kansas City School of Law, assistant professor; Lawyers and judges category | Publish qualified last-civilian candidate and occupation; no immediate claim |

## Publication and archival result

- All ten records have saved, reviewable research attempts and non-`not_started`
  statuses.
- One qualified last-civilian employer candidate, one qualified Army-entry
  occupation and one high-confidence earlier military assignment are published
  with claim-level citations.
- Two high-confidence identity claims are published; neither is upgraded to
  confirmed without a direct OSS-personnel linkage.
- Eight profiles remain unresolved and public with specific Box 137 next
  actions; two carry critical identifier-review priorities.
- Seven Library of Congress candidates are explicitly rejected and no
  common-name Army occupation is transferred to an indexed person.
- No full private identifier, raw Army row, live API response, speculative
  namesake or rejected candidate enters public data.
