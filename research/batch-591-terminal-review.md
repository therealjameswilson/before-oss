# Batch 591 — PDF page 120, rows 21–46

Reviewed 2026-09-20 UTC. All 26 printed rows were visually checked against
the rendered [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf)
page and remain separate source rows and person entities. The first two rows
are Box 190; most subsequent rows are Box 191. Frank DoGenova is an
out-of-sequence Box 186 entry at 230/86/30/01, and the last row, Laura B
Doll, is Box 192. The other entries show 230/86/30/02. The printed ranks
and location anomalies were not normalized into occupations or employers.
All 26 have durable CIA Reading Room, Library of Congress, and bounded
cross-source review attempts. Online dispositions are 24
`requires_archival_review`, one `occupation_only_found`, and one
`verified_employer_found`. Physical personnel files have not been examined.

The strongest employer finding is [Winfried B. Lerg's dated biography of
Major Patrick Dolan](https://doi.org/10.25969/mediarep/18337), independently
corroborated for wartime OSS identity by the [Eisenhower Presidential Library
finding aid](https://www.eisenhowerlibrary.gov/sites/default/files/finding-aids/pdf/yarrow-bernard-papers.pdf).
Lerg puts Dolan in the advertising department of a Chicago daily called the
*Times* from 1936, at Columbia Records in New York from 1938, and at the
Office of the Coordinator of Information from 1941. Columbia Records is
therefore the last **named civilian employer** before his government work;
the Chicago newspaper is earlier employment. COI is a qualified probable
immediate **government affiliation** before OSS, not a civilian employer.
The exact Columbia departure and individual COI-to-OSS transfer remain to
be verified in Box 191.

The [Academy of Natural Sciences account](https://ansp.org/~/media/Files/ans/membership/Acad_Frontiers_2010-Spring.ashx?la=en)
and a [NARA wartime Tibet account](https://prologue.blogs.archives.gov/2011/02/08/the-oss-and-the-dalai-lama/)
jointly identify Captain Brooke Dolan. His Academy trusteeship began in
1935 and its expeditions are documented, but they do **not** establish paid
employment. [Cornell's OSS reference](https://news.cornell.edu/stories/1998/10/wild-bill-donovan-nuremberg-papers-cu)
and a [1932 federal court opinion](https://law.justia.com/cases/federal/district-courts/FSupp/1/339/1883664/)
identify Otto C Doering Jr. and establish a prewar legal occupation, not a
named law-firm employer. [Confracourt's municipal history](https://mairie-confracourt.fr/wp-content/uploads/sites/679/2018/02/7-octobre-2022.pdf)
documents Captain Simon Doillon's French Resistance role before an OSS
liaison; he is now classified as Allied/foreign military personnel, with no
inferred civilian employer or formal U.S. Army commission. A
[Washington Post obituary](https://www.washingtonpost.com/archive/local/1995/09/26/obituaries/6ef0cb58-9567-4924-9c44-9428ce2c1aae/)
for Margaret Dole Rust explicitly mentions OSS work, but her match to the
index's Margaret Dole remains only probable until Box 191 supplies another
identifier. Her postwar civic roles are not pre-OSS employment.

Five Army bulk entries were accepted as **identity-only** crosswalks for
Donald G Doehring, Michael M Doherty, John Dolence, Rudolph Dolezal, and
Wallace F Doer. Wallace's official bulk surname is spelled with an extra
`r`; the discrepancy is explicit. Andrew J Dolak's protected identifier
matches a bulk entry printed `DOL ANDREW J`, but the material surname
conflict keeps that lead **probable**, not high-confidence. No Army bulk
occupation code was translated into a named employer. Ten LoC OCR
candidates were rejected after context review, including wrong initials,
postwar social notices, and a 1869 namesake. A same-name Foreign Service
career for Frederic R Dolbeare is held privately because no source bridges
it to the indexed Box 191 person.

The prior research-status label for Cordelia Dodson was corrected from
`verified_employer_found` to `requires_archival_review`: her already
published Pentagon/Military Intelligence government assignment and Reed
College student affiliation remain supported, but neither is a named
civilian employer. This correction did not retract the underlying citations.

The database now has 23,978/23,978 linked source rows, 23,940 active people,
and 5,737/23,940 people with a nonplanned research attempt (23.9641%).
Confirmed/high published employer coverage is 265/23,940 (1.1069%);
confirmed/high affiliation coverage is 606/23,940 (2.5313%); assessed
archival-review coverage is 5,692/23,940 (23.7761%). There are 18,203
`not_started` people, 259 possible-duplicate groups, and 124 conflict
cases. Private SQLite holds 10,700 attempts and 4,828 claims (1,308
confirmed; 1,840 high; 1,366 medium; 185 low; 129 conflicting), 4,938
citation records, and 2,275 unique source-document keys. The public
projection contains 2,179 affiliations, 684 organizations, 3,743 sources,
and 4,639 claims. The full-index goal remains unfinished.

This review replays from
`research/evidence-page-120-dodge-through-doll_batch-591_2026-09-20.json`,
`research/army_review_decisions_2026-09-20_batch591.csv`, and
`research/loc_review_decisions_2026-09-20_batch591.csv`. The NARA Catalog
API key was not used; Army identities came from the official bulk file,
not Catalog API responses. Next sequential cohort: PDF page 121, rows
1–20. The site release and live-deployment checks are recorded separately
in `reports/release_batch_591.md` when complete.

```bash
python3 -m oss_research assign-page-batch --batch-name batch-591 --page 120 --first-row 21 --last-row 46
python3 -m oss_research research --source cia --batch batch-591 --max-queries 26 --resume
python3 -m oss_research research --source loc --batch batch-591 --max-queries 26 --resume
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch591.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-20_batch591.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-120-dodge-through-doll_batch-591_2026-09-20.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```
