# Batch 600: NARA index page 128, Dunlap through Durham

The original NARA PDF page 128 was rendered at inspection resolution and
compared against all 46 extracted rows. Names, ranks, protected-identifier
column occupancy, boxes, notes, and locations match. The printed box sequence
returns to Box 206 for Loyal Durand Jr. after Virginia R Durand in Box 207;
the source order and values are preserved, not silently regularized. Page 128
has been added to the page-review ledger. In total, 101 of 522 pages have
direct visual review; the remaining 421 have not been visually certified.
The ingest validation still passes all programmatic gates with 23,978 of
23,978 printed rows linked, zero foreign-key errors, and all prior parser
warning rows visually resolved.

Forty-five page-128 people received rate-limited Library of Congress
Chronicling America searches in two resumable cohorts. Grier Durant had an
earlier archival-review disposition, so all 46 people on the page now have a
non-`not_started` research status. The adapter saved 39 newspaper discovery
candidates and reported zero query errors or rate-limit blocks. Newspaper
hits are not employer claims until page context, identity, and chronology
are independently checked.

Fourteen official Army Serial Number Merged File candidates were reviewed
privately: 12 accepted on exact name (including the indexed suffix when
present) plus nonshared protected identifier, and two held as probable for
Vern/Vernon and an extra middle initial. These are identity decisions only;
the Army bulk file does not name civilian employers. No full identifier is
published.

The 1938 [New York Adjutant General report](https://museum.dmna.ny.gov/application/files/2916/1141/3435/AG_Report_1938.pdf),
printed and PDF page 53, identifies Sergeant Louis Dups in Headquarters
Troop, 101st Cavalry. An original [OSS ETO memorandum of 3 May 1945](https://www.archives.gov/files/research/jfk/releases/104-10165-10120.pdf),
PDF page 4, lists Major Louis Dups in the Cavalry among OSS personnel.
Together with the indexed Major Louis Dups in Box 206, the uncommon name
and branch support a high-confidence **earlier military assignment**. The
sources do not identify his immediate pre-OSS assignment or a civilian
employer, and the public profile says so.

IEEE and IBM both document an IBM engineer named Stephen W. Dunwell, but
neither links that biography to the indexed Captain Stephen W Dunwell in
Box 206. IBM was withheld pending direct identity evidence. Virginia E
Dunlap (page 127) and Virginia A Dunlap (page 128) share Box 205 but have
different printed middle initials; they remain separate person entities
in one visible possible-duplicate group.

Current local coverage after this batch: 23,978 linked source rows;
23,940 active people; 6,098 with saved nonplanned research attempts
(25.472%); 269 with confirmed/high published employer evidence (1.1236%);
614 with confirmed/high published affiliation evidence (2.5647%); and
5,731 with archival-review dispositions (23.939%). There are still 17,842
`not_started` people across the entire index. Claim counts: 1,311
confirmed, 1,858 high, 1,369 medium, 185 low, and 132 conflicting.
Possible-duplicate groups: 265. The page-128 search is **not** a terminal
research protocol for all 46 people or for the index as a whole.

Replay commands from the repository root (with Python dependencies installed):

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_page128_2026-09-20.json
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch600.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-128-dunlap-durham_batch-600_2026-09-20.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The private SQLite database remains local; review decisions, reviewed
evidence, sanitized adapter checkpoints, and redacted public assets are
versioned for reproducibility. No NARA Catalog API key was placed in this
checkout, and no authenticated Catalog query was made. Box 205–207 file
examination remains essential for many unresolved identities and jobs.
