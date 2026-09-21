# Batch 620: PDF pages 271–280 and variant review

Original NARA PDF pages **271–280** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the extraction;
there were no corrections. Page 275 had already been audited as a parser-warning
page, so this replay advances the complete-page ledger by nine pages and **414**
rows. The visual-review ledger now covers **233/522 pages** and
**10,684/23,978 rows**: **10,655** reviewed rows match the extraction, **29**
retain earlier reviewed corrections, and **13,294** remain for complete visual
comparison.

The review preserves literal index anomalies instead of silently repairing
them. On page 275 row 29, the digits printed for Phillip Levy are visibly in
the rank column while the private-identifier column is blank. The extraction
therefore remains unchanged and the warning is resolved as a faithful
transcription.

Twenty-four possible-duplicate, spelling-variant, or private-identifier
conflict groups covering **49 active people** were reviewed. Forty-seven people
remain ambiguous with high archival priority. Stacey Lloyd and Kwong W Lo are
marked conflicting with critical priority because page 280 prints the same
private identifier beside materially different names. Same-identifier
spelling or name-expansion pairs—including Frank / Franklin Lindsay,
Litivinos / Litwinas, and Lochner / Lockner—remain separate pending direct
file review. Exact-name rows with different identifiers also remain separate.
Five earlier machine-generated identifier groups were replaced by reviewed,
non-identifying group labels; no private identifier appears in a committed
group label or public output.

The bounded, read-only Library of Congress discovery pass completed **46**
live searches across the two page-271 queues, producing **33** newspaper
candidates and no adapter errors. Context review rejected all 33 as unrelated
namesakes, wrong initials, commemorative references, postwar references, or
items whose metadata and unavailable OCR did not establish indexed identity or
pre-OSS employment. The 12 people with candidates returned to `in_progress`;
the discovery pass created nonplanned attempt coverage for **45** page-271
people. These searches do not constitute the completed multi-source protocol.
No authenticated NARA Catalog request was made and no raw LoC response was
retained.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,330/23,939 (30.6195%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,210/23,939 (25.9409%)**. There are
**16,609** `not_started` people, **469** active possible-duplicate groups, and
**143** active people with conflicting identity or source status. The database
stores **12,388** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection has **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Local release validation

Release validation is recorded in `reports/release_batch_620.md` after the
tracked-only candidate has passed the full test, build, accessibility, link,
redaction, and deterministic-build suite.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages271-280_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch620.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages271-280-duplicate-review_batch-620_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Recreate the exact 21 page queues idempotently with these commands:

```sh
python3 -m oss_research assign-page-batch --batch-name page-271-lee-lefferts-b620 --page 271 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-271-leffler-leick-b620 --page 271 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-272-leininger-lemire-b620 --page 272 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-272-lemke-lent-b620 --page 272 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-273-lent-leone-b620 --page 273 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-273-leone-leroy-b620 --page 273 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-274-leroy-lester-b620 --page 274 --first-row 1 --last-row 19
python3 -m oss_research assign-page-batch --batch-name page-274-lester-letellier-b620 --page 274 --first-row 21 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-274-letendre-levetine-b620 --page 274 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-275-levie-levy-b620 --page 275 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-275-levy-lewis-b620 --page 275 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-276-lewis-lewis-b620 --page 276 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-276-lewis-lichtenberger-b620 --page 276 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-277-lichtenberger-lightsey-b620 --page 277 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-277-lightstone-lindamood-b620 --page 277 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-278-lindbeck-lindsay-b620 --page 278 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-278-lindsay-linscott-b620 --page 278 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-279-linsenmann-lipton-b620 --page 279 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-279-lisandrelli-littlefield-b620 --page 279 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-280-littlefield-lloyd-b620 --page 280 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-280-lloyd-jones-lockwood-b620 --page 280 --first-row 24 --last-row 46
```

Jane Lester at page 274 row 20 retains the earlier `pilot-v1` assignment and
`occupation_only_found` terminal status, so Batch 620 deliberately does not
overwrite that queue ownership.

The page-271 LoC passes are already checkpointed. Continue with the first
unsearched queue, then rebuild all derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-272-leininger-lemire-b620 --max-queries 23 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
