# Batch 649: pages 45-54 extraction audit and Mellen-Mencoboni research

All **460** printed rows on original NARA PDF pages 45-54 were compared with
the immutable extraction at 180 dpi. Pages 46, 50, and 53 were already in the
deterministic or warning-page audit; the remaining **322** rows received their
first complete visual comparison in this batch. Every row matches. Complete-
page visual review now covers **475/522 pages** and **21,816/23,978 rows**:
**21,784** reviewed rows match the extraction, **32** retain reviewed
corrections, and **2,162** remain unaudited. Every PDF page remains represented,
every parser warning is resolved, and SQLite integrity and foreign-key checks
pass.

The page-315/316 `Constance L. Mellen` through `Daniel J. Mencoboni` queue
contains **22 source rows and 22 cautious person entities**. Each person
received four saved source-specific query plans and one saved manual review
outcome. Four source families were staged: NARA, CIA Reading Room, Library of
Congress, and targeted web research. The NARA, CIA, and web calls were dry-run
plans; the LoC adapter ran live in one bounded sequence. All six LoC newspaper
candidates were rejected after direct page-context inspection. No authenticated
NARA Catalog request was made and no API key was stored or logged.

Fourteen official Army identity candidates received explicit review decisions.
Ten exact normalized-name plus nonshared protected-identifier bridges were
accepted. August O. Melnar remains probable because the fixed-width Army name
field is corrupted. Oleg Melnikoff II remains probable because the Army record
spells the surname `Melnikof` and records Roman numeral `I`. Joseph V. Menanga
remains conflicting because the protected identifier appears with `Menengas`
in both the Army file and another index row. The records are not silently
merged. Full protected identifiers remain private.

Amos W. Melton is a high-confidence identity based on the exact uncommon name,
compatible officer context, and a Texas State Historical Association biography
that explicitly documents his 1944 OSS assignment. The evidence model keeps
two predecessor questions separate:

- the **Fort Worth Star-Telegram** is his last documented civilian employer
  before entering wartime service in June 1942; and
- the **United States Army Air Forces** is his immediate documented military
  assignment before transfer to OSS in 1944.

The November 6, 1945 Office of Price Administration directory entry for
Dolores J. Mencke was checked in the official GovInfo scan. It postdates OSS
dissolution and has no Box 517 identity bridge, so it remains a rejected
post-OSS lead rather than a pre-OSS affiliation. Prominent William L. Mellon
biographies, unrelated Charles J. Mellott and Milton Melnick obituaries, and
postwar Oleg Melnikoff and Daniel Mencoboni records were likewise not
transferred without the required identity and temporal bridges.

The final queue state is **18** `in_progress`, two
`needs_identity_review`, one `conflicting_sources`, and one
`verified_employer_found`. Identity statuses are 11 `high_confidence`, eight
`unresolved`, two `probable`, and one `conflicting`. The evidence bundle adds
**16** claims: 13 high, two medium, and one conflicting.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,032/23,939 (33.5519%)**;
confirmed/high verified-employer coverage is **285/23,939 (1.1905%)**;
confirmed/high verified-affiliation coverage is **637/23,939 (2.6609%)**;
archival-review disposition coverage is **6,490/23,939 (27.1106%)**. There are
**15,902** `not_started` people, **492** possible-duplicate groups, and **180**
active conflicts. SQLite stores **13,564** attempts or plans and **5,080**
claims: 1,311 confirmed, 2,033 high, 1,394 medium, 187 low, and 155 conflicting.
It contains **5,120** citation records and **2,424** unique source documents.
The public projection contains **2,243** affiliations, **720** organizations,
**3,912** sources, and **4,889** claims.

The oil-company category remains an evidence-scoped set of **seven people
across nine historically named companies**. Amos W. Melton is not included:
the Star-Telegram was a newspaper, not an oil employer. Full-index historical
research is unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages45-54_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch649.csv
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-23_batch649.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page315-316-mellen-mencoboni-review_batch-649_2026-09-23.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Continue with the next bounded research and extraction-audit batch, then run:

```sh
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw Catalog API response, copyrighted page
image, or private reviewer note is committed or included in the public site.
