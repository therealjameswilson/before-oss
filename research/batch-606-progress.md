# Batch 606: pages 138–140 and bounded research

Rendered PDF pages 138, 139, and 140 at 180 dpi and checked every one of
their **138 printed rows** against the immutable SQLite extraction. All
rows matched; no parser correction was needed. The distinct visual-review
ledger is now **111/522 pages**, leaving **411** pages. Page 139 prints two
consecutive `Ruth E Evans` rows in Box 225. Both source rows and both person
entities remain separate, with a shared possible-duplicate group and a Box
225 review request. Page 140 prints the similar `Frank B Falkner` and `Frank
B Falknor` records; their existing private-identifier conflict remains
flagged for review, not silently merged.

The first-pass Library of Congress adapter completed **45/45** searches for
the page-138 batch and **9/9** for the first page-139 batch. It saved **5**
and **20** unreviewed newspaper-page discovery leads respectively. None is
an accepted identity, employment claim, or completed multi-source research
protocol. The remaining **36** page-139 and **46** page-140 people are
assigned to durable batches but have **not** received this LoC pass. Their
`not_started` and existing statuses remain visible. The first page-139 run
stopped after an incomplete HTTP body. The LoC adapter now retries that
specific transient failure, records an exhausted failure, and resumes only
unfinished searches. No authenticated NARA Catalog request was made.

[John King Fairbank's](https://therealjameswilson.github.io/before-oss/people/e091453b-28d3-5f35-a907-415c62dfc364/)
page-140 profile now distinguishes two questions. A [USC institutional
article](https://uschinatoday.org/features/2007/11/09/john-king-fairbank-present-at-the-creation/)
dates his work for the Coordinator of Information to 1941; the
[NARA RG 226 agency history](https://www.archives.gov/research/holocaust/finding-aid/military/rg-226.html)
dates OSS succession to June 1942; a [Harvard Fairbank Center
interview](https://fairbank.fas.harvard.edu/research/blog/madame-fairbanks-living-room/)
places his OSS collecting in China in 1942–43. COI is therefore published
only as a **probable immediate government assignment, medium confidence**;
the individual transfer date and exact COI position are unknown. Harvard
University remains the separately documented last civilian employer.
Neither COI nor these sources establish a new verified civilian employer.

At this checkpoint, **23,978/23,978** source rows link to **23,940** active
people. **6,559/23,940** have a nonplanned research attempt (27.3977%);
**271/23,940** have confirmed/high published employer evidence (1.1320%);
**617/23,940** have confirmed/high published affiliation evidence (2.5773%);
and **5,769/23,940** have an assessed archival-review disposition
(24.0977%). **17,381** remain `not_started`; there are **281**
possible-duplicate groups. SQLite retains **11,604** attempts or plans and
**4,867** claims: 1,311 confirmed, 1,868 high, 1,371 medium, 185 low, and
132 conflicting. It has **5,006** source/citation records and **2,334**
unique source-document keys. The public projection has **2,204**
affiliations, **694** organizations, **3,803** sources, and **4,678** claims.
The featured oil-company category remains **seven** cited employees; the
first-pass searches did not change it. Full-index research is unfinished.

Local QA passed: 124 Python unit tests; the bounded desktop, phone, and
tablet release/browser/accessibility suite; the 200-profile structural
audit; the 24,693-page internal-link check; public-data redaction checks;
and the static Astro build. The structural profile sample is not a manual
source audit. External URLs were inventoried but not all live-checked.

## Replay and continuation

After importing earlier batches into the private SQLite database:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_page138_2026-09-21.json
python3 -m oss_research import-page-reviews research/parser_visual_review_page139_2026-09-21.json
python3 -m oss_research import-page-reviews research/parser_visual_review_page140_2026-09-21.json
python3 -m oss_research assign-page-batch --batch-name page-138-escoute-evans-b606 --page 138 --first-row 2 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-139-evans-a-b606 --page 139 --first-row 1 --last-row 9
python3 -m oss_research assign-page-batch --batch-name page-139-evans-fairbairn-b606 --page 139 --first-row 11 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-140-fairbairn-farber-b606 --page 140 --first-row 1 --last-row 46
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-reviewed-evidence research/evidence-page139-ruth-evans-duplicate-review_batch-606_2026-09-21.json
python3 -m oss_research import-reviewed-evidence research/evidence-john-king-fairbank-coi_batch-606_2026-09-21.json
python3 -m oss_research research --source loc --batch page-139-evans-fairbairn-b606 --max-queries 36 --resume
python3 -m oss_research research --source loc --batch page-140-fairbairn-farber-b606 --max-queries 46 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

Page 138, row 1 (`Pierre Escot`) and page 139, row 10 (`Margaret Evans`)
already belong to the pilot batch and were preserved there. The API key
was not used, copied into the repository, or emitted to public assets.
The private SQLite database is not committed; replay checkpoints contain
sanitized attempt metadata, not raw external response payloads.
