# Batch 586 — PDF page 118, rows 31–46

Reviewed 2026-09-20 UTC. The final sixteen printed rows on page 118 of
[NARA's OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf)
were compared with a rendered page image. Rows 31–35 are in Box 187; rows
36–46 are in Box 188. Every printed row remains distinct. The source lists
Charles DiMary as `Capt` but does not specify a service branch; the index
category is therefore indeterminate while the commissioned-officer filter
still includes the printed captain rank.

All sixteen have saved bounded CIA Reading Room and Library of Congress
searches, exact-name OSS and employment/occupation variants, a contextual
institutional or archival check, and a manual terminal online review. Six
[official Army bulk-file](https://catalog.archives.gov/id/1263923) matches
establish high-confidence identity only for Nick L DiMarco, Salvatore
DiMattino/Di Mattino, Orlando F Dimenna, Gaetano Dimille/Di Mille, Victor
Dimitrijevich, and Richard S Dinner. Each match has a nonshared private
identifier and name agreement. No full identifier or Army occupation code
is published as an employer.

The strongest employment evidence is a contemporaneous
[OSS Cairo field-board interview with Martin Dinga](https://digitalcollections.hoover.org/internal/media/dispatcher/331585/full),
interview LVI, printed pp. 62–63 (PDF pp. 65–66). Dinga identifies the
**Red Cross** as the affiliation immediately before his March 1944 OSS
recruitment in Cairo. A later compensation question supports treating the
role as civilian employment, although its exact job title and the national
Red Cross society are unspecified. The public organization is therefore
`Red Cross (society unspecified)`; it is **not** silently merged with the
American Red Cross. Dinga also describes earlier children's-aid and
settlement-house social work in New York City without naming an employer.
That earlier statement is published as occupation evidence only. The
Hoover-hosted PDF supplies a direct wartime OSS interview; its bracketed
project source title is descriptive because an item-level catalog title was
not available from the accessible media link. Unrelated personal and
medical information in the larger transcript is neither retained nor
published.

A [Harvard Law Bulletin class notice](https://hls.harvard.edu/wp-content/uploads/2008/09/WEB-HLB-f08-NCN.pdf)
independently identifies Eugene A. Dinet Jr. with WWII OSS service, matching
the indexed full name and suffix at high confidence. The notice's law-school
class and teaching career are postwar, so no pre-OSS employer was assigned.
For Charles DiMary, a
[French military historical-service file list](https://afmd.org/files/images/Glossaire/SHDGR_28P4.pdf)
points to dossier GR 28 P 4 19–541 for Charles Dimary, and a
[French diplomatic-archives finding aid](https://archivesdiplomatiques.diplomatie.gouv.fr/media/ae642036-2a55-4064-9cd5-7d43604998c2.pdf)
lists a Captain Dimary in Albert Kammerer's papers, 94PAAP28. These name/rank
clues do not directly link the French person to the indexed Box 187 file or
name his prior employer. They remain review leads, not a published identity
or occupation assertion.

Six LoC newspaper candidates were read in the official OCR context: five
rejected and one retained as private plausible. The five Alaska references
for incomplete `D M Dimond` concern Delegate **Anthony J** Dimond and cannot
be attached to the indexed person. A
[1940 *Key West Citizen* page](https://www.loc.gov/resource/sn83016244/1940-07-20/ed-1/?sp=1)
names engineer John M Dimick, matching the indexed name and initial, but
gives no OSS or Box 188 identifier. No engineer claim was published for the
index person. Later institutions named for Richard S Dinner and modern or
genealogical namesakes likewise were not treated as pre-OSS employers.

Fifteen people have terminal online `requires_archival_review` dispositions;
Martin Dinga has terminal `verified_employer_found` with Box 188 still useful
for the exact Red Cross society and earlier chronology. These statuses
describe completed *bounded online review*, not examination of the physical
files. No reliable pre-OSS employer has yet been identified in accessible
sources reviewed for the other fifteen; that is not a claim they had none.
The NARA Catalog API was not used in this cohort. The Army crosswalk uses a
separately published official bulk file and consumes no Catalog API quota.

After import, the private database has 23,978/23,978 linked index rows and
23,940 active people. Nonplanned research-attempt coverage is 5,646/23,940
(23.5840%); confirmed/high published employer coverage is 264/23,940
(1.1028%); confirmed/high published affiliation coverage is 603/23,940
(2.5188%); and assessed archival-review coverage is 5,601/23,940
(23.3960%). There remain 18,294 `not_started` people, 258 possible-duplicate
groups, and 124 conflict cases. The private database has 10,424 attempts,
4,775 claims (1,307 confirmed; 1,795 high; 1,360 medium; 184 low; 129
conflicting), 4,912 citation records, and 2,254 unique source-document
keys. The public projection has 2,170 affiliations, 678 organizations,
3,718 sources, and 4,587 claims. Full-index research is not complete.

Resume or reproduce this cohort against the existing private SQLite file:

```bash
python3 -m oss_research assign-page-batch --batch-name batch-586 --page 118 --first-row 31 --last-row 46
python3 -m oss_research research --source cia --batch batch-586 --max-queries 16 --resume
python3 -m oss_research research --source loc --batch batch-586 --max-queries 16 --resume
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch586.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-20_batch586.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-118-dilworth-through-dinner_batch-586_2026-09-20.json
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

Assignments, fingerprints, decisions, and evidence import are idempotent.
LoC decisions require private discovery candidates to be replayed first.
The next bounded cohort begins on PDF page 119, row 1.
