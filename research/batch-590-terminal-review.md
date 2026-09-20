# Batch 590 — PDF page 120, rows 1–20

Reviewed 2026-09-20 UTC. All twenty printed rows were checked against a
rendered page of the [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf).
All are distinct source rows and person entities, indexed in Box 190 at
location 230/86/30/02. The printed `British A` notation for Richard I
Dobson and `also AS` note for David S Dodge are preserved literally, not
expanded into unsupported affiliations. Donald E Dodge's unusual serial
prefix was visually checked and remains private. All twenty have durable
CIA Reading Room, Library of Congress, and bounded manual cross-source
attempts with terminal **online** `requires_archival_review` status.
Physical personnel files have not been examined.

Nine official [Army bulk-file](https://catalog.archives.gov/id/1263923)
entries provide identity-only crosswalks for Otto Dobrovolny, Joseph C
Dockendorf, Kenneth C Dockery, Paul G Dodd, Perry G Dodd, Chester A Dodge,
David S Dodge, and Harvey H Dodge. All agree by a nonshared protected
identifier. The Otto bulk entry has an extra middle initial not printed in
the index. Harvey has two bulk entries with the same protected identifier,
but discrepant surplus initials and entry dates; they are not a second OSS
person or employer evidence. Army occupation codes are not named employers.

A [Washington Post obituary section on Robert R. Dodderidge](https://www.washingtonpost.com/archive/local/1992/01/31/samuel-c-brightman-dies/6e535bc1-3ab3-4175-97ff-a72add5f8ecb/)
identifies his wartime OSS service and places a White House aide role earlier
in the sequence. Distinctive full name, Army career, OSS connection, and the
index's Major rank support a high-confidence identity match. The obituary
does **not** state a direct White House-to-OSS transfer or give exact dates.
The role is therefore a visibly qualified, medium-confidence **earlier
government assignment**, not an immediate affiliation or last civilian
employer. It is excluded from default high-confidence aggregates. Box 190
is needed for the direct transfer sequence.

An [Indiana University Dodd, Mead finding aid](https://archives.iu.edu/html/InU-Li-VAA8772.html)
names an Edward H Dodd Jr with a publishing career. It has no OSS/Box 190
identity bridge and has not been applied as an employer claim to the indexed
Edward H Dodd Jr. This lead is private pending direct personnel-file review.
Eight LoC newspaper OCR candidates were rejected after context inspection:
two Paul G Dodd results actually named Paul A or Paul C Dodd; Chester and
Donald Dodge results had different middle initials; four George C Dodds
contexts did not provide an inspectable bridge. No namesake job was adopted.

The database contains 23,978/23,978 linked source rows, 23,940 active people,
and 5,712/23,940 people with a nonplanned research attempt (23.8596%).
Confirmed/high employer coverage is 264/23,940 (1.1028%), confirmed/high
affiliation coverage is 604/23,940 (2.5230%), and assessed archival-review
coverage is 5,667/23,940 (23.6717%). There are 18,228 `not_started` people,
259 possible-duplicate groups, and 124 conflict cases. Private SQLite holds
10,622 attempts and 4,810 claims (1,308 confirmed; 1,827 high; 1,362 medium;
184 low; 129 conflicting), 4,927 citation records, and 2,265 unique
source-document keys. The public projection has 2,174 affiliations, 679
organizations, 3,733 sources, and 4,622 claims. The complete-index goal
remains unfinished.

This review is replayable from
`research/evidence-page-120-dobretzberger-through-dodge_batch-590_2026-09-20.json`,
`research/army_review_decisions_2026-09-20_batch590.csv`, and
`research/loc_review_decisions_2026-09-20_batch590.csv`. The Catalog API key
was not used; Army identities came from the official bulk file rather than
Catalog API responses. Next sequential cohort: PDF page 120, rows 21–40.

Local QA passed: seven ingest checks covering all 522 PDF pages, SQLite
integrity and foreign keys, 111 Python unit tests, a stratified 200-profile
audit, Astro checking across 220 files, and a 24,652-page static build.
The bounded release browser suite passed 78/78 checks across desktop,
phone, and tablet, including 30 accessibility checks. All 24,652 HTML files
passed the internal-link check; 50,142 external URLs were inventoried, not
exhaustively live-checked. The public-identifier audit found zero unexpected
full-number matches. The checked-in public-data manifest matched 67 assets
and 96,599,802 bytes. Public deployment remains a separate step.

```bash
python3 -m oss_research assign-page-batch --batch-name batch-590 --page 120 --first-row 1 --last-row 20
python3 -m oss_research research --source cia --batch batch-590 --max-queries 20 --resume
python3 -m oss_research research --source loc --batch batch-590 --max-queries 20 --resume
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch590.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-20_batch590.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-120-dobretzberger-through-dodge_batch-590_2026-09-20.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```
