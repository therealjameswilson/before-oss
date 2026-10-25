# Batch 904 research audit

## Scope

- Index boundary: NARA personnel index PDF page 442, rows 1-23.
- Printed range: Leland M Spore through Rosario F Squatrito.
- Archive range: Box 734, location 230/86/41/02.
- Preserved source rows: 23.
- Active person entities: 23.
- Terminal outcomes saved: 23.
- Official Army bulk identity bridges accepted: 6.
- Protected identifiers in public evidence: 0.

## Outcomes

| Outcome | People | Notes |
|---|---:|---|
| Verified employer found | 2 | Drexel A Sprecher; Robert B Springsteen |
| Documented prewar employer found | 1 | Stewart Springer; not promoted to immediate or last civilian employment |
| Needs temporal review | 1 | Enrico Squadra and the 1943 Office of War Information listing |
| Conflicting sources | 1 | Rosario F Squatrito; employer lead and occupational conflict both preserved |
| Occupation only found | 5 | Accepted official Army matches; no named employer inferred |
| Requires archival review | 13 | Minimum staged protocol completed; Box 734 remains necessary |

Jack H Spradlin already had a prior nonplanned attempt, so the batch added 22
newly attempted people to project-wide research-attempt coverage even though
all 23 received a new reviewable Batch 904 outcome.

## Published evidence decisions

### Drexel A Sprecher

The United States Holocaust Memorial Museum and John Q. Barrett's documented
chronology support the distinctive identity, National Labor Relations Board
employment from 1938 until Army enlistment in 1942, and transfer from the Army
into OSS in 1944. The public profile therefore models the Army as the immediate
military affiliation and the NLRB as the last civilian employer.

### Stewart Springer

NOAA identifies Springer in the OSS shark-repellent project. Mote Marine
Laboratory's institutional biography dates Bass Biological Laboratory work to
1936-1940, while a contemporary National Museum report independently connects
specimens from that laboratory to Springer. Because the accessible record does
not fill the 1940-to-wartime gap, Bass Biological Laboratory remains an earlier
documented prewar employer only.

### Robert B Springsteen

The Library of Congress Veterans History Project transcript supplies the
first-person sequence: work at "McGill's," departure for Army service in May
1942, and reporting to OSS on 20 April 1944. The official Congressional Record
history normalizes McGill's to McGill Manufacturing Company in Valparaiso. No
job title is invented.

### Enrico Squadra

A 1943 Congressional Record personnel listing identifies Enrico Squadra as an
associate script editor in the Office of War Information's Italian-language
section in New York. The exact name and relevant wartime context support a
high-confidence identity, but the listing does not establish its sequence
relative to OSS. The profile therefore remains in temporal review.

### Rosario F Squatrito

Official Army and Operation Ginny evidence confirm the identity while keeping
the protected identifier private. The Army entry record decodes to the
historical longshoremen/stevedores category. A later National Park Service
history and a la Repubblica account describe tool-and-die work, and the latter
names Superior Die Cutting. The qualified employer lead and the occupational
conflict are both public; default analytics exclude the conflict.

## Army occupation decisions

| Person | Army-entry date | Historical code | Qualified occupation |
|---|---|---:|---|
| Jack H Spradlin | 1942-09-28 | 677 | Filers, grinders, buffers, and polishers (metal) |
| Albert I Spratt Jr | 1941-06-03 | 110 | Printing and publishing clerks, not elsewhere classified |
| Roland G Spratt | 1943-04-29 | 137 | Stenographers and typists |
| Robert F Spreen | 1942-04-09 | 001 | Accountants and auditors |
| Nicholas C Squadrito | 1941-02-25 | 227 | Waiters and waitresses, except private family |
| Rosario F Squatrito | 1942-10-26 | 747 | Longshoremen and stevedores; conflicting narrative evidence retained |

These historical categories identify neither an employer nor a workplace.

## Rejected and unresolved leads

Thirteen people received the full staged exact-name, OSS-context, official,
occupation/employer, obituary, institutional, newspaper, directory and
archival search protocol without a defensible result. Discovery-only roster
evidence for Michael Sproveri, a military cemetery namesake for Harold A
Sprinkle, and postwar business evidence for a Donald W Sprung namesake were not
promoted to public facts. Each unresolved profile directs researchers to Box
734 rather than asserting that no pre-OSS employment existed.

## Reproducibility

- Evidence generator: `scripts/generate_batch904_bundle.py`
- Reviewed evidence: `research/evidence-page442-spore-to-squatrito-review_batch-904_2026-10-25.json`
- Army decisions: `research/army_review_decisions_2026-10-25_batch904.csv`
- Browser regression: `site/tests/batch904.spec.ts`
- Public redaction result: passed.
- SQLite quick check: `ok`.
- Foreign-key errors: 0.
- Extraction validation: 23,978/23,978 rows, all 522 pages represented, every
  parser-warning row visually resolved.
