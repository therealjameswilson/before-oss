# Batch 647: pages 18-34 extraction audit and Meegan-Meigs research

All **460** printed rows on original NARA PDF pages 18, 19, 22, 23, 26,
27, 29, 30, 31, and 34 were compared with the immutable extraction at 180
dpi. Every row matches the current extraction. Complete-page visual review now
covers **458/522 pages** and **21,034/23,978 rows**: **21,002** reviewed rows
match the extraction, **32** retain reviewed corrections, and **2,944** remain
unaudited. Every PDF page remains represented, every parser warning is
resolved, and SQLite integrity and foreign-key checks pass.

The page-315 `Jospeh Meegan` through `Richard L. Meigs` queue contains **22
source rows and 22 cautious person entities**. Each person received four
saved source-specific query plans and one saved manual source-review outcome.
Nine preexisting official Army candidates received explicit decisions: seven
accepted high-confidence identity bridges and two retained conflicts. William
G. Mehillos does not silently become `MEHILOS`, and Eugene W. Mehner does not
silently become `MOHNER`; both require personnel-file review.

The evidence bundle adds five published affiliations. Leonard C. Meeker's
chronology separates the Treasury General Counsel's Office, the Office of the
Solicitor General as his last documented civilian pre-service assignment, and
the Army as his probable immediate institutional path into OSS. Gaudens
Megaro's chronology separates Queens College employment from the Coordinator
of Information, the documented immediate predecessor organization to his OSS
service. Lincoln Mei remains only a probable identity match; the 1949 Senate
report supports his Army chronology, not a pre-OSS employer. Commercial
people-finder pages, genealogy leads, modern namesakes, search-result snippets,
and postwar employment were not promoted to claims.

The final queue state is **17** `in_progress`, two
`verified_employer_found`, two `conflicting_sources`, and one
`needs_identity_review`. Identity statuses are ten `unresolved`, nine
`high_confidence`, two `conflicting`, and one `probable`. The cohort adds
**17** evidence claims: 14 high, one medium, and two conflicting. Full service
numbers remain private.

Rebuilt coverage is **23,978/23,978** linked source rows and **23,939** active
person entities. Research-attempt coverage is **7,989/23,939 (33.3723%)**;
confirmed/high verified-employer coverage is **282/23,939 (1.1780%)**;
confirmed/high verified-affiliation coverage is **634/23,939 (2.6484%)**;
archival-review disposition coverage is **6,447/23,939 (26.9309%)**. There are
**15,945** `not_started` people, **492** possible-duplicate groups, and **175**
active conflicts. SQLite stores **13,349** attempts or plans and **5,047**
claims: 1,311 confirmed, 2,007 high, 1,392 medium, 187 low, and 150
conflicting. It contains **5,101** citation records and **2,409** unique source
documents. The public projection contains **2,237** affiliations, **714**
organizations, **3,894** sources, and **4,856** claims.

The oil-company category remains an evidence-scoped set of **seven people
across nine historically named companies**. No Batch 647 person was added
without documented oil-company employment. Full-index historical research is
unfinished.

## Replay and continuation

After importing prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages18-34_sparse_2026-09-23.json
python3 -m oss_research import-review-decisions research/identity_review_decisions_2026-09-23_batch647.csv
python3 -m oss_research import-reviewed-evidence research/evidence-page315-meegan-meigs-review_batch-647_2026-09-23.json
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
