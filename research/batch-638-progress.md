# Batch 638: PDF pages 451-460 and McGill-McGovern research

All **460** printed rows on original NARA PDF pages 451-460 were compared
against SQLite at 180 dpi. Every page matches the current extraction and
requires no correction. Pages 453, 455, and 456 were already present in the
deterministic random audit, so this batch adds seven pages and 322 rows to the
complete-page ledger. Visual review now covers **380/522 pages** and
**17,446/23,978 rows**: **17,414** reviewed rows match the extraction, **32**
retain reviewed corrections, and **6,532** remain for complete visual
comparison.

The page-309 `Barry McGill` through `William M. McGovern` queue contains 23
source rows representing **23** cautious person entities. Its Library of
Congress pass saved a live result for every person: 16 searches returned no
result and seven people produced 11 discovery candidates. Every official item
and OCR context was inspected. All 11 were rejected as initial conflicts,
unbridged common or famous names, spousal references, or postwar material. The
Northwestern University professor William M. McGovern is not assigned to the
index row from a name match alone. No rejected material is published as
identity or employment evidence.

Nine official Army bulk candidates were reviewed. Eight received
high-confidence identity decisions from nonshared protected identifiers and
exact normalized names or explicitly retained variants. Army-added `Jr.`
suffixes remain visible for William L. McGill and Edward J. McGlynn. The
fixed-width `HARL N` rendering for Harlan McGonigal is retained as a sourced
variant and still requires Box 506 review. Leon A. McGinnis remains
`conflicting`: the protected identifier agrees with an Army Leon McGinnis
entry, but that entry prints middle initial D. The two adjacent David K.
McGinnis rows remain separate ambiguous entities because one is a CAF-11 row
in Box 505, the other is unranked in Box 506, and neither supplies a protected
identifier linking them. Full identifiers stay private. Army grade and
occupation codes were not converted into employers or predecessor
affiliations.

The final 23-person queue state is **20** `in_progress`, two
`needs_identity_review`, and one `conflicting_sources`. All **20** candidates
in the cohort now have review decisions: eight accepted, one conflicting, and
11 rejected. None remains unreviewed. This is research-attempt progress, not
completion of the minimum research protocol. No new employer or affiliation
claim was made.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,786/23,939
(32.5243%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,322/23,939
(26.4088%)**. There are **16,146** `not_started` people, **488** active
possible-duplicate groups, and **165** active people with conflicting identity
or source status. The database stores **12,925** attempts or plans and
**4,957** claims: **1,311** confirmed, **1,944** high, **1,375** medium,
**187** low, and **140** conflicting. It contains **5,068** source/citation
records and **2,386** unique document keys. The public projection contains
**2,224** affiliations, **708** organizations, **3,861** sources, and **4,766**
claims. The oil-company category remains a supported, incomplete evidence set
of seven people across nine companies. Full-index historical research is
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages451-460_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch638.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch638.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page309-mcgill-mcgovern-review_batch-638_2026-09-22.json
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
