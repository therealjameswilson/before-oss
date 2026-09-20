# Batch 601: NARA index pages 129–131, Durkee through Edgell

The original NARA personnel-index PDF pages 129–131 were rendered at 170 dpi
and visually compared with all 138 extracted rows, 46 per page. Names, ranks,
protected-identifier column occupancy, boxes, notes, and archive locations
match. Page 129 was already in the earlier visual sample; pages 130–131 were
newly reviewed. The distinct visual-review ledger is now **103/522 pages**;
**419** pages remain to be visually certified. The full ingest validation
passes: **23,978/23,978** printed rows are linked, all 522 pages are represented,
and SQLite has no foreign-key errors.

Three rate-limited Library of Congress batches searched 46 people each with
138 read-only queries and zero adapter errors or rate-limit blocks. The
adapter saved 20, 39, and 15 newspaper-page candidates on pages 129, 130,
and 131 respectively. All **74** remain unreviewed discovery leads, not
evidence of employment or a completed multi-source protocol. The page cohort
has 21 `candidate_found`, 103 `in_progress`, 12 `needs_identity_review`,
and 2 previously `verified_employer_found` people. No one on these pages
remains `not_started`.

Eight official Army Serial Number Merged File crosswalks were accepted for
**identity only** using exact indexed names plus a nonshared protected
identifier. The review file stores only Army bulk ordinals, not full service
numbers. It makes no employer claims. Six pairs remain separate possible
duplicates: Alfio/Alfred M D'Urso and the two Albert Duryee rows (Box 207),
the two John A Dykes and Edward A Dyro rows (Box 209), the two Paul E Eckel
rows (Box 211), and W I/Wilbur I Eckstrom (Box 212). The Duryee rows have
different protected identifiers. None was merged by name or box.

The page-131 Colonel William A. Eddy already had a high-confidence civilian
employer claim. New review of the original [Hobart and William Smith
yearbook](https://hwslibrary.contentdm.oclc.org/digital/api/collection/p16757coll4/id/14731/download),
printed page 11, establishes that his formal college resignation took effect
in August 1942 even though he had been on Marine active duty since 1941.
The [Marine Corps history](https://www.usmcu.edu/Portals/218/Herringbone%20Cloak%20-%20GI%20Dagger%20Marines%20Of%20The%20OSS.pdf),
chapter II, dates active-duty orders to June 1941, a subsequent Cairo naval
attaché posting, and Donovan's transfer of Eddy into the Coordinator of
Information's North Africa operation by January 1942. The [National Archives
agency history](https://www.archives.gov/research/holocaust/finding-aid/military/rg-226.html)
dates OSS's succession to COI to 13 June 1942. The profile now separately
models last civilian employer (Hobart), concurrent military assignment
(Marine Corps), and immediate pre-OSS institutional affiliation (COI). It
does not claim that the college presidency continued as day-to-day employment
after June 1941 or that Eddy's exact individual OSS transfer day is known.
The Marine publication carries a quotation/reproduction restriction, so only
project-authored paraphrases are stored.

Current local coverage: 23,978 linked source rows; 23,940 active people;
6,234 with saved nonplanned research attempts (26.0401%); 269 with
confirmed/high published employer evidence (1.1236%); 614 with
confirmed/high published affiliation evidence (2.5647%); 5,743 with
archival-review dispositions (23.9891%); 17,706 `not_started` people;
and 271 possible-duplicate groups. Private claim-confidence counts are
1,311 confirmed, 1,860 high, 1,368 medium, 185 low, and 132 conflicting.
The index-wide minimum completed-research protocol is **not** met.

Replay from the repository root after initializing a local SQLite database
and importing earlier checkpoints:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages129-131_2026-09-20.json
python3 -m oss_research import-review-decisions research/review-decisions-army-pages129-131_batch-601_2026-09-20.csv
python3 -m oss_research import-reviewed-evidence research/evidence-eddy-timeline-and-page129-131-duplicates_batch-601_2026-09-20.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

The private SQLite database stays local. The reviewed evidence, identity
decisions, sanitized adapter checkpoints, and redacted public assets are
versioned. No NARA API key was present or used in this checkout.
