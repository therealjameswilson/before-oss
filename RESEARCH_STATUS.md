# Research status

Generated from the current local SQLite database on 2026-07-29 UTC.

## Distinct coverage measures

| Measure | Numerator | Denominator | Percent |
|---|---:|---:|---:|
| Index coverage | 23,978 linked source rows | 23,978 printed rows | 100.0000% |
| Research-attempt coverage | 130 people with a non-planned attempt | 23,941 person entities | 0.5430% |
| Verified-affiliation coverage | 48 people with any confirmed/high published pre-OSS affiliation | 23,941 person entities | 0.2005% |
| Verified-employer coverage | 24 people with confirmed/high published employment or self-employment | 23,941 person entities | 0.1002% |
| Archival-review coverage | 56 people with an individual file-access/priority assessment | 23,941 person entities | 0.2339% |

## Extraction and identity

- PDF pages: 522 / 522
- Source rows: 23,978
- Cautious person entities: 23,941
- Linked source rows: 23,978
- Possible duplicate groups: 203
- Automatic same-name/same-service-number groups: 37
- Same-service-number/different-name candidate groups: 165
- Identity status `confirmed`: 6
- Identity status `high_confidence`: 84
- Identity status `probable`: 3
- Identity status `ambiguous`: 1
- Identity status `unresolved`: 23,847

## Personnel categories

- Unknown or indeterminate: 16,670
- Enlisted Army personnel: 3,455
- Commissioned Army officers: 2,052
- Commissioned Marine Corps officers: 2
- Civilian professional or administrative grades: 1,434
- Foreign or Allied military personnel: 241
- Enlisted naval personnel: 47
- Commissioned naval officers: 36
- Warrant officers: 4

Commissioned classification: 2,092 yes; 4,947 no; 16,902 indeterminate.

## Research queue and pilot

- `not_started`: 23,811
- `in_progress`: 82
- `candidate_found`: 1
- `needs_identity_review`: 4
- `documented_prewar_employer_found`: 3
- `occupation_only_found`: 1
- `requires_archival_review`: 2
- `verified_employer_found`: 37
- Stratified pilot size: 75
- Pilot difficulty tiers: T1 26; T2 19; T3 15; T4 15
- NARA dry-run plans recorded: 111
- Live CIA exact-name OSS attempts: 176
- Live Library of Congress attempts: 301
- Manual web-discovery plans recorded: 476
- Live NARA requests: 0
- Reviewed NARA digitized-personnel-file attempts: 4
- Reviewed official-web attempts: 51, including three identity resolutions
  supported by Library of Congress name-authority records
- Total recorded attempts/plans: 1,119
- Library of Congress discovery candidates: 19 total; 17 rejected after
  page-context review and 2 still unreviewed
- Reviewed people with published evidence: 56 (Mort S. Bobrow, Morris Berg,
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
  Kirkpatrick Jr., Ray S. Cline, and Paul Mellon)
- Published affiliations: 108
- Published claims: 155 (28 confirmed, 109 high, 18 medium)
- Citation records: 106; public source export: 103; unique source documents: 102
- Canonical organizations: 79
- Conflicts: 0
- NARA pull-list rows: 23,941

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
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The same bounded NARA run is available through the manually triggered GitHub
Actions workflow, so local Terminal access is not required once the repository
secret and contact variable are configured.
