# Batch 641: PDF pages 481-490 and McKee-McKiernan research

All **460** printed rows on original NARA PDF pages 481-490 were compared
against SQLite at 180 dpi. Pages 481, 486, and 489 were already present in
the deterministic random audit, so this batch adds seven pages and **322**
rows to the complete-page ledger. Every page matches the current extraction
and requires no correction. Visual review now covers **405/522 pages** and
**18,596/23,978 rows**: **18,564** reviewed rows match the extraction, **32**
retain reviewed corrections, and **5,382** remain for complete visual
comparison.

The page-311 `Eugene F. McKee` through `William F. McKiernan` queue contains
23 source rows representing **23** cautious person entities. Its Library of
Congress pass saved a live outcome for every person. The pass created 12 new
newspaper candidates, and six preexisting official Army candidates brought
the cohort total to 18. All 12 newspaper item contexts were inspected and
rejected because they identify a different name or initial, are postwar, are
a spouse-form mention, or provide no rank, protected-identifier, Box 508-509,
or OSS bridge. The rejected results include people styled A.G., M., W.M., or
Katheryn McKenzie; postwar state senator John L. McKeon; an 1847 district
attorney John McKeon; Mrs. Samuel A. McKee; Industrial Foremen's Club
president William B. McKenzie; and William K. McKenzie in a traffic listing.
Their offices, organizations, and occupations are not transferred to the
indexed people.

Five official Army bulk candidates received high-confidence identity
decisions. Howard R. McKee, Samuel R. McKee, A.Q. McKenzie, Francis W.
McKenzie, and Louis F. McKenzie each have an exact normalized-name match and
a nonshared protected identifier. Fixed-width `MC KEE` and `MC KENZIE`
spacing, Army grades, entry dates, and occupation codes are identity context,
not employer evidence.

One protected-identifier conflict remains visible. The identifier printed for
James A. McKenskey points to an official Army entry for Philip Cappella. The
names conflict completely, so James remains `conflicting`, requires critical
Box 509 review, and receives no identity or employment inference from that
record. The full identifier is excluded from public output.

The two adjacent Lieutenant Colonel Stewart L. McKenney rows share the same
name, rank, box, and archival location but carry different protected
identifiers. They remain separate ambiguous entities in possible-duplicate
group `page311-stewart-l-mckenney`. Both Box 508 files must be compared before
either row can be merged or receive shared evidence.

The final 23-person queue state is **20** `in_progress`, two
`needs_identity_review`, and one `conflicting_sources`. All **18** candidates
in the cohort have review decisions: five accepted, one conflicting, and 12
rejected. None remains unreviewed. This is research-attempt progress, not
completion of the minimum research protocol. No new employer or affiliation
claim was made.

Rebuilt coverage remains **23,978/23,978** linked source rows and **23,939**
active person entities. Research-attempt coverage is **7,855/23,939
(32.8126%)**; confirmed/high verified-employer coverage is **280/23,939
(1.1696%)**; confirmed/high verified-affiliation coverage is **628/23,939
(2.6233%)**; archival-review disposition coverage is **6,339/23,939
(26.4798%)**. There are **16,079** `not_started` people, **489** active
possible-duplicate groups, and **168** active people with conflicting identity
or source status. The database stores **13,028** attempts or plans and
**4,974** claims: **1,311** confirmed, **1,956** high, **1,377** medium,
**187** low, and **143** conflicting. It contains **5,074** source/citation
records and **2,389** unique document keys. The public projection contains
**2,224** affiliations, **708** organizations, **3,867** sources, and **4,783**
claims. The oil-company category remains a supported, incomplete evidence set
of seven people across nine companies. Full-index historical research is
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages481-490_2026-09-22.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-22_batch641.csv
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-22_batch641.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page311-mckee-mckiernan-review_batch-641_2026-09-22.json
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
