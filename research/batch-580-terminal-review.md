# Batch 580 — terminal online review, PDF page 117 rows 1–10

Reviewed 2026-09-20 UTC. The ten printed Box 185 rows at `230/86/30/01`
were checked against the rendered NARA PDF page. Each remains a separate
source row and person entity. The saved CIA and Library of Congress checks,
bounded exact-name OSS and employer/occupation searches, institutional and
archival searches, official Army bulk crosswalk, and original OSS award page
are recorded in the private database and the importable
`evidence-page-117-deyoung-through-diamondes_batch-580_2026-09-20.json` bundle.
All ten people now have a terminal `requires_archival_review` disposition,
research notes, rejection reasons where applicable, and a Box 185 next action.
No physical personnel file has been inspected.

The [official Army merged file](https://catalog.archives.gov/id/1263923)
provides high-confidence identity-only matches for Serge A Diab, Spyros
Dialismas, and Goodhue Diament, based on exact names and nonshared protected
identifiers. An [original 19 July 1945 OSS Mission to France award
list](https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf),
PDF pages 79 and 82, independently confirms Goodhue's name, technical grade,
and identifier. These sources document wartime identity, **not** a pre-OSS
employer. Full identifiers are confined to the private database.

Paul and Pavlos Diamantoukos remain separate indexed people in a visible
possible-duplicate group. The official Army entry agrees with the identifier
printed on Paul's row but gives the name Pavlos, also printed on the adjacent
unnumbered row. This conflict cannot be settled by choosing a preferred name;
compare both Box 185 files before merging or attributing work history.

[Densho's biography of John Edward de
Young](https://encyclopedia.densho.org/John%20E.%20de%20Young) describes its
subject leaving a University of Chicago anthropology Ph.D. program for the
OSS Far East Desk. The unnumbered index row gives only John E Deyoung. Its
identity link to the biography is a qualified candidate, not a high-confidence
match. The candidate *student* affiliation is retained privately as a
low-confidence review lead, withheld from public affiliation and employer
aggregates. Even if confirmed, student status would not make Chicago an
employer. The cited 1950 anthropologists directory and Box 185 should be
compared before publication of the candidate's chronology as this indexed
person's fact.

For Louis A Dezman, John G Dial Jr., Melvin Diamond, and Damon Diamondes,
accessible searches reviewed here did not yield a named employer with both a
sound identity bridge and a pre-OSS temporal bridge. A radio-amateur callbook,
postwar city directories, genealogy, modern namesakes, and an unexplained
`also AS` index note do not supply such proof. The same employer question
remains open for the three Army-matched people and both Diamantoukos rows.
The public profiles say, "No reliable pre-OSS employer has yet been identified
in the accessible sources reviewed," not that they had no prior employer.

After import, the local SQLite report records 23,978/23,978 linked source
rows, 23,940 active person entities, 5,564 with nonplanned research attempts,
261 with confirmed/high published employer evidence, 5,519 with assessed
archival-review dispositions, and 18,376 active `not_started` people. The
corresponding percentages are 100%, 23.2414%, 1.0902%, and 23.0535%.
This is progress in a full-index research program, not completion of it.

Resume on a database containing the Batch 580 initial adapter and Army
checkpoints with:

```bash
python3 -m oss_research import-reviewed-evidence research/evidence-page-117-deyoung-through-diamondes_batch-580_2026-09-20.json
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The import is idempotent. The research queue next needs a bounded cohort
after page 117 row 10, while Box 185 pull-list work can proceed in parallel
when access is available. Do not interpret a terminal online disposition as
a completed physical-file review.
