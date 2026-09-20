# Batch 597 — PDF page 125, Dresden through Dubuc

Reviewed 2026-09-20 UTC. All 46 printed rows on page 125 of the original [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf) were compared with the stored extraction and matched without correction. Page 125 was already in the extraction QA sample, so the distinct visually reviewed page count remains **99**. All 522 PDF pages and all parser-warning rows still pass the recorded extraction gates. These 46 rows are linked to 46 separate active people; no same-name rows were merged by convenience.

A bounded [Library of Congress API](https://www.loc.gov/apis/) pass made 46 successful, rate-limited read-only discovery searches with no blocked requests or errors. Six candidate links for five people remain **unreviewed** because the underlying item pages were not accessible in the source reader. They are not evidence of an employer. All 46 page-125 people have at least one saved nonplanned attempt, but the one-query discovery pass does not complete the minimum historical research protocol. Eight page-125 candidates were privately accepted as identity-only matches to the official [Army Serial Number Merged File](https://catalog.archives.gov/id/1263923) using exact full name and unique protected identifier (seven cases), or a recorded surname-spacing variant plus unique identifier (one case). The decisions are in `research/army_review_decisions_2026-09-20_batch597.csv`; no bulk occupation code was turned into an employer claim. No authenticated NARA Catalog API request was made.

The [wartime OSS personnel interview-board proceedings](https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full), held in Caserta on 4–5 May 1944 and hosted by Hoover Institution, yielded two direct pre-OSS findings beyond the discovery pass:

- Martin L Druckenmiller, page 125 row 21, Box 200: the board's PDF page 19 matches the indexed full name and a unique protected identifier, corroborated by the official Army bulk entry. It explicitly places him in a U.S. Army replacement center in Africa immediately before his March 1944 OSS assignment. It calls him a draftsman in civilian life but **does not name a civilian employer**. The Army pathway and occupation are separate claims. The OCR of the board's [accompanying index](https://digitalcollections.hoover.org/internal/media/dispatcher/331574/full) transcribes a different first name; its page image has not been checked, so this is flagged rather than silently accepted as an alias. Box 200 should be reviewed for a named civilian employer and the variant.
- Robert Gamble, page 161 row 24, Box 261: the board's PDF page 22 agrees with the NARA index on full name, sergeant rank, and a unique protected identifier. It says he worked for the **Packard Car Company in Detroit** in civilian life, entered the Army in December 1942, and was assigned OSS in February 1943. Packard is therefore a directly documented **earlier** pre-OSS employer, not a demonstrated last civilian employer; no Packard job title or employment dates are supplied. His immediate formal pathway was military service. Packard Car Company is preserved as the historical name found, not silently merged with Packard Motors Export Corporation.
- Robert J Koch, page 254 row 41, Box 414: the board's PDF page 3 names a major of that name and mentions civilian work, but its OCR-transcribed protected identifier differs from the index row. Without examining the original image and personnel file, the apparent match is an **identity lead only**. No employer or immediate affiliation is assigned to this indexed person.

The reviewed evidence bundle `research/evidence-page-125-dresden-dubuc_batch-597_2026-09-20.json` adds five citation records, three affiliations, six claims, three manual source-review attempts, and three person updates. Public evidence uses brief excerpts or project-authored paraphrases; full identifiers remain private. Page-125 statuses are 39 `in_progress`, five `candidate_found`, one previously `documented_prewar_employer_found`, and one `requires_archival_review`. The first 44 still need substantive source review or disambiguation. The third source-reviewed person, Koch, is outside the page-125 queue and remains `needs_identity_review`.

Project-wide index coverage is **23,978/23,978** linked rows; research-attempt coverage **5,963/23,940** people (24.9081%); verified-employer coverage **268/23,940** (1.1195%); verified-affiliation coverage **612/23,940** (2.5564%); archival-review assessment **5,711/23,940** (23.8555%). `not_started` is **17,977**. Private attempts total **10,948**; private claim confidence is 1,311 confirmed, 1,852 high, 1,368 medium, 185 low, and 131 conflicting. Source citations total **4,957** across **2,290** unique document keys. The existing [oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/) remains six cited employees at eight historical oil companies; Packard is not an oil employer.

Replay and resume:

```bash
python3 -m oss_research assign-page-batch --batch-name page-125-dresden-dubuc-b597 --page 125 --first-row 1 --last-row 46
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch597.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-125-dresden-dubuc_batch-597_2026-09-20.json
python3 -m oss_research research --source loc --batch page-125-dresden-dubuc-b597 --max-queries 20 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

The current CIA Reading Room robots policy disallows automated search. The LoC candidates require item-level inspection. The Hoover index OCR discrepancy and Koch's identifier conflict require original-page and personnel-file review. Neither absence of an online employer nor a single automated query proves that a person had no prior employer.
