# Batch 634: PDF pages 411-420 and McDaniel-McDonald research

All **460** printed rows on original NARA PDF pages 411-420 were compared
against SQLite at 180 dpi. Every page matches the current extraction and
requires no correction. This adds ten pages and 460 rows to the complete-page
ledger. Visual review now covers **347/522 pages** and **15,928/23,978 rows**:
**15,896** reviewed rows match the extraction, **32** retain reviewed
corrections, and **8,050** remain for complete visual comparison.

The complete page-307 `Charles W. McDaniel` through `Kenneth C. McDonald`
queue contains **23** people. Its Library of Congress pass saved one live
result for every person and created **21** discovery candidates across seven
people. Every official item context was inspected, including a direct official
OCR fetch for the one item whose first JSON response was malformed. All 21
candidates were rejected because they concerned conflicting initials,
unrelated or contextless names, postwar material, or common names without an
indexed-person bridge.

Six official Army bulk candidates were reviewed. Gene A. McDaniel, Dewey E.
McDonald, George S. McDonald, Georgie R. McDonald, and Jasper N. McDonald
received high-confidence identity crosswalks from exact normalized names and
nonshared protected identifiers. Fixed-width `MC DANIEL` and `MC DONALD`
spacing is treated as formatting, not a public name variant. Differences
between Army-entry and index grades remain chronology questions for the
personnel file; neither Army grades nor occupation codes were converted into
employers or predecessor affiliations. The protected identifier printed for
indexed Private James E. McDaniel instead resolves to a wholly different Army
name. That Army identity was not assigned to McDaniel; his profile is
explicitly `conflicting_sources` pending Box 502 review.

The Dervey A. McDonald and Hervey A. McDonald rows remain separate ambiguous
entities in duplicate group `p307-dervey-hervey-mcdonald-b623`. They share a
printed protected identifier but have different names and ranks. Name
similarity and identifier reuse do not justify merging immutable rows or
person entities without comparison of both Box 502 files.

The final 23-person queue state is **20** `in_progress`, two
`needs_identity_review`, and one `conflicting_sources`. All **29** candidates
have review decisions; none remains unreviewed. This is research-attempt
progress, not completion of the minimum research protocol. No new employer or
affiliation claim was made.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,698/23,939
(32.1567%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,300/23,939
(26.3169%)**. There are **16,229** `not_started` people, **488** active
possible-duplicate groups, and **161** active people with conflicting identity
or source status. The database stores **12,781** attempts or plans and
**4,928** claims: **1,311** confirmed, **1,920** high, **1,375** medium,
**187** low, and **135** conflicting. It contains **5,060** source/citation
records and **2,382** unique document keys. The public projection contains
**2,224** affiliations, **708** organizations, **3,853** sources, and
**4,737** claims. The oil-company category remains a supported, incomplete
evidence set of seven people across nine companies. Full-index historical
research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages411-420_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch634.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch634.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page307-mcdaniel-mcdonald-review_batch-634_2026-09-22.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research and visual-audit batch, then rebuild:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, copyrighted page image, or
private reviewer note is committed or included in the public site. No
authenticated NARA Catalog request was made.
