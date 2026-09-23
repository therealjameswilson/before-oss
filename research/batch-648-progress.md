# Batch 648: pages 35-44 extraction audit and Meily-Melkonian research

All **460** printed rows on original NARA PDF pages 35-44 were compared with
the immutable extraction at 180 dpi. Page 43 received an independent 240 dpi
comparison because its dense names and column alignment warranted a second
look. Every row matches the current extraction. Complete-page visual review
now covers **468/522 pages** and **21,494/23,978 rows**: **21,462** reviewed
rows match the extraction, **32** retain reviewed corrections, and **2,484**
remain unaudited. Every PDF page remains represented, every parser warning is
resolved, and SQLite integrity and foreign-key checks pass.

The page-315 `John J. Meily` through `Michael Melkonian` queue contains **22
source rows and 21 cautious person entities**. The two Michael Melkonian rows
remain separate immutable source records linked to one duplicate-group entity.
Each person received four saved source-specific query plans and one saved
manual source-review outcome. Eleven official Army candidates received
explicit decisions: seven exact protected-identifier bridges were accepted
and four conflicts were retained. Patrick J. Melanson's printed identifier
maps to `WOOD WILLIAM G`; Kosta Melinkoff's points to Army `MELNIKOFF KOSTA`;
and both Michael Melkonian rows point to Army `MILKONIAN MICHAEL`. None of
those names is silently substituted.

The evidence bundle adds four published affiliations. Ib Jorgen Melchior's
chronology separates Radio City Music Hall, his last documented civilian
employer, from subsequent United States Army service as the best-supported
immediate institutional path into OSS. Leif Edvin Kristiansen Meland's
merchant-sea work aboard D/S Cate B remains an earlier documented pre-OSS
affiliation rather than an immediate or last-civilian claim because the
1940-1942 interval is unresolved. His service in the 99th Infantry Battalion
(Separate) is documented separately as the immediate military assignment from
which he was recruited into OSS. John J. Meily remains unresolved between a
career Foreign Service officer and that man's same-name Marine officer son;
neither candidate's employment feeds analytics. Michael Melehes's exact rare
name and grade are corroborated in a Detachment 101 document, but no pre-OSS
employer is invented.

The final queue state is **15** `in_progress`, four `conflicting_sources`, one
`documented_prewar_employer_found`, and one `verified_employer_found`.
Identity statuses are nine `high_confidence`, eight `unresolved`, and four
`conflicting`. The cohort adds **17** evidence claims: 13 high and four
conflicting. Full service numbers remain private.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **8,010/23,939 (33.4600%)**;
confirmed/high verified-employer coverage is **284/23,939 (1.1863%)**;
confirmed/high verified-affiliation coverage is **636/23,939 (2.6568%)**;
archival-review disposition coverage is **6,468/23,939 (27.0187%)**. There are
**15,924** `not_started` people, **492** possible-duplicate groups, and **179**
active conflicts. SQLite stores **13,454** attempts or plans and **5,064**
claims: 1,311 confirmed, 2,020 high, 1,392 medium, 187 low, and 154
conflicting. It contains **5,116** citation records and **2,421** unique source
documents. The public projection contains **2,348** affiliations, **718**
organizations, **3,909** sources, and **4,873** claims.

The oil-company category remains an evidence-scoped set of **seven people
across nine historically named companies**. No Batch 648 person was added
without documented oil-company employment. Full-index historical research is
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages35-44_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch648.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page315-meily-melkonian-review_batch-648_2026-09-23.json
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
No authenticated NARA Catalog request was made.
