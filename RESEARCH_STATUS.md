# Research status

Generated from the current local SQLite database on 2026-07-28/29 UTC.

## Distinct coverage measures

| Measure | Numerator | Denominator | Percent |
|---|---:|---:|---:|
| Index coverage | 23,978 linked source rows | 23,978 printed rows | 100.0000% |
| Research-attempt coverage | 79 people with a non-planned attempt | 23,941 person entities | 0.3300% |
| Verified-employer coverage | 5 people with a confirmed/high published affiliation | 23,941 person entities | 0.0209% |
| Archival-review coverage | 5 people with an individual file-access/priority assessment | 23,941 person entities | 0.0209% |

## Extraction and identity

- PDF pages: 522 / 522
- Source rows: 23,978
- Cautious person entities: 23,941
- Linked source rows: 23,978
- Possible duplicate groups: 202
- Automatic same-name/same-service-number groups: 37
- Same-service-number/different-name candidate groups: 165
- Identity status `confirmed`: 5
- Identity status `high_confidence`: 38
- Identity status `unresolved`: 23,898

## Personnel categories

- Unknown or indeterminate: 16,691
- Enlisted Army personnel: 3,455
- Commissioned Army officers: 2,048
- Civilian professional or administrative grades: 1,424
- Foreign or Allied military personnel: 241
- Enlisted naval personnel: 47
- Commissioned naval officers: 31
- Warrant officers: 4

Commissioned classification: 2,081 yes; 4,937 no; 16,923 indeterminate.

## Research queue and pilot

- `not_started`: 23,862
- `in_progress`: 73
- `candidate_found`: 1
- `verified_employer_found`: 5
- Stratified pilot size: 75
- Pilot difficulty tiers: T1 26; T2 19; T3 15; T4 15
- NARA dry-run plans recorded: 111
- Live CIA exact-name OSS attempts: 176
- Live Library of Congress attempts: 301
- Manual web-discovery plans recorded: 476
- Live NARA requests: 0
- Reviewed NARA digitized-personnel-file attempts: 4
- Total recorded attempts/plans: 1,068
- Library of Congress discovery candidates: 19 total; 17 rejected after
  page-context review and 2 still unreviewed
- Reviewed people with published evidence: 6 (Mort S. Bobrow, Julia C.
  McWilliams, Ralph J. Bunche, William J. Casey, Arthur J. Goldberg, and
  Sterling W. Hayden)
- Published affiliations: 25
- Published claims: 35 (28 confirmed, 5 high, 2 medium)
- Sources supporting public claims: 8
- Canonical organizations: 23
- Conflicts: 0
- NARA pull-list rows: 23,973

Planned dry-run requests do not count as research-attempt coverage.
Medium-confidence published affiliations do not count as verified-employer
coverage.

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
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The same bounded NARA run is available through the manually triggered GitHub
Actions workflow, so local Terminal access is not required once the repository
secret and contact variable are configured.
