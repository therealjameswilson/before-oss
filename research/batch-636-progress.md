# Batch 636: PDF pages 431-440 and McDowell-McFadden research

All **460** printed rows on original NARA PDF pages 431-440 were compared
against SQLite at 180 dpi. Every page matches the current extraction and
requires no correction. This batch adds ten pages and 460 rows to the
complete-page ledger. Visual review now covers **366/522 pages** and
**16,802/23,978 rows**: **16,770** reviewed rows match the extraction, **32**
retain reviewed corrections, and **7,176** remain for complete visual
comparison.

The page-308 `Robert H. McDowell` through `Thomas J. McFadden` queue contains
23 source rows representing **21** cautious person entities. Its Library of
Congress pass saved one live result for every person and created four discovery
candidates across three people. Every official item context was inspected. All
four were rejected because they were an unbridged draft-list name, an unrelated
nineteenth-century boxer, an 1893 deed reference, or a different-initial legal
notice.

Four official Army bulk candidates were reviewed. Charles W. McFadden received
a high-confidence identity crosswalk from exact normalized name and a
nonshared protected identifier. Two candidates for the two preserved Stuart P.
McFadden index rows resolve to the same official Army record; the one cautious
person entity remains linked to both immutable source rows and retains a
duplicate-review flag. The protected identifier printed for Edward C. McElroy
instead resolves to a wholly different Army name. That Army identity was not
assigned, and the profile is explicitly `conflicting_sources` pending Box 504
review. Full identifiers and the unrelated Army name remain private. Army
grades and occupation codes were not converted into employers or predecessor
affiliations.

The two identical Robert D. McFadden rows remain separate immutable source
records linked to one high-confidence entity because the printed name, rank,
box, and protected identifier agree. The file still requires review to explain
why the person appears twice. The final 21-person queue state is **20**
`in_progress` and one `conflicting_sources`. All **eight** candidates have
review decisions; none remains unreviewed. This is research-attempt progress,
not completion of the minimum research protocol. No new employer or
affiliation claim was made.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,742/23,939
(32.3405%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,303/23,939
(26.3294%)**. There are **16,187** `not_started` people, **488** active
possible-duplicate groups, and **164** active people with conflicting identity
or source status. The database stores **12,850** attempts or plans and
**4,937** claims: **1,311** confirmed, **1,926** high, **1,375** medium,
**187** low, and **138** conflicting. It contains **5,064** source/citation
records and **2,384** unique document keys. The public projection contains
**2,224** affiliations, **708** organizations, **3,857** sources, and
**4,746** claims. The oil-company category remains a supported, incomplete
evidence set of seven people across nine companies. Full-index historical
research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages431-440_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch636.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch636.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page308-mcdowell-mcfadden-review_batch-636_2026-09-22.json
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
