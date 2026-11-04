# Batch 1008 progress — PDF page 498

Batch 1008 covers all 46 printed rows on source-index PDF page 498, from
Marjorie J. Werner through T. B. Weston. The page was rendered from the source
PDF and visually inspected at original detail. All 46 extracted rows agree with
the printed table. The two separately printed Robert C. West rows remain two
entities in one name-only review group; no name-only merge was made.

## Reviewed evidence

Eleven exact-name, nonshared protected-identifier comparisons with NARA's
official Army bulk file were accepted. The associated 1942-1944 historical
codes support three student records and eight broad occupation categories.
They identify no named employer, school, workplace or OSS-transfer date. Full
identifiers and raw bulk rows remain private.

The reviewed evidence bundle also records:

- a probable 1941 Doris M. Werntz directory match, qualified as accountant at
  Firestone and not labeled immediate or last-civilian employment;
- a confirmed Theodore A. Wertime identity from the protected Army bridge and
  a direct OSS obituary statement, without a named employer;
- a high-confidence Colonel Paul West identity from a contemporary OSS report
  in Greece, without a pre-OSS affiliation inference;
- a high-confidence Guy Randolph Westmacott identity and a qualified,
  temporally unresolved Grenadier Guards military affiliation from the London
  Gazette;
- a probable First Lieutenant Logan E. Weston identity lead from an official
  Army history, with no OSS sequence inferred;
- an explicit shared-identifier conflict for Roland E. Weschler and an explicit
  Captain-versus-T/5 grade conflict for Arthur J. Westgard.

Search-result snippets, unbridged obituaries, unsourced genealogy, relatives,
postwar-only namesakes and common-name biographies were rejected as final
evidence. No authenticated NARA Catalog API request was made.

## Durable result

All 46 people have saved non-planned research attempts and terminal outcomes:

- 31 `requires_archival_review`
- 12 `occupation_only_found`
- 1 `documented_prewar_employer_found`
- 2 `conflicting_sources`

The bundle adds 10 citation records, two organizations, 13 affiliations and 20
claims: one confirmed, two high, 15 medium and two conflicting. It adds no new
confirmed/high named employer, so verified-employer coverage remains unchanged.

Replay:

```bash
python3 scripts/generate_batch1008_bundle.py
python3 -m oss_research import-review-decisions \
  research/army_loc_entity_review_decisions_2026-11-03_batch1008.csv
python3 -m oss_research import-reviewed-evidence \
  research/evidence-page498-werner-to-weston-review_batch-1008_2026-11-03.json
python3 -m oss_research validate-ingest
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
python3 -m oss_research audit-profiles
```

## Coverage after import

- index coverage: 23,978/23,978 linked rows (100%)
- research-attempt coverage: 16,297/23,935 active people (68.0886%)
- verified-employer coverage: 528/23,935 (2.2060%)
- verified-affiliation coverage: 1,159/23,935 (4.8423%)
- archival-review coverage: 14,773/23,935 (61.7213%)
- not started: 7,633

The next indexed boundary is PDF page 499, row 1, Westphal Mau M. Weston.
