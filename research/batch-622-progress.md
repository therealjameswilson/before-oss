# Batch 622: PDF pages 291-300 and variant review

Original NARA PDF pages **291-300** were rendered at 180 dpi. All **460**
printed rows were compared against the immutable SQLite extraction for row
order, indexed spelling, initials, rank, private-identifier column occupancy,
box, notes, and archival location. All ten complete pages match the current
extraction. Pages 292 and 293 had already been audited as parser-warning pages,
so this replay adds eight pages and **368** rows to the complete-page ledger.
Visual review now covers **250/522 pages** and **11,466/23,978 rows**:
**11,434** reviewed rows match the extraction, **32** retain reviewed
corrections, and **12,512** remain for complete visual comparison.

The review preserves literal index anomalies rather than silently repairing
them. Examples include the scientific-notation-looking Malloy text on page
291; numeric text printed in the rank column on pages 292 and 293; the starred
Manthos entry without a first name; Manaloe / Manoloe, Manierre / Manniere,
Marnocaa / Marnocha, and Mathews / Matthews spellings; duplicated Maratzo and
Marchigiani source rows; clipped `Raymond-Jea`, `Also Mat`, and `Norwegi`
notes; mixed-case and unfamiliar grades; `Rigiberto`, `Sr.`; `Williiam`; the
literal uncertain digit in Steve Mastros's identifier; and the Mattox row whose
printed first-name and middle-name columns read `F` and `Anna`.

Twenty-two bounded queues were assigned for **456** previously unowned people.
Carl D Marshall at page 296 row 27 and John B Martin at page 297 row 42 retain
their earlier `pilot-v1` ownership and statuses, so Batch 622 deliberately does
not overwrite those research checkpoints. The ten pages contain **458** active
person entities because two pairs of exact duplicate source rows already link
to single high-confidence people.

The two page-291 Library of Congress passes completed **46** live searches,
producing **25** newspaper candidates across eight people with zero adapter
errors. Every candidate was inspected in official item-level OCR context. They
were rejected as mismatched initials or names, unrelated surname occurrences,
tennis-only references, spouse material, postwar material, or OCR without a
usable exact-name context. All eight affected people remain `in_progress` for
later official, CIA, institutional, directory, biographical, and archival
stages. No employer claim was added, no raw LoC response was retained, and no
authenticated NARA request was made.

Eleven possible-duplicate, spelling-variant, exact-repeat, or
private-identifier conflict groups covering **24 people** were reviewed. Two
exact duplicate source-row pairs remain linked to high-confidence person
entities. Thirteen people remain `ambiguous`; eight carry `conflicting` status;
one previously confirmed person retains that identity status while the newly
documented index-identifier conflict stays visible. The reviewed groups cover
Manaloe / Manoloe; Manierre / Manniere and its displaced number; duplicated
Maratzo and Marchigiani rows; March / Marck; three unrelated names sharing an
identifier across pages 27, 149, and 294; Glasbrenner / Mantho; Manual / Monroe;
Marnocaa / Marnocha; three Marritts / Meritts / Merritts forms; and the Eugene
K Mathews / Matthews cluster plus its unrelated St. Laurent identifier
conflict. No uncertain entities were merged, and public group labels remain
non-identifying.

The page-review importer is now monotonic: replaying a complete-page match can
no longer downgrade a prior `reviewed_after_correction` page or
`reviewed_corrected` row. A regression test covers that behavior. Older page
bundles were also cleaned so their matching-page lists no longer overlap any
row-correction page; the repository-wide overlap audit returns an empty set.

At this checkpoint, **23,978/23,978** printed rows link to **23,939** active
person entities. Research-attempt coverage is **7,422/23,939 (31.0038%)**;
confirmed/high verified-employer coverage is **280/23,939 (1.1696%)**;
confirmed/high verified-affiliation coverage is **628/23,939 (2.6233%)**;
archival-review disposition coverage is **6,258/23,939 (26.1414%)**. There are
**16,517** `not_started` people, **477** active possible-duplicate groups, and
**154** active people with conflicting identity or source status. The database
stores **12,480** attempts or plans and **4,900** claims: **1,311** confirmed,
**1,898** high, **1,374** medium, **185** low, and **132** conflicting. It
contains **5,045** source/citation records and **2,372** unique document keys.
The public projection remains **2,224** affiliations, **708** organizations,
**3,842** sources, and **4,711** claims. The oil-company category remains a
supported, incomplete evidence set of **seven** people across nine companies.
Full-index historical research is unfinished.

## Replay and continuation

After importing the prior durable batches into private SQLite:

```sh
python3 -m oss_research import-page-reviews research/parser_visual_review_pages291-300_2026-09-21.json
python3 -m oss_research import-review-decisions research/loc_review_decisions_2026-09-21_batch622.csv
python3 -m oss_research import-reviewed-evidence research/evidence-pages291-300-duplicate-review_batch-622_2026-09-21.json
python3 -m oss_research import-adapter-checkpoints research/adapter_attempt_checkpoints.json
```

Recreate the exact 22 page queues idempotently with these commands:

```sh
python3 -m oss_research assign-page-batch --batch-name page-291-maiza-malia-b622 --page 291 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-291-malick-malone-b622 --page 291 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-292-maloof-maness-b622 --page 292 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-292-maney-mann-b622 --page 292 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-293-mann-manson-b622 --page 293 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-293-mantho-mar-b622 --page 293 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-294-marah-marciari-b622 --page 294 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-294-marck-margolyes-b622 --page 294 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-295-margulas-markette-b622 --page 295 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-295-markham-marnocaa-b622 --page 295 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-296-marnocha-marsh-b622 --page 296 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-296-marsh-marshall-b622 --page 296 --first-row 24 --last-row 26
python3 -m oss_research assign-page-batch --batch-name page-296-marshall-marszalek-b622 --page 296 --first-row 28 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-297-martaus-martin-b622 --page 297 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-297-martin-martin-a-b622 --page 297 --first-row 24 --last-row 41
python3 -m oss_research assign-page-batch --batch-name page-297-martin-martin-b-b622 --page 297 --first-row 43 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-298-martin-martinez-b622 --page 298 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-298-martinez-masiokas-b622 --page 298 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-299-maslikosa-masterson-b622 --page 299 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-299-masterson-mathewson-b622 --page 299 --first-row 24 --last-row 46
python3 -m oss_research assign-page-batch --batch-name page-300-mathiakes-mattera-b622 --page 300 --first-row 1 --last-row 23
python3 -m oss_research assign-page-batch --batch-name page-300-matthai-matuszek-b622 --page 300 --first-row 24 --last-row 46
```

The page-291 LoC passes and decisions are already checkpointed. Continue with
the first unsearched queue, then rebuild all derived outputs:

```sh
python3 -m oss_research research --source loc --batch page-292-maloof-maness-b622 --max-queries 23 --resume
python3 -m oss_research export-adapter-checkpoints
python3 -m oss_research export-derived
python3 -m oss_research build-public-data
python3 -m oss_research coverage-report
```

No API key, full service number, raw API response, or private reviewer note is
committed or included in the public site.
