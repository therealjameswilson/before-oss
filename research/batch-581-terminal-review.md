# Batch 581 — terminal online review, PDF page 117 rows 11–20

Reviewed 2026-09-20 UTC. The ten printed Box 185 rows at `230/86/30/01`
were checked on a rendering of the original [NARA OSS personnel
index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf).
They remain ten separate source rows and person entities. The adjacent
George C Dibert rows are flagged as a possible duplicate group, **not**
merged. Joseph Diaz's unusually long printed identifier was verified on the
page image and was not silently corrected. No physical personnel file was
inspected.

All ten people have saved CIA Reading Room and Library of Congress checks,
exact-name OSS and occupation/employer discovery, source-review notes, and a
terminal online disposition. The five accepted [official Army bulk-file
crosswalks](https://catalog.archives.gov/id/1263923)—Ismael E Diaz,
Dominick N Diblasi, John S Diblasi, Charles Dibner, and Louis D DiCicco—
confirm wartime identities from matching full names (allowing documented
surname spacing) and nonshared protected identifiers. They do **not** identify
pre-OSS employers. The full identifiers remain private. A same-name [VA
memorial](https://www.vlm.cem.va.gov/JOHNSDIBLASI/7bfba1) for John S Di Blasi
was inspected but not attached to the index row: it lacks a unique identity
bridge. Modern namesakes and later obituaries were also rejected as employer
evidence.

One last civilian employer is newly supported. An original 19 October 1942
[*Broadcasting* item](https://www.worldradiohistory.com/Archive-BC/BC-1942/1942-10-19-BC.pdf),
printed page 39, identifies George C. Dibert as a J. Walter Thompson Co.
spacebuyer newly commissioned a captain in the Army Specialist Corps. Lawrence
C. Soley's [*Radio Warfare*](https://device.report/m/e9158badfd31ef45c1f1ef2e1c1562f9d4b35b7710bdd77b93b5c3583dccb029)
(1989), pages 99 and 161, independently connects a Thompson media director
George Dibert to OSS Morale Operations and refers to Major Dibert. Together
with the index's major rank, the uncommon full name and rank progression
support a high-confidence identity and employment claim for the **numbered
major row only**. J. Walter Thompson is classified as his last documented
civilian employer before Army service. Neither source proves it was his
immediate pre-OSS affiliation; the Army-to-OSS transfer sequence is open.
Soley cites an OSS memo to Major Dibert at RG 226, Entry 148, Box 81, Folder
1180, which remains an archival lead rather than an inspected original. The
adjacent unnumbered Dibert row has no employer claim and requires side-by-side
Box 185 review.

Nine of the ten people have terminal `requires_archival_review` dispositions;
the numbered major has `verified_employer_found` and still has an archival
next action. No other accessible source reviewed here established a named
pre-OSS employer with sound identity and temporal links. Their profiles say
that no reliable employer has **yet been identified in the accessible sources
reviewed**, not that they lacked prior employment. See the importable
`evidence-page-117-diaz-through-dicicco_batch-581_2026-09-20.json` and
`army_review_decisions_2026-09-20_batch581.csv`. The NARA Catalog API was not
called; the Army data comes from the separate official bulk file.

After import, private SQLite contains 23,978/23,978 linked printed rows and
23,940 active cautious person entities. Nonplanned research-attempt coverage
is 5,574/23,940 (23.2832%); confirmed/high published employer coverage is
262/23,940 (1.0944%); broader verified-affiliation coverage is 600/23,940
(2.5063%); and archival-review assessment is 5,529/23,940 (23.0952%).
The active queue still contains 18,366 `not_started` people. These figures
demonstrate progress, not completion of the full research goal.

Resume on the existing private database with:

```bash
python3 -m oss_research assign-page-batch --batch-name batch-581 --page 117 --first-row 11 --last-row 20
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch581.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-117-diaz-through-dicicco_batch-581_2026-09-20.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The assignment and evidence import are idempotent. The Army review decisions
require the private official bulk crosswalk candidates to exist first; do not
infer an employer from an Army occupation code. The next bounded page cohort
starts at page 117, row 21 (Ann J Dick).
