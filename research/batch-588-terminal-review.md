# Batch 588 — PDF page 119, rows 21–40

Reviewed 2026-09-20 UTC. All twenty printed rows on page 119 of the
[NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf)
were checked against a rendered page. All refer to Box 189 at location
230/86/30/01. No source row or namesake was silently merged. Each person has
durable CIA Reading Room, Library of Congress, and bounded cross-source manual
attempts, with an archival next action. All twenty have terminal **online**
research status: nineteen `requires_archival_review`, one
`occupation_only_found`. These statuses do not mean physical files were read.

Seven official [Army bulk-file](https://catalog.archives.gov/id/1263923)
crosswalks establish one confirmed and six high-confidence person identities
through nonshared protected identifiers. The full identifiers are kept private.
Salvatore Disclafani is also named, with the same protected identifier, in
[Marco Patucchi's Operation Ginny account](https://www.repubblica.it/cronaca/2019/03/24/news/world_war_two_italy_the_lost_platoon-222381822/).
It explicitly gives his pre-draft occupation as **polisher**, but names no
employer. The article's construction-company job belongs to his father, not
Salvatore. A [Syracuse University account](https://veterans.syracuse.edu/news/on-veterans-day-we-are-at-our-best-when-we-share-their-stories/)
names Salvatore among the Ginny volunteers and says OSS recruited the group
from U.S. Army ranks. His Army affiliation is therefore published only as a
**qualified medium-confidence** immediate predecessor, pending an individual
transfer record. It is not a civilian employer. No named pre-OSS civilian
employer was established in this cohort.

The page 119 Jacques B DiSibour row, Box 189, resembles a separately indexed
Jacques B DeSibour row, Box 182. They are linked as a *possible* duplicate
group, not merged; the earlier entity's employment claims have not been
copied to this row. The two physical files need comparison. The three
adjacent Jack C, John, and John W Dixon rows also remain separate. All eleven
LoC OCR candidates were rejected after context review. In particular, a
1950 newspaper's John Dixon employed at a Sohio service station has no
identity bridge to the wartime indexed John Dixon and is postwar; he is
**not** included in the oil-company employee category. Another OCR hit
falsely concatenated Raleigh, North Carolina and Roy Dixon. The Boston
University [January 1945 *Bostonia* item](https://open.bu.edu/handle/2144/19538)
for Vance A. Ditrinco documents alumni and wartime service context, not
university employment or a dated pre-OSS sequence. Leonard H Dismore's
printed `British A` and Marcus A Dixon's `French` note remain uninterpreted.

The private database now contains 23,978/23,978 linked source rows and 23,940
active people. Research-attempt coverage is 5,686/23,940 (23.7510%);
confirmed/high employer coverage 264/23,940 (1.1028%); confirmed/high
affiliation coverage 604/23,940 (2.5230%); assessed archival-review coverage
5,641/23,940 (23.5631%). There are 18,254 `not_started` people, 259
possible-duplicate groups, and 124 conflict cases. Private SQLite holds
10,544 research attempts, 4,799 claims (1,308 confirmed; 1,817 high; 1,361
medium; 184 low; 129 conflicting), 4,922 citation records, and 2,262 unique
source-document keys. The public projection has 2,173 affiliations, 678
organizations, 3,728 sources, and 4,611 claims. The complete-index research
goal remains active.

The source review and decisions are replayable from
`research/evidence-page-119-disclafani-through-djuraskovic_batch-588_2026-09-20.json`,
`research/army_review_decisions_2026-09-20_batch588.csv`, and
`research/loc_review_decisions_2026-09-20_batch588.csv`. The Catalog API key
was not used; the Army crosswalk came from an official bulk file, not a
Catalog API response. The next page-119 cohort is rows 41–46.

Local QA passed: seven ingestion checks, SQLite integrity and foreign keys,
111 Python unit tests, the stratified 200-profile audit, Astro type checking
across 217 files, a 24,651-page static build, 72/72 bounded release browser
checks across desktop/phone/tablet (including 30 accessibility checks), all
internal links, and the full public-identifier redaction audit. External URLs
were inventoried, not exhaustively live-checked. Public deployment is a
separate step and is not implied by these local tests.

```bash
python3 -m oss_research assign-page-batch --batch-name batch-588 --page 119 --first-row 21 --last-row 40
python3 -m oss_research research --source cia --batch batch-588 --max-queries 20 --resume
python3 -m oss_research research --source loc --batch batch-588 --max-queries 20 --resume
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch588.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-20_batch588.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-119-disclafani-through-djuraskovic_batch-588_2026-09-20.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```
