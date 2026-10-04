# Batch 736: Parry-Pascone research

Batch 736 completes PDF page 358, rows 24-46, from **Arthur J Parry**
through **John Pascone**. A 300-dpi visual inspection confirmed all 23
printed rows in Boxes 587-588 at location 230/86/38/02. Embedded text was
checked against the page render, including the box transition at John
Pascone. Original spellings, ranks, grades, notes, and protected identifiers
remain recoverable in the private database.

The inspection preserves unusual and incomplete printed forms rather than
silently expanding or correcting them. **George G Parry** is printed as
`Lt COM`; **Richard Parry** has `Lt` with no serial value; **Edward M Parsen**
is noted as Belgian; **Harvey Parsons** has the visibly truncated note
`Norwegi`; **Paul A Pasco** is printed as `S/Lt` and noted as French; and
**John Pascone** has the incomplete note `Refer to`. **Jacintha Pascal** is
printed as P-2 and **Herman H Partnon** as WAE.

Seven high-confidence identities come from exact official Army bulk matches
with nonshared protected identifiers: **Arthur J Parry**, **Edward M
Parsen**, **Edwin O Parsons**, **Ira H Parsons**, **Allen V Partington**,
**Norman S Pascal**, and **John Pascone**. These matches establish identity
only. Protected identifiers and coded Army data remain private and are not
converted into employer or occupation claims.

The indexed protected identifier for **William E Parry** points to an Army
record under a different name. Two candidate rows associated with **Marvin F
Partain** also point to different Army names. These mismatches remain visible
as conflicts, no Army metadata is transferred, and the personnel files
receive critical archival-review priority.

No defensible pre-OSS employer was found for the cohort. A rare-name
Moluccan lead for Dominggus Pasalbessy remains an unresolved identity lead.
A 1943 newspaper namesake for John J Pascoe was rejected because its
private-to-corporal chronology conflicts with the indexed second-lieutenant
record. A John Pascone genealogy lead is discovery-only, and a Gustav A
Parsons First World War officer lead lacks an OSS bridge. Other unbridged or
irrelevant namesakes were rejected rather than published.

The CIA adapter failed closed under the source's access policy. The Library
of Congress adapter recorded one bounded access error. The web adapter saved
23 deterministic query plans before manual staged review. No authenticated
NARA Catalog API request was made because a key was not exposed to this run.

All 23 people have terminal dispositions: 21 require archival review and two
have conflicting sources. Identity statuses are seven high_confidence, two
conflicting, and 14 unresolved. The reviewed bundle imports two sources, nine
claims, 18 claim-source links, 23 person updates, and 23 consolidated research
attempts. Seven accepted and three conflicting identity-review decisions are
recorded.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **9,962/23,939 (41.6141%)**;
confirmed/high verified-employer coverage is **334/23,939 (1.3952%)**;
confirmed/high verified-affiliation coverage is **745/23,939 (3.1121%)**;
archival-review disposition coverage is **8,420/23,939 (35.1727%)**. There
are **13,972** not_started people, **523** possible-duplicate groups, and
**333** active conflicts. SQLite stores **18,225** attempts or plans and
**6,373** claims: 1,382 confirmed, 2,959 high, 1,537 medium, 198 low, 295
conflicting, and two unresolved. It contains **5,716** citation records and
**2,890** unique source documents. The public projection contains **2,490**
affiliations, **863** organizations, **4,492** sources, and **6,166** claims.
Full-index historical research remains unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

~~~sh
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research assign-page-batch --batch-name batch-736-parry-pascone --page 358 --first-row 24 --last-row 46
python3 -m oss_research research --source cia --batch batch-736-parry-pascone --max-queries 23
python3 -m oss_research research --source loc --batch batch-736-parry-pascone --max-queries 23
python3 -m oss_research research --source web --batch batch-736-parry-pascone --resume --max-queries 23 --dry-run
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-10-04_batch736.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page358-parry-pascone-review_batch-736_2026-10-04.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research export-review-queue
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
~~~

Adapter checkpoints must be imported before final reviewed decisions and
evidence so temporary discovery states cannot supersede reviewed dispositions.
The next research boundary is PDF page 359, rows 1-23, from Angeline Pascuzzi
through Jane Paterson.

No API key, full service or officer number, raw Catalog or LoC API response,
copyrighted page image, street address, living-relative detail, modern
people-finder record, or private reviewer note is committed or included in the
public site. No authenticated NARA Catalog API request was made for this batch.
