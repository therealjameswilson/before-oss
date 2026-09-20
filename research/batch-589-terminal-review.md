# Batch 589 — PDF page 119, rows 41–46

Reviewed 2026-09-20 UTC. All six printed rows were checked against a rendered
page of the [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf).
The first is in Box 189, location 230/86/30/01; the other five are in Box 190,
location 230/86/30/02. All are distinct source rows and person entities.
Each has durable CIA Reading Room, Library of Congress, and bounded manual
cross-source attempts, with terminal **online** `requires_archival_review`
status. Physical personnel files have not been examined.

The page visibly prints `Dobberstein, J` in the surname column and `Albert`
in the given-name column. The public profile retains this awkward original
index order until Box 190 or another direct record establishes where the `J`
belongs. Paul Dobbs's unusual printed serial formatting was also visually
verified and remains private. A same-name military newsletter for Theodore
D'Luski, a postwar directory Albert Dobberstein, and a John Dobes Jr roster
were not accepted as identity or employment evidence.

For indexed Francis Dobo, a [2024 PUNKT interview](https://punkt.hu/en/2024/06/30/a-previously-unknown-hungarian-related-photo-collection-discovered-in-america-interview-with-michael-dobo/)
describes a Francis F. Dobo's work for Opera Mundi, Gabriel Wells, and the
Office of War Information. This is a *candidate career*, not a match to the
Box 190 row: the index gives no middle initial or protected identifier, and
the article does not say he served in OSS. Archival descriptions at the
[British Library](https://searcharchives.bl.uk/catalog/040-002084143) and
[Tate](https://archive.tate.org.uk/Record.aspx?id=TGA+200410%2F1%2F1%2F146&src=CalmView.Catalog)
concern postwar activity and do not bridge the identity. No employer from
those records is attached to indexed Francis Dobo or published on his page.

Indexed John Dobo agrees by name and a nonshared protected identifier with
ordinal 4127916 in the official [Army bulk file](https://catalog.archives.gov/id/1263923).
The match supports high-confidence **identity only**. Its occupation code is
not a named employer; no immediate Army-to-OSS assignment is inferred. John
and Francis Dobo remain separate.

The database contains 23,978/23,978 linked source rows, 23,940 active people,
and 5,692/23,940 people with a nonplanned research attempt (23.7761%).
Confirmed/high employer coverage remains 264/23,940 (1.1028%), and
confirmed/high affiliation coverage remains 604/23,940 (2.5230%). Assessed
archival-review coverage is 5,647/23,940 (23.5881%). There are 18,248
`not_started` people, 259 possible-duplicate groups, and 124 conflict cases.
Private SQLite contains 10,562 attempts, 4,800 claims (1,308 confirmed;
1,818 high; 1,361 medium; 184 low; 129 conflicting), 4,924 citation records,
and 2,263 unique source-document keys. The public projection has 2,173
affiliations, 678 organizations, 3,730 sources, and 4,612 claims. The
complete-index goal is not done.

This review is replayable from
`research/evidence-page-119-dluski-through-dobo_batch-589_2026-09-20.json`
and `research/army_review_decisions_2026-09-20_batch589.csv`. The Catalog
API key was not used; the Army crosswalk is from an official bulk file, not
a Catalog API response. The next sequential cohort begins on PDF page 120.

Local QA passed: seven ingestion checks (including all 522 pages), SQLite
integrity and foreign keys, 111 Python unit tests, the stratified 200-profile
audit, Astro checking across 219 files, and a 24,651-page static build. The
bounded release browser suite passed 78/78 checks across desktop, phone, and
tablet, including 30 accessibility checks and explicit oil-company category
tests. All 24,651 HTML files passed the internal-link check; 50,140 unique
external URLs were inventoried, not exhaustively live-checked. The public
identifier audit found zero unexpected full-number matches. The checked-in
public-data manifest matched 67 assets and 96,550,116 bytes. Public
deployment is a separate step and is not implied by local tests.

```bash
python3 -m oss_research assign-page-batch --batch-name batch-589 --page 119 --first-row 41 --last-row 46
python3 -m oss_research research --source cia --batch batch-589 --max-queries 6 --resume
python3 -m oss_research research --source loc --batch batch-589 --max-queries 6 --resume
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch589.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-119-dluski-through-dobo_batch-589_2026-09-20.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```
