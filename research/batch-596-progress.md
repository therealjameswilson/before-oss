# Batch 596 — PDF page 124, Downey through Drendel

Re-reviewed 2026-09-20 UTC. All 46 printed rows on page 124 of the original [NARA OSS personnel index](https://www.archives.gov/files/iwg/declassified-records/rg-226-oss/personnel-database.pdf) were compared with the stored extraction and matched without correction. This includes two separate Millard P Downey rows, the Fred B Drake `also AS` note, Rene Drap's `French` note and S/Lt rank, and the Box 197–199 transitions. The matching decision is replayable from `research/parser_visual_review_page124_2026-09-20.json`. Page 124 was already among the extraction sample's visually reviewed pages, so the distinct-page total remains 99; the extraction validation still passes all 522 page-coverage and low-confidence-row gates.

A bounded [Library of Congress API](https://www.loc.gov/apis/) pass made 46 successful, rate-limited read-only searches, with zero blocked requests or errors and two duplicate query fingerprints skipped. It retained 22 **unreviewed discovery candidates** for ten people. Neither a newspaper hit nor a search snippet is an employer claim. All 46 people now have a recorded nonplanned research attempt, but 42 still need substantive source review or disambiguation beyond that pass. The sanitized adapter checkpoints are in `research/adapter_attempt_checkpoints.json`.

Source-reviewed findings:

- Donald M Dozer, Box 198 row 18: a contemporary [*Maryland Historical Magazine* article](https://msa.maryland.gov/megafile/msa/speccol/sc5800/sc5881/000001/000000/000142/pdf/msa_sc_5881_1_142.pdf) identifies Donald Marquand Dozer with the University of Maryland in June 1941. An independently inspected [*Washington Post* obituary](https://www.washingtonpost.com/archive/local/1980/08/16/donald-m-dozer-professor-expert-on-latin-america/4ed6f37c-a45b-490d-a713-322fb000c383/) says he joined Maryland's faculty in 1937 and moved to government intelligence service in 1942. Maryland is published as a high-confidence **last civilian employer before wartime government service**, not as a proved immediate predecessor to OSS. His 1936 State Department archivist role is a separate, qualified earlier government assignment. The specific 1942 intelligence office and exact OSS-entry date require Box 198. A University of California memorial PDF was access-challenged and its search snippet was not used as evidence.
- Alexis N Dragnich, Box 198 row 23: [Vanderbilt University's obituary](https://news.vanderbilt.edu/2009/08/12/political-scientist-alex-n-dragnich-dead-at-97-86530/) identifies an **Alex N** Dragnich in OSS, but the index prints **Alexis N**. No inspected source directly bridges the name forms. Doctoral study is not employment and later Vanderbilt teaching is not pre-OSS work. The identity remains probable, with `needs_identity_review` and no employer claim.
- A protected-identifier crosswalk to the official [Army Serial Number Merged File](https://catalog.archives.gov/id/1263923) yielded seven exact full-name/nonshared-identifier matches. These are accepted as **private identity-only decisions** for William D Downey, Alfred E Downs, David W Doyle, Donald E Dozois, Frank L Drago, Kenneth W Drake, and John W Draper; none is promoted to a public biography or employer claim. Two crosswalks conflict with the index: Myftar S Dragoti maps to a wholly different Army name, and the indexed middle initial for Spiros D Drakos differs from the bulk record. Both are published only as labeled identity conflicts, with no employer inferred. Full identifiers remain private.

The reviewed evidence bundle `research/evidence-page-124-downey-drendel_batch-596_2026-09-20.json` adds six citation records, two affiliations, five claims, four manual source-review attempts, and four person updates. The seven accepted and two conflicting Army decisions are in `research/army_review_decisions_2026-09-20_batch596.csv`. No authenticated NARA Catalog API request was made; the official Army file was an unrestricted bulk source, not a Catalog API response.

Page-124 statuses are 32 `in_progress`, ten `candidate_found`, two `conflicting_sources`, one `verified_employer_found`, and one `needs_identity_review`. The 42 in-progress/candidate people have **not** completed the minimum multi-source research protocol. Project-wide index coverage is **23,978/23,978** linked rows; research-attempt coverage **5,916/23,940** people (24.7118%); verified-employer coverage **267/23,940** (1.1153%); verified-affiliation coverage **610/23,940** (2.5480%); archival-review assessment **5,708/23,940** (23.8429%). `not_started` is **18,024**. Private attempts total **10,899**; claim confidence is 1,308 confirmed, 1,849 high, 1,368 medium, 185 low, and 131 conflicting. Source citations total 4,952 across 2,286 unique document keys.

The homepage and dedicated [oil-company category](https://therealjameswilson.github.io/before-oss/oil-companies/) remain restricted to six people with cited employment claims at eight historical oil companies. The batch adds a distinct “Evidence conflicts” section to affected person profiles, and the browser suite checks that disputed identity evidence does not create an employer or oil-category membership.

Replay and resume:

```bash
python3 -m oss_research import-page-reviews research/parser_visual_review_page124_2026-09-20.json
python3 -m oss_research assign-page-batch --batch-name page-124-downey-drendel-b596 --page 124 --first-row 1 --last-row 46
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research import-review-decisions research/army_review_decisions_2026-09-20_batch596.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page-124-downey-drendel_batch-596_2026-09-20.json
python3 -m oss_research research --source loc --batch page-124-downey-drendel-b596 --max-queries 20 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research coverage-report
python3 -m oss_research build-public-data
```

CIA Reading Room automated search remains disallowed by the current robots policy. The Army name/initial conflicts require personnel-file comparison; neither should be silently corrected. Dozer's exact transfer chronology, Dragnich's name bridge, and most other page-124 employer questions still require further archival or institutional research.
