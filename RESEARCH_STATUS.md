# Research status

Generated from the current local SQLite database on 2026-07-28/29 UTC.

## Distinct coverage measures

| Measure | Numerator | Denominator | Percent |
|---|---:|---:|---:|
| Index coverage | 23,978 linked source rows | 23,978 printed rows | 100.0000% |
| Research-attempt coverage | 1 person with a non-planned attempt | 23,941 person entities | 0.0042% |
| Verified-employer coverage | 0 people with a confirmed/high published affiliation | 23,941 person entities | 0.0000% |
| Archival-review coverage | 0 people with an individual file-access/priority assessment | 23,941 person entities | 0.0000% |

## Extraction and identity

- PDF pages: 522 / 522
- Source rows: 23,978
- Cautious person entities: 23,941
- Linked source rows: 23,978
- Possible duplicate groups: 202
- Automatic same-name/same-service-number groups: 37
- Same-service-number/different-name candidate groups: 165
- Identity status `high_confidence`: 37
- Identity status `unresolved`: 23,904

## Personnel categories

- Unknown or indeterminate: 16,696
- Enlisted Army personnel: 3,455
- Commissioned Army officers: 2,048
- Civilian professional or administrative grades: 1,421
- Foreign or Allied military personnel: 241
- Enlisted naval personnel: 47
- Commissioned naval officers: 29
- Warrant officers: 4

Commissioned classification: 2,079 yes; 4,934 no; 16,928 indeterminate.

## Research queue and pilot

- `not_started`: 23,940
- `in_progress`: 1
- Stratified pilot size: 75
- Pilot difficulty tiers: T1 26; T2 19; T3 15; T4 15
- NARA dry-run plans recorded: 75
- CIA dry-run plans recorded: 2
- Manual web-discovery plans recorded: 2
- Live NARA requests: 0
- Live Library of Congress attempts: 1
- Total recorded attempts/plans: 80
- Published affiliation claims: 0
- Sources supporting public claims: 0
- Conflicts: 0
- NARA pull-list rows: 23,978

Planned dry-run requests do not count as research-attempt coverage.

## Current blockers

1. Live NARA research requires `NARA_API_KEY` and
   `BEFORE_OSS_CONTACT_EMAIL`. The adapter correctly fails closed without them.
2. A standard NARA key cannot cover this source population in one month. The
   default project soft stop is 9,000 of a 10,000-request allowance; later-month
   continuation or an approved higher quota is required.
3. The CIA Reading Room currently returns a redirect loop in this environment.
   The adapter records access failures and does not bypass the restriction.
4. Completing the minimum research protocol for tens of thousands of people and
   reviewing physical personnel files is continuing archival work, not a single
   automated build step.

## Resume

```bash
python3 -m oss_research nara-check
python3 -m oss_research research --source nara --batch pilot-v1 --max-queries 75
python3 -m oss_research research --source cia --batch pilot-v1 --max-queries 75
python3 -m oss_research research --source loc --batch pilot-v1 --max-queries 75
python3 -m oss_research export-review-queue
python3 -m oss_research import-review-decisions review_decisions.csv
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```
