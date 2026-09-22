# Batch 637: PDF pages 441-450 and McFaddin-McGhee research

All **460** printed rows on original NARA PDF pages 441-450 were compared
against SQLite at 180 dpi. Every page matches the current extraction and
requires no correction. Pages 442, 444, and 447 were already present in the
deterministic random audit, so this batch adds seven pages and 322 rows to the
complete-page ledger. Visual review now covers **373/522 pages** and
**17,124/23,978 rows**: **17,092** reviewed rows match the extraction, **32**
retain reviewed corrections, and **6,854** remain for complete visual
comparison.

The page-308 `Lawerence B. McFaddin` through `William M. McGhee` queue contains
23 source rows representing **23** cautious person entities. Its Library of
Congress pass saved a live result for every person and created 11 discovery
candidates across six people. Every official item and OCR context was
inspected. All 11 were rejected because their names or initials conflicted or
because the item supplied no rank, protected-identifier, OSS, or Box 505 bridge.
The rejected material is not published as identity or employment evidence.

Eleven official Army bulk candidates were reviewed. Ten received
high-confidence identity decisions from nonshared protected identifiers and
exact normalized names or explicitly retained variants. The variants include
Lawerence/Lawrence, Frank/Francis J., an Army `MCTFARLAND` rendering, and an
Army-added middle initial. The anomalous Army grade code for William M. McGhee
remains uninterpreted. The official Army entry supports the McGaragle spelling
for William C. McGaragle, but his protected identifier is also printed for
William C. McAragle on page 303. Both people remain separate and ambiguous
pending comparison of Boxes 496 and 505. The neighboring Edward A.
McCaughy/McGaughy cluster likewise remains separate and ambiguous. Full
identifiers stay private. Army grade and occupation codes were not converted
into employers or predecessor affiliations.

The final 23-person queue state is **20** `in_progress` and three
`needs_identity_review`. All **24** candidates in the cohort now have review
decisions: ten accepted, three probable, and 11 rejected. None remains
unreviewed. This is research-attempt progress, not completion of the minimum
research protocol. No new employer or affiliation claim was made.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,763/23,939
(32.4283%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,313/23,939
(26.3712%)**. There are **16,167** `not_started` people, **488** active
possible-duplicate groups, and **164** active people with conflicting identity
or source status. The database stores **12,890** attempts or plans and
**4,948** claims: **1,311** confirmed, **1,936** high, **1,375** medium,
**187** low, and **139** conflicting. It contains **5,066** source/citation
records and **2,385** unique document keys. The public projection contains
**2,224** affiliations, **708** organizations, **3,859** sources, and **4,757**
claims. The oil-company category remains a supported, incomplete evidence set
of seven people across nine companies. Full-index historical research is
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages441-450_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch637.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch637.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page308-mcfaddin-mcghee-review_batch-637_2026-09-22.json
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
