# Batch 504 discovery checkpoint

2026-09-13 UTC. This checkpoint covers personnel-index PDF page 100 rows
20-29, Walter M Cuddy Jr. through Jane Culbertson, crossing from Box 157 to
Box 158 at archival location 230/86/29/04. The index page and the official
Army occupation-code page were rendered and visually inspected. Literal
private identifiers are omitted.

## Cohort and disposition

| PDF row | Source record | Person entity | Indexed name | Disposition |
|---:|---|---|---|---|
| 100:20 | 38dc8981-5225-57a1-88bd-86c0ae54ea68 | 2dbfa59b-f026-5aed-9456-1f9f853bada3 | Walter M Cuddy Jr. | Confirmed enlisted Army identity; qualified printing occupation only |
| 100:21 | cfaf0ccc-c35d-5778-bfa4-ea9489e88300 | 3d16196a-e9d8-5c6d-8389-c213c16ba5f6 | John H Cudmore | Unresolved; unrelated newspaper probate notice rejected |
| 100:22 | f916c548-9f87-5ca3-aff3-80f1d5e5a989 | 4bc2de73-077f-5f07-a1b5-a13874dc02ff | Frank Cuellar | Ambiguous; exact-name Army row has a different private identifier and is withheld |
| 100:23 | 3123eb9a-bbe4-551d-a507-931d16515eaf | 40bd9b2d-264e-5842-9499-10ae6eaf98d3 | Rodolfo E Cueva | Ambiguous; name-only Army candidate lacks a direct OSS bridge |
| 100:24 | 27f8ff5c-9aa3-5556-b30d-1d01df8a40ea | bc53e536-8919-59cb-b760-64d9928a0847 | Domingo Cuevas | Unresolved; no reliable identity bridge or pre-OSS affiliation found |
| 100:25 | 4e004a2c-5b93-513c-a138-92ddae585ac9 | 8d9ac81b-e576-5636-9f1c-cbababa88946 | Mario J Cugia | Confirmed enlisted Army identity; qualified printing/publishing occupation only |
| 100:26 | 17a2489c-426c-55c0-9d3e-10460fa48ab3 | 18dff061-47dd-532d-aed9-95e1affef495 | Saburo Cujow | Unresolved; no reliable identity bridge or pre-OSS affiliation found |
| 100:27 | 98cc8133-e34d-54a2-be1c-48914802e555 | 4301edb6-d672-55ee-8659-abad726ee17d | Frederick C Culbert | Unresolved and kept separate from Frederick P Culbert |
| 100:28 | 55d24655-ea8b-5a39-ab4a-27fca9c15183 | 2434a0ca-c538-572c-be3b-dde55a2b03dd | Frederick P Culbert | High-confidence State Department/Foreign Service pathway immediately before wartime intelligence assignment; earlier Navy and unnamed business history documented |
| 100:29 | 2f865da8-a7a7-59fc-b392-38b901bf4cf7 | aaf1d806-5ddb-580b-af22-e83861cd2c09 | Jane Culbertson | Unresolved; newspaper OCR token collision rejected |

## Visual and field audit

The page image confirms the ten-row sequence, Box 157 for Walter Cuddy and
John Cudmore, Box 158 for the remaining eight people, and location
230/86/29/04. The source spellings, initials, suffix and empty rank fields
remain recoverable. Full printed identifiers stay private and are masked in
the public projection.

The official Army code-list page confirms code 448 as the skilled occupation
“Pressmen and plate printers, printing” and code 849 as the unskilled category
“Occupations in printing and publishing, n.e.c.” These labels support
occupations, not employers.

## Army merged-file adjudication

The complete 9,200,232-record Army Serial Number Merged File was scanned from
the official fixed-width data.

- Walter M Cuddy Jr. has exact name, middle initial, suffix and private-
  identifier agreement. His private row records Private rank, 11 May 1943
  entry and occupation code 448. It confirms an enlisted Army identity and a
  printing occupation, not a named employer.
- Mario J Cugia has exact name and private-identifier agreement. His private
  row records Private rank, 20 March 1943 entry and occupation code 849. It
  confirms an enlisted Army identity and a broad printing/publishing
  occupation, not a named employer.
- Frank Cuellar has no strict private-identifier hit. An exact-name Army row
  carries a different private identifier, so it remains a rejected identity
  shortcut rather than a published occupation.
