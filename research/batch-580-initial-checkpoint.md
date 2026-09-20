# Batch 580 — initial discovery checkpoint, PDF page 117 rows 1–10

Review date: 2026-09-20 UTC. The ten printed rows are in Box 185, location
`230/86/30/01`. The source page was rendered and checked against embedded
text. Rank abbreviations displaced into the middle-initial column remain
recoverable as printed for Goodhue Diament (`T-4`) and Damon Diamondes
(`T/Sgt`). This is a discovery checkpoint, **not** a terminal review or an
employer finding. No physical personnel file has been inspected.

The private queue now has `assigned_batch=batch-580` for all ten cautious
person entities. The CIA Reading Room adapter saved 11 `no_result` searches
(John E Deyoung was searched twice); the Library of Congress adapter saved
ten `no_result` searches. All ten people therefore have a non-planned attempt,
but the minimum multi-source research protocol remains in progress. No NARA
Catalog API request was made, and no search failure is treated as proof of
an absence of previous employment. The sanitized adapter checkpoint is in
`research/adapter_attempt_checkpoints.json`.

The [official Army bulk file](https://catalog.archives.gov/id/1263923)
matches protected identifiers and full indexed names for Serge A Diab,
Spyros Dialismas, and Goodhue Diament. Their identity-only candidates were
accepted in `army_review_decisions_2026-09-20_batch580.csv`; no occupation
code or Army status was converted into an employer. Goodhue has a second,
independent official identity bridge: an original 19 July 1945 OSS Mission to
France award list in [NARA document 104-10165-10120, PDF pages 79 and
82](https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf)
gives his name, technical grade and the same protected identifier. Its
Ardennes Campaign citation describes wartime service, not pre-OSS work.

Paul and Pavlos Diamantoukos are separate adjacent index rows. The Army bulk
entry shares Paul's protected identifier but names `PAVLOS`. The candidate
is marked `conflicting`, and neither row has been merged or assigned the
other's biography. Their Box 185 files need side-by-side review.

The [Densho Encyclopedia biography of John E. de
Young](https://encyclopedia.densho.org/John%20E.%20de%20Young), authored by
Brian Niiya, explicitly states that a John Edward de Young left a University
of Chicago anthropology Ph.D. program to become an OSS Far East Desk regional
planner. The article was inspected directly in the browser. It is a
high-value **candidate** for the unnumbered John E Deyoung index row, and
the relationship would be *student*, not employment. Without a unique index
identifier or personnel-file comparison, the school and biography have not
yet been imported as a settled claim. Seek the article's cited 1950
*International Directory of Anthropologists* entry and compare Box 185.

Remaining names in the cohort: Louis A Dezman, John G Dial Jr., Melvin
Diamond, and Damon Diamondes. Exact OSS and employer/occupation searches
have not yet yielded a source linking a named predecessor organization to
these index rows. Later directories, modern namesakes and genealogy snippets
are not employment evidence. Continue institutional, wartime, newspaper and
archival checks before a terminal disposition.

Resume with the next source family; do not run an unrestricted query sweep:

```bash
python3 -m oss_research assign-page-batch --batch-name batch-580 --page 117 --first-row 1 --last-row 10
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research research --source nara --batch batch-580 --max-queries 10 --dry-run
```

To replay the Army decisions in a fresh database, first run the documented
`army-bulk-match` crosswalk to completion against the verified private
`ASNEF.FIN.DAT` file, then import
`research/army_review_decisions_2026-09-20_batch580.csv`. The assignment,
adapter checkpoint and review import are idempotent. The NARA command above
is only a dry run; live Catalog access still requires an unexposed local key
and budget check.
