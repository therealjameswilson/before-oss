# Research status

Generated from the current local SQLite database on 2026-07-29 UTC.

## Distinct coverage measures

| Measure | Numerator | Denominator | Percent |
|---|---:|---:|---:|
| Index coverage | 23,978 linked source rows | 23,978 printed rows | 100.0000% |
| Research-attempt coverage | 154 people with a non-planned attempt | 23,941 person entities | 0.6432% |
| Verified-affiliation coverage | 71 people with any confirmed/high published pre-OSS affiliation | 23,941 person entities | 0.2966% |
| Verified-employer coverage | 41 people with confirmed/high published employment or self-employment | 23,941 person entities | 0.1713% |
| Archival-review coverage | 80 people with an individual file-access/priority assessment | 23,941 person entities | 0.3342% |

## Extraction and identity

- PDF pages: 522 / 522
- Source rows: 23,978
- Cautious person entities: 23,941
- Linked source rows: 23,978
- Possible duplicate groups: 203
- Automatic same-name/same-service-number groups: 37
- Same-service-number/different-name candidate groups: 165
- Identity status `confirmed`: 6
- Identity status `high_confidence`: 107
- Identity status `probable`: 4
- Identity status `ambiguous`: 1
- Identity status `unresolved`: 23,823

## Personnel categories

- Unknown or indeterminate: 16,661
- Enlisted Army personnel: 3,455
- Commissioned Army officers: 2,052
- Commissioned Marine Corps officers: 4
- Civilian professional or administrative grades: 1,441
- Foreign or Allied military personnel: 241
- Enlisted naval personnel: 47
- Commissioned naval officers: 36
- Warrant officers: 4

Commissioned classification: 2,094 yes; 4,954 no; 16,893 indeterminate.

## Research queue and pilot

- `not_started`: 23,787
- `in_progress`: 83
- `candidate_found`: 1
- `needs_identity_review`: 5
- `documented_prewar_employer_found`: 6
- `occupation_only_found`: 1
- `requires_archival_review`: 6
- `verified_employer_found`: 52
- Stratified pilot size: 75
- Pilot difficulty tiers: T1 26; T2 19; T3 15; T4 15
- NARA dry-run plans recorded: 111
- Live CIA exact-name OSS attempts: 176
- Live Library of Congress attempts: 301
- Manual web-discovery plans recorded: 476
- Live NARA requests: 0
- Reviewed NARA digitized-personnel-file attempts: 4
- Reviewed official-web attempts: 76, including three identity resolutions
  supported by Library of Congress name-authority records
- Total recorded attempts/plans: 1,144
- Library of Congress discovery candidates: 19 total; 17 rejected after
  page-context review and 2 still unreviewed
- Reviewed people with published evidence: 80 (Mort S. Bobrow, Morris Berg,
  Ralph J. Bunche, William J. Casey, Julia C. McWilliams, William E. Colby,
  Arthur J. Goldberg, Virginia Hall, Sterling W. Hayden, Richard M. Helms, John
  Ford, Christian J. Lambertsen, Alfonso Rodriguez, Sidney L. Bartlett, Rene
  Veuve, Jun Atshushi Iwamatsu, Tomoe Iwamatsu, Joseph Savoldi Jr., Peter J.
  Ortiz, Fisher Howe, Betty A. Lussier, Cordelia Dodson, James Angleton, Edna
  W. Andrade, Jane Burrell, Edmund M. Burke, Robert C. Broughton, Barbara J.
  Lauwers, Conrad F. LaGueux, Cora Du Bois, Franklin P. Holcomb, James C. Luce,
  Jeanne H. Taylor, Sherman Kent, Stanley P. Lovell, Walter C. Langer, and
  William L. Langer, William J. Donovan, Carl F. Eifler, David K. E. Bruce,
  Frank G. Wisner, John A. Bross, Kermit Roosevelt Jr., S. Lane Faison Jr.,
  Peter M. F. Sichel, the separately preserved ambiguous Peter M. Sichel index
  row, Aaron Bank, Archimedes L. Patti, Arthur M. Schlesinger Jr., John K.
  Singlaub, John King Fairbank, Walt W. Rostow, Roger Hilsman Jr., Lyman B.
  Kirkpatrick Jr., Ray S. Cline, Paul Mellon, Carleton S. Coon, Norman Holmes
  Pearson, Philip E. Mosely, Millard Preston Goodfellow, Whitney H.
  Shepardson, William Alfred Eddy, Archibald Bulloch Roosevelt Jr., John Hadley
  Nicanor Hemingway, Gertrude Sanford Legendre, DeWitt Clinton Poole, John
  Magruder, Donald Chase Downes, Bruce Campbell Hopper, the probable Leopold
  Schwarzschild identity, Paul Cushing Child, Stewart Johonnot Oliver Alsop,
  Ross Lee Finney, Doris Sharrar Bohrer, Chauncy Dennison Harris, Gardner
  Ackley, Marie Aline Griffith, John William Gardner, Hugh Montgomery, and
  Lucien E. Conein)
- Published affiliations: 156
- Published claims: 237 (32 confirmed, 181 high, 24 medium)
- Citation records: 172; public source export: 169; unique source documents: 164
- Canonical organizations: 113
- Conflicts: 0
- NARA pull-list rows: 23,926

Planned dry-run requests do not count as research-attempt coverage.
Medium-confidence evidence does not count toward either verified measure.
Student, military, government, volunteer, and professional relationships count
toward verified-affiliation coverage but not verified-employer coverage.

## Current blockers

1. Live NARA research requires the `NARA_API_KEY` GitHub Actions secret and
   `BEFORE_OSS_CONTACT_EMAIL` Actions variable. They are not configured, so the
   adapter correctly fails closed without making a request.
2. A standard NARA key cannot cover this source population in one month. The
   default project soft stop is 9,000 of a 10,000-request allowance; later-month
   continuation or an approved higher quota is required.
3. Two William P. Weiss Library of Congress candidates remain unreviewed
   because the underlying page/full-text endpoints began returning access
   errors. They remain candidates, not facts.
4. Completing the minimum research protocol for tens of thousands of people and
   reviewing physical personnel files is continuing archival work, not a single
   automated build step.

## Resume

```bash
python3 -m oss_research nara-check
python3 -m oss_research research --source nara --batch pilot-v1 --max-queries 111 --resume
python3 -m oss_research research --source cia --batch pilot-v1 --max-queries 75 --resume
python3 -m oss_research research --source loc --batch pilot-v1 --max-queries 75 --resume
python3 -m oss_research export-review-queue
python3 -m oss_research import-review-decisions review_decisions.csv
python3 -m oss_research import-reviewed-evidence research/evidence_mort-s-bobrow_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_julia-c-mcwilliams_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_selected-nara-personnel-files_batch-002_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_cia-institutional-biographies_batch-003_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_cia-official-biographies_batch-004_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_cia-loc-aliases_batch-005_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_cia-wartime-pathways_batch-006_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_cia-education-and-service_batch-007_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_official-pathways_batch-008_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_official-pathways_batch-009_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_official-pathways_batch-010_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_institutional-pathways_batch-011_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_official-pathways_batch-012_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_official-pathways_batch-013_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_institutional-pathways_batch-014_2026-07-29.json
python3 -m oss_research import-reviewed-evidence research/evidence_official-institutional-pathways_batch-015_2026-07-29.json
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The same bounded NARA run is available through the manually triggered GitHub
Actions workflow, so local Terminal access is not required once the repository
secret and contact variable are configured.