- Rodolfo E Cueva has a name-only Army row dated 26 December 1941. With no
  direct OSS or identifier bridge, it remains a private candidate.
- John Cudmore, Domingo Cuevas, Saburo Cujow, both Culberts and Jane Culbertson
  have no matching Army evidence. Absence from the Army file is not treated as
  negative proof.

## Frederick P Culbert pathway

The direct wartime *Plan for North Africa* identifies Frederick P. Culbert as
a serving vice consul and control officer selected for the GYMNAST work. This
supports a high-confidence, explicit-immediate U.S. Department of State /
Foreign Service government assignment. A later Foreign Service Journal
account dates his recall for Western Task Force duty to September 1942.

The two sources disagree on the control-officer city: the wartime plan names
Casablanca while the 1979 account names Dakar. The database preserves both
source claims, leaves the normalized city blank, and publishes a conflict note
instead of harmonizing them.

The same official plan documents Naval Academy class of 1916, earlier Navy
service and a later business-executive history in France and Germany. Navy
service is an earlier military assignment. Because no business is named, the
business history is an occupation-only affiliation and not a verified
employer. The plan recommends Commander rank in the Naval Reserve, but a
recommendation is not proof that a commission issued; the index entity's
commissioned-officer value therefore remains unknown. A 1946 Foreign Service
Journal item independently anchors the exact-name Foreign Service identity to
work connected with the November 1942 North Africa landings.

Frederick C Culbert remains a distinct unresolved index entity. No evidence is
transferred between the two same-surname records.

## CIA, Library of Congress, web and review audit

Ten bounded CIA Reading Room checks returned no adapter candidates. Ten
Library of Congress checks produced two candidates, both rejected after
official page context was inspected:

- John H Cudmore's candidate was an unrelated Frank A. Cudmore probate notice.
- Jane Culbertson's candidate was an OCR/token collision joining “Maxine
  Janes” and “Culbertson.”

Both decisions are stored in
`research/loc_review_decisions_2026-09-13_batch504.csv` and were imported
twice; the second import reported only duplicates. Exact-name OSS,
employment, occupation, institutional, newspaper, obituary, military and
archival searches were assessed for all ten people. No quota-sensitive NARA
Catalog API request was made.

The sanitized adapter checkpoint now contains 2,546 attempts, 520 candidates
and 45 person updates. Batch 504 adds 20 actual adapter attempts, ten
synthesized outcomes, seven sources, five affiliations and twelve claims. The
evidence bundle was imported twice with duplicate-only results on the second
pass.

## Employer-analytics correction

Batch 504 makes the employer metric match the documented methodology: an
employment relationship counts as a verified employer only when it names an
organization; self-employment remains countable. An unnamed employment
history can still be published as an affiliation, but cannot create an
employer or sector statistic.

This excludes Culbert's unnamed business-executive history and corrects an
older unnamed Betty A Lussier aircraft-manufacturing record. Rhea G Clyman
continues to count through separately documented named/self-employed evidence.
The resulting verified-employer total is 243, down from the previously
reported 244 despite this batch's new supported pathway.

## Coverage after Batch 504

- Index coverage: 23,978 of 23,978 source rows linked, 100.0000%.
- Research-attempt coverage: 4,808 of 23,940 active person entities, 20.0835%.
- Verified-affiliation coverage: 548 people, 2.2891%.
- Verified-employer coverage: 243 people, 1.0150%.
- Archival-review coverage: 4,763 people assessed, 19.8956%.
- Claims by confidence: 1,137 confirmed; 1,413 high; 1,142 medium; 124 low;
  103 conflicting.
- Current research statuses: 229 verified employer; 95 documented prewar
  employer; 876 occupation only; 2,988 requires archival review; 241 needs
  identity review; 17 needs temporal review; 91 conflicting; 82 no reliable
  result after protocol; 137 completed; 44 in progress; 7 candidate found;
  1 blocked by source access; 19,132 not started.

## Archival next actions

Boxes 157-158 remain necessary for the unresolved and ambiguous people in this
cohort and for verifying the exact Army-to-OSS pathways behind the two
confirmed enlisted identities. Frederick P Culbert's indexed file should test
the high-confidence identity bridge, resolve the Casablanca/Dakar conflict and
establish whether the recommended Naval Reserve commission was ever issued.

Research resumes with page 100 rows 30-39, Ruth B Culbertson through Carson W
Culp, all in Box 158.
